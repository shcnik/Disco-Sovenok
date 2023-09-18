# МОДИФИКАЦИЯ ГРАФИЧЕСКОГО ИНТЕРФЕЙСА

init python:
    import pygame
    import os
    import os.path
    import renpy.store as store
    from renpy.store import *
    from renpy.display.im import ImageBase, image, cache, Composite

    def ds_init_custom():
        ds_skill_points['logic'], ds_skill_points['encyclopedia'], ds_skill_points['rhetoric'], ds_skill_points['drama'], ds_skill_points['conceptualization'], ds_skill_points['visual_calculus'] = 3, 3, 3, 3, 3, 3
        ds_skill_points['volition'], ds_skill_points['inland_empire'], ds_skill_points['authority'], ds_skill_points['empathy'], ds_skill_points['esprit'], ds_skill_points['suggestion'] = 3, 3, 3, 3, 3, 3
        ds_skill_points['endurance'], ds_skill_points['pain_threshold'], ds_skill_points['physical_instrument'], ds_skill_points['instinct'], ds_skill_points['shivers'], ds_skill_points['half_light'] = 3, 3, 3, 3, 3, 3
        ds_skill_points['perception'], ds_skill_points['coordination'], ds_skill_points['reaction_speed'], ds_skill_points['savoir_faire'], ds_skill_points['interfacing'], ds_skill_points['composure'] = 3, 3, 3, 3, 3, 3
        ds_available_points = 8
    
    def ds_abs(x):
        if x < 0:
            return -x
        return x

    # Источник кода ниже: https://es-doc.vercel.app/guide/code-examples.html
    # (с правками автора данного мода)
    SCREENS = [
        "main_menu",
        # "game_menu_selector",
        # "quit",
        # "say",
        # "preferences",
        # "save",
        # "load",
        # "nvl",
        # "choice",
        # "text_history_screen",
        # "yesno_prompt",
    ]

    def ds_screen_save():  # Функция сохранения экранов из оригинала.
        for name in SCREENS:
            renpy.display.screen.screens[
                ("ds_old_" + name, None)
            ] = renpy.display.screen.screens[(name, None)]

    def ds_screen_act():  # Функция замены экранов из оригинала на собственные.
        config.window_title = u"Disco Sovenok"  # Здесь вводите название вашего мода.
        for (
            name
        ) in (
            SCREENS
        ):
            renpy.display.screen.screens[(name, None)] = renpy.display.screen.screens[
                ('ds_' + name, None)
            ]

    def ds_screens_diact():  # Функция обратной замены.
        # Пытаемся заменить экраны.
        try:
            config.window_title = u"Бесконечное лето"
            for name in SCREENS:
                renpy.display.screen.screens[(name, None)] = renpy.display.screen.screens[
                    ("ds_old_" + name, None)
                ]
        except:  # Если возникают ошибки, то мы выходим из игры, чтобы избежать Traceback
            renpy.quit()

    # Объединяем функцию сохранения экранов и замены в одну.
    def ds_screens_save_act():
        ds_screen_save()
        ds_screen_act()

    def bg_tmp_image(bgname):
        renpy.image(
            "text " + bgname,
            LiveComposite(
                (config.screen_width, config.screen_height),
                (0, 0),
                "#ffff7f",
                (50, 150),
                Text(u"А здесь будет фон про " + bgname, size=40, color="6A7183"),
            ),
        )
        return "text " + bgname

    store.small_map_pics_ds = {
        "bgpic_ds": "mods/disco_sovenok/gui/map/small_map_bg.jpg",  # Путь до фона карты
        "avaliable_ds": "mods/disco_sovenok/gui/map/small_map_avaliable.jpg",  # Путь до версии карты с idle-версией
        "selected_ds": "mods/disco_sovenok/gui/map/small_map_selected.jpg",  # Путь до версии карты с hover-версией
    }

    store.small_map_zones_ds = {
        "house_el_sh": {
            "position": [842, 282, 892, 330],
            "default_bg": bg_tmp_image(u"Электроник и Шурик"),
        },
        "house_sl_mz": {
            "position": [1024, 242, 1068, 303],
            "default_bg": bg_tmp_image(u"Славя и Женя"),
        },
        "house_un_mi": {
            "position": [809, 143, 852, 200],
            "default_bg": bg_tmp_image(u"Лена и Мику"),
        },
        "house_me_mt": {
            "position": [958, 168, 1020, 227],
            "default_bg": bg_tmp_image(u"Семён и ОД"),
        },
        "house_dv_us": {
            "position": [715, 616, 763, 665],
            "default_bg": bg_tmp_image(u"Алиса и Ульяна"),
        },
        "scene": {
            "position": [1062, 54, 1154, 139],
            "default_bg": bg_tmp_image(u"Эстрада"),
        },
        "square": {
            "position": [887, 360, 1001, 546],
            "default_bg": bg_tmp_image(u"Площадь"),
        },
        "music_club": {
            "position": [627, 255, 694, 340],
            "default_bg": bg_tmp_image(u"Музклуб"),
        },
        "dining_hall": {
            "position": [1010, 456, 1144, 588],
            "default_bg": bg_tmp_image(u"Столовая"),
        },
        "sport_area": {
            "position": [1219, 376, 1584, 657],
            "default_bg": bg_tmp_image(u"Спорткомплекс"),
        },
        "beach": {"position": [1198, 674, 1490, 833], "default_bg": bg_tmp_image(u"Пляж")},
        "boathouse": {
            "position": [832, 801, 957, 855],
            "default_bg": bg_tmp_image(u"Лодочный причал"),
        },
        "booth": {"position": [905, 663, 949, 732], "default_bg": bg_tmp_image(u"Будка")},
        "clubs": {"position": [435, 437, 650, 605], "default_bg": bg_tmp_image(u"Клубы")},
        "library": {
            "position": [1158, 271, 1285, 360],
            "default_bg": bg_tmp_image(u"Библиотека"),
        },
        "medic_house": {
            "position": [1042, 360, 1188, 444],
            "default_bg": bg_tmp_image(u"Медпункт"),
        },
        "forest": {"position": [558, 58, 691, 194], "default_bg": bg_tmp_image(u"о. Лес")},
        "entrance": {
            "position": [286, 441, 414, 556],
            "default_bg": bg_tmp_image(u"Стоянка"),
        },
        "admin": {
            "position": [774, 348, 879, 449],
            "default_bg": bg_tmp_image(u"Админ. корпус"),
        },
        "shower_room": {
            "position": [695, 433, 791, 530],
            "default_bg": bg_tmp_image(u"Душевая"),
        },
        "old_building": {
            "position": [230, 1004, 337, 1073],
            "default_bg": bg_tmp_image(u"Старый корпус"),
        },
        "storage": {
            "position": [1148, 481, 1215, 583],
            "default_bg": bg_tmp_image(u"Склад"),
        },
    }

    global_map_result_small_ds = "error"

    store.small_map_enabled_ds = False
    store.small_map_enabled_ds_tmp = False

    def init_small_map_zones_realization_ds(zones_ds, default):
        global global_zones_small_ds
        global_zones_small_ds = zones_ds
        for i, data in global_zones_small_ds.iteritems():
            data["label"] = default
            data["avaliable"] = False

    class DSSmallMap(renpy.Displayable):
        def __init__(self, pics, default):
            renpy.Displayable.__init__(self)
            self.pics = pics
            self.default = default
            config.overlay_functions.append(self.overlay)

        def disable_all_zones(self):
            global global_zones_small_ds
            for name, data in global_zones_small_ds.iteritems():
                data["label"] = self.default
                data["avaliable"] = False

        def enable_all_zones(self):
            global global_zones_small_ds
            for name, data in global_zones_small_ds.iteritems():
                data["label"] = self.default
                data["avaliable"] = True

        def set_zone(self, name, label):
            global global_zones_small_ds
            global_zones_small_ds[name]["label"] = label
            global_zones_small_ds[name]["avaliable"] = True

        def reset_zone(self, name):
            global global_zones_small_ds
            global_zones_small_ds[name]["label"] = self.default
            global_zones_small_ds[name]["avaliable"] = False

        def enable_empty_zone(self, name):
            global global_zones_small_ds
            self.set_zone(name, self.default)
            global_zones_small_ds[name]["avaliable"] = True

        def reset_current_zone(self):
            self.enable_empty_zone(global_map_result_small_ds)

        def disable_current_zone(self):
            global global_zones_small_ds
            global_zones_small_ds[global_map_result_small_ds]["avaliable"] = False

        def event(self, ev, x, y, st):
            return

        def render(self, width, height, st, at):
            return renpy.Render(1, 1)

        def zoneclick(self, name):
            global global_zones_small_ds
            global global_map_result_small_ds
            store.small_map_enabled_ds = False
            renpy.scene("mapoverlay")
            global_map_result_small_ds = name
            renpy.hide("widget small_map_ds")
            ui.jumps(global_zones_small_ds[name]["label"])()

        def overlay(self):
            if store.small_map_enabled_ds:
                global global_zones_small_ds
                renpy.scene("mapoverlay")
                ui.layer("mapoverlay")
                for name, data in global_zones_small_ds.iteritems():
                    if data["avaliable"]:
                        pos = data["position"]
                        print(name)
                        ui.imagebutton(
                            im.Crop(
                                self.pics["avaliable_ds"],
                                pos[0],
                                pos[1],
                                pos[2] - pos[0],
                                pos[3] - pos[1],
                            ),
                            im.Crop(
                                self.pics["selected_ds"],
                                pos[0],
                                pos[1],
                                pos[2] - pos[0],
                                pos[3] - pos[1],
                            ),
                            clicked=renpy.curry(self.zoneclick)(name),
                            xpos=pos[0],
                            ypos=pos[1],
                        )
                ui.close()
    
    store.small_map_ds = DSSmallMap(store.small_map_pics_ds, default)

    def disable_small_map():
        store.small_map_enabled_ds_tmp = store.small_map_enabled_ds_tmp or store.small_map_enabled_ds
        store.small_map_enabled_ds = False

    def enable_small_map():
        store.small_map_enabled_ds = store.small_map_enabled_ds_tmp
        store.small_map_enabled_ds_tmp = False

    config_session = False

    if not config_session:
        def disable_all_zones_ds_small():
            store.small_map_ds.disable_all_zones()

        def enable_all_zones_ds_small():
            store.small_map_ds.enable_all_zones()

        def set_zone_ds_small(name, label):
            store.small_map_ds.set_zone(name, label)

        def reset_zone_ds_small(name):
            store.small_map_ds.reset_zone(name)

        def enable_empty_zone_ds_small(name):
            store.small_map_ds.enable_empty_zone(name)

        def reset_current_zone_ds_small():
            store.small_map_ds.reset_current_zone()

        def disable_current_zone_ds_small():
            store.small_map_ds.disable_current_zone()

        def show_small_map_ds():
            ui.jumps("_show_small_map_ds")()

        def init_small_map_zones_ds():
            init_small_map_zones_realization_ds(store.small_map_zones_ds, "nothing_here")

init:
    $ mods["disco_sovenok"] = u"Disco Sovenok"

    if not config_session:
        image widget small_map_ds = "mods/disco_sovenok/gui/map/small_map_bg.jpg" # Путь до фона карты
        image bg small_map_ds     = "mods/disco_sovenok/gui/map/small_map_available.jpg" # Путь до версии карты с idle-версией

    $ init_small_map_zones_ds()

    $ ds_chosen_skill = None
    $ ds_available_points = 8

label _show_small_map_ds:
    show widget small_map_ds
    $ store.small_map_enabled_ds = True
    $ ui.interact()
    jump _show_small_map_ds

transform out_up(new_widget=None, old_widget=None):
    delay 0.1
    old_widget
    events False
    yanchor 1.0
    linear 0.1 ypos 0.0

transform out_bottom(new_widget=None, old_widget=None):
    delay 0.1
    old_widget
    events False
    yanchor 0.0
    linear 0.1 ypos 1.0

transform out_right(new_widget=None, old_widget=None):
    delay 0.1
    old_widget
    events False
    xanchor 0.0
    linear 0.1 xpos 1.0

transform out_left(new_widget=None, old_widget=None):
    delay 0.1
    old_widget
    events False
    xanchor 1.0
    linear 0.1 xpos 0.0

transform in_up(new_widget=None, old_widget=None):
    delay 0.1
    new_widget
    events True
    yanchor 1.0
    ypos 0.0
    linear 0.1 yanchor 0.0 ypos 0.0

transform in_bottom(new_widget=None, old_widget=None):
    delay 0.1
    new_widget
    events True
    yanchor 0.0
    ypos 1.0
    linear 0.1 yanchor 1.0 ypos 1.0

transform in_right(new_widget=None, old_widget=None):
    delay 0.1
    new_widget
    events True
    xanchor 0.0
    xpos 1.0
    linear 0.1 xanchor 1.0 xpos 1.0

transform in_left(new_widget=None, old_widget=None):
    delay 0.1
    old_widget
    events True
    xanchor 1.0
    xpos 0.0
    linear 0.1 xanchor 0.0 xpos 0.0

screen ds_main_menu():
    tag menu
    modal True
    add "bg ext_road_day":
        xalign 0.5
        yalign 0.5
    add "mods/disco_sovenok/gui/menu/main_menu.png":
        xanchor 0.5
        yanchor 0.5
        xpos 0.2
        ypos 0.5
    text "DISCO SOVENOK" size 150 font "mods/disco_sovenok/gui/fonts/KosugiMaru.ttf" xalign 0.95 yalign 0.95
    imagebutton: # Начать игру
        auto "mods/disco_sovenok/gui/menu/start_%s.png"
        xanchor 0.0
        yanchor 0.5
        xpos 0.1
        ypos 0.25
        action [Show("ds_choose_type"), Hide("ds_main_menu")]
    imagebutton: # Загрузить
        auto "mods/disco_sovenok/gui/menu/load_%s.png"
        xanchor 0.0
        yanchor 0.5
        xpos 0.1
        ypos 0.30
        action [Hide('ds_settings', transition=moveoutright), Hide('ds_achievements', transition=moveoutright), Hide('ds_gallery', transition=moveoutright), Show('ds_load', transition=moveinright)]
    imagebutton: # Настройки
        auto "mods/disco_sovenok/gui/menu/settings_%s.png"
        xanchor 0.0
        yanchor 0.5
        xpos 0.1
        ypos 0.35
        action [Hide('ds_load', transition=moveoutright), Hide('ds_achievements', transition=moveoutright), Hide('ds_gallery', transition=moveoutright), Show('ds_settings', transition=moveinright)]
    imagebutton: # Достижения
        auto "mods/disco_sovenok/gui/menu/achieve_%s.png"
        xanchor 0.0
        yanchor 0.5
        xpos 0.1
        ypos 0.40
        action [Hide('ds_settings', transition=moveoutright), Hide('ds_load', transition=moveoutright), Hide('ds_gallery', transition=moveoutright), Show('ds_achievements', transition=moveinright)]
    imagebutton: # Галерея
        auto "mods/disco_sovenok/gui/menu/gallery_%s.png"
        xanchor 0.0
        yanchor 0.5
        xpos 0.1
        ypos 0.45
        action [Hide('ds_settings', transition=moveoutright), Hide('ds_achievements', transition=moveoutright), Hide('ds_load', transition=moveoutright), Show('ds_gallery', transition=moveinright)]
    imagebutton: # Выход
        auto "mods/disco_sovenok/gui/menu/quit_%s.png"
        xanchor 0.0
        yanchor 0.5
        xpos 0.1
        ypos 0.50
        action Confirm(u"Вы действительно хотите выйти в главное меню?", [(Function(ds_screens_diact)), ShowMenu("main_menu")], confirm_selected=True)
    
screen ds_settings():
    pass

screen ds_load():
    pass

screen ds_achievements():
    pass

screen ds_gallery():
    pass
    
screen ds_choose_type():
    modal True
    tag menu
    add "bg ext_road_day":
        xalign 0.5
        yalign 0.5
    add "mods/disco_sovenok/gui/menu/type_title.png":
        xalign 0.0
        yalign 0.0
        xoffset 20
    hbox:
        xalign 0.5
        yalign 1.0
        spacing 20
        imagebutton:
            auto "mods/disco_sovenok/gui/menu/incel_type_%s.png"
            yanchor 1.0
            at transform:
                ypos 2.0
                linear 0.2 ypos 1.0
            action [SetVariable("ds_archetype", 1), Start("ds_start")]
            activate_sound ds_selection
                
        imagebutton:
            auto "mods/disco_sovenok/gui/menu/normic_type_%s.png"
            yanchor 1.0
            at transform:
                ypos 0.0
                linear 0.2 ypos 1.0
            action [SetVariable("ds_archetype", 2), Start("ds_start")]
            activate_sound ds_selection
            
        imagebutton:
            auto "mods/disco_sovenok/gui/menu/chad_type_%s.png"
            yanchor 1.0
            at transform:
                ypos 2.0
                linear 0.2 ypos 1.0
            action [SetVariable("ds_archetype", 3), Start("ds_start")]
            activate_sound ds_selection
            
        imagebutton:
            auto "mods/disco_sovenok/gui/menu/own_type_%s.png"
            yanchor 1.0
            at transform:
                ypos 0.0
                linear 0.2 ypos 1.0
            action [SetVariable("ds_archetype", 0), Function(ds_init_custom), Show('ds_skills', setup=True, change=True), Show("ds_skill_table"), Hide('ds_choose_type')]
            activate_sound ds_selection
    
screen ds_skills(setup, change):
    python:
        SKILLS = [
            'logic', 'encyclopedia', 'rhetoric', 'drama', 'conceptualization', 'visual_calculus',
            'volition', 'inland_empire', 'authority', 'empathy', 'esprit', 'suggestion',
            'endurance', 'pain_threshold', 'physical_instrument', 'instinct', 'shivers', 'half_light',
            'perception', 'coordination', 'reaction_speed', 'savoir_faire', 'interfacing', 'composure'
        ]

    modal True
    tag menu
    if setup:
        add "bg ext_road_day":
            xalign 0.5
            yalign 0.5

    imagebutton:
        xalign 0.0
        xoffset 20
        yalign 1.0
        yoffset -20
        auto "mods/disco_sovenok/gui/skills/back_%s.png"
        action [If(setup, true=[Hide("ds_skill_table"), Hide("ds_skill_info"), Show("ds_choose_type")])]
    if setup:
        imagebutton:
            xalign 1.0
            xoffset -20
            yalign 1.0
            yoffset -20
            auto "mods/disco_sovenok/gui/skills/confirm_%s.png"
            action Start('ds_start')
    if change:
        frame:
            background None
            add "mods/disco_sovenok/gui/skills/available.png"
            xalign 0.5
            yalign 1.0
            xmaximum 525
            ymaximum 75
            yoffset -20
            text str(ds_available_points // 10)+" "+str(ds_available_points % 10):
                size 80
                font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                color "#000000"
                xalign 1.0
                yalign 0.5
                xoffset -5
                yoffset 10

screen ds_skill_table():
    python:
        SKILLS = [
            'logic', 'encyclopedia', 'rhetoric', 'drama', 'conceptualization', 'visual_calculus',
            'volition', 'inland_empire', 'authority', 'empathy', 'esprit', 'suggestion',
            'endurance', 'pain_threshold', 'physical_instrument', 'instinct', 'shivers', 'half_light',
            'perception', 'coordination', 'reaction_speed', 'savoir_faire', 'interfacing', 'composure'
        ]
    frame:
        background "mods/disco_sovenok/gui/skills/attr_lines.png"
        yalign 0.0
        at transform:
            xanchor 1.0
            xpos 0.0
            linear 0.1 xanchor 0.0 xpos 0.0
        fixed:
            xalign 0.5
            yalign 1.0
            xmaximum 1155
            grid 6 4:
                xalign 1.0
                for skill in SKILLS:
                    fixed:
                        xmaximum 180
                        ymaximum 245
                        add "mods/disco_sovenok/gui/skills/[skill].png":
                            xalign 0.5
                            yalign 0.0
                        text str(ds_skill_points[skill]):
                            xalign 1.0
                            yalign 0.0
                            xoffset -10
                            yoffset 5
                            size 48
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        imagebutton:
                            xoffset 2
                            auto "mods/disco_sovenok/gui/skills/skill_%s.png"
                            selected If(ds_chosen_skill == skill)
                            action [ Hide('ds_skill_info'), SetVariable('ds_chosen_skill', skill), Show('ds_skill_info')]
                            activate_sound ds_btn_click

screen ds_hud():
    modal False
    hbox:
        xalign 0.0
        yalign 0.0
        imagebutton:
            idle "mods/disco_sovenok/gui/hud/call_skills.png"
            hover "mods/disco_sovenok/gui/hud/call_skills.png"
            action [Hide("ds_lp_points"), ToggleScreen("ds_skill_table"), Hide("ds_skill_info")]
        imagebutton:
            idle "mods/disco_sovenok/gui/hud/call_lp.png"
            hover "mods/disco_sovenok/gui/hud/call_skills.png"
            action [Hide("ds_skill_table"), Hide("ds_skill_info"), ToggleScreen("ds_lp_points")]

screen ds_skill_info():
    python:
        SKILLS = [
            'logic', 'encyclopedia', 'rhetoric', 'drama', 'conceptualization', 'visual_calculus',
            'volition', 'inland_empire', 'authority', 'empathy', 'esprit', 'suggestion',
            'endurance', 'pain_threshold', 'physical_instrument', 'instinct', 'shivers', 'half_light',
            'perception', 'coordination', 'reaction_speed', 'savoir_faire', 'interfacing', 'composure'
        ]

        SKILL_NAMES = {
            'logic': 'ЛОГИКА',
            'encyclopedia': 'ЭНЦИКЛОПЕДИЯ',
            'rhetoric': 'РИТОРИКА',
            'drama': 'ДРАМА',
            'conceptualization': 'КОНЦЕПТУАЛИЗАЦИЯ',
            'visual_calculus': 'ВИЗУАЛЬНЫЙ АНАЛИЗ',
            'volition': 'CИЛА ВОЛИ',
            'inland_empire': 'ВНУТРЕННЯЯ ИМПЕРИЯ',
            'authority': 'АВТОРИТЕТ',
            'empathy': 'ЭМПАТИЯ',
            'esprit': 'КОМАНДНАЯ ВОЛНА',
            'suggestion': 'ВНУШЕНИЕ',
            'endurance': 'CТОЙКОСТЬ',
            'pain_threshold': 'БОЛЕВОЙ ПОРОГ',
            'physical_instrument': 'ГРУБАЯ СИЛА',
            'instinct': 'ИНСТИНКТ',
            'shivers': 'ТРЕПЕТ',
            'half_light': 'CУМРАК',
            'perception': 'ВОСПРИЯТИЕ',
            'coordination': 'КООРДИНАЦИЯ',
            'reaction_speed': 'СКОРОСТЬ РЕАКЦИИ',
            'savoir_faire': 'ЭКВИЛИБРИСТИКА',
            'interfacing': 'ТЕХНИКА',
            'composure': 'CАМООБЛАДАНИЕ'
        }

        SKILL_DESCR = {
            'logic': 'Управляй интеллектуальной стихией. Разложи мир по полочкам.',
            'encyclopedia': 'Задействуй все свои знания. Удивляй эрудицией.',
            'rhetoric': 'Совершенствуй искусство убеждения. Наслаждайся ожесточёнными интеллектуальными баталиями.',
            'drama': 'Переиграй всех. Ври, но не дай обмануть себя.',
            'conceptualization': 'Стань ценителем творчества. Развей чуткость к искусству.',
            'visual_calculus': 'Восстанавливай события. Заставь законы природы работать на тебя.',
            'volition': 'Держи себя в руках. Сохраняй боевой дух.',
            'inland_empire': 'Интуиция и чутьё. Сны наяву.',
            'authority': 'Подавляй и властвуй. Заяви о себе.',
            'empathy': 'Чувствуй других. Задействуй зеркальные нейроны.',
            'esprit': 'Работай в команде. Будь единым целым с другими.',
            'suggestion': 'Очаровывай мужчин и женщин. Ты — их кукловод.',
            'endurance': 'Держи удар. Не дай себя прикончить.',
            'pain_threshold': 'Разве это боль? Придумайте что-нибудь пожёстче.',
            'physical_instrument': 'Играй мышцами. Наслаждайся своим здоровьем.',
            'instinct': 'Не бойся своих желаний. Демонстрируй своё либидо.',
            'shivers': 'Почувствуй дрожь. Настройся на волну «Совёнка».',
            'half_light': 'Доверься своему телу. Запугивай людей.',
            'perception': 'Смотри, слушай, нюхай, вкушай и осязай. Не упусти не единой детали.',
            'coordination': 'Целься! Огонь!',
            'reaction_speed': 'Будь быстрым, а не мёртвым.',
            'savoir_faire': 'Скользи как тень. Поражай великолепием.',
            'interfacing': 'Управляй механизмами. Вскрывай замки и обчищай карманы.',
            'composure': 'Выпрями спину. Сохраняй покерфейс.'
        }
    fixed:
        add "mods/disco_sovenok/gui/skills/skill_info.png"
        xmaximum 690
        ymaximum 980
        xalign 1.0
        xoffset -20
        add "mods/disco_sovenok/gui/skills/skill_info.png"
        for skill in SKILLS:
            vbox:
                showif (ds_chosen_skill == None):
                    text "Выберите умение."
                showif (ds_chosen_skill == skill):
                    hbox:
                        xalign 0.0
                        xoffset 10
                        add "mods/disco_sovenok/gui/skills/[skill]_large.png" xalign 0.0 yalign 0.0 xoffset 5 yoffset 10
                        if not renpy.get_screen('ds_hud'):
                            vbox:
                                xalign 1.0
                                yalign 0.0
                                showif (ds_skill_points[skill] + ds_available_points >= 1) or (ds_skill_points[skill] == 1):
                                    imagebutton:
                                        auto "mods/disco_sovenok/gui/skills/terrible_%s.png"
                                        selected If(ds_skill_points[skill] == 1)
                                        action [SetVariable('ds_available_points', ds_available_points + (ds_skill_points[skill] - 1)), SensitiveIf(SetDict(ds_skill_points, skill, 1))]
                                        activate_sound ds_selection
                                showif (ds_skill_points[skill] + ds_available_points >= 2) or (ds_skill_points[skill] == 2):
                                    imagebutton:
                                        auto "mods/disco_sovenok/gui/skills/bad_%s.png"
                                        selected If(ds_skill_points[skill] == 2)
                                        action [SetVariable('ds_available_points', ds_available_points + (ds_skill_points[skill] - 2)), SensitiveIf(SetDict(ds_skill_points, skill, 2))]
                                        activate_sound ds_selection
                                showif (ds_skill_points[skill] + ds_available_points >= 3) or (ds_skill_points[skill] == 3):
                                    imagebutton:
                                        auto "mods/disco_sovenok/gui/skills/medium_%s.png"
                                        selected If(ds_skill_points[skill] == 3)
                                        action [SetVariable('ds_available_points', ds_available_points + (ds_skill_points[skill] - 3)), SensitiveIf(SetDict(ds_skill_points, skill, 3))]
                                        activate_sound ds_selection
                                showif (ds_skill_points[skill] + ds_available_points >= 4) or (ds_skill_points[skill] == 4):
                                    imagebutton:
                                        auto "mods/disco_sovenok/gui/skills/good_%s.png"
                                        selected If(ds_skill_points[skill] == 4)
                                        action [SetVariable('ds_available_points', ds_available_points + (ds_skill_points[skill] - 4)), SensitiveIf(SetDict(ds_skill_points, skill, 4))]
                                        activate_sound ds_selection
                                showif (ds_skill_points[skill] + ds_available_points >= 5) or (ds_skill_points[skill] == 5):
                                    imagebutton:
                                        auto "mods/disco_sovenok/gui/skills/excellent_%s.png"
                                        selected If(ds_skill_points[skill] == 5)
                                        action [SetVariable('ds_available_points', ds_available_points + (ds_skill_points[skill] - 5)), SensitiveIf(SetDict(ds_skill_points, skill, 5))]
                                        activate_sound ds_selection
                                showif (ds_skill_points[skill] + ds_available_points >= 6) or (ds_skill_points[skill] == 6):
                                    imagebutton:
                                        auto "mods/disco_sovenok/gui/skills/genius_%s.png"
                                        selected If(ds_skill_points[skill] == 6)
                                        action [SetVariable('ds_available_points', ds_available_points + (ds_skill_points[skill] - 6)), SensitiveIf(SetDict(ds_skill_points, skill, 6))]
                                        activate_sound ds_selection
                        else:
                            text str(ds_skill_points[skill]):
                                size 240
                                font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                                xalign 1.0
                                yalign 0.0
                                xoffset 10
                                yoffset 10
                    text SKILL_NAMES[skill] xalign 0.5 xoffset 10 yoffset 10 size 48
                    text SKILL_DESCR[skill] yalign 1.0 yoffset 10 xoffset 10 size 24 xfill True
    
screen ds_lp_points():
    fixed:
        xmaximum 1815
        ymaximum 975
        add "mods/disco_sovenok/gui/lp/lp_base.png"
        yalign 0.0
        at transform:
            xanchor 0.0
            xpos 1.0
            linear 0.1 xanchor 1.0 xpos 1.0
        grid 2 4:
            xspacing 30
            xfill True
            yfill True
            transpose True
            hbox:
                if (ds_met['dv'] > 0):
                    if ds_lp_dv > 0:
                        add "mods/disco_sovenok/gui/lp/dv_portrait_pos.png" xoffset 40 yoffset 55
                    elif ds_lp_dv < 0:
                        add "mods/disco_sovenok/gui/lp/dv_portrait_neg.png" xoffset 40 yoffset 55
                    else:
                        add "mods/disco_sovenok/gui/lp/dv_portrait.png" xoffset 40 yoffset 55
                else:
                    add "mods/disco_sovenok/gui/lp/unknown.png" xoffset 40 yoffset 55
                fixed:
                    xalign 0.5
                    xoffset 50
                    if ds_met['dv'] == 0:
                        text "ИМЯ НЕИЗВЕСТНО":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            yalign 0.5
                            yoffset 20
                    elif ds_met['dv'] == 1:
                        text "ИМЯ НЕИЗВЕСТНО":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            color "#ffaa00"
                            yalign 0.5
                            yoffset 20
                    else:
                        text "АЛИСА":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            color "#ffaa00"
                            yalign 0.5
                            yoffset 20
                fixed:
                    xoffset -205
                    yoffset 85
                    text (("– " if ds_lp_dv < 0 else "0 ")+str(ds_abs(ds_lp_dv) // 10)+" "+str(ds_abs(ds_lp_dv) % 10)):
                        size 90
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#000000"
            hbox:
                if (ds_met['un'] > 0):
                    if ds_lp_un > 0:
                        add "mods/disco_sovenok/gui/lp/un_portrait_pos.png" xoffset 40 yoffset 35
                    elif ds_lp_un < 0:
                        add "mods/disco_sovenok/gui/lp/un_portrait_neg.png" xoffset 40 yoffset 35
                    else:
                        add "mods/disco_sovenok/gui/lp/un_portrait.png" xoffset 40 yoffset 35
                else:
                    add "mods/disco_sovenok/gui/lp/unknown.png" xoffset 40 yoffset 35
                fixed:
                    xalign 0.5
                    xoffset 50
                    if ds_met['un'] == 0:
                        text "ИМЯ НЕИЗВЕСТНО":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            yalign 0.5
                    elif ds_met['un'] == 1:
                        text "ИМЯ НЕИЗВЕСТНО":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            color "#b956ff"
                            yalign 0.5
                    else:
                        text "ЛЕНА":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            color "#b956ff"
                            yalign 0.5
                fixed:
                    xoffset -205
                    yoffset 75
                    text (("– " if ds_lp_un < 0 else "0 ")+str(ds_abs(ds_lp_un) // 10)+" "+str(ds_abs(ds_lp_un) % 10)):
                        size 90
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#000000"
            hbox:
                if (ds_met['sl'] > 0):
                    if ds_lp_sl > 0:
                        add "mods/disco_sovenok/gui/lp/sl_portrait_pos.png" xoffset 35 yoffset 40
                    elif ds_lp_sl < 0:
                        add "mods/disco_sovenok/gui/lp/sl_portrait_neg.png" xoffset 35 yoffset 40
                    else:
                        add "mods/disco_sovenok/gui/lp/sl_portrait.png" xoffset 35 yoffset 40
                else:
                    add "mods/disco_sovenok/gui/lp/unknown.png" xoffset 35 yoffset 40
                fixed:
                    xalign 0.5
                    xoffset 50
                    if ds_met['sl'] == 0:
                        text "ИМЯ НЕИЗВЕСТНО":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            yalign 0.5
                    elif ds_met['sl'] == 1:
                        text "ИМЯ НЕИЗВЕСТНО":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            color "#ffd200"
                            yalign 0.5
                    else:
                        text "CЛАВЯ":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            color "#ffd200"
                            yalign 0.5
                fixed:
                    xoffset -205
                    yoffset 75
                    text (("– " if ds_lp_sl < 0 else "0 ")+str(ds_abs(ds_lp_sl) // 10)+" "+str(ds_abs(ds_lp_sl) % 10)):
                        size 90
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#000000"
            hbox:
                if (ds_met['us'] > 0):
                    if ds_lp_us > 0:
                        add "mods/disco_sovenok/gui/lp/us_portrait_pos.png" xoffset 37 yoffset 28
                    elif ds_lp_us < 0:
                        add "mods/disco_sovenok/gui/lp/us_portrait_neg.png" xoffset 37 yoffset 28
                    else:
                        add "mods/disco_sovenok/gui/lp/us_portrait.png" xoffset 37 yoffset 28
                else:
                    add "mods/disco_sovenok/gui/lp/unknown.png" xoffset 37 yoffset 28
                fixed:
                    xalign 0.5
                    xoffset 50
                    if ds_met['us'] == 0:
                        text "ИМЯ НЕИЗВЕСТНО":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            yalign 0.5
                            yoffset -20
                    elif ds_met['us'] == 1:
                        text "ИМЯ НЕИЗВЕСТНО":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            color "#ff3200"
                            yalign 0.5
                            yoffset -20
                    else:
                        text "УЛЬЯНА":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            color "#ff3200"
                            yalign 0.5
                            yoffset -20
                fixed:
                    xoffset -205
                    yoffset 65
                    text (("– " if ds_lp_us < 0 else "0 ")+str(ds_abs(ds_lp_us) // 10)+" "+str(ds_abs(ds_lp_us) % 10)):
                        size 90
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#000000"
            hbox:
                if (ds_met['mi'] > 0) and False:
                    add "mods/disco_sovenok/gui/lp/mi_portrait.png"
                else:
                    add "mods/disco_sovenok/gui/lp/unknown.png"
                fixed:
                    xalign 0.5
                    xoffset 10
                    if ds_met['mi'] == 0:
                        text "ИМЯ НЕИЗВЕСТНО":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            yalign 0.5
                            yoffset 20
                    elif ds_met['mi'] == 1:
                        text "ИМЯ НЕИЗВЕСТНО":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            color "#00deff"
                            yalign 0.5
                            yoffset 20
                    else:
                        text "МИКУ":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            color "#00deff"
                            yalign 0.5
                            yoffset 20
                fixed:
                    xoffset -225
                    yoffset 85
                    text (("– " if ds_lp_mi < 0 else "0 ")+str(ds_abs(ds_lp_mi) // 10)+" "+str(ds_abs(ds_lp_mi) % 10)):
                        size 90
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#000000"
            hbox:
                if (ds_met['el'] > 0) and False:
                    add "mods/disco_sovenok/gui/lp/el_portrait.png"
                else:
                    add "mods/disco_sovenok/gui/lp/unknown.png"
                fixed:
                    xalign 0.5
                    xoffset 10
                    if ds_met['el'] == 0:
                        text "ИМЯ НЕИЗВЕСТНО":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            yalign 0.5
                    elif ds_met['el'] == 1:
                        text "ИМЯ НЕИЗВЕСТНО":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            color "#ffff00"
                            yalign 0.5
                    else:
                        text "ЭЛЕКТРОНИК":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            color "#ffff00"
                            yalign 0.5
                fixed:
                    xoffset -225
                    yoffset 75
                    text "0 0 0":
                        size 90
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#000000"
            hbox:
                if (ds_met['mt'] > 0) and False:
                    add "mods/disco_sovenok/gui/lp/mt_portrait.png"
                else:
                    add "mods/disco_sovenok/gui/lp/unknown.png"
                fixed:
                    xalign 0.5
                    xoffset 10
                    if ds_met['mt'] == 0:
                        text "ИМЯ НЕИЗВЕСТНО":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            yalign 0.5
                    elif ds_met['mt'] == 1:
                        text "ИМЯ НЕИЗВЕСТНО":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            color "#00ea32"
                            yalign 0.5
                    else:
                        text "ОЛЬГА":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            color "#00ea32"
                            yalign 0.5
                fixed:
                    xoffset -225
                    yoffset 75
                    text "0 0 0":
                        size 90
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#000000"
            hbox:
                if (ds_met['mz'] > 0) and False:
                    add "mods/disco_sovenok/gui/lp/mz_portrait.png"
                else:
                    add "mods/disco_sovenok/gui/lp/unknown.png"
                fixed:
                    xalign 0.5
                    xoffset 10
                    if ds_met['mz'] == 0:
                        text "ИМЯ НЕИЗВЕСТНО":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            yalign 0.5
                            yoffset -20
                    elif ds_met['mz'] == 1:
                        text "ИМЯ НЕИЗВЕСТНО":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            color "#5481db"
                            yalign 0.5
                            yoffset -20
                    else:
                        text "ЖЕНЯ":
                            size 56
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            color "#5481db"
                            yalign 0.5
                            yoffset -20
                fixed:
                    xoffset -225
                    yoffset 65
                    text "0 0 0":
                        size 90
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#000000"

