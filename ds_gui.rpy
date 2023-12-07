# МОДИФИКАЦИЯ ГРАФИЧЕСКОГО ИНТЕРФЕЙСА

init python:
    import pygame
    import os
    import os.path
    import renpy.store as store
    from renpy.store import *
    from renpy.display.im import ImageBase, image, cache, Composite
    from abc import ABCMeta, abstractmethod

    def ds_min(x, y):
        if x < y:
            return x
        return y

    def ds_max(x, y):
        if x > y:
            return x
        return y

    ds_level_names = {
        '6': u'Элементарно',
        '8': u'Просто',
        '10': u'Средне',
        '11': u'Средне',
        '12': u'Сложно',
        '13': u'Опасно',
        '14': u'Рискованно',
        '15': u'Легендарно',
        '16': u'Невероятно',
        '18': u'Немыслимо',
        '20': u'Невозможно'
    }

    def ds_result_tag(tag, argument):
        open_bracket = '['
        global ds_last_skillcheck
        global ds_level_names
        return [ (renpy.TEXT_TAG, 'color=#b5b5b5'), (renpy.TEXT_TEXT, open_bracket), (renpy.TEXT_TEXT, ds_level_names[str(ds_last_skillcheck.threshold)]),  (renpy.TEXT_TEXT, ': '), (renpy.TEXT_TEXT, 'Успех' if ds_last_skillcheck.result(invoke_callbacks=False) else 'Неудача'), (renpy.TEXT_TEXT, '] '),  (renpy.TEXT_TAG, '/color') ]
    
    def ds_check_tag(tag, argument):
        open_bracket = '['
        global ds_level_names
        skill, level = argument.split(':')
        return [ (renpy.TEXT_TAG, 'color=#b5b5b5'), (renpy.TEXT_TEXT, open_bracket), (renpy.TEXT_TEXT, ds_skill_list[skill].name), (renpy.TEXT_TEXT, ' – '), (renpy.TEXT_TEXT, ds_level_names[level]), (renpy.TEXT_TEXT, ' '), (renpy.TEXT_TEXT, str(level)), (renpy.TEXT_TEXT, '] '), (renpy.TEXT_TAG, '/color')]

    config.self_closing_custom_text_tags['result'] = ds_result_tag
    config.self_closing_custom_text_tags['check'] = ds_check_tag

    def ds_get_check_res_style(*args):
        return ds_check_res_style

    def ds_init_custom():
        global ds_skill_list
        for skill in ds_skill_list:
            ds_skill_list[skill].set_level(3)
        ds_available_points = 1
        ds_semtype = 0
    
    def ds_abs(x):
        if x < 0:
            return -x
        return x

    # ПЕРЕОПРЕДЕЛЕНИЕ ЭКРАНОВ

    # Источник кода ниже: https://es-doc.vercel.app/guide/code-examples.html
    # (с правками автора данного мода)
    SCREENS = [
        "main_menu",
        "game_menu_selector",
        # "quit",
        "say",
        # "preferences",
        "save",
        "load",
        "nvl",
        "choice",
        "text_history_screen",
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

    # КАРТЫ (НАВИГАЦИОННЫЕ)

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
    
    # ГАЛЕРЕЯ

    class DSImage():
        __metaclass__ = ABCMeta

        @abstractmethod
        def get_type(self):
            pass

        @abstractmethod
        def get_name(self):
            pass

        @abstractmethod
        def get_full_name(self):
            pass

        @abstractmethod
        def get_add_img(self):
            pass

        @abstractmethod
        def is_hentai(self):
            pass

        @abstractmethod
        def is_orig(self):
            pass

        def is_seen(self):
            return renpy.seen_image(self.get_full_name())
        
        def get_all_img(self):
            return [self.get_full_name()] + self.get_add_img()
    
    class DSBackground(DSImage):
        def __init__(self, name, add_img=[], orig=False, hent=False):
            self.__name = name
            self.__orig = orig
            self.__hent = hent
            self.__add_img = []
            for img in add_img:
                self.__add_img.append('bg '+img)
        
        def get_name(self):
            return self.__name
        
        def get_type(self):
            return 'bg'
        
        def get_add_img(self):
            return self.__add_img

        def is_orig(self):
            return self.__orig

        def is_hentai(self):
            return self.__hent

        def get_full_name(self):
            return self.get_type() + ' ' + self.get_name()
    
    class DSArtImage(DSImage):
        def __init__(self, name, add_img=[], orig=False, hent=False):
            self.__name = name
            self.__orig = orig
            self.__hent = hent
            self.__add_img = []
            for img in add_img:
                self.__add_img.append('cg '+img)
        
        def get_name(self):
            return self.__name
        
        def get_type(self):
            return 'cg'
        
        def get_add_img(self):
            return self.__add_img

        def is_orig(self):
            return self.__orig

        def is_hentai(self):
            return self.__hent

        def get_full_name(self):
            return self.get_type() + ' ' + self.get_name()
    
    ds_bg_list = [
        DSBackground('bus_stop', orig=True),
        DSBackground('ext_aidpost_day', orig=True),
        DSBackground('ext_aidpost_night', orig=True),
        DSBackground('ext_bathhouse_night', orig=True),
        DSBackground('ext_beach_day', orig=True),
        DSBackground('ext_beach_sunset', orig=True),
        DSBackground('ext_beach_night', orig=True),
        DSBackground('ext_boathouse_day', orig=True),
        DSBackground('ext_boathouse_night', orig=True),
        DSBackground('ext_bus', orig=True),
        DSBackground('ext_bus_night', orig=True),
        DSBackground('ext_camp_entrance_day', orig=True),
        DSBackground('ext_camp_entrance_night', orig=True),
        DSBackground('ext_clubs_day', orig=True),
        DSBackground('ext_clubs_night', orig=True),
        DSBackground('ext_dining_hall_away_day', orig=True),
        DSBackground('ext_dining_hall_away_sunset', orig=True),
        DSBackground('ext_dining_hall_away_night', orig=True),
        DSBackground('ext_dining_hall_near_day', orig=True),
        DSBackground('ext_dining_hall_near_sunset', orig=True),
        DSBackground('ext_dining_hall_near_night', orig=True),
        DSBackground('ext_house_of_dv_day', orig=True),
        DSBackground('ext_house_of_dv_night', orig=True),
        DSBackground('ext_house_of_mt_day', orig=True),
        DSBackground('ext_house_of_mt_night', orig=True),
        DSBackground('ext_house_of_mt_night_without_light', orig=True),
        DSBackground('ext_house_of_mt_sunset', orig=True),
        DSBackground('ext_house_of_sl_day', orig=True),
        DSBackground('ds_ext_sl_house_sunset'),
        DSBackground('ds_ext_sl_house_night'),
        DSBackground('ds_ext_sl_house_night2'),
        DSBackground('ext_house_of_un_day', orig=True),
        DSBackground('ds_ext_un_sunset'),
        DSBackground('ds_ext_un_night'),
        DSBackground('ext_houses_day', orig=True),
        DSBackground('ext_houses_sunset', orig=True),
        DSBackground('ext_island_day', orig=True),
        DSBackground('ext_island_night', orig=True),
        DSBackground('ext_library_day', orig=True),
        DSBackground('ext_library_night', orig=True),
        DSBackground('ext_musclub_day', orig=True),
        DSBackground('ds_ext_musclub_sunset'),
        DSBackground('ds_ext_musclub_night'),
        DSBackground('ds_ext_musclub_veranda_day'),
        DSBackground('ext_no_bus', orig=True),
        DSBackground('ext_no_bus_night', orig=True),
        DSBackground('ext_no_bus_sunset', orig=True),
        DSBackground('ext_old_building_night', orig=True),
        DSBackground('ext_old_building_night_moonlight', orig=True),
        DSBackground('ext_path2_day', orig=True),
        DSBackground('ext_path2_night', orig=True),
        DSBackground('ext_path_day', orig=True),
        DSBackground('ext_path_night', orig=True),
        DSBackground('ext_path_sunset', orig=True),
        DSBackground('ext_playground_day', orig=True),
        DSBackground('ext_playground_night', orig=True),
        DSBackground('ext_polyana_day', orig=True),
        DSBackground('ext_polyana_sunset', orig=True),
        DSBackground('ext_polyana_night', orig=True),
        DSBackground('ext_road_day', orig=True),
        DSBackground('ext_road_night', orig=True),
        DSBackground('ext_road_night2', orig=True),
        DSBackground('ext_road_sunset', orig=True),
        DSBackground('ext_square_day', orig=True),
        DSBackground('ext_square_day_city', orig=True),
        DSBackground('ext_square_night', orig=True),
        DSBackground('ext_square_night_party', orig=True),
        DSBackground('ext_square_night_party2', orig=True),
        DSBackground('ext_square_sunset', orig=True),
        DSBackground('ext_stage_big_night', orig=True),
        DSBackground('ext_stage_normal_day', orig=True),
        DSBackground('ext_stage_normal_night', orig=True),
        DSBackground('ext_washstand2_day', orig=True),
        DSBackground('ext_washstand_day', orig=True),
        DSBackground('ds_ext_train'),
        DSBackground('ds_ext_el_house_day'),
        DSBackground('ds_ext_el_house_sunset'),
        DSBackground('ds_ext_el_house_night'),
        DSBackground('ds_ext_houses_night'),
        DSBackground('ds_ext_clubs_gate_night'),
        DSBackground('ds_ext_clubs_gate_day'),
        DSBackground('ds_ext_storage_day'),
        DSBackground('ds_ext_storage_sunset'),
        DSBackground('ds_ext_storage_night'),
        DSBackground('ds_ext_showers_day'),
        DSBackground('ds_ext_showers_night'),
        DSBackground('ds_ext_backdoor_day'),
        DSBackground('ds_ext_backdoor_sunset'),
        DSBackground('ds_ext_backdoor_night'),
        DSBackground('ds_ext_backroad_day'),
        DSBackground('ds_ext_backroad_sunset'),
        DSBackground('ds_ext_railroad_day'),
        DSBackground('ds_ext_railroad_sunset'),
        DSBackground('ds_ext_bus_town'),
        DSBackground('ds_ext_square2_day'),
        DSBackground('ds_ext_square2_night'),
        DSBackground('ds_ext_another_club_day'),
        DSBackground('ds_ext_admin_day'),
        DSBackground('ds_ext_admin_night'),
        DSBackground('int_aidpost_day', orig=True),
        DSBackground('int_aidpost_day_apple', orig=True),
        DSBackground('int_aidpost_night', orig=True),
        DSBackground('int_bus', orig=True),
        DSBackground('ds_int_bus_forest'),
        DSBackground('int_bus_black', orig=True),
        DSBackground('int_bus_night', orig=True),
        DSBackground('int_bus_people_day', orig=True),
        DSBackground('int_bus_people_night', orig=True),
        DSBackground('int_catacombs_door', orig=True),
        DSBackground('int_catacombs_entrance', orig=True),
        DSBackground('int_catacombs_entrance_red', orig=True),
        DSBackground('int_catacombs_hole', orig=True),
        DSBackground('int_catacombs_living', orig=True),
        DSBackground('int_catacombs_living_nodoor', orig=True),
        DSBackground('int_clubs_male2_night', orig=True),
        DSBackground('int_clubs_male2_night_nolight', orig=True),
        DSBackground('int_clubs_male_day', orig=True),
        DSBackground('int_clubs_male_sunset', orig=True),
        DSBackground('int_dining_hall_day', orig=True),
        DSBackground('int_dining_hall_night', orig=True),
        DSBackground('int_dining_hall_people_day', orig=True),
        DSBackground('int_dining_hall_sunset', orig=True),
        DSBackground('int_house_of_dv_day', orig=True),
        DSBackground('int_house_of_dv_night', orig=True),
        DSBackground('int_house_of_mt_day', orig=True),
        DSBackground('int_house_of_mt_night', orig=True),
        DSBackground('int_house_of_mt_night2', orig=True),
        DSBackground('int_house_of_mt_noitem_night', orig=True),
        DSBackground('int_house_of_mt_sunset', orig=True),
        DSBackground('int_house_of_sl_day', orig=True),
        DSBackground('int_house_of_un_day', orig=True),
        DSBackground('int_house_of_un_night', orig=True),
        DSBackground('int_liaz', orig=True),
        DSBackground('int_library_day', orig=True),
        DSBackground('int_library_night', orig=True),
        DSBackground('int_library_night2', orig=True),
        DSBackground('int_mine', orig=True),
        DSBackground('int_mine_coalface', orig=True),
        DSBackground('int_mine_crossroad', orig=True),
        DSBackground('int_mine_door', orig=True),
        DSBackground('int_mine_exit_night_light', orig=True),
        DSBackground('int_mine_exit_night_nolight', orig=True),
        DSBackground('int_mine_exit_night_torch', orig=True),
        DSBackground('int_mine_halt', orig=True),
        DSBackground('int_mine_room', orig=True),
        DSBackground('int_mine_room_red', orig=True),
        DSBackground('int_musclub_day', orig=True),
        DSBackground('int_old_building_night', orig=True),
        DSBackground('ds_int_storage_day'),
        DSBackground('ds_int_storage_day2'),
        DSBackground('ds_int_storage_night'),
        DSBackground('ds_int_sporthall_day'),
        DSBackground('ds_int_sporthall_night'),
        DSBackground('ds_int_dininghall_table1_day'),
        DSBackground('ds_int_dininghall_table1_sunset'),
        DSBackground('ds_int_dininghall_table1_night'),
        DSBackground('ds_int_dininghall_table2_day'),
        DSBackground('ds_int_dininghall_table2_sunset'),
        DSBackground('ds_int_dininghall_door_day'),
        DSBackground('ds_int_dininghall_door_sunset'),
        DSBackground('ds_int_dininghall_door_night'),
        DSBackground('ds_int_el_house_sunset'),
        DSBackground('ds_int_el_house_night'),
        DSBackground('ds_int_sl_night'),
        DSBackground('ds_int_sl_night_light'),
        DSBackground('ds_int_bathhouse'),
        DSBackground('ds_int_bathhouse_steam'),
        DSBackground('ds_int_library_basement'),
        DSBackground('ds_int_train'),
        DSBackground('ds_int_admin_corridor'),
        DSBackground('ds_int_admin_day'),
        DSBackground('ds_int_admin_night'),
        DSBackground('ds_int_admin_night_light'),
        DSBackground('ds_int_admin_day_boxes1'),
        DSBackground('ds_int_admin_sunset_boxes1'),
        DSBackground('ds_int_admin_day_boxes2'),
        DSBackground('ds_int_admin_sunset_boxes2'),
        DSBackground('ds_int_admin_night_boxes2'),
        DSBackground('ds_int_admin_morning_boxes2'),
        DSBackground('ds_int_kitchen_day'),
        DSBackground('ds_int_kitchen_sunset'),
        DSBackground('ds_int_kitchen_night'),
        DSBackground('ds_int_wardrobe'),
        DSBackground('ds_int_clubs_pantry'),
        DSBackground('ds_int_toilet_day'),
        DSBackground('ds_int_toilet_night'),
        DSBackground('ds_field_day'),
        DSBackground('semen_room', orig=True),
        DSBackground('semen_room_window', orig=True),
    ]

    ds_cg_list = [
        DSArtImage('ds_day1_bus_window'),
        DSArtImage('ds_day1_bus_exit'),
        DSArtImage('ds_day1_hide'),
        DSArtImage('d1_food_normal', orig=True),
        DSArtImage('d1_food_skolop', orig=True),
        DSArtImage('d1_grasshopper', orig=True),
        DSArtImage('d1_rena_sunset', orig=True),
        DSArtImage('d1_sl_dinner_0', orig=True, add_img=['d1_sl_dinner']),
        DSArtImage('d1_uv_2', orig=True, add_img=['d1_uv']),
        DSArtImage('ds_day1_grasshopper_f1', add_img=['ds_day1_grasshopper_f2', 'ds_day1_grasshopper_f3']),
        DSArtImage('ds_day1_dv_on_grass'),
        DSArtImage('ds_day1_dv_dinner'),
        DSArtImage('ds_day1_dv_hiding'),
        DSArtImage('ds_day1_un_book'),
        DSArtImage('d2_mirror', orig=True),
        DSArtImage('ds_day2_mt_undress1', add_img=['ds_day2_mt_undress2']),
        DSArtImage('ds_day2_lineup'),
        DSArtImage('d2_micu_lib', orig=True),
        DSArtImage('ds_day2_mi_piano1', add_img=['ds_day2_mi_piano2']),
        DSArtImage('ds_day2_cs_near', orig=True),
        DSArtImage('ds_day2_dv_hits_el'),
        DSArtImage('d2_sovenok', orig=True),
        DSArtImage('d2_ussr_falling', orig=True),
        DSArtImage('d2_2ch_beach', orig=True),
        DSArtImage('ds_day2_swim_dv'),
        DSArtImage('d2_slavya_forest', orig=True),
        DSArtImage('ds_day2_sl_swim', hent=True),
        DSArtImage('d3_disco', orig=True),
        DSArtImage('ds_day3_dv_guitar', orig=True),
        DSArtImage('d3_dv_scene_2', add_img=['d3_dv_scene_1']),
        DSArtImage('ds_day3_train'),
        DSArtImage('ds_day3_sl_bath', hent=True),
        DSArtImage('d3_sl_dance', orig=True),
        DSArtImage('d3_sl_evening', orig=True),
        DSArtImage('d3_sl_library', orig=True),
        DSArtImage('d3_soccer', orig=True),
        DSArtImage('d3_un_dance', orig=True),
        DSArtImage('d3_un_forest', orig=True),
        DSArtImage('d3_us_dinner', orig=True),
        DSArtImage('d3_us_library_1', orig=True, add_img=['d3_us_library_2', 'd3_us_library_3', 'd3_us_library_4']),
        DSArtImage('d3_ussr_catched', orig=True),
        DSArtImage('ds_day3_disco_dv'),
        DSArtImage('ds_day3_dv_dance'),
        DSArtImage('ds_day3_us_caught_f1', add_img=['ds_day3_us_caught_f2', 'ds_day3_us_caught_f3']),
        DSArtImage('ds_day3_us_potato_1', add_img=['ds_day3_us_potato_2']),
        DSArtImage('ds_day3_mi_piano_1', add_img=['ds_day3_mi_piano_2']),
        DSArtImage('ds_day3_mi_guitar'),
        DSArtImage('ds_day3_mi_teaching'),
        DSArtImage('ds_day3_robot_fail'),
        DSArtImage('ds_day3_hatch', add_img=['ds_dayx_hatch_open']),
        DSArtImage('ds_day3_cs_waiting'),
        DSArtImage('day4_us_morning', orig=True),
        DSArtImage('d4_catac', orig=True),
        DSArtImage('d4_catac_dv', orig=True),
        DSArtImage('d4_catac_sl', orig=True),
        DSArtImage('d4_catac_un', orig=True),
        DSArtImage('d4_catac_us_2', orig=True, add_img=['d4_catac_us']),
        DSArtImage('d4_dv_mt', orig=True),
        DSArtImage('ds_day4_el_undress'),
        DSArtImage('d4_mi_guitar', orig=True),
        DSArtImage('d4_mi_sing', orig=True),
        DSArtImage('d4_sh_sit', orig=True),
        DSArtImage('d4_sh_stay', orig=True),
        DSArtImage('d4_us_cancer', orig=True),
        DSArtImage('d4_us_morning', orig=True),
        DSArtImage('d4_uv', orig=True),
        DSArtImage('d4_uv_1', orig=True),
        DSArtImage('d5_boat', orig=True),
        DSArtImage('d5_boat_2', orig=True),
        DSArtImage('d5_cake', orig=True),
        DSArtImage('d5_clubs_robot', orig=True),
        DSArtImage('d5_dv_argue', orig=True, add_img=['d5_dv_argue_2', 'd5_dv_argue_3']),
        DSArtImage('d5_dv_island', orig=True),
        DSArtImage('ds_dayx_us_wash1', orig=True, add_img=['ds_dayx_us_wash2', 'ds_dayx_us_wash3']),
        DSArtImage('d5_mi', orig=True),
        DSArtImage('d5_sh_us', orig=True),
        DSArtImage('d5_sl_sleep_2', orig=True, add_img=['d5_sl_sleep']),
        DSArtImage('d5_strawberry_race', orig=True),
        DSArtImage('d5_un_island', orig=True),
        DSArtImage('d5_un_sleep', orig=True),
        DSArtImage('d5_us_ghost', orig=True, add_img=['d5_us_ghost_2']),
        DSArtImage('d5_us_kiss', orig=True),
        DSArtImage('d5_us_sit', orig=True),
        DSArtImage('ds_day4_uv_appear1', orig=True, add_img=['ds_day4_uv_appear2']),
        DSArtImage('d6_dv_fight', orig=True, add_img=['d6_dv_fight_2', 'd6_dv_fight_3']),
        DSArtImage('d6_pioneer', orig=True),
        DSArtImage('d6_sl_forest_2', orig=True, add_img=['d6_sl_forest']),
        DSArtImage('d6_sl_swim', orig=True),
        DSArtImage('d6_sl_hentai_2', orig=True, hent=True, add_img=['d6_sl_hentai_1']),
        DSArtImage('d6_un_evening_2', orig=True, add_img=['d6_un_evening_1']),
        DSArtImage('d6_un_punch', orig=True),
        DSArtImage('d6_us_film', orig=True),
        DSArtImage('d6_us_night_2', orig=True),
        DSArtImage('d6_uv', orig=True, add_img=['d6_uv_2']),
        DSArtImage('d7_dv', orig=True, add_img=['d7_dv_2']),
        DSArtImage('d7_pioneers_leaving', orig=True),
        DSArtImage('d7_pioneers_leaving_without_us', orig=True),
        DSArtImage('ds_dayx_sl_morning1', add_img=['ds_dayx_sl_morning2']),
        DSArtImage('ds_dayx_un_sex1', hent=True, add_img=['ds_dayx_un_sex2']),
        DSArtImage('d7_un_suicide', orig=True),
        DSArtImage('d7_uv', orig=True),
        DSArtImage('ds_dayx_mi_sex1', hent=True, add_img=['ds_dayx_mi_sex2']),
        DSArtImage('uvao_h_cenz', hent=True),
        DSArtImage('ds_day9_dv_sex1', hent=True, add_img=['ds_day9_dv_sex2', 'ds_day9_dv_sex3']),
        DSArtImage('epilogue_dv_2', orig=True),
        DSArtImage('epilogue_dv_3', orig=True),
        DSArtImage('epilogue_mi_1', orig=True),
        DSArtImage('epilogue_mi_2', orig=True),
        DSArtImage('epilogue_mi_3', orig=True),
        DSArtImage('epilogue_mi_4', orig=True),
        DSArtImage('epilogue_mi_5', orig=True),
        DSArtImage('epilogue_mi_6', orig=True),
        DSArtImage('epilogue_mi_7', orig=True),
        DSArtImage('epilogue_mi_8', orig=True),
        DSArtImage('epilogue_mi_9', orig=True),
        DSArtImage('epilogue_sl', orig=True),
        DSArtImage('epilogue_sl_2', orig=True),
        DSArtImage('epilogue_un', orig=True),
        DSArtImage('epilogue_un_bad', orig=True),
        DSArtImage('epilogue_un_good', orig=True),
        DSArtImage('epilogue_us', orig=True, add_img=['epilogue_us_alone', 'epilogue_us_3_a']),
        DSArtImage('epilogue_uv', orig=True),
        DSArtImage('epilogue_uv_2', orig=True, add_img=['epilogue_uv_3']),
        DSArtImage('final_all_2', orig=True),
    ]

    renpy.start_predict_screen('ds_gallery')

init:
    if not config_session:
        image widget small_map_ds = "mods/disco_sovenok/gui/map/small_map_bg.jpg" # Путь до фона карты
        image bg small_map_ds     = "mods/disco_sovenok/gui/map/small_map_available.jpg" # Путь до версии карты с idle-версией

    $ init_small_map_zones_ds()

    $ ds_chosen_skill = None
    $ ds_available_points = 1

label _show_small_map_ds:
    show widget small_map_ds
    $ store.small_map_enabled_ds = True
    $ ui.interact()
    jump _show_small_map_ds

style ds_check_res_style:
    color "#b5b5b5"

style ds_history_style_ch:
    font "0@mods/disco_sovenok/gui/fonts/Baskerville.ttc"
    rest_indent 30
    textalign 0.0
    hover_color "#86cd4d"
    idle_color "#ffdd7d"
    outlines [(absolute(0), "#000", absolute(1), absolute(1))]

style ds_history_style_noch:
    font "0@mods/disco_sovenok/gui/fonts/Baskerville.ttc"
    first_indent 30
    rest_indent 30
    textalign 0.0
    hover_color "#86cd4d"
    idle_color "#ffdd7d"
    outlines [(absolute(0), "#000", absolute(1), absolute(1))]

style ds_history_style_ch_prolog:
    font "0@mods/disco_sovenok/gui/fonts/Baskerville.ttc"
    rest_indent 30
    textalign 0.0
    idle_color "#afdafc"
    hover_color "#ffdd7d"
    outlines [(absolute(0), "#000", absolute(1), absolute(1))]

style ds_history_style_noch_prolog:
    font "0@mods/disco_sovenok/gui/fonts/Baskerville.ttc"
    first_indent 30
    rest_indent 30
    textalign 0.0
    idle_color "#afdafc"
    hover_color "#ffdd7d"
    outlines [(absolute(0), "#000", absolute(1), absolute(1))]

style ds_say_style_prolog:
    size 24
    color "#00bfff"
    drop_shadow [ (-1, -1), (1, -1), (-1, 1), (1, 1) ]
    drop_shadow_color "#000001"
    font "0@mods/disco_sovenok/gui/fonts/Baskerville.ttc"
    line_spacing 2

style ds_say_style:
    size 24
    color "#ffdd7d"
    drop_shadow [ (-1, -1), (1, -1), (-1, 1), (1, 1) ]
    drop_shadow_color "#000001"
    font "0@mods/disco_sovenok/gui/fonts/Baskerville.ttc"
    line_spacing 2

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

screen ds_game_menu_selector():
    tag menu
    modal True
    window:
        background None
        at transform:
            on show:
                xoffset -1920
                linear 0.1 xoffset 0
            on hide:
                xoffset 0
                linear 0.1 xoffset -1920
        add "mods/disco_sovenok/gui/menu/main_menu.png":
            xanchor 0.5
            yanchor 0.5
            xpos 0.2
            ypos 0.5
        imagebutton: # Продолжить
            auto "mods/disco_sovenok/gui/menu/continue_%s.png"
            xanchor 0.0
            yanchor 0.5
            xpos 0.1
            ypos 0.25
            action [Hide('ds_settings', transition=moveouttop), Hide('ds_achievements', transition=moveouttop), Hide('ds_gallery', transition=moveouttop), Hide('ds_load'), Hide("ds_game_menu_selector", transition=moveoutleft), Return()]
        showif not renpy.get_screen('ds_save'):
            imagebutton: # Сохранить
                auto "mods/disco_sovenok/gui/menu/save_%s.png"
                xanchor 0.0
                yanchor 0.5
                xpos 0.1
                ypos 0.30
                action [Hide('ds_preferences', transition=moveouttop), Hide('ds_achievements', transition=moveouttop), Hide('ds_gallery', transition=moveouttop), Hide('ds_load', transition=moveouttop), Show('ds_save', transition=moveintop)]
        else:
            add "mods/disco_sovenok/gui/menu/selected_base.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.2
                ypos 0.30
            add "mods/disco_sovenok/gui/menu/save_selected.png":
                xanchor 0.0
                yanchor 0.5
                xpos 0.1
                ypos 0.30
        showif not renpy.get_screen('ds_load'):
            imagebutton: # Загрузить
                auto "mods/disco_sovenok/gui/menu/load_%s.png"
                xanchor 0.0
                yanchor 0.5
                xpos 0.1
                ypos 0.35
                action [Hide('ds_preferences'), Hide('ds_achievements'), Hide('ds_gallery'), Hide('ds_save'), With(moveouttop), Show('ds_load'), With(moveintop)]
        else:
            add "mods/disco_sovenok/gui/menu/selected_base.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.2
                ypos 0.35
            add "mods/disco_sovenok/gui/menu/load_selected.png":
                xanchor 0.0
                yanchor 0.5
                xpos 0.1
                ypos 0.35
        showif not renpy.get_screen('ds_settings'):
            imagebutton: # Настройки
                auto "mods/disco_sovenok/gui/menu/settings_%s.png"
                xanchor 0.0
                yanchor 0.5
                xpos 0.1
                ypos 0.40
                action [Hide('ds_load'), Hide('ds_achievements'), Hide('ds_gallery'), Hide('ds_save', transition=moveouttop), Show('ds_preferences')]
        else:
            add "mods/disco_sovenok/gui/menu/selected_base.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.2
                ypos 0.40
            add "mods/disco_sovenok/gui/menu/settings_selected.png":
                xanchor 0.0
                yanchor 0.5
                xpos 0.1
                ypos 0.40
        showif not renpy.get_screen('ds_achievements'):
            imagebutton: # Достижения
                auto "mods/disco_sovenok/gui/menu/achieve_%s.png"
                xanchor 0.0
                yanchor 0.5
                xpos 0.1
                ypos 0.45
                action [Hide('ds_settings'), Hide('ds_load'), Hide('ds_gallery'), Hide('ds_save', transition=moveouttop), Show('ds_achievements')]
        else:
            add "mods/disco_sovenok/gui/menu/selected_base.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.2
                ypos 0.45
            add "mods/disco_sovenok/gui/menu/achieve_selected.png":
                xanchor 0.0
                yanchor 0.5
                xpos 0.1
                ypos 0.45
        showif not renpy.get_screen('ds_gallery'):
            imagebutton: # Галерея
                auto "mods/disco_sovenok/gui/menu/gallery_%s.png"
                xanchor 0.0
                yanchor 0.5
                xpos 0.1
                ypos 0.50
                action [Hide('ds_preferences', transition=moveouttop), Hide('ds_achievements', transition=moveouttop), Hide('ds_load', transition=moveouttop), Hide('ds_save', transition=moveouttop), Show('ds_gallery', transition=moveintop)]
        else:
            add "mods/disco_sovenok/gui/menu/selected_base.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.2
                ypos 0.50
            add "mods/disco_sovenok/gui/menu/gallery_selected.png":
                xanchor 0.0
                yanchor 0.5
                xpos 0.1
                ypos 0.50
        imagebutton: # В меню
            auto "mods/disco_sovenok/gui/menu/menu_%s.png"
            xanchor 0.0
            yanchor 0.5
            xpos 0.1
            ypos 0.55
            action [Hide('ds_settings'), Hide('ds_gallery'), Hide('ds_achievements'), Hide('ds_load'), Hide('ds_save'), MainMenu()]
        imagebutton: # Выход
            auto "mods/disco_sovenok/gui/menu/exit_%s.png"
            xanchor 0.0
            yanchor 0.5
            xpos 0.1
            ypos 0.60
            action [Hide('ds_settings'), Hide('ds_gallery'), Hide('ds_achievements'), Hide('ds_load'), Hide('ds_save'), ShowMenu('quit')]

screen ds_main_menu():
    python:
        from time import localtime, strftime
        t = strftime("%H:%M:%S", localtime())
        hour, minute, sec = t.split(":")
        hour = int(hour)
    tag menu
    modal True
    if hour in [22,23,24,0,1,2,3,4,5,6]:
        add "bg ext_road_night":
            xalign 0.5
            yalign 0.5
    elif hour in [20,21,7,8]:
        add "bg ext_road_sunset":
            xalign 0.5
            yalign 0.5
    else:
        add "bg ext_road_day":
            xalign 0.5
            yalign 0.5
    fixed:
        at transform:
            on show:
                xoffset -1920
                linear 0.1 xoffset 0
            on hide:
                xoffset 0
                linear 0.1 xoffset -1920
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
            action [Hide('ds_settings'), Hide('ds_achievements'), Hide('ds_gallery'), Hide('ds_load'), SetVariable('ds_game_started', False), Show("ds_choose_type"), Hide("ds_main_menu", transition=moveoutleft)]
        showif not renpy.get_screen('ds_load'):
            imagebutton: # Загрузить
                auto "mods/disco_sovenok/gui/menu/load_%s.png"
                xanchor 0.0
                yanchor 0.5
                xpos 0.1
                ypos 0.30
                action [Hide('ds_preferences'), Hide('ds_achievements'), Hide('ds_gallery'), Show('ds_load')]
        else:
            add "mods/disco_sovenok/gui/menu/selected_base.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.2
                ypos 0.30
            add "mods/disco_sovenok/gui/menu/load_selected.png":
                xanchor 0.0
                yanchor 0.5
                xpos 0.1
                ypos 0.30
        showif not renpy.get_screen('ds_preferences'):
            imagebutton: # Настройки
                auto "mods/disco_sovenok/gui/menu/settings_%s.png"
                xanchor 0.0
                yanchor 0.5
                xpos 0.1
                ypos 0.35
                action [Hide('ds_load'), Hide('ds_achievements'), Hide('ds_gallery'), Show('ds_preferences')]
        else:
            add "mods/disco_sovenok/gui/menu/selected_base.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.2
                ypos 0.35
            add "mods/disco_sovenok/gui/menu/settings_selected.png":
                xanchor 0.0
                yanchor 0.5
                xpos 0.1
                ypos 0.35
        showif not renpy.get_screen('ds_achievements'):
            imagebutton: # Достижения
                auto "mods/disco_sovenok/gui/menu/achieve_%s.png"
                xanchor 0.0
                yanchor 0.5
                xpos 0.1
                ypos 0.40
                action [Hide('ds_preferences'), Hide('ds_load'), Hide('ds_gallery'), Show('ds_achievements')]
        else:
            add "mods/disco_sovenok/gui/menu/selected_base.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.2
                ypos 0.40
            add "mods/disco_sovenok/gui/menu/achieve_selected.png":
                xanchor 0.0
                yanchor 0.5
                xpos 0.1
                ypos 0.40
        showif not renpy.get_screen('ds_gallery'):
            imagebutton: # Галерея
                auto "mods/disco_sovenok/gui/menu/gallery_%s.png"
                xanchor 0.0
                yanchor 0.5
                xpos 0.1
                ypos 0.45
                action [Hide('ds_preferences', transition=moveouttop), Hide('ds_achievements', transition=moveouttop), Hide('ds_load', transition=moveouttop), Show('ds_gallery', transition=moveintop)]
        else:
            add "mods/disco_sovenok/gui/menu/selected_base.png":
                xanchor 0.5
                yanchor 0.5
                xpos 0.2
                ypos 0.45
            add "mods/disco_sovenok/gui/menu/gallery_selected.png":
                xanchor 0.0
                yanchor 0.5
                xpos 0.1
                ypos 0.45
        imagebutton: # В меню БЛ
            auto "mods/disco_sovenok/gui/menu/quit_%s.png"
            xanchor 0.0
            yanchor 0.5
            xpos 0.1
            ypos 0.50
            action [Hide('ds_preferences'), Hide('ds_gallery'), Hide('ds_achievements'), Hide('ds_load'), Hide('ds_save'), Confirm(u"Вы действительно хотите выйти в главное меню?", [(Function(ds_screens_diact)), ShowMenu("main_menu")], confirm_selected=True)]
        imagebutton: # Выход
            auto "mods/disco_sovenok/gui/menu/exit_%s.png"
            xanchor 0.0
            yanchor 0.5
            xpos 0.1
            ypos 0.55
            action [Hide('ds_preferences'), Hide('ds_gallery'), Hide('ds_achievements'), Hide('ds_load'), Hide('ds_save'), ShowMenu('quit')]
    
screen ds_preferences():
    frame:
        background "mods/disco_sovenok/gui/loadsave/loadsave_base.png"
        yfill True
        xalign 1.0
        xoffset -100
        xmaximum 1100
        at transform:
            on show:
                yoffset -1080
                linear 0.1 yoffset 0
            on hide:
                yoffset 0
                linear 0.1 yoffset -1080
        fixed:
            yalign 0.0
            ymaximum 1000
            xsize 1100
            vbox:
                xminimum 1100
                fixed:
                    ymaximum 50
                    text "Режим экрана":
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#ffffff"
                        size 30
                        xalign 0.0
                        xoffset 20
                    hbox:
                        ysize 50
                        xanchor 0.5
                        xpos 0.75
                        imagebutton:
                            auto "mods/disco_sovenok/gui/settings/decrease_%s.png"
                            action Preference('display', 'toggle')
                        if preferences.fullscreen:
                            text "На весь экран":
                                ysize 50
                                font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                                color "#ffffff"
                                size 24
                        else:
                            text "В окне":
                                ysize 50
                                font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                                color "#ffffff"
                                size 24
                        imagebutton:
                            auto "mods/disco_sovenok/gui/settings/increase_%s.png"
                            action Preference('display', 'toggle')
                fixed:
                    ymaximum 50
                    text "Размер шрифта":
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#ffffff"
                        size 30
                        xalign 0.0
                        xoffset 20
                    hbox:
                        ysize 50
                        xanchor 0.5
                        xpos 0.75
                        imagebutton:
                            auto "mods/disco_sovenok/gui/settings/decrease_%s.png"
                            action ToggleField(persistent, 'font_size', true_value='large', false_value='small')
                        if persistent.font_size == 'large':
                            text "Большой":
                                ysize 50
                                font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                                color "#ffffff"
                                size 30
                        else:
                            text "Обычный":
                                ysize 50
                                font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                                color "#ffffff"
                                size 24
                        imagebutton:
                            auto "mods/disco_sovenok/gui/settings/increase_%s.png"
                            action ToggleField(persistent, 'font_size', true_value='large', false_value='small')
                fixed:
                    ymaximum 50
                    text "Пропускать":
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#ffffff"
                        size 30
                        xalign 0.0
                        xoffset 20
                    hbox:
                        ysize 50
                        xanchor 0.5
                        xpos 0.75
                        imagebutton:
                            auto "mods/disco_sovenok/gui/settings/decrease_%s.png"
                            action Preference("skip", "toggle")
                        if preferences.skip_unseen:
                            text "Всё":
                                ysize 50
                                font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                                color "#ffffff"
                                size 24
                        else:
                            text "Виденное":
                                ysize 50
                                font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                                color "#ffffff"
                                size 24
                        imagebutton:
                            auto "mods/disco_sovenok/gui/settings/increase_%s.png"
                            action Preference("skip", "toggle")
                fixed:
                    ymaximum 50
                    text "Продолжать пропуск после выбора":
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#ffffff"
                        size 30
                        xalign 0.0
                        xoffset 20
                    imagebutton:
                        auto "mods/disco_sovenok/gui/settings/checkbox_%s.png"
                        xanchor 0.5
                        xpos 0.75
                        selected (preferences.skip_after_choices)
                        action SelectedIf(Preference('after choices', 'toggle'))
                fixed:
                    ymaximum 50
                    text "Автопереход":
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#ffffff"
                        size 30
                        xalign 0.0
                        xoffset 20
                    imagebutton:
                        auto "mods/disco_sovenok/gui/settings/checkbox_%s.png"
                        xanchor 0.5
                        xpos 0.75
                        selected (preferences.text_cps != 0)
                        action SelectedIf(Preference('auto-forward', 'toggle'))
                fixed:
                    ymaximum 50
                    text "Время автоперехода":
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#ffffff"
                        size 30
                        xalign 0.0
                        xoffset 20
                    showif preferences.afm_enable :
                        hbox:
                            ysize 50
                            xanchor 0.5
                            xpos 0.75
                            bar:
                                xmaximum 250
                                value Preference('auto-forward time')
                                base_bar "mods/disco_sovenok/gui/settings/bar_base.png"
                                thumb "mods/disco_sovenok/gui/settings/bar_thumb.png"
                fixed:
                    ymaximum 50
                    text "Cкорость показа текста":
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#ffffff"
                        size 30
                        xalign 0.0
                        xoffset 20
                    hbox:
                        ysize 50
                        xanchor 0.5
                        xpos 0.75
                        bar:
                            xmaximum 250
                            value Preference('text speed')
                            base_bar "mods/disco_sovenok/gui/settings/bar_base.png"
                            thumb "mods/disco_sovenok/gui/settings/bar_thumb.png"
                            thumb_offset 10
                null height 50
                fixed:
                    ymaximum 50
                    text "Громкость музыки":
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#ffffff"
                        size 30
                        xalign 0.0
                        xoffset 20
                    hbox:
                        ysize 50
                        xanchor 0.5
                        xpos 0.75
                        bar:
                            xmaximum 250
                            value Preference('music volume')
                            base_bar "mods/disco_sovenok/gui/settings/bar_base.png"
                            thumb "mods/disco_sovenok/gui/settings/bar_thumb.png"
                            thumb_offset 10
                fixed:
                    ymaximum 50
                    text "Громкость звуков":
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#ffffff"
                        size 30
                        xalign 0.0
                        xoffset 20
                    hbox:
                        ysize 50
                        xanchor 0.5
                        xpos 0.75
                        bar:
                            xmaximum 250
                            value Preference('sound volume')
                            base_bar "mods/disco_sovenok/gui/settings/bar_base.png"
                            thumb "mods/disco_sovenok/gui/settings/bar_thumb.png"
                            thumb_offset 10
                fixed:
                    ymaximum 50
                    text "Громкость эмбиента":
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#ffffff"
                        size 30
                        xalign 0.0
                        xoffset 20
                    hbox:
                        ysize 50
                        xanchor 0.5
                        xpos 0.75
                        bar:
                            xmaximum 250
                            value Preference('voice volume')
                            base_bar "mods/disco_sovenok/gui/settings/bar_base.png"
                            thumb "mods/disco_sovenok/gui/settings/bar_thumb.png"
                            thumb_offset 10
                null height 50
                fixed:
                    ymaximum 50
                    text "Заменять интерфейс при запуске":
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#ffffff"
                        size 30
                        xalign 0.0
                        xoffset 20
                    imagebutton:
                        auto "mods/disco_sovenok/gui/settings/checkbox_%s.png"
                        xanchor 0.5
                        xpos 0.75
                        selected persistent.ds_settings['replace_interface']
                        action SelectedIf(ToggleDict(persistent.ds_settings, 'replace_interface'))
                fixed:
                    ymaximum 50
                    text "Показывать другие сохранения":
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#ffffff"
                        size 30
                        xalign 0.0
                        xoffset 20
                    imagebutton:
                        auto "mods/disco_sovenok/gui/settings/checkbox_%s.png"
                        xanchor 0.5
                        xpos 0.75
                        selected persistent.ds_settings['show_other_saves']
                        action SelectedIf(ToggleDict(persistent.ds_settings, 'show_other_saves'))
                null height 50
                fixed:
                    ymaximum 50
                    text "Хентай-содержимое":
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#ffffff"
                        size 30
                        xalign 0.0
                        xoffset 20
                    imagebutton:
                        auto "mods/disco_sovenok/gui/settings/checkbox_%s.png"
                        xanchor 0.5
                        xpos 0.75
                        selected persistent.ds_settings['hentai']
                        action SelectedIf(ToggleDict(persistent.ds_settings, 'hentai'))
                fixed:
                    ymaximum 50
                    text "Нецензурная лексика":
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#ffffff"
                        size 30
                        xalign 0.0
                        xoffset 20
                    imagebutton:
                        auto "mods/disco_sovenok/gui/settings/checkbox_%s.png"
                        xanchor 0.5
                        xpos 0.75
                        selected persistent.ds_settings['obscene']
                        action SelectedIf(ToggleDict(persistent.ds_settings, 'obscene'))

screen ds_load():
    default cur_slot = (0, 0)
    frame:
        background "mods/disco_sovenok/gui/loadsave/loadsave_base.png"
        yfill True
        xalign 1.0
        xoffset -100
        xmaximum 1100
        at transform:
            on show:
                yoffset -1080
                linear 0.1 yoffset 0
            on hide:
                yoffset 0
                linear 0.1 yoffset -1080
        fixed:
            if cur_slot != (0, 0):
                add FileScreenshot(cur_slot[1], page=cur_slot[0]):
                    xalign 0.5
                    xysize (640, 360)
            add "mods/disco_sovenok/gui/loadsave/frame.png":
                xalign 0.5
                xysize (640, 360)
            xalign 0.5
            yalign 0.0
            yoffset 30
        fixed:
            yalign 0.0
            yoffset 400
            ymaximum 600
            vpgrid:
                cols 1
                rows len(renpy.list_saved_games())
                child_size (1080, None)
                mousewheel True
                yinitial 0.0
                scrollbars 'vertical'
                arrowkeys True
                pagekeys True
                spacing 10
                for slot in range(119, 11, -1):
                    if FileSaveName(slot % 12 + 1, page=(slot // 12)).upper().replace('\n', ' ') != '':
                        fixed:
                            xmaximum 1080
                            ymaximum 50
                            imagebutton:
                                xalign 0.5
                                yalign 0.0
                                auto "mods/disco_sovenok/gui/loadsave/entry_%s.png"
                                action [SetScreenVariable('cur_slot', (slot // 12, slot % 12 + 1))]
                            text FileSaveName(slot % 12 + 1, page=(slot // 12)).upper().replace('\n', ' '):
                                font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                                color "#000000"
                                xmaximum 900
                                size 30
                                xalign 0.0
                                xoffset 10
                                yalign 0.5
                            text FileTime(slot % 12 + 1, page=(slot // 12), format='%d.%m.%y %H:%M'):
                                font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                                size 24
                                xalign 1.0
                                xoffset -10
                                yalign 0.5
                                color "#000000"
        hbox:
            xalign 0.5
            yalign 1.0
            yoffset -10
            imagebutton:
                auto "mods/disco_sovenok/gui/loadsave/delete_%s.png"
                action [FileDelete(cur_slot[1], page=cur_slot[0]), SetScreenVariable('cur_slot', (0,0))]
            imagebutton:
                auto "mods/disco_sovenok/gui/loadsave/load_%s.png"
                action FileLoad(cur_slot[1], page=cur_slot[0])

screen ds_save():
    default cur_slot = (0, 0)
    default empty_slot = (10, 0)
    python:
        for slot in range(119, 11, -1):
            if FileSaveName(slot % 12 + 1, page=(slot // 12)).upper().replace('\n', ' ') == '':
                empty_slot = (slot // 12, slot % 12 + 1)
            else:
                break
    frame:
        background "mods/disco_sovenok/gui/loadsave/loadsave_base.png"
        yfill True
        xalign 1.0
        xoffset -100
        xmaximum 1100
        at transform:
            on show:
                yoffset -1080
                linear 0.1 yoffset 0
            on hide:
                yoffset 0
                linear 0.1 yoffset -1080
        fixed:
            if cur_slot != (0, 0):
                add FileScreenshot(cur_slot[1], page=cur_slot[0]):
                    xalign 0.5
                    xysize (640, 360)
            add "mods/disco_sovenok/gui/loadsave/frame.png":
                xalign 0.5
                xysize (640, 360)
            xalign 0.5
            yalign 0.0
            yoffset 30
        fixed:
            yalign 0.0
            yoffset 400
            ymaximum 600
            vpgrid:
                cols 1
                child_size (1080, None)
                mousewheel True
                yinitial 0.0
                scrollbars 'vertical'
                arrowkeys True
                pagekeys True
                spacing 10
                if empty_slot[0] < 10:
                    rows int(len(renpy.list_saved_games()) + 1)
                    fixed:
                        xmaximum 1080
                        ymaximum 50
                        imagebutton:
                            xalign 0.5
                            yalign 0.0
                            auto "mods/disco_sovenok/gui/loadsave/newentry_%s.png"
                            action FileSave(empty_slot[1], page=empty_slot[0])
                else:
                    rows len(renpy.list_saved_games())
                for slot in range(119, 11, -1):
                    if FileSaveName(slot % 12 + 1, page=(slot // 12)).upper().replace('\n', ' ') != '':
                        fixed:
                            xmaximum 1080
                            ymaximum 50
                            imagebutton:
                                xalign 0.5
                                yalign 0.0
                                auto "mods/disco_sovenok/gui/loadsave/entry_%s.png"
                                action [SetScreenVariable('cur_slot', (slot // 12, slot % 12 + 1))]
                            text FileSaveName(slot % 12 + 1, page=(slot // 12)).upper().replace('\n', ' '):
                                font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                                color "#000000"
                                xmaximum 900
                                size 30
                                xalign 0.0
                                xoffset 10
                                yalign 0.5
                            text FileTime(slot % 12 + 1, page=(slot // 12), format='%d.%m.%y %H:%M'):
                                font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                                size 24
                                xalign 1.0
                                xoffset -10
                                yalign 0.5
                                color "#000000"
        hbox:
            xalign 0.5
            yalign 1.0
            yoffset -10
            imagebutton:
                auto "mods/disco_sovenok/gui/loadsave/delete_%s.png"
                action [FileDelete(cur_slot[1], page=cur_slot[0]), SetScreenVariable('cur_slot', (0,0))]
            imagebutton:
                auto "mods/disco_sovenok/gui/loadsave/save_%s.png"
                action Confirm(u"Вы действительно хотите перезаписать это сохранение?", FileSave(cur_slot[1], page=cur_slot[0]), confirm_selected=True)

screen ds_gallery():
    default gallery_table = {'bg': ds_bg_list, 'cg': ds_cg_list}
    default gallery_mode = 'bg'
    frame:
        background "mods/disco_sovenok/gui/gallery/gallery_base.png"
        yfill True
        xalign 1.0
        xoffset -200
        xmaximum 1000
        at transform:
            on show:
                yoffset -1080
                linear 0.1 yoffset 0
            on hide:
                yoffset 0
                linear 0.1 yoffset -1080
        hbox:
            xalign 0.5
            yalign 0.0
            yoffset 20
            xoffset 100
            showif gallery_mode == 'bg':
                add "mods/disco_sovenok/gui/gallery/bg_selected.png"
                label "|":
                    text_font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                    text_size 36
                    text_color "#ffffff"
                imagebutton:
                    auto "mods/disco_sovenok/gui/gallery/cg_%s.png"
                    action SetScreenVariable('gallery_mode', 'cg')
            else:
                imagebutton:
                    auto "mods/disco_sovenok/gui/gallery/bg_%s.png"
                    action SetScreenVariable('gallery_mode', 'bg')
                label "|":
                    text_font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                    text_size 36
                    text_color "#ffffff"
                add "mods/disco_sovenok/gui/gallery/cg_selected.png"
        fixed:
            yalign 1.0
            ymaximum 980
            vpgrid:
                cols 3
                rows int(len(gallery_table[gallery_mode]) // 3 + 1)
                child_size (1000, None)
                mousewheel True
                yinitial 0.0
                xoffset 100
                scrollbars 'vertical'
                arrowkeys True
                pagekeys True
                spacing 10
                for i in range(0, (len(gallery_table[gallery_mode]) // 3 + 1) * 3):
                    fixed:
                        xmaximum 300
                        ymaximum 170
                        if i < len(gallery_table[gallery_mode]):
                            if gallery_table[gallery_mode][i].is_seen():
                                add gallery_table[gallery_mode][i].get_full_name():
                                    xalign 0.5
                                    yalign 0.0
                                    zoom 0.15625
                                    crop (0, 0, 1920, 1080)
                                imagebutton:
                                    auto "mods/disco_sovenok/gui/gallery/frame_%s.png"
                                    xalign 0.5
                                    yalign 0.0
                                    action Function(renpy.call_in_new_context, 'ds_gallery_show_images', imglist=gallery_table[gallery_mode][i].get_all_img())
                            else:
                                add "mods/disco_sovenok/gui/gallery/locked.png":
                                    xalign 0.5
                                    yalign 0.0
                                imagebutton:
                                    auto "mods/disco_sovenok/gui/gallery/frame_%s.png"
                                    xalign 0.5
                                    yalign 0.0
                                    action NullAction()

label ds_gallery_show_images(imglist=[]):
    python:
        for img in imglist:
            renpy.show(img)
            renpy.with_statement(fade)
            renpy.pause()
            renpy.hide(img)
    return

screen ds_achievements():
    python:
        ACHIEVEMENTS = {
            'gen': ['preterm', 'bus_crash', 'beat_girls', 'know_history', 'had_sex', 'us_gone', 'mi_rape', 'arstotzka', 'electrocution'],
            'dv': [],
            'un': [],
            'sl': [],
            'us': ['us_escape'],
            'mi': [],
            'mt': [],
            'el': [],
            'mz': [],
            'yn': [],
            'cs': [],
            'oth': []
        }
        ACH_CLASSES = ['gen', 'dv', 'un', 'sl', 'us', 'mi', 'mt', 'el', 'mz', 'yn', 'cs', 'oth']
    default cur_class = None
    frame:
        background "mods/disco_sovenok/gui/gallery/gallery_base.png"
        yfill True
        xalign 1.0
        xoffset -200
        xmaximum 1000
        at transform:
            on show:
                yoffset -1080
                linear 0.1 yoffset 0
            on hide:
                yoffset 0
                linear 0.1 yoffset -1080
        vbox:
            xalign 0.0
            xoffset 10
            for cl in ACH_CLASSES:
                imagebutton:
                    auto "mods/disco_sovenok/gui/ach/"+cl+"_%s.png"
                    xalign 0.0
                    action SelectedIf(SetScreenVariable('cur_class', cl))
        if cur_class != None:
            vbox:
                xalign 1.0
                for ach in ACHIEVEMENTS[cur_class]:
                    if persistent.ds_achievements[ach]:
                        add "mods/disco_sovenok/gui/ach/"+cur_class+"/"+ach+".png":
                            xalign 1.0
                            xoffset -100
                    else:
                        add "mods/disco_sovenok/gui/ach/locked.png":
                            xalign 1.0
                            xoffset -100
        imagebutton:
            auto "mods/disco_sovenok/gui/ach/reset_%s.png"
            xalign 1.0
            yalign 1.0
            xoffset -10
            action Confirm("Вы уверены, что хотите сбросить достижения?", Function(ds_reset_achievements), confirm_selected=True)

    
screen ds_choose_type():
    python:
        from time import localtime, strftime
        t = strftime("%H:%M:%S", localtime())
        hour, minute, sec = t.split(":")
        hour = int(hour)
    tag menu
    modal True
    if hour in [22,23,24,0,1,2,3,4,5,6]:
        add "bg ext_road_night":
            xalign 0.5
            yalign 0.5
    elif hour in [20,21,7,8]:
        add "bg ext_road_sunset":
            xalign 0.5
            yalign 0.5
    else:
        add "bg ext_road_day":
            xalign 0.5
            yalign 0.5
    add "mods/disco_sovenok/gui/menu/type_title.png":
        xalign 0.0
        yalign 0.0
        xoffset 15
    hbox:
        xalign 0.5
        yalign 1.0
        spacing 20
        imagebutton:
            auto "mods/disco_sovenok/gui/menu/int_type_%s.png"
            yanchor 1.0
            at transform:
                ypos 2.0
                linear 0.2 ypos 1.0
            action [SetVariable("ds_archetype", 1), Start("ds_start")]
            activate_sound ds_selection
                
        imagebutton:
            auto "mods/disco_sovenok/gui/menu/psy_type_%s.png"
            yanchor 1.0
            at transform:
                ypos 0.0
                linear 0.2 ypos 1.0
            action [SetVariable("ds_archetype", 2), Start("ds_start")]
            activate_sound ds_selection
            
        imagebutton:
            auto "mods/disco_sovenok/gui/menu/fys_type_%s.png"
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
            action [SetVariable("ds_archetype", 0), Function(ds_init_custom), Show('ds_skills', setup=True), Hide('ds_choose_type')]
            activate_sound ds_selection
    
screen ds_skills(setup=False):
    python:
        SKILLS = [
            'logic', 'encyclopedia', 'rhetoric', 'drama', 'conceptualization', 'visual_calculus',
            'volition', 'inland_empire', 'authority', 'empathy', 'esprit', 'suggestion',
            'endurance', 'pain_threshold', 'physical_instrument', 'instinct', 'shivers', 'half_light',
            'perception', 'coordination', 'reaction_speed', 'savoir_faire', 'interfacing', 'composure'
        ]
    default chosen_skill = None
    modal True
    tag menu
    if setup:
        if hour in [22,23,24,0,1,2,3,4,5,6]:
            add "bg ext_road_night":
                xalign 0.5
                yalign 0.5
        elif hour in [20,21,7,8]:
            add "bg ext_road_sunset":
                xalign 0.5
                yalign 0.5
        else:
            add "bg ext_road_day":
                xalign 0.5
                yalign 0.5
    imagebutton:
        xalign 0.0
        xoffset 20
        yalign 1.0
        yoffset -20
        auto "mods/disco_sovenok/gui/skills/back_%s.png"
        if setup:
            action [Show("ds_choose_type"), Hide("ds_skills")]
        else:
            action Return()
    if setup:
        imagebutton:
            xalign 1.0
            xoffset -20
            yalign 1.0
            yoffset -20
            auto "mods/disco_sovenok/gui/skills/confirm_%s.png"
            action Start('ds_start')
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
    use ds_skill_table
    if chosen_skill != None:
        use ds_skill_info:
            fixed:
                ymaximum 390
                if setup:
                    vbox:
                        xalign 1.0
                        yalign 0.0
                        showif (ds_skill_list[chosen_skill].level + ds_available_points >= 1) or (ds_skill_list[chosen_skill].level == 1):
                            imagebutton:
                                auto "mods/disco_sovenok/gui/skills/terrible_%s.png"
                                selected If(ds_skill_list[chosen_skill].level == 1)
                                action [SetVariable('ds_available_points', ds_available_points + (ds_skill_list[chosen_skill].level - 1)), SensitiveIf(Function(ds_skill_list[skill].set_level, 1))]
                                activate_sound ds_selection
                        showif (ds_skill_list[chosen_skill].level + ds_available_points >= 2) or (ds_skill_list[chosen_skill].level == 2):
                            imagebutton:
                                auto "mods/disco_sovenok/gui/skills/bad_%s.png"
                                selected If(ds_skill_list[chosen_skill].level == 2)
                                action [SetVariable('ds_available_points', ds_available_points + (ds_skill_list[chosen_skill].level - 2)), SensitiveIf(Function(ds_skill_list[skill].set_level, 2))]
                                activate_sound ds_selection
                        showif (ds_skill_list[chosen_skill].level + ds_available_points >= 3) or (ds_skill_list[chosen_skill].level == 3):
                            imagebutton:
                                auto "mods/disco_sovenok/gui/skills/medium_%s.png"
                                selected If(ds_skill_list[chosen_skill].level == 3)
                                action [SetVariable('ds_available_points', ds_available_points + (ds_skill_list[chosen_skill].level - 3)), SensitiveIf(Function(ds_skill_list[skill].set_level, 3))]
                                activate_sound ds_selection
                        showif (ds_skill_list[chosen_skill].level + ds_available_points >= 4) or (ds_skill_list[chosen_skill].level == 4):
                            imagebutton:
                                auto "mods/disco_sovenok/gui/skills/good_%s.png"
                                selected If(ds_skill_list[chosen_skill].level == 4)
                                action [SetVariable('ds_available_points', ds_available_points + (ds_skill_list[chosen_skill].level - 4)), SensitiveIf(Function(ds_skill_list[skill].set_level, 4))]
                                activate_sound ds_selection
                        showif (ds_skill_list[chosen_skill].level + ds_available_points >= 5) or (ds_skill_list[chosen_skill].level == 5):
                            imagebutton:
                                auto "mods/disco_sovenok/gui/skills/excellent_%s.png"
                                selected If(ds_skill_list[chosen_skill].level == 5)
                                action [SetVariable('ds_available_points', ds_available_points + (ds_skill_list[chosen_skill].level - 5)), SensitiveIf(Function(ds_skill_list[skill].set_level, 5))]
                                activate_sound ds_selection
                        showif (ds_skill_list[chosen_skill].level + ds_available_points >= 6) or (ds_skill_list[chosen_skill].level == 6):
                            imagebutton:
                                auto "mods/disco_sovenok/gui/skills/genius_%s.png"
                                selected If(ds_skill_list[chosen_skill].level == 6)
                                action [SetVariable('ds_available_points', ds_available_points + (ds_skill_list[chosen_skill].level - 6)), SensitiveIf(Function(ds_skill_list[skill].set_level, 6))]
                                activate_sound ds_selection
                else:
                    grid 2 5:
                        xalign 1.0
                        yalign 0.0
                        xoffset 10
                        yoffset 10
                        text "Базовый уровень: " font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        text str(ds_skill_list[chosen_skill].level) font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        text "Бонус от типа: " font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        text str(ds_skill_list[chosen_skill].get_type_bonus()) font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        text "Бонус от кружка: " font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        text str(ds_skill_list[chosen_skill].get_member_bonus()) font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        text "Урон: " font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        text str(ds_skill_list[chosen_skill].get_damage_bonus()) font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        text "Всего:" font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        text str(ds_skill_list[chosen_skill].get_total()) font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                    vbox:
                        xalign 0.5
                        yalign 1.0
                        text "ДО СЛЕДУЮЩЕГО УРОВНЯ" font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc":
                            xalign 0.0
                            xoffset 10
                        text str(ds_skill_list[chosen_skill].xp) + "/100" font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc":
                            xalign 1.0
                            xoffset -10

screen ds_skill_table:
    python:
        SKILLS = [
            'logic', 'encyclopedia', 'rhetoric', 'drama', 'conceptualization', 'visual_calculus',
            'volition', 'inland_empire', 'authority', 'empathy', 'esprit', 'suggestion',
            'endurance', 'pain_threshold', 'physical_instrument', 'instinct', 'shivers', 'half_light',
            'perception', 'coordination', 'reaction_speed', 'savoir_faire', 'interfacing', 'composure'
        ]
    default chosen_skill = None
    frame:
        background "mods/disco_sovenok/gui/skills/attr_lines.png"
        yalign 0.0
        at transform:
            on show:
                xanchor 1.0
                xpos 0.0
                linear 0.1 xanchor 0.0 xpos 0.0
            on hide:
                xanchor 0.0
                xpos 0.0
                linear 0.1 xanchor 1.0 xpos 0.0
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
                        add "mods/disco_sovenok/gui/skills/[skill]_large.png":
                            xalign 0.5
                            yalign 0.0
                            xysize (173, 240)
                        text str(ds_skill_list[skill].get_total()):
                            xalign 1.0
                            yalign 0.0
                            xoffset -10
                            yoffset 5
                            size 48
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        text ds_skill_list[skill].name.upper():
                            xalign 0.5
                            yalign 1.0
                            yoffset -5
                            size 18
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        imagebutton:
                            xoffset 2
                            auto "mods/disco_sovenok/gui/skills/skill_%s.png"
                            selected If(chosen_skill == skill)
                            action SetScreenVariable('chosen_skill', skill)
                            activate_sound ds_btn_click

screen ds_call_hud():
    modal False
    add "mods/disco_sovenok/gui/hud/call_hud.png":
        xalign 0.0
        yalign 0.0
    mousearea:
        area (0, 0, 21, 33)
        hovered [Show('ds_hud'), Hide('ds_call_hud')]
        unhovered [NullAction()]

screen ds_hud():
    modal False
    add "mods/disco_sovenok/gui/hud/hud.png" xalign 0.0 yalign 0.0
    mousearea:
        area (0, 0, 500, 70)
        hovered Show('ds_hud')
        unhovered [Show('ds_call_hud'), Hide('ds_hud')]
    hbox:
        xalign 0.0
        yalign 0.0
        imagebutton:
            yalign 0.0
            auto "mods/disco_sovenok/gui/hud/menu_%s.png"
            action ShowMenu('ds_game_menu_selector')
        imagebutton:
            yalign 0.0
            auto "mods/disco_sovenok/gui/hud/skills_%s.png"
            action ShowMenu('ds_skills')
        imagebutton:
            yalign 0.0
            auto "mods/disco_sovenok/gui/hud/lp_%s.png"
            action ShowMenu('ds_lp_points')
        grid 2 4:
            transpose True
            yalign 0.0
            xspacing 10
            fixed:
                xmaximum 120
                ymaximum 15
                text "ЗДОРОВЬЕ":
                    font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                    size 12
                    xalign 0.0
                text str(ds_health.level())+"/"+str(ds_health.level() - ds_health.diff()):
                    font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                    size 12
                    xalign 1.0
            fixed:
                xmaximum 120
                ymaximum 15
                bar:
                    left_bar "mods/disco_sovenok/gui/hud/bar_health.png"
                    right_bar "mods/disco_sovenok/gui/hud/bar_empty.png"
                    bar_resizing False
                    thumb None
                    value ds_health.level()
                    range ds_skill_list['endurance'].get_total()
            fixed:
                xmaximum 120
                ymaximum 15
                text "БОЕВОЙ ДУХ":
                    font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                    size 12
                    xalign 0.0
                text str(ds_morale.level())+"/"+str(ds_morale.level() - ds_morale.diff()):
                    font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                    size 12
                    xalign 1.0
            fixed:
                xmaximum 120
                ymaximum 15
                bar:
                    left_bar "mods/disco_sovenok/gui/hud/bar_morale.png"
                    right_bar "mods/disco_sovenok/gui/hud/bar_empty.png"
                    bar_resizing False
                    thumb None
                    value ds_morale.level()
                    range ds_skill_list['volition'].get_total()
            fixed:
                xmaximum 120
                ymaximum 15
                text "РЕПУТАЦИЯ":
                    font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                    size 12
                    xalign 0.0
                text str(ds_karma):
                    font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                    size 12
                    xalign 1.0
            fixed:
                xmaximum 120
                ymaximum 15
                bar:
                    base_bar "mods/disco_sovenok/gui/hud/bar_karma.png"
                    thumb "mods/disco_sovenok/gui/hud/bar_thumb.png"
                    value max(ds_karma+50, 0)
                    range 100
            fixed:
                xmaximum 120
                ymaximum 15
                text "ОМЕГА/АЛЬФА":
                    font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                    size 12
                    xalign 0.0
                text str(ds_semtype):
                    font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                    size 12
                    xalign 1.0
            fixed:
                xmaximum 120
                ymaximum 15
                bar:
                    base_bar "mods/disco_sovenok/gui/hud/bar_type.png"
                    thumb "mods/disco_sovenok/gui/hud/bar_thumb.png"
                    value max(ds_semtype+6, 0)
                    range 12
                
screen ds_skill_info:
    fixed:
        xmaximum 690
        ymaximum 980
        xalign 1.0
        xoffset -20
        add "mods/disco_sovenok/gui/skills/skill_info.png"
        at transform:
            on show:
                yoffset -1080
                linear 0.1 yoffset 0
            on hide:
                yoffset 0
                linear 0.1 yoffset -1080
        vbox:
            hbox:
                xalign 0.0
                xoffset 10
                add "mods/disco_sovenok/gui/skills/[chosen_skill]_large.png" xalign 0.0 yalign 0.0 xoffset 5 yoffset 10
                transclude
            text ds_skill_list[chosen_skill].name.upper():
                xalign 0.5
                xoffset 10
                yoffset 10
                size 48
                font "0@mods/disco_sovenok/gui/fonts/Baskerville.ttc"
            text ds_skill_list[chosen_skill].descr:
                yalign 1.0
                yoffset 10
                xoffset 10
                size 24
                xfill True
                font "0@mods/disco_sovenok/gui/fonts/Baskerville.ttc"
    
screen ds_lp_points():
    python:
        CHARS = ['dv', 'un', 'sl', 'us', 'mi', 'yn', 'el', 'mt', 'mz', 'cs']

        CHAR_COLORS = {
            'dv': "#ffaa00",
            'un': "#b956ff",
            'sl': "#ffd200",
            'us': "#ff3200",
            'mi': "#00deff",
            'yn': "#74b05f",
            'el': "#ffff00",
            'mt': "#00ea32",
            'mz': "#5481db",
            'cs': "#a5a5ff"
        }

        CHAR_NAMES = {
            'dv': "АЛИСА",
            'un': "ЛЕНА",
            'sl': "СЛАВЯ",
            'us': "УЛЬЯНА",
            'mi': "МИКУ",
            'yn': "ЯНА",
            'el': "ЭЛЕКТРОНИК",
            'mt': "ОЛЬГА",
            'mz': "ЖЕНЯ",
            'cs': "ВИОЛА"
        }
    fixed:
        xmaximum 1810
        ymaximum 975
        add "mods/disco_sovenok/gui/lp/lp_base.png"
        yalign 0.0
        at transform:
            on show:
                xanchor 0.0
                xpos 1.0
                linear 0.1 xanchor 1.0 xpos 1.0
            on hide:
                xanchor 1.0
                xpos 1.0
                linear 0.1 xanchor 0.0 xpos 1.0
        grid 2 5:
            xspacing 30
            xoffset 34
            transpose True
            for char in CHARS:
                fixed:
                    xmaximum 855
                    xminimum 855
                    ymaximum 175
                    yminimum 175
                    hbox:
                        xalign 0.0
                        if ds_met[char] > 0:
                            if ds_lp[char] > 0:
                                add "mods/disco_sovenok/gui/lp/"+char+"_portrait_pos.png" yalign 0.5
                            elif ds_lp[char] < 0:
                                add "mods/disco_sovenok/gui/lp/"+char+"_portrait_neg.png" yalign 0.5
                            else:
                                add "mods/disco_sovenok/gui/lp/"+char+"_portrait.png" yalign 0.5
                        else:
                            add "mods/disco_sovenok/gui/lp/unknown.png" yalign 0.5
                        if ds_met[char] == 0:
                            text "ИМЯ НЕИЗВЕСТНО":
                                size 56
                                font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                                yalign 0.5
                                xoffset 25
                        elif ds_met[char] == 1:
                            text "ИМЯ НЕИЗВЕСТНО":
                                size 56
                                font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                                color CHAR_COLORS[char]
                                yalign 0.5
                                xoffset 25
                        else:
                            text CHAR_NAMES[char]:
                                size 56
                                font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                                color CHAR_COLORS[char]
                                yalign 0.5
                                xoffset 25
                    text (("– " if ds_lp[char] < 0 else "0 ")+str(ds_abs(ds_lp[char]) // 10)+" "+str(ds_abs(ds_lp[char]) % 10)):
                        size 90
                        xalign 1.0
                        yalign 0.5
                        xoffset -15
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#000000"
    imagebutton:
        xalign 0.0
        xoffset 20
        yalign 1.0
        yoffset -20
        auto "mods/disco_sovenok/gui/skills/back_%s.png"
        action Return()

screen ds_say:
    on "show" action Hide('ds_check_result')
    on "hide" action Hide('ds_check_result') 
    window:
        background None
        id "window"           
        add ("mods/disco_sovenok/gui/say/dialogue_box.png"):
            xalign 0.5
            yalign 1.0 
        imagebutton:
            auto ("mods/disco_sovenok/gui/say/backward_%s.png") 
            xalign 0.0
            yalign 1.0
            xoffset 20
            yoffset -50
            action ShowMenu("text_history")         
        imagebutton:
            auto ("mods/disco_sovenok/gui/say/hide_%s.png")
            xalign 0.0
            yalign 1.0
            xoffset 20
            yoffset -200
            action HideInterface()
        imagebutton:
            auto ("mods/disco_sovenok/gui/say/forward_%s.png")
            xalign 1.0
            yalign 1.0
            xoffset -20
            yoffset -50
            action Skip()
        text what:
            id "what"
            xalign 0.0
            yalign 0.0
            xoffset 170
            yoffset 900
            xmaximum 1580
            drop_shadow [ (-1, -1), (1, -1), (-1, 1), (1, 1) ]
            drop_shadow_color "#000001"
            font "0@mods/disco_sovenok/gui/fonts/Baskerville.ttc"
            line_spacing 2
            if persistent.font_size == 'small':
                size 24
            else:
                size 30
            if persistent.timeofday == 'prologue':
                color "#afdafc"
            else:
                color "#ffdd7d"
        if 'result}' in what:
            mousearea:
                area (170, 900, 1580, 280)
                hovered Show('ds_check_result')
                unhovered Hide('ds_check_result')
        if who:
            text who.upper():
                id "who"
                xalign 0.0
                yalign 1.0
                xoffset 170
                yoffset -190
                size 35
                drop_shadow [ (-1, -1), (1, -1), (-1, 1), (1, 1) ]
                drop_shadow_color "#000"
                font "0@mods/disco_sovenok/gui/fonts/Baskerville.ttc"
                line_spacing 2

screen ds_text_history_screen:
    window:
        background None
        at transform:
            on show:
                xoffset 1920
                linear 0.2 xoffset -35
                linear 0.1 xoffset 0
            on hide:
                xoffset -115
                linear 0.1 xoffset 1920
        yfill True
        frame:
            xalign 1.0
            xoffset -115
            background "mods/disco_sovenok/gui/history/text_history.png"
            xmaximum 500
            viewport:
                child_size (500, None)
                mousewheel True
                yinitial 1.0
                scrollbars 'vertical'
                arrowkeys True
                pagekeys True
                vbox:
                    xmaximum 450
                    yalign 1.0
                    xalign 0.0
                    xoffset 10
                    for entry in _history_list:
                        if entry.who is not None:
                            textbutton ("{color="+Color(color=entry.who_args['color']).hexcode+"}"+entry.who.upper()+"{/color} — "+entry.what):
                                background None
                                action RollbackToIdentifier(entry.rollback_identifier)
                                if persistent.font_size == 'small':
                                    text_size 24
                                else:
                                    text_size 30
                                if persistent.timeofday == 'prologue':
                                    text_style 'ds_history_style_ch_prolog'
                                else:
                                    text_style 'ds_history_style_ch'
                        else:
                            textbutton entry.what:
                                background None
                                action RollbackToIdentifier(entry.rollback_identifier)
                                if persistent.font_size == 'small':
                                    text_size 24
                                else:
                                    text_size 30
                                if persistent.timeofday == 'prologue':
                                    text_style 'ds_history_style_noch_prolog'
                                else:
                                    text_style 'ds_history_style_noch'
                        null height 20
                    null height 200

screen ds_nvl:
    window:
        background None
        at transform:
            on show:
                xoffset 1920
                linear 0.2 xoffset -35
                linear 0.1 xoffset 0
            on hide:
                xoffset -115
                linear 0.1 xoffset 1920
        yfill True
        frame:
            xalign 1.0
            xoffset -115
            background "mods/disco_sovenok/gui/history/text_history.png"
            xmaximum 500
            viewport:
                child_size (500, None)
                mousewheel True
                yinitial 1.0
                scrollbars 'vertical'
                arrowkeys True
                pagekeys True
                vbox:
                    xmaximum 450
                    yalign 1.0
                    xalign 0.0
                    xoffset 10
                    for who, what, who_id, what_id, window_id in dialogue:
                        window:
                            id window_id
                            vbox:
                                if who is not None:
                                    hbox:
                                        text who:
                                            id who_id
                                            if persistent.font_size == 'small':
                                                size 24
                                            else:
                                                size 30
                                            if persistent.timeofday == 'prologue':
                                                style 'ds_history_style_ch_prolog'
                                            else:
                                                style 'ds_history_style_ch'
                                        text " — ":
                                            if persistent.font_size == 'small':
                                                size 24
                                            else:
                                                size 30
                                            if persistent.timeofday == 'prologue':
                                                style 'ds_history_style_ch_prolog'
                                            else:
                                                style 'ds_history_style_ch'
                                text what:
                                    id what_id
                                    if persistent.font_size == 'small':
                                        size 24
                                    else:
                                        size 30
                                    if persistent.timeofday == 'prologue':
                                        style 'ds_history_style_noch_prolog'
                                    else:
                                        style 'ds_history_style_noch'
                        null height 20
                    if items:
                        null height 50
                        for i in range(0, len(items)):
                            if items[i][1]:
                                button:
                                    background None
                                    action items[i][1]
                                    text str(i + 1) + ". " + items[i][0]:
                                        idle_color "#ffffff"
                                        hover_color "#86cd4d"
                                        font "0@mods/disco_sovenok/gui/fonts/Baskerville.ttc"
                                        if persistent.font_size == 'small':
                                            size 24
                                        else:
                                            size 30
                                    if i < 9:
                                        keysym str(i + 1)
                    null height 200

screen ds_choice(items):
    on 'hide' action Hide('ds_check_info')
    window:
        background None
        at transform:
            on show:
                xoffset 1920
                linear 0.2 xoffset -35
                linear 0.1 xoffset 0
            on hide:
                xoffset -115
                linear 0.1 xoffset 1920
        yfill True
        frame:
            xalign 1.0
            xoffset -115
            background "mods/disco_sovenok/gui/history/text_history.png"
            xmaximum 500
            viewport:
                child_size (500, None)
                mousewheel True
                yinitial 1.0
                scrollbars 'vertical'
                arrowkeys True
                pagekeys True
                vbox:
                    xmaximum 450
                    yalign 1.0
                    xalign 0.0
                    xoffset 10
                    for entry in _history_list:
                        if entry.who is not None:
                            textbutton ("{color="+Color(color=entry.who_args['color']).hexcode+"}"+entry.who.upper()+"{/color} — "+entry.what):
                                background None
                                action NullAction()
                                if persistent.font_size == 'small':
                                    text_size 24
                                else:
                                    text_size 30
                                if persistent.timeofday == 'prologue':
                                    text_style 'ds_history_style_ch_prolog'
                                else:
                                    text_style 'ds_history_style_ch'
                        else:
                            textbutton entry.what:
                                background None
                                action NullAction()
                                if persistent.font_size == 'small':
                                    text_size 24
                                else:
                                    text_size 30
                                if persistent.timeofday == 'prologue':
                                    text_style 'ds_history_style_noch_prolog'
                                else:
                                    text_style 'ds_history_style_noch'
                        null height 20
                    null height 50
                    for i in range(0, len(items)):
                        python:
                            skill = None
                            level = None
                            if 'skill' in items[i].kwargs:
                                skill = items[i].kwargs['skill']
                                level = items[i].kwargs['level']
                            modifiers = []
                            if 'modifiers' in items[i].kwargs:
                                modifiers = items[i].kwargs['modifiers']
                        if items[i].action:
                            button:
                                background None
                                if skill is None:
                                    action items[i].action
                                    text str(i + 1) + ". " + items[i][0]:
                                        idle_color "#ffffff"
                                        hover_color "#86cd4d"
                                        font "0@mods/disco_sovenok/gui/fonts/Baskerville.ttc"
                                        if persistent.font_size == 'small':
                                            size 24
                                        else:
                                            size 30
                                    if i < 9:
                                        keysym str(i + 1)
                                else:
                                    action [Function(ds_skill_list[skill].check, threshold=level, modifiers=modifiers), items[i].action]
                                    hovered Show('ds_check_info', skill=skill, threshold=level, modifiers=modifiers)
                                    unhovered Hide('ds_check_info')
                                    text str(i + 1) + ". " + "{check="+items[i].kwargs['skill']+":"+str(items[i].kwargs['level'])+"}"+items[i][0]:
                                        idle_color "#ffffff"
                                        hover_color "#86cd4d"
                                        font "0@mods/disco_sovenok/gui/fonts/Baskerville.ttc"
                                        if persistent.font_size == 'small':
                                            size 24
                                        else:
                                            size 30
                                    if i < 9:
                                        keysym str(i + 1)
                    null height 200


screen ds_guitar_game():
    imagemap:
        ground "mods/disco_sovenok/gui/guitar/guitar.jpg"
        idle "mods/disco_sovenok/gui/guitar/guitar.jpg"
        hover "mods/disco_sovenok/gui/guitar/guitar.jpg"
        hotspot (62, 325, 53, 67) action Call('ds_check_sound', 1) keysym '1'
        hotspot (120, 325, 47, 68) action Call('ds_check_sound', 2) keysym '2'
        hotspot (173, 323, 43, 70) action Call('ds_check_sound', 3) keysym '3'
        hotspot (222, 323, 42, 72) action Call('ds_check_sound', 4) keysym '4'
        hotspot (268, 322, 40, 73) action Call('ds_check_sound', 5) keysym '5'
        hotspot (313, 322, 36, 75) action Call('ds_check_sound', 6) keysym '6'
        hotspot (355, 321, 34, 77) action Call('ds_check_sound', 7) keysym '7'
        hotspot (395, 320, 32, 78) action Call('ds_check_sound', 8) keysym '8'
        hotspot (432, 319, 30, 80) action Call('ds_check_sound', 9) keysym '9'
        hotspot (467, 318, 28, 81) action Call('ds_check_sound', 10) keysym '0'
        hotspot (500, 318, 26, 82) action Call('ds_check_sound', 11) keysym 'q'
        hotspot (531, 318, 26, 82) action Call('ds_check_sound', 12) keysym 'w'
        hotspot (562, 317, 23, 83) action Call('ds_check_sound', 13) keysym 'e'
        hotspot (590, 317, 21, 84) action Call('ds_check_sound', 14) keysym 'r'
        hotspot (616, 316, 21, 85) action Call('ds_check_sound', 15) keysym 't'
        hotspot (642, 315, 19, 86) action Call('ds_check_sound', 16) keysym 'y'
        hotspot (665, 315, 18, 87) action Call('ds_check_sound', 17) keysym 'u'
        hotspot (688, 315, 16, 87) action Call('ds_check_sound', 18) keysym 'i'
        hotspot (708, 314, 16, 88) action Call('ds_check_sound', 19) keysym 'o'
        hotspot (729, 314, 14, 89) action Call('ds_check_sound', 20) keysym 'p'
        hotspot (747, 314, 13, 91) action Call('ds_check_sound', 21) keysym '['
        hotspot (765, 314, 13, 91) action Call('ds_check_sound', 22) keysym ']'
        hotspot (823, 305, 189, 105) action Call('ds_check_sound', 0) keysym 'K_SPACE'

screen ds_check_result():
    frame:
        background "mods/disco_sovenok/gui/check/check_base.png"
        xmaximum 600
        ymaximum 390
        yalign 0.0
        yoffset 20
        xalign 1.0
        at transform:
            on show:
                xoffset 600
                linear 0.2 xoffset -20
            on hide:
                xoffset -20
                linear 0.2 xoffset 600
        add ("mods/disco_sovenok/gui/skills/%s_large.png" % ds_last_skillcheck.skill):
            xalign 0.0
            yalign 0.5
            xoffset -5
        vbox:
            xalign 1.0
            yalign 0.0
            xoffset 5
            yoffset -5
            add ("mods/disco_sovenok/gui/check/%s_caption.png" % ds_last_skillcheck.skill)
            fixed:
                xmaximum 310
                ymaximum 30
                text "Уровень:":
                    font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                    color "#ffffff"
                    size 24
                    xalign 0.0
                text str(ds_last_skillcheck.level):
                    font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                    color "#ffffff"
                    size 24
                    xalign 1.0
            fixed:
                xmaximum 320
                ymaximum 30 

                text "Кубики:":
                    font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                    color "#ffffff"
                    size 24
                    xalign 0.0
                text str(ds_last_skillcheck.dices[0]) + "+" + str(ds_last_skillcheck.dices[1]) + "=" + str(ds_last_skillcheck.dices[0] + ds_last_skillcheck.dices[1]):
                    font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                    color "#ffffff"
                    size 24
                    xalign 1.0
            if len(ds_last_skillcheck.applied_modifiers) != 0:
                for modifier in ds_last_skillcheck.applied_modifiers:
                    fixed:
                        xmaximum 320
                        ymaximum 30
                        text modifier[2]:
                            font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                            color "#ffffff"
                            size 24
                            xalign 0.0
                        if modifier[1] > 0:
                            text "+" + str(modifier[1]):
                                font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                                color "#008000"
                                size 24
                                xalign 1.0
                        else:
                            text str(modifier[1]):
                                font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                                color "#ff0000"
                                size 24
                                xalign 1.0
        vbox:
            xalign 1.0
            yalign 1.0
            fixed:
                xmaximum 320
                ymaximum 30
                text "Всего:":
                    font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                    color "#ffffff"
                    size 24
                    xalign 0.0
                text str(ds_last_skillcheck.total_points()):
                    font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                    color "#ffffff"
                    size 24
                    xalign 1.0
            add "mods/disco_sovenok/gui/check/separator.png"
            fixed:
                xmaximum 320
                ymaximum 30
                text "Порог:":
                    font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                    color "#ffffff"
                    size 24
                    xalign 0.0
                text str(ds_last_skillcheck.threshold):
                    font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                    color "#ffffff"
                    size 24
                    xalign 1.0
            fixed:
                xmaximum 320
                ymaximum 30
                if ds_last_skillcheck.dices == (6, 6):
                    text "КРИТ. УСПЕХ":
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#008000"
                        size 24
                        xalign 0.5
                elif ds_last_skillcheck.dices == (1, 1):
                    text "КРИТ. НЕУДАЧА":
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#ff0000"
                        size 24
                        xalign 0.5
                elif ds_last_skillcheck.result():
                    text "УСПЕХ":
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#008000"
                        size 24
                        xalign 0.5
                else:
                    text "НЕУДАЧА":
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#ff0000"
                        size 24
                        xalign 0.5

screen ds_check_info(skill, threshold, modifiers):
    python:
        POSSIB = [97, 97, 97, 97, 92, 83, 72, 58, 42, 28, 17, 8, 3, 3]
        chance = POSSIB[ds_max(ds_min(threshold - ds_skill_list[skill].get_total(), 13), 0)]
    frame:
        background "mods/disco_sovenok/gui/check/check_base.png"
        xmaximum 600
        ymaximum 390
        yalign 0.0
        yoffset 20
        xalign 1.0
        at transform:
            on show:
                xoffset 600
                linear 0.2 xoffset -20
            on hide:
                xoffset -20
                linear 0.2 xoffset 600
        add ("mods/disco_sovenok/gui/skills/%s_large.png" % skill):
            xalign 0.0
            yalign 0.5
            xoffset -5
        vbox:
            xalign 1.0
            yalign 0.0
            add ("mods/disco_sovenok/gui/check/%s_caption.png" % skill)
            fixed:
                xmaximum 310
                ymaximum 50
                if chance < 30:
                    text "НИЗКИЕ ШАНСЫ":
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#ff0000"
                        size 30
                        xalign 0.5
                elif chance > 70:
                    text "ВЫСОКИЕ ШАНСЫ":
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#008000"
                        size 30
                        xalign 0.5
                else:
                    text "РАВНЫЕ ШАНСЫ":
                        font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                        color "#ffff00"
                        size 30
                        xalign 0.5
            fixed:
                xmaximum 320
                ymaximum 150
                text '{size=72}[chance]{/size}{color=#ffffff}%{/color}':
                    font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                    if chance < 30:
                        color "#ff0000"
                    elif chance > 70:
                        color "#008000"
                    else:
                        color "#ffff00"
                    size 60
                    xalign 0.5
            if modifiers != None:
                for condition, bonus, descr in modifiers:
                    if eval(condition):
                        fixed:
                            xmaximum 320
                            ymaximum 30
                            text descr:
                                font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                                color "#ffffff"
                                size 24
                                xalign 0.0
                            if bonus > 0:
                                text "+" + str(bonus):
                                    font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                                    color "#008000"
                                    size 24
                                    xalign 1.0
                            else:
                                text str(bonus):
                                    font "0@mods/disco_sovenok/gui/fonts/PTSans.ttc"
                                    color "#ff0000"
                                    size 24
                                    xalign 1.0

screen ds_start_game:
    modal True
    imagebutton:
        auto "mods/disco_sovenok/gui/start_game_%s.png"
        xalign 0.5
        yalign 0.8
        action [Return(True), Hide('ds_start_screen')]

label ds_achievement(ach):
    play sound sfx_achievement
    python:
        if not persistent.ds_achievements[ach]:
            renpy.show('ds_'+ach, at_list=[achievement_trans])
            renpy.pause(3, hard=True)
            renpy.hide('ds_'+ach)
            persistent.ds_achievements[ach] = True
    return