# ОПИСАНИЕ МАТЕРИАЛОВ, НЕОБХОДИМЫХ ДЛЯ РАБОТЫ МОДА

init python:
    from random import randint

    class DSSkill:
        def __init__(self, id, name, descr, type_bonus_fn=None, member_bonus=[('', 0)], damage_bonus=None):
            self.id = id
            self.name = name
            self.descr = descr
            self.xp = 0
            self.level = 0
            self.type_bonus_fn = type_bonus_fn
            self.member_bonus = member_bonus
            self.damage_bonus = damage_bonus
            self.check_results = []
        
        def get_type_bonus(self):
            global ds_semtype
            if self.type_bonus_fn is None:
                return 0
            return self.type_bonus_fn(ds_semtype, self.id)

        def get_member_bonus(self):
            global ds_member
            result = 0
            for member, bonus in self.member_bonus:
                if ds_member[member]:
                    result += bonus
            return result

        def get_damage_bonus(self):
            if self.damage_bonus is None:
                return 0
            return eval(self.damage_bonus).diff()

        def get_total(self):
            return self.level + self.get_type_bonus() + self.get_member_bonus() + self.get_damage_bonus()

        def set_level(self, level):
            self.level = level
            self.xp = 0

        def up(self, points):
            global ds_callbacks
            self.xp += points
            while self.xp >= 100:
                self.level += 1
                self.xp -= 100
                for callback in ds_callbacks:
                    callback(self.name, self.level)
        
        def check(self, threshold, passive=False, modifiers=[]):
            dices = [1, 2, 3, 4, 5, 6]
            first_dice = renpy.random.choice(dices)
            second_dice = renpy.random.choice(dices)
            points = self.get_total()
            applied_modifiers = []
            for variable, bonus, label in modifiers:
                if eval(variable):
                    points += bonus
                    applied_modifiers.append((variable, bonus, label))
            result = DSSkillcheckRes(self.id, self.get_total(), int(threshold), not passive, dices, applied_modifiers)
            self.check_results.append(result)
            global ds_callbacks
            for callback in ds_callbacks['check']:
                callback(result)
            return result

    class DSSkillcheckRes:
        def __init__(self, skill, level, threshold, check_type, dices, modifiers):
            self.skill = skill
            self.level = level
            self.threshold = threshold
            self.is_active = check_type
            self.dices = dices
            self.applied_modifiers = modifiers
        
        def __bool__(self):
            return self.result()

        def __repr__(self):
            return str(threshold) + ':' + ('success' if self.result() else 'failure')
        
        def total_points(self):
            points = self.level + self.dices[0] + self.dices[1]
            for modifier in self.applied_modifiers:
                points += modifier[1]
            return points

        def result(self, invoke_callbacks=True):
            is_success = (self.dices != (1, 1)) and ((self.dices == (6, 6)) or (self.total_points() >= self.threshold))
            global ds_callbacks
            if invoke_callbacks:
                for callback in ds_callbacks['get_result']:
                    callback(self, is_success)
            return is_success
    
    def ds_type_bonus(semtype, skill):
        if skill in ['authority', 'composure']:
            if semtype >= 3:
                return 1
            elif semtype <= -3:
                return -1
            else:
                return 0
        elif skill in ['empathy']:
            if semtype <= -3:
                return 1
            elif semtype >= 3:
                return -1
            else:
                return 0
        return 0

    def ds_show_check(result, is_success):
        if result.is_active:
            # renpy.show('roll')
            if is_success:
                renpy.play(ds_check_success, channel='sound')
            else:
                renpy.play(ds_check_failure, channel='sound')
            renpy.pause(delay=1.0, hard=True)
            # renpy.hide('roll')
            if is_success:
                renpy.show('check success')
            else:
                renpy.show('check failure')
            renpy.show("first_dice dice" + str(result.dices[0]))
            renpy.show("second_dice dice" + str(result.dices[1]))
            renpy.pause(delay=1.0)
            renpy.hide('check')
            renpy.hide('first_dice')
            renpy.hide('second_dice')
    
    def ds_up_skill(result):
        global ds_skill_list
        ds_skill_list[result.skill].up(ds_max(result.threshold - result.total_points(), 0))
    
    def ds_save_last(result):
        global ds_last_skillcheck
        ds_last_skillcheck = result
    
    class DSLifeParameter:
        def __init__(self, skill, callbacks):
            self.diff_level = 0
            self.skill = skill
            self.callbacks = callbacks
        
        def level(self):
            global ds_skill_list
            return ds_skill_list[skill].get_total()
        
        def diff(self):
            return self.diff_level
        
        def damage(self):
            self.diff_level -= 1
            for callback in self.callbacks['damage']:
                callback(self.level())
        
        def up(self):
            self.diff_level += 1
            for callback in self.callbacks['up']:
                callback(self.level())
        
        def restore(self):
            self.diff_level = 0
            for callback in self.callbacks['restore']:
                callback()

        def reset(self):
            self.diff_level = 0
    
    def ds_show_damage_health(*args, **kwargs):
        renpy.show('health damage', at_list=[show_damage])
        renpy.pause(1.5)
        renpy.hide('health')
    
    def ds_show_damage_morale(*args, **kwargs):
        renpy.show('morale damage', at_list=[show_damage])
        renpy.pause(1.5)
        renpy.hide('morale')
    
    def ds_die_zero_health(level, *args, **kwargs):
        if level <= 0:
            ui.jumps('ds_end_out_of_health')
    
    def ds_die_zero_morale(level, *args, **kwargs):
        if level <= 0:
            ui.jumps('ds_end_out_of_morale')
    
    def ds_show_up_health(*args, **kwargs):
        renpy.show('health up')
        renpy.with_statement(wiperight)
        renpy.pause(1.5)
        renpy.hide('health')
        renpy.with_statement(wiperight)
    
    def ds_show_up_morale(*args, **kwargs):
        renpy.show('morale up')
        renpy.with_statement(wiperight)
        renpy.pause(1.5)
        renpy.hide('morale')
        renpy.with_statement(wiperight)
    
    def ds_show_restore_health(*args, **kwargs):
        renpy.show('health restore')
        renpy.with_statement(wiperight)
        renpy.pause(1.5)
        renpy.hide('health')
        renpy.with_statement(wiperight)
    
    def ds_show_restore_morale(*args, **kwargs):
        renpy.show('morale restore')
        renpy.with_statement(wiperight)
        renpy.pause(1.5)
        renpy.hide('morale')
        renpy.with_statement(wiperight)

    def ds_get_maximal_girl():
        res = None
        max_lp = 0
        if ds_lp_dv > max_lp:
            res = 'dv'
            max_lp = ds_lp_dv
        if ds_lp_un > max_lp:
            res = 'un'
            max_lp = ds_lp_un
        if ds_lp_sl > max_lp:
            res = 'sl'
            max_lp = ds_lp_sl
        if ds_lp_us > max_lp:
            res = 'us'
            max_lp = ds_lp_us
        if ds_lp_mi > max_lp:
            res = 'mi'
            max_lp = ds_lp_mi
        return res

    class DSSprite(python_object):
        def __init__(self, id, emotions, outfits=[], acc=[], dist=[], naked=['naked'], overrides={}):
            """
            :param str id: ИД персонажа (должен соответствовать каталогу, где лежат спрайты)
            :emotions list[list[str]]: Двумерный список с набором атрибутов. Из этого списка будет составлена карта для определения номера позы
            :outfits list[str]: Список доступных нарядов (кортеж из названия позы и названия одежды, None означает пропуск соответстующего слоя при генерации одежды)
            :acc list[str]: Cписок доступных аксессуаров
            :dist list[str]: Список доступных расстояний
            :overrides dict[tuple[str, str, str], tuple[str, str, str, str]]: Список особых названий файлов при определённой комбинации эмоции-одежды-аксессуара в виде «тело-эмоция-одежда-аксессуар» (None в индексе означает «любой», в значении - «сохранить»)
            """
            self.template = 'mods/disco_sovenok/sprite/{dist}/'+id+'/'+id+'_{body}_{image}.png'
            self.emotion_to_body_index = {
                emotion: i for i, emotion_layer in enumerate(emotions) for emotion in emotion_layer
            }
            self.outfits = set(outfits)
            self.acc = set(acc)
            self.dist = set(dist)
            self.naked = set(naked)
            self.overrides = overrides
        
        def _duplicate(self, args):
            emotion, body_index = None, 0
            body, outfit, dist = 'body', None, 'normal'
            acc_tmp = []
            acc = []
            for attr in args.args:
                # Если атрибут эмоция, то находим индекс позы и запоминаем эмоцию
                if attr in self.emotion_to_body_index:
                    emotion = attr
                    body_index = self.emotion_to_body_index[emotion]
                # Запоминаем наряд
                elif attr in self.outfits and attr not in self.naked:
                    outfit = attr
                elif attr in self.acc:
                    acc_tmp.append(attr)
                elif attr in self.dist:
                    dist = dist
            
            def get_override(body, emotion, outfit, acc):
                new_body, new_emotion, new_outfit, new_acc = body, None, None, None
                combinations = [
                    (emotion, outfit, acc),
                    (None, outfit, acc),
                    (emotion, None, acc),
                    (emotion, outfit, None),
                    (None, None, acc),
                    (None, outfit, None),
                    (emotion, None, None),
                    (None, None, None)
                ]
                for comb in combinations:
                    if comb in self.overrides:
                        new_body, new_emotion, new_outfit, new_acc = self.overrides[comb]
                        break
                if new_body is None:
                    new_body = 'body'
                if new_emotion is None:
                    new_emotion = emotion
                if new_outfit is None:
                    new_outfit = outfit
                if new_acc is None:
                    new_acc = acc
                return (new_body, new_emotion, new_outfit, new_acc)

            images = []
            
            def format(image, dist):
                return self.template.format(image=image, body=body_index + 1, dist=dist)
            
            def add(image, dist):
                if image is None:
                    return
                images.append(format(image, dist))
            
            for a in acc_tmp:
                body, emotion, outfit, a = get_override(body, emotion, outfit, a)
                acc.append(a)

            add(body, dist)
            if outfit:
                add(outfit, dist)
            if not emotion:
                raise Exception('No emotion provided for sprite.')
            add(emotion, dist)
            for a in acc:
                add(a, dist)

            return Fixed(*images, xfit=True, yfit=True)

        def _choose_attributes(self, tag, required, optional):
            optional = list(optional) if optional else []

            outfit = None
            emotion = None
            acc = []
            dist = 'normal'
            conflicts = set()
            for attr in required:
                if attr in self.emotion_to_body_index:
                    # Если эмоция уже определена, то значит у нас конфликт атрибутов
                    if emotion:
                        conflicts.add(emotion)
                        conflicts.add(attr)
                    emotion = attr
                elif attr in self.outfits:
                    # Если наряд уже определён, то значит у нас конфликт атрибутов
                    if outfit:
                        conflicts.add(outfit)
                        conflicts.add(attr)
                    outfit = attr
                # аксессуары могут сочетаться
                elif attr in self.acc:
                    acc.append(attr)
                elif attr in self.dist:
                    # Если дистанция уже определена как не normal, то у нас конфликт атрибутов
                    if dist != 'normal':
                        conflicts.add(dist)
                        conflicts.add(attr)

            if conflicts:
                raise Exception('Attribute conflict: %s' % conflicts)
            
            # Выкидываем уже существующие атрибуты, если они конфликтуют с новыми
            if emotion:
                optional = [attr for attr in optional if attr not in self.emotion_to_body_index]
            if outfit:
                optional = [attr for attr in optional if attr not in self.outfits]
            if dist:
                optional = [attr for attr in optional if attr not in self.dist]
            
            return tuple(required) + tuple(optional)
    
    class DSScene:
        def __init__(self, name, filename, tag, hent=False):
            self.name = name
            self.filename = filename
            self.tag = tag
            self.hent = hent
        
        def is_seen():
            return renpy.seen_image(tag + ' ' + name)

    class DSSceneManager(python_object):
        def __init__(self, tag):
            self.tag = tag
            self.imgs = []
            self.cl = {}
        
        def register(self, name, filename, hent=False):
            self.imgs.append({name: DSScene(name, filename, self.tag, hent)})
            self.cl[name] = len(self.imgs) - 1
        
        def register(self, imglist, hent=False):
            to_add = {}
            for img in imglist:
                to_add[img] = DSScene(img, imglist[img], self.tag, hent)
                self.cl[img] = len(self.imgs)
            self.imgs.append(to_add)
        
        def get_info(self, name):
            return self.imgs[self.cl[name]][name]

        def _duplicate(self, args):
            img_to_show = None
            for arg in args.args:
                img_to_show = self.get_info(arg)
            if img_to_show is None:
                raise Exception('no scene defined')
            return Fixed(img_to_show.filename, xfit=True, yfit=True)

        def _choose_attributes(self, tag, required, optional):
            return tuple(optional)

        def __len__(self):
            return len(self.cl)

        def __getitem__(self, key):
            return self.imgs[self.cl[key]][key]

        def __iter__(self):
            return iter(self.imgs)

        def __contains__(self, item):
            return item in self.cl

        def __delitem__(self, key):
            del self.imgs[self.cl[key]][key]
            del self.cl[key]
        
        def __iadd__(self, item):
            self.register(item[0], item[1], item[2])
        
    def ds_define_sprite(char, emo, dist='normal', body_num=1, cloth=None, acc=None, acc2=None, body_name='body'):
        if cloth and acc:
            return ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+cloth+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+acc+".png"), im.matrix.tint(0.94, 0.82, 1.0) ), "persistent.sprite_time=='night'",im.MatrixColor(im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+cloth+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+acc+".png"), im.matrix.tint(0.63, 0.78, 0.82) ), True, im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+cloth+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+acc+".png") )
        if cloth:
            return ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+cloth+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png"), im.matrix.tint(0.94, 0.82, 1.0) ), "persistent.sprite_time=='night'",im.MatrixColor(im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+cloth+".png"), im.matrix.tint(0.63, 0.78, 0.82) ), True, im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+cloth+".png") )
        if acc:
            return ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+acc+".png"), im.matrix.tint(0.94, 0.82, 1.0) ), "persistent.sprite_time=='night'",im.MatrixColor(im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+acc+".png"), im.matrix.tint(0.63, 0.78, 0.82) ), True, im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+acc+".png") )
        return ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png"), im.matrix.tint(0.94, 0.82, 1.0) ), "persistent.sprite_time=='night'",im.MatrixColor(im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png"), im.matrix.tint(0.63, 0.78, 0.82) ), True, im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png") )

    def ds_define_chars():
        global ds_char_table
        for char in ds_char_table:
            for dist in ds_char_table[char]:
                for emo in ds_char_table[char][dist]['emo']:
                    body_num = ds_char_table[char][dist]['emo'][emo]
                    for cloth in ds_char_table[char][dist]['cloth']:
                        cloth_file = ds_char_table[char][dist]['cloth'][cloth]
                        if dist == 'normal':
                            renpy.image('[char] [emo] [cloth]', ds_define_sprite(char, emo, body_num=body_num, cloth=cloth_file))
                        else:
                            renpy.image('[char] [emo] [cloth] [dist]', ds_define_sprite(char, emo, dist=dist, body_num=body_num, cloth=cloth_file))
                        for acc in ds_char_table[char][dist]['acc']:
                            acc_file = ds_char_table[char][dist]['acc'][acc]
                            if dist == 'normal':
                                renpy.image('[char] [emo] [acc] [cloth]', ds_define_sprite(char, emo, body_num=body_num, cloth=cloth_file, acc=acc_file))
                            else:
                                renpy.image('[char] [emo] [acc] [cloth] [dist]', ds_define_sprite(char, emo, dist=dist, body_num=body_num, cloth=cloth_file, acc=acc_file))

    # Класс, реализующий фонарик (для хождения по шахтам)
    class DSFlashlight(renpy.Displayable):
        def __init__(self, child, mask, curtain="#000", **kwargs):
            super(DSFlashlight, self).__init__(**kwargs)

            self.events = True

            self.child = renpy.displayable(child)
            self.mask = renpy.displayable(mask)
            self.curtain = renpy.displayable(curtain)

            self.xpos, self.ypos = renpy.get_mouse_pos()

        def render(self, width, height, st, at):

            scene = renpy.render(self.child, width, height, st, at)
            curtain = renpy.render(self.curtain, width, height, st, at)

            mask = renpy.render(self.mask, width, height, st, at)
            mask_width, mask_height = mask.get_size()

            light = renpy.Render(width, height, opaque=False)

            light.place(self.mask, self.xpos - (mask_width / 2.0), self.ypos - (mask_height / 2.0))

            rv = renpy.Render(width, height, opaque=False)

            rv.operation = renpy.display.render.IMAGEDISSOLVE
            rv.operation_alpha = True
            rv.operation_complete = 256.0 / (256.0 + 256.0)
            rv.operation_parameter = 256

            if renpy.display.render.models:
                rv.mesh = True
                rv.add_shader("renpy.imagedissolve",)
                rv.add_uniform("u_renpy_dissolve_offset", 0)
                rv.add_uniform("u_renpy_dissolve_multiplier", 1.0)
                rv.add_property("mipmap", renpy.config.mipmap_dissolves if (self.style.mipmap is None) else self.style.mipmap)

            rv.blit(light, (0, 0), focus=False, main=False)
            rv.blit(curtain, (0, 0), focus=False, main=False)
            rv.blit(scene, (0, 0), focus=True, main=True)

            return rv

        def event(self, ev, x, y, st):

            if self.events and ev.type == pygame.MOUSEMOTION:
                self.xpos, self.ypos = renpy.get_mouse_pos()
                renpy.redraw(self, 0)

                return self.child.event(ev, x, y, st)
            else:
                return None

        def visit(self):
            return [self.child, self.mask, self.curtain]
    
    def ds_reset_achievements():
        for ach in persistent.ds_achievements:
            persistent.ds_achievements[ach] = False
    
    def ds_set_all_achievements():
        for ach in persistent.ds_achievements:
            persistent.ds_achievements[ach] = True

init:
    define SKILL_NAMES = {
        'logic': u"Логика",
        'encyclopedia': u"Энциклопедия",
        'rhetoric': u"Риторика",
        'drama': u"Драма",
        'conceptualization': u"Концептуализация",
        'visual_calculus': u"Визуальный анализ",
        'volition': u"Cила воли",
        'inland_empire': u"Внутренняя империя",
        'authority': u"Авторитет",
        'empathy': u"Эмпатия",
        'esprit': u"Командная волна",
        'suggestion': u"Внушение",
        'endurance': u"Cтойкость",
        'pain_threshold': u"Болевой порог",
        'physical_instrument': u"Грубая сила",
        'instinct': u"Инстинкт",
        'shivers': u"Трепет",
        'half_light': u"Сумрак",
        'perception': u"Восприятие",
        'coordination': u"Координация",
        'reaction_speed': u"Скорость реакции",
        'savoir_faire': u"Эквилибристика",
        'interfacing': u"Техника",
        'composure': u"Самообладание",
    }

    define SKILL_DESCR = {
        'logic': 'Управляй интеллектуальной стихией. Разложи мир по полочкам.\n\nОтлично подойдёт аналитикам, чистым рационалистам и, конечно, тем, кто дружит с логикой.',
        'encyclopedia': 'Задействуй все свои знания. Удивляй эрудицией.\n\nОтлично подойдёт любителям пораскинуть мозгами, историкам, помешанным на интересных фактах',
        'rhetoric': 'Совершенствуй искусство убеждения. Наслаждайся ожесточёнными интеллектуальными баталиями.\n\nОтлично подойдёт идеологам, умелым собеседникам, диванным экспертам.',
        'drama': 'Переиграй всех. Ври, но не дай обмануть себя.\n\nОтлично подойдёт тайным агентам, театральным актёрам, психопатам.',
        'conceptualization': 'Стань ценителем творчества. Развей чуткость к искусству.\n\nОтлично подойдёт творческим натурам, любителям психоделики, критикам.',
        'visual_calculus': 'Восстанавливай события. Заставь законы природы работать на тебя.\n\nОтлично подойдёт учёным, боевым тактикам, людям с математическим складом ума.',
        'volition': 'Держи себя в руках. Сохраняй боевой дух.\n\nОтлично подойдёт тем, кто дружит с головой, уравновешенным, тем, кто не склонен к самоубийствам.',
        'inland_empire': 'Интуиция и чутьё. Сны наяву.\n\nОтлично подойдёт мечтателям, охотникам за паранатуральными явлениями, воображенцам.',
        'authority': 'Подавляй и властвуй. Заяви о себе.\n\nОтлично подойдёт лидерам, мастерам психологической войны, жаждующим уважения.',
        'empathy': 'Чувствуй других. Задействуй зеркальные нейроны.\n\nОтлично подойдёт тонким психологам, интервьюверам, людям с широкой душой.',
        'esprit': 'Работай в команде. Будь единым целым с другими.\n\nОтлично подходит любителям подвижных игр, общественным деятелям, экстравертам.',
        'suggestion': 'Очаровывай мужчин и женщин. Ты — их кукловод.\n\nОтлично подойдёт дипломатам, обаяшкам, социопатам.',
        'endurance': 'Держи удар. Не дай себя прикончить.\n\nОтлично подойдёт тем, кто способен держать удар, неусыпным наблюдателям, вечным двигателям.',
        'pain_threshold': 'Разве это боль? Придумайте что-нибудь пожёстче.\n\nОтлично подойдёт непобедимым бойцам, тем, кто всё никак не сдохнет, мазохистам.',
        'physical_instrument': 'Играй мышцами. Наслаждайся своим здоровьем.\n\nОтлично подойдёт мощным мужикам, любителям помахать кулаками, спортсменам.',
        'instinct': 'Не бойся своих желаний. Демонстрируй своё либидо.\n\nОтлично подойдёт любителям секса, помешанным на сексе, пошлякам.',
        'shivers': 'Почувствуй дрожь. Настройся на волну «Совёнка».\n\nОтлично подойдёт любителям лагерной жизни, народным мудрецам, по-настоящему сверхъестественным натурам.',
        'half_light': 'Доверься своему телу. Запугивай людей.\n\nОтлично подойдёт нервным, тем, кто сначала нападают, а потом задают вопросы, тем, кто ненавидит сюрпризы.',
        'perception': 'Смотри, слушай, нюхай, вкушай и осязай. Не упусти не единой детали.\n\nОтлично подойдёт въедливым, чувственным личностям, сборщикам хлама.',
        'coordination': 'Целься! Огонь!\n\nОтлично подойдёт метателям мячей, снайперам, жонглёрам.',
        'reaction_speed': 'Будь быстрым, а не мёртвым.\n\nОтлично подойдёт тем, в кого хрен попадёшь, импровизаторам, любителям пинбола.',
        'savoir_faire': 'Скользи как тень. Поражай великолепием.\n\nОтлично подойдёт акробатам, ворам, невыносимым хвастунам.',
        'interfacing': 'Управляй механизмами. Вскрывай замки и обчищай карманы.\n\nОтлично подойдёт швецам, жнецам, на дуде игрецам.',
        'composure': 'Выпрями спину. Сохраняй покерфейс.\n\nОтлично подойдёт картёжникам, военным фетишистам, крутым перцам.'
    }       

    default ds_skill_list = {
        'logic': DSSkill('logic', SKILL_NAMES['logic'], SKILL_DESCR['logic'], member_bonus=[('library', 1)]),
        'encyclopedia': DSSkill('encyclopedia', SKILL_NAMES['encyclopedia'], SKILL_DESCR['encyclopedia'], member_bonus=[('library', 1)]),
        'rhetoric': DSSkill('rhetoric', SKILL_NAMES['rhetoric'], SKILL_DESCR['rhetoric'], member_bonus=[('library', 1)]),
        'drama': DSSkill('drama', SKILL_NAMES['drama'], SKILL_DESCR['drama'], member_bonus=[('library', 1)]),
        'conceptualization': DSSkill('conceptualization', SKILL_NAMES['conceptualization'], SKILL_DESCR['conceptualization'], member_bonus=[('library', 1)]),
        'visual_calculus': DSSkill('visual_calculus', SKILL_NAMES['visual_calculus'], SKILL_DESCR['visual_calculus'], member_bonus=[('library', 1)]),

        'volition': DSSkill('volition', SKILL_NAMES['volition'], SKILL_DESCR['volition'], member_bonus=[('music', 1)], damage_bonus='ds_morale'),
        'inland_empire': DSSkill('inland_empire', SKILL_NAMES['inland_empire'], SKILL_DESCR['inland_empire'], member_bonus=[('music', 1)]),
        'authority': DSSkill('authority', SKILL_NAMES['authority'], SKILL_DESCR['authority'], member_bonus=[('music', 1)]),
        'empathy': DSSkill('empathy', SKILL_NAMES['empathy'], SKILL_DESCR['empathy'], member_bonus=[('music', 1)]),
        'esprit': DSSkill('esprit', SKILL_NAMES['esprit'], SKILL_DESCR['esprit'], member_bonus=[('music', 1)]),
        'suggestion': DSSkill('suggestion', SKILL_NAMES['suggestion'], SKILL_DESCR['suggestion'], member_bonus=[('music', 1)]),

        'endurance': DSSkill('endurance', SKILL_NAMES['endurance'], SKILL_DESCR['endurance'], member_bonus=[('sport', 1)], damage_bonus='ds_morale'),
        'pain_threshold': DSSkill('pain_threshold', SKILL_NAMES['pain_threshold'], SKILL_DESCR['pain_threshold'], member_bonus=[('sport', 1)]),
        'physical_instrument': DSSkill('physical_instrument', SKILL_NAMES['physical_instrument'], SKILL_DESCR['physical_instrument'], member_bonus=[('sport', 1)]),
        'instinct': DSSkill('instinct', SKILL_NAMES['instinct'], SKILL_DESCR['instinct'], member_bonus=[('sport', 1)]),
        'shivers': DSSkill('shivers', SKILL_NAMES['shivers'], SKILL_DESCR['shivers'], member_bonus=[('sport', 1)]),
        'half_light': DSSkill('half_light', SKILL_NAMES['half_light'], SKILL_DESCR['half_light'], member_bonus=[('sport', 1)]),

        'perception': DSSkill('perception', SKILL_NAMES['perception'], SKILL_DESCR['perception'], member_bonus=[('cyber', 1)]),
        'coordination': DSSkill('coordination', SKILL_NAMES['coordination'], SKILL_DESCR['coordination'], member_bonus=[('cyber', 1)]),
        'reaction_speed': DSSkill('reaction_speed', SKILL_NAMES['reaction_speed'], SKILL_DESCR['reaction_speed'], member_bonus=[('cyber', 1)]),
        'savoir_faire': DSSkill('savoir_faire', SKILL_NAMES['savoir_faire'], SKILL_DESCR['savoir_faire'], member_bonus=[('cyber', 1)]),
        'interfacing': DSSkill('interfacing', SKILL_NAMES['interfacing'], SKILL_DESCR['interfacing'], member_bonus=[('cyber', 1)]),
        'composure': DSSkill('composure', SKILL_NAMES['composure'], SKILL_DESCR['composure'], member_bonus=[('cyber', 1)]),
    }

    define ds_callbacks = {
        'check': [ds_up_skill, ds_save_last],
        'level_up': [],
        'get_result': [ds_show_check],
    }

    define ds_archetype_presets = {
        1: {
            'logic': 5,
            'encyclopedia': 6,
            'rhetoric': 5,
            'drama': 5,
            'conceptualization': 5,
            'visual_calculus': 5,
            'volition': 2,
            'inland_empire': 2,
            'authority': 2,
            'empathy': 2,
            'esprit': 2,
            'suggestion': 2,
            'endurance': 1,
            'pain_threshold': 1,
            'physical_instrument': 1,
            'instinct': 1,
            'shivers': 1,
            'half_light': 1,
            'perception': 4,
            'coordination': 4,
            'reaction_speed': 4,
            'savoir_faire': 4,
            'interfacing': 4,
            'composure': 4,
        },
        2: {
            'logic': 3,
            'encyclopedia': 3,
            'rhetoric': 3,
            'drama': 3,
            'conceptualization': 3,
            'visual_calculus': 3,
            'volition': 5,
            'inland_empire': 6,
            'authority': 5,
            'empathy': 5,
            'esprit': 5,
            'suggestion': 5,
            'endurance': 2,
            'pain_threshold': 2,
            'physical_instrument': 2,
            'instinct': 2,
            'shivers': 2,
            'half_light': 2,
            'perception': 2,
            'coordination': 2,
            'reaction_speed': 2,
            'savoir_faire': 2,
            'interfacing': 2,
            'composure': 2,
        },
        3: {
            'logic': 1,
            'encyclopedia': 1,
            'rhetoric': 1,
            'drama': 1,
            'conceptualization': 1,
            'visual_calculus': 1,
            'volition': 2,
            'inland_empire': 2,
            'authority': 2,
            'empathy': 2,
            'esprit': 2,
            'suggestion': 2,
            'endurance': 5,
            'pain_threshold': 5,
            'physical_instrument': 6,
            'instinct': 5,
            'shivers': 5,
            'half_light': 5,
            'perception': 4,
            'coordination': 4,
            'reaction_speed': 4,
            'savoir_faire': 4,
            'interfacing': 4,
            'composure': 4,
        },
    }

# Переменные
    default ds_menuset = set()

## C кем знаком? (0 - не знает ничего, 1 - знает внешность, 2 - знает, как зовут)

    default ds_met = {
        'dv': 0,
        'un': 0,
        'sl': 0,
        'us': 0,
        'mi': 0,
        'el': 0,
        'mt': 0,
        'mz': 0,
        'cs': 0,
        'yn': 0
    }

## Куда записан?

    default ds_member = {
        'music': False,
        'cyber': False,
        'sport': False,
        'library': False
    }
 
## Уровни сложности проверок
    define lvl_trivial = 6 # Элементарно
    define lvl_easy = 8 # Просто
    define lvl_medium = 10 # Средне
    define lvl_up_medium = 11 # Средне
    define lvl_challenging = 12 # Сложно
    define lvl_formidable = 13 # Тяжело
    define lvl_legendary = 14 # Легендарно
    define lvl_heroic = 15 # Героично
    define lvl_godly = 16 # Невероятно
    define lvl_unimaginable = 18 # Немыслимо
    define lvl_impossible = 20 # Невозможно

## Отношение персонажей
    default ds_lp = {
        'dv': 0,
        'sl': 0,
        'un': 0,
        'us': 0,
        'mi': 0,
        'el': 0,
        'mt': 0,
        'mz': 0,
        'cs': 0,
        'yn': 0
    }

## Общие параметры
    default ds_karma = 0 # Репутация - насколько хорошо себя ведёт ГГ
    default ds_health = DSLifeParameter('endurance', {'damage': [ds_show_damage_health, ds_die_zero_health], 'up': [ds_show_up_health], 'restore': [ds_show_restore_health]}) # Здоровье
    default ds_morale = DSLifeParameter('volition', {'damage': [ds_show_damage_morale, ds_die_zero_morale], 'up': [ds_show_up_morale], 'restore': [ds_show_restore_morale]}) # Боевой дух
    default ds_archetype = 0 # Избранный персонаж
    default ds_knowing = 0 # Знание
    default ds_semtype = 0 # Тип Семёна
    default ds_homo_traits = 0

    $ ds_game_started = False

    default ds_last_skillcheck = None # Результат последней проверки

# Эффекты

    transform semi_transparent:
        alpha 0.5
    
    transform show_damage:
        alpha 0.5
        pause 0.1
        alpha 0.0
        pause 0.1
        alpha 0.5
        pause 0.1
        alpha 0.0
        pause 0.1
        alpha 0.5
        pause 1.0
        linear 0.1 alpha 0.0

    transform show_restore:
        alpha 0.0
        linear 0.1 alpha 0.5
        pause 1.0
        linear 0.1 alpha 0.0

    image fx ds_rain:
        "mods/disco_sovenok/bg/rain/rain1.png"
        pause 0.1
        "mods/disco_sovenok/bg/rain/rain2.png"
        pause 0.1
        "mods/disco_sovenok/bg/rain/rain3.png"
        pause 0.1
        "mods/disco_sovenok/bg/rain/rain4.png"
        pause 0.1
        "mods/disco_sovenok/bg/rain/rain5.png"
        pause 0.1
        repeat

    transform ds_thunder(child):
        child
        choice:
            pause 5.0
        choice:
            pause 10.0
        choice:
            pause 20.0
        choice:
            pause 25.0
        choice:
            pause 50.0
        child with Fade(0.05, 0.1, 0.05, color="#fff")
        pause 0.05
        child with Fade(0.05, 0.1, 0.05, color="#fff")
        repeat

    # Последующие анимации взяты из БКРР

    # Анимации "встань" и "сядь" для спрайтов

    transform ds_sit_down:
        subpixel True
        parallel:
            ease 1.0 ypos 0.22
        parallel:
            ease 0.75 zoom 1.05
            ease 0.5 zoom 1.0

    transform ds_sit_down1:
        subpixel True
        parallel:
            ease 1.0 ypos 0.15
        parallel:
            ease 0.75 zoom 1.05
            ease 0.5 zoom 1.0

    transform ds_sit_down1_close:
        subpixel True
        parallel:
            ease 1.0 ypos 0.05
        parallel:
            ease 0.75 zoom 1.05
            ease 0.5 zoom 1.0
    
    # вариант, где спрайт уже сидит (авторский)
    transform ds_seated:
        subpixel True
        ypos 0.22
    
    transform ds_seated1:
        subpixel True
        ypos 0.15
    
    transform ds_seated1_close:
        subpixel True
        ypos 0.05

    transform ds_get_up:
        subpixel True
        parallel:
            ease 1.0 ypos 0.0
        parallel:
            ease 0.75 zoom 1.05
            ease 0.5 zoom 1.0

    transform ds_get_up_fast:
        subpixel True
        parallel:
            ease 0.3 ypos 0.0
        parallel:
            ease 0.2 zoom 1.05
            ease 0.07 zoom 1.0

    # Анимация стула, когда персонаж встаёт или садится

    transform ds_chair_move_sd:
        yanchor 0.0
        ypos 0.1
        zoom 0.95
        ease 0.75 ypos 0.0 zoom 1.0

    transform ds_chair_move_gu:
        yanchor 0.0
        ease 0.75 ypos 0.1 zoom 0.95

    # Анимация движения вперёд

    transform ds_moving_forward_near(t, z=1.5):
        subpixel True
        truecenter
        linear t zoom z ypos 0.25

    transform ds_moving_forward_far(t, z=1.5):
        subpixel True
        truecenter
        linear t zoom z ypos 0.40

    # Анимация бега

    transform ds_running_atl:
        truecenter
        zoom 1.25
        parallel:
            ease 0.25 zoom 1.30 rotate 0.75
            ease 0.20 zoom 1.25 rotate -0.75
            ease 0.25 zoom 1.30 rotate 0.75
            ease 0.20 zoom 1.35 rotate -0.75
            repeat
        parallel:
            ease 0.25 xpos 0.495
            ease 0.20 xpos 0.505
            repeat
        parallel:
            ease 0.25 ypos 0.495
            ease 0.30 ypos 0.505
            repeat

    # Анимация воды

    transform ds_water_atl:
        truecenter
        subpixel True
        alpha 0.8
        ease 0.5 zoom 1.2
        parallel:
            choice:
                ease 1.5 zoom 1.19
                ease 1.5 zoom 1.21
            choice 2:
                ease 2.0 zoom 1.195
                ease 2.0 zoom 1.205
            repeat
        parallel:
            choice:
                ease 15.0 xpos 0.51
            choice:
                ease 15.0 xpos 0.49
            choice:
                ease 20.0 xpos 0.51
            choice:
                ease 20.0 xpos 0.49
            repeat
        parallel:
            choice:
                ease 1.5 rotate 0.0
            choice:
                ease 1.5 rotate 0.5
                ease 1.5 rotate -0.5
            choice:
                ease 2.5 rotate 0.5
                ease 2.5 rotate -0.5
            choice:
                ease 2.5 rotate 0.75
                ease 2.5 rotate -0.75
            repeat

    # Эффект встряски

    transform ds_shake_atl:
        truecenter
        zoom 1.2
        parallel:
            linear 0.15 rotate -1
            linear 0.15 rotate 0.5
            linear 0.15 rotate -0.5
            linear 0.15 rotate 0
        parallel:
            ease 0.25 zoom 1.0

    transform ds_bus_shaking:
        subpixel True
        truecenter
        zoom 1.03
        parallel:
            linear 0.2 xoffset -2
            linear 0.3 xoffset 3
            linear 0.2 xoffset -1
            linear 0.3 xoffset 2
            repeat
        parallel:
            linear 0.2 yoffset -1
            linear 0.25 yoffset 2
            linear 0.2 yoffset -1
            repeat

    transform ds_shiver_atl:
        truecenter
        ease 0.25 zoom 1.1
        parallel:
            ease 0.25 zoom 1.11 rotate 0.75
            ease 0.25 zoom 1.1 rotate -0.75
            repeat
        parallel:
            ease 0.10 xpos 0.495
            ease 0.10 xpos 0.505
            repeat
        parallel:
            ease 0.15 ypos 0.495
            ease 0.15 ypos 0.505
            repeat

    transform ds_shiver_lite:
        truecenter
        ease 0.25 zoom 1.005
        parallel:
            ease 0.35 zoom 1.006 rotate 0.01
            ease 0.35 zoom 1.005 rotate -0.01
            repeat
        parallel:
            ease 0.15 xpos 0.499
            ease 0.15 xpos 0.501
            repeat
        parallel:
            ease 0.25 ypos 0.499
            ease 0.25 ypos 0.501
            repeat

    transform ds_shiver_guitar_fight:
        subpixel True
        truecenter
        ease 0.25 zoom 1.005
        pause 1.2
        parallel:
            ease 0.35 zoom 1.006
            ease 0.35 zoom 1.005
            repeat
        # parallel:
        #     ease 0.15 xpos 0.499
        #     ease 0.15 xpos 0.501
        #     repeat
        parallel:
            ease 0.25 ypos 0.499
            ease 0.11 ypos 0.501
            repeat

    transform ds_dream_bg_throbbing:
        subpixel True
        truecenter
        parallel:
            ease 3.0 zoom 1.05
            ease 3.0 zoom 1.0
            repeat

    transform ds_dream_sprite_rotate_clockwise:
        subpixel True
        alpha 0.6
        truecenter
        zoom 1.4
        parallel:
            ease 7.0 zoom 3.0
        parallel:
            ease 7.0 xalign 0.9
        parallel:
            ease 7.0 rotate 50
        parallel:
            linear 6.0 alpha 0.0

    transform ds_dream_sprite_rotate_counterclockwise:
        subpixel True
        alpha 0.6
        truecenter
        zoom 1.4
        parallel:
            ease 5.0 zoom 3.0
        parallel:
            ease 5.0 xalign 0.1
        parallel:
            ease 5.0 rotate -40
        parallel:
            linear 4.0 alpha 0.0


    # Отсвет от пламени

    transform ds_glow_atl(imgf):
        im.MatrixColor(imgf, im.matrix.brightness(0.17))
        choice 2:
            ease 0.4 alpha 0.5
        choice 2:
            ease 0.3 alpha 0.75
        choice 2:
            ease 0.3 alpha 0.6
        choice:
            ease 0.25 alpha 0.9
        choice:
            ease 0.2 alpha 1.0
        repeat

    # Эффект двоения в глазах

    transform ds_appdouble_atl(imgn, z=1.1, zt=1.0, t=1.0):
        contains:
            ImageReference(imgn)
            truecenter
            linear zt zoom z
        contains:
            ImageReference(imgn)
            truecenter
            zoom z
            alpha 0.0
            pause zt
            linear t xpos 0.48 alpha 0.3 zoom (z + 0.05)
        contains:
            ImageReference(imgn)
            truecenter
            zoom z
            alpha 0.0
            pause zt
            linear t xpos 0.51 alpha 0.2 zoom (z + 0.05)

    transform ds_vertigo_atl(imgn, z=1.1, zt=1.0, t=1.0, first=39, second=11):
        contains:
            ImageReference(imgn)
            truecenter
            linear zt zoom z
        contains:
            ImageReference(imgn)
            truecenter
            zoom z
            alpha 0.0
            pause zt
            parallel:
                linear t alpha 0.3 zoom (z + 0.05)
            parallel:
                linear 5.0 rotate -first
                linear 10.0 rotate first
                linear 5.0 rotate 0
                repeat
        contains:
            ImageReference(imgn)
            truecenter
            zoom z
            alpha 0.0
            pause zt
            linear t alpha 0.2 zoom (z + 0.05)
            parallel:
                linear 1.0 rotate second
                linear 2.0 rotate -second
                linear 1.0 rotate 0
                repeat
            parallel:
                linear 1.5 zoom (z + 0.15)
                linear 2.5 zoom (z + 0.05)
    
    transform ds_running:
        zoom 1.05 anchor (48,27)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (25,25)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (-25,25)
        repeat

# Персонажи

## Оригинальные обозначения
# cs - Виола
# dv - Алиса
# el - Электроник
# mi - Мику
# mt - ОД
# mz - Женя
# pi - Пионер
# sh - Шурик
# sl - Славя
# un - Лена
# us - Ульяна
# uv - Юля
# me - Семён

## Атрибуты - внутренние голоса
    $ lgc = Character (u'Логика', color="00ffff", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ enc = Character (u'Энциклопедия', color="00ffff", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ rhe = Character (u'Риторика', color="00ffff", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ dra = Character (u'Драма', color="00ffff", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ con = Character (u'Концептуализация', color="00ffff", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ vic = Character (u'Визуальный анализ', color="00ffff", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    $ vol = Character (u'Сила воли', color="800080", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ ine = Character (u'Внутренняя империя', color="800080", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ aut = Character (u'Авторитет', color="800080", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ emp = Character (u'Эмпатия', color="800080", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ esp = Character (u'Командная волна', color="800080", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ sug = Character (u'Внушение', color="800080", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    $ edr = Character (u'Стойкость', color="e52b50", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ pat = Character (u'Болевой порог', color="e52b50", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ phi = Character (u'Грубая сила', color="e52b50", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ ins = Character (u'Инстинкт', color="e52b50", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ shi = Character (u'Трепет', color="e52b50", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ hfl = Character (u'Сумрак', color="e52b50", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    $ per_eye = Character (u'Восприятие (зрение)', color="f8f32b", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ per_hea = Character (u'Восприятие (слух)', color="f8f32b", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ per_sme = Character (u'Восприятие (обоняние)', color="f8f32b", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ per_tas = Character (u'Восприятие (вкус)', color="f8f32b", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ per_toc = Character (u'Восприятие (осязание)', color="f8f32b", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ cor = Character (u'Координация', color="f8f32b", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ res = Character (u'Скорость реакции', color="f8f32b", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ svf = Character (u'Эквилибристика', color="f8f32b", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ inf = Character (u'Техника', color="f8f32b", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ com = Character (u'Самообладание', color="f8f32b", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    $ arb = Character (u'Рептильный мозг', color="ffffff", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ lim = Character (u'Лимбическая система', color="ffffff", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

## Голоса девушек
    $ dvv = Character (u'Девушка', color="ffaa00", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ mig = Character (u'Девушка', color="00deff", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ mtg = Character (u'Девушка', color="00ea32", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ slv = Character (u'Девушка', color="ffd200", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ unv = Character (u'Девушка', color="b956ff", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ usv = Character (u'Девушка', color="ff3200", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ elg = Character (u'Парень', color="ffff00", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

## Иные персонажи

    $ cr = Character (u'Повешенный труп', color="e1dd7d", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ gn = Character (u'Генда', color="7d7f7d", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ ck = Character (u'Повариха', color="1f75fe", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ ynp = Character (u'Девушка', color="74b05f", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ yn = Character (u'Яна', color="74b05f", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ fz = Character (u'Борис Саныч', color="7b001c", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ fzp = Character (u'Физрук', color="7b001c", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ sb = Character (u'Девушка', color="ff335c", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ ag = Character (u'Мужчина', color="999999", ctc="ctc_animation", ctc_position="fixed", drop_shadow=[ (2, 2) ], drop_shadow_color="#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ moa = Character (u'Министерство въезда', color="ff3200", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ book = Character (u'Книга', color='ffffff', ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

# Изображения

    image ds_epigraph = "mods/disco_sovenok/cg/epigraph.png"
    image ds_tournament = "mods/disco_sovenok/gui/cards/table/alt_tournament_bg.png"

    image ds_bus_crash = "mods/disco_sovenok/gui/ach/gen/bus_crash.png"
    image ds_beat_girls = "mods/disco_sovenok/gui/ach/gen/beat_girls.png"
    image ds_know_history = "mods/disco_sovenok/gui/ach/gen/know_history.png"
    # image ds_had_sex = "mods/disco_sovenok/gui/ach/gen/had_sex.png"
    image ds_us_gone = "mods/disco_sovenok/gui/ach/gen/us_gone.png"
    # image ds_mi_rape = "mods/disco_sovenok/gui/ach/gen/mi_rape.png"
    image ds_arstotzka = "mods/disco_sovenok/gui/ach/gen/arztotzka.png"
    image ds_electrocution = "mods/disco_sovenok/gui/ach/gen/electrocution.png"
    # image ds_us_escape = "mods/disco_sovenok/gui/ach/us/us_escape.png"image ds_bus_crash = "mods/disco_sovenok/gui/ach/gen/bus_crash.png"

# Таблица эмоций, одежд и аксессуаров персонажей
# Эмоции (emo) -- словарь, определяющий номер тела, соответствующий эмоции
# Одежда (cloth) и аксессуары (acc) -- словари, определяющие фактическое название файла (None соответствует необходимости проигнорировать соответствующий элемент)
    '''
    define ds_char_table = {
        'ar': {
            'normal': {
                'emo': {
                    'dontlike': 2,
                    'dontlike2': 1,
                    'laugh': 1,
                    'laugh2': 1,
                    'normal': 1,
                    'smile': 1,
                    'sad': 2,
                },
                'cloth': {
                    'pioneer': None,
                },
                'acc': {}
            }
        },
        'dn': {
            'normal': {
                'emo': {
                    'dontcare': 1,
                    'grin': 1,
                    'normal': 1,
                    'smile': 1,
                    'unsured': 1,
                    'dontlike': 2,
                    'upset': 2,
                    'sad': 3,
                    'scared': 3,
                    'shocked': 3,
                    'sick': 3,
                    'surprise': 3,
                },
                'cloth': {
                    'pioneer': None,
                },
                'acc': {}
            }
        },
        'dv': {
            'normal': {
                'emo': {
                    'concent': 1,
                    'cry': 1,
                    'evil_smile': 1,
                    'scared': 1,
                    'shocked': 1,
                    'surprise': 1,
                    'think': 1,
                    'grin': 2,
                    'think2': 2,
                    'closed_eyes': 3,
                    'cry_smile': 3,
                    'guilty': 3,
                    'sad': 3,
                    'shy': 3,
                    'dontlike': 4,
                    'laugh': 4,
                    'normal': 4,
                    'sad2': 4,
                    'shy2': 4,
                    'smile': 4,
                    'soft_smile': 4,
                    'tired': 4,
                    'angry': 5,
                    'rage': 5,
                },
                'cloth': {
                    'naked': None,
                    'casual': 'casual',
                    'dress': 'dress',
                    'modern': 'modern',
                    'pioneer': 'pioneer',
                    'pioneer2': 'pioneer2',
                    'sport': 'sport1',
                    'sport2': 'sport2',
                    'swim': 'swim',
                    'underwear': 'underwear',
                    'winter': 'winter',
                },
                'acc': {}
            },
            'close': {
                'emo': {
                    'cry': 1,
                    'evil_smile': 1,
                    'scared': 1,
                    'shocked': 1,
                    'surprise': 1,
                    'grin': 2,
                    'closed_eyes': 3,
                    'guilty': 3,
                    'sad': 3,
                    'shy': 3,
                    'laugh': 4,
                    'smile': 4,
                    'soft_smile': 4,
                    'angry': 5,
                    'rage': 5,
                },
                'cloth': {
                    'naked': None,
                    'dress': 'dress',
                    'modern': 'modern',
                    'pioneer': 'pioneer',
                    'pioneer2': 'pioneer2',
                    'sport': 'sport1',
                    'swim': 'swim',
                },
                'acc': {}
            },
            'far': {
                'emo': {
                    'concent': 1,
                    'cry': 1,
                    'evil_smile': 1,
                    'scared': 1,
                    'shocked': 1,
                    'surprise': 1,
                    'think': 1,
                    'grin': 2,
                    'guilty': 3,
                    'sad': 3,
                    'shy': 3,
                    'laugh': 4,
                    'normal': 4,
                    'sad2': 4,
                    'shy2': 4,
                    'smile': 4,
                    'soft_smile': 4,
                    'tired': 4,
                    'angry': 5,
                    'rage': 5,
                },
                'cloth': {
                    'naked': None,
                    'dress': 'dress',
                    'modern': 'modern',
                    'pioneer': 'pioneer',
                    'pioneer2': 'pioneer2',
                    'sport': 'sport1',
                    'swim': 'swim',
                },
                'acc': {}
            }
        },
        'el': {
            'normal': {
                'emo': {
                    'grin': 1,
                    'normal': 1,
                    'smile': 1,
                    'fingal': 2,
                    'sad': 2,
                    'scared': 2,
                    'shocked': 2,
                    'surprise': 2,
                    'upset': 2,
                    'angry': 3,
                    'laugh': 3,
                    'serious': 3,
                },
                'cloth': {
                    'naked': None,
                    'modern': 'shirt_black',
                    'pioneer': 'pioneer',
                },
                'acc': {}
            },
            'close': {
                'emo': {
                    'grin': 1,
                    'normal': 1,
                    'smile': 1,
                    'fingal': 2,
                    'sad': 2,
                    'scared': 2,
                    'shocked': 2,
                    'surprise': 2,
                    'upset': 2,
                    'angry': 3,
                    'laugh': 3,
                    'serious': 3,
                },
                'cloth': {
                    'naked': None,
                    'pioneer': 'pioneer',
                },
                'acc': {}
            },
            'far': {
                'emo': {
                    'grin': 1,
                    'normal': 1,
                    'smile': 1,
                    'fingal': 2,
                    'sad': 2,
                    'scared': 2,
                    'shocked': 2,
                    'surprise': 2,
                    'upset': 2,
                    'angry': 3,
                    'laugh': 3,
                    'serious': 3,
                },
                'cloth': {
                    'naked': None,
                    'pioneer': 'pioneer',
                },
                'acc': {}
            }
        },
        'mi': {
            'normal': {
                'emo': {
                    'cry': 1,
                    'dontlike': 1,
                    'guilty': 1,
                    'laugh': 1,
                    'pity': 1,
                    'scared': 1,
                    'shocked': 1,
                    'shy': 1,
                    'surprise': 1,
                    'unsure': 1,
                    'cry_smile': 2,
                    'grin': 2,
                    'happy': 2,
                    'pity_grin': 2,
                    'pity_smile': 2,
                    'sad_smile': 2,
                    'sad': 2,
                    'smile': 2,
                    'angry': 3,
                    'charmed': 3,
                    'confusion': 3,
                    'despair': 3,
                    'joy': 3,
                    'normal': 3,
                    'rage': 3,
                    'serious': 3,
                    'tender': 3,
                    'upset': 3,
                    'yawn': 3,
                },
                'cloth': {
                    'naked': None,
                    'casual': 'casual',
                    'modern': 'civil',
                    'pioneer': 'pioneer',
                    'sport': 'sport',
                    'underwear': 'underwear',
                },
                'acc': {}
            },
            'close': {
                'emo': {
                    'cry': 1,
                    'dontlike': 1,
                    'guilty': 1,
                    'laugh': 1,
                    'pity': 1,
                    'scared': 1,
                    'shocked': 1,
                    'shy': 1,
                    'surprise': 1,
                    'unsure': 1,
                    'cry_smile': 2,
                    'grin': 2,
                    'happy': 2,
                    'pity_grin': 2,
                    'pity_smile': 2,
                    'sad_smile': 2,
                    'sad': 2,
                    'smile': 2,
                    'angry': 3,
                    'charmed': 3,
                    'confusion': 3,
                    'despair': 3,
                    'joy': 3,
                    'normal': 3,
                    'rage': 3,
                    'serious': 3,
                    'tender': 3,
                    'upset': 3,
                    'yawn': 3,
                },
                'cloth': {
                    'naked': None,
                    'modern': 'civil',
                    'pioneer': 'pioneer',
                    'sport': 'sport',
                    'underwear': 'underwear',
                },
                'acc': {}
            },
            'far': {
                'emo': {
                    'cry': 1,
                    'dontlike': 1,
                    'guilty': 1,
                    'laugh': 1,
                    'pity': 1,
                    'scared': 1,
                    'shocked': 1,
                    'shy': 1,
                    'surprise': 1,
                    'unsure': 1,
                    'cry_smile': 2,
                    'grin': 2,
                    'happy': 2,
                    'pity_grin': 2,
                    'pity_smile': 2,
                    'sad_smile': 2,
                    'sad': 2,
                    'smile': 2,
                    'angry': 3,
                    'charmed': 3,
                    'confusion': 3,
                    'despair': 3,
                    'joy': 3,
                    'normal': 3,
                    'rage': 3,
                    'serious': 3,
                    'tender': 3,
                    'upset': 3,
                    'yawn': 3,
                },
                'cloth': {
                    'naked': None,
                    'casual': 'casual',
                    'modern': 'civil',
                    'pioneer': 'pioneer',
                    'sport': 'sport',
                    'underwear': 'underwear',
                },
                'acc': {}
            }
        },
        'mz': {
            'normal': {
                'emo': {
                    'amazed': 1,
                    'bukal': 1,
                    'fun': 1,
                    'hope': 1,
                    'laugh': 1,
                    'normal': 1,
                    'sad': 1,
                    'sceptic': 1,
                    'angry': 2,
                    'cry': 2,
                    'rage': 2,
                    'shyangry': 2,
                    'smile': 2,
                    'confused': 3,
                    'excitement': 3,
                    'shy': 3,
                },
                'cloth': {
                    'naked': None,
                    'pioneer': 'pioneer',
                    'pullover': 'pullover',
                    'swim': 'swimsuit',
                },
                'acc': {
                    'glasses': 'glasses',
                }
            },
            'close': {
                'emo': {
                    'amazed': 1,
                    'bukal': 1,
                    'fun': 1,
                    'hope': 1,
                    'laugh': 1,
                    'normal': 1,
                    'sad': 1,
                    'sceptic': 1,
                    'angry': 2,
                    'cry': 2,
                    'rage': 2,
                    'shyangry': 2,
                    'smile': 2,
                    'confused': 3,
                    'excitement': 3,
                    'shy': 3,
                },
                'cloth': {
                    'naked': None,
                    'pioneer': 'pioneer',
                    'pullover': 'pullover',
                    'swim': 'swimsuit',
                },
                'acc': {
                    'glasses': 'glasses',
                }
            },
            'far': {
                'emo': {
                    'amazed': 1,
                    'bukal': 1,
                    'fun': 1,
                    'hope': 1,
                    'laugh': 1,
                    'normal': 1,
                    'sad': 1,
                    'sceptic': 1,
                    'angry': 2,
                    'cry': 2,
                    'rage': 2,
                    'shyangry': 2,
                    'smile': 2,
                    'confused': 3,
                    'excitement': 3,
                    'shy': 3,
                },
                'cloth': {
                    'naked': None,
                    'pioneer': 'pioneer',
                    'pullover': 'pullover',
                    'swim': 'swimsuit',
                },
                'acc': {
                    'glasses': 'glasses',
                }
            }
        },
        'sh': {
            'normal': {
                'emo': {
                    'laugh': 1,
                    'scared': 1,
                    'smile': 1,
                    'upset': 1,
                    'cry': 2,
                    'rage': 2,
                    'smile2': 2,
                    'normal': 3,
                    'serious': 3,
                    'surprise': 3,
                },
                'cloth': {
                    'towel': None,
                    'bathrobe': 'bathrobe',
                    'pioneer': 'pioneer',
                    'shirt': 'shirt',
                },
                'acc': {
                    'red_nose': 'red_nose'
                }
            },
            'close': {
                'emo': {
                    'laugh': 1,
                    'scared': 1,
                    'smile': 1,
                    'upset': 1,
                    'cry': 2,
                    'rage': 2,
                    'smile2': 2,
                    'normal': 3,
                    'serious': 3,
                    'surprise': 3,
                },
                'cloth': {
                    'towel': None,
                    'bathrobe': 'bathrobe',
                    'pioneer': 'pioneer',
                    'shirt': 'shirt',
                },
                'acc': {
                    'red_nose': 'red_nose'
                }
            },
            'far': {
                'emo': {
                    'laugh': 1,
                    'scared': 1,
                    'smile': 1,
                    'upset': 1,
                    'cry': 2,
                    'rage': 2,
                    'smile2': 2,
                    'normal': 3,
                    'serious': 3,
                    'surprise': 3,
                },
                'cloth': {
                    'towel': None,
                    'bathrobe': 'bathrobe',
                    'pioneer': 'pioneer',
                    'shirt': 'shirt',
                },
                'acc': {
                    'red_nose': 'red_nose'
                }
            }
        },
        'sl': {
            'normal': {
                'emo': {
                    'dontlike': 1,
                    'involve': 1,
                    'normal': 1,
                    'serious': 1,
                    'smile': 1,
                    'happy': 2,
                    'laugh': 2,
                    'shy': 2,
                    'shy2': 2,
                    'shy3': 2,
                    'smile2': 2,
                    'tricky': 2,
                    'tricky2': 2,
                    'angry': 3,
                    'cry_smile': 3,
                    'happy2': 3,
                    'obsessed': 3,
                    'sad': 3,
                    'shy4': 3,
                    'smile3': 3,
                    'surprise': 3,
                    'scared': 4,
                    'scared2': 4,
                    'tender': 4,
                    'tender2': 4,
                },
                'cloth': {
                    'naked': None,
                    'dress': 'dress',
                    'modern': 'casual',
                    'pioneer': 'pioneer',
                    'sport': 'sport',
                    'swim': 'swim',
                },
                'acc': {}
            },
            'close': {
                'emo': {
                    'dontlike': 1,
                    'involve': 1,
                    'normal': 1,
                    'serious': 1,
                    'smile': 1,
                    'happy': 2,
                    'laugh': 2,
                    'shy': 2,
                    'shy2': 2,
                    'shy3': 2,
                    'smile2': 2,
                    'tricky': 2,
                    'tricky2': 2,
                    'angry': 3,
                    'cry_smile': 3,
                    'happy2': 3,
                    'obsessed': 3,
                    'sad': 3,
                    'shy4': 3,
                    'smile3': 3,
                    'surprise': 3,
                    'scared': 4,
                    'scared2': 4,
                    'tender': 4,
                    'tender2': 4,
                },
                'cloth': {
                    'naked': None,
                    'dress': 'dress',
                    'pioneer': 'pioneer',
                    'sport': 'sport',
                    'swim': 'swim',
                },
                'acc': {}
            },
            'far': {
                'emo': {
                    'dontlike': 1,
                    'involve': 1,
                    'normal': 1,
                    'serious': 1,
                    'smile': 1,
                    'happy': 2,
                    'laugh': 2,
                    'shy': 2,
                    'shy2': 2,
                    'shy3': 2,
                    'smile2': 2,
                    'tricky': 2,
                    'tricky2': 2,
                    'angry': 3,
                    'cry_smile': 3,
                    'happy2': 3,
                    'obsessed': 3,
                    'sad': 3,
                    'shy4': 3,
                    'smile3': 3,
                    'surprise': 3,
                    'scared': 4,
                    'scared2': 4,
                    'tender': 4,
                    'tender2': 4,
                },
                'cloth': {
                    'naked': None,
                    'dress': 'dress',
                    'pioneer': 'pioneer',
                    'sport': 'sport',
                    'swim': 'swim',
                },
                'acc': {}
            }
        },
        'ul': {
            'normal': {
                'emo': {
                    'angry': 1,
                    'normal': 1,
                    'sad': 1,
                    'dontlike': 2,
                    'grin': 2,
                    'guilty': 2,
                    'serious': 3,
                    'smile': 3,
                    'surprise': 3,
                },
                'cloth': {
                    'swim': None,
                    'dress': 'dress',
                    'pioneer': 'pioneer',
                },
                'acc': {
                    'bunny': 'bunny'
                }
            },
            'close': {
                'emo': {
                    'angry': 1,
                    'normal': 1,
                    'sad': 1,
                    'dontlike': 2,
                    'grin': 2,
                    'guilty': 2,
                    'serious': 3,
                    'smile': 3,
                    'surprise': 3,
                },
                'cloth': {
                    'swim': None,
                    'dress': 'dress',
                    'pioneer': 'pioneer',
                },
                'acc': {
                    'bunny': 'bunny'
                }
            },
            'far': {
                'emo': {
                    'angry': 1,
                    'normal': 1,
                    'sad': 1,
                    'dontlike': 2,
                    'grin': 2,
                    'guilty': 2,
                    'serious': 3,
                    'smile': 3,
                    'surprise': 3,
                },
                'cloth': {
                    'swim': None,
                    'dress': 'dress',
                    'pioneer': 'pioneer',
                },
                'acc': {
                    'bunny': 'bunny'
                }
            }
        },
        'un': {
            'normal': {
                'emo': {
                    'angry': 1,
                    'evil_grin': 1,
                    'evil_laugh': 1,
                    'evil': 1,
                    'evil_smile': 1,
                    'evil_surprise': 1,
                    'hysteric': 1,
                    'normal': 1,
                    'shy_smile': 1,
                    'shy_smile': 1,
                    'shy': 1,
                    'shy2': 1,
                    'smile': 1,
                    'smile2': 1,
                    'snide_smile': 1,
                    'sorrow': 1,
                    'cry_smile': 2,
                    'cry': 2,
                    'cry2': 2,
                    'cry3': 2,
                    'sad': 2,
                    'scared': 2,
                    'shocked': 2,
                    'surprise': 2,
                    'angry2': 3,
                    'grin': 3,
                    'laugh': 3,
                    'rage': 3,
                    'serious': 3,
                    'smile3': 3,
                },
                'cloth': {
                    'naked': None,
                    'dress': 'dress',
                    'modern': 'designer',
                    'pioneer': 'pioneer',
                    'night': 'sleep',
                    'sport': 'sport',
                    'swim': 'swim',
                    'underwear': 'underwear',
                },
                'acc': {
                    'closed_eyes': 'close_eyes',
                }
            },
            'close': {
                'emo': {
                    'angry': 1,
                    'evil_grin': 1,
                    'evil_laugh': 1,
                    'evil': 1,
                    'evil_smile': 1,
                    'evil_surprise': 1,
                    'hysteric': 1,
                    'normal': 1,
                    'shy_smile': 1,
                    'shy_smile': 1,
                    'shy': 1,
                    'shy2': 1,
                    'smile': 1,
                    'smile2': 1,
                    'snide_smile': 1,
                    'sorrow': 1,
                    'cry_smile': 2,
                    'cry': 2,
                    'cry2': 2,
                    'cry3': 2,
                    'sad': 2,
                    'scared': 2,
                    'shocked': 2,
                    'surprise': 2,
                    'angry2': 3,
                    'grin': 3,
                    'laugh': 3,
                    'rage': 3,
                    'serious': 3,
                    'smile3': 3,
                },
                'cloth': {
                    'naked': None,
                    'dress': 'dress',
                    'pioneer': 'pioneer',
                    'sport': 'sport',
                    'swim': 'swim',
                },
                'acc': {
                    'closed_eyes': 'close_eyes',
                }
            },
            'far': {
                'emo': {
                    'angry': 1,
                    'evil_grin': 1,
                    'evil_laugh': 1,
                    'evil': 1,
                    'evil_smile': 1,
                    'evil_surprise': 1,
                    'hysteric': 1,
                    'normal': 1,
                    'shy_smile': 1,
                    'shy_smile': 1,
                    'shy': 1,
                    'shy2': 1,
                    'smile': 1,
                    'smile2': 1,
                    'snide_smile': 1,
                    'sorrow': 1,
                    'cry_smile': 2,
                    'cry': 2,
                    'cry2': 2,
                    'cry3': 2,
                    'sad': 2,
                    'scared': 2,
                    'shocked': 2,
                    'surprise': 2,
                    'angry2': 3,
                    'grin': 3,
                    'laugh': 3,
                    'rage': 3,
                    'serious': 3,
                    'smile3': 3,
                },
                'cloth': {
                    'naked': None,
                    'dress': 'dress',
                    'pioneer': 'pioneer',
                    'sport': 'sport',
                    'swim': 'swim',
                },
                'acc': {
                    'closed_eyes': 'close_eyes',
                }
            }
        },
        'vt': {
            'normal': {
                'emo': {
                    'angry': 1,
                    'rage': 1,
                    'shy': 1,
                    'normal': 2,
                    'sad': 2,
                    'smile': 2,
                    'laugh': 3,
                    'scared': 3,
                },
                'cloth': {
                    'swim': None,
                    'pioneer': 'pioneer',
                    'shirt': 'shirt',
                },
                'acc': {}
            }
        }
    }
    '''

## BG

    image bg ds_int_bus_forest = "mods/disco_sovenok/bg/int_bus_path.jpg"

    image bg ds_int_sporthall_day = "mods/disco_sovenok/bg/int_sporthall_day_7dl.jpg"
    image bg ds_int_sporthall_night = "mods/disco_sovenok/bg/int_sporthall_night_7dl.jpg"

    image bg ds_int_dininghall_table1_day = "mods/disco_sovenok/bg/dva_dish2.jpg"
    image bg ds_int_dininghall_table1_sunset = "mods/disco_sovenok/bg/dva_dish2s.jpg"
    image bg ds_int_dininghall_table1_night = "mods/disco_sovenok/bg/dva_dish2n.jpg"

    image bg ds_int_dininghall_table2_day = "mods/disco_sovenok/bg/dva_dish_day.jpg"
    image bg ds_int_dininghall_table2_sunset = "mods/disco_sovenok/bg/dva_dish_sunset.jpg"

    image bg ds_int_dininghall_door_day = "mods/disco_sovenok/bg/int_dining_hall_door_day.jpg"
    image bg ds_int_dininghall_door_sunset = "mods/disco_sovenok/bg/int_dining_hall_door_sunset.jpg"
    image bg ds_int_dininghall_door_night = "mods/disco_sovenok/bg/int_dining_hall_door_night.jpg"

    image bg ds_ext_sl_house_sunset = "mods/disco_sovenok/bg/ext_house_of_sl_sunset.jpg"
    image bg ds_ext_sl_house_night = "mods/disco_sovenok/bg/ext_house_of_sl_night.jpg"
    image bg ds_ext_sl_house_night2 = "mods/disco_sovenok/bg/ext_house_of_sl_night.jpg"

    image bg ds_ext_musclub_sunset = "mods/disco_sovenok/bg/ext_music_club_sunset.jpg"
    image bg ds_ext_musclub_night = "mods/disco_sovenok/bg/ext_music_club_night.png"

    image bg ds_ext_musclub_veranda_day = "mods/disco_sovenok/bg/ext_music_club_verandah_day.jpg"

    image bg ds_ext_el_house_day = "mods/disco_sovenok/bg/ext_house_of_el_day.jpg"
    image bg ds_ext_el_house_sunset = "mods/disco_sovenok/bg/ext_house_of_el_sunset.jpg"
    image bg ds_ext_el_house_night = "mods/disco_sovenok/bg/ext_house_of_el_night.jpg"

    image bg ds_int_el_house_sunset = "mods/disco_sovenok/bg/ext_house_of_el_sunset.jpg"
    image bg ds_int_el_house_night = "mods/disco_sovenok/bg/ext_house_of_el_night.jpg"

    image bg ds_int_sl_night = "mods/disco_sovenok/bg/int_house_of_sl_night.jpg"
    image bg ds_int_sl_night_light = "mods/disco_sovenok/bg/int_house_of_sl_night_light.jpg"

    image bg ds_ext_un_night = "mods/disco_sovenok/bg/ext_house_of_un_night_7dl.jpg"
    image bg ds_ext_un_sunset = "mods/disco_sovenok/bg/ext_house_of_un_sunset1.jpg"

    image bg ds_ext_houses_night = "mods/disco_sovenok/bg/ext_houses_night.jpg"

    image bg ds_ext_clubs_gate_night = "mods/disco_sovenok/bg/ext_clubs_gate_night.jpg"
    image bg ds_ext_clubs_gate_day = "mods/disco_sovenok/bg/ext_clubs_gate.jpg"

    image bg ds_ext_storage_day = "mods/disco_sovenok/bg/ext_warehouse_day_7dl.jpg"
    image bg ds_ext_storage_sunset = "mods/disco_sovenok/bg/ext_warehouse_sunset_7dl.jpg"
    image bg ds_ext_storage_night = "mods/disco_sovenok/bg/ext_warehouse_night_7dl.jpg"

    image bg ds_int_storage_day = "mods/disco_sovenok/bg/int_warehouse_day_7dl.jpg"
    image bg ds_int_storage_day2 = "mods/disco_sovenok/bg/int_warehouse_day2_7dl.jpg"
    image bg ds_int_storage_night = "mods/disco_sovenok/bg/int_warehouse_night_7dl.jpg"

    image bg ds_ext_showers_day = "mods/disco_sovenok/bg/ext_shower_day_7dl.jpg"
    image bg ds_ext_showers_night = "mods/disco_sovenok/bg/ext_shower_night_7dl.jpg"

    image bg ds_int_bathhouse = "mods/disco_sovenok/bg/int_bathhouse1.jpg"
    image bg ds_int_bathhouse_steam = "mods/disco_sovenok/bg/int_bathhouse_steam.jpg"

    image bg ds_int_library_basement = "mods/disco_sovenok/bg/int_library_basement.jpg"

    image bg ds_ext_backdoor_day = "mods/disco_sovenok/bg/ext_backdoor_day_7dl.jpg"
    image bg ds_ext_backdoor_sunset = "mods/disco_sovenok/bg/ext_backdoor_sunset_7dl.jpg"
    image bg ds_ext_backdoor_night = "mods/disco_sovenok/bg/ext_backdoor_night_7dl.jpg"

    image bg ds_ext_backroad_day = "mods/disco_sovenok/bg/ext_backroad_day_7dl.jpg"
    image bg ds_ext_backroad_sunset = "mods/disco_sovenok/bg/ext_backroad_sunset_7dl.jpg"

    image bg ds_ext_railroad_day = "mods/disco_sovenok/bg/ext_railroad_day.png"
    image bg ds_ext_railroad_sunset = "mods/disco_sovenok/bg/ext_railroad_sunset.jpg"

    image bg ds_int_train = "mods/disco_sovenok/bg/int_train_7dl.jpg"
    image bg ds_ext_train = "mods/disco_sovenok/bg/ext_train.jpg"

    image bg ds_ext_bus_town = "mods/disco_sovenok/bg/ext_bus_city.jpg"

    image bg ds_ext_square2_day = "mods/disco_sovenok/bg/ext_square2_day_7dl.jpg"
    image bg ds_ext_square2_night = "mods/disco_sovenok/bg/ext_square_alt_night.jpg"

    image bg ds_ext_another_club_day = "mods/disco_sovenok/bg/ext_another_club_day.jpg"

    image bg ds_ext_admin_day = "mods/disco_sovenok/bg/ext_admins_day_7dl.jpg"
    image bg ds_ext_admin_night = "mods/disco_sovenok/bg/ext_admins_night_7dl.jpg"

    image bg ds_int_admin_corridor = "mods/disco_sovenok/bg/int_admin_corridor.jpg"

    image bg ds_int_admin_day = "mods/disco_sovenok/bg/int_admin_day.png"
    image bg ds_int_admin_night = "mods/disco_sovenok/bg/int_admin_night.png"
    image bg ds_int_admin_night_light = "mods/disco_sovenok/bg/int_admin_night_light.png"
    image bg ds_int_admin_day_boxes1 = "mods/disco_sovenok/bg/int_admin_boxes_day.png"
    image bg ds_int_admin_sunset_boxes1 = "mods/disco_sovenok/bg/int_admin_boxes_sunset.png"
    image bg ds_int_admin_day_boxes2 = "mods/disco_sovenok/bg/int_admin_halfboxes_day.png"
    image bg ds_int_admin_sunset_boxes2 = "mods/disco_sovenok/bg/int_admin_halfboxes_sunset.png"
    image bg ds_int_admin_night_boxes2 = "mods/disco_sovenok/bg/int_admin_halfboxes_night.png"
    image bg ds_int_admin_morning_boxes2 = "mods/disco_sovenok/bg/int_admin_halfboxes_morning.png"

    image bg ds_int_kitchen_day = "mods/disco_sovenok/bg/int_kitchen_day.jpg"
    image bg ds_int_kitchen_sunset = "mods/disco_sovenok/bg/int_kitchen_sunset.jpg"
    image bg ds_int_kitchen_night = "mods/disco_sovenok/bg/int_kitchen_night.jpg"

    image bg ds_int_wardrobe = "mods/disco_sovenok/bg/int_wardrobe.jpg"

    image bg ds_int_clubs_pantry = "mods/disco_sovenok/bg/backroom.jpg"

    image bg ds_field_day = "mods/disco_sovenok/bg/ext_meadow_day.jpg"

    image bg ds_int_toilet_day = "mods/disco_sovenok/bg/int_toilet_day.png"
    image bg ds_int_toilet_night = "mods/disco_sovenok/bg/int_toilet_night.jpg"

    image bg ds_ext_camp_entrance_sunset = "mods/disco_sovenok/bg/ext_camp_entrance_sunset.jpg"

    image bg ds_papers_please_back = "mods/disco_sovenok/bg/papers_please.png"
    image ds_papers_please_front = "mods/disco_sovenok/bg/papers_please_front.png"
    image bg ds_papers_please_teract = "mods/disco_sovenok/bg/battle_tracers_2.png"

    image bg ds_ext_bus_sunset = "mods/disco_sovenok/bg/ext_bus_sunset.png"

    image bg ds_int_aidpost_night_nolight = "mods/disco_sovenok/bg/int_aidpost_no_light_night_7dl.jpg"

    image bg ds_ext_abyss_night = "mods/disco_sovenok/bg/ext_abyss_night.jpg"

    image bg ds_spb_dream1 = "mods/disco_sovenok/bg/ext_city_night2_7dl.jpg"
    image bg ds_spb_dream2 = "mods/disco_sovenok/bg/ext_city_night_7dl.jpg"
    image bg ds_spb_dream3 = "mods/disco_sovenok/bg/ext_gostinka_night_7dl.jpg"

    image bg ds_int_bus_sunset = "mods/disco_sovenok/bg/int_bus_sunset.jpg"

    image bg ds_church_entrance = "mods/disco_sovenok/bg/int_d3_hideout_7dl.jpg"
    image bg ds_church = "mods/disco_sovenok/bg/int_church_7dl.jpg"

    image bg ds_ext_old_building_day = "mods/disco_sovenok/bg/dct_ext_old_building_day.jpg"
    image bg ds_int_old_building_day = "mods/disco_sovenok/bg/int_old_building_day.jpg"
    image bg ds_int_old_building_room_day = "mods/disco_sovenok/bg/int_old_building_room_day.png"
    image bg ds_int_old_building_secondfloor = "mods/disco_sovenok/bg/secondfloor.jpg"
    image bg ds_int_old_building_cabinet_day = "mods/disco_sovenok/bg/int_old_building_cab_day_7dl.jpg"
    image bg ds_int_old_building_room2_day = "mods/disco_sovenok/bg/ss_datroom_day.jpg"

    image bg ds_int_another_club_day = "mods/disco_sovenok/bg/int_editorial_day_7dl.jpg"

    image bg ds_ext_stage_big_day = "mods/disco_sovenok/bg/ext_stage_big_day_7dl.jpg"
    image bg ds_ext_stage_big_sunset = "mods/disco_sovenok/bg/ext_stage_big_sunset_7dl.jpg"
    image bg ds_ext_stage_near_sunset = "mods/disco_sovenok/bg/ext_stage_near_sunset.jpg"

    image bg ds_ext_camp_entrance_car = "mods/disco_sovenok/bg/ext_camp_car.png"

## Новые CG

    image cg ds_day1_bus_window = "mods/disco_sovenok/cg/d1_me_bus_window_ll.jpg"
    image cg ds_day1_bus_exit = "mods/disco_sovenok/cg/camp_entrance_door.jpg"

    image cg ds_day1_hide = "mods/disco_sovenok/cg/d1_hide.jpg"

    image cg ds_day1_grasshopper_f1 = "mods/disco_sovenok/cg/d1_grasshopper_1_tttt.jpg"
    image cg ds_day1_grasshopper_f2 = "mods/disco_sovenok/cg/d1_grasshopper_2_tttt.jpg"
    image cg ds_day1_grasshopper_f3 = "mods/disco_sovenok/cg/d1_grasshopper_3_tttt.jpg"

    image cg ds_day1_dv_on_grass = "mods/disco_sovenok/cg/dv_fall_on_grass2.jpg"

    image cg ds_day1_dv_dinner = "mods/disco_sovenok/cg/Semyon_Alice_Dinner1.jpg"
    image cg ds_day1_dv_hiding = "mods/disco_sovenok/cg/night_event.jpg"

    image cg ds_day1_un_book = "mods/disco_sovenok/cg/d1_un_book_7dl.jpg"

    image cg ds_day2_lineup = "mods/disco_sovenok/cg/d2_all_lineup_ll.jpg"

    image cg ds_day2_dv_hits_el = "mods/disco_sovenok/cg/dv_hits_el.jpg"

    image cg ds_day2_swim_dv = "mods/disco_sovenok/cg/d2_water_dan.jpg"

    image cg ds_day3_train = "mods/disco_sovenok/cg/d2_us_trainhop_7dl.jpg"

    image cg ds_day3_disco_dv = "mods/disco_sovenok/cg/d6_disco2_7dl.jpg"
    image cg ds_day3_dv_dance = "mods/disco_sovenok/cg/d6_dv_dance_pioneer_7dl.jpg"

    image cg ds_dayx_volleyball = "mods/disco_sovenok/cg/volleyball.jpg"

    image cg ds_dayx_dv_argue = "mods/disco_sovenok/cg/dv_argue.jpg"

    image cg ds_day3_us_caught_f1 = "mods/disco_sovenok/cg/US_Polyana1.jpg"
    image cg ds_day3_us_caught_f2 = "mods/disco_sovenok/cg/US_Polyana2.jpg"
    image cg ds_day3_us_caught_f3 = "mods/disco_sovenok/cg/US_Polyana3.jpg"

    image cg ds_day3_us_potato_1 = "mods/disco_sovenok/cg/d5_potato_1.jpg"
    image cg ds_day3_us_potato_2 = "mods/disco_sovenok/cg/d5_potato_2.jpg"

    image cg ds_day3_mi_piano_1 = "mods/disco_sovenok/cg/cg_mi_piano1_ll.jpg"
    image cg ds_day3_mi_piano_2 = "mods/disco_sovenok/cg/cg_mi_piano2_ll.jpg"
    image cg ds_day3_mi_guitar = "mods/disco_sovenok/cg/d4_mi_guitar_club_7dl.jpg"
    image cg ds_day3_mi_teaching = "mods/disco_sovenok/cg/d7_mi_embrace.png"

    image cg ds_day3_robot_fail = "mods/disco_sovenok/cg/catday_warp_cat.jpg"

    image cg ds_day3_hatch = "mods/disco_sovenok/cg/d4_hatch_night_7dl.jpg"
    image cg ds_dayx_hatch_open = "mods/disco_sovenok/cg/d4_hatch_night_open_7dl.jpg"

    image cg ds_day3_cs_waiting = "mods/disco_sovenok/cg/ViCG1.jpg"

    image cg ds_day3_disco_with_dv = "mods/disco_sovenok/cg/d6_disco2_7dl.jpg"

    image cg ds_day3_un_fullmoon = "mods/disco_sovenok/cg/d3_beach_fullmoon.png"

    image cg ds_day3_dance_dv_shy = "mods/disco_sovenok/cg/d3_dv_dance_shy_ll.png"
    image cg ds_day3_dance_dv_normal = "mods/disco_sovenok/cg/d3_dv_dance_normal_ll.png"
    image cg ds_day3_dance_dv_grin = "mods/disco_sovenok/cg/d3_dv_dance_grin_ll.png"

    image cg ds_day3_dance_mi = "mods/disco_sovenok/cg/d3_mi_dance_afar_7dl.jpg"
    image cg ds_day3_dance_mi_costume = "mods/disco_sovenok/cg/d3_mi_dance_afar_bordo_7dl.jpg"

    image cg ds_day3_dance_mt = "mods/disco_sovenok/cg/d3_mt_dance.jpg"

    image cg ds_day3_dance_ya = "mods/disco_sovenok/cg/d3_dance_ya.png"

    image cg ds_day4_us_dv_play = "mods/disco_sovenok/cg/ussrr_dv_p_d4.jpg"

    image cg ds_day4_cs_car = "mods/disco_sovenok/cg/d4_cs_car_day_cs_7dl.jpg"

## Фансервисные CG (добавляются из-за цензуры в steam)

    image cg ds_day2_cs_near = "mods/disco_sovenok/cg/d5_cs.jpg"

    image cg ds_day2_mt_undress1 = "mods/disco_sovenok/cg/d2_mt_undressed.jpg"
    image cg ds_day2_mt_undress2 = "mods/disco_sovenok/cg/d2_mt_undressed_2.jpg"

    image cg ds_day2_mi_piano2 = "mods/disco_sovenok/cg/d2_miku_piano.jpg"
    image cg ds_day2_mi_piano1 = "mods/disco_sovenok/cg/d2_miku_piano2.jpg"

    image cg ds_day2_sl_swim = "mods/disco_sovenok/cg/d2_sl_swim.jpg"

    image cg ds_day3_dv_guitar = "mods/disco_sovenok/cg/d3_dv_guitar.jpg"

    image cg ds_day3_sl_bath = "mods/disco_sovenok/cg/d3_sl_bathhouse.jpg"

    image cg ds_day4_el_undress = "mods/disco_sovenok/cg/d4_el_wash.jpg"

    image cg ds_day4_uv_appear1 = "mods/disco_sovenok/cg/d4_uv_1.jpg"
    image cg ds_day4_uv_appear2 = "mods/disco_sovenok/cg/d4_uv.jpg"

    image cg ds_dayx_us_wash1 = "mods/disco_sovenok/cg/d5_dv_us_wash.jpg"
    image cg ds_dayx_us_wash2 = "mods/disco_sovenok/cg/d5_dv_us_wash_3.jpg"
    image cg ds_dayx_us_wash3 = "mods/disco_sovenok/cg/d5_dv_us_wash_4.jpg"

    image cg ds_dayx_sl_swim = "mods/disco_sovenok/cg/d6_sl_swim.jpg"

    image cg ds_dayx_sl_morning1 = "mods/disco_sovenok/cg/d7_sl_morning.jpg"
    image cg ds_dayx_sl_morning2 = "mods/disco_sovenok/cg/d7_sl_morning_2.jpg"

## CG 18+ (отсутствуют в steam-версии)

    # С Алисой
    image cg ds_day9_dv_sex1 = "mods/disco_sovenok/cg/d6_dv_hentai_2.jpg"
    image cg ds_day9_dv_sex2 = "mods/disco_sovenok/cg/d6_dv_hentai2_7dl.jpg"
    image cg ds_day9_dv_sex3 = "mods/disco_sovenok/cg/d6_dv_hentai.jpg"

    # Со Славей
    image cg ds_dayx_sl_sex1 = "mods/disco_sovenok/cg/d6_sl_hentai_2.jpg"
    image cg ds_dayx_sl_sex2 = "mods/disco_sovenok/cg/d6_sl_hentai_1.jpg"

    # С Леной
    image cg ds_dayx_un_sex1 = "mods/disco_sovenok/cg/d7_un_hentai_3.jpg"
    image cg ds_dayx_un_sex2 = "mods/disco_sovenok/cg/d7_un_hentai.jpg"

    # С Мику
    image cg ds_dayx_mi_sex1 = "mods/disco_sovenok/cg/miku_h_1_cenz.jpg"
    image cg ds_dayx_mi_sex2 = "mods/disco_sovenok/cg/miku_h_2_cenz.jpg"

    # С Электроником

    # С ОД

    # C Виолой

    image cg ds_day2_cs_sex1 = "mods/disco_sovenok/cg/uprtviolahentai.jpg"
    image cg ds_day2_cs_sex2 = "mods/disco_sovenok/cg/uprtviolahentai2.jpg"
    image cg ds_day2_cs_sex3 = "mods/disco_sovenok/cg/uprtviolahentai3.jpg"

# Аудио

## Музыка

    $ ds_death_bell = "mods/disco_sovenok/music/Heroes of Might and Magic III Necropolis theme by Paul Romero.ogg"
    $ ds_dream = "mods/disco_sovenok/music/british-sea-power-tiger-king.ogg"
    $ ds_dream2 = "mods/disco_sovenok/music/jack-wall-enter-spire.mp3"
    $ ds_cs_theme = "mods/disco_sovenok/music/violatheme.ogg"
    $ ds_sl_theme = "mods/disco_sovenok/music/newslavyatheme.ogg"
    $ ds_chase = "mods/disco_sovenok/music/benny_hill.mp3"
    $ ds_evading = "mods/disco_sovenok/music/soviet_connection.mp3"
    $ ds_ussr_anthem = "mods/disco_sovenok/music/ussr_anthem.mp3"
    $ ds_workout = "mods/disco_sovenok/music/marafonec.mp3"
    $ ds_papers_please = "mods/disco_sovenok/music/Papers_Please.mp3"
    $ ds_old_camp = "mods/disco_sovenok/music/british-sea-power-the-doomed-commercial-area.ogg"
    $ ds_drinking = "mods/disco_sovenok/music/ryumka_vodki.ogg"
    $ ds_endgame = "mods/disco_sovenok/music/Wolfgang-Amadeus-Mozart-Requiem-Mass-in-D-Minor_-K626_-VIII.-Lacrimosa.ogg"
    $ ds_goodend_dv = "mods/disco_sovenok/music/27-Off-We-Go-Into-The-Wild-Pale-Yonder.ogg"
    $ ds_goodend_mi_jp = "mods/disco_sovenok/music/goluboy_vagon.ogg"
    $ ds_goodend_un = "mods/disco_sovenok/music/yanderesong.ogg"
    $ ds_church_theme = "mods/disco_sovenok/music/church_theme.mp3"

    $ ds_mi_piano_1 = "mods/disco_sovenok/music/mi_piano_1.mp3"
    $ ds_mi_piano_2 = "mods/disco_sovenok/music/mi_piano_2.mp3"
    $ ds_mi_piano_3 = "mods/disco_sovenok/music/mi_piano_3.mp3"
    $ ds_mi_piano_4 = "mods/disco_sovenok/music/mi_piano_4.mp3"
    $ ds_mi_piano_5 = "mods/disco_sovenok/music/mi_piano_5.mp3"

## SFX

    $ ds_check_success = "mods/disco_sovenok/sound/check-success.ogg"
    $ ds_check_failure = "mods/disco_sovenok/sound/check-failure.ogg"
    $ ds_sfx_int = "mods/disco_sovenok/sound/intellect.ogg"
    $ ds_sfx_psy = "mods/disco_sovenok/sound/psyche.ogg"
    $ ds_sfx_fys = "mods/disco_sovenok/sound/physique.ogg"
    $ ds_sfx_mot = "mods/disco_sovenok/sound/motorics.ogg"

    $ ds_crash = "mods/disco_sovenok/sound/car_crash_7dl.ogg"
    $ ds_train_horn = "mods/disco_sovenok/sound/train_horn_7dl.ogg"
    $ ds_train = "mods/disco_sovenok/sound/train_income_7dl.ogg"
    $ ds_un_scream = "mods/disco_sovenok/sound/kriklol.ogg"
    $ ds_stamp = "mods/disco_sovenok/sound/stamp.mp3"
    $ ds_mi_sign = "mods/disco_sovenok/sound/paper_on_wood.mp3"
    $ ds_pen = "mods/disco_sovenok/sound/pismo-ruchkoj.mp3"
    $ ds_fall = "mods/disco_sovenok/sound/bodyfall_7dl.ogg"

    $ ds_btn_click = "mods/disco_sovenok/sound/click.mp3"
    $ ds_selection = "mods/disco_sovenok/sound/selection.mp3"

    $ ds_ambience_train = "mods/disco_sovenok/ambience/train_depart_7dl.ogg"
    $ ds_ambience_shower = "mods/disco_sovenok/ambience/ambience_showers_7dl.ogg"
    $ ds_ambience_spb_weather = "mods/disco_sovenok/ambience/spb_weather.mp3"

    $ ds_electrocution = "mods/disco_sovenok/sound/electrocution.mp3"

    $ ds_alert = "mods/disco_sovenok/sound/alert.mp3"
    $ ds_bombing = "mods/disco_sovenok/sound/bombing.mp3"

    $ ds_things_fall = "mods/disco_sovenok/sound/things_fall.mp3"

    $ ds_auto_ignite = "mods/disco_sovenok/sound/auto_roar_7dl.ogg"

# Спрайты

## Кубики

    image first_dice dice1 = Transform(Image("mods/disco_sovenok/sprite/dices/1.png"), anchor=(1.0, 0.0), pos=(0.48, 0.5))
    image first_dice dice2 = Transform(Image("mods/disco_sovenok/sprite/dices/2.png"), anchor=(1.0, 0.0), pos=(0.48, 0.5))
    image first_dice dice3 = Transform(Image("mods/disco_sovenok/sprite/dices/3.png"), anchor=(1.0, 0.0), pos=(0.48, 0.5))
    image first_dice dice4 = Transform(Image("mods/disco_sovenok/sprite/dices/4.png"), anchor=(1.0, 0.0), pos=(0.48, 0.5))
    image first_dice dice5 = Transform(Image("mods/disco_sovenok/sprite/dices/5.png"), anchor=(1.0, 0.0), pos=(0.48, 0.5))
    image first_dice dice6 = Transform(Image("mods/disco_sovenok/sprite/dices/6.png"), anchor=(1.0, 0.0), pos=(0.48, 0.5))

    image second_dice dice1 = Transform(Image("mods/disco_sovenok/sprite/dices/1.png"), anchor=(0.0, 0.0), pos=(0.52, 0.5))
    image second_dice dice2 = Transform(Image("mods/disco_sovenok/sprite/dices/2.png"), anchor=(0.0, 0.0), pos=(0.52, 0.5))
    image second_dice dice3 = Transform(Image("mods/disco_sovenok/sprite/dices/3.png"), anchor=(0.0, 0.0), pos=(0.52, 0.5))
    image second_dice dice4 = Transform(Image("mods/disco_sovenok/sprite/dices/4.png"), anchor=(0.0, 0.0), pos=(0.52, 0.5))
    image second_dice dice5 = Transform(Image("mods/disco_sovenok/sprite/dices/5.png"), anchor=(0.0, 0.0), pos=(0.52, 0.5))
    image second_dice dice6 = Transform(Image("mods/disco_sovenok/sprite/dices/6.png"), anchor=(0.0, 0.0), pos=(0.52, 0.5))

## Расширение персонажей

    image ag = DSSprite(
        id='ag',
        emotions=[
            ['ok', 'grin', 'happy', 'normal', 'surprise'],
            ['angry', 'rage', 'normal', 'shocked', 'tired']
        ],
        outfits=[ 'casual' ],
        dist=[ 'far' ]
    )

    image ar = DSSprite(
        id='ar',
        emotions=[
            ['dontlike2', 'laugh', 'laugh2', 'normal', 'smile'],
            ['dontlike', 'sad']
        ]
    )

    image cs = DSSprite(
        id='cs',
        emotions=[
            ['angry', 'badgirl', 'cry', 'dontlike', 'doubt', 'grin', 'irritated', 'laugh', 'normal', 'rage', 'sad', 'scared', 'serious', 'shy', 'smile', 'sorrow', 'tired', 'upset']
        ],
        outfits=['civil', 'civil2', 'dress', 'medic1', 'medic2', 'medic3', 'medic4', 'naked', 'panties', 'swim', 'underwear'],
        acc=['glasses', 'stethoscope', 'umbrella'],
        overrides={
            (None, 'medic1', 'glasses'): ('medic1', None, None, 'glasses2'),
            (None, 'medic1', None): ('medic1', None, None, None),
            (None, 'medic2', None): ('medic2', None, None, None),
            (None, 'medic3', None): ('medic3', None, None, None),
            (None, 'medic4', None): ('medic4', None, None, None),
        }
    )

    image dn = DSSprite(
        id='dn',
        emotions=[
            ['dontcare', 'grin', 'normal', 'smile', 'unsure'],
            ['dontlike', 'upset'],
            ['sad', 'scared', 'shocked', 'sick', 'surprise']
        ],
        outfits=['pioneer'],
        naked=['pioneer']
    )

    image dv = DSSprite(
        id='dv',
        emotions=[
            ['concent', 'cry', 'evil_smile', 'scared', 'shocked', 'surprise', 'think'],
            ['grin', 'think2'],
            ['closed_eyes', 'cry_smile', 'guilty', 'sad', 'shy'],
            ['dontlike', 'laugh', 'normal', 'sad2', 'shy2', 'smile', 'soft_smile', 'tired'],
            ['angry', 'rage']
        ],
        outfits=['casual', 'dress', 'modern', 'naked', 'pioneer', 'pioneer2', 'raincoat', 'sport1', 'sport2', 'swim', 'underwear', 'winter'],
        dist=['close', 'far']
    )

    image dvk = DSSprite(
        id='dvk',
        emotions=[
            ['dontlike', 'happy', 'normal', 'smile', 'surprise'],
            ['angry'],
            ['guilty', 'sad', 'sad2', 'shy']
        ],
        outfits=['casual', 'dress']
    )

    image dvw = DSSprite(
        id='dvw',
        emotions=[
            ['laugh', 'normal', 'rage', 'smile'],
        ],
        overrides={
            ('rage', None, None): ('rage', None, None, None),
            (None, None, None): ('normal', None, None, None)
        }
    )

    image el = DSSprite(
        id='el',
        emotions=[
            ['grin', 'normal', 'smile'],
            ['fingal', 'sad', 'scared', 'shocked', 'surprise', 'upset'],
            ['angry', 'laugh', 'serious']
        ],
        outfits=['modern', 'naked', 'pioneer'],
        dist=['close', 'far'],
        overrides={
            (None, 'modern', None): (None, None, 'shirt_black', None),
        }
    )

    image fz = DSSprite(
        id='ba',
        emotions=[
            ['angry', 'normal', 'rage', 'serious', 'smile']
        ],
        outfits=['uniform']
    )

    image gb = DSSprite(
        id='gb',
        emotions=[
            ['calm', 'normal', 'sorrow', 'unsure'],
            ['dontlike', 'sigh', 'smile', 'treat'],
            ['angry', 'pain', 'sad', 'scared'],
        ],
        dist=['close', 'far']
    )

    image ck = DSSprite(
        id='ma',
        emotions=[
            ['laugh', 'normal', 'sad', 'serious', 'smile']
        ],
        outfits=['uniform'],
        dist=['close', 'far']
    )

    image mi = DSSprite(
        id='mi',
        emotions=[
            ['cry', 'dontlike', 'guilty', 'laugh', 'pity', 'scared', 'shocked', 'shy', 'surprise', 'unsure'],
            ['cry_smile', 'grin', 'happy', 'pity_grin', 'pity_smile', 'sad_smile', 'sad', 'smile'],
            ['angry', 'charmed', 'confused', 'despair', 'joy', 'normal', 'rage', 'serious', 'tender', 'upset', 'yawn']
        ],
        outfits=['casual', 'civil', 'naked', 'pioneer', 'sport', 'underwear'],
        dist=['close', 'far']
    )

    image mt = DSSprite(
        id='mt',
        emotions=[
            ['normal', 'sad', 'smile', 'surprise'],
            ['angry', 'rage', 'shocked'],
            ['grin', 'laugh', 'scared']
        ],
        outfits=['dress', 'naked', 'night', 'pioneer', 'swim'],
        acc=['panama'],
        dist=['close', 'far']
    )

    image mz = DSSprite(
        id='mz',
        emotions=[
            ['amazed', 'bukal', 'fun', 'hope', 'laugh', 'normal', 'sad', 'sceptic'],
            ['angry', 'cry', 'rage', 'shyangry', 'smile'],
            ['confused', 'excitement', 'shy']
        ],
        outfits=['naked', 'pioneer', 'pullover', 'swim'],
        acc=['glasses'],
        dist=['close', 'far']
    )

    image sh = DSSprite(
        id='sh',
        emotions=[
            ['laugh', 'scared', 'smile', 'upset'],
            ['cry', 'rage', 'smile2'],
            ['normal', 'serious', 'surprise']
        ],
        outfits=['bathrobe', 'pioneer', 'shirt', 'towel'],
        acc=['red_nose'],
        dist=['close', 'far'],
        naked=['towel']
    )

    image sl = DSSprite(
        id='sl',
        emotions=[
            ['dontlike', 'involve', 'normal', 'serious', 'smile'],
            ['happy', 'laugh', 'shy', 'shy2', 'shy3', 'smile2', 'tricky', 'tricky2'],
            ['angry', 'cry_smile', 'happy2', 'obsessed', 'sad', 'shy4', 'smile3'],
            ['scared', 'scared2', 'tender', 'tender2']
        ],
        outfits=['casual', 'dress', 'naked', 'pioneer', 'sport'],
        dist=['close', 'far']
    )

    image ul = DSSprite(
        id='ul',
        emotions=[
            ['angry', 'normal', 'sad'],
            ['dontlike', 'grin', 'guilty'],
            ['serious', 'smile', 'surprise']
        ],
        outfits=['bunny', 'dress', 'pioneer', 'swim'],
        naked=['swim'],
        dist=['close', 'far']
    )

    image un = DSSprite(
        id='un',
        emotions=[
            ['angry', 'evil_grin', 'evil_laugh', 'evil_smile', 'evil_surprise', 'evil', 'hysteric', 'normal', 'shy_smile', 'shy_smile2', 'shy', 'shy2', 'smile', 'smile2', 'sorrow'],
            ['cry_smile', 'cry', 'cry2', 'cry3', 'sad', 'scared', 'shocked', 'surprise'],
            ['angry2', 'grin', 'laugh', 'rage', 'serious', 'smile3']
        ],
        outfits=['modern', 'dress', 'naked', 'pioneer', 'sleep', 'swim', 'underwear'],
        acc=['closed_eyes'],
        dist=['close', 'far'],
        overrides={
            (None, 'modern', None): (None, None, 'designer', None)
        }
    )

    image uv = DSSprite(
        id='uv',
        emotions=[
            ['dontlike', 'rage', 'sad', 'shocked'],
            ['normal', 'smile'],
            ['grin', 'laugh', 'surprise2'],
            ['guilty', 'surprise', 'upset']
        ],
        outfits=['dress', 'naked'],
        dist=['close', 'far'],
        overrides={
            (None, 'dress', None): (None, None, 'pioneer', None)
        }
    )

    image vt = DSSprite(
        id='vt',
        emotions=[
            ['angry', 'rage', 'shy'],
            ['normal', 'sad', 'smile'],
            ['laugh', 'scared']
        ],
        outfits=['pioneer', 'shirt', 'swim'],
        naked=['swim']
    )

    image yn = DSSprite(
        id='ya',
        emotions=[
            ['guilty', 'happy', 'normal', 'sad', 'shy', 'shy2', 'smile2', 'surprise'],
            ['happy2', 'laugh', 'smile']
        ],
        outfits=['dress', 'naked', 'pioneer'],
        dist=['close', 'far'],
        overrides={
            ('normal', None, None): (None, 'sad', None, None),
            ('sad', None, None): (None, 'verysad', None, None),
            ('shy2', None, None): (None, 'veryshy', None, None),
            ('smile2', None, None): (None, 'normal', None, None)
        }
    )

## Сны Семёна

    image piw normal = "mods/disco_sovenok/sprite/normal/piw/qq.png"

    image sub arb = ds_define_sprite('undv', '', body_num=5)
    image sub lim = ds_define_sprite('undv', '', body_num=1)
    image sub trs = ds_define_sprite('undv', '', body_num=4)

# Эффекты

    ## Бросок кубиков
    image roll = SnowBlossom("mods/disco_sovenok/sprite/strip.png", count=100, xspeed=-150, fast=True)
    image check success = Transform(Image("mods/disco_sovenok/bg/success.png"), alpha=0.3)
    image check failure = Transform(Image("mods/disco_sovenok/bg/failure.png"), alpha=0.3)
    image health damage = "mods/disco_sovenok/bg/health_damage.png"
    image morale damage = "mods/disco_sovenok/bg/morale_damage.png"
    image health up = "mods/disco_sovenok/bg/health_up.png"
    image morale up = "mods/disco_sovenok/bg/morale_up.png"
    image health restore = "mods/disco_sovenok/bg/health_restore.png"
    image morale restore = "mods/disco_sovenok/bg/morale_restore.png"
    
## Документы
'''
    image passport dv = im.Composite(
        (520, 648),
        (0, 0), "mods/disco_sovenok/sprite/papers/PassportInnerObristan.png",
        (30, 390), Text("ДВАЧЕВСКАЯ АЛИСА", size=30, color="#000000"),
        (115, 435), Text("03.04.1972", size=30, color="#000000"),
        (115, 470), Text("Ж", size=30, color="#000000"),
        (115, 505), Text("СКАЛ", size=30, color="#000000"),
        (115, 505), Text("19.01.2009", size=30, color="#000000"),
        (40, 580), Text("ZUN2C-DER07", size=30, color="#000000"),
        (335, 430), Image("mods/disco_sovenok/sprite/papers/dv_photo.png")
    )
    image passport dv approved = im.Composite(
        (520, 648),
        (0, 0), "passport dv",
        (115, 90), Image("mods/disco_sovenok/sprite/papers/EntryGranted.png")
    )
    image passport dv denied = im.Composite(
        (520, 648),
        (0, 0), "passport dv",
        (115, 90), Image("mods/disco_sovenok/sprite/papers/EntryDenied.png")
    )

    image passport un = im.Composite(
        (520, 648),
        (0, 0), "mods/disco_sovenok/sprite/papers/PassportInnerKolechia.png",
        (40, 380), Text("УНЫЛОВА ЛЕНА", size=30, color="#000000"),
        (270, 435), Text("25.09.1972", size=30, color="#000000"),
        (115, 470), Text("Ж", size=30, color="#000000"),
        (115, 505), Text("ЗАП. ГРЕШТИН", size=30, color="#000000"),
        (115, 505), Text("21.12.2013", size=30, color="#000000"),
        (200, 585), Text("YAN22-IICH0", size=30, color="#000000"),
        (30, 430), Image("mods/disco_sovenok/sprite/papers/un_photo.png")
    )
    image passport un approved = im.Composite(
        (520, 648),
        (0, 0), "passport un",
        (115, 90), Image("mods/disco_sovenok/sprite/papers/EntryGranted.png")
    )
    image passport un denied = im.Composite(
        (520, 648),
        (0, 0), "passport un",
        (115, 90), Image("mods/disco_sovenok/sprite/papers/EntryDenied.png")
    )

    image passport sl = im.Composite(
        (520, 648),
        (0, 0), "mods/disco_sovenok/sprite/papers/PassportInnerRepublia.png",
        (30, 340), Text("ФЕОКТИСТОВА СЛАВЯНА", size=30, color="#000000"),
        (100, 395), Text("12.05.1972", size=30, color="#000000"),
        (100, 430), Text("Ж", size=30, color="#000000"),
        (100, 460), Text("СТ. ГЛОРИАН", size=30, color="#000000"),
        (100, 495), Text("29.12.1989", size=30, color="#000000"),
        (30, 585), Text("B2C07-NAKAA", size=30, color="#000000"),
        (340, 385), Image("mods/disco_sovenok/sprite/papers/sl_photo.png")
    )
    image passport sl approved = im.Composite(
        (520, 648),
        (0, 0), "passport sl",
        (115, 90), Image("mods/disco_sovenok/sprite/papers/EntryGranted.png")
    )
    image passport sl denied = im.Composite(
        (520, 648),
        (0, 0), "passport sl",
        (115, 90), Image("mods/disco_sovenok/sprite/papers/EntryDenied.png")
    )

    image passport mi = im.Composite(
        (520, 648),
        (0, 0), "mods/disco_sovenok/sprite/papers/PassportInnerImpor.png",
        (30, 335), Text("ХАЦУНЕ МИКУ", size=30, color="#000000"),
        (270, 390), Text("31.08.1972", size=30, color="#000000"),
        (270, 430), Text("Ж", size=30, color="#000000"),
        (270, 460), Text("ЦУНКЕЙДО", size=30, color="#000000"),
        (270, 495), Text("20.05.2010", size=30, color="#000000"),
        (195, 580), Text("VOCAL-OID01", size=30, color="#000000"),
        (40, 385), Image("mods/disco_sovenok/sprite/papers/mi_photo.png")
    )
    image passport mi approved = im.Composite(
        (520, 648),
        (0, 0), "passport mi",
        (115, 90), Image("mods/disco_sovenok/sprite/papers/EntryGranted.png")
    )
    image passport mi denied = im.Composite(
        (520, 648),
        (0, 0), "passport mi",
        (115, 90), Image("mods/disco_sovenok/sprite/papers/EntryDenied.png")
    )
'''
