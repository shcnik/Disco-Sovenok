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
            return ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+cloth+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+acc+".png"), im.matrix.tint(0.94, 0.82, 1.0) ), "persistent.sprite_time=='night'",im.MatrixColor(im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+cloth+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+acc+".png"), im.matrix.tint(0.63, 0.78, 0.82) ), True, im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+cloth+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+acc+".png") )
        if cloth:
            return ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+cloth+".png"), im.matrix.tint(0.94, 0.82, 1.0) ), "persistent.sprite_time=='night'",im.MatrixColor(im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+cloth+".png"), im.matrix.tint(0.63, 0.78, 0.82) ), True, im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+cloth+".png") )
        if acc:
            return ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+acc+".png"), im.matrix.tint(0.94, 0.82, 1.0) ), "persistent.sprite_time=='night'",im.MatrixColor(im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+acc+".png"), im.matrix.tint(0.63, 0.78, 0.82) ), True, im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+acc+".png") )
        return ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png"), im.matrix.tint(0.94, 0.82, 1.0) ), "persistent.sprite_time=='night'",im.MatrixColor(im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png"), im.matrix.tint(0.63, 0.78, 0.82) ), True, im.Composite((900,1080), (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+body_name+".png", (0,0), "mods/disco_sovenok/sprite/"+dist+"/"+char+"/"+char+"_"+str(body_num)+"_"+emo+".png") )

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
    $ lgc = Character (u'Логика', color="00ffff", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ enc = Character (u'Энциклопедия', color="00ffff", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ rhe = Character (u'Риторика', color="00ffff", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ dra = Character (u'Драма', color="00ffff", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ con = Character (u'Концептуализация', color="00ffff", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ vic = Character (u'Визуальный анализ', color="00ffff", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    $ vol = Character (u'Сила воли', color="800080", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ ine = Character (u'Внутренняя империя', color="800080", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ aut = Character (u'Авторитет', color="800080", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ emp = Character (u'Эмпатия', color="800080", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ esp = Character (u'Командная волна', color="800080", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ sug = Character (u'Внушение', color="800080", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    $ edr = Character (u'Стойкость', color="e52b50", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ pat = Character (u'Болевой порог', color="e52b50", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ phi = Character (u'Грубая сила', color="e52b50", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ ins = Character (u'Инстинкт', color="e52b50", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ shi = Character (u'Трепет', color="e52b50", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ hfl = Character (u'Сумрак', color="e52b50", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    $ per_eye = Character (u'Восприятие (зрение)', color="f8f32b", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ per_hea = Character (u'Восприятие (слух)', color="f8f32b", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ per_sme = Character (u'Восприятие (обоняние)', color="f8f32b", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ per_tas = Character (u'Восприятие (вкус)', color="f8f32b", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ per_toc = Character (u'Восприятие (осязание)', color="f8f32b", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ cor = Character (u'Координация', color="f8f32b", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ res = Character (u'Скорость реакции', color="f8f32b", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ svf = Character (u'Эквилибристика', color="f8f32b", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ inf = Character (u'Техника', color="f8f32b", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ com = Character (u'Самообладание', color="f8f32b", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

    $ arb = Character (u'Рептильный мозг', color="ffffff", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ lim = Character (u'Лимбическая система', color="ffffff", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

## Голоса девушек
    $ dvv = Character (u'Девушка', color="ffaa00", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ mig = Character (u'Девушка', color="00deff", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ mtg = Character (u'Девушка', color="00ea32", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ slv = Character (u'Девушка', color="ffd200", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ unv = Character (u'Девушка', color="b956ff", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ usv = Character (u'Девушка', color="ff3200", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ elg = Character (u'Парень', color="ffff00", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

## Иные персонажи

    $ cr = Character (u'Повешенный труп', color="e1dd7d", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ gn = Character (u'Генда', color="7d7f7d", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ ck = Character (u'Повариха', color="1f75fe", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ yap = Character (u'Девушка', color="74b05f", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ ya = Character (u'Яна', color="74b05f", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ fz = Character (u'Борис Саныч', color="7b001c", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ fzp = Character (u'Физрук', color="7b001c", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ sb = Character (u'Девушка', color="ff335c", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ ag = Character (u'Мужчина', color="999999", ctc="ctc_animation", ctc_position="fixed", drop_shadow=[ (2, 2) ], drop_shadow_color="#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")
    $ moa = Character (u'Министерство въезда', color="ff3200", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000")

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

## В steam-версии де-факто body == swim, поэтому определяем собственные голые спрайты

    # Алиса
    image dv angry naked = ds_define_sprite('dv', 'angry', body_num=5)
    image dv angry naked close = ds_define_sprite('dv', 'angry', dist='close', body_num=5)
    image dv angry naked far = ds_define_sprite('dv', 'angry', dist='far', body_num=5)

    image dv cry naked = ds_define_sprite('dv', 'cry', body_num=1)
    image dv cry naked close = ds_define_sprite('dv', 'cry', dist='close', body_num=1)
    image dv cry naked far = ds_define_sprite('dv', 'cry', dist='far', body_num = 1)

    image dv grin naked = ds_define_sprite('dv', 'grin', body_num=2)
    image dv grin naked close = ds_define_sprite('dv', 'grin', dist='close', body_num=2)
    image dv grin naked far = ds_define_sprite('dv', 'grin', dist='far', body_num=2)

    image dv guilty naked = ds_define_sprite('dv', 'guilty', body_num=3)
    image dv guilty naked close = ds_define_sprite('dv', 'guilty', dist='close', body_num=3)
    image dv guilty naked far = ds_define_sprite('dv', 'guilty', dist='far', body_num=3)

    image dv laugh naked = ds_define_sprite('dv', 'laugh', body_num=4)
    image dv laugh naked close = ds_define_sprite('dv', 'laugh', dist='close', body_num=4)
    image dv laugh naked far = ds_define_sprite('dv', 'laugh', dist='far', body_num=4)

    image dv normal naked = ds_define_sprite('dv', 'normal', body_num=4)
    image dv normal naked close = ds_define_sprite('dv', 'normal', dist='close', body_num=4)
    image dv normal naked far = ds_define_sprite('dv', 'normal', dist='far', body_num=4)

    image dv rage naked = ds_define_sprite('dv', 'rage', body_num=5)
    image dv rage naked close = ds_define_sprite('dv', 'rage', dist='close', body_num=5)
    image dv rage naked far = ds_define_sprite('dv', 'rage', dist='far', body_num=5)

    image dv sad naked = ds_define_sprite('dv', 'sad', body_num=3)
    image dv sad naked close = ds_define_sprite('dv', 'sad', dist='close', body_num=3)
    image dv sad naked far = ds_define_sprite('dv', 'sad', dist='far', body_num=3)

    image dv scared naked = ds_define_sprite('dv', 'scared', body_num=1)
    image dv scared naked close = ds_define_sprite('dv', 'scared', dist='close', body_num=1)
    image dv scared naked far = ds_define_sprite('dv', 'scared', dist='far', body_num=1)

    image dv shocked naked = ds_define_sprite('dv', 'shocked', body_num=1)
    image dv shocked naked close = ds_define_sprite('dv', 'shocked', dist='close', body_num=1)
    image dv shocked naked far = ds_define_sprite('dv', 'shocked', dist='far', body_num=1)

    image dv shy naked = ds_define_sprite('dv', 'shy', body_num=3)
    image dv shy naked close = ds_define_sprite('dv', 'shy', dist='close', body_num=3)
    image dv shy naked far = ds_define_sprite('dv', 'shy', dist='far', body_num=3)

    image dv smile naked = ds_define_sprite('dv', 'smile', body_num=4)
    image dv smile naked close = ds_define_sprite('dv', 'smile', dist='close', body_num=4)
    image dv smile naked far = ds_define_sprite('dv', 'smile', dist='far', body_num=4)

    image dv surprise naked = ds_define_sprite('dv', 'surprise', body_num=1)
    image dv surprise naked close = ds_define_sprite('dv', 'surprise', dist='close', body_num=1)
    image dv surprise naked far = ds_define_sprite('dv', 'surprise', dist='far', body_num=1)

    # Электроник
    image el angry naked = ds_define_sprite('el', 'angry', body_num=3)
    image el angry naked close = ds_define_sprite('el', 'angry', dist='close', body_num=3)
    image el angry naked far = ds_define_sprite('el', 'angry', dist='far', body_num=3)

    image el fingal naked = ds_define_sprite('el', 'fingal', body_num=2)
    image el fingal naked close = ds_define_sprite('el', 'fingal', dist='close', body_num=2)
    image el fingal naked far = ds_define_sprite('el', 'fingal', dist='far', body_num=2)

    image el grin naked = ds_define_sprite('el', 'grin', body_num=1)
    image el grin naked close = ds_define_sprite('el', 'grin', dist='close', body_num=1)
    image el grin naked far = ds_define_sprite('el', 'grin', dist='far', body_num=1)

    image el laugh naked = ds_define_sprite('el', 'laugh', body_num=3)
    image el laugh naked close = ds_define_sprite('el', 'laugh', dist='close', body_num=3)
    image el laugh naked far = ds_define_sprite('el', 'laugh', dist='far', body_num=3)

    image el normal naked = ds_define_sprite('el', 'normal', body_num=1)
    image el normal naked close = ds_define_sprite('el', 'normal', dist='close', body_num=1)
    image el normal naked far = ds_define_sprite('el', 'normal', dist='far', body_num=1)

    image el sad naked = ds_define_sprite('el', 'sad', body_num=2)
    image el sad naked close = ds_define_sprite('el', 'sad', dist='close', body_num=2)
    image el sad naked far = ds_define_sprite('el', 'sad', dist='far', body_num=2)

    image el scared naked = ds_define_sprite('el', 'scared', body_num=2)
    image el scared naked close = ds_define_sprite('el', 'scared', dist='close', body_num=2)
    image el scared naked far = ds_define_sprite('el', 'scared', dist='far', body_num=2)

    image el serious naked = ds_define_sprite('el', 'serious', body_num=3)
    image el serious naked close = ds_define_sprite('el', 'serious', dist='close', body_num=3)
    image el serious naked far = ds_define_sprite('el', 'serious', dist='far', body_num=3)

    image el shocked naked = ds_define_sprite('el', 'shocked', body_num=2)
    image el shocked naked close = ds_define_sprite('el', 'shocked', dist='close', body_num=2)
    image el shocked naked far = ds_define_sprite('el', 'shocked', dist='far', body_num=2)

    image el smile naked = ds_define_sprite('el', 'smile', body_num=1)
    image el smile naked close = ds_define_sprite('el', 'smile', dist='close', body_num=1)
    image el smile naked far = ds_define_sprite('el', 'smile', dist='far', body_num=1)

    image el surprise naked = ds_define_sprite('el', 'surprise', body_num=2)
    image el surprise naked close = ds_define_sprite('el', 'surprise', dist='close', body_num=2)
    image el surprise naked far = ds_define_sprite('el', 'surprise', dist='far', body_num=2)

    image el upset naked = ds_define_sprite('el', 'upset', body_num=2)
    image el upset naked close = ds_define_sprite('el', 'upset', dist='close', body_num=2)
    image el upset naked far = ds_define_sprite('el', 'upset', dist='far', body_num=2)

    # Мику
    image mi angry naked = ds_define_sprite('mi', 'angry', body_num=3)
    image mi angry naked close = ds_define_sprite('mi', 'angry', dist='close', body_num=3)
    image mi angry naked far = ds_define_sprite('mi', 'angry', dist='far', body_num=3)

    image mi cry naked = ds_define_sprite('mi', 'cry', body_num=1)
    image mi cry naked close = ds_define_sprite('mi', 'cry', dist='close', body_num=1)
    image mi cry naked far = ds_define_sprite('mi', 'cry', dist='far', body_num=1)

    image mi cry_smile naked = ds_define_sprite('mi', 'cry_smile', body_num=2)
    image mi cry_smile naked close = ds_define_sprite('mi', 'cry_smile', dist='close', body_num=2)
    image mi cry_smile naked far = ds_define_sprite('mi', 'cry_smile', dist='far', body_num=2)

    image mi dontlike naked = ds_define_sprite('mi', 'dontlike', body_num=1)
    image mi dontlike naked close = ds_define_sprite('mi', 'dontlike', dist='close', body_num=1)
    image mi dontlike naked far = ds_define_sprite('mi', 'dontlike', dist='far', body_num=1)

    image mi grin naked = ds_define_sprite('mi', 'grin', body_num=2)
    image mi grin naked close = ds_define_sprite('mi', 'grin', dist='close', body_num=2)
    image mi grin naked far = ds_define_sprite('mi', 'grin', dist='far', body_num=2)

    image mi happy naked = ds_define_sprite('mi', 'happy', body_num=2)
    image mi happy naked close = ds_define_sprite('mi', 'happy', dist='close', body_num=2)
    image mi happy naked far = ds_define_sprite('mi', 'happy', dist='far', body_num=2)

    image mi laugh naked = ds_define_sprite('mi', 'laugh', body_num=1)
    image mi laugh naked close = ds_define_sprite('mi', 'laugh', dist='close', body_num=1)
    image mi laugh naked far = ds_define_sprite('mi', 'laugh', dist='far', body_num=1)

    image mi normal naked = ds_define_sprite('mi', 'normal', body_num=3)
    image mi normal naked close = ds_define_sprite('mi', 'normal', dist='close', body_num=3)
    image mi normal naked far = ds_define_sprite('mi', 'normal', dist='far', body_num=3)

    image mi rage naked = ds_define_sprite('mi', 'rage', body_num=3)
    image mi rage naked close = ds_define_sprite('mi', 'rage', dist='close', body_num=3)
    image mi rage naked far = ds_define_sprite('mi', 'rage', dist='far', body_num=3)

    image mi sad naked = ds_define_sprite('mi', 'sad', body_num=2)
    image mi sad naked close = ds_define_sprite('mi', 'sad', dist='close', body_num=2)
    image mi sad naked far = ds_define_sprite('mi', 'sad', dist='far', body_num=2)

    image mi scared naked = ds_define_sprite('mi', 'scared', body_num=1)
    image mi scared naked close = ds_define_sprite('mi', 'scared', dist='close', body_num=1)
    image mi scared naked far = ds_define_sprite('mi', 'scared', dist='far', body_num=1)

    image mi serious naked = ds_define_sprite('mi', 'serious', body_num=3)
    image mi serious naked close = ds_define_sprite('mi', 'serious', dist='close', body_num=3)
    image mi serious naked far = ds_define_sprite('mi', 'serious', dist='far', body_num=3)

    image mi shocked naked = ds_define_sprite('mi', 'shocked', body_num=1)
    image mi shocked naked close = ds_define_sprite('mi', 'shocked', dist='close', body_num=1)
    image mi shocked naked far = ds_define_sprite('mi', 'shocked', dist='far', body_num=1)

    image mi shy naked = ds_define_sprite('mi', 'shy', body_num=1)
    image mi shy naked close = ds_define_sprite('mi', 'shy', dist='close', body_num=1)
    image mi shy naked far = ds_define_sprite('mi', 'shy', dist='far', body_num=1)

    image mi smile naked = ds_define_sprite('mi', 'smile', body_num=2)
    image mi smile naked close = ds_define_sprite('mi', 'smile', dist='close', body_num=2)
    image mi smile naked far = ds_define_sprite('mi', 'smile', dist='far', body_num=2)

    image mi surprise naked = ds_define_sprite('mi', 'surprise', body_num=1)
    image mi surprise naked close = ds_define_sprite('mi', 'surprise', dist='close', body_num=1)
    image mi surprise naked far = ds_define_sprite('mi', 'surprise', dist='far', body_num=1)

    image mi upset naked = ds_define_sprite('mi', 'upset', body_num=3)
    image mi upset naked close = ds_define_sprite('mi', 'upset', dist='close', body_num=3)
    image mi upset naked far = ds_define_sprite('mi', 'upset', dist='far', body_num=3)

    # ОД
    image mt angry naked = ds_define_sprite('mt', 'angry', body_num=2)
    image mt angry naked close = ds_define_sprite('mt', 'angry', dist='close', body_num=2)
    image mt angry naked far = ds_define_sprite('mt', 'angry', dist='far', body_num=2)

    image mt grin naked = ds_define_sprite('mt', 'grin', body_num=3)
    image mt grin naked close = ds_define_sprite('mt', 'grin', dist='close', body_num=3)
    image mt grin naked far = ds_define_sprite('mt', 'grin', dist='far', body_num=3)

    image mt laugh naked = ds_define_sprite('mt', 'laugh', body_num=3)
    image mt laugh naked close = ds_define_sprite('mt', 'laugh', dist='close', body_num=3)
    image mt laugh naked far = ds_define_sprite('mt', 'laugh', dist='far', body_num=3)

    image mt normal naked = ds_define_sprite('mt', 'normal', body_num=1)
    image mt normal naked close = ds_define_sprite('mt', 'normal', dist='close', body_num=1)
    image mt normal naked far = ds_define_sprite('mt', 'normal', dist='far', body_num=1)

    image mt rage naked = ds_define_sprite('mt', 'rage', body_num=2)
    image mt rage naked close = ds_define_sprite('mt', 'rage', dist='close', body_num=2)
    image mt rage naked far = ds_define_sprite('mt', 'rage', dist='far', body_num=2)

    image mt sad naked = ds_define_sprite('mt', 'sad', body_num=1)
    image mt sad naked close = ds_define_sprite('mt', 'sad', dist='close', body_num=1)
    image mt sad naked far = ds_define_sprite('mt', 'sad', dist='far', body_num=1)

    image mt scared naked = ds_define_sprite('mt', 'scared', body_num=3)
    image mt scared naked close = ds_define_sprite('mt', 'scared', dist='close', body_num=3)
    image mt scared naked far = ds_define_sprite('mt', 'scared', dist='far', body_num=3)

    image mt shocked naked = ds_define_sprite('mt', 'shocked', body_num=2)
    image mt shocked naked close = ds_define_sprite('mt', 'shocked', dist='close', body_num=2)
    image mt shocked naked far = ds_define_sprite('mt', 'shocked', dist='far', body_num=2)

    image mt smile naked = ds_define_sprite('mt', 'smile', body_num=1)
    image mt smile naked close = ds_define_sprite('mt', 'smile', dist='close', body_num=1)
    image mt smile naked far = ds_define_sprite('mt', 'smile', dist='far', body_num=1)

    image mt surprise naked = ds_define_sprite('mt', 'surprise', body_num=1)
    image mt surprise naked close = ds_define_sprite('mt', 'surprise', dist='close', body_num=1)
    image mt surprise naked far = ds_define_sprite('mt', 'surprise', dist='far', body_num=1)

    # Славя
    image sl angry naked = ds_define_sprite('sl', 'angry', body_num=3)
    image sl angry naked close = ds_define_sprite('sl', 'angry', dist='close', body_num=3)
    image sl angry naked far = ds_define_sprite('sl', 'angry', dist='far', body_num=3)

    image sl happy naked = ds_define_sprite('sl', 'happy', body_num=2)
    image sl happy naked close = ds_define_sprite('sl', 'happy', dist='close', body_num=2)
    image sl happy naked far = ds_define_sprite('sl', 'happy', dist='far', body_num=2)
    
    image sl laugh naked = ds_define_sprite('sl', 'laugh', body_num=2)
    image sl laugh naked close = ds_define_sprite('sl', 'laugh', dist='close', body_num=2)
    image sl laugh naked far = ds_define_sprite('sl', 'laugh', dist='far', body_num=2)

    image sl normal naked = ds_define_sprite('sl', 'normal', body_num=1)
    image sl normal naked close = ds_define_sprite('sl', 'normal', dist='close', body_num=1)
    image sl normal naked far = ds_define_sprite('sl', 'normal', dist='far', body_num=1)

    image sl sad naked = ds_define_sprite('sl', 'sad', body_num=3)
    image sl sad naked close = ds_define_sprite('sl', 'sad', dist='close', body_num=3)
    image sl sad naked far = ds_define_sprite('sl', 'sad', dist='far', body_num=3)

    image sl scared naked = ds_define_sprite('sl', 'scared', body_num=4)
    image sl scared naked close = ds_define_sprite('sl', 'scared', dist='close', body_num=4)
    image sl scared naked far = ds_define_sprite('sl', 'scared', dist='far', body_num=4)

    image sl serious naked = ds_define_sprite('sl', 'serious', body_num=1)
    image sl serious naked close = ds_define_sprite('sl', 'serious', dist='close', body_num=1)
    image sl serious naked far = ds_define_sprite('sl', 'serious', dist='far', body_num=1)

    image sl shy naked = ds_define_sprite('sl', 'shy', body_num=2)
    image sl shy naked close = ds_define_sprite('sl', 'shy', dist='close', body_num=2)
    image sl shy naked far = ds_define_sprite('sl', 'shy', dist='far', body_num=2)

    image sl smile naked = ds_define_sprite('sl', 'smile', body_num=1)
    image sl smile naked close = ds_define_sprite('sl', 'smile', dist='close', body_num=1)
    image sl smile naked far = ds_define_sprite('sl', 'smile', dist='far', body_num=1)

    image sl smile2 naked = ds_define_sprite('sl', 'smile2', body_num=2)
    image sl smile2 naked close = ds_define_sprite('sl', 'smile2', dist='close', body_num=2)
    image sl smile2 naked far = ds_define_sprite('sl', 'smile2', dist='far', body_num=2)

    image sl surprise naked = ds_define_sprite('sl', 'surprise', body_num=3)
    image sl surprise naked close = ds_define_sprite('sl', 'surprise', dist='close', body_num=3)
    image sl surprise naked far = ds_define_sprite('sl', 'surprise', dist='far', body_num=3)

    image sl tender naked = ds_define_sprite('sl', 'tender', body_num=4)
    image sl tender naked close = ds_define_sprite('sl', 'tender', dist='close', body_num=4)
    image sl tender naked far = ds_define_sprite('sl', 'tender', dist='far', body_num=4)

    # Лена
    image un angry naked = ds_define_sprite('un', 'angry', body_num=1)
    image un angry naked close = ds_define_sprite('un', 'angry', dist='close', body_num=1)
    image un angry naked far = ds_define_sprite('un', 'angry', dist='far', body_num=1)

    image un angry2 naked = ds_define_sprite('un', 'angry2', body_num=3)
    image un angry2 naked close = ds_define_sprite('un', 'angry2', dist='close', body_num=3)
    image un angry2 naked far = ds_define_sprite('un', 'angry2', dist='far', body_num=3)

    image un cry naked = ds_define_sprite('un', 'cry', body_num=2)
    image un cry naked close = ds_define_sprite('un', 'cry', dist='close', body_num=2)
    image un cry naked far = ds_define_sprite('un', 'cry', dist='far', body_num=2)

    image un cry_smile naked = ds_define_sprite('un', 'cry_smile', body_num=2)
    image un cry_smile naked close = ds_define_sprite('un', 'cry_smile', dist='close', body_num=2)
    image un cry_smile naked far = ds_define_sprite('un', 'cry_smile', dist='far', body_num=2)

    image un evil_smile naked = ds_define_sprite('un', 'evil_smile', body_num=1)
    image un evil_smile naked close = ds_define_sprite('un', 'evil_smile', dist='close', body_num=1)
    image un evil_smile naked far = ds_define_sprite('un', 'evil_smile', dist='far', body_num=1)

    image un grin naked = ds_define_sprite('un', 'grin', body_num=3)
    image un grin naked close = ds_define_sprite('un', 'grin', dist='close', body_num=3)
    image un grin naked far = ds_define_sprite('un', 'grin', dist='far', body_num=3)

    image un laugh naked = ds_define_sprite('un', 'laugh', body_num=3)
    image un laugh naked close = ds_define_sprite('un', 'laugh', dist='close', body_num=3)
    image un laugh naked far = ds_define_sprite('un', 'laugh', dist='far', body_num=3)

    image un normal naked = ds_define_sprite('un', 'normal', body_num=1)
    image un normal naked close = ds_define_sprite('un', 'normal', dist='close', body_num=1)
    image un normal naked far = ds_define_sprite('un', 'normal', dist='far', body_num=1)

    image un rage naked = ds_define_sprite('un', 'rage', body_num=3)
    image un rage naked close = ds_define_sprite('un', 'rage', dist='close', body_num=3)
    image un rage naked far = ds_define_sprite('un', 'rage', dist='far', body_num=3)

    image un sad naked = ds_define_sprite('un', 'sad', body_num=2)
    image un sad naked close = ds_define_sprite('un', 'sad', dist='close', body_num=2)
    image un sad naked far = ds_define_sprite('un', 'sad', dist='far', body_num=2)

    image un scared naked = ds_define_sprite('un', 'scared', body_num=2)
    image un scared naked close = ds_define_sprite('un', 'scared', dist='close', body_num=2)
    image un scared naked far = ds_define_sprite('un', 'scared', dist='far', body_num=2)

    image un serious naked = ds_define_sprite('un', 'serious', body_num=3)
    image un serious naked close = ds_define_sprite('un', 'serious', dist='close', body_num=3)
    image un serious naked far = ds_define_sprite('un', 'serious', dist='far', body_num=3)

    image un shocked naked = ds_define_sprite('un', 'shocked', body_num=2)
    image un shocked naked close = ds_define_sprite('un', 'shocked', dist='close', body_num=2)
    image un shocked naked far = ds_define_sprite('un', 'shocked', dist='far', body_num=2)

    image un shy naked = ds_define_sprite('un', 'shy', body_num=1)
    image un shy naked close = ds_define_sprite('un', 'shy', dist='close', body_num=1)
    image un shy naked far = ds_define_sprite('un', 'shy', dist='far', body_num=1)

    image un smile naked = ds_define_sprite('un', 'smile', body_num=1)
    image un smile naked close = ds_define_sprite('un', 'smile', dist='close', body_num=1)
    image un smile naked far = ds_define_sprite('un', 'smile', dist='far', body_num=1)

    image un smile2 naked = ds_define_sprite('un', 'smile2', body_num=1)
    image un smile2 naked close = ds_define_sprite('un', 'smile2', dist='close', body_num=1)
    image un smile2 naked far = ds_define_sprite('un', 'smile2', dist='far', body_num=1)

    image un smile3 naked = ds_define_sprite('un', 'smile3', body_num=3)
    image un smile3 naked close = ds_define_sprite('un', 'smile3', dist='close', body_num=3)
    image un smile3 naked far = ds_define_sprite('un', 'smile3', dist='far', body_num=3)

    image un surprise naked = ds_define_sprite('un', 'surprise', body_num=2)
    image un surprise naked close = ds_define_sprite('un', 'surprise', dist='close', body_num=2)
    image un surprise naked far = ds_define_sprite('un', 'surprise', dist='far', body_num=2)

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

    # Алиса
    image dv angry casual = ds_define_sprite('dv', 'angry', body_num=5, cloth='casual')
    image dv cry casual = ds_define_sprite('dv', 'cry', body_num=1, cloth='casual')
    image dv grin casual = ds_define_sprite('dv', 'grin', body_num=2, cloth='casual')
    image dv guilty casual = ds_define_sprite('dv', 'guilty', body_num=3, cloth='casual')
    image dv laugh casual = ds_define_sprite('dv', 'laugh', body_num=4, cloth='casual')
    image dv normal casual = ds_define_sprite('dv', 'normal', body_num=4, cloth='casual')
    image dv rage casual = ds_define_sprite('dv', 'rage', body_num=5, cloth='casual')
    image dv sad casual = ds_define_sprite('dv', 'sad', body_num=3, cloth='casual')
    image dv scared casual = ds_define_sprite('dv', 'scared', body_num=1, cloth='casual')
    image dv shocked casual = ds_define_sprite('dv', 'shocked', body_num=1, cloth='casual')
    image dv shy casual = ds_define_sprite('dv', 'shy', body_num=3, cloth='casual')
    image dv smile casual = ds_define_sprite('dv', 'smile', body_num=4, cloth='casual')
    image dv surprise casual = ds_define_sprite('dv', 'surprise', body_num=1, cloth='casual')

    image dv angry dress = ds_define_sprite('dv', 'angry', body_num=5, cloth='dress')
    image dv cry dress = ds_define_sprite('dv', 'cry', body_num=1, cloth='dress')
    image dv grin dress = ds_define_sprite('dv', 'grin', body_num=2, cloth='dress')
    image dv guilty dress = ds_define_sprite('dv', 'guilty', body_num=3, cloth='dress')
    image dv laugh dress = ds_define_sprite('dv', 'laugh', body_num=4, cloth='dress')
    image dv normal dress = ds_define_sprite('dv', 'normal', body_num=4, cloth='dress')
    image dv rage dress = ds_define_sprite('dv', 'rage', body_num=5, cloth='dress')
    image dv sad dress = ds_define_sprite('dv', 'sad', body_num=3, cloth='dress')
    image dv scared dress = ds_define_sprite('dv', 'scared', body_num=1, cloth='dress')
    image dv shocked dress = ds_define_sprite('dv', 'shocked', body_num=1, cloth='dress')
    image dv shy dress = ds_define_sprite('dv', 'shy', body_num=3, cloth='dress')
    image dv smile dress = ds_define_sprite('dv', 'smile', body_num=4, cloth='dress')
    image dv surprise dress = ds_define_sprite('dv', 'surprise', body_num=1, cloth='dress')

    image dv angry modern = ds_define_sprite('dv', 'angry', body_num=5, cloth='modern')
    image dv angry modern close = ds_define_sprite('dv', 'angry', dist='close', body_num=5, cloth='modern')
    image dv angry modern far = ds_define_sprite('dv', 'angry', dist='far', body_num=5, cloth='modern')

    image dv cry modern = ds_define_sprite('dv', 'cry', body_num=1, cloth='modern')
    image dv cry modern close = ds_define_sprite('dv', 'cry', dist='close', body_num=1, cloth='modern')
    image dv cry modern far = ds_define_sprite('dv', 'cry', dist='far', body_num = 1, cloth='modern')

    image dv grin modern = ds_define_sprite('dv', 'grin', body_num=2, cloth='modern')
    image dv grin modern close = ds_define_sprite('dv', 'grin', dist='close', body_num=2, cloth='modern')
    image dv grin modern far = ds_define_sprite('dv', 'grin', dist='far', body_num=2, cloth='modern')

    image dv guilty modern = ds_define_sprite('dv', 'guilty', body_num=3, cloth='modern')
    image dv guilty modern close = ds_define_sprite('dv', 'guilty', dist='close', body_num=3, cloth='modern')
    image dv guilty modern far = ds_define_sprite('dv', 'guilty', dist='far', body_num=3, cloth='modern')

    image dv laugh modern = ds_define_sprite('dv', 'laugh', body_num=4, cloth='modern')
    image dv laugh modern close = ds_define_sprite('dv', 'laugh', dist='close', body_num=4, cloth='modern')
    image dv laugh modern far = ds_define_sprite('dv', 'laugh', dist='far', body_num=4, cloth='modern')

    image dv normal modern = ds_define_sprite('dv', 'normal', body_num=4, cloth='modern')
    image dv normal modern close = ds_define_sprite('dv', 'normal', dist='close', body_num=4, cloth='modern')
    image dv normal modern far = ds_define_sprite('dv', 'normal', dist='far', body_num=4, cloth='modern')

    image dv rage modern = ds_define_sprite('dv', 'rage', body_num=5, cloth='modern')
    image dv rage modern close = ds_define_sprite('dv', 'rage', dist='close', body_num=5, cloth='modern')
    image dv rage modern far = ds_define_sprite('dv', 'rage', dist='far', body_num=5, cloth='modern')

    image dv sad modern = ds_define_sprite('dv', 'sad', body_num=3, cloth='modern')
    image dv sad modern close = ds_define_sprite('dv', 'sad', dist='close', body_num=3, cloth='modern')
    image dv sad modern far = ds_define_sprite('dv', 'sad', dist='far', body_num=3, cloth='modern')

    image dv scared modern = ds_define_sprite('dv', 'scared', body_num=1, cloth='modern')
    image dv scared modern close = ds_define_sprite('dv', 'scared', dist='close', body_num=1, cloth='modern')
    image dv scared modern far = ds_define_sprite('dv', 'scared', dist='far', body_num=1, cloth='modern')

    image dv shocked modern = ds_define_sprite('dv', 'shocked', body_num=1, cloth='modern')
    image dv shocked modern close = ds_define_sprite('dv', 'shocked', dist='close', body_num=1, cloth='modern')
    image dv shocked modern far = ds_define_sprite('dv', 'shocked', dist='far', body_num=1, cloth='modern')

    image dv shy modern = ds_define_sprite('dv', 'shy', body_num=3, cloth='modern')
    image dv shy modern close = ds_define_sprite('dv', 'shy', dist='close', body_num=3, cloth='modern')
    image dv shy modern far = ds_define_sprite('dv', 'shy', dist='far', body_num=3, cloth='modern')

    image dv smile modern = ds_define_sprite('dv', 'smile', body_num=4, cloth='modern')
    image dv smile modern close = ds_define_sprite('dv', 'smile', dist='close', body_num=4, cloth='modern')
    image dv smile modern far = ds_define_sprite('dv', 'smile', dist='far', body_num=4, cloth='modern')

    image dv surprise modern = ds_define_sprite('dv', 'surprise', body_num=1, cloth='modern')
    image dv surprise modern close = ds_define_sprite('dv', 'surprise', dist='close', body_num=1, cloth='modern')
    image dv surprise modern far = ds_define_sprite('dv', 'surprise', dist='far', body_num=1, cloth='modern')

    image dv angry modern = ds_define_sprite('dv', 'angry', body_num=5, cloth='modern')
    image dv angry modern close = ds_define_sprite('dv', 'angry', dist='close', body_num=5, cloth='modern')
    image dv angry modern far = ds_define_sprite('dv', 'angry', dist='far', body_num=5, cloth='modern')

    image dv cry modern = ds_define_sprite('dv', 'cry', body_num=1, cloth='modern')
    image dv cry modern close = ds_define_sprite('dv', 'cry', dist='close', body_num=1, cloth='modern')
    image dv cry modern far = ds_define_sprite('dv', 'cry', dist='far', body_num = 1, cloth='modern')

    image dv grin modern = ds_define_sprite('dv', 'grin', body_num=2, cloth='modern')
    image dv grin modern close = ds_define_sprite('dv', 'grin', dist='close', body_num=2, cloth='modern')
    image dv grin modern far = ds_define_sprite('dv', 'grin', dist='far', body_num=2, cloth='modern')

    image dv guilty modern = ds_define_sprite('dv', 'guilty', body_num=3, cloth='modern')
    image dv guilty modern close = ds_define_sprite('dv', 'guilty', dist='close', body_num=3, cloth='modern')
    image dv guilty modern far = ds_define_sprite('dv', 'guilty', dist='far', body_num=3, cloth='modern')

    image dv laugh modern = ds_define_sprite('dv', 'laugh', body_num=4, cloth='modern')
    image dv laugh modern close = ds_define_sprite('dv', 'laugh', dist='close', body_num=4, cloth='modern')
    image dv laugh modern far = ds_define_sprite('dv', 'laugh', dist='far', body_num=4, cloth='modern')

    image dv normal modern = ds_define_sprite('dv', 'normal', body_num=4, cloth='modern')
    image dv normal modern close = ds_define_sprite('dv', 'normal', dist='close', body_num=4, cloth='modern')
    image dv normal modern far = ds_define_sprite('dv', 'normal', dist='far', body_num=4, cloth='modern')

    image dv rage modern = ds_define_sprite('dv', 'rage', body_num=5, cloth='modern')
    image dv rage modern close = ds_define_sprite('dv', 'rage', dist='close', body_num=5, cloth='modern')
    image dv rage modern far = ds_define_sprite('dv', 'rage', dist='far', body_num=5, cloth='modern')

    image dv sad modern = ds_define_sprite('dv', 'sad', body_num=3, cloth='modern')
    image dv sad modern close = ds_define_sprite('dv', 'sad', dist='close', body_num=3, cloth='modern')
    image dv sad modern far = ds_define_sprite('dv', 'sad', dist='far', body_num=3, cloth='modern')

    image dv scared modern = ds_define_sprite('dv', 'scared', body_num=1, cloth='modern')
    image dv scared modern close = ds_define_sprite('dv', 'scared', dist='close', body_num=1, cloth='modern')
    image dv scared modern far = ds_define_sprite('dv', 'scared', dist='far', body_num=1, cloth='modern')

    image dv shocked modern = ds_define_sprite('dv', 'shocked', body_num=1, cloth='modern')
    image dv shocked modern close = ds_define_sprite('dv', 'shocked', dist='close', body_num=1, cloth='modern')
    image dv shocked modern far = ds_define_sprite('dv', 'shocked', dist='far', body_num=1, cloth='modern')

    image dv shy modern = ds_define_sprite('dv', 'shy', body_num=3, cloth='modern')
    image dv shy modern close = ds_define_sprite('dv', 'shy', dist='close', body_num=3, cloth='modern')
    image dv shy modern far = ds_define_sprite('dv', 'shy', dist='far', body_num=3, cloth='modern')

    image dv smile modern = ds_define_sprite('dv', 'smile', body_num=4, cloth='modern')
    image dv smile modern close = ds_define_sprite('dv', 'smile', dist='close', body_num=4, cloth='modern')
    image dv smile modern far = ds_define_sprite('dv', 'smile', dist='far', body_num=4, cloth='modern')

    image dv surprise modern = ds_define_sprite('dv', 'surprise', body_num=1, cloth='modern')
    image dv surprise modern close = ds_define_sprite('dv', 'surprise', dist='close', body_num=1, cloth='modern')
    image dv surprise modern far = ds_define_sprite('dv', 'surprise', dist='far', body_num=1, cloth='modern')

    image dv angry sport = ds_define_sprite('dv', 'angry', body_num=5, cloth='sport')
    image dv angry sport close = ds_define_sprite('dv', 'angry', dist='close', body_num=5, cloth='sport')
    image dv angry sport far = ds_define_sprite('dv', 'angry', dist='far', body_num=5, cloth='sport')

    image dv cry sport = ds_define_sprite('dv', 'cry', body_num=1, cloth='sport')
    image dv cry sport close = ds_define_sprite('dv', 'cry', dist='close', body_num=1, cloth='sport')
    image dv cry sport far = ds_define_sprite('dv', 'cry', dist='far', body_num = 1, cloth='sport')

    image dv grin sport = ds_define_sprite('dv', 'grin', body_num=2, cloth='sport')
    image dv grin sport close = ds_define_sprite('dv', 'grin', dist='close', body_num=2, cloth='sport')
    image dv grin sport far = ds_define_sprite('dv', 'grin', dist='far', body_num=2, cloth='sport')

    image dv guilty sport = ds_define_sprite('dv', 'guilty', body_num=3, cloth='sport')
    image dv guilty sport close = ds_define_sprite('dv', 'guilty', dist='close', body_num=3, cloth='sport')
    image dv guilty sport far = ds_define_sprite('dv', 'guilty', dist='far', body_num=3, cloth='sport')

    image dv laugh sport = ds_define_sprite('dv', 'laugh', body_num=4, cloth='sport')
    image dv laugh sport close = ds_define_sprite('dv', 'laugh', dist='close', body_num=4, cloth='sport')
    image dv laugh sport far = ds_define_sprite('dv', 'laugh', dist='far', body_num=4, cloth='sport')

    image dv normal sport = ds_define_sprite('dv', 'normal', body_num=4, cloth='sport')
    image dv normal sport close = ds_define_sprite('dv', 'normal', dist='close', body_num=4, cloth='sport')
    image dv normal sport far = ds_define_sprite('dv', 'normal', dist='far', body_num=4, cloth='sport')

    image dv rage sport = ds_define_sprite('dv', 'rage', body_num=5, cloth='sport')
    image dv rage sport close = ds_define_sprite('dv', 'rage', dist='close', body_num=5, cloth='sport')
    image dv rage sport far = ds_define_sprite('dv', 'rage', dist='far', body_num=5, cloth='sport')

    image dv sad sport = ds_define_sprite('dv', 'sad', body_num=3, cloth='sport')
    image dv sad sport close = ds_define_sprite('dv', 'sad', dist='close', body_num=3, cloth='sport')
    image dv sad sport far = ds_define_sprite('dv', 'sad', dist='far', body_num=3, cloth='sport')

    image dv scared sport = ds_define_sprite('dv', 'scared', body_num=1, cloth='sport')
    image dv scared sport close = ds_define_sprite('dv', 'scared', dist='close', body_num=1, cloth='sport')
    image dv scared sport far = ds_define_sprite('dv', 'scared', dist='far', body_num=1, cloth='sport')

    image dv shocked sport = ds_define_sprite('dv', 'shocked', body_num=1, cloth='sport')
    image dv shocked sport close = ds_define_sprite('dv', 'shocked', dist='close', body_num=1, cloth='sport')
    image dv shocked sport far = ds_define_sprite('dv', 'shocked', dist='far', body_num=1, cloth='sport')

    image dv shy sport = ds_define_sprite('dv', 'shy', body_num=3, cloth='sport')
    image dv shy sport close = ds_define_sprite('dv', 'shy', dist='close', body_num=3, cloth='sport')
    image dv shy sport far = ds_define_sprite('dv', 'shy', dist='far', body_num=3, cloth='sport')

    image dv smile sport = ds_define_sprite('dv', 'smile', body_num=4, cloth='sport')
    image dv smile sport close = ds_define_sprite('dv', 'smile', dist='close', body_num=4, cloth='sport')
    image dv smile sport far = ds_define_sprite('dv', 'smile', dist='far', body_num=4, cloth='sport')

    image dv surprise sport = ds_define_sprite('dv', 'surprise', body_num=1, cloth='sport')
    image dv surprise sport close = ds_define_sprite('dv', 'surprise', dist='close', body_num=1, cloth='sport')
    image dv surprise sport far = ds_define_sprite('dv', 'surprise', dist='far', body_num=1, cloth='sport')

    image dv evil_smile naked = ds_define_sprite('dv', 'evil_smile', body_num=1)
    image dv evil_smile naked close = ds_define_sprite('dv', 'evil_smile', dist='close', body_num=1)
    image dv evil_smile naked far = ds_define_sprite('dv', 'evil_smile', dist='far', body_num=1)
    image dv evil_smile casual = ds_define_sprite('dv', 'evil_smile', body_num=1, cloth='casual')
    image dv evil_smile casual close = ds_define_sprite('dv', 'evil_smile', dist='close', body_num=1, cloth='casual')
    image dv evil_smile casual far = ds_define_sprite('dv', 'evil_smile', dist='far', body_num=1, cloth='casual')
    image dv evil_smile modern = ds_define_sprite('dv', 'evil_smile', body_num=1, cloth='modern')
    image dv evil_smile modern close = ds_define_sprite('dv', 'evil_smile', dist='close', body_num=1, cloth='modern')
    image dv evil_smile modern far = ds_define_sprite('dv', 'evil_smile', dist='far', body_num=1, cloth='modern')
    image dv evil_smile pioneer = ds_define_sprite('dv', 'evil_smile', body_num=1, cloth='pioneer')
    image dv evil_smile pioneer close = ds_define_sprite('dv', 'evil_smile', dist='close', body_num=1, cloth='pioneer')
    image dv evil_smile pioneer far = ds_define_sprite('dv', 'evil_smile', dist='far', body_num=1, cloth='pioneer')
    image dv evil_smile pioneer2 = ds_define_sprite('dv', 'evil_smile', body_num=1, cloth='pioneer2')
    image dv evil_smile pioneer2 close = ds_define_sprite('dv', 'evil_smile', dist='close', body_num=1, cloth='pioneer2')
    image dv evil_smile pioneer2 far = ds_define_sprite('dv', 'evil_smile', dist='far', body_num=1, cloth='pioneer2')
    image dv evil_smile swim = ds_define_sprite('dv', 'evil_smile', body_num=1, cloth='swim')
    image dv evil_smile swim close = ds_define_sprite('dv', 'evil_smile', dist='close', body_num=1, cloth='swim')
    image dv evil_smile swim far = ds_define_sprite('dv', 'evil_smile', dist='far', body_num=1, cloth='swim')

    image dv think naked = ds_define_sprite('dv', 'think', body_num=1)
    image dv think casual = ds_define_sprite('dv', 'think', body_num=1, cloth='casual')
    image dv think modern = ds_define_sprite('dv', 'think', body_num=1, cloth='modern')
    image dv think pioneer = ds_define_sprite('dv', 'think', body_num=1, cloth='pioneer')
    image dv think pioneer2 = ds_define_sprite('dv', 'think', body_num=1, cloth='pioneer2')
    image dv think swim = ds_define_sprite('dv', 'think', body_num=1, cloth='swim')

    image dv think2 naked = ds_define_sprite('dv', 'think2', body_num=2)
    image dv think2 casual = ds_define_sprite('dv', 'think2', body_num=2, cloth='casual')
    image dv think2 modern = ds_define_sprite('dv', 'think2', body_num=2, cloth='modern')
    image dv think2 pioneer = ds_define_sprite('dv', 'think2', body_num=2, cloth='pioneer')
    image dv think2 pioneer2 = ds_define_sprite('dv', 'think2', body_num=2, cloth='pioneer2')
    image dv think2 swim = ds_define_sprite('dv', 'think2', body_num=2, cloth='swim')

    image dv cry_smile naked = ds_define_sprite('dv', 'cry_smile', body_num=3)
    image dv cry_smile casual = ds_define_sprite('dv', 'cry_smile', body_num=3, cloth='casual')
    image dv cry_smile modern = ds_define_sprite('dv', 'cry_smile', body_num=3, cloth='modern')
    image dv cry_smile pioneer = ds_define_sprite('dv', 'cry_smile', body_num=3, cloth='pioneer')
    image dv cry_smile pioneer2 = ds_define_sprite('dv', 'cry_smile', body_num=3, cloth='pioneer2')
    image dv cry_smile swim = ds_define_sprite('dv', 'cry_smile', body_num=3, cloth='swim')

    image dv closed_eyes naked = ds_define_sprite('dv', 'closed_eyes', body_num=3)
    image dv closed_eyes naked close = ds_define_sprite('dv', 'closed_eyes', dist='close', body_num=3)
    image dv closed_eyes casual = ds_define_sprite('dv', 'closed_eyes', body_num=3, cloth='casual')
    image dv closed_eyes modern = ds_define_sprite('dv', 'closed_eyes', body_num=3, cloth='modern')
    image dv closed_eyes modern close = ds_define_sprite('dv', 'closed_eyes', dist='close', body_num=3, cloth='modern')
    image dv closed_eyes pioneer = ds_define_sprite('dv', 'closed_eyes', body_num=3, cloth='pioneer')
    image dv closed_eyes pioneer close = ds_define_sprite('dv', 'closed_eyes', dist='close', body_num=3, cloth='pioneer')
    image dv closed_eyes pioneer2 = ds_define_sprite('dv', 'closed_eyes', body_num=3, cloth='pioneer2')
    image dv closed_eyes pioneer2 close = ds_define_sprite('dv', 'closed_eyes', dist='close', body_num=3, cloth='pioneer2')
    image dv closed_eyes swim = ds_define_sprite('dv', 'closed_eyes', body_num=3, cloth='swim')
    image dv closed_eyes swim close = ds_define_sprite('dv', 'closed_eyes', dist='close', body_num=3, cloth='swim')

    image dv shy2 naked = ds_define_sprite('dv', 'shy2', body_num=3)
    image dv shy2 naked far = ds_define_sprite('dv', 'shy2', dist='far', body_num=3)
    image dv shy2 casual = ds_define_sprite('dv', 'shy2', body_num=3, cloth='casual')
    image dv shy2 modern = ds_define_sprite('dv', 'shy2', body_num=3, cloth='modern')
    image dv shy2 modern far = ds_define_sprite('dv', 'shy2', dist='far', body_num=3, cloth='modern')
    image dv shy2 pioneer = ds_define_sprite('dv', 'shy2', body_num=3, cloth='pioneer')
    image dv shy2 pioneer far = ds_define_sprite('dv', 'shy2', dist='far', body_num=3, cloth='pioneer')
    image dv shy2 pioneer2 = ds_define_sprite('dv', 'shy2', body_num=3, cloth='pioneer2')
    image dv shy2 pioneer2 far = ds_define_sprite('dv', 'shy2', dist='far', body_num=3, cloth='pioneer2')
    image dv shy2 swim = ds_define_sprite('dv', 'shy2', body_num=3, cloth='swim')
    image dv shy2 swim far = ds_define_sprite('dv', 'shy2', dist='far', body_num=3, cloth='swim')

    image dv tired naked = ds_define_sprite('dv', 'tired', body_num=4)
    image dv tired naked far = ds_define_sprite('dv', 'tired', dist='far', body_num=4)
    image dv tired casual = ds_define_sprite('dv', 'tired', body_num=4, cloth='casual')
    image dv tired modern = ds_define_sprite('dv', 'tired', body_num=4, cloth='modern')
    image dv tired modern far = ds_define_sprite('dv', 'tired', dist='far', body_num=4, cloth='modern')
    image dv tired pioneer = ds_define_sprite('dv', 'tired', body_num=4, cloth='pioneer')
    image dv tired pioneer far = ds_define_sprite('dv', 'tired', dist='far', body_num=4, cloth='pioneer')
    image dv tired pioneer2 = ds_define_sprite('dv', 'tired', body_num=4, cloth='pioneer2')
    image dv tired pioneer2 far = ds_define_sprite('dv', 'tired', dist='far', body_num=4, cloth='pioneer2')
    image dv tired swim = ds_define_sprite('dv', 'tired', body_num=4, cloth='swim')
    image dv tired swim far = ds_define_sprite('dv', 'tired', dist='far', body_num=4, cloth='swim')

    image dv soft_smile naked = ds_define_sprite('dv', 'soft_smile', body_num=4)
    image dv soft_smile naked close = ds_define_sprite('dv', 'soft_smile', dist='close', body_num=4)
    image dv soft_smile naked far = ds_define_sprite('dv', 'soft_smile', dist='far', body_num=4)
    image dv soft_smile casual = ds_define_sprite('dv', 'soft_smile', body_num=4, cloth='casual')
    image dv soft_smile dress = ds_define_sprite('dv', 'soft_smile', body_num=4, cloth='dress')
    image dv soft_smile dress close = ds_define_sprite('dv', 'soft_smile', dist='close', body_num=4, cloth='dress')
    image dv soft_smile dress far = ds_define_sprite('dv', 'soft_smile', dist='far', body_num=4, cloth='dress')
    image dv soft_smile modern = ds_define_sprite('dv', 'soft_smile', body_num=4, cloth='modern')
    image dv soft_smile modern close = ds_define_sprite('dv', 'soft_smile', dist='close', body_num=4, cloth='modern')
    image dv soft_smile modern far = ds_define_sprite('dv', 'soft_smile', dist='far', body_num=4, cloth='modern')
    image dv soft_smile pioneer = ds_define_sprite('dv', 'soft_smile', body_num=4, cloth='pioneer')
    image dv soft_smile pioneer close = ds_define_sprite('dv', 'soft_smile', dist='close', body_num=4, cloth='pioneer')
    image dv soft_smile pioneer far = ds_define_sprite('dv', 'soft_smile', dist='far', body_num=4, cloth='pioneer')
    image dv soft_smile pioneer2 = ds_define_sprite('dv', 'soft_smile', body_num=4, cloth='pioneer2')
    image dv soft_smile pioneer2 close = ds_define_sprite('dv', 'soft_smile', dist='close', body_num=4, cloth='pioneer2')
    image dv soft_smile pioneer2 far = ds_define_sprite('dv', 'soft_smile', dist='far', body_num=4, cloth='pioneer2')
    image dv soft_smile swim = ds_define_sprite('dv', 'soft_smile', body_num=4, cloth='swim')
    image dv soft_smile swim close = ds_define_sprite('dv', 'soft_smile', dist='close', body_num=4, cloth='swim')
    image dv soft_smile swim far = ds_define_sprite('dv', 'soft_smile', dist='far', body_num=4, cloth='swim')

    image dv heart = ds_define_sprite('dv', 'grin', dist='far', body_num=2, body_name='heart')

    # Электроник

    image el angry modern = ds_define_sprite('el', 'angry', body_num=3, cloth='shirt_black')
    image el angry modern close = ds_define_sprite('el', 'angry', dist='close', body_num=3, cloth='shirt_black')
    image el angry modern far = ds_define_sprite('el', 'angry', dist='far', body_num=3, cloth='shirt_black')

    image el fingal modern = ds_define_sprite('el', 'fingal', body_num=2, cloth='shirt_black')
    image el fingal modern close = ds_define_sprite('el', 'fingal', dist='close', body_num=2, cloth='shirt_black')
    image el fingal modern far = ds_define_sprite('el', 'fingal', dist='far', body_num=2, cloth='shirt_black')

    image el grin modern = ds_define_sprite('el', 'grin', body_num=1, cloth='shirt_black')
    image el grin modern close = ds_define_sprite('el', 'grin', dist='close', body_num=1, cloth='shirt_black')
    image el grin modern far = ds_define_sprite('el', 'grin', dist='far', body_num=1, cloth='shirt_black')

    image el laugh modern = ds_define_sprite('el', 'laugh', body_num=3, cloth='shirt_black')
    image el laugh modern close = ds_define_sprite('el', 'laugh', dist='close', body_num=3, cloth='shirt_black')
    image el laugh modern far = ds_define_sprite('el', 'laugh', dist='far', body_num=3, cloth='shirt_black')

    image el normal modern = ds_define_sprite('el', 'normal', body_num=1, cloth='shirt_black')
    image el normal modern close = ds_define_sprite('el', 'normal', dist='close', body_num=1, cloth='shirt_black')
    image el normal modern far = ds_define_sprite('el', 'normal', dist='far', body_num=1, cloth='shirt_black')

    image el sad modern = ds_define_sprite('el', 'sad', body_num=2, cloth='shirt_black')
    image el sad modern close = ds_define_sprite('el', 'sad', dist='close', body_num=2, cloth='shirt_black')
    image el sad modern far = ds_define_sprite('el', 'sad', dist='far', body_num=2, cloth='shirt_black')

    image el scared modern = ds_define_sprite('el', 'scared', body_num=2, cloth='shirt_black')
    image el scared modern close = ds_define_sprite('el', 'scared', dist='close', body_num=2, cloth='shirt_black')
    image el scared modern far = ds_define_sprite('el', 'scared', dist='far', body_num=2, cloth='shirt_black')

    image el serious modern = ds_define_sprite('el', 'serious', body_num=3, cloth='shirt_black')
    image el serious modern close = ds_define_sprite('el', 'serious', dist='close', body_num=3, cloth='shirt_black')
    image el serious modern far = ds_define_sprite('el', 'serious', dist='far', body_num=3, cloth='shirt_black')

    image el shocked modern = ds_define_sprite('el', 'shocked', body_num=2, cloth='shirt_black')
    image el shocked modern close = ds_define_sprite('el', 'shocked', dist='close', body_num=2, cloth='shirt_black')
    image el shocked modern far = ds_define_sprite('el', 'shocked', dist='far', body_num=2, cloth='shirt_black')

    image el smile modern = ds_define_sprite('el', 'smile', body_num=1, cloth='shirt_black')
    image el smile modern close = ds_define_sprite('el', 'smile', dist='close', body_num=1, cloth='shirt_black')
    image el smile modern far = ds_define_sprite('el', 'smile', dist='far', body_num=1, cloth='shirt_black')

    image el surprise modern = ds_define_sprite('el', 'surprise', body_num=2, cloth='shirt_black')
    image el surprise modern close = ds_define_sprite('el', 'surprise', dist='close', body_num=2, cloth='shirt_black')
    image el surprise modern far = ds_define_sprite('el', 'surprise', dist='far', body_num=2, cloth='shirt_black')

    image el upset modern = ds_define_sprite('el', 'upset', body_num=2, cloth='shirt_black')
    image el upset modern close = ds_define_sprite('el', 'upset', dist='close', body_num=2, cloth='shirt_black')
    image el upset modern far = ds_define_sprite('el', 'upset', dist='far', body_num=2, cloth='shirt_black')

    # Мику

    image mi angry modern = ds_define_sprite('mi', 'angry', body_num=3, cloth='civil')
    image mi angry modern close = ds_define_sprite('mi', 'angry', dist='close', body_num=3, cloth='civil')
    image mi angry modern far = ds_define_sprite('mi', 'angry', dist='far', body_num=3, cloth='civil')

    image mi cry modern = ds_define_sprite('mi', 'cry', body_num=1, cloth='civil')
    image mi cry modern close = ds_define_sprite('mi', 'cry', dist='close', body_num=1, cloth='civil')
    image mi cry modern far = ds_define_sprite('mi', 'cry', dist='far', body_num=1, cloth='civil')

    image mi cry_smile modern = ds_define_sprite('mi', 'cry_smile', body_num=2, cloth='civil')
    image mi cry_smile modern close = ds_define_sprite('mi', 'cry_smile', dist='close', body_num=2, cloth='civil')
    image mi cry_smile modern far = ds_define_sprite('mi', 'cry_smile', dist='far', body_num=2, cloth='civil')

    image mi dontlike modern = ds_define_sprite('mi', 'dontlike', body_num=1, cloth='civil')
    image mi dontlike modern close = ds_define_sprite('mi', 'dontlike', dist='close', body_num=1, cloth='civil')
    image mi dontlike modern far = ds_define_sprite('mi', 'dontlike', dist='far', body_num=1, cloth='civil')

    image mi grin modern = ds_define_sprite('mi', 'grin', body_num=2, cloth='civil')
    image mi grin modern close = ds_define_sprite('mi', 'grin', dist='close', body_num=2, cloth='civil')
    image mi grin modern far = ds_define_sprite('mi', 'grin', dist='far', body_num=2, cloth='civil')

    image mi happy modern = ds_define_sprite('mi', 'happy', body_num=2, cloth='civil')
    image mi happy modern close = ds_define_sprite('mi', 'happy', dist='close', body_num=2, cloth='civil')
    image mi happy modern far = ds_define_sprite('mi', 'happy', dist='far', body_num=2, cloth='civil')

    image mi laugh modern = ds_define_sprite('mi', 'laugh', body_num=1, cloth='civil')
    image mi laugh modern close = ds_define_sprite('mi', 'laugh', dist='close', body_num=1, cloth='civil')
    image mi laugh modern far = ds_define_sprite('mi', 'laugh', dist='far', body_num=1, cloth='civil')

    image mi normal modern = ds_define_sprite('mi', 'normal', body_num=3, cloth='civil')
    image mi normal modern close = ds_define_sprite('mi', 'normal', dist='close', body_num=3, cloth='civil')
    image mi normal modern far = ds_define_sprite('mi', 'normal', dist='far', body_num=3, cloth='civil')

    image mi rage modern = ds_define_sprite('mi', 'rage', body_num=3, cloth='civil')
    image mi rage modern close = ds_define_sprite('mi', 'rage', dist='close', body_num=3, cloth='civil')
    image mi rage modern far = ds_define_sprite('mi', 'rage', dist='far', body_num=3, cloth='civil')

    image mi sad modern = ds_define_sprite('mi', 'sad', body_num=2, cloth='civil')
    image mi sad modern close = ds_define_sprite('mi', 'sad', dist='close', body_num=2, cloth='civil')
    image mi sad modern far = ds_define_sprite('mi', 'sad', dist='far', body_num=2, cloth='civil')

    image mi scared modern = ds_define_sprite('mi', 'scared', body_num=1, cloth='civil')
    image mi scared modern close = ds_define_sprite('mi', 'scared', dist='close', body_num=1, cloth='civil')
    image mi scared modern far = ds_define_sprite('mi', 'scared', dist='far', body_num=1, cloth='civil')

    image mi serious modern = ds_define_sprite('mi', 'serious', body_num=3, cloth='civil')
    image mi serious modern close = ds_define_sprite('mi', 'serious', dist='close', body_num=3, cloth='civil')
    image mi serious modern far = ds_define_sprite('mi', 'serious', dist='far', body_num=3, cloth='civil')

    image mi shocked modern = ds_define_sprite('mi', 'shocked', body_num=1, cloth='civil')
    image mi shocked modern close = ds_define_sprite('mi', 'shocked', dist='close', body_num=1, cloth='civil')
    image mi shocked modern far = ds_define_sprite('mi', 'shocked', dist='far', body_num=1, cloth='civil')

    image mi shy modern = ds_define_sprite('mi', 'shy', body_num=1, cloth='civil')
    image mi shy modern close = ds_define_sprite('mi', 'shy', dist='close', body_num=1, cloth='civil')
    image mi shy modern far = ds_define_sprite('mi', 'shy', dist='far', body_num=1, cloth='civil')

    image mi smile modern = ds_define_sprite('mi', 'smile', body_num=2, cloth='civil')
    image mi smile modern close = ds_define_sprite('mi', 'smile', dist='close', body_num=2, cloth='civil')
    image mi smile modern far = ds_define_sprite('mi', 'smile', dist='far', body_num=2, cloth='civil')

    image mi surprise modern = ds_define_sprite('mi', 'surprise', body_num=1, cloth='civil')
    image mi surprise modern close = ds_define_sprite('mi', 'surprise', dist='close', body_num=1, cloth='civil')
    image mi surprise modern far = ds_define_sprite('mi', 'surprise', dist='far', body_num=1, cloth='civil')

    image mi upset modern = ds_define_sprite('mi', 'upset', body_num=3, cloth='civil')
    image mi upset modern close = ds_define_sprite('mi', 'upset', dist='close', body_num=3, cloth='civil')
    image mi upset modern far = ds_define_sprite('mi', 'upset', dist='far', body_num=3, cloth='civil')

    # ОД
    image mt angry night = ds_define_sprite('mt', 'angry', body_num=2, cloth='nightdress')
    image mt angry night close = ds_define_sprite('mt', 'angry', dist='close', body_num=2, cloth='nightdress')
    image mt angry night far = ds_define_sprite('mt', 'angry', dist='far', body_num=2, cloth='nightdress')

    image mt grin night = ds_define_sprite('mt', 'grin', body_num=3, cloth='nightdress')
    image mt grin night close = ds_define_sprite('mt', 'grin', dist='close', body_num=3, cloth='nightdress')
    image mt grin night far = ds_define_sprite('mt', 'grin', dist='far', body_num=3, cloth='nightdress')

    image mt laugh night = ds_define_sprite('mt', 'laugh', body_num=3, cloth='nightdress')
    image mt laugh night close = ds_define_sprite('mt', 'laugh', dist='close', body_num=3, cloth='nightdress')
    image mt laugh night far = ds_define_sprite('mt', 'laugh', dist='far', body_num=3, cloth='nightdress')

    image mt normal night = ds_define_sprite('mt', 'normal', body_num=1, cloth='nightdress')
    image mt normal night close = ds_define_sprite('mt', 'normal', dist='close', body_num=1, cloth='nightdress')
    image mt normal night far = ds_define_sprite('mt', 'normal', dist='far', body_num=1, cloth='nightdress')

    image mt rage night = ds_define_sprite('mt', 'rage', body_num=2, cloth='nightdress')
    image mt rage night close = ds_define_sprite('mt', 'rage', dist='close', body_num=2, cloth='nightdress')
    image mt rage night far = ds_define_sprite('mt', 'rage', dist='far', body_num=2, cloth='nightdress')

    image mt sad night = ds_define_sprite('mt', 'sad', body_num=1, cloth='nightdress')
    image mt sad night close = ds_define_sprite('mt', 'sad', dist='close', body_num=1, cloth='nightdress')
    image mt sad night far = ds_define_sprite('mt', 'sad', dist='far', body_num=1, cloth='nightdress')

    image mt scared night = ds_define_sprite('mt', 'scared', body_num=3, cloth='nightdress')
    image mt scared night close = ds_define_sprite('mt', 'scared', dist='close', body_num=3, cloth='nightdress')
    image mt scared night far = ds_define_sprite('mt', 'scared', dist='far', body_num=3, cloth='nightdress')

    image mt shocked night = ds_define_sprite('mt', 'shocked', body_num=2, cloth='nightdress')
    image mt shocked night close = ds_define_sprite('mt', 'shocked', dist='close', body_num=2, cloth='nightdress')
    image mt shocked night far = ds_define_sprite('mt', 'shocked', dist='far', body_num=2, cloth='nightdress')

    image mt smile night = ds_define_sprite('mt', 'smile', body_num=1, cloth='nightdress')
    image mt smile night close = ds_define_sprite('mt', 'smile', dist='close', body_num=1, cloth='nightdress')
    image mt smile night far = ds_define_sprite('mt', 'smile', dist='far', body_num=1, cloth='nightdress')

    image mt surprise night = ds_define_sprite('mt', 'surprise', body_num=1, cloth='nightdress')
    image mt surprise night close = ds_define_sprite('mt', 'surprise', dist='close', body_num=1, cloth='nightdress')
    image mt surprise night far = ds_define_sprite('mt', 'surprise', dist='far', body_num=1, cloth='nightdress')

    # Женя

    image mz amazed naked = ds_define_sprite('mz', 'amazed', body_num=1)
    image mz amazed glasses body = ds_define_sprite('mz', 'amazed', body_num=1, cloth='body', acc='glasses')
    image mz amazed naked far = ds_define_sprite('mz', 'amazed', body_num=1, dist='far')
    image mz amazed glasses naked far = ds_define_sprite('mz', 'amazed', body_num=1, dist='far', acc='glasses')
    image mz amazed naked close = ds_define_sprite('mz', 'amazed', body_num=1, dist='close')
    image mz amazed glasses naked close = ds_define_sprite('mz', 'amazed', body_num=1, dist='close', acc='glasses')
    
    image mz amazed pioneer  = ds_define_sprite('mz', 'amazed', body_num=1, cloth='pioneer')
    image mz amazed glasses pioneer = ds_define_sprite('mz', 'amazed', body_num=1, cloth='pioneer', acc='glasses')
    image mz amazed pioneer far = ds_define_sprite('mz', 'amazed', body_num=1, dist='far', cloth='pioneer')
    image mz amazed glasses pioneer far = ds_define_sprite('mz', 'amazed', body_num=1, dist='far', cloth='pioneer', acc='glasses')
    image mz amazed pioneer close = ds_define_sprite('mz', 'amazed', body_num=1, dist='close', cloth='pioneer')
    image mz amazed glasses pioneer close = ds_define_sprite('mz', 'amazed', body_num=1, dist='close', cloth='pioneer', acc='glasses')
    
    image mz amazed swimsuit = ds_define_sprite('mz', 'amazed', body_num=1, cloth='swimsuit')
    image mz amazed glasses swimsuit = ds_define_sprite('mz', 'amazed', body_num=1, cloth='swimsuit', acc='glasses')
    image mz amazed swimsuit far = ds_define_sprite('mz', 'amazed', body_num=1, dist='far', cloth='swimsuit')
    image mz amazed glasses swimsuit far = ds_define_sprite('mz', 'amazed', body_num=1, dist='far', cloth='swimsuit', acc='glasses')
    image mz amazed swimsuit close = ds_define_sprite('mz', 'amazed', body_num=1, dist='close', cloth='swimsuit')
    image mz amazed glasses swimsuit close = ds_define_sprite('mz', 'amazed', body_num=1, dist='close', cloth='swimsuit', acc='glasses')
    
    image mz amazed pullover  = ds_define_sprite('mz', 'amazed', body_num=1, cloth='pullover')
    image mz amazed glasses pullover = ds_define_sprite('mz', 'amazed', body_num=1, cloth='pullover', acc='glasses')
    image mz amazed pullover far = ds_define_sprite('mz', 'amazed', body_num=1, dist='far', cloth='pullover')
    image mz amazed glasses pullover far = ds_define_sprite('mz', 'amazed', body_num=1, dist='far', cloth='pullover', acc='glasses')
    image mz amazed pullover close = ds_define_sprite('mz', 'amazed', body_num=1, dist='close', cloth='pullover')
    image mz amazed glasses pullover close = ds_define_sprite('mz', 'amazed', body_num=1, dist='close', cloth='pullover', acc='glasses')
    
    image mz bukal naked = ds_define_sprite('mz', 'bukal', body_num=1)
    image mz bukal glasses body = ds_define_sprite('mz', 'bukal', body_num=1, cloth='body', acc='glasses')
    image mz bukal naked far = ds_define_sprite('mz', 'bukal', body_num=1, dist='far')
    image mz bukal glasses naked far = ds_define_sprite('mz', 'bukal', body_num=1, dist='far', acc='glasses')
    image mz bukal naked close = ds_define_sprite('mz', 'bukal', body_num=1, dist='close')
    image mz bukal glasses naked close = ds_define_sprite('mz', 'bukal', body_num=1, dist='close', acc='glasses')
    
    image mz bukal pioneer  = ds_define_sprite('mz', 'bukal', body_num=1, cloth='pioneer')
    image mz bukal glasses pioneer = ds_define_sprite('mz', 'bukal', body_num=1, cloth='pioneer', acc='glasses')
    image mz bukal pioneer far = ds_define_sprite('mz', 'bukal', body_num=1, dist='far', cloth='pioneer')
    image mz bukal glasses pioneer far = ds_define_sprite('mz', 'bukal', body_num=1, dist='far', cloth='pioneer', acc='glasses')
    image mz bukal pioneer close = ds_define_sprite('mz', 'bukal', body_num=1, dist='close', cloth='pioneer')
    image mz bukal glasses pioneer close = ds_define_sprite('mz', 'bukal', body_num=1, dist='close', cloth='pioneer', acc='glasses')
    
    image mz bukal swimsuit  = ds_define_sprite('mz', 'bukal', body_num=1, cloth='swimsuit')
    image mz bukal glasses swimsuit = ds_define_sprite('mz', 'bukal', body_num=1, cloth='swimsuit', acc='glasses')
    image mz bukal swimsuit far = ds_define_sprite('mz', 'bukal', body_num=1, dist='far', cloth='swimsuit')
    image mz bukal glasses swimsuit far = ds_define_sprite('mz', 'bukal', body_num=1, dist='far', cloth='swimsuit', acc='glasses')
    image mz bukal swimsuit close = ds_define_sprite('mz', 'bukal', body_num=1, dist='close', cloth='swimsuit')
    image mz bukal glasses swimsuit close = ds_define_sprite('mz', 'bukal', body_num=1, dist='close', cloth='swimsuit', acc='glasses')
    
    image mz bukal pullover  = ds_define_sprite('mz', 'bukal', body_num=1, cloth='pullover')
    image mz bukal glasses pullover = ds_define_sprite('mz', 'bukal', body_num=1, cloth='pullover', acc='glasses')
    image mz bukal pullover far = ds_define_sprite('mz', 'bukal', body_num=1, dist='far', cloth='pullover')
    image mz bukal glasses pullover far = ds_define_sprite('mz', 'bukal', body_num=1, dist='far', cloth='pullover', acc='glasses')
    image mz bukal pullover close = ds_define_sprite('mz', 'bukal', body_num=1, dist='close', cloth='pullover')
    image mz bukal glasses pullover close = ds_define_sprite('mz', 'bukal', body_num=1, dist='close', cloth='pullover', acc='glasses')
    
    image mz laugh naked = ds_define_sprite('mz', 'laugh', body_num=1)
    image mz laugh glasses body = ds_define_sprite('mz', 'laugh', body_num=1, cloth='body', acc='glasses')
    image mz laugh naked far = ds_define_sprite('mz', 'laugh', body_num=1, dist='far')
    image mz laugh glasses naked far = ds_define_sprite('mz', 'laugh', body_num=1, dist='far', acc='glasses')
    image mz laugh naked close = ds_define_sprite('mz', 'laugh', body_num=1, dist='close')
    image mz laugh glasses naked close = ds_define_sprite('mz', 'laugh', body_num=1, dist='close', acc='glasses')
    
    image mz laugh pioneer  = ds_define_sprite('mz', 'laugh', body_num=1, cloth='pioneer')
    image mz laugh glasses pioneer = ds_define_sprite('mz', 'laugh', body_num=1, cloth='pioneer', acc='glasses')
    image mz laugh pioneer far = ds_define_sprite('mz', 'laugh', body_num=1, dist='far', cloth='pioneer')
    image mz laugh glasses pioneer far = ds_define_sprite('mz', 'laugh', body_num=1, dist='far', cloth='pioneer', acc='glasses')
    image mz laugh pioneer close = ds_define_sprite('mz', 'laugh', body_num=1, dist='close', cloth='pioneer')
    image mz laugh glasses pioneer close = ds_define_sprite('mz', 'laugh', body_num=1, dist='close', cloth='pioneer', acc='glasses')
    
    image mz laugh swimsuit  = ds_define_sprite('mz', 'laugh', body_num=1, cloth='swimsuit')
    image mz laugh glasses swimsuit = ds_define_sprite('mz', 'laugh', body_num=1, cloth='swimsuit', acc='glasses')
    image mz laugh swimsuit far = ds_define_sprite('mz', 'laugh', body_num=1, dist='far', cloth='swimsuit')
    image mz laugh glasses swimsuit far = ds_define_sprite('mz', 'laugh', body_num=1, dist='far', cloth='swimsuit', acc='glasses')
    image mz laugh swimsuit close = ds_define_sprite('mz', 'laugh', body_num=1, dist='close', cloth='swimsuit')
    image mz laugh glasses swimsuit close = ds_define_sprite('mz', 'laugh', body_num=1, dist='close', cloth='swimsuit', acc='glasses')
    
    image mz laugh pullover  = ds_define_sprite('mz', 'laugh', body_num=1, cloth='pullover')
    image mz laugh glasses pullover = ds_define_sprite('mz', 'laugh', body_num=1, cloth='pullover', acc='glasses')
    image mz laugh pullover far = ds_define_sprite('mz', 'laugh', body_num=1, dist='far', cloth='pullover')
    image mz laugh glasses pullover far = ds_define_sprite('mz', 'laugh', body_num=1, dist='far', cloth='pullover', acc='glasses')
    image mz laugh pullover close = ds_define_sprite('mz', 'laugh', body_num=1, dist='close', cloth='pullover')
    image mz laugh glasses pullover close = ds_define_sprite('mz', 'laugh', body_num=1, dist='close', cloth='pullover', acc='glasses')
    
    image mz normal naked = ds_define_sprite('mz', 'normal', body_num=1)
    image mz normal glasses body = ds_define_sprite('mz', 'normal', body_num=1, cloth='body', acc='glasses')
    image mz normal naked far = ds_define_sprite('mz', 'normal', body_num=1, dist='far')
    image mz normal glasses naked far = ds_define_sprite('mz', 'normal', body_num=1, dist='far', acc='glasses')
    image mz normal naked close = ds_define_sprite('mz', 'normal', body_num=1, dist='close')
    image mz normal glasses naked close = ds_define_sprite('mz', 'normal', body_num=1, dist='close', acc='glasses')
    
    image mz normal pioneer  = ds_define_sprite('mz', 'normal', body_num=1, cloth='pioneer')
    image mz normal glasses pioneer = ds_define_sprite('mz', 'normal', body_num=1, cloth='pioneer', acc='glasses')
    image mz normal pioneer far = ds_define_sprite('mz', 'normal', body_num=1, dist='far', cloth='pioneer')
    image mz normal glasses pioneer far = ds_define_sprite('mz', 'normal', body_num=1, dist='far', cloth='pioneer', acc='glasses')
    image mz normal pioneer close = ds_define_sprite('mz', 'normal', body_num=1, dist='close', cloth='pioneer')
    image mz normal glasses pioneer close = ds_define_sprite('mz', 'normal', body_num=1, dist='close', cloth='pioneer', acc='glasses')
    
    image mz normal swimsuit  = ds_define_sprite('mz', 'normal', body_num=1, cloth='swimsuit')
    image mz normal glasses swimsuit = ds_define_sprite('mz', 'normal', body_num=1, cloth='swimsuit', acc='glasses')
    image mz normal swimsuit far = ds_define_sprite('mz', 'normal', body_num=1, dist='far', cloth='swimsuit')
    image mz normal glasses swimsuit far = ds_define_sprite('mz', 'normal', body_num=1, dist='far', cloth='swimsuit', acc='glasses')
    image mz normal swimsuit close = ds_define_sprite('mz', 'normal', body_num=1, dist='close', cloth='swimsuit')
    image mz normal glasses swimsuit close = ds_define_sprite('mz', 'normal', body_num=1, dist='close', cloth='swimsuit', acc='glasses')
    
    image mz normal pullover  = ds_define_sprite('mz', 'normal', body_num=1, cloth='pullover')
    image mz normal glasses pullover = ds_define_sprite('mz', 'normal', body_num=1, cloth='pullover', acc='glasses')
    image mz normal pullover far = ds_define_sprite('mz', 'normal', body_num=1, dist='far', cloth='pullover')
    image mz normal glasses pullover far = ds_define_sprite('mz', 'normal', body_num=1, dist='far', cloth='pullover', acc='glasses')
    image mz normal pullover close = ds_define_sprite('mz', 'normal', body_num=1, dist='close', cloth='pullover')
    image mz normal glasses pullover close = ds_define_sprite('mz', 'normal', body_num=1, dist='close', cloth='pullover', acc='glasses')
    
    image mz fun naked = ds_define_sprite('mz', 'fun', body_num=1)
    image mz fun glasses body = ds_define_sprite('mz', 'fun', body_num=1, cloth='body', acc='glasses')
    image mz fun naked far = ds_define_sprite('mz', 'fun', body_num=1, dist='far')
    image mz fun glasses naked far = ds_define_sprite('mz', 'fun', body_num=1, dist='far', acc='glasses')
    image mz fun naked close = ds_define_sprite('mz', 'fun', body_num=1, dist='close')
    image mz fun glasses naked close = ds_define_sprite('mz', 'fun', body_num=1, dist='close', acc='glasses')
    
    image mz fun pioneer  = ds_define_sprite('mz', 'fun', body_num=1, cloth='pioneer')
    image mz fun glasses pioneer = ds_define_sprite('mz', 'fun', body_num=1, cloth='pioneer', acc='glasses')
    image mz fun pioneer far = ds_define_sprite('mz', 'fun', body_num=1, dist='far', cloth='pioneer')
    image mz fun glasses pioneer far = ds_define_sprite('mz', 'fun', body_num=1, dist='far', cloth='pioneer', acc='glasses')
    image mz fun pioneer close = ds_define_sprite('mz', 'fun', body_num=1, dist='close', cloth='pioneer')
    image mz fun glasses pioneer close = ds_define_sprite('mz', 'fun', body_num=1, dist='close', cloth='pioneer', acc='glasses')
    
    image mz fun swimsuit  = ds_define_sprite('mz', 'fun', body_num=1, cloth='swimsuit')
    image mz fun glasses swimsuit = ds_define_sprite('mz', 'fun', body_num=1, cloth='swimsuit', acc='glasses')
    image mz fun swimsuit far = ds_define_sprite('mz', 'fun', body_num=1, dist='far', cloth='swimsuit')
    image mz fun glasses swimsuit far = ds_define_sprite('mz', 'fun', body_num=1, dist='far', cloth='swimsuit', acc='glasses')
    image mz fun swimsuit close = ds_define_sprite('mz', 'fun', body_num=1, dist='close', cloth='swimsuit')
    image mz fun glasses swimsuit close = ds_define_sprite('mz', 'fun', body_num=1, dist='close', cloth='swimsuit', acc='glasses')
    
    image mz fun pullover  = ds_define_sprite('mz', 'fun', body_num=1, cloth='pullover')
    image mz fun glasses pullover = ds_define_sprite('mz', 'fun', body_num=1, cloth='pullover', acc='glasses')
    image mz fun pullover far = ds_define_sprite('mz', 'fun', body_num=1, dist='far', cloth='pullover')
    image mz fun glasses pullover far = ds_define_sprite('mz', 'fun', body_num=1, dist='far', cloth='pullover', acc='glasses')
    image mz fun pullover close = ds_define_sprite('mz', 'fun', body_num=1, dist='close', cloth='pullover')
    image mz fun glasses pullover close = ds_define_sprite('mz', 'fun', body_num=1, dist='close', cloth='pullover', acc='glasses')
    
    image mz sad naked = ds_define_sprite('mz', 'sad', body_num=1)
    image mz sad glasses body = ds_define_sprite('mz', 'sad', body_num=1, cloth='body', acc='glasses')
    image mz sad naked far = ds_define_sprite('mz', 'sad', body_num=1, dist='far')
    image mz sad glasses naked far = ds_define_sprite('mz', 'sad', body_num=1, dist='far', acc='glasses')
    image mz sad naked close = ds_define_sprite('mz', 'sad', body_num=1, dist='close')
    image mz sad glasses naked close = ds_define_sprite('mz', 'sad', body_num=1, dist='close', acc='glasses')
    
    image mz sad pioneer  = ds_define_sprite('mz', 'sad', body_num=1, cloth='pioneer')
    image mz sad glasses pioneer = ds_define_sprite('mz', 'sad', body_num=1, cloth='pioneer', acc='glasses')
    image mz sad pioneer far = ds_define_sprite('mz', 'sad', body_num=1, dist='far', cloth='pioneer')
    image mz sad glasses pioneer far = ds_define_sprite('mz', 'sad', body_num=1, dist='far', cloth='pioneer', acc='glasses')
    image mz sad pioneer close = ds_define_sprite('mz', 'sad', body_num=1, dist='close', cloth='pioneer')
    image mz sad glasses pioneer close = ds_define_sprite('mz', 'sad', body_num=1, dist='close', cloth='pioneer', acc='glasses')
    
    image mz sad swimsuit  = ds_define_sprite('mz', 'sad', body_num=1, cloth='swimsuit')
    image mz sad glasses swimsuit = ds_define_sprite('mz', 'sad', body_num=1, cloth='swimsuit', acc='glasses')
    image mz sad swimsuit far = ds_define_sprite('mz', 'sad', body_num=1, dist='far', cloth='swimsuit')
    image mz sad glasses swimsuit far = ds_define_sprite('mz', 'sad', body_num=1, dist='far', cloth='swimsuit', acc='glasses')
    image mz sad swimsuit close = ds_define_sprite('mz', 'sad', body_num=1, dist='close', cloth='swimsuit')
    image mz sad glasses swimsuit close = ds_define_sprite('mz', 'sad', body_num=1, dist='close', cloth='swimsuit', acc='glasses')
    
    image mz sad pullover  = ds_define_sprite('mz', 'sad', body_num=1, cloth='pullover')
    image mz sad glasses pullover = ds_define_sprite('mz', 'sad', body_num=1, cloth='pullover', acc='glasses')
    image mz sad pullover far = ds_define_sprite('mz', 'sad', body_num=1, dist='far', cloth='pullover')
    image mz sad glasses pullover far = ds_define_sprite('mz', 'sad', body_num=1, dist='far', cloth='pullover', acc='glasses')
    image mz sad pullover close = ds_define_sprite('mz', 'sad', body_num=1, dist='close', cloth='pullover')
    image mz sad glasses pullover close = ds_define_sprite('mz', 'sad', body_num=1, dist='close', cloth='pullover', acc='glasses')
    
    image mz hope naked = ds_define_sprite('mz', 'hope', body_num=1)
    image mz hope glasses body = ds_define_sprite('mz', 'hope', body_num=1, cloth='body', acc='glasses')
    image mz hope naked far = ds_define_sprite('mz', 'hope', body_num=1, dist='far')
    image mz hope glasses naked far = ds_define_sprite('mz', 'hope', body_num=1, dist='far', acc='glasses')
    image mz hope naked close = ds_define_sprite('mz', 'hope', body_num=1, dist='close')
    image mz hope glasses naked close = ds_define_sprite('mz', 'hope', body_num=1, dist='close', acc='glasses')
    
    image mz hope pioneer  = ds_define_sprite('mz', 'hope', body_num=1, cloth='pioneer')
    image mz hope glasses pioneer = ds_define_sprite('mz', 'hope', body_num=1, cloth='pioneer', acc='glasses')
    image mz hope pioneer far = ds_define_sprite('mz', 'hope', body_num=1, dist='far', cloth='pioneer')
    image mz hope glasses pioneer far = ds_define_sprite('mz', 'hope', body_num=1, dist='far', cloth='pioneer', acc='glasses')
    image mz hope pioneer close = ds_define_sprite('mz', 'hope', body_num=1, dist='close', cloth='pioneer')
    image mz hope glasses pioneer close = ds_define_sprite('mz', 'hope', body_num=1, dist='close', cloth='pioneer', acc='glasses')
    
    image mz hope swimsuit  = ds_define_sprite('mz', 'hope', body_num=1, cloth='swimsuit')
    image mz hope glasses swimsuit = ds_define_sprite('mz', 'hope', body_num=1, cloth='swimsuit', acc='glasses')
    image mz hope swimsuit far = ds_define_sprite('mz', 'hope', body_num=1, dist='far', cloth='swimsuit')
    image mz hope glasses swimsuit far = ds_define_sprite('mz', 'hope', body_num=1, dist='far', cloth='swimsuit', acc='glasses')
    image mz hope swimsuit close = ds_define_sprite('mz', 'hope', body_num=1, dist='close', cloth='swimsuit')
    image mz hope glasses swimsuit close = ds_define_sprite('mz', 'hope', body_num=1, dist='close', cloth='swimsuit', acc='glasses')
    
    image mz hope pullover  = ds_define_sprite('mz', 'hope', body_num=1, cloth='pullover')
    image mz hope glasses pullover = ds_define_sprite('mz', 'hope', body_num=1, cloth='pullover', acc='glasses')
    image mz hope pullover far = ds_define_sprite('mz', 'hope', body_num=1, dist='far', cloth='pullover')
    image mz hope glasses pullover far = ds_define_sprite('mz', 'hope', body_num=1, dist='far', cloth='pullover', acc='glasses')
    image mz hope pullover close = ds_define_sprite('mz', 'hope', body_num=1, dist='close', cloth='pullover')
    image mz hope glasses pullover close = ds_define_sprite('mz', 'hope', body_num=1, dist='close', cloth='pullover', acc='glasses')
    
    image mz sceptic naked = ds_define_sprite('mz', 'sceptic', body_num=1)
    image mz sceptic glasses body = ds_define_sprite('mz', 'sceptic', body_num=1, cloth='body', acc='glasses')
    image mz sceptic naked far = ds_define_sprite('mz', 'sceptic', body_num=1, dist='far')
    image mz sceptic glasses naked far = ds_define_sprite('mz', 'sceptic', body_num=1, dist='far', acc='glasses')
    image mz sceptic naked close = ds_define_sprite('mz', 'sceptic', body_num=1, dist='close')
    image mz sceptic glasses naked close = ds_define_sprite('mz', 'sceptic', body_num=1, dist='close', acc='glasses')
    
    image mz sceptic pioneer  = ds_define_sprite('mz', 'sceptic', body_num=1, cloth='pioneer')
    image mz sceptic glasses pioneer = ds_define_sprite('mz', 'sceptic', body_num=1, cloth='pioneer', acc='glasses')
    image mz sceptic pioneer far = ds_define_sprite('mz', 'sceptic', body_num=1, dist='far', cloth='pioneer')
    image mz sceptic glasses pioneer far = ds_define_sprite('mz', 'sceptic', body_num=1, dist='far', cloth='pioneer', acc='glasses')
    image mz sceptic pioneer close = ds_define_sprite('mz', 'sceptic', body_num=1, dist='close', cloth='pioneer')
    image mz sceptic glasses pioneer close = ds_define_sprite('mz', 'sceptic', body_num=1, dist='close', cloth='pioneer', acc='glasses')
    
    image mz sceptic swimsuit  = ds_define_sprite('mz', 'sceptic', body_num=1, cloth='swimsuit')
    image mz sceptic glasses swimsuit = ds_define_sprite('mz', 'sceptic', body_num=1, cloth='swimsuit', acc='glasses')
    image mz sceptic swimsuit far = ds_define_sprite('mz', 'sceptic', body_num=1, dist='far', cloth='swimsuit')
    image mz sceptic glasses swimsuit far = ds_define_sprite('mz', 'sceptic', body_num=1, dist='far', cloth='swimsuit', acc='glasses')
    image mz sceptic swimsuit close = ds_define_sprite('mz', 'sceptic', body_num=1, dist='close', cloth='swimsuit')
    image mz sceptic glasses swimsuit close = ds_define_sprite('mz', 'sceptic', body_num=1, dist='close', cloth='swimsuit', acc='glasses')
    
    image mz sceptic pullover  = ds_define_sprite('mz', 'sceptic', body_num=1, cloth='pullover')
    image mz sceptic glasses pullover = ds_define_sprite('mz', 'sceptic', body_num=1, cloth='pullover', acc='glasses')
    image mz sceptic pullover far = ds_define_sprite('mz', 'sceptic', body_num=1, dist='far', cloth='pullover')
    image mz sceptic glasses pullover far = ds_define_sprite('mz', 'sceptic', body_num=1, dist='far', cloth='pullover', acc='glasses')
    image mz sceptic pullover close = ds_define_sprite('mz', 'sceptic', body_num=1, dist='close', cloth='pullover')
    image mz sceptic glasses pullover close = ds_define_sprite('mz', 'sceptic', body_num=1, dist='close', cloth='pullover', acc='glasses')
    
    image mz angry naked = ds_define_sprite('mz', 'angry', body_num=2)
    image mz angry glasses body = ds_define_sprite('mz', 'angry', body_num=2, cloth='body', acc='glasses')
    image mz angry naked far = ds_define_sprite('mz', 'angry', body_num=2, dist='far')
    image mz angry glasses naked far = ds_define_sprite('mz', 'angry', body_num=2, dist='far', acc='glasses')
    image mz angry naked close = ds_define_sprite('mz', 'angry', body_num=2, dist='close')
    image mz angry glasses naked close = ds_define_sprite('mz', 'angry', body_num=2, dist='close', acc='glasses')
    
    image mz angry pioneer  = ds_define_sprite('mz', 'angry', body_num=2, cloth='pioneer')
    image mz angry glasses pioneer = ds_define_sprite('mz', 'angry', body_num=2, cloth='pioneer', acc='glasses')
    image mz angry pioneer far = ds_define_sprite('mz', 'angry', body_num=2, dist='far', cloth='pioneer')
    image mz angry glasses pioneer far = ds_define_sprite('mz', 'angry', body_num=2, dist='far', cloth='pioneer', acc='glasses')
    image mz angry pioneer close = ds_define_sprite('mz', 'angry', body_num=2, dist='close', cloth='pioneer')
    image mz angry glasses pioneer close = ds_define_sprite('mz', 'angry', body_num=2, dist='close', cloth='pioneer', acc='glasses')
    
    image mz angry swimsuit  = ds_define_sprite('mz', 'angry', body_num=2, cloth='swimsuit')
    image mz angry glasses swimsuit = ds_define_sprite('mz', 'angry', body_num=2, cloth='swimsuit', acc='glasses')
    image mz angry swimsuit far = ds_define_sprite('mz', 'angry', body_num=2, dist='far', cloth='swimsuit')
    image mz angry glasses swimsuit far = ds_define_sprite('mz', 'angry', body_num=2, dist='far', cloth='swimsuit', acc='glasses')
    image mz angry swimsuit close = ds_define_sprite('mz', 'angry', body_num=2, dist='close', cloth='swimsuit')
    image mz angry glasses swimsuit close = ds_define_sprite('mz', 'angry', body_num=2, dist='close', cloth='swimsuit', acc='glasses')
    
    image mz angry pullover  = ds_define_sprite('mz', 'angry', body_num=2, cloth='pullover')
    image mz angry glasses pullover = ds_define_sprite('mz', 'angry', body_num=2, cloth='pullover', acc='glasses')
    image mz angry pullover far = ds_define_sprite('mz', 'angry', body_num=2, dist='far', cloth='pullover')
    image mz angry glasses pullover far = ds_define_sprite('mz', 'angry', body_num=2, dist='far', cloth='pullover', acc='glasses')
    image mz angry pullover close = ds_define_sprite('mz', 'angry', body_num=2, dist='close', cloth='pullover')
    image mz angry glasses pullover close = ds_define_sprite('mz', 'angry', body_num=2, dist='close', cloth='pullover', acc='glasses')
    
    image mz cry naked = ds_define_sprite('mz', 'cry', body_num=2)
    image mz cry glasses body = ds_define_sprite('mz', 'cry', body_num=2, cloth='body', acc='glasses')
    image mz cry naked far = ds_define_sprite('mz', 'cry', body_num=2, dist='far')
    image mz cry glasses naked far = ds_define_sprite('mz', 'cry', body_num=2, dist='far', acc='glasses')
    image mz cry naked close = ds_define_sprite('mz', 'cry', body_num=2, dist='close')
    image mz cry glasses naked close = ds_define_sprite('mz', 'cry', body_num=2, dist='close', acc='glasses')
    
    image mz cry pioneer  = ds_define_sprite('mz', 'cry', body_num=2, cloth='pioneer')
    image mz cry glasses pioneer = ds_define_sprite('mz', 'cry', body_num=2, cloth='pioneer', acc='glasses')
    image mz cry pioneer far = ds_define_sprite('mz', 'cry', body_num=2, dist='far', cloth='pioneer')
    image mz cry glasses pioneer far = ds_define_sprite('mz', 'cry', body_num=2, dist='far', cloth='pioneer', acc='glasses')
    image mz cry pioneer close = ds_define_sprite('mz', 'cry', body_num=2, dist='close', cloth='pioneer')
    image mz cry glasses pioneer close = ds_define_sprite('mz', 'cry', body_num=2, dist='close', cloth='pioneer', acc='glasses')
    
    image mz cry swimsuit  = ds_define_sprite('mz', 'cry', body_num=2, cloth='swimsuit')
    image mz cry glasses swimsuit = ds_define_sprite('mz', 'cry', body_num=2, cloth='swimsuit', acc='glasses')
    image mz cry swimsuit far = ds_define_sprite('mz', 'cry', body_num=2, dist='far', cloth='swimsuit')
    image mz cry glasses swimsuit far = ds_define_sprite('mz', 'cry', body_num=2, dist='far', cloth='swimsuit', acc='glasses')
    image mz cry swimsuit close = ds_define_sprite('mz', 'cry', body_num=2, dist='close', cloth='swimsuit')
    image mz cry glasses swimsuit close = ds_define_sprite('mz', 'cry', body_num=2, dist='close', cloth='swimsuit', acc='glasses')
    
    image mz cry pullover  = ds_define_sprite('mz', 'cry', body_num=2, cloth='pullover')
    image mz cry glasses pullover = ds_define_sprite('mz', 'cry', body_num=2, cloth='pullover', acc='glasses')
    image mz cry pullover far = ds_define_sprite('mz', 'cry', body_num=2, dist='far', cloth='pullover')
    image mz cry glasses pullover far = ds_define_sprite('mz', 'cry', body_num=2, dist='far', cloth='pullover', acc='glasses')
    image mz cry pullover close = ds_define_sprite('mz', 'cry', body_num=2, dist='close', cloth='pullover')
    image mz cry glasses pullover close = ds_define_sprite('mz', 'cry', body_num=2, dist='close', cloth='pullover', acc='glasses')
    
    image mz shyangry naked = ds_define_sprite('mz', 'shyangry', body_num=2)
    image mz shyangry glasses body = ds_define_sprite('mz', 'shyangry', body_num=2, cloth='body', acc='glasses')
    image mz shyangry naked far = ds_define_sprite('mz', 'shyangry', body_num=2, dist='far')
    image mz shyangry glasses naked far = ds_define_sprite('mz', 'shyangry', body_num=2, dist='far', acc='glasses')
    image mz shyangry naked close = ds_define_sprite('mz', 'shyangry', body_num=2, dist='close')
    image mz shyangry glasses naked close = ds_define_sprite('mz', 'shyangry', body_num=2, dist='close', acc='glasses')
    
    image mz shyangry pioneer  = ds_define_sprite('mz', 'shyangry', body_num=2, cloth='pioneer')
    image mz shyangry glasses pioneer = ds_define_sprite('mz', 'shyangry', body_num=2, cloth='pioneer', acc='glasses')
    image mz shyangry pioneer far = ds_define_sprite('mz', 'shyangry', body_num=2, dist='far', cloth='pioneer')
    image mz shyangry glasses pioneer far = ds_define_sprite('mz', 'shyangry', body_num=2, dist='far', cloth='pioneer', acc='glasses')
    image mz shyangry pioneer close = ds_define_sprite('mz', 'shyangry', body_num=2, dist='close', cloth='pioneer')
    image mz shyangry glasses pioneer close = ds_define_sprite('mz', 'shyangry', body_num=2, dist='close', cloth='pioneer', acc='glasses')
    
    image mz shyangry swimsuit  = ds_define_sprite('mz', 'shyangry', body_num=2, cloth='swimsuit')
    image mz shyangry glasses swimsuit = ds_define_sprite('mz', 'shyangry', body_num=2, cloth='swimsuit', acc='glasses')
    image mz shyangry swimsuit far = ds_define_sprite('mz', 'shyangry', body_num=2, dist='far', cloth='swimsuit')
    image mz shyangry glasses swimsuit far = ds_define_sprite('mz', 'shyangry', body_num=2, dist='far', cloth='swimsuit', acc='glasses')
    image mz shyangry swimsuit close = ds_define_sprite('mz', 'shyangry', body_num=2, dist='close', cloth='swimsuit')
    image mz shyangry glasses swimsuit close = ds_define_sprite('mz', 'shyangry', body_num=2, dist='close', cloth='swimsuit', acc='glasses')
    
    image mz shyangry pullover  = ds_define_sprite('mz', 'shyangry', body_num=2, cloth='pullover')
    image mz shyangry glasses pullover = ds_define_sprite('mz', 'shyangry', body_num=2, cloth='pullover', acc='glasses')
    image mz shyangry pullover far = ds_define_sprite('mz', 'shyangry', body_num=2, dist='far', cloth='pullover')
    image mz shyangry glasses pullover far = ds_define_sprite('mz', 'shyangry', body_num=2, dist='far', cloth='pullover', acc='glasses')
    image mz shyangry pullover close = ds_define_sprite('mz', 'shyangry', body_num=2, dist='close', cloth='pullover')
    image mz shyangry glasses pullover close = ds_define_sprite('mz', 'shyangry', body_num=2, dist='close', cloth='pullover', acc='glasses')
    
    image mz rage naked = ds_define_sprite('mz', 'rage', body_num=2)
    image mz rage glasses body = ds_define_sprite('mz', 'rage', body_num=2, cloth='body', acc='glasses')
    image mz rage naked far = ds_define_sprite('mz', 'rage', body_num=2, dist='far')
    image mz rage glasses naked far = ds_define_sprite('mz', 'rage', body_num=2, dist='far', acc='glasses')
    image mz rage naked close = ds_define_sprite('mz', 'rage', body_num=2, dist='close')
    image mz rage glasses naked close = ds_define_sprite('mz', 'rage', body_num=2, dist='close', acc='glasses')
    
    image mz rage pioneer  = ds_define_sprite('mz', 'rage', body_num=2, cloth='pioneer')
    image mz rage glasses pioneer = ds_define_sprite('mz', 'rage', body_num=2, cloth='pioneer', acc='glasses')
    image mz rage pioneer far = ds_define_sprite('mz', 'rage', body_num=2, dist='far', cloth='pioneer')
    image mz rage glasses pioneer far = ds_define_sprite('mz', 'rage', body_num=2, dist='far', cloth='pioneer', acc='glasses')
    image mz rage pioneer close = ds_define_sprite('mz', 'rage', body_num=2, dist='close', cloth='pioneer')
    image mz rage glasses pioneer close = ds_define_sprite('mz', 'rage', body_num=2, dist='close', cloth='pioneer', acc='glasses')
    
    image mz rage swimsuit  = ds_define_sprite('mz', 'rage', body_num=2, cloth='swimsuit')
    image mz rage glasses swimsuit = ds_define_sprite('mz', 'rage', body_num=2, cloth='swimsuit', acc='glasses')
    image mz rage swimsuit far = ds_define_sprite('mz', 'rage', body_num=2, dist='far', cloth='swimsuit')
    image mz rage glasses swimsuit far = ds_define_sprite('mz', 'rage', body_num=2, dist='far', cloth='swimsuit', acc='glasses')
    image mz rage swimsuit close = ds_define_sprite('mz', 'rage', body_num=2, dist='close', cloth='swimsuit')
    image mz rage glasses swimsuit close = ds_define_sprite('mz', 'rage', body_num=2, dist='close', cloth='swimsuit', acc='glasses')
    
    image mz rage pullover  = ds_define_sprite('mz', 'rage', body_num=2, cloth='pullover')
    image mz rage glasses pullover = ds_define_sprite('mz', 'rage', body_num=2, cloth='pullover', acc='glasses')
    image mz rage pullover far = ds_define_sprite('mz', 'rage', body_num=2, dist='far', cloth='pullover')
    image mz rage glasses pullover far = ds_define_sprite('mz', 'rage', body_num=2, dist='far', cloth='pullover', acc='glasses')
    image mz rage pullover close = ds_define_sprite('mz', 'rage', body_num=2, dist='close', cloth='pullover')
    image mz rage glasses pullover close = ds_define_sprite('mz', 'rage', body_num=2, dist='close', cloth='pullover', acc='glasses')
    
    image mz smile naked = ds_define_sprite('mz', 'smile', body_num=2)
    image mz smile glasses body = ds_define_sprite('mz', 'smile', body_num=2, cloth='body', acc='glasses')
    image mz smile naked far = ds_define_sprite('mz', 'smile', body_num=2, dist='far')
    image mz smile glasses naked far = ds_define_sprite('mz', 'smile', body_num=2, dist='far', acc='glasses')
    image mz smile naked close = ds_define_sprite('mz', 'smile', body_num=2, dist='close')
    image mz smile glasses naked close = ds_define_sprite('mz', 'smile', body_num=2, dist='close', acc='glasses')
    
    image mz smile pioneer  = ds_define_sprite('mz', 'smile', body_num=2, cloth='pioneer')
    image mz smile glasses pioneer = ds_define_sprite('mz', 'smile', body_num=2, cloth='pioneer', acc='glasses')
    image mz smile pioneer far = ds_define_sprite('mz', 'smile', body_num=2, dist='far', cloth='pioneer')
    image mz smile glasses pioneer far = ds_define_sprite('mz', 'smile', body_num=2, dist='far', cloth='pioneer', acc='glasses')
    image mz smile pioneer close = ds_define_sprite('mz', 'smile', body_num=2, dist='close', cloth='pioneer')
    image mz smile glasses pioneer close = ds_define_sprite('mz', 'smile', body_num=2, dist='close', cloth='pioneer', acc='glasses')
    
    image mz smile swimsuit  = ds_define_sprite('mz', 'smile', body_num=2, cloth='swimsuit')
    image mz smile glasses swimsuit = ds_define_sprite('mz', 'smile', body_num=2, cloth='swimsuit', acc='glasses')
    image mz smile swimsuit far = ds_define_sprite('mz', 'smile', body_num=2, dist='far', cloth='swimsuit')
    image mz smile glasses swimsuit far = ds_define_sprite('mz', 'smile', body_num=2, dist='far', cloth='swimsuit', acc='glasses')
    image mz smile swimsuit close = ds_define_sprite('mz', 'smile', body_num=2, dist='close', cloth='swimsuit')
    image mz smile glasses swimsuit close = ds_define_sprite('mz', 'smile', body_num=2, dist='close', cloth='swimsuit', acc='glasses')
    
    image mz smile pullover  = ds_define_sprite('mz', 'smile', body_num=2, cloth='pullover')
    image mz smile glasses pullover = ds_define_sprite('mz', 'smile', body_num=2, cloth='pullover', acc='glasses')
    image mz smile pullover far = ds_define_sprite('mz', 'smile', body_num=2, dist='far', cloth='pullover')
    image mz smile glasses pullover far = ds_define_sprite('mz', 'smile', body_num=2, dist='far', cloth='pullover', acc='glasses')
    image mz smile pullover close = ds_define_sprite('mz', 'smile', body_num=2, dist='close', cloth='pullover')
    image mz smile glasses pullover close = ds_define_sprite('mz', 'smile', body_num=2, dist='close', cloth='pullover', acc='glasses')
    
    image mz confused naked = ds_define_sprite('mz', 'confused', body_num=3)
    image mz confused glasses body = ds_define_sprite('mz', 'confused', body_num=3, cloth='body', acc='glasses')
    image mz confused naked far = ds_define_sprite('mz', 'confused', body_num=3, dist='far')
    image mz confused glasses naked far = ds_define_sprite('mz', 'confused', body_num=3, dist='far', acc='glasses')
    image mz confused naked close = ds_define_sprite('mz', 'confused', body_num=3, dist='close')
    image mz confused glasses naked close = ds_define_sprite('mz', 'confused', body_num=3, dist='close', acc='glasses')
    
    image mz confused pioneer  = ds_define_sprite('mz', 'confused', body_num=3, cloth='pioneer')
    image mz confused glasses pioneer = ds_define_sprite('mz', 'confused', body_num=3, cloth='pioneer', acc='glasses')
    image mz confused pioneer far = ds_define_sprite('mz', 'confused', body_num=3, dist='far', cloth='pioneer')
    image mz confused glasses pioneer far = ds_define_sprite('mz', 'confused', body_num=3, dist='far', cloth='pioneer', acc='glasses')
    image mz confused pioneer close = ds_define_sprite('mz', 'confused', body_num=3, dist='close', cloth='pioneer')
    image mz confused glasses pioneer close = ds_define_sprite('mz', 'confused', body_num=3, dist='close', cloth='pioneer', acc='glasses')
    
    image mz confused swimsuit  = ds_define_sprite('mz', 'confused', body_num=3, cloth='swimsuit')
    image mz confused glasses swimsuit = ds_define_sprite('mz', 'confused', body_num=3, cloth='swimsuit', acc='glasses')
    image mz confused swimsuit far = ds_define_sprite('mz', 'confused', body_num=3, dist='far', cloth='swimsuit')
    image mz confused glasses swimsuit far = ds_define_sprite('mz', 'confused', body_num=3, dist='far', cloth='swimsuit', acc='glasses')
    image mz confused swimsuit close = ds_define_sprite('mz', 'confused', body_num=3, dist='close', cloth='swimsuit')
    image mz confused glasses swimsuit close = ds_define_sprite('mz', 'confused', body_num=3, dist='close', cloth='swimsuit', acc='glasses')
    
    image mz confused pullover  = ds_define_sprite('mz', 'confused', body_num=3, cloth='pullover')
    image mz confused glasses pullover = ds_define_sprite('mz', 'confused', body_num=3, cloth='pullover', acc='glasses')
    image mz confused pullover far = ds_define_sprite('mz', 'confused', body_num=3, dist='far', cloth='pullover')
    image mz confused glasses pullover far = ds_define_sprite('mz', 'confused', body_num=3, dist='far', cloth='pullover', acc='glasses')
    image mz confused pullover close = ds_define_sprite('mz', 'confused', body_num=3, dist='close', cloth='pullover')
    image mz confused glasses pullover close = ds_define_sprite('mz', 'confused', body_num=3, dist='close', cloth='pullover', acc='glasses')
    
    image mz shy naked = ds_define_sprite('mz', 'shy', body_num=3)
    image mz shy glasses body = ds_define_sprite('mz', 'shy', body_num=3, cloth='body', acc='glasses')
    image mz shy naked far = ds_define_sprite('mz', 'shy', body_num=3, dist='far')
    image mz shy glasses naked far = ds_define_sprite('mz', 'shy', body_num=3, dist='far', acc='glasses')
    image mz shy naked close = ds_define_sprite('mz', 'shy', body_num=3, dist='close')
    image mz shy glasses naked close = ds_define_sprite('mz', 'shy', body_num=3, dist='close', acc='glasses')
    
    image mz shy pioneer  = ds_define_sprite('mz', 'shy', body_num=3, cloth='pioneer')
    image mz shy glasses pioneer = ds_define_sprite('mz', 'shy', body_num=3, cloth='pioneer', acc='glasses')
    image mz shy pioneer far = ds_define_sprite('mz', 'shy', body_num=3, dist='far', cloth='pioneer')
    image mz shy glasses pioneer far = ds_define_sprite('mz', 'shy', body_num=3, dist='far', cloth='pioneer', acc='glasses')
    image mz shy pioneer close = ds_define_sprite('mz', 'shy', body_num=3, dist='close', cloth='pioneer')
    image mz shy glasses pioneer close = ds_define_sprite('mz', 'shy', body_num=3, dist='close', cloth='pioneer', acc='glasses')
    
    image mz shy swimsuit  = ds_define_sprite('mz', 'shy', body_num=3, cloth='swimsuit')
    image mz shy glasses swimsuit = ds_define_sprite('mz', 'shy', body_num=3, cloth='swimsuit', acc='glasses')
    image mz shy swimsuit far = ds_define_sprite('mz', 'shy', body_num=3, dist='far', cloth='swimsuit')
    image mz shy glasses swimsuit far = ds_define_sprite('mz', 'shy', body_num=3, dist='far', cloth='swimsuit', acc='glasses')
    image mz shy swimsuit close = ds_define_sprite('mz', 'shy', body_num=3, dist='close', cloth='swimsuit')
    image mz shy glasses swimsuit close = ds_define_sprite('mz', 'shy', body_num=3, dist='close', cloth='swimsuit', acc='glasses')
    
    image mz shy pullover  = ds_define_sprite('mz', 'shy', body_num=3, cloth='pullover')
    image mz shy glasses pullover = ds_define_sprite('mz', 'shy', body_num=3, cloth='pullover', acc='glasses')
    image mz shy pullover far = ds_define_sprite('mz', 'shy', body_num=3, dist='far', cloth='pullover')
    image mz shy glasses pullover far = ds_define_sprite('mz', 'shy', body_num=3, dist='far', cloth='pullover', acc='glasses')
    image mz shy pullover close = ds_define_sprite('mz', 'shy', body_num=3, dist='close', cloth='pullover')
    image mz shy glasses pullover close = ds_define_sprite('mz', 'shy', body_num=3, dist='close', cloth='pullover', acc='glasses')
    
    image mz excitement naked = ds_define_sprite('mz', 'excitement', body_num=3)
    image mz excitement glasses body = ds_define_sprite('mz', 'excitement', body_num=3, cloth='body', acc='glasses')
    image mz excitement naked far = ds_define_sprite('mz', 'excitement', body_num=3, dist='far')
    image mz excitement glasses naked far = ds_define_sprite('mz', 'excitement', body_num=3, dist='far', acc='glasses')
    image mz excitement naked close = ds_define_sprite('mz', 'excitement', body_num=3, dist='close')
    image mz excitement glasses naked close = ds_define_sprite('mz', 'excitement', body_num=3, dist='close', acc='glasses')
    
    image mz excitement pioneer  = ds_define_sprite('mz', 'excitement', body_num=3, cloth='pioneer')
    image mz excitement glasses pioneer = ds_define_sprite('mz', 'excitement', body_num=3, cloth='pioneer', acc='glasses')
    image mz excitement pioneer far = ds_define_sprite('mz', 'excitement', body_num=3, dist='far', cloth='pioneer')
    image mz excitement glasses pioneer far = ds_define_sprite('mz', 'excitement', body_num=3, dist='far', cloth='pioneer', acc='glasses')
    image mz excitement pioneer close = ds_define_sprite('mz', 'excitement', body_num=3, dist='close', cloth='pioneer')
    image mz excitement glasses pioneer close = ds_define_sprite('mz', 'excitement', body_num=3, dist='close', cloth='pioneer', acc='glasses')
    
    image mz excitement swimsuit  = ds_define_sprite('mz', 'excitement', body_num=3, cloth='swimsuit')
    image mz excitement glasses swimsuit = ds_define_sprite('mz', 'excitement', body_num=3, cloth='swimsuit', acc='glasses')
    image mz excitement swimsuit far = ds_define_sprite('mz', 'excitement', body_num=3, dist='far', cloth='swimsuit')
    image mz excitement glasses swimsuit far = ds_define_sprite('mz', 'excitement', body_num=3, dist='far', cloth='swimsuit', acc='glasses')
    image mz excitement swimsuit close = ds_define_sprite('mz', 'excitement', body_num=3, dist='close', cloth='swimsuit')
    image mz excitement glasses swimsuit close = ds_define_sprite('mz', 'excitement', body_num=3, dist='close', cloth='swimsuit', acc='glasses')
    
    image mz excitement pullover  = ds_define_sprite('mz', 'excitement', body_num=3, cloth='pullover')
    image mz excitement glasses pullover = ds_define_sprite('mz', 'excitement', body_num=3, cloth='pullover', acc='glasses')
    image mz excitement pullover far = ds_define_sprite('mz', 'excitement', body_num=3, dist='far', cloth='pullover')
    image mz excitement glasses pullover far = ds_define_sprite('mz', 'excitement', body_num=3, dist='far', cloth='pullover', acc='glasses')
    image mz excitement pullover close = ds_define_sprite('mz', 'excitement', body_num=3, dist='close', cloth='pullover')
    image mz excitement glasses pullover close = ds_define_sprite('mz', 'excitement', body_num=3, dist='close', cloth='pullover', acc='glasses')
    
    image mz amazed casual  = ds_define_sprite('mz', 'amazed', body_num=1, cloth='casual')
    image mz bukal casual  = ds_define_sprite('mz', 'bukal', body_num=1, cloth='casual')
    image mz normal casual  = ds_define_sprite('mz', 'normal', body_num=1, cloth='casual')
    image mz fun casual  = ds_define_sprite('mz', 'fun', body_num=1, cloth='casual')

    # Шурик

    image sh laugh towel = ds_define_sprite('sh', 'laugh', body_num=1)
    image sh laugh towel far = ds_define_sprite('sh', 'laugh', body_num=1, dist='far')
    image sh laugh towel close = ds_define_sprite('sh', 'laugh', body_num=1, dist='close')

    image sh scared towel = ds_define_sprite('sh', 'scared', body_num=1)
    image sh scared towel far = ds_define_sprite('sh', 'scared', body_num=1, dist='far')
    image sh scared towel close = ds_define_sprite('sh', 'scared', body_num=1, dist='close')

    image sh smile towel = ds_define_sprite('sh', 'smile', body_num=1)
    image sh smile towel far = ds_define_sprite('sh', 'smile', body_num=1, dist='far')
    image sh smile towel close = ds_define_sprite('sh', 'smile', body_num=1, dist='close')

    image sh upset towel = ds_define_sprite('sh', 'upset', body_num=1)
    image sh upset towel far = ds_define_sprite('sh', 'upset', body_num=1, dist='far')
    image sh upset towel close = ds_define_sprite('sh', 'upset', body_num=1, dist='close')

    image sh cry towel = ds_define_sprite('sh', 'cry', body_num=2)
    image sh cry towel far = ds_define_sprite('sh', 'cry', body_num=2, dist='far')
    image sh cry towel close = ds_define_sprite('sh', 'cry', body_num=2, dist='close')

    image sh mad_smile towel = ds_define_sprite('sh', 'normal_smile', body_num=2)
    image sh mad_smile towel far = ds_define_sprite('sh', 'normal_smile', body_num=2, dist='far')
    image sh mad_smile towel close = ds_define_sprite('sh', 'normal_smile', body_num=2, dist='close')

    image sh rage towel = ds_define_sprite('sh', 'rage', body_num=2)
    image sh rage towel far = ds_define_sprite('sh', 'rage', body_num=2, dist='far')
    image sh rage towel close = ds_define_sprite('sh', 'rage', body_num=2, dist='close')

    image sh normal towel = ds_define_sprite('sh', 'normal', body_num=3)
    image sh normal towel far = ds_define_sprite('sh', 'normal', body_num=3, dist='far')
    image sh normal towel close = ds_define_sprite('sh', 'normal', body_num=3, dist='close')

    image sh serious towel = ds_define_sprite('sh', 'serious', body_num=3)
    image sh serious towel far = ds_define_sprite('sh', 'serious', body_num=3, dist='far')
    image sh serious towel close = ds_define_sprite('sh', 'serious', body_num=3, dist='close')

    image sh surprise towel = ds_define_sprite('sh', 'surprise', body_num=3)
    image sh surprise towel far = ds_define_sprite('sh', 'surprise', body_num=3, dist='far')
    image sh surprise towel close = ds_define_sprite('sh', 'surprise', body_num=3, dist='close')

    image sh laugh bathrobe = ds_define_sprite('sh', 'laugh', body_num=1, cloth='bathrobe')
    image sh laugh bathrobe far = ds_define_sprite('sh', 'laugh', body_num=1, dist='far', cloth='bathrobe')
    image sh laugh bathrobe close = ds_define_sprite('sh', 'laugh', body_num=1, dist='close', cloth='bathrobe')

    image sh scared bathrobe = ds_define_sprite('sh', 'scared', body_num=1, cloth='bathrobe')
    image sh scared bathrobe far = ds_define_sprite('sh', 'scared', body_num=1, dist='far', cloth='bathrobe')
    image sh scared bathrobe close = ds_define_sprite('sh', 'scared', body_num=1, dist='close', cloth='bathrobe')

    image sh smile bathrobe = ds_define_sprite('sh', 'smile', body_num=1, cloth='bathrobe')
    image sh smile bathrobe far = ds_define_sprite('sh', 'smile', body_num=1, dist='far', cloth='bathrobe')
    image sh smile bathrobe close = ds_define_sprite('sh', 'smile', body_num=1, dist='close', cloth='bathrobe')

    image sh upset bathrobe = ds_define_sprite('sh', 'upset', body_num=1, cloth='bathrobe')
    image sh upset bathrobe far = ds_define_sprite('sh', 'upset', body_num=1, dist='far', cloth='bathrobe')
    image sh upset bathrobe close = ds_define_sprite('sh', 'upset', body_num=1, dist='close', cloth='bathrobe')

    image sh cry bathrobe = ds_define_sprite('sh', 'cry', body_num=2, cloth='bathrobe')
    image sh cry bathrobe far = ds_define_sprite('sh', 'cry', body_num=2, dist='far', cloth='bathrobe')
    image sh cry bathrobe close = ds_define_sprite('sh', 'cry', body_num=2, dist='close', cloth='bathrobe')

    image sh mad_smile bathrobe = ds_define_sprite('sh', 'normal_smile', body_num=2, cloth='bathrobe')
    image sh mad_smile bathrobe far = ds_define_sprite('sh', 'normal_smile', body_num=2, dist='far', cloth='bathrobe')
    image sh mad_smile bathrobe close = ds_define_sprite('sh', 'normal_smile', body_num=2, dist='close', cloth='bathrobe')

    image sh rage bathrobe = ds_define_sprite('sh', 'rage', body_num=2, cloth='bathrobe')
    image sh rage bathrobe far = ds_define_sprite('sh', 'rage', body_num=2, dist='far', cloth='bathrobe')
    image sh rage bathrobe close = ds_define_sprite('sh', 'rage', body_num=2, dist='close', cloth='bathrobe')

    image sh normal bathrobe = ds_define_sprite('sh', 'normal', body_num=3, cloth='bathrobe')
    image sh normal bathrobe far = ds_define_sprite('sh', 'normal', body_num=3, dist='far', cloth='bathrobe')
    image sh normal bathrobe close = ds_define_sprite('sh', 'normal', body_num=3, dist='close', cloth='bathrobe')

    image sh serious bathrobe = ds_define_sprite('sh', 'serious', body_num=3, cloth='bathrobe')
    image sh serious bathrobe far = ds_define_sprite('sh', 'serious', body_num=3, dist='far', cloth='bathrobe')
    image sh serious bathrobe close = ds_define_sprite('sh', 'serious', body_num=3, dist='close', cloth='bathrobe')

    image sh surprise bathrobe = ds_define_sprite('sh', 'surprise', body_num=3, cloth='bathrobe')
    image sh surprise bathrobe far = ds_define_sprite('sh', 'surprise', body_num=3, dist='far', cloth='bathrobe')
    image sh surprise bathrobe close = ds_define_sprite('sh', 'surprise', body_num=3, dist='close', cloth='bathrobe')

    image sh laugh sport = ds_define_sprite('sh', 'laugh', body_num=1, cloth='shirt')
    image sh laugh sport far = ds_define_sprite('sh', 'laugh', body_num=1, dist='far', cloth='shirt')
    image sh laugh sport close = ds_define_sprite('sh', 'laugh', body_num=1, dist='close', cloth='shirt')

    image sh scared sport = ds_define_sprite('sh', 'scared', body_num=1, cloth='shirt')
    image sh scared sport far = ds_define_sprite('sh', 'scared', body_num=1, dist='far', cloth='shirt')
    image sh scared sport close = ds_define_sprite('sh', 'scared', body_num=1, dist='close', cloth='shirt')

    image sh smile sport = ds_define_sprite('sh', 'smile', body_num=1, cloth='shirt')
    image sh smile sport far = ds_define_sprite('sh', 'smile', body_num=1, dist='far', cloth='shirt')
    image sh smile sport close = ds_define_sprite('sh', 'smile', body_num=1, dist='close', cloth='shirt')

    image sh upset sport = ds_define_sprite('sh', 'upset', body_num=1, cloth='shirt')
    image sh upset sport far = ds_define_sprite('sh', 'upset', body_num=1, dist='far', cloth='shirt')
    image sh upset sport close = ds_define_sprite('sh', 'upset', body_num=1, dist='close', cloth='shirt')

    image sh cry sport = ds_define_sprite('sh', 'cry', body_num=2, cloth='shirt')
    image sh cry sport far = ds_define_sprite('sh', 'cry', body_num=2, dist='far', cloth='shirt')
    image sh cry sport close = ds_define_sprite('sh', 'cry', body_num=2, dist='close', cloth='shirt')

    image sh mad_smile sport = ds_define_sprite('sh', 'normal_smile', body_num=2, cloth='shirt')
    image sh mad_smile sport far = ds_define_sprite('sh', 'normal_smile', body_num=2, dist='far', cloth='shirt')
    image sh mad_smile sport close = ds_define_sprite('sh', 'normal_smile', body_num=2, dist='close', cloth='shirt')

    image sh rage sport = ds_define_sprite('sh', 'rage', body_num=2, cloth='shirt')
    image sh rage sport far = ds_define_sprite('sh', 'rage', body_num=2, dist='far', cloth='shirt')
    image sh rage sport close = ds_define_sprite('sh', 'rage', body_num=2, dist='close', cloth='shirt')

    image sh normal sport = ds_define_sprite('sh', 'normal', body_num=3, cloth='shirt')
    image sh normal sport far = ds_define_sprite('sh', 'normal', body_num=3, dist='far', cloth='shirt')
    image sh normal sport close = ds_define_sprite('sh', 'normal', body_num=3, dist='close', cloth='shirt')

    image sh serious sport = ds_define_sprite('sh', 'serious', body_num=3, cloth='shirt')
    image sh serious sport far = ds_define_sprite('sh', 'serious', body_num=3, dist='far', cloth='shirt')
    image sh serious sport close = ds_define_sprite('sh', 'serious', body_num=3, dist='close', cloth='shirt')

    image sh surprise sport = ds_define_sprite('sh', 'surprise', body_num=3, cloth='shirt')
    image sh surprise sport far = ds_define_sprite('sh', 'surprise', body_num=3, dist='far', cloth='shirt')
    image sh surprise sport close = ds_define_sprite('sh', 'surprise', body_num=3, dist='close', cloth='shirt')

    # Славя

    image sl angry modern = ds_define_sprite('sl', 'angry', body_num=3, cloth='casual')
    image sl angry modern close = ds_define_sprite('sl', 'angry', dist='close', body_num=3, cloth='casual')
    image sl angry modern far = ds_define_sprite('sl', 'angry', dist='far', body_num=3, cloth='casual')

    image sl happy modern = ds_define_sprite('sl', 'happy', body_num=2, cloth='casual')
    image sl happy modern close = ds_define_sprite('sl', 'happy', dist='close', body_num=2, cloth='casual')
    image sl happy modern far = ds_define_sprite('sl', 'happy', dist='far', body_num=2, cloth='casual')
    
    image sl laugh modern = ds_define_sprite('sl', 'laugh', body_num=2, cloth='casual')
    image sl laugh modern close = ds_define_sprite('sl', 'laugh', dist='close', body_num=2, cloth='casual')
    image sl laugh modern far = ds_define_sprite('sl', 'laugh', dist='far', body_num=2, cloth='casual')

    image sl normal modern = ds_define_sprite('sl', 'normal', body_num=1, cloth='casual')
    image sl normal modern close = ds_define_sprite('sl', 'normal', dist='close', body_num=1, cloth='casual')
    image sl normal modern far = ds_define_sprite('sl', 'normal', dist='far', body_num=1, cloth='casual')

    image sl sad modern = ds_define_sprite('sl', 'sad', body_num=3, cloth='casual')
    image sl sad modern close = ds_define_sprite('sl', 'sad', dist='close', body_num=3, cloth='casual')
    image sl sad modern far = ds_define_sprite('sl', 'sad', dist='far', body_num=3, cloth='casual')

    image sl scared modern = ds_define_sprite('sl', 'scared', body_num=4, cloth='casual')
    image sl scared modern close = ds_define_sprite('sl', 'scared', dist='close', body_num=4, cloth='casual')
    image sl scared modern far = ds_define_sprite('sl', 'scared', dist='far', body_num=4, cloth='casual')

    image sl serious modern = ds_define_sprite('sl', 'serious', body_num=1, cloth='casual')
    image sl serious modern close = ds_define_sprite('sl', 'serious', dist='close', body_num=1, cloth='casual')
    image sl serious modern far = ds_define_sprite('sl', 'serious', dist='far', body_num=1, cloth='casual')

    image sl shy modern = ds_define_sprite('sl', 'shy', body_num=2, cloth='casual')
    image sl shy modern close = ds_define_sprite('sl', 'shy', dist='close', body_num=2, cloth='casual')
    image sl shy modern far = ds_define_sprite('sl', 'shy', dist='far', body_num=2, cloth='casual')

    image sl smile modern = ds_define_sprite('sl', 'smile', body_num=1, cloth='casual')
    image sl smile modern close = ds_define_sprite('sl', 'smile', dist='close', body_num=1, cloth='casual')
    image sl smile modern far = ds_define_sprite('sl', 'smile', dist='far', body_num=1, cloth='casual')

    image sl smile2 modern = ds_define_sprite('sl', 'smile2', body_num=2, cloth='casual')
    image sl smile2 modern close = ds_define_sprite('sl', 'smile2', dist='close', body_num=2, cloth='casual')
    image sl smile2 modern far = ds_define_sprite('sl', 'smile2', dist='far', body_num=2, cloth='casual')

    image sl surprise modern = ds_define_sprite('sl', 'surprise', body_num=3, cloth='casual')
    image sl surprise modern close = ds_define_sprite('sl', 'surprise', dist='close', body_num=3, cloth='casual')
    image sl surprise modern far = ds_define_sprite('sl', 'surprise', dist='far', body_num=3, cloth='casual')

    image sl tender modern = ds_define_sprite('sl', 'tender', body_num=4, cloth='casual')
    image sl tender modern close = ds_define_sprite('sl', 'tender', dist='close', body_num=4, cloth='casual')
    image sl tender modern far = ds_define_sprite('sl', 'tender', dist='far', body_num=4, cloth='casual')

    # Лена

    image un angry modern = ds_define_sprite('un', 'angry', body_num=1, cloth='designer')
    image un angry modern close = ds_define_sprite('un', 'angry', dist='close', body_num=1, cloth='designer')
    image un angry modern far = ds_define_sprite('un', 'angry', dist='far', body_num=1, cloth='designer')

    image un angry2 modern = ds_define_sprite('un', 'angry2', body_num=3, cloth='designer')
    image un angry2 modern close = ds_define_sprite('un', 'angry2', dist='close', body_num=3, cloth='designer')
    image un angry2 modern far = ds_define_sprite('un', 'angry2', dist='far', body_num=3, cloth='designer')

    image un cry modern = ds_define_sprite('un', 'cry', body_num=2, cloth='designer')
    image un cry modern close = ds_define_sprite('un', 'cry', dist='close', body_num=2, cloth='designer')
    image un cry modern far = ds_define_sprite('un', 'cry', dist='far', body_num=2, cloth='designer')

    image un cry_smile modern = ds_define_sprite('un', 'cry_smile', body_num=2, cloth='designer')
    image un cry_smile modern close = ds_define_sprite('un', 'cry_smile', dist='close', body_num=2, cloth='designer')
    image un cry_smile modern far = ds_define_sprite('un', 'cry_smile', dist='far', body_num=2, cloth='designer')

    image un evil_smile modern = ds_define_sprite('un', 'evil_smile', body_num=1, cloth='designer')
    image un evil_smile modern close = ds_define_sprite('un', 'evil_smile', dist='close', body_num=1, cloth='designer')
    image un evil_smile modern far = ds_define_sprite('un', 'evil_smile', dist='far', body_num=1, cloth='designer')

    image un grin modern = ds_define_sprite('un', 'grin', body_num=3, cloth='designer')
    image un grin modern close = ds_define_sprite('un', 'grin', dist='close', body_num=3, cloth='designer')
    image un grin modern far = ds_define_sprite('un', 'grin', dist='far', body_num=3, cloth='designer')

    image un laugh modern = ds_define_sprite('un', 'laugh', body_num=3, cloth='designer')
    image un laugh modern close = ds_define_sprite('un', 'laugh', dist='close', body_num=3, cloth='designer')
    image un laugh modern far = ds_define_sprite('un', 'laugh', dist='far', body_num=3, cloth='designer')

    image un normal modern = ds_define_sprite('un', 'normal', body_num=1, cloth='designer')
    image un normal modern close = ds_define_sprite('un', 'normal', dist='close', body_num=1, cloth='designer')
    image un normal modern far = ds_define_sprite('un', 'normal', dist='far', body_num=1, cloth='designer')

    image un rage modern = ds_define_sprite('un', 'rage', body_num=3, cloth='designer')
    image un rage modern close = ds_define_sprite('un', 'rage', dist='close', body_num=3, cloth='designer')
    image un rage modern far = ds_define_sprite('un', 'rage', dist='far', body_num=3, cloth='designer')

    image un sad modern = ds_define_sprite('un', 'sad', body_num=2, cloth='designer')
    image un sad modern close = ds_define_sprite('un', 'sad', dist='close', body_num=2, cloth='designer')
    image un sad modern far = ds_define_sprite('un', 'sad', dist='far', body_num=2, cloth='designer')

    image un scared modern = ds_define_sprite('un', 'scared', body_num=2, cloth='designer')
    image un scared modern close = ds_define_sprite('un', 'scared', dist='close', body_num=2, cloth='designer')
    image un scared modern far = ds_define_sprite('un', 'scared', dist='far', body_num=2, cloth='designer')

    image un serious modern = ds_define_sprite('un', 'serious', body_num=3, cloth='designer')
    image un serious modern close = ds_define_sprite('un', 'serious', dist='close', body_num=3, cloth='designer')
    image un serious modern far = ds_define_sprite('un', 'serious', dist='far', body_num=3, cloth='designer')

    image un shocked modern = ds_define_sprite('un', 'shocked', body_num=2, cloth='designer')
    image un shocked modern close = ds_define_sprite('un', 'shocked', dist='close', body_num=2, cloth='designer')
    image un shocked modern far = ds_define_sprite('un', 'shocked', dist='far', body_num=2, cloth='designer')

    image un shy modern = ds_define_sprite('un', 'shy', body_num=1, cloth='designer')
    image un shy modern close = ds_define_sprite('un', 'shy', dist='close', body_num=1, cloth='designer')
    image un shy modern far = ds_define_sprite('un', 'shy', dist='far', body_num=1, cloth='designer')

    image un smile modern = ds_define_sprite('un', 'smile', body_num=1, cloth='designer')
    image un smile modern close = ds_define_sprite('un', 'smile', dist='close', body_num=1, cloth='designer')
    image un smile modern far = ds_define_sprite('un', 'smile', dist='far', body_num=1, cloth='designer')

    image un smile2 modern = ds_define_sprite('un', 'smile2', body_num=1, cloth='designer')
    image un smile2 modern close = ds_define_sprite('un', 'smile2', dist='close', body_num=1, cloth='designer')
    image un smile2 modern far = ds_define_sprite('un', 'smile2', dist='far', body_num=1, cloth='designer')

    image un smile3 modern = ds_define_sprite('un', 'smile3', body_num=3, cloth='designer')
    image un smile3 modern close = ds_define_sprite('un', 'smile3', dist='close', body_num=3, cloth='designer')
    image un smile3 modern far = ds_define_sprite('un', 'smile3', dist='far', body_num=3, cloth='designer')

    image un surprise modern = ds_define_sprite('un', 'surprise', body_num=2, cloth='designer')
    image un surprise modern close = ds_define_sprite('un', 'surprise', dist='close', body_num=2, cloth='designer')
    image un surprise modern far = ds_define_sprite('un', 'surprise', dist='far', body_num=2, cloth='designer')

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
