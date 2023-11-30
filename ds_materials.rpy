# ОПИСАНИЕ МАТЕРИАЛОВ, НЕОБХОДИМЫХ ДЛЯ РАБОТЫ МОДА

init python:
    from random import randint

    class DSSkillcheckRes:
        def __init__(self, skill, level, threshold, dices, modifiers, result):
            self.skill = skill
            self.level = level
            self.threshold = threshold
            self.dices = dices
            self.applied_modifiers = modifiers
            self.result = result
            self.show = True
        
        def total_points(self):
            points = self.level + self.dices[0] + self.dices[1]
            for modifier in self.applied_modifiers:
                points += modifier[1]
            return points
        
        def hide(self):
            self.show = False
        
        def need_show(self):
            return self.show

    ds_skill_list = {
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

    ds_show_check_result = 0

    # Функция, организующая проверки
    def skillcheck(skill, threshold, passive=False, modifiers=[]):
        global ds_last_skillcheck
        global ds_show_check_result
        dices = [1, 2, 3, 4, 5, 6]
        first_dice = renpy.random.choice(dices)
        second_dice = renpy.random.choice(dices)
        points = ds_get_total_skill(skill)
        applied_modifiers = []
        for variable, bonus, label in modifiers:
            if eval(variable):
                points += bonus
                applied_modifiers.append((variable, bonus, label))
        result = ((first_dice, second_dice) != (1, 1)) and (((first_dice, second_dice) == (6, 6)) or (points + first_dice + second_dice >= threshold))
        if not passive:
            # renpy.show('roll')
            if result:
                renpy.play(ds_check_success, channel='sound')
            else:
                renpy.play(ds_check_failure, channel='sound')
            renpy.pause(delay=1.0, hard=True)
            # renpy.hide('roll')
            if result:
                renpy.show('check success')
            else:
                renpy.show('check failure')
            renpy.show("first_dice dice" + str(first_dice))
            renpy.show("second_dice dice" + str(second_dice))
            renpy.pause(delay=1.0)
            renpy.hide('check')
            renpy.hide('first_dice')
            renpy.hide('second_dice')
        ds_last_skillcheck = DSSkillcheckRes(skill, ds_get_total_skill(skill), threshold, (first_dice, second_dice), applied_modifiers, result)
        ds_show_check_result = 2
        return result

    def ds_up_skill(skill, points):
        global ds_xp
        global ds_skill_points
        ds_xp[skill] += points
        while ds_xp[skill] >= 100:
            ds_skill_points[skill] += 1
            ds_xp[skill] -= 100

    def ds_damage_health(go_if_zero='ds_end_out_of_health'):
        global ds_health
        ds_health -= 1
        renpy.show('health damage', at_list=[show_damage])
        renpy.pause(1.5)
        renpy.hide('health')
        if ds_health <= 0:
            ui.jumps(go_if_zero)
    
    def ds_damage_morale(go_if_zero='ds_end_out_of_morale'):
        global ds_morale
        ds_morale -= 1
        renpy.show('morale damage', at_list=[show_damage])
        renpy.pause(1.5)
        renpy.hide('morale')
        if ds_morale <= 0:
            ui.jumps(go_if_zero)
    
    def ds_up_health():
        global ds_health
        if ds_health < 0:
            ds_health += 1
        renpy.show('health up')
        renpy.with_statement(wiperight)
        renpy.pause(1.5)
        renpy.hide('health')
        renpy.with_statement(wiperight)
    
    def ds_up_morale():
        global ds_morale
        if ds_morale < 0:
            ds_morale += 1
        renpy.show('morale up')
        renpy.with_statement(wiperight)
        renpy.pause(1.5)
        renpy.hide('morale')
        renpy.with_statement(wiperight)
    
    def ds_restore_health():
        global ds_health
        ds_health = 0
        renpy.show('health restore')
        renpy.with_statement(wiperight)
        renpy.pause(1.5)
        renpy.hide('health')
        renpy.with_statement(wiperight)
    
    def ds_restore_morale():
        global ds_morale
        ds_morale = 0
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

    def ds_get_total_skill(skill):
        result = ds_skill_points[skill]
        if skill in ['logic', 'encyclopedia', 'rhetoric', 'drama', 'conceptualization', 'visual_calculus']:
            if ds_member['library']:
                result += 1
        if skill in ['volition', 'inland_empire', 'authority', 'empathy', 'esprit', 'suggestion']:
            if ds_member['music']:
                result += 1
        if skill in ['endurance', 'pain_threshold', 'physical_instrument', 'instinct', 'shivers', 'half_light']:
            if ds_member['sport']:
                result += 1
        if skill in ['perception', 'coordination', 'reaction_speed', 'savoir_faire', 'interfacing', 'composure']:
            if ds_member['cyber']:
                result += 1
        if skill == 'endurance':
            result += ds_health
        if skill == 'volition':
            result += ds_morale
        if not (skill in ['volition', 'authority', 'suggestion', 'composure']):
            return result
        if ds_semtype >= 3:
            result += 1
        elif ds_semtype <= -3:
            result -= 1
        return result

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

# Переменные
    default ds_menuset = set()

## Значения атрибутов
    default ds_skill_points = {
        'logic': 0,
        'encyclopedia': 0,
        'rhetoric': 0,
        'drama': 0,
        'conceptualization': 0,
        'visual_calculus': 0,
        'volition': 0,
        'inland_empire': 0,
        'authority': 0,
        'empathy': 0,
        'esprit': 0,
        'suggestion': 0,
        'endurance': 0,
        'pain_threshold': 0,
        'physical_instrument': 0,
        'instinct': 0,
        'shivers': 0,
        'half_light': 0,
        'perception': 0,
        'coordination': 0,
        'reaction_speed': 0,
        'savoir_faire': 0,
        'interfacing': 0,
        'composure': 0
    }

    default ds_xp = {
        'logic': 0,
        'encyclopedia': 0,
        'rhetoric': 0,
        'drama': 0,
        'conceptualization': 0,
        'visual_calculus': 0,
        'volition': 0,
        'inland_empire': 0,
        'authority': 0,
        'empathy': 0,
        'esprit': 0,
        'suggestion': 0,
        'endurance': 0,
        'pain_threshold': 0,
        'physical_instrument': 0,
        'instinct': 0,
        'shivers': 0,
        'half_light': 0,
        'perception': 0,
        'coordination': 0,
        'reaction_speed': 0,
        'savoir_faire': 0,
        'interfacing': 0,
        'composure': 0
    }

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
        'ya': 0
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
        'ya': 0
    }

## Общие параметры
    default ds_karma = 0 # Репутация - насколько хорошо себя ведёт ГГ
    default ds_health = 0 # Здоровье
    default ds_morale = 0 # Боевой дух
    default ds_archetype = 0 # Избранный персонаж
    default ds_knowing = 0 # Знание
    default ds_semtype = 0 # Тип Семёна
    default ds_homo_traits = 0

    $ ds_game_started = False

    default ds_last_skillcheck = None # Результат последней проверки (позволяет сделать появление новых опций с проверками без ввода дополнительных переменных)

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
    $ yap = Character (u'Девушка', color="74b05f", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ ya = Character (u'Яна', color="74b05f", ctc="ctc_animation", ctc_position="fixed", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
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

    # Виола
    image cs angry naked = ds_define_sprite('cs', 'angry')
    image cs badgirl naked = ds_define_sprite('cs', 'badgirl')
    image cs cry naked = ds_define_sprite('cs', 'cry')
    image cs dontlike naked = ds_define_sprite('cs', 'dontlike')
    image cs doubt naked = ds_define_sprite('cs', 'doubt')
    image cs grin naked = ds_define_sprite('cs', 'grin')
    image cs irritated naked = ds_define_sprite('cs', 'irritated')
    image cs laugh naked = ds_define_sprite('cs', 'laugh')
    image cs normal naked = ds_define_sprite('cs', 'normal')
    image cs rage naked = ds_define_sprite('cs', 'rage')
    image cs sad naked = ds_define_sprite('cs', 'sad')
    image cs scared naked = ds_define_sprite('cs', 'scared')
    image cs serious naked = ds_define_sprite('cs', 'serious')
    image cs shy naked = ds_define_sprite('cs', 'shy')
    image cs smile naked = ds_define_sprite('cs', 'smile')
    image cs sorrow naked = ds_define_sprite('cs', 'sorrow')
    image cs tired naked = ds_define_sprite('cs', 'tired')
    image cs upset naked = ds_define_sprite('cs', 'upset')

    image cs angry panties = ds_define_sprite('cs', 'angry', body_name='panties')
    image cs badgirl panties = ds_define_sprite('cs', 'badgirl', body_name='panties')
    image cs cry panties = ds_define_sprite('cs', 'cry', body_name='panties')
    image cs dontlike panties = ds_define_sprite('cs', 'dontlike', body_name='panties')
    image cs doubt panties = ds_define_sprite('cs', 'doubt', body_name='panties')
    image cs grin panties = ds_define_sprite('cs', 'grin', body_name='panties')
    image cs irritated panties = ds_define_sprite('cs', 'irritated', body_name='panties')
    image cs laugh panties = ds_define_sprite('cs', 'laugh', body_name='panties')
    image cs normal panties = ds_define_sprite('cs', 'normal', body_name='panties')
    image cs rage panties = ds_define_sprite('cs', 'rage', body_name='panties')
    image cs sad panties = ds_define_sprite('cs', 'sad', body_name='panties')
    image cs scared panties = ds_define_sprite('cs', 'scared', body_name='panties')
    image cs serious panties = ds_define_sprite('cs', 'serious', body_name='panties')
    image cs shy panties = ds_define_sprite('cs', 'shy', body_name='panties')
    image cs smile panties = ds_define_sprite('cs', 'smile', body_name='panties')
    image cs sorrow panties = ds_define_sprite('cs', 'sorrow', body_name='panties')
    image cs tired panties = ds_define_sprite('cs', 'tired', body_name='panties')
    image cs upset panties = ds_define_sprite('cs', 'upset', body_name='panties')

    image cs angry medic1 = ds_define_sprite('cs', 'angry', body_name='medic1')
    image cs badgirl medic1 = ds_define_sprite('cs', 'badgirl', body_name='medic1')
    image cs cry medic1 = ds_define_sprite('cs', 'cry', body_name='medic1')
    image cs dontlike medic1 = ds_define_sprite('cs', 'dontlike', body_name='medic1')
    image cs doubt medic1 = ds_define_sprite('cs', 'doubt', body_name='medic1')
    image cs grin medic1 = ds_define_sprite('cs', 'grin', body_name='medic1')
    image cs irritated medic1 = ds_define_sprite('cs', 'irritated', body_name='medic1')
    image cs laugh medic1 = ds_define_sprite('cs', 'laugh', body_name='medic1')
    image cs normal medic1 = ds_define_sprite('cs', 'normal', body_name='medic1')
    image cs rage medic1 = ds_define_sprite('cs', 'rage', body_name='medic1')
    image cs sad medic1 = ds_define_sprite('cs', 'sad', body_name='medic1')
    image cs scared medic1 = ds_define_sprite('cs', 'scared', body_name='medic1')
    image cs serious medic1 = ds_define_sprite('cs', 'serious', body_name='medic1')
    image cs shy medic1 = ds_define_sprite('cs', 'shy', body_name='medic1')
    image cs smile medic1 = ds_define_sprite('cs', 'smile', body_name='medic1')
    image cs sorrow medic1 = ds_define_sprite('cs', 'sorrow', body_name='medic1')
    image cs tired medic1 = ds_define_sprite('cs', 'tired', body_name='medic1')
    image cs upset medic1 = ds_define_sprite('cs', 'upset', body_name='medic1')

    image cs angry medic2 = ds_define_sprite('cs', 'angry', body_name='medic2')
    image cs badgirl medic2 = ds_define_sprite('cs', 'badgirl', body_name='medic2')
    image cs cry medic2 = ds_define_sprite('cs', 'cry', body_name='medic2')
    image cs dontlike medic2 = ds_define_sprite('cs', 'dontlike', body_name='medic2')
    image cs doubt medic2 = ds_define_sprite('cs', 'doubt', body_name='medic2')
    image cs grin medic2 = ds_define_sprite('cs', 'grin', body_name='medic2')
    image cs irritated medic2 = ds_define_sprite('cs', 'irritated', body_name='medic2')
    image cs laugh medic2 = ds_define_sprite('cs', 'laugh', body_name='medic2')
    image cs normal medic2 = ds_define_sprite('cs', 'normal', body_name='medic2')
    image cs rage medic2 = ds_define_sprite('cs', 'rage', body_name='medic2')
    image cs sad medic2 = ds_define_sprite('cs', 'sad', body_name='medic2')
    image cs scared medic2 = ds_define_sprite('cs', 'scared', body_name='medic2')
    image cs serious medic2 = ds_define_sprite('cs', 'serious', body_name='medic2')
    image cs shy medic2 = ds_define_sprite('cs', 'shy', body_name='medic2')
    image cs smile medic2 = ds_define_sprite('cs', 'smile', body_name='medic2')
    image cs sorrow medic2 = ds_define_sprite('cs', 'sorrow', body_name='medic2')
    image cs tired medic2 = ds_define_sprite('cs', 'tired', body_name='medic2')
    image cs upset medic2 = ds_define_sprite('cs', 'upset', body_name='medic2')

    image cs angry medic3 = ds_define_sprite('cs', 'angry', body_name='medic3')
    image cs badgirl medic3 = ds_define_sprite('cs', 'badgirl', body_name='medic3')
    image cs cry medic3 = ds_define_sprite('cs', 'cry', body_name='medic3')
    image cs dontlike medic3 = ds_define_sprite('cs', 'dontlike', body_name='medic3')
    image cs doubt medic3 = ds_define_sprite('cs', 'doubt', body_name='medic3')
    image cs grin medic3 = ds_define_sprite('cs', 'grin', body_name='medic3')
    image cs irritated medic3 = ds_define_sprite('cs', 'irritated', body_name='medic3')
    image cs laugh medic3 = ds_define_sprite('cs', 'laugh', body_name='medic3')
    image cs normal medic3 = ds_define_sprite('cs', 'normal', body_name='medic3')
    image cs rage medic3 = ds_define_sprite('cs', 'rage', body_name='medic3')
    image cs sad medic3 = ds_define_sprite('cs', 'sad', body_name='medic3')
    image cs scared medic3 = ds_define_sprite('cs', 'scared', body_name='medic3')
    image cs serious medic3 = ds_define_sprite('cs', 'serious', body_name='medic3')
    image cs shy medic3 = ds_define_sprite('cs', 'shy', body_name='medic3')
    image cs smile medic3 = ds_define_sprite('cs', 'smile', body_name='medic3')
    image cs sorrow medic3 = ds_define_sprite('cs', 'sorrow', body_name='medic3')
    image cs tired medic3 = ds_define_sprite('cs', 'tired', body_name='medic3')
    image cs upset medic3 = ds_define_sprite('cs', 'upset', body_name='medic3')

    image cs angry medic4 = ds_define_sprite('cs', 'angry', body_name='medic4')
    image cs badgirl medic4 = ds_define_sprite('cs', 'badgirl', body_name='medic4')
    image cs cry medic4 = ds_define_sprite('cs', 'cry', body_name='medic4')
    image cs dontlike medic4 = ds_define_sprite('cs', 'dontlike', body_name='medic4')
    image cs doubt medic4 = ds_define_sprite('cs', 'doubt', body_name='medic4')
    image cs grin medic4 = ds_define_sprite('cs', 'grin', body_name='medic4')
    image cs irritated medic4 = ds_define_sprite('cs', 'irritated', body_name='medic4')
    image cs laugh medic4 = ds_define_sprite('cs', 'laugh', body_name='medic4')
    image cs normal medic4 = ds_define_sprite('cs', 'normal', body_name='medic4')
    image cs rage medic4 = ds_define_sprite('cs', 'rage', body_name='medic4')
    image cs sad medic4 = ds_define_sprite('cs', 'sad', body_name='medic4')
    image cs scared medic4 = ds_define_sprite('cs', 'scared', body_name='medic4')
    image cs serious medic4 = ds_define_sprite('cs', 'serious', body_name='medic4')
    image cs shy medic4 = ds_define_sprite('cs', 'shy', body_name='medic4')
    image cs smile medic4 = ds_define_sprite('cs', 'smile', body_name='medic4')
    image cs sorrow medic4 = ds_define_sprite('cs', 'sorrow', body_name='medic4')
    image cs tired medic4 = ds_define_sprite('cs', 'tired', body_name='medic4')
    image cs upset medic4 = ds_define_sprite('cs', 'upset', body_name='medic4')

    image cs angry medic1 glasses = ds_define_sprite('cs', 'angry', body_name='medic1', acc='glasses2')
    image cs badgirl medic1 glasses = ds_define_sprite('cs', 'badgirl', body_name='medic1', acc='glasses2')
    image cs cry medic1 glasses = ds_define_sprite('cs', 'cry', body_name='medic1', acc='glasses2')
    image cs dontlike medic1 glasses = ds_define_sprite('cs', 'dontlike', body_name='medic1', acc='glasses2')
    image cs doubt medic1 glasses = ds_define_sprite('cs', 'doubt', body_name='medic1', acc='glasses2')
    image cs grin medic1 glasses = ds_define_sprite('cs', 'grin', body_name='medic1', acc='glasses2')
    image cs irritated medic1 glasses = ds_define_sprite('cs', 'irritated', body_name='medic1', acc='glasses2')
    image cs laugh medic1 glasses = ds_define_sprite('cs', 'laugh', body_name='medic1', acc='glasses2')
    image cs normal medic1 glasses = ds_define_sprite('cs', 'normal', body_name='medic1', acc='glasses2')
    image cs rage medic1 glasses = ds_define_sprite('cs', 'rage', body_name='medic1', acc='glasses2')
    image cs sad medic1 glasses = ds_define_sprite('cs', 'sad', body_name='medic1', acc='glasses2')
    image cs scared medic1 glasses = ds_define_sprite('cs', 'scared', body_name='medic1', acc='glasses2')
    image cs serious medic1 glasses = ds_define_sprite('cs', 'serious', body_name='medic1', acc='glasses2')
    image cs shy medic1 glasses = ds_define_sprite('cs', 'shy', body_name='medic1', acc='glasses2')
    image cs smile medic1 glasses = ds_define_sprite('cs', 'smile', body_name='medic1', acc='glasses2')
    image cs sorrow medic1 glasses = ds_define_sprite('cs', 'sorrow', body_name='medic1', acc='glasses2')
    image cs tired medic1 glasses = ds_define_sprite('cs', 'tired', body_name='medic1', acc='glasses2')
    image cs upset medic1 glasses = ds_define_sprite('cs', 'upset', body_name='medic1', acc='glasses2')

    image cs angry medic2 glasses = ds_define_sprite('cs', 'angry', body_name='medic2', acc='glasses')
    image cs badgirl medic2 glasses = ds_define_sprite('cs', 'badgirl', body_name='medic2', acc='glasses')
    image cs cry medic2 glasses = ds_define_sprite('cs', 'cry', body_name='medic2', acc='glasses')
    image cs dontlike medic2 glasses = ds_define_sprite('cs', 'dontlike', body_name='medic2', acc='glasses')
    image cs doubt medic2 glasses = ds_define_sprite('cs', 'doubt', body_name='medic2', acc='glasses')
    image cs grin medic2 glasses = ds_define_sprite('cs', 'grin', body_name='medic2', acc='glasses')
    image cs irritated medic2 glasses = ds_define_sprite('cs', 'irritated', body_name='medic2', acc='glasses')
    image cs laugh medic2 glasses = ds_define_sprite('cs', 'laugh', body_name='medic2', acc='glasses')
    image cs normal medic2 glasses = ds_define_sprite('cs', 'normal', body_name='medic2', acc='glasses')
    image cs rage medic2 glasses = ds_define_sprite('cs', 'rage', body_name='medic2', acc='glasses')
    image cs sad medic2 glasses = ds_define_sprite('cs', 'sad', body_name='medic2', acc='glasses')
    image cs scared medic2 glasses = ds_define_sprite('cs', 'scared', body_name='medic2', acc='glasses')
    image cs serious medic2 glasses = ds_define_sprite('cs', 'serious', body_name='medic2', acc='glasses')
    image cs shy medic2 glasses = ds_define_sprite('cs', 'shy', body_name='medic2', acc='glasses')
    image cs smile medic2 glasses = ds_define_sprite('cs', 'smile', body_name='medic2', acc='glasses')
    image cs sorrow medic2 glasses = ds_define_sprite('cs', 'sorrow', body_name='medic2', acc='glasses')
    image cs tired medic2 glasses = ds_define_sprite('cs', 'tired', body_name='medic2', acc='glasses')
    image cs upset medic2 glasses = ds_define_sprite('cs', 'upset', body_name='medic2', acc='glasses')

    image cs angry medic3 glasses = ds_define_sprite('cs', 'angry', body_name='medic3', acc='glasses')
    image cs badgirl medic3 glasses = ds_define_sprite('cs', 'badgirl', body_name='medic3', acc='glasses')
    image cs cry medic3 glasses = ds_define_sprite('cs', 'cry', body_name='medic3', acc='glasses')
    image cs dontlike medic3 glasses = ds_define_sprite('cs', 'dontlike', body_name='medic3', acc='glasses')
    image cs doubt medic3 glasses = ds_define_sprite('cs', 'doubt', body_name='medic3', acc='glasses')
    image cs grin medic3 glasses = ds_define_sprite('cs', 'grin', body_name='medic3', acc='glasses')
    image cs irritated medic3 glasses = ds_define_sprite('cs', 'irritated', body_name='medic3', acc='glasses')
    image cs laugh medic3 glasses = ds_define_sprite('cs', 'laugh', body_name='medic3', acc='glasses')
    image cs normal medic3 glasses = ds_define_sprite('cs', 'normal', body_name='medic3', acc='glasses')
    image cs rage medic3 glasses = ds_define_sprite('cs', 'rage', body_name='medic3', acc='glasses')
    image cs sad medic3 glasses = ds_define_sprite('cs', 'sad', body_name='medic3', acc='glasses')
    image cs scared medic3 glasses = ds_define_sprite('cs', 'scared', body_name='medic3', acc='glasses')
    image cs serious medic3 glasses = ds_define_sprite('cs', 'serious', body_name='medic3', acc='glasses')
    image cs shy medic3 glasses = ds_define_sprite('cs', 'shy', body_name='medic3', acc='glasses')
    image cs smile medic3 glasses = ds_define_sprite('cs', 'smile', body_name='medic3', acc='glasses')
    image cs sorrow medic3 glasses = ds_define_sprite('cs', 'sorrow', body_name='medic3', acc='glasses')
    image cs tired medic3 glasses = ds_define_sprite('cs', 'tired', body_name='medic3', acc='glasses')
    image cs upset medic3 glasses = ds_define_sprite('cs', 'upset', body_name='medic3', acc='glasses')

    image cs angry medic4 glasses = ds_define_sprite('cs', 'angry', body_name='medic4', acc='glasses')
    image cs badgirl medic4 glasses = ds_define_sprite('cs', 'badgirl', body_name='medic4', acc='glasses')
    image cs cry medic4 glasses = ds_define_sprite('cs', 'cry', body_name='medic4', acc='glasses')
    image cs dontlike medic4 glasses = ds_define_sprite('cs', 'dontlike', body_name='medic4', acc='glasses')
    image cs doubt medic4 glasses = ds_define_sprite('cs', 'doubt', body_name='medic4', acc='glasses')
    image cs grin medic4 glasses = ds_define_sprite('cs', 'grin', body_name='medic4', acc='glasses')
    image cs irritated medic4 glasses = ds_define_sprite('cs', 'irritated', body_name='medic4', acc='glasses')
    image cs laugh medic4 glasses = ds_define_sprite('cs', 'laugh', body_name='medic4', acc='glasses')
    image cs normal medic4 glasses = ds_define_sprite('cs', 'normal', body_name='medic4', acc='glasses')
    image cs rage medic4 glasses = ds_define_sprite('cs', 'rage', body_name='medic4', acc='glasses')
    image cs sad medic4 glasses = ds_define_sprite('cs', 'sad', body_name='medic4', acc='glasses')
    image cs scared medic4 glasses = ds_define_sprite('cs', 'scared', body_name='medic4', acc='glasses')
    image cs serious medic4 glasses = ds_define_sprite('cs', 'serious', body_name='medic4', acc='glasses')
    image cs shy medic4 glasses = ds_define_sprite('cs', 'shy', body_name='medic4', acc='glasses')
    image cs smile medic4 glasses = ds_define_sprite('cs', 'smile', body_name='medic4', acc='glasses')
    image cs sorrow medic4 glasses = ds_define_sprite('cs', 'sorrow', body_name='medic4', acc='glasses')
    image cs tired medic4 glasses = ds_define_sprite('cs', 'tired', body_name='medic4', acc='glasses')
    image cs upset medic4 glasses = ds_define_sprite('cs', 'upset', body_name='medic4', acc='glasses')

    image cs angry civil = ds_define_sprite('cs', 'angry', cloth='civil')
    image cs badgirl civil = ds_define_sprite('cs', 'badgirl', cloth='civil')
    image cs cry civil = ds_define_sprite('cs', 'cry', cloth='civil')
    image cs dontlike civil = ds_define_sprite('cs', 'dontlike', cloth='civil')
    image cs doubt civil = ds_define_sprite('cs', 'doubt', cloth='civil')
    image cs grin civil = ds_define_sprite('cs', 'grin', cloth='civil')
    image cs irritated civil = ds_define_sprite('cs', 'irritated', cloth='civil')
    image cs laugh civil = ds_define_sprite('cs', 'laugh', cloth='civil')
    image cs normal civil = ds_define_sprite('cs', 'normal', cloth='civil')
    image cs rage civil = ds_define_sprite('cs', 'rage', cloth='civil')
    image cs sad civil = ds_define_sprite('cs', 'sad', cloth='civil')
    image cs scared civil = ds_define_sprite('cs', 'scared', cloth='civil')
    image cs serious civil = ds_define_sprite('cs', 'serious', cloth='civil')
    image cs shy civil = ds_define_sprite('cs', 'shy', cloth='civil')
    image cs smile civil = ds_define_sprite('cs', 'smile', cloth='civil')
    image cs sorrow civil = ds_define_sprite('cs', 'sorrow', cloth='civil')
    image cs tired civil = ds_define_sprite('cs', 'tired', cloth='civil')
    image cs upset civil = ds_define_sprite('cs', 'upset', cloth='civil')

    image cs angry civil2 = ds_define_sprite('cs', 'angry', cloth='civil2')
    image cs badgirl civil2 = ds_define_sprite('cs', 'badgirl', cloth='civil2')
    image cs cry civil2 = ds_define_sprite('cs', 'cry', cloth='civil2')
    image cs dontlike civil2 = ds_define_sprite('cs', 'dontlike', cloth='civil2')
    image cs doubt civil2 = ds_define_sprite('cs', 'doubt', cloth='civil2')
    image cs grin civil2 = ds_define_sprite('cs', 'grin', cloth='civil2')
    image cs irritated civil2 = ds_define_sprite('cs', 'irritated', cloth='civil2')
    image cs laugh civil2 = ds_define_sprite('cs', 'laugh', cloth='civil2')
    image cs normal civil2 = ds_define_sprite('cs', 'normal', cloth='civil2')
    image cs rage civil2 = ds_define_sprite('cs', 'rage', cloth='civil2')
    image cs sad civil2 = ds_define_sprite('cs', 'sad', cloth='civil2')
    image cs scared civil2 = ds_define_sprite('cs', 'scared', cloth='civil2')
    image cs serious civil2 = ds_define_sprite('cs', 'serious', cloth='civil2')
    image cs shy civil2 = ds_define_sprite('cs', 'shy', cloth='civil2')
    image cs smile civil2 = ds_define_sprite('cs', 'smile', cloth='civil2')
    image cs sorrow civil2 = ds_define_sprite('cs', 'sorrow', cloth='civil2')
    image cs tired civil2 = ds_define_sprite('cs', 'tired', cloth='civil2')
    image cs upset civil2 = ds_define_sprite('cs', 'upset', cloth='civil2')

    image cs normal naked close = ds_define_sprite('cs', 'normal', dist='close')
    image cs shy naked close = ds_define_sprite('cs', 'shy', dist='close')
    image cs smile naked close = ds_define_sprite('cs', 'smile', dist='close')

    image cs normal panties close = ds_define_sprite('cs', 'normal', body_name='panties', dist='close')
    image cs shy panties close = ds_define_sprite('cs', 'shy', body_name='panties', dist='close')
    image cs smile panties close = ds_define_sprite('cs', 'smile', body_name='panties', dist='close')

    image cs normal medic close = ds_define_sprite('cs', 'normal', body_name='medic', dist='close', acc='glasses')
    image cs shy medic close = ds_define_sprite('cs', 'shy', body_name='medic', dist='close', acc='glasses')
    image cs smile medic close = ds_define_sprite('cs', 'smile', body_name='medic', dist='close', acc='glasses')

    image cs badgirl naked far = ds_define_sprite('cs', 'badgirl', dist='far')
    image cs dontlike naked far = ds_define_sprite('cs', 'dontlike', dist='far')
    image cs doubt naked far = ds_define_sprite('cs', 'doubt', dist='far')
    image cs laugh naked far = ds_define_sprite('cs', 'laugh', dist='far')
    image cs normal naked far = ds_define_sprite('cs', 'normal', dist='far')
    image cs scared naked far = ds_define_sprite('cs', 'scared', dist='far')
    image cs shy naked far = ds_define_sprite('cs', 'shy', dist='far')
    image cs smile naked far = ds_define_sprite('cs', 'smile', dist='far')

    image cs badgirl panties far = ds_define_sprite('cs', 'badgirl', body_name='panties', dist='far')
    image cs dontlike panties far = ds_define_sprite('cs', 'dontlike', body_name='panties', dist='far')
    image cs doubt panties far = ds_define_sprite('cs', 'doubt', body_name='panties', dist='far')
    image cs laugh panties far = ds_define_sprite('cs', 'laugh', body_name='panties', dist='far')
    image cs normal panties far = ds_define_sprite('cs', 'normal', body_name='panties', dist='far')
    image cs scared panties far = ds_define_sprite('cs', 'scared', body_name='panties', dist='far')
    image cs shy panties far = ds_define_sprite('cs', 'shy', body_name='panties', dist='far')
    image cs smile panties far = ds_define_sprite('cs', 'smile', body_name='panties', dist='far')

    image cs badgirl medic far = ds_define_sprite('cs', 'badgirl', body_name='medic', dist='far', acc='glasses')
    image cs dontlike medic far = ds_define_sprite('cs', 'dontlike', body_name='medic', dist='far', acc='glasses')
    image cs doubt medic far = ds_define_sprite('cs', 'doubt', body_name='medic', dist='far', acc='glasses')
    image cs laugh medic far = ds_define_sprite('cs', 'laugh', body_name='medic', dist='far', acc='glasses')
    image cs normal medic far = ds_define_sprite('cs', 'normal', body_name='medic', dist='far', acc='glasses')
    image cs scared medic far = ds_define_sprite('cs', 'scared', body_name='medic', dist='far', acc='glasses')
    image cs shy medic far = ds_define_sprite('cs', 'shy', body_name='medic', dist='far', acc='glasses')
    image cs smile medic far = ds_define_sprite('cs', 'smile', body_name='medic', dist='far', acc='glasses')

    $ ds_define_chars()

## Новые персонажи

    # Повариха
    image ck laugh = ds_define_sprite('ma', 'laugh')
    image ck normal = ds_define_sprite('ma', 'normal')
    image ck sad = ds_define_sprite('ma', 'sad')
    image ck serious = ds_define_sprite('ma', 'serious')
    image ck smile = ds_define_sprite('ma', 'smile')

    image ck laugh close = ds_define_sprite('ma', 'laugh', dist='close')
    image ck normal close = ds_define_sprite('ma', 'normal', dist='close')
    image ck sad close = ds_define_sprite('ma', 'sad', dist='close')
    image ck serious close = ds_define_sprite('ma', 'serious', dist='close')
    image ck smile close = ds_define_sprite('ma', 'smile', dist='close')

    image ck laugh far = ds_define_sprite('ma', 'laugh', dist='far')
    image ck normal far = ds_define_sprite('ma', 'normal', dist='far')
    image ck sad far = ds_define_sprite('ma', 'sad', dist='far')
    image ck serious far = ds_define_sprite('ma', 'serious', dist='far')
    image ck smile far = ds_define_sprite('ma', 'smile', dist='far')

    # Яна
    image ya guilty naked = ds_define_sprite('ya', 'guilty', body_num=1)
    image ya happy naked = ds_define_sprite('ya', 'happy', body_num=1)
    image ya happy2 naked = ds_define_sprite('ya', 'happy2', body_num=2)
    image ya laugh naked = ds_define_sprite('ya', 'laugh', body_num=2)
    image ya normal naked = ds_define_sprite('ya', 'sad', body_num=1)
    image ya sad naked = ds_define_sprite('ya', 'verysad', body_num=1)
    image ya shy naked = ds_define_sprite('ya', 'shy', body_num=1)
    image ya shy2 naked = ds_define_sprite('ya', 'veryshy', body_num=1)
    image ya smile naked = ds_define_sprite('ya', 'smile', body_num=2)
    image ya smile2 naked = ds_define_sprite('ya', 'normal', body_num=1)
    image ya surprise naked = ds_define_sprite('ya', 'surprise', body_num=1)
    image ya guilty pioneer = ds_define_sprite('ya', 'guilty', body_num=1, cloth='pioneer')
    image ya happy pioneer = ds_define_sprite('ya', 'happy', body_num=1, cloth='pioneer')
    image ya happy2 pioneer = ds_define_sprite('ya', 'happy2', body_num=2, cloth='pioneer')
    image ya laugh pioneer = ds_define_sprite('ya', 'laugh', body_num=2, cloth='pioneer')
    image ya normal pioneer = ds_define_sprite('ya', 'sad', body_num=1, cloth='pioneer')
    image ya sad pioneer = ds_define_sprite('ya', 'verysad', body_num=1, cloth='pioneer')
    image ya shy pioneer = ds_define_sprite('ya', 'shy', body_num=1, cloth='pioneer')
    image ya shy2 pioneer = ds_define_sprite('ya', 'veryshy', body_num=1, cloth='pioneer')
    image ya smile pioneer = ds_define_sprite('ya', 'smile', body_num=2, cloth='pioneer')
    image ya smile2 pioneer = ds_define_sprite('ya', 'normal', body_num=1, cloth='pioneer')
    image ya surprise pioneer = ds_define_sprite('ya', 'surprise', body_num=1, cloth='pioneer')
    image ya guilty dress = ds_define_sprite('ya', 'guilty', body_num=1, cloth='dress')
    image ya happy dress = ds_define_sprite('ya', 'happy', body_num=1, cloth='dress')
    image ya happy2 dress = ds_define_sprite('ya', 'happy2', body_num=2, cloth='dress')
    image ya laugh dress = ds_define_sprite('ya', 'laugh', body_num=2, cloth='dress')
    image ya normal dress = ds_define_sprite('ya', 'sad', body_num=1, cloth='dress')
    image ya sad dress = ds_define_sprite('ya', 'verysad', body_num=1, cloth='dress')
    image ya shy dress = ds_define_sprite('ya', 'shy', body_num=1, cloth='dress')
    image ya shy2 dress = ds_define_sprite('ya', 'veryshy', body_num=1, cloth='dress')
    image ya smile dress = ds_define_sprite('ya', 'smile', body_num=2, cloth='dress')
    image ya smile2 dress = ds_define_sprite('ya', 'normal', body_num=1, cloth='dress')
    image ya surprise dress = ds_define_sprite('ya', 'surprise', body_num=1, cloth='dress')

    image ya guilty naked close = ds_define_sprite('ya', 'guilty', body_num=1, dist='close')
    image ya happy naked close = ds_define_sprite('ya', 'happy', body_num=1, dist='close')
    image ya happy2 naked close = ds_define_sprite('ya', 'happy2', body_num=2, dist='close')
    image ya laugh naked close = ds_define_sprite('ya', 'laugh', body_num=2, dist='close')
    image ya normal naked close = ds_define_sprite('ya', 'sad', body_num=1, dist='close')
    image ya sad naked close = ds_define_sprite('ya', 'verysad', body_num=1, dist='close')
    image ya shy naked close = ds_define_sprite('ya', 'shy', body_num=1, dist='close')
    image ya shy2 naked close = ds_define_sprite('ya', 'veryshy', body_num=1, dist='close')
    image ya smile naked close = ds_define_sprite('ya', 'smile', body_num=2, dist='close')
    image ya smile2 naked close = ds_define_sprite('ya', 'normal', body_num=1, dist='close')
    image ya surprise naked close = ds_define_sprite('ya', 'surprise', body_num=1, dist='close')
    image ya guilty pioneer close = ds_define_sprite('ya', 'guilty', body_num=1, cloth='pioneer', dist='close')
    image ya happy pioneer close = ds_define_sprite('ya', 'happy', body_num=1, cloth='pioneer', dist='close')
    image ya happy2 pioneer close = ds_define_sprite('ya', 'happy2', body_num=2, cloth='pioneer', dist='close')
    image ya laugh pioneer close = ds_define_sprite('ya', 'laugh', body_num=2, cloth='pioneer', dist='close')
    image ya normal pioneer close = ds_define_sprite('ya', 'sad', body_num=1, cloth='pioneer', dist='close')
    image ya sad pioneer close = ds_define_sprite('ya', 'verysad', body_num=1, cloth='pioneer', dist='close')
    image ya shy pioneer close = ds_define_sprite('ya', 'shy', body_num=1, cloth='pioneer', dist='close')
    image ya shy2 pioneer close = ds_define_sprite('ya', 'veryshy', body_num=1, cloth='pioneer', dist='close')
    image ya smile pioneer close = ds_define_sprite('ya', 'smile', body_num=2, cloth='pioneer', dist='close')
    image ya smile2 pioneer close = ds_define_sprite('ya', 'normal', body_num=1, cloth='pioneer', dist='close')
    image ya surprise pioneer close = ds_define_sprite('ya', 'surprise', body_num=1, cloth='pioneer', dist='close')
    image ya guilty dress close = ds_define_sprite('ya', 'guilty', body_num=1, cloth='dress', dist='close')
    image ya happy dress close = ds_define_sprite('ya', 'happy', body_num=1, cloth='dress', dist='close')
    image ya happy2 dress close = ds_define_sprite('ya', 'happy2', body_num=2, cloth='dress', dist='close')
    image ya laugh dress close = ds_define_sprite('ya', 'laugh', body_num=2, cloth='dress', dist='close')
    image ya normal dress close = ds_define_sprite('ya', 'sad', body_num=1, cloth='dress', dist='close')
    image ya sad dress close = ds_define_sprite('ya', 'verysad', body_num=1, cloth='dress', dist='close')
    image ya shy dress close = ds_define_sprite('ya', 'shy', body_num=1, cloth='dress', dist='close')
    image ya shy2 dress close = ds_define_sprite('ya', 'veryshy', body_num=1, cloth='dress', dist='close')
    image ya smile dress close = ds_define_sprite('ya', 'smile', body_num=2, cloth='dress', dist='close')
    image ya smile2 dress close = ds_define_sprite('ya', 'normal', body_num=1, cloth='dress', dist='close')
    image ya surprise dress close = ds_define_sprite('ya', 'surprise', body_num=1, cloth='dress', dist='close')

    image ya guilty naked far = ds_define_sprite('ya', 'guilty', body_num=1, dist='far')
    image ya happy naked far = ds_define_sprite('ya', 'happy', body_num=1, dist='far')
    image ya happy2 naked far = ds_define_sprite('ya', 'happy2', body_num=2, dist='far')
    image ya laugh naked far = ds_define_sprite('ya', 'laugh', body_num=2, dist='far')
    image ya normal naked far = ds_define_sprite('ya', 'sad', body_num=1, dist='far')
    image ya sad naked far = ds_define_sprite('ya', 'verysad', body_num=1, dist='far')
    image ya shy naked far = ds_define_sprite('ya', 'shy', body_num=1, dist='far')
    image ya shy2 naked far = ds_define_sprite('ya', 'veryshy', body_num=1, dist='far')
    image ya smile naked far = ds_define_sprite('ya', 'smile', body_num=2, dist='far')
    image ya smile2 naked far = ds_define_sprite('ya', 'normal', body_num=1, dist='far')
    image ya surprise naked far = ds_define_sprite('ya', 'surprise', body_num=1, dist='far')
    image ya guilty pioneer far = ds_define_sprite('ya', 'guilty', body_num=1, cloth='pioneer', dist='far')
    image ya happy pioneer far = ds_define_sprite('ya', 'happy', body_num=1, cloth='pioneer', dist='far')
    image ya happy2 pioneer far = ds_define_sprite('ya', 'happy2', body_num=2, cloth='pioneer', dist='far')
    image ya laugh pioneer far = ds_define_sprite('ya', 'laugh', body_num=2, cloth='pioneer', dist='far')
    image ya normal pioneer far = ds_define_sprite('ya', 'sad', body_num=1, cloth='pioneer', dist='far')
    image ya sad pioneer far = ds_define_sprite('ya', 'verysad', body_num=1, cloth='pioneer', dist='far')
    image ya shy pioneer far = ds_define_sprite('ya', 'shy', body_num=1, cloth='pioneer', dist='far')
    image ya shy2 pioneer far = ds_define_sprite('ya', 'veryshy', body_num=1, cloth='pioneer', dist='far')
    image ya smile pioneer far = ds_define_sprite('ya', 'smile', body_num=2, cloth='pioneer', dist='far')
    image ya smile2 pioneer far = ds_define_sprite('ya', 'normal', body_num=1, cloth='pioneer', dist='far')
    image ya surprise pioneer far = ds_define_sprite('ya', 'surprise', body_num=1, cloth='pioneer', dist='far')
    image ya guilty dress far = ds_define_sprite('ya', 'guilty', body_num=1, cloth='dress', dist='far')
    image ya happy dress far = ds_define_sprite('ya', 'happy', body_num=1, cloth='dress', dist='far')
    image ya happy2 dress far = ds_define_sprite('ya', 'happy2', body_num=2, cloth='dress', dist='far')
    image ya laugh dress far = ds_define_sprite('ya', 'laugh', body_num=2, cloth='dress', dist='far')
    image ya normal dress far = ds_define_sprite('ya', 'sad', body_num=1, cloth='dress', dist='far')
    image ya sad dress far = ds_define_sprite('ya', 'verysad', body_num=1, cloth='dress', dist='far')
    image ya shy dress far = ds_define_sprite('ya', 'shy', body_num=1, cloth='dress', dist='far')
    image ya shy2 dress far = ds_define_sprite('ya', 'veryshy', body_num=1, cloth='dress', dist='far')
    image ya smile dress far = ds_define_sprite('ya', 'smile', body_num=2, cloth='dress', dist='far')
    image ya smile2 dress far = ds_define_sprite('ya', 'normal', body_num=1, cloth='dress', dist='far')
    image ya surprise dress far = ds_define_sprite('ya', 'surprise', body_num=1, cloth='dress', dist='far')

    # Физрук
    image fz angry uniform = ds_define_sprite('ba', 'evil', cloth='uniform')
    image fz normal uniform = ds_define_sprite('ba', 'normal', cloth='uniform')
    image fz rage uniform = ds_define_sprite('ba', 'rage', cloth='uniform')
    image fz serious uniform = ds_define_sprite('ba', 'em1', cloth='uniform')
    image fz smile uniform = ds_define_sprite('ba', 'smile', cloth='uniform')

    image fz angry naked = ds_define_sprite('ba', 'evil')
    image fz normal naked = ds_define_sprite('ba', 'normal')
    image fz rage naked = ds_define_sprite('ba', 'rage')
    image fz serious naked = ds_define_sprite('ba', 'em1')
    image fz smile naked = ds_define_sprite('ba', 'smile')

## Сны Семёна

    image dvw normal = "mods/disco_sovenok/sprite/normal/dvw/dv_normal.png"
    image dvw laugh = "mods/disco_sovenok/sprite/normal/dvw/dv_laugh.png"
    image dvw smile  = "mods/disco_sovenok/sprite/normal/dvw/dv_smile.png"
    image dvw rage = "mods/disco_sovenok/sprite/normal/dvw/dv_rage.png"

    image piw normal = "mods/disco_sovenok/sprite/normal/piw/qq.png"

    image sub arb = ds_define_sprite('undv', '', body_num=5)
    image sub lim = ds_define_sprite('undv', '', body_num=1)
    image sub trs = ds_define_sprite('undv', '', body_num=4)

    image ag grin = ds_define_sprite('ag', 'grin', body_num=1, cloth='casual')
    image ag happy = ds_define_sprite('ag', 'happy', body_num=1, cloth='casual')
    image ag normal = ds_define_sprite('ag', 'norm', body_num=1, cloth='casual')
    image ag ok = ds_define_sprite('ag', 'allisok', body_num=1, cloth='casual')
    image ag surprise = ds_define_sprite('ag', 'surprise', body_num=1, cloth='casual')
    image ag angry = ds_define_sprite('ag', 'angry', body_num=2, cloth='casual')
    image ag rage = ds_define_sprite('ag', 'furious', body_num=2, cloth='casual')
    image ag shocked = ds_define_sprite('ag', 'shock', body_num=2, cloth='casual')
    image ag tired = ds_define_sprite('ag', 'tired', body_num=2, cloth='casual')
    image ag confused = ds_define_sprite('ag', 'normal_hand', body_num=3, cloth='casual')
    image ag grin far = ds_define_sprite('ag', 'grin', body_num=1, cloth='casual', dist='far')
    image ag happy far = ds_define_sprite('ag', 'happy', body_num=1, cloth='casual', dist='far')
    image ag normal far = ds_define_sprite('ag', 'norm', body_num=1, cloth='casual', dist='far')
    image ag ok far = ds_define_sprite('ag', 'allisok', body_num=1, cloth='casual', dist='far')
    image ag surprise far = ds_define_sprite('ag', 'surprise', body_num=1, cloth='casual', dist='far')
    image ag angry far = ds_define_sprite('ag', 'angry', body_num=2, cloth='casual', dist='far')
    image ag rage far = ds_define_sprite('ag', 'furious', body_num=2, cloth='casual', dist='far')
    image ag shocked far = ds_define_sprite('ag', 'shock', body_num=2, cloth='casual', dist='far')
    image ag tired far = ds_define_sprite('ag', 'tired', body_num=2, cloth='casual', dist='far')
    image ag confused far = ds_define_sprite('ag', 'normal_hand', body_num=3, cloth='casual', dist='far')

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
