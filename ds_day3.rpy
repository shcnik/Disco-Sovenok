# DISCO SOVENOK
# ОБЩИЙ РУТ. ДЕНЬ 3

init:
    $ ds_was_on_lineup = False
    $ ds_accept_mz = False
    $ ds_understood_mz_reason = False
    $ ds_promise_un = False
    $ ds_to_help_un = False
    $ ds_whom_helped = None
    $ ds_dance_dv = False
    $ ds_dv_invite = False
    $ ds_el_mz_relation = False
    $ ds_seen_catgirl_photo = False
    $ ds_un_club = False
    $ ds_sugar = 0
    $ ds_morning_exercise = False
    $ ds_mi_costume = False
    $ ds_promise_sl = False
    $ ds_framed_dv = False
    $ ds_punished = False
    $ ds_after_lunch_who = None
    $ ds_mi_accept_dv = False
    $ ds_concert_part = False
    $ ds_composition_type = 0
    $ ds_forest_accept_sl = 0
    $ ds_helped_sl_lib = False
    $ ds_day3_evening_who = None
    $ ds_un_dance_accept = False
    $ ds_dumped_dv = False
    $ ds_dumped_un = False
    $ ds_day3_dv_conflict = False
    $ ds_played_guitar = False

    default ds_approved_pp = {
        'dv': False,
        'un': False,
        'sl': False,
        'us': False,
        'mi': False,
        'el': False,
        'mt': False
    }

label ds_day3_morning:
    $ ds_restore_health()
    $ ds_restore_morale()

    $ backdrop = "days"
    $ new_chapter(3, u"Disco Sovenok. День 3")
    $ save_name = u"Disco Sovenok. Общий рут. День 3."
    $ day_time()

    scene bg black 

    window show
    play sound ds_sfx_psy
    vol "Ночь оставила после себя тревогу, ты просыпаешься разбитым физически, истощённым морально."
    play sound ds_sfx_psy
    ine "С тобой такое постоянно: во сне видишь невозможно яркие сцены, как будто попал в голливудский блокбастер с лихо закрученным сюжетом, высококлассными актёрами и многомиллионными спецэффектами, а наутро не помнишь оттуда и кадра."
    ine "Вот и сейчас ты пытаешься восстановить картины, которые показывал тебе отдыхающий мозг, но эта часть памяти пуста – то ли заархивирована, то ли вообще отформатирована."
    vol "Наверное, оно и к лучшему."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_house_of_mt_day 
    show unblink 
    with fade

    if ds_sl_workouts:
        play music ds_sl_theme fadein 5
        show sl normal sport at center with dissolve

        sl "Доброе утро, Семён!"
        play sound ds_sfx_mot
        per_eye "Часы показывают 6 утра."
        th "Чего ей надо от меня так рано?.."
        if skillcheck('reaction_speed', lvl_easy, passive=True):
            play sound ds_sfx_mot
            res "{result}Вообще-то, ты самолично вчера предложил по утрам заниматься!"
            $ ds_skill_points['reaction_speed'] += 1
            window hide
            menu:
                "Спросить":
                    window show
                    me "Ты чего так рано?"
                    show sl suprise sport at center with dspr
                    sl "Так ведь вчера договаривались позаниматься спортом."
                "Прогнать":
                    window show
                    me "Ты чего припёрлась так рано?! Я спать хочу!"
                    show sl scared sport at center with dspr
                    sl "Так ведь... вчера... сам предложил..."
                    me "А, точно..."
                    $ ds_lp['sl'] -= 1
                "Продолжить":
                    window show
                    me "А, помню-помню, пробежки..."
        else:
            window hide
            menu:
                "Спросить":
                    window show
                    me "Ты чего так рано?"
                    show sl suprise sport at center with dspr
                    sl "Так ведь вчера договаривались позаниматься спортом."
                "Прогнать":
                    window show
                    me "Ты чего припёрлась так рано?! Я спать хочу!"
                    show sl scared sport at center with dspr
                    sl "Так ведь... вчера... сам предложил..."
                    me "А, точно..."
                    $ ds_lp['sl'] -= 1
        window hide
        menu:
            "Пойти":
                window show
                me "Идём, только я соберусь сейчас!"
                show sl smile sport at center with dspr
                sl "Отлично!"
                $ ds_lp['sl'] += 1
                jump ds_day3_sl_workout
            "Отказаться":
                window show
                me "Знаешь, я передумал... не хочется что-то, да и лень..."
                show sl sad sport at center with dspr
                sl "Вот как... ну ладно... до встречи тогда."
                hide sl with dissolve
                "Она выходит."
                $ ds_lp['sl'] -= 1
            "{check=drama:12}Притвориться, что не можешь":
                if skillcheck('drama', lvl_challenging):
                    window show
                    dra "{result}У вас болит... скажем, живот, мессир."
                    me "Ох... слушай, давай не в этот раз... у меня живот разболелся..."
                    dra "Вы достаточно правдоподобно показываете боль в животе."
                    show sl scared sport at center with dspr
                    sl "Ой... ты к медсестре сходи тогда! Когда она заступит на пост!"
                    show sl normal sport at center with dspr
                    sl "Ладно, я побежала, завтра позанимаемся!"
                    hide sl with dissolve
                    dra "Кажется, она поверила."
                else:
                    window show
                    dra "{result}Вы и пытаетесь изобразить, что у вас что-то болит, мессир, но ничего внятного не получается."
                    me "Ах... у меня всё болит..."
                    show sl angry sport at center with dspr
                    sl "Врать нехорошо, Семён! Сказал бы, что просто не хочешь!"
                    sl "А так делать нехорошо... да и вообще, зачем тогда сам предлагал?!"
                    sl "Ладно, я пойду! Удачного дня!"
                    $ ds_lp['sl'] -= 2
    else:
        window show
        play sound ds_sfx_mot
        per_eye "Часы показывают 7 утра."

        play music music_list["everyday_theme"] fadein 5

        th "Что-то сегодня я рано."
    jump ds_day3_dressing


label ds_day3_sl_workout:
    scene bg ext_house_of_mt_day
    show sl normal sport at center
    with dissolve
    stop music fadeout 3
    sl "Так, погоди, нам надо же взять тебе спортивную форму!"
    me "Да..."
    sl "Она на складе... ты подождёшь тут, или сходим вместе?"
    window hide
    menu:
        "Подождать Славю":
            window show
            me "Cходи ты, а я подожду."
            sl "Ладно... кстати, а какой у тебя рост?"
            me "Метр восемьдесят три..."
            sl "Отлично! Я быстро!"
            hide sl with dissolve
            $ ds_lp['sl'] -= 1

            "Ты стоишь и ждёшь Славю."
            window hide
            $ renpy.pause(3.0)
            window show

            if ds_sl_keys:
                show sl sad sport at center with dissolve
                sl "Всё отменяется! Я ключи потеряла!"
                th "Точно, ключи..."
                play sound ds_sfx_mot
                res "Они у тебя в кармане же!"
                window hide
                menu:
                    "Отдать ключи":
                        window show
                        me "А, я их нашёл, как раз тебе хотел отдать..."
                        show sl smile sport at center with dspr
                        sl "Ой, спасибо! Ты меня спас!"
                        sl "Так, сейчас я сбегаю ещё раз!"
                        $ ds_lp['sl'] += 1
                        $ ds_karma += 5
                    "Не отдавать":
                        window show
                        me "Не знаю..."
                        sl "Похоже, сегодня позаниматься не получится..."
                        sl "Ладно, удачи..."
                        hide sl with dissolve
                        play sound ds_sfx_psy
                        emp "Похоже, ей грозят серьёзные последствия... или она хотела провести время с тобой, а тут всё накрылось медным тазом."
                        emp "А между тем ключи у тебя-то!"
                        "Славя уходит, а ты заходишь обратно в домик."
                        jump ds_day3_dressing
                hide sl with dissolve
                window hide
                $ renpy.pause(3.0)
                window show
            show sl smile sport at center with dissolve
            sl "А вот и я! С формой!"
        "Сходить вместе":
            window show
            me "Лучше пойдём вместе."
            show sl smile sport at center with dspr
            sl "Хорошо, идём!"

            window hide
            scene bg ext_houses_day
            show sl normal sport at center
            with dissolve
            $ renpy.pause(1.0)
            scene bg ds_ext_storage_day
            show sl normal sport at center
            with dissolve
            window show

            "Вы подходите к складу."
            if ds_sl_keys:
                sl "Так... ой!"
                show sl scared sport at left with dspr
                sl "Я же потеряла ключи..."
                show sl sad sport at center with dspr
                sl "Мне же влетит от вожатой..."
                th "Точно, ключи..."
                play sound ds_sfx_mot
                res "Они у тебя в кармане же!"
                window hide
                menu:
                    "Отдать ключи":
                        window show
                        me "А, я их нашёл, как раз тебе хотел отдать..."
                        show sl smile sport at center with dspr
                        sl "Ой, спасибо! Ты меня спас!"
                        $ ds_lp['sl'] += 1
                        $ ds_karma += 5
                        play sound sfx_keys_rattle
                        "Ты передаёшь ключи Славе."
                    "Не отдавать":
                        window show
                        me "Не знаю..."
                        sl "Похоже, сегодня позаниматься не получится..."
                        sl "Ладно, удачи..."
                        hide sl with dissolve
                        play sound ds_sfx_psy
                        emp "Похоже, ей грозят серьёзные последствия... или она хотела провести время с тобой, а тут всё накрылось медным тазом."
                        emp "А между тем ключи у тебя-то!"
                        "Славя уходит, а ты возвращаешься к себе."
                        scene bg ext_house_of_mt_day
                        with dissolve
                        jump ds_day3_dressing

            play sound sfx_key_drawer
            "Славя открывает замок, и вы заходите."

            scene bg ds_int_storage_day
            show sl normal sport at center
            with dissolve

            sl "Погодь, сейчас найду тебе форму. Какой у тебя рост?"
            me "Метр восемьдесят три..."
            sl "Отлично, подожди!"
            scene bg ds_int_storage_day2
            show sl normal sport far at fleft
            with dissolve

            window hide
            $ renpy.pause(0.5)
            window show
            show sl smile sport at center with dspr
            sl "Вот она! Возвращаемся!"

            scene bg ds_ext_storage_day
            with dissolve
            play sound sfx_lock_close
            "Славя запирает дверь, и вы возвращаетесь."

            window hide
            scene bg ext_houses_day
            show sl normal sport at center
            with dissolve
            $ renpy.pause(1.0)
            scene bg ds_ext_house_of_mt_day
            show sl normal sport at center
            with dissolve
            window show
        "Сходить одному":
            window show
            me "Да я и сам схожу... подожди меня тут!"
            if ds_sl_keys:
                sl "А, ну ладно... так, вот ключ..."
                show sl scared sport at center with dspr
                sl "А где ключи?!"
                sl "Ой, я же их потеряла где-то..."
                show sl sad sport at center with dspr
                sl "Мне же влетит от вожатой..."
                th "Точно, ключи..."
                play sound ds_sfx_mot
                res "Они у тебя в кармане же!"
                window hide
                menu:
                    "Отдать ключи":
                        window show
                        me "А, я их нашёл, как раз тебе хотел отдать..."
                        show sl smile sport at center with dspr
                        sl "Ой, спасибо! Ты меня спас!"
                        sl "Так, отдашь, когда сходишь за формой."
                        $ ds_lp['sl'] += 1
                        $ ds_karma += 5
                    "Не отдавать":
                        window show
                        me "Не знаю..."
                        sl "Похоже, сегодня позаниматься не получится..."
                        sl "Ладно, удачи..."
                        hide sl with dissolve
                        play sound ds_sfx_psy
                        emp "Похоже, ей грозят серьёзные последствия... или она хотела провести время с тобой, а тут всё накрылось медным тазом."
                        emp "А между тем ключи у тебя-то!"
                        "Славя уходит, а ты заходишь обратно в домик."
                        jump ds_day3_dressing
            else:
                sl "А, ну ладно... так, вот ключ от склада."
                play sound sfx_keys_rattle
            sl "Возвращайся поскорее!"

            window hide
            scene bg ext_houses_day
            with dissolve
            $ renpy.pause(1.0)
            scene bg ds_ext_storage_day
            with dissolve
            window show

            "Ты подходишь к складу."
            "Предсказуемо, он оказывается заперт."
            play sound ds_sfx_mot
            inf "К счастью, у тебя оказывается ключ!"
            if not ds_some_key:
                inf "Кстати, может, и себе ключик заберёшь?"
                window hide
                menu:
                    "{check=interfacing:8}Отцепить ключ":
                        if skillcheck('interfacing', lvl_easy):
                            window show
                            inf "{result}Это легче лёгкого, благо тебе и скрываться не надо!"
                            $ ds_some_key = True
                            "Ты кладёшь в карман отцепленный ключ."
                        else:
                            window show
                            inf "{result}Ты пытаешься отсоединить ключ от кольца, но ничего не выходит!"
                            inf "Ключи просто падают на землю..."
                            th "Ладно, не в этот раз..."
                        $ ds_skill_points['interfacing'] += 1
                    "Не отцеплять":
                        window show
                        th "Да ну, зачем он мне?"
            play sound sfx_key_drawer

            scene bg ds_int_storage_day
            with dissolve
            "Ты заходишь на склад."
            play sound ds_sfx_mot
            per_eye "Ты видишь коробки с надписями «Свечи» и «Лампочки» - явно не то, что надо."
            per_eye "Этот стеллаж в остальном заполнен постельным бельём - идём дальше." 
            scene bg ds_int_storage_day2
            with dissolve
            per_eye "А вот тут есть всякая одежда."
            per_eye "Вскоре ты находишь спортивную форму своего размера - благо все размеры помечены."

            scene bg ds_ext_storage_day
            with dissolve
            play sound sfx_lock_close
            "Ты запираешь дверь и возвращаешься к Славе."

            scene bg ext_house_of_mt_day
            show sl smile sport at center
            with dissolve
            sl "О, вернулся! Ещё и с формой!"
            me "Да..."
            sl "Так, отдавай ключи и иди переодеваться."
            if not ds_some_key:
                window hide
                menu:
                    "Просто отдать":
                        window show
                        me "Вот, держи."
                        play sound sfx_keys_rattle
                    "{check=interfacing:16}Отцепить ключ себе":
                        if skillcheck('interfacing', lvl_godly):
                            window show
                            inf "{result}Ты ловко двигаешь пальцами у себя в кармане... "
                            window hide
                            $ renpy.pause(0.5)
                            window show
                            inf "И в итоге туда проваливается какой-то ключик."
                            $ ds_skill_points['interfacing'] += 1
                            inf "Остальное ты вынимаешь и протягиваешь Славе."
                            me "Вот, держи."
                            play sound sfx_keys_rattle
                        else:
                            window show
                            play sound sfx_keys_rattle
                            $ renpy.pause(0.5)
                            play sound ds_sfx_mot
                            inf "{result}Но ключи слишком громко шумят, и Славя обращает внимание."
                            $ ds_skill_points['interfacing'] += 1
                            show sl serious pioneer at center with dspr
                            sl "Так, Семён, отдавай ключи!"
                            me "Вот, отдаю..."
                            play sound sfx_keys_rattle
                            $ ds_lp['sl'] -= 1
            else:
                me "Вот, держи."
                play sound sfx_keys_rattle
            sl "Отлично!"
    sl "Так, иди в домик и переодевайся, я тебя тут подожду!"
    me "Хорошо..."
    "С этими словами ты заходишь в домик."

    scene bg int_house_of_mt_day
    play sound ds_sfx_mot
    per_eye "Ольга Дмитриевна всё ещё спит."
    "Ты быстро переодеваешься и выходишь."

    scene bg ext_house_of_mt_day
    show sl normal sport at center
    with dissolve

    sl "Переоделся? Отлично! Побежали!"
    "И она побежала."
    play music ds_workout fadein 3
    play sound ds_sfx_fys
    edr "Приготовься... {w}Побежал!"

    window hide
    scene bg ext_houses_day:
        zoom 1.05 anchor (48,27)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (25,25)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (-25,25)
        repeat
    show sl normal sport at center
    with dissolve
    $ renpy.pause(3.0, hard=True)
    scene bg ext_path2_day:
        zoom 1.05 anchor (48,27)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (25,25)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (-25,25)
        repeat
    show sl normal sport at center
    with dissolve
    $ renpy.pause(3.0, hard=True)
    scene bg ext_musclub_day:
        zoom 1.05 anchor (48,27)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (25,25)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (-25,25)
        repeat
    show sl normal sport at center
    with dissolve
    $ renpy.pause(3.0, hard=True)
    scene bg ds_ext_clubs_gate_day:
        zoom 1.05 anchor (48,27)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (25,25)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (-25,25)
        repeat
    show sl normal sport at center
    with dissolve
    $ renpy.pause(3.0, hard=True)
    scene bg ext_square_day:
        zoom 1.05 anchor (48,27)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (25,25)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (-25,25)
        repeat
    show sl normal sport at center
    with dissolve
    $ renpy.pause(3.0, hard=True)
    scene bg ext_aidpost_day:
        zoom 1.05 anchor (48,27)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (25,25)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (-25,25)
        repeat
    show sl normal sport at center
    with dissolve
    $ renpy.pause(3.0, hard=True)
    scene bg ext_library_day:
        zoom 1.05 anchor (48,27)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (25,25)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (-25,25)
        repeat
    show sl normal sport at center
    with dissolve
    $ renpy.pause(3.0, hard=True)
    scene bg ext_stage_normal_day:
        zoom 1.05 anchor (48,27)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (25,25)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (-25,25)
        repeat
    show sl normal sport at center
    with dissolve
    $ renpy.pause(3.0, hard=True)
    scene bg ext_house_of_mt_day:
        zoom 1.05 anchor (48,27)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (25,25)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (-25,25)
        repeat
    show sl normal sport at center
    with dissolve

    window show
    play sound ds_sfx_fys
    edr "Ты уже выбиваешься из сил."
    play sound ds_sfx_psy
    aut "Однако, Славя продолжает бежать как ни в чём не бывало."
    window hide
    menu:
        "{check=endurance:12}Продолжить бежать":
            if skillcheck('endurance', lvl_challenging):
                window show
                edr "{result}У тебя открывается второе дыхание! Беги дальше!"
                $ ds_skill_points['endurance'] += 1
                window hide

                scene bg ext_houses_day:
                    zoom 1.05 anchor (48,27)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (25,25)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (-25,25)
                    repeat
                show sl normal sport at center
                with dissolve
                $ renpy.pause(3.0, hard=True)
                scene bg ext_path2_day:
                    zoom 1.05 anchor (48,27)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (25,25)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (-25,25)
                    repeat
                show sl normal sport at center
                with dissolve
                $ renpy.pause(3.0, hard=True)
                scene bg ext_musclub_day:
                    zoom 1.05 anchor (48,27)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (25,25)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (-25,25)
                    repeat
                show sl normal sport at center
                with dissolve
                $ renpy.pause(3.0, hard=True)
                scene bg ds_ext_clubs_gate_day:
                    zoom 1.05 anchor (48,27)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (25,25)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (-25,25)
                    repeat
                show sl normal sport at center
                with dissolve
                $ renpy.pause(3.0, hard=True)
                scene bg ext_square_day:
                    zoom 1.05 anchor (48,27)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (25,25)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (-25,25)
                    repeat
                show sl normal sport at center
                with dissolve
                $ renpy.pause(3.0, hard=True)
                scene bg ext_aidpost_day:
                    zoom 1.05 anchor (48,27)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (25,25)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (-25,25)
                    repeat
                show sl normal sport at center
                with dissolve
                $ renpy.pause(3.0, hard=True)
                scene bg ext_library_day:
                    zoom 1.05 anchor (48,27)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (25,25)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (-25,25)
                    repeat
                show sl normal sport at center
                with dissolve
                $ renpy.pause(3.0, hard=True)
                scene bg ext_stage_normal_day:
                    zoom 1.05 anchor (48,27)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (25,25)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (-25,25)
                    repeat
                show sl normal sport at center
                with dissolve
                $ renpy.pause(3.0, hard=True)
                scene bg ext_house_of_mt_day
                show sl normal sport at center
                with dissolve

                window show
                sl "Фух, на сегодня хватит! Хорошо побегали!"
                sl "Теперь надо в душ сходить!"
                sl "Ты иди, а я попозже подойду!"
                hide sl with dissolve
                "И она убегает."
            else:
                window show
                edr "{result}Ты пытаешься побежать... но от усталости падаешь."
                scene bg ext_house_of_mt_day
                play sound sfx_body_bump
                with vpunch
                $ ds_damage_health()
                stop music fadeout 3
                show sl scared sport at center with dspr
                sl "С тобой всё хорошо, Семён?"
                me "Да... просто споткнулся..."
                show sl serious sport at center with dspr
                sl "Так, значит, с тебя на сегодня хватит."
                show sl smile sport at center with dspr
                sl "Ты и так неплохо побегал, молодец!"
                $ ds_skill_points['endurance'] += 1
                sl "В общем, иди в душ, а я побежала дальше! Удачи!"
                hide sl with dissolve
        "Cойти с дистанции":
            window show
            me "Погоди, Славя! Я больше не могу!"
            scene bg ext_house_of_mt_day
            show sl surprise sport at center with dspr
            stop music fadeout 3
            sl "Всё нормально, Семён?"
            me "Да... просто устал..."
            show sl smile sport at center with dspr
            sl "Ну ничего! Ты всё равно молодец!"
            sl "В общем, иди в душ, а я побежала дальше! Удачи!"
            hide sl with dissolve
            "И с этими словами она убегает."
    stop music fadeout 3
    "А ты идёшь принять душ."
    scene bg int_house_of_mt_day
    with dissolve
    "Но перед этим заходишь в домик за своей пионерской формой."
    window hide
    scene bg ext_house_of_mt_day
    with dissolve
    $ renpy.pause(3.0)
    scene bg ds_ext_showers_day
    with dissolve
    window show
    "Все кабинки оказываются пустыми."
    th "Какую мне выбрать?"
    window hide
    menu:
        "1":
            pass
        "2":
            pass
        "3":
            pass
        "4":
            pass
    window show
    "Ты заходишь в кабинку и снимаешь с себя всю одежду."
    window hide
    play sound sfx_open_water_sink
    play ambience ds_ambience_shower
    $ renpy.pause(1.0)
    window show
    play sound ds_sfx_fys
    pat "В душе вода не такая холодная. Ты можешь даже нормально помыться!"
    window hide
    $ renpy.pause(1.0)
    play sound sfx_close_water_sink
    stop ambience
    "Ты надеваешь на себя пионерскую форму и выходишь из кабинки."
    show sl normal sport far at right with dissolve
    "В этот момент тебе навстречу идёт Славя."
    show sl normal sport at center with dspr
    sl "И снова привет! Как помылся?"
    me "Нормально..."
    show sl smile sport at center with dspr
    sl "Ну и хорошо. До встречи!"
    hide sl with dissolve
    "Она заходит в душ, также скидывает с себя всё и включает воду."
    play ambience ds_ambience_shower
    if skillcheck('instinct', lvl_trivial, passive=True):
        play sound ds_sfx_fys
        ins "{result}Тебе очень хочется посмотреть на её девичью красу..."
        play sound ds_sfx_psy
        vol "Но стоит ли? Только испортишь отношения с ней."
        window hide
        menu:
            "{check=savoir_faire:14}Подглянуть":
                if skillcheck('savoir_faire', lvl_legendary):
                    window show
                    svf "{result}Тебе удаётся воспользоваться тем, что дверцы закрываются неплотно."
                    svf "Ты подсматриваешь в щель так, что Славя тебя не видит."
                    $ ds_skill_points['savoir_faire'] += 1
                    ins "Однако, и ты толком ничего разглядеть не можешь!"
                    ins "Лишь немного её груди."
                    ins "Но тебе и этого достаточно."
                    $ ds_skill_points['instinct'] += 1
                    window hide
                    $ renpy.pause(1.5)
                    window show
                    svf "Когда Славя выключает воду, ты быстро отбегаешь."
                else:
                    window show
                    svf "{result}Ты начинаешь смотреть сверху дверцы, и Славя предсказуемо тебя замечает."
                    sl "Cемён! Дай мне помыться, пожалуйста."
                    $ ds_lp['sl'] -= 1
                    "Она легонько тебя отталкивает."
                    ins "Обидно... ты же даже не разглядел только ничего!"
                    "Ты уходишь к себе."
            "Распахнуть дверцу":
                window show
                "Ты берёшь дверцу и открываешь её."
                show sl angry naked at left with dissolve
                play sound ds_sfx_mot
                com "Однако, Славю хоть сколь-нибудь удивить у тебя не вышло. Для неё нагота не является чем-то сакральным."
                play sound ds_sfx_psy
                emp "Но ты ей не даёшь спокойно помыться, и это её злит."
                sl "Cемён! Дай мне помыться, пожалуйста."
                hide sl with dissolve
                "C этими словами она закрывает дверь."
                $ ds_lp['sl'] -= 1
                $ ds_skill_points['instinct'] += 1
                "А ты уходишь к себе."
                ins "То, что ты увидел, тебе понравилось."
            "Отбросить мысль":
                window show
                th "И правда, не стоит..."
                "И ты уходишь."
    stop ambience fadeout 3
    jump ds_day3_meet_mt

label ds_day3_dressing:
    scene bg int_house_of_mt_day
    with dissolve
    play sound ds_sfx_mot
    per_eye "Ольга Дмитриевна ещё спит, плотно укутавшись в одеяло."
    th "И как можно – летом, в такую жару..."
    "Ты встаёшь, потягиваешься..."
    window hide
    menu:
        "Посмотреть в зеркало":
            window show
            "Ты подходишь к зеркалу и осматриваешь себя."

            play sound sfx_open_cabinet_2
            if ds_know_face:
                scene cg d2_mirror
                with dissolve
                th "Надо побриться."
                "Странное решение – раньше хватало и пары раз в месяц, а сейчас от моего внешнего вида как будто что-то зависело!"
                "Однако бритву я так и не нашёл."
                th "Хотя зачем – сейчас я выгляжу от силы лет на семнадцать."
            else:

                scene cg d2_mirror :
                    zoom 1.8 anchor (0.5, 0.31) pos (0.5, 0.5)
                    linear 5.0 zoom 1.0 align (0.5, 0.5)
                with dissolve

                window show
                "Ты смотришь на новоиспеченного пионера и аж отпрыгнул в сторону от неожиданности!"
                "Из зеркала на тебя смотрит какой-то подросток, похожий на тебя."
                play sound ds_sfx_mot
                res "Но не ты!"
                res "Куда пропали недельная небритость, мешки под глазами, сутулость и смертельно уставшее выражение лица?!"
                play sound ds_sfx_int
                lgc "Похоже, тебя не закинули назад во времени или в параллельную реальность, а просто поменяли с кем-то телами."
                th "Действительно просто!{w} Такое же на каждом шагу встречается!"
                per_eye "Ты приглядываешься к незнакомцу повнимательнее и только теперь понял, что это ты сам!"
                per_eye "Только образца конца школы – начала института."
                th "Ладно, хотя бы так."
                th "Наверное, действительно, человек в стрессовой ситуации…"
                if ds_rude_mt:
                    th "А вот вожатая заметила и вчера ночью меня отчитала за неподобающее обращение к ней…"
                th "К черту!"
                $ ds_know_face = True
            play sound sfx_close_cabinet
            scene bg int_house_of_mt_day
            with dissolve
        "Забить":
            window show
    play sound ds_sfx_int
    lgc "Завтрак – не раньше девяти, а это значит, что ещё полно времени."
    lgc "Которое можно потратить, например, на утренний моцион и гигиенические процедуры."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_washstand2_day 
    with dissolve

    play sound sfx_open_water_sink
    play sound_loop sfx_water_sink_stream fadein 2

    window show
    play sound ds_sfx_fys
    pat "В этот раз вода не показалась такой леденяще обжигающей, как вчера."
    play sound ds_sfx_psy
    vol "Напротив – приятная прохлада придаёт тебе бодрости и помогает быстрее вернуться к реальности."
    lgc "Сегодня зубной порошок не кажется таким уж анахронизмом, и у тебя даже мелькает мысль, что он не особо отличается от зубной пасты."
    window hide

    stop sound_loop
    play sound sfx_close_water_sink

    scene bg ext_houses_day
    with dissolve
    $ renpy.pause(1.0)
    scene bg ext_house_of_mt_day
    with dissolve
    $ renpy.pause(0.5)
    jump ds_day3_meet_mt

label ds_day3_meet_mt:
    $ persistent.sprite_time = "day"
    scene bg int_house_of_mt_day 
    with dissolve

    show mt normal pioneer at center   with dissolve
    window show
    "Когда ты возвращаешься в домик вожатой, Ольга Дмитриевна уже проснулась."
    "Она стоит перед зеркалом и расчёсывает волосы."
    if skillcheck('suggestion', lvl_easy, passive=True):
        play sound ds_sfx_psy
        sug "{result}Похвали волосы! Ей будет приятно, и это улучшит её отношение к тебе."
        show mt smile pioneer at center   with dspr
        mt "Доброе утро, Семён!"
        window hide
        menu:
            "Похвалить волосы":
                window show
                me "Доброе утро. У вас, кстати, прекрасные волосы!"
                show mt laugh pioneer at center with dspr
                mt "Cпасибо, Семён!"
                $ ds_lp['mt'] += 1
                $ ds_skill_points['suggestion'] += 1
            "Просто поздороваться":
                window show
                me "Доброе."
    else:
        show mt smile pioneer at center   with dspr
        mt "Доброе утро, Семён!"
        me "Доброе."
    play sound ds_sfx_psy
    vol "От недосыпа ещё немного гудит голова и путаются мысли, но это лучше, что ты всё-таки вылез из кровати, а не остался, как обычно, досыпать дежурные пару-тройку часов."
    show mt normal pioneer at center   with dspr
    mt "Что-то ты сегодня рано."
    me "Так получилось…"
    mt "Опять ты без галстука, давай я…"
    window hide
    menu:
        "Позволить":
            window show
            "Она завязывает тебе галстук."
            $ ds_lp['mt'] += 1
            show mt smile pioneer at center with dspr
            mt "Вот теперь ты настоящий пионер!"
            show mt normal pioneer at center with dspr
            mt "Не забудь: у нас линейка ещё!"
        "Отказаться":
            window show
            me "Да я сам, ничего страшного… когда на завтрак пойду."
            mt "Нет уж, давай сейчас!{w} До завтрака у нас ещё линейка, не забывай!"
    th "Забудешь тут!"
    me "А что сегодня на линейке на этой будет?"
    mt "Я расскажу о плане на день."
    window hide
    menu:
        "Cпросить про план":
            window show
            me "И каков план?"
            show mt grin pioneer at center   with dspr
            mt "А это ты узнаешь на линейке!"
            "Она хитро улыбается."
        "Промолчать":
            window show
    play sound ds_sfx_psy
    sug "И что тебе на этой линейке делать?"
    window hide
    menu:
        "Cмирно пойти":
            window show
            me "Ладно..."
            mt "Так, идём!"
            $ ds_karma += 5
            jump ds_day3_lineup
        "{check=drama:15}Попытаться избежать":
            if skillcheck('drama', lvl_heroic):
                window show
                play sound ds_sfx_int
                dra "{result}Изобразите, что у вас болит живот."
                $ ds_skill_points['drama'] += 1
                me "Ольга Дмитриевна, знаете, у меня что-то живот разболелся – мне бы…"
                me "Ну, вы понимаете…"
                me "Думаю, ничего страшного, если я разок пропущу, а то будет неприятно, если я прямо там…"
                show mt normal pioneer at center   with dspr
                mt "У тебя есть ещё минут пять."
                me "Боюсь, не успею.{w} Давайте вы мне расскажете сейчас."
                me "Нет, я постараюсь, но если вдруг…"
                mt "Ладно уж!{w} Сегодня у нас по плану уборка территории, сортировка книг в библиотеке, ещё кое-что, а вечером – танцы."
                show mt angry pioneer at center   with dspr
                mt "Смотри у меня!"
                mt "Чтобы обязательно сегодня поучаствовал в жизни лагеря!"
                dra "Всенепременно!"
                me "Конечно, конечно, а сейчас мне бы…"
                show mt normal pioneer at center   with dspr

                stop music fadeout 3

                mt "Иди уж!"
                window hide
                $ persistent.sprite_time = "day"
                scene bg ext_house_of_mt_day 
                with dissolve

                play ambience ambience_camp_center_day fadein 2

                window show
                svf "Ты выходишь из домика, обходишь его и прячешься в кустах, дожидаясь, пока Ольга Дмитриевна уйдёт."
                vol "По правде говоря, у тебя не было особых причин так себя вести."
                window hide
                with fade2

                window show
                "Когда вожатая уходит, ты возвращаешься назад в домик."
                th "Подожду завтрака."
                window hide

                stop ambience fadeout 2

                pause(2)

                $ persistent.sprite_time = "day"
                scene bg int_house_of_mt_day 
                with dissolve

                play ambience ambience_int_cabin_day fadein 3
            else:
                window show
                play sound ds_sfx_int
                dra "{result}У вас не хватает фантазии придумать и изобразить, что вы {i}не можете{/i} пойти на линейку."
                $ ds_skill_points['drama'] += 1
                me "Ну Ольга Дмитриевна, давайте я сегодня..."
                show mt angry pioneer at center with dspr
                mt "Нет, Семён, посещение линейки обязательно!"
                $ ds_karma -= 5
                me "Ладно..."
                show mt normal pioneer at center with dspr
                mt "Так, идём!"
                jump ds_day3_lineup
        "{check=authority:16}Протестовать":
            if skillcheck('authority', lvl_godly):
                window show
                play sound ds_sfx_psy
                aut "{result}Ты свободная личность! И никуда ты не пойдёшь!"
                aut "Покажи своим лицом и телом, что тут ты главный."
                me "Не пойду я никуда, и вообще у меня дела! Важнее, чем ваша линейка!"
                show mt surprise pioneer at center with dspr
                mt "Эм... ну ладно..."
                aut "Её очень сильно удивил твой ход."
                $ ds_skill_points['authority'] += 1
                $ ds_karma -= 10
                $ ds_lp['mt'] -= 1
                show mt normal pioneer at center with dspr
                mt "Сегодня у нас по плану уборка территории, сортировка книг в библиотеке, ещё кое-что, а вечером – танцы."
                mt "И в жизни лагеря поучаствуй обязательно!"
                me "Ну ладно..."
                hide mt with dissolve
            else:
                window show
                play sound ds_sfx_psy
                aut "{result}У тебя не хватит решимости пойти против вожатой."
                $ ds_skill_points['authority'] += 1
                me "Ну Ольга Дмитриевна, давайте я сегодня..."
                show mt angry pioneer at center with dspr
                mt "Нет, Семён, посещение линейки обязательно!"
                $ ds_karma -= 5
                me "Ладно..."
                show mt normal pioneer at center with dspr
                mt "Так, идём!"
                jump ds_day3_lineup
        "{check=savoir_faire:15}Улизнуть":
            if skillcheck('savoir_faire', lvl_heroic):
                window show
                play sound ds_sfx_mot
                svf "{result}Ты резко срываешься с места и бросаешься в дверь."
                scene bg ext_house_of_mt_day
                with dissolve
                mt "CЕМЁН!"
                svf "Прячься в кусты!"
                $ ds_skill_points['savoir_faire'] += 1
                window hide
                $ renpy.pause(1.0)
                window show
                show mt rage pioneer at center with dspr
                mt "Куда побежал?!"
                mt "Пионер обязан ходить на линейки! И участвовать в жизни лагеря!"
                $ ds_karma -= 10
                $ ds_lp['mt'] -= 1
                me "Ладно..."
                jump ds_day3_lineup
            else:
                window show
                play sound ds_sfx_mot
                svf "{result}Ты пытаешься сбежать, бросаешься в дверь..."
                svf "Но тут лестница! Ты запинаешься о неё и падаешь!"
                window hide
                scene bg ext_house_of_mt_day
                with vpunch
                $ ds_damage_health()
                $ renpy.pause(0.5)
                window show
                show mt shocked pioneer at center with dissolve
                mt "Ты чего, Семён? Всё нормально?"
                me "Да... просто ударился..."
                mt "Ладно... полежи тогда в домике пока..."
                show mt normal pioneer at center with dspr
                mt "Сегодня у нас по плану уборка территории, сортировка книг в библиотеке, ещё кое-что, а вечером – танцы."
                mt "Обязательно поучаствуй в жизни лагеря!"
                mt "Ну, если будешь чувствовать себя нормально... иначе к медсестре!"
                scene bg int_house_of_mt_day
                with dissolve
    window show
    play sound ds_sfx_psy
    vol "Итак, участвовать в общественной деятельности сегодня ты не планируешь."
    vol "Уборка, книги в библиотеке – это совсем не то, чем должен заниматься человек в твоём положении."
    play sound ds_sfx_int
    lgc "Однако уже прошло два дня, а ты ни на йоту не приблизился к разгадке."
    lgc "Все местные обитатели кажутся в целом совершенно нормальными людьми – они не были замешаны в каких-то тайных заговорах, не сотрудничали с инопланетянами и вряд ли подозревали о провалах во времени."
    play sound ds_sfx_psy
    ine "Конечно, каждый (а скорее даже – каждая) из них не без странностей, но странности эти не выходили за рамки разумного."
    lgc "Более того, встретив любого из здешних пионеров в своём привычном мире, ты бы даже не подумал, что с ними что-то не так."
    ine "Скорее, они показались бы мне куда более нормальными и естественными, чем, скажем, я сам."
    lgc "Эта линия рассуждений выглядит весьма логичной, нелогичным в ней было лишь отсутствие ответов."
    play sound ds_sfx_int
    enc "Обычные люди в необычном месте."
    enc "Где-то ты об этом уже слышал, где-то видел."
    ine "Десятки пионеров (а может, их куда больше) живут привычной жизнью, занимаются привычными делами изо дня в день и даже не подозревают, что мир вокруг них совсем не такой, каким должен быть."
    lgc "Ладно.{w} Но это – ситуация с их точки зрения.{w} Мне же не знаком не только мир лагеря «Совёнок», но и его обитатели, пусть даже по обстоятельствам они и ведут себя так, как по идее и должны."
    lgc "Сейчас необходимо решить один вопрос – имеют ли люди здесь какое-то отношение ко всему, что с тобой произошло?"
    play sound ds_sfx_int
    rhe "И найдёшь ли ты ответы у них?"
    rhe "Или, может быть, до истины тебе придётся докапываться другим путём?"
    window hide

    stop ambience fadeout 2  

    with fade2

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_away_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 2

    window show
    "Обычной толпы голодных пионеров возле столовой не наблюдается."
    window hide

    stop ambience fadeout 2

    $ renpy.pause(1)

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_day 
    with dissolve

    play ambience ambience_dining_hall_empty fadein 3

    window show
    play sound ds_sfx_mot
    res "Да и внутри немноголюдно."
    play sound ds_sfx_int
    lgc "Наверное, большинство детей позавтракало ещё до 9 часов."
    th "И хорошо: меньше народу – больше кислороду!"

    jump ds_day3_breakfast

label ds_day3_lineup:
    $ ds_was_on_lineup = True

    $ persistent.sprite_time = 'day'
    scene bg ext_square_day
    with dissolve
    show mt normal pioneer at center with dspr
    play ambience ambience_medium_crowd_outdoors 
    mt "А вот и мы! Все построились?"
    stop ambience
    mt "Отлично, приступаем!"

    scene cg ds_day2_lineup
    with dissolve

    mt "Сегодня очень важный день в жизни лагеря! Начну с того, что вечером у нас состоятся танцы!"
    voices "Ура!"
    mt "Явка обязательна без исключений! Как известно, пионер должен проводить время вместе со своим коллективом!"
    play sound ds_sfx_mot
    res "Непохоже, что обязательная явка хоть кого-то расстроила..."
    if skillcheck('empathy', lvl_easy, passive=True):
        play sound ds_sfx_psy
        emp "{result}Разве что Алиса, похоже, не очень-то горит желанием танцевать."
    mt "Однако, как известно, делу время, а потехе час! Поэтому сегодня мы должны поработать на славу!"
    play sound ds_sfx_int
    rhe "Говоря «мы», она подразумевает «вы», то есть пионеры."
    mt "Cегодня по плану наши основные задачи - следующие!"
    mt "А - уборка территории. За неё отвечает Славяна Феоктистова!"
    mt "Б - наши учёные-кибернетики Александр Демьяненко и Сергей Сыроежкин разрабатывают очень важный для лагеря проект. Желающие могут присоединиться!"
    play sound ds_sfx_psy
    sug "Как хитро устроились! Занимаются своими делами, пока остальные работают!"
    mt "В - сегодня проводится ремонт спортплощадки под руководством нашего уважаемого преподавателя физической культуры Бориса Александровича!"
    mt "Г - наведение порядка на сцене... под ответственность Алисы Двачевской..."
    if skillcheck('perception', lvl_challenging, passive=True):
        play sound ds_sfx_mot
        per_hea "{result}Ты можешь услышать, как вожатая говорит шёпотом: «прости господи»."
        play sound ds_sfx_psy
        emp "Видимо, она назначила Алису скрепя сердце."
    mt "Д - сортировка книг в библиотеке. За это отвечает наша уважаемая библиотекарша Евгения Мицгол."
    play sound ds_sfx_int
    lgc "Она весь алфавит решила использовать, что ли?"
    mt "Е - разбор вещей, хранящихся в кладовке музыкального клуба, под руководством Мику Хацуне."
    mt "И наконец Ж - вашей любимой вожатой, то есть мне, нужна помощь с наведением порядка в документации в административном корпусе."
    mt "Прошу после завтрака подойти ко мне и отметиться, куда вы пойдёте!"
    window hide
    play sound sfx_dinner_horn_processed
    $ renpy.pause(1.0)
    window show
    play sound ds_sfx_mot
    res "Она закончила аккурат к завтраку."
    mt "Линейка окончена!"
    scene bg ext_square_day with dissolve
    "Все идут завтракать."
    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_away_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 2

    window show
    "У столовой как обычно многолюдно. Однако, тебе удаётся прорваться одним из первых."
    window hide

    stop ambience fadeout 2

    $ renpy.pause(1)

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_day 
    with dissolve

    play ambience ambience_dining_hall_full fadein 3

    window show
    show ck normal at center with dissolve
    "Ты берёшь еду без особых задержек."
    hide ck with dissolve

    jump ds_day3_breakfast


label ds_day3_breakfast:
    "В дальнем углу столовой одиноко сидит Лена и лениво ковыряет вилкой нечто бесформенное, отдалённо напоминающее кашу."
    play sound ds_sfx_psy
    sug "Позавтракать с ней – отличная идея: тихо, спокойно и можно о чём-нибудь поговорить."
    sug "Ну, или хотя бы попытаться."
    window hide
    menu:
        "{check=volition:8}Позавтракать с Леной":
            if skillcheck('volition', lvl_easy):
                window show
                play sound ds_sfx_psy
                vol "{result}Ты решительно направляешься в её сторону."
                $ ds_skill_points['volition'] += 1
                play sound ds_sfx_mot
                svf "Но тут тебя хватают за руку!"
                show mz normal glasses pioneer at center   with dissolve
                "Женя, вчерашняя библиотекарша."
                mz "Бери завтрак и садись, есть разговор."
                if not skillcheck('composure', lvl_medium, passive=True):
                    play sound ds_sfx_mot
                    com "{result}Ты несколько растерялся и молчишь."
                    show mz bukal glasses pioneer at center   with dspr
                    mz "Чего стоишь?"
                me "Извини, но не слишком ли это… резко?"
                show mz normal glasses pioneer at center   with dspr
                mz "А что такого-то? Бери завтрак и садись."
                play sound ds_sfx_psy
                aut "Похоже, для неё такое поведение совершенно нормально."
                window hide
                menu:
                    "{check=volition:10}Пойти к Лене":
                        if skillcheck('volition', lvl_medium):
                            window show
                            play sound ds_sfx_psy
                            vol "{result}Ты уверен, что Лена будет не против твоей компании."
                            vol "А Женя... вряд ли у неё что-то срочное."
                            $ ds_lp['un'] += 1
                            $ ds_skill_points['volition'] += 1
                            jump ds_day3_breakfast_un
                        else:
                            window show
                            play sound ds_sfx_psy
                            vol "{result}Нет, у тебя не хватает воли уйти от Жени к Лене."
                            $ ds_skill_points['volition'] += 1
                    "Остаться с Женей":
                        $ ds_lp['mz'] += 1
                        jump ds_day3_breakfast_mz
            else:
                window show
                play sound ds_sfx_psy
                vol "Однако у тебя не хватает решимости предложить свою компанию Лене - вдруг откажет?"
        "Позавтракать одному":
            window show
    "Ты только сел было за стол, как к тебе подсаживается Женя, вчерашняя библиотекарша."
    show mz normal glasses pioneer at center with dissolve
    mz "Есть разговор!"
    if not skillcheck('composure', lvl_medium, passive=True):
        play sound ds_sfx_mot
        com "{result}Ты несколько растерялся и молчишь."
        show mz bukal glasses pioneer at center   with dspr
        mz "Чего расселся?"
    window hide
    menu:
        "Сделать замечание":
            me "Извини, но не слишком ли это… резко?"
            show mz normal glasses pioneer at center   with dspr
            mz "А что такого-то?"
            play sound ds_sfx_psy
            aut "Похоже, для неё такое поведение совершенно нормально."
        "{check=suggestion:12}Сделать комплимент":
            if skillcheck('suggestion', lvl_challenging):
                window show
                sug "{result}Скажи ей про её волосы. Или про лицо."
                me "А у тебя прекрасные волосы. Такие густые, и цвет красивый!"
                $ ds_lp['mz'] += 1
                show mz shy glasses pioneer at center with dspr
                mz "Это хорошо, что ты так считаешь... но разговор не ждёт!"
            else:
                window show
                sug "{result}Тебе не приходит в голову хороших комплиментов."
                me "Прекрасно выглядишь!"
                $ ds_lp['mz'] += 1
                show mz shy glasses pioneer at center with dspr
                mz "Это хорошо, что ты так считаешь... но разговор не ждёт!"
            $ ds_skill_points['suggestion'] += 1
        "Промолчать":
            pass
    window hide
    jump ds_day3_breakfast_mz

label ds_day3_breakfast_mz:
    window show
    play sound ds_sfx_int
    enc "Вдруг получится узнать что-то новое.{w} Всё-таки она книжный червь."
    window hide

    with fade

    play music music_list["your_bright_side"] fadein 5

    show mz normal glasses pioneer at center   with dspr
    window show
    "Через минуту ты уже сидишь напротив Жени, а перед тобой на столе стоял поднос с нехитрым набором блюд: каша овсяная, два яйца варёных, хлеб белый, четыре куска, сосиска варёная, одна штука, компот из непонятного набора фруктов и ягод, один стакан."
    me "Приятного аппетита!"
    mz "Спасибо."
    play sound ds_sfx_int
    rhe "Будь вежливым."
    play sound ds_sfx_psy
    aut "А также постарайся есть как можно аккуратнее – не чавкая, не роняя на себя кусочки еды и не обливаясь компотом."
    me "Так о чём ты хотела поговорить?"
    show mz smile glasses pioneer at center   with dspr
    mz "Сегодня у нас в библиотеке…"
    window hide
    menu:
        "Выслушать":
            window show
            th "Лучше выслушать, а не то пропущу что-нибудь ценное."
            mz "...после обеда будет уборка."
            mz "Сначала, до обеда, я буду протирать книги. Потом, после обеда и до ночи, я буду их сортировать."
            mz "Ты видел, сколько там книг. Мне одной не управиться, так что Ольга Дмитриевна сказала позвать тебя. Сказала, что ты не откажешь."
            play sound ds_sfx_psy
            aut "Твоего мнения тут уже никто не спрашивает."
            mz "Так что готовься. Дел у тебя всё равно никаких, я уверена."
            show mz sceptic glasses pioneer at center  with dspr
            mz "Да и если есть, Ольга Дмитриевна провозгласила день уборки, так что ты никуда не денешься."
            aut "А не слишком ли нагло? Она вожатой себя возомнила?"
            play sound ds_sfx_int
            rhe "Не-не-не, не вздумай так отвечать."
            play sound ds_sfx_mot
            com "Твои намерения выдаёт лишь недоуменный взгляд в её сторону."
            show mz normal glasses pioneer at center  with dspr
            mz "После обеда или после ужина. Лучше после обеда. Не забудь!"
            vol "Соглашаться не хочется. Но с другой стороны, если будешь открыто отлынивать, проблем не оберёшься."
            window hide
            menu:
                "Cогласиться безусловно":
                    window show
                    me "Конечно, не забуду и приду!"
                    $ ds_lp['mz'] += 1
                    "Женя кивает тебе и активнее принимается за еду."
                "Согласиться, но оставить путь для отступления":
                    window show
                    th "Как бы так ей ответить, чтобы и уступить, и чтобы потом можно было безнаказанно пропустить уборку?"
                    play sound ds_sfx_int
                    rhe "Да всё элементарно - у тебя же можешь {i}что-нибудь{/i} случиться? Может."
                    me "Если ничего не произойдёт, то приду."
                    "Женя кивает тебе и активнее принимается за еду."
                "Отказаться":
                    window show
                    me "Не пойду я в библиотеку! У меня уже есть другие задачи!"
                    show mz bukal glasses pioneer at center with dspr
                    mz "Да как скажешь! Найду другого кого-нибудь!"
            if skillcheck('rhetoric', lvl_trivial, passive=True):
                rhe "{result}Спроси её про год! Про что-нибудь!"
                window hide
                menu:
                    "Cпросить":
                        window show
                        $ ds_skill_points['rhetoric'] += 1
                        me "Слушай, а какой сейчас год, что-то совсем со счёта сбился?"
                        show mz sceptic glasses pioneer at center  with dspr
                        mz "Как будто ты не знаешь, какой сейчас год. Что ты мне глупые вопросы задаёшь."
                        me "Я бы не спрашивал, если бы знал."
                        show mz bukal glasses pioneer at center with dspr
                        mz "А ты не знаешь?"
                        me "Нет. У меня память плохая. Так какой сейчас год?"
                        "Ты мило улыбаешься."
                        show mz normal glasses pioneer at center  with dspr
                        mz "Не понимаю, куда ты клонишь."
                        mz "Можешь просто прибавить количество прожитых лет к году рождения. Если у тебя в этом году дня рождения ещё не было, то отними один."
                        th "Разве тебе не было бы проще ответить, какой год, чем всю эту тираду проговаривать?"
                        "Но ответила она правильно, так что перефразировать вопрос я не мог. Ладно, придумаем что-нибудь другое."
                        me "А ты случайно не знаешь, что у нас тут за речка протекает? Или это и не речка вовсе?"
                        "Градус недоумения накалялся."
                        $ renpy.pause(1)
                        show mz fun glasses pioneer at center with dspr
                        mz "Ты разговор так что ли хочешь поддержать?"
                        show mz bukal glasses pioneer at center  with dspr
                        mz "Обычно в такой ситуации задают другие вопросы. \"Как дела\", там, \"как настроение\",..."
                        "Бесполезно."
                        me "Ладно, тогда как у тебя дела?"
                        show mz sceptic glasses pioneer at center  with dspr
                        $ renpy.pause(2)
                        hide mz with dissolve
                        "Женя лишь покачала головой, допила компот и ушла."
                    "Не спрашивать":
                        window show
                        "Женя быстро доедает завтрак и уходит без комментариев."
                        th "Вот же... даже не попрощалась..."
            else:
                "Женя быстро доедает завтрак и уходит без комментариев."
                th "Вот же... даже не попрощалась..."
            window hide

            stop music fadeout 3

            $ renpy.pause(1)

            jump ds_day3_after_breakfast
        "Проигнорировать":
            window show
            $ ds_lp['mz'] -= 1
    play sound ds_sfx_psy
    ine "Дальше тебе вспоминились слова Ольги Дмитриевны о задачах на сегодня, так что дальше ты не слушаешь."
    mz "… не забудь!"
    window hide
    menu:
        "Переспросить":
            window show
            me "А? Чего?"
        "{check=logic:10}Восстановить просьбу Жени":
            if skillcheck('logic', lvl_medium, modifiers=[('ds_was_on_lineup', 2, 'Знаешь задачу Жени')]):
                window show
                play sound ds_sfx_int
                lgc "{result}Она, скорее всего, хочет, чтобы ты ей помог. В библиотеке. В рамках общественно-полезного труда, упомянутого вожатой утром."
                me "Да, я понял: нужно помочь тебе в библиотеке."
                show mz normal glasses pioneer at center with dspr
                mz "Отлично, тогда до встречи!"
                hide mz with dissolve
                me "Ладно..."
                hide mz with dissolve
                "Женя встаёт и направляется к выходу."
                if skillcheck('reaction_speed', lvl_trivial, passive=True):
                    play sound ds_sfx_mot
                    res "{result}Она же не доела!"
                    window hide
                    menu:
                        "Окликнуть":
                            window show
                            me "Подожди, ты же не доела…"
                            play sound ds_sfx_psy
                            emp "Но она, похоже, даже не собирается оборачиваться."
                        "Отпустить":
                            window show
                            th "Ну и пусть идёт!"
                jump ds_day3_breakfast_un
            else:
                window show
                play sound ds_sfx_int
                lgc "{result}Однако, у тебя не получается ничего подходящего придумать."
                $ ds_skill_points['logic'] += 1
                play sound ds_sfx_int
                dra "Более того, ваше выражение лица выдаёт, что вы не понимаете происходящего."
                show mz angry glasses pioneer at center with dspr
                mz "Ты не слушаешь!"
        "{check=drama:11}Притвориться, что понял":
            if skillcheck('drama', lvl_up_medium):
                window show
                play sound ds_sfx_int
                dra "{result}Вы, мессир, прекрасно всё поняли и уж точно ничего не забыли!"
                $ ds_skill_points['drama'] += 1
                me "Хорошо, я тебя понял."
                $ ds_accept_mz = True
                show mz normal glasses pioneer at center with dspr
                mz "Отлично, тогда до встречи!"
                hide mz with dissolve
                "Женя встаёт и направляется к выходу."
                if skillcheck('reaction_speed', lvl_trivial, passive=True):
                    play sound ds_sfx_mot
                    res "{result}Она же не доела!"
                    window hide
                    menu:
                        "Окликнуть":
                            window show
                            me "Подожди, ты же не доела…"
                            play sound ds_sfx_psy
                            emp "Но она, похоже, даже не собирается оборачиваться."
                        "Отпустить":
                            window show
                            th "Ну и пусть идёт!"
                res "А чего она, собственно, от тебя хотела?"
                jump ds_day3_breakfast_un
            else:
                window show
                play sound ds_sfx_int
                dra "{result}На вашем лице, мессир, всё написано, как в книге."
                $ ds_skill_points['drama'] += 1
                show mz angry glasses pioneer at center with dspr
                mz "Ты не слушаешь!"
                $ ds_lp['mz'] -= 1
    show mz normal glasses pioneer at center   with dspr
    mz "Говорю, не забудь после обеда прийти в библиотеку."
    me "Зачем?"
    show mz angry glasses pioneer at center   with dspr
    mz "Ты меня вообще слушал?"
    me "Нет."
    show mz rage glasses pioneer at center   with dspr
    "Женя сначала краснеет, потом, зеленеет, а потом её лицо принимает нежно-фиолетовый оттенок."
    mz "Сегодня! После обеда! В библиотеку! Понял, хунта проклятая?!"
    play sound ds_sfx_mot
    res "Хунта?{w} Это ещё что за матерное слово такое неведомое?"
    rhe "Пионер же не ругается, как ты мог забыть!"
    if skillcheck('encyclopedia', lvl_medium, passive=True):
        play sound ds_sfx_int
        enc "{result}Вообще, «хунта» - это группировка, обычно военная, захватившая власть насильственно."
        enc "Но на имиджбордах недовольство постом нередко выражали словом «х***а», записанном именно что в виде «XYNTA», читаемом «хунта». Мем ещё был такой, с Номадом."
        $ ds_skill_points['encyclopedia'] += 1
        play sound ds_sfx_psy
        aut "То есть, она выматерилась на тебя?!"
    window hide
    menu:
        "Мирно согласиться":
            window show
            me "Конечно, обязательно приду!"
            $ ds_accept_mz = True
            show mz normal glasses pioneer at center with dspr
            mz "Отлично, тогда до встречи!"
            hide mz with dissolve
            me "Ладно..."
        "Начать перепалку":
            window show
            me "Ты как меня назвала?!"
            show mz angry glasses pioneer at center with dspr
            mz "Как слышал! После завтрака в библиотеку!"
            play sound ds_sfx_psy
            aut "Чего это она вздумала тобой командовать?! Непорядок!"
            me "Никуда я не пойду! Сама разбирайся со своей библиотекой!"
            mz "Значит, так?! Да я вожатой расскажу, как ты отлыниваешь от общественной работы!"
            play sound ds_sfx_int
            rhe "Вообще говоря, никто не сказал, что ты обязан именно в библиотеке отбывать трудовую повинность!"
            me "А причём тут библиотека? Я не отказываюсь от работы, я лишь требую уважения к себе!"
            show mz rage glasses pioneer at center with dspr
            mz "Ах ты так?! Не нужна мне твоя помощь, попрошу других мужчин!"
            hide mz with dissolve
            $ ds_lp['mz'] -= 1
        "Докопаться до «хунты»":
            window show
            me "Какая такая хунта?! Причём тут я?!"
            mz "Притом! Не слушаешь меня совсем! Полное неуважение!"
            rhe "По всей видимости, она использует это слово как ругательство, не вникая в смысл."
            rhe "Примерно так же обсценную лексику используют, не вспоминая, что они связаны с половым актом."
            me "Нет, всё-таки, хунта-то тут причём? Ты вообще знаешь, что это значит?"
            show mz angry glasses pioneer at center with dspr
            mz "Да что ты прицепился?!"
            mz "Назвала и назвала? По сути ответить нечего?!"
            me "Мне как бы неприятно, что ты меня оскорбляешь."
            mz "Ладно, я поняла... попрошу кого-нибудь другого!"
            hide mz with dissolve
        "Спросить про год" if ds_knowing == 0:
            window show
            if skillcheck('rhetoric', lvl_easy, passive=True):
                rhe "{result}Согласись с ней, а затем спроси"
                me "Ах, да, конечно! Извини! Обязательно приду!"
                $ ds_skill_points['rhetoric'] += 1
            me "Слушай, а какой сейчас год, что-то совсем со счёта сбился?"
            rhe "Ты решаешь играть в открытую."
            show mz bukal glasses pioneer at center   with dspr
            "Она недоуменно смотрит на тебя."
            mz "Совсем, что ли, крыша поехала?"
            me "Признаться, последние несколько дней есть такое подозрение."
            "Женя ничего не отвечает."
            me "Так год какой?"
            "Ты мило улыбаешься."
            show mz normal glasses pioneer at center   with dspr
            mz "Слушай, может, тебе в медпункт сходить?"
            me "А там мне подскажут, какой год?"
            show mz bukal glasses pioneer at center   with dspr
            mz "И не только это подскажут!"
            hide mz  with dissolve
    "Женя встаёт и направляется к выходу."
    if skillcheck('reaction_speed', lvl_trivial, passive=True):
        play sound ds_sfx_mot
        res "{result}Она же не доела!"
        window hide
        menu:
            "Окликнуть":
                window show
                me "Подожди, ты же не доела…"
                play sound ds_sfx_psy
                emp "Но она, похоже, даже не собирается оборачиваться."
            "Отпустить":
                window show
                th "Ну и пусть идёт!"
    window hide

    stop music fadeout 3

    $ renpy.pause(1)

    jump ds_day3_after_breakfast

label ds_day3_breakfast_un:
    window show
    show mz bukal glasses pioneer at center   with dspr
    mz "Подожди-ка! Успеешь ещё!"
    me "Извини, давай потом."
    hide mz  with dissolve
    "Ты аккуратно освобождаешь свой рукав от её руки и направлаешься в дальний конец столовой."
    "Женя что-то кричит тебе вслед, но ты её не слушаешь."
    $ ds_lp['mz'] -= 1
    show un normal pioneer at center   with dissolve
    me "Привет, доброе утро!"
    play sound ds_sfx_mot
    com "Лена, услышав крики библиотекарши, уже некоторое время украдкой поглядывает на тебя."
    show un smile pioneer at center   with dspr
    un "Доброе…"
    com "Как ни странно, она не краснеет, а даже улыбается."
    me "Можно к тебе присесть? Я сейчас сбегаю за завтраком."
    un "Да, конечно."
    hide un  with dissolve
    window hide

    $ renpy.pause(0.5)
    window show
    show ck normal at center with dspr
    ck "Доброе утро, пионер!"
    play sound ds_sfx_psy
    sug "К сожалению, брать для Лены завтрак неактуально."
    "Повариха выдаёт тебе завтрак."
    hide ck with dissolve
    "Ты возвращаешься к Лене."
    window hide
    $ renpy.pause(0.5)

    show un normal pioneer at center   with dspr
    window show
    "Через минуту ты уже сидишь напротив неё с нехитрым набором блюд на подносе: каша овсяная, два яйца варёных, хлеб белый, четыре куска, сосиска варёная, одна штука, компот из непонятного набора фруктов и ягод, один стакан."
    window hide
    menu:
        "Пожелать приятного аппетита":
            window show
            me "Приятного аппетита!"
            show un smile pioneer at center   with dspr
            un "Спасибо."
            $ ds_lp['un'] += 1
        "Промолчать":
            window show
    "Ты стараешься есть как можно аккуратнее – не чавкая, не роняя на себя кусочки еды и не обливаясь компотом."
    th "Ведь можно же, если захотеть, есть как человек, а не как оголодавший боров!"
    play sound ds_sfx_int
    rhe "Лена, как обычно, молчит, а значит, начинать разговор придётся тебе."
    window hide
    menu:
        "{check=rhetoric:8}Заговорить с Леной":
            if skillcheck('rhetoric', lvl_easy, modifiers=[('ds_was_on_lineup', 1, 'Знаешь о танцах')]):
                window show
                rhe "{result}Танцы! Сегодня танцы! Поговори о них."
                $ ds_skill_points['rhetoric'] += 1
            else:
                window show
                rhe "{result}Тебе не приходит в голову никаких тем для разговора."
                $ ds_skill_points['rhetoric'] += 1
                "Поэтому вы молча доедаете завтрак и расходитесь."
                hide un with dissolve
                window hide

                $ renpy.pause (1)

                jump ds_day3_after_breakfast
        "Поесть молча":
            window show
            th "Что-то не хочется мне с ней разговаривать..."
            "Вы сидите молча, пока не съедаете завтрак. После чего расходитесь."
            hide un with dissolve
            window hide

            $ renpy.pause (1)

            jump ds_day3_after_breakfast
    me "Пойдёшь сегодня на танцы?"
    show un normal pioneer at center   with dspr
    un "Да, наверное…"
    "Она делает небольшую паузу."
    un "А ты?"
    if skillcheck('suggestion', lvl_easy, passive=True):
        play sound ds_sfx_psy
        sug "{result}Ты склонишь её к себе (ещё больше), если скажешь, что пойдёшь только с ней."
    window hide
    menu:
        "Иду на танцы":
            window show
            me "Конечно же иду!"
            show un smile pioneer at center with dspr
            un "Хорошо."
            window hide
            menu:
                "{check=suggestion:12}Пригласить Лену":
                    if skillcheck('suggestion', lvl_challenging):
                        window show
                        play sound ds_sfx_psy
                        sug "{result}Скажи, что она выглядит прекрасно, и что ты хочешь видеть её на танцах."
                        me "Ты так прекрасно выглядишь, кстати... тебе обязательно нужно прийти на танцы!"
                        show un shy pioneer at center with dspr
                        un "Хорошо... спасибо..."
                        $ ds_lp['un'] += 1
                        $ ds_skill_points['suggestion'] += 1
                    else:
                        window show
                        play sound ds_sfx_psy
                        sug "{result}Вперёд, приглашай!"
                        me "Тебе обязательно нужно прийти! И потанцевать! Со мной!"
                        show un scared pioneer at center with dspr
                        un "Э... а... наверное..."
                        un "Зачем так грубо только?.. Я и так собиралась пойти..."
                        sug "Похоже, ты её отпугнул. Не так резко же надо было приглашать."
                        $ ds_skill_points['suggestion'] += 1
                "Не приглашать":
                    window show
        "Не иду на танцы":
            window show
            me "Да ну, зачем мне эти танцы?"
            show un surprise pioneer at center with dspr
            un "Ну как же, явка туда обязательна..."
            $ ds_karma -= 5
            me "Скажу, что дела, вот и всё!"
            if ds_us_escape:
                th "Или вообще к тому времени сбегу!"
            show un normal pioneer at center with dspr
            un "Ну, как скажешь..."
        "Пойду только с тобой" if ds_last_skillcheck.result:
            window show
            me "Ну не знаю..."
            me "Если, конечно, ты меня приглашаешь..."
            show un shy pioneer at center   with dspr
            "Лена краснеет и отводит взгляд."
            un "Ну, я не знаю насчёт..."
            window hide
            menu:
                "Сделать вид, будто пошутил":
                    window show
                    me "Извини, это была шутка."
                    play sound ds_sfx_psy
                    emp "Наверное, не стоило так {i}шутить{/i}."
                "Подтвердить серьёзность":
                    window show
                    me "Да ладно тебе!"
            un "Хорошо."
            $ ds_lp['un'] += 2
            $ ds_skill_points['suggestion'] += 1
            $ ds_promise_un = True
            "Безучастно произносит она и смотрит к себе в тарелку, продолжая всё больше краснеть."
        "Ответить неопределённо":
            window show
            me "Не знаю ещё…"
            "Хотя идти мне совершенно не хотелось."
            "Я и в школе не любил дискотеки, а уж в более сознательном возрасте…"
            show un surprise pioneer at center   with dspr
            un "А почему?"
            me "Что почему?"
            un "Почему не хочешь идти?"
            window hide
            menu:
                "Нет желания":
                    window show
                    me "Я же не сказал, что не хочу…"
                    show un normal pioneer at center   with dspr
                    un "Ну, ладно тогда."
                "Есть дела":
                    window show
                    me "Ну, у меня дела..."
                    show un normal pioneer at center   with dspr
                    un "Ну, ладно тогда."
                "Решил пойти":
                    me "Я не сказал, что не пойду. На самом деле я решил пойти туда..."
                    show un smile pioneer at center with dspr
                    un "Хорошо..."
    window hide
    menu:
        "Спросить про Женю":
            window show
            me "А ты не знаешь, что Женя хотела?"
            show un normal pioneer at center   with dspr
            un "А?"
            me "Ну, я когда в столовую зашёл, она... ну, что-то хотела от меня."
            un "Не знаю..."
            me "Ясно."
            rhe "Разговор явно зашёл в тупик"
            com "Ты стараешься сделать вид, что полностью сосредоточен на еде."
        "Не спрашивать":
            pass
    window hide

    with fade

    window show
    "Лена закончила завтрак быстрее меня."
    show un smile2 pioneer at center   with dspr
    un "Ладно, я пойду. Увидимся!"
    me "Да, пока!"
    hide un  with dissolve
    window hide

    $ renpy.pause (1)

    jump ds_day3_after_breakfast

label ds_day3_after_breakfast:
    window show
    play sound ds_sfx_mot
    per_tas "Ты дожёвываешь сосиску, которая больше напоминает кусок витой пары."

    stop ambience fadeout 2

    th "С едой покончено – самое время отправиться на поиски разгадок."
    window hide

    if ds_us_escape:
        $ persistent.sprite_time = "day"
        scene bg ext_dining_hall_near_day
        show us laugh2 sport at center
        with dissolve

        "Прямо возле крыльца тебя перехватывает Ульяна."
        us "Бу!"
        me "Привет-привет..."
        show us grin sport at center with dspr
        us "Ты не забыл о наших планах на сегодня?"
        window hide
        menu:
            "Вспомнить самому":
                window show
                me "Да, помню, побег..."
            "Попросить напомнить":
                window show
                me "Напомни, пожалуйста?"
                show us dontlike sport at center with dspr
                us "Как так, уже забыл... сбежать мы хотели!"
                me "А, точно."
        show us normal sport at center with dspr
        us "Ну чего, пойдём?"
        if ds_us_betray:
            play music music_list['you_lost_me'] fadein 2
            show mt rage pioneer far at right with dissolve
            mt "И никуда ты не пойдёшь, Советова!"
            show us supr3 sport at center with dspr
            us "А... что я?"
            show mt rage pioneer at right with dspr
            mt "Да знаю я, что ты побег задумала! Не вышло!"
            show us angry sport at center with dspr
            us "Ах ты предатель! Не буду больше с тобой дружить!"
            $ ds_lp['us'] *= -1
            mt "Семён - послушный пионер, не то, что ты!"
            mt "Идём, сегодня дежурить в столовой будешь!"
            hide us
            hide mt
            with dissolve
            stop music fadeout 2
            "А ты идёшь своей дорогой."
        else:
            window hide
            menu:
                "Пойти":
                    window show
                    me "Да, идём!"
                    show us smile sport at center with dspr
                    us "Отлично! За мной!"
                    $ ds_lp['us'] += 1
                    jump ds_day3_escape
                "Отказаться":
                    window show
                    me "Знаешь, я подумал, что лучше будет не сбегать..."
                    show us dontlike sport at center with dspr
                    us "Вот как? Да ты трус просто! Сама убегу, без тебя!"
                    $ ds_lp['us'] -= 1
                    $ ds_damage_morale()
                    us "Счастливо оставаться!"
                    hide us with dissolve
                    "И она убегает быстрее, чем ты успеваешь что-нибудь вставить."
                    "И ты просто идёшь своей дорогой."

    $ persistent.sprite_time = "day"
    scene bg ext_aidpost_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "Через некоторое время ты выходишь к медпункту."
    th "Там мне уж точно делать нечего."
    play sound ds_sfx_fys
    hfl "Хоть медсестра и кажется весьма доброжелательной, лучше держаться от неё подальше."
    hfl "Такая доброжелательность скорее пугает!"
    play sound ds_sfx_psy
    vol "Возможно, она что-то и знает, но ты не решаешься вот так запросто взять и зайти в медпункт."
    vol "Тем более нет никакого повода.{w} Даже самого малюсенького."
    play sound ds_sfx_fys
    ins "Да ладно тебе, она же такая привлекательная!"
    "Погружённый в свои мысли, ты не замечаешь медсестру, стоящую на крыльце."

    play music music_list["eternal_longing"] fadein 5

    show cs normal far at center   with dissolve
    cs "Привет… пионер!"
    show cs normal at center   with dissolve
    "Она подходит ближе."
    cs "Никак заболел, подлечиться пришёл?"
    me "Да нет… я… гулял просто…"
    show cs smile at center   with dspr
    cs "Понятно всё с тобой, прогульщик."
    show cs normal at center   with dspr
    cs "Ну, раз уж пришёл, у меня для тебя есть ответственное поручение."
    "Ты вопросительно смотришь на неё."
    com "От слова «поручение» тебе становится не по себе – уж слишком добровольно-принудительно оно звучит."
    show cs smile at center   with dspr
    "Медсестра ехидно улыбается."
    cs "Вы мне поможете составить опись лекарств, которые сегодня привезли."
    play sound ds_sfx_mot
    res "Мы?{w} Кто мы?{w} Неужели она решила, что недостаточно вежлива со мной?"

    stop music fadeout 3

    th "Хотя куда уж вежливее…"
    show un normal pioneer at left   with dissolve
    un "Привет…"

    "Из-за спины медсестры выглядывает Лена."
    play sound ds_sfx_mot
    per_eye "Странно, что ты её не заметил."
    show cs normal at center   with dspr
    cs "После ужина приходите сюда, я Лене всё объяснила, она тебе потом расскажет."
    res "Лекарства, значит? Привезли сегодня?"
    res "Но, по словам Ольги Дмитриевны, автобуса не будет ещё несколько дней."
    me "Получается, сегодня кто-то приезжал в лагерь?"
    cs "Да, с утра из райцентра, а что?"
    me "Нет, ничего, просто…"
    show cs smile at center   with dspr
    cs "Вот и славно… пионер!{w} Значит, вечером, после ужина, сразу сюда!"
    un "Может быть, я…"
    "Всё это время ты совсем не замечал Лену."
    play sound ds_sfx_int
    con "Действительно, её навыкам маскировки позавидовал бы и опытный спецназовец."
    show un shy pioneer at left   with dspr
    un "Я и одна могла бы справиться."

    show cs normal at center   with dspr
    cs "Там много – несколько коробок, ты что!"
    cs "Тем более пионер всегда готов!"
    show cs shy at center   with dspr
    cs "Так... пионер?"
    "Она смотрит на меня и как-то не по-доброму улыбается."
    vol "Тратить весь вечер на подобную работу тебе совсем не хочется, тем более есть дела и поважнее."
    vol "Но и отказываться вроде как неудобно."
    play sound ds_sfx_mot
    com "Хотя, не будь здесь Лены, ты бы что-нибудь обязательно придумал."

    window hide
    menu:
        "Согласиться":
            $ ds_lp['un'] += 1
            $ ds_lp['cs'] += 1
            $ ds_karma += 10
            $ ds_to_help_un = True
            window show
            me "Хорошо, я приду!"
            show cs smile at center with dspr
            cs "Так и должен отвечать пионер!"
            cs "А теперь я пойду."
            play sound ds_sfx_psy
            vol "Не обольщайся: больше лозунгу «Всегда готов!» ты соотвествовать не стал."
            cs "Тогда можете идти."

            stop ambience fadeout 2

            play music music_list["timid_girl"] fadein 5

            hide cs  with dissolve
            show un shy pioneer at left :
                linear 1.0 xalign 0.5
            "Ты переводишь взгляд на Лену, которая всё так же смотрит себе под ноги."
            play sound ds_sfx_psy
            ine "Наверное, за всё время, что она разглядывает землю, можно неплохо изучить жизнь и повадки различных насекомых."
            ine "Прибавить к этому, что Лена любит читать, и наверняка прочитала много книг по биологии, ботанике и т.д."
            play sound ds_sfx_int
            lgc "Может, она хочет стать энтомологом?"
            window hide

            with fade2

            $ persistent.sprite_time = "day"
            scene bg ext_square_day 
            with dissolve

            show un normal pioneer at center   with dissolve
            window show
            un "А куда ты дальше?"
            "Слова Лены отвлекают тебя от этих непонятных мыслей."
            "Вы уже давно просто стоите на площади"
            vol "А твои размышления о жизни жуков – всего лишь повод отвлечься от неловкой ситуации."
            th "Впрочем, что здесь неловкого?"
            un "Только ты не забудь, хорошо?"
            me "Не забыть чего?"
            show un serious pioneer at center   with dspr
            un "Ну, как же… Вечером, после ужина… В медпункт…"
            "На её лице мелькает тень недовольства."
            th "Да нет, не может такого быть!"
            me "Конечно, конечно! Сразу после ужина я весь в твоём распоряжении."
            show un shy pioneer at center   with dspr
            play sound ds_sfx_psy
            emp "Уже поздно – после этих слов Лена ещё больше покраснела."
            emp "Надо срочно как-то разрядить создавшееся напряжение."
            me "А почему медсестра именно тебя попросила?"
            show un normal pioneer at center   with dspr
            un "Не знаю.{w} Я просто сидела на лавочке, читала книжку, а она подошла и…"
            play sound ds_sfx_psy
            aut "Как умно с её стороны обратиться к человеку, который точно не откажет!"
            me "Ясно.{w} Ладно, тогда после ужина…"
            show un smile pioneer at center   with dspr
            un "Хорошо.{w} Я пойду тогда?"
            me "Да, конечно!"
            hide un  with dissolve

            stop music fadeout 3

            "Она направляется куда-то в сторону кружков, а ты ещё некоторое время просто стоишь на площади."
        "{check=drama:12}Сослаться на помощь Ольге Дмитриевне":
            if skillcheck('drama', lvl_challenging):
                play sound ds_sfx_int
                dra "{result}Ты выполняешь очень ответственное поручение для Ольги Дмитриевны! Помогаешь ей разобрать документы пионеров, скажем."
                me "Знаете, мне надо с Ольгой Дмитриевной документы разбирать."
                me "Ну, типа в ком..."
                play sound ds_sfx_int
                rhe "Тут нет компьютеров, тут ЭВМ!"
                me "В ЭВМ занести, я же типа мужчина, лучше разбираюсь!"
                show cs normal at center with dspr
                cs "Вот как... ну ладно, как скажешь."
                $ ds_lp['un'] -= 1
                me "Ты извини, просто, понимаешь…"
                "Лена стоит, всё так же уставившись куда-то себе под ноги, и краснеет, краснеет всё больше."
                un "Да ничего… Я сама…"
                me "Ну, ладно тогда."
                "Воцарилось неловкое молчание."
                vol "Хочется сквозь землю провалиться из-за вранья, из-за того, что наверняка обидел Лену."
                un "Ну, пока тогда?"
                me "Пока!"
                hide cs 
                hide un 
                with dissolve
                "Ты разворачиваешься и быстро направляешься прочь от медпункта."

                stop music fadeout 3

                play sound ds_sfx_mot
                com "Хотя тебе безумно хочется перейти на бег, стоит идти обычным шагом."
                window hide

                $ persistent.sprite_time = "day"
                scene bg ext_square_day 
                with dissolve

                window show
                com "Немного прийти в себя ты смог только на площади."
            else:
                play music music_list["you_won_t_let_me_down"] fadein 5

                window show
                play sound ds_sfx_int
                dra "{result}Врать тут вряд ли стоит."
                dra "И вообще, чем ты можешь помочь Ольге Дмитриевне вечером?"
                me "Знаете, меня тут Ольга Дмитриевна просила помочь..."
                show cs normal at center   with dspr
                cs "Да? И чем это ты собрался ей помогать?"
                dra "Дело принимает неприятный для тебя оборот."
                vol "Но ты решаешь идти до конца."
                me "У неё в домике…{w} В домике уборку сделать, вещи разобрать и всё такое."
                me "Вы же знаете, какой у неё там бардак!"
                show cs smile at center   with dspr
                cs "Небось и шкафчик свой попросила разобрать?"
                play sound ds_sfx_psy
                aut "Медсестра смотрит на тебя так, что фиаско Наполеона при Ватерлоо кажется всего лишь досадной неприятностью по сравнению с твоим нынешним поражением."
                $ ds_damage_morale()
                "Ты уже было собрался что-то ответить, но она продолжает."
                show cs normal at center   with dspr
                cs "Ладно уж… пионер.{w} Без тебя разберёмся."
                $ ds_karma -= 10
                $ ds_lp['un'] -= 1
                $ ds_lp['cs'] -= 1
                me "Ты извини, просто, понимаешь…"
                "Лена стоит, всё так же уставившись куда-то себе под ноги, и краснеет, краснеет всё больше."
                un "Да ничего… Я сама…"
                me "Ну, ладно тогда."
                "Воцарилось неловкое молчание."
                vol "Хочется сквозь землю провалиться из-за неудавшегося вранья, из-за того, что наверняка обидел Лену."
                un "Ну, пока тогда?"
                me "Пока!"
                "Медсестра всё так же ехидно улыбается."
                hide cs 
                hide un 
                with dissolve
                "Ты разворачиваешься и быстро направляешься прочь от медпункта."

                stop music fadeout 3

                play sound ds_sfx_mot
                com "Хотя тебе безумно хочется перейти на бег, стоит идти обычным шагом."
                window hide

                $ persistent.sprite_time = "day"
                scene bg ext_square_day 
                with dissolve

                window show
                com "Немного прийти в себя ты смог только на площади."
            $ ds_skill_points['drama'] += 1
        "Отказать":
            window show
            me "Знаете... не хочу я сидеть с лекарствами и бумажками!"
            show cs normal at center   with dspr
            cs "Ладно уж… пионер.{w} Без тебя разберёмся."
            $ ds_karma -= 10
            $ ds_lp['un'] -= 2
            $ ds_lp['cs'] -= 1
            me "Ты извини, просто, понимаешь…"
            "Лена стоит, всё так же уставившись куда-то себе под ноги, и краснеет, краснеет всё больше."
            un "Да ничего… Я сама…"
            me "Ну, ладно тогда."
            "Воцарилось неловкое молчание."
            vol "Хочется сквозь землю провалиться из-за неудавшегося вранья, из-за того, что наверняка обидел Лену."
            un "Ну, пока тогда?"
            me "Пока!"
            "Медсестра всё так же ехидно улыбается."
            hide cs 
            hide un 
            with dissolve
            "Ты разворачиваешься и быстро направляешься прочь от медпункта."

            stop music fadeout 3

            play sound ds_sfx_mot
            com "Хотя тебе безумно хочется перейти на бег, стоит идти обычным шагом."
            window hide

            $ persistent.sprite_time = "day"
            scene bg ext_square_day 
            with dissolve

            window show
            com "Немного прийти в себя ты смог только на площади."
    th "И что дальше?"
    play sound ds_sfx_psy
    vol "Зайди домой, забери мобильник."
    vol "Неизвестно, куда тебя ещё сегодня занесёт, а время знать нужно всегда!"
    play sound ds_sfx_int
    lgc "Хотя не проще ли завести часы?"

    python:
        d3_volume = _preferences.volumes['music']
        volume(0.15,"music")

    play music music_list["kostry"] fadein 3

    play sound ds_sfx_mot
    per_hea "В обычный фоновый шум пионерлагеря закралась какая-то новая мелодия."
    per_hea "Похоже на электрогитару."
    per_hea "Три повторяющихся аккорда, не более того."
    per_hea "Однако эта мелодия кажется какой-то тёплой, словно пропущенной через ламповый усилитель."
    play sound ds_sfx_mot
    res "Хотя откуда тут такая роскошь?"
    per_hea "Звуки доносятся, очевидно, со стороны сцены."
    th "Интересно, кто бы это мог быть?"
    if skillcheck('logic', lvl_up_medium, passive=True, modifiers=[('ds_was_on_lineup', 1, 'Знаешь, что Алиса на сцене')]):
        play sound ds_sfx_int
        lgc "{result}Так ведь Алиса вроде как играет на гитаре... скорее всего, это она."
    window hide

    stop ambience fadeout 2

    menu:
        "Пойти посмотреть":
            $ ds_lp['dv'] += 1
            jump ds_day3_stage_dv
        "Не обращать внимания":
            window show
            th "И пусть себе играет, мне сейчас не до этого."
            window hide
            stop music fadeout 2
            jump ds_day3_house_mt

label ds_day3_escape:
    $ ds_whom_helped = 'esc'
    $ persistent.sprite_time = 'day'
    scene bg ds_ext_backdoor_day
    with dissolve

    show us normal sport at center with dissolve
    "Вы тихонько выбираетесь из лагеря через задний ход."
    play sound ds_sfx_mot
    svf "Никакого наблюдения тут не ведётся (наверное), так что трудностей это не вызывает."

    scene bg ds_ext_backroad_day
    with dissolve

    show us normal sport at center with dissolve
    "Вы вышли из лагеря."
    us "Идём туда! К железной дороге!"
    play sound ds_sfx_int
    lgc "По всей видимости, она хочет уехать на поезде."
    me "Идём... тебе виднее..."
    show us smile sport at center with dspr
    us "То-то же!"

    window hide
    $ renpy.pause(1.0)

    scene bg ds_ext_railroad_day
    with dissolve
    window show

    show us normal sport at left with dissolve
    "Долго ли, коротко ли, но вы наконец подходите к железнодорожному мосту."
    play sound ds_train_horn
    "И как раз вовремя - к вам приближается поезд."
    play sound2 ds_train
    show us grin sport at left with dspr
    us "Готов? {w}Прыгай!"

    scene cg ds_day3_train
    with dissolve
    "Ульяна срывается с места и бежит навстречу поезду."
    "Она прыгает и зацепляется за очередной проходящий вагон."
    window hide
    menu:
        "{check=savoir_faire:13}Запрыгнуть":
            if skillcheck('savoir_faire', lvl_formidable):
                window show
                play sound ds_sfx_mot
                svf "{result}Ты с лёгкостью прыгаешь и цепляешься за тот же вагон, что и Ульяна."
                svf "После этого вы забираетесь внутрь."
                $ ds_skill_points['savoir_faire'] += 1
                $ ds_lp['us'] += 1
                jump ds_day3_us_escaped
            else:
                window show
                play sound ds_sfx_mot
                svf "{result}Ты пытаешься зацепиться за вагон... но срываешься и падаешь!"
                play sound ds_fall
                $ ds_damage_health()

                scene bg ds_ext_railroad_day
                with dissolve
                "Проезжает последний вагон..."
                stop sound2 fadeout 5
                play sound ds_sfx_mot
                res "И Ульянка уехала одна!"
                us "А-а-а-а..."
                play sound ds_sfx_psy
                emp "Она напугана таким исходом."

                show mt scared pioneer at center
                show dv scared pioneer2 at right
                show sl scared pioneer at left
                with dissolve
                play sound ds_sfx_fys
                hfl "Час от часу не легче... готовься к мучительной казни..."
                mt "ГДЕ УЛЬЯНА?!"
                me "Она уехала на поезде... я не смог её остановить, извините..."
                mt "Это п****ц... и да, никто из вас этого не слышал!"
                show dv surprise pioneer2 at right with dspr
                play sound ds_sfx_mot
                res "Кто бы мог подумать, что Ольга Дмитриевна тоже умеет материться..."
                mt "Это конец... наш лагерь закроют, а нас всех накажут!"
                show mt sad pioneer at center
                show dv sad pioneer2 at right
                show sl upset pioneer at left
                with dspr
                mt "Ладно, идём сдаваться..."
                "И вы идёте в сторону лагеря."
                scene black with dissolve2
                jump ds_end_us_gone
        "{check=reaction_speed:14}Снять Ульяну":
            if skillcheck('reaction_speed', lvl_legendary):
                window show
                play sound ds_sfx_mot
                res "{result}Ты успеваешь метнуться к вагону как раз вовремя и сорвать с него Ульяну."
                play sound ds_fall
                $ ds_skill_points['reaction_speed'] += 1

                scene bg ds_ext_railroad_day
                with dissolve
                "Проезжает последний вагон..."
                stop sound2 fadeout 5
                show us dontlike sport at center with dissolve
                us "Что ты наделал?!"
                me "Cбегать - идея очень глупая... всё равно поймают и накажут."
                us "Какой ты скучный..."
                $ ds_lp['us'] -= 1

                show mt scared pioneer at center
                show dv scared pioneer2 at right
                show sl scared pioneer at left
                show us surp1 sport close at cleft
                with dissolve
                play sound ds_sfx_fys
                hfl "Час от часу не легче... готовься к мучительной казни..."
                show mt rage pioneer at center with dspr
                mt "Советова! Что ты творишь?!"
                us "Ой... я просто пошутить хотела..."
                mt "Ты вообще чем думаешь?! Ты понимаешь, чем твоя «шутка» могла обернуться для всех нас?!"
                mt "А ты, Семён?! Почему не остановил?!"
                me "Вообще-то, я как раз её и снял..."
                show mt surprise pioneer at center with dspr
                mt "Ну ладно... в какой-то степени ты молодец..."
                show mt angry pioneer at center with dspr
                mt "Но ты, по-видимому, знал о планах Советовой! И не сказал!"
                $ ds_karma -= 20
                mt "Так, ладно, идём обедать! Точнее, не так - Советова и Пёрсунов идёт дежурить в столовой, а все остальные - обедать!"
                me "Но Ольга Дмитриевна..."
                mt "Никаких «но»! Я всё сказала! Уму непостижимо!"
                "И вы возвращаетесь в лагерь."
                show dv normal pioneer2 close at right with dspr
                "Но перед этим Алиса подбегает к тебе и говорит шёпотом."
                dv "Cпасибо, что вернул мою подругу!"
                window hide

                scene bg ds_ext_backroad_day
                with dissolve

                $ renpy.pause(0.5)

                scene bg ds_ext_backdoor_day
                with dissolve

                $ renpy.pause(0.5)

                scene bd ext_square_day
                with dissolve

                show mt angry pioneer at center
                show dv normal pioneer2 at right
                show sl angry pioneer at left
                show us sad sport at cleft
                with dissolve

                mt "Так, Советова и Пёрсунов, марш в столовую!"
                mt "Как раз обед уже закончился, вам надо будет убрать!"
                jump ds_day3_punishment2
            else:
                window show
                play sound ds_sfx_mot
                svf "{result}Ты пытаешься схватить Ульяну... но поезд оказывается быстрее, и он увозит её."

                scene bg ds_ext_railroad_day
                with dissolve
                "Проезжает последний вагон..."
                stop sound2 fadeout 5
                play sound ds_sfx_mot
                res "И Ульянка уехала одна!"
                us "А-а-а-а..."
                play sound ds_sfx_psy
                emp "Она напугана таким исходом."

                show mt scared pioneer at center
                show dv scared pioneer2 at right
                show sl scared pioneer at left
                with dissolve
                play sound ds_sfx_fys
                hfl "Час от часу не легче... готовься к мучительной казни..."
                mt "ГДЕ УЛЬЯНА?!"
                me "Она уехала на поезде... я не смог её остановить, извините..."
                mt "Это п****ц... и да, никто из вас этого не слышал!"
                show dv surprise pioneer2 at right with dspr
                play sound ds_sfx_mot
                res "Кто бы мог подумать, что Ольга Дмитриевна тоже умеет материться..."
                mt "Это конец... наш лагерь закроют, а нас всех накажут!"
                show mt sad pioneer at center
                show dv sad pioneer2 at right
                show sl upset pioneer at left
                with dspr
                mt "Ладно, идём сдаваться..."
                "И вы идёте в сторону лагеря."
                scene black with dissolve2
                jump ds_end_us_gone
        "Ничего не делать":
            window show

            scene bg ds_ext_railroad_day
            with dissolve
            "Проезжает последний вагон..."
            stop sound2 fadeout 5
            play sound ds_sfx_mot
            res "И Ульянка уехала одна!"
            us "А-а-а-а..."
            play sound ds_sfx_psy
            emp "Она напугана таким исходом."

            show mt scared pioneer at center
            show dv scared pioneer2 at right
            show sl scared pioneer at left
            with dissolve
            play sound ds_sfx_fys
            hfl "Час от часу не легче... готовься к мучительной казни..."
            mt "ГДЕ УЛЬЯНА?!"
            me "Она уехала на поезде... я не смог её остановить, извините..."
            mt "Это п****ц... и да, никто из вас этого не слышал!"
            show dv surprise pioneer2 at right with dspr
            play sound ds_sfx_mot
            res "Кто бы мог подумать, что Ольга Дмитриевна тоже умеет материться..."
            mt "Это конец... наш лагерь закроют, а нас всех накажут!"
            show mt sad pioneer at center
            show dv sad pioneer2 at right
            show sl upset pioneer at left
            with dspr
            mt "Ладно, идём сдаваться..."
            "И вы идёте в сторону лагеря."
            scene black with dissolve2
            jump ds_end_us_gone

label ds_day3_us_escaped:
    scene bg ds_int_train
    show us grin sport at center
    with dissolve

    play ambience ds_ambience_train

    us "Ура! Ура! Получилось!"
    me "И куда мы теперь поедем?"
    us "А пока поезд не остановится!"
    me "Ладно... а потом куда?"
    us "Что ты такой зануда? Посмотрим!"
    me "Ну... как скажешь..."

    play sound ds_sfx_fys
    edr "От покачивания поезда тебя укачивает, и ты засыпаешь."
    stop ambience fadeout 5
    show blink
    scene black
    window hide
    $ renpy.pause(5.0)
    window show
    hide blink
    show unblink

    $ ds_restore_health()
    $ ds_restore_morale()

    scene bg ds_int_train
    show us normal sport at center
    us "Просыпайся, мы приехали!"
    me "Уже?"
    us "Ну да! Выходим!"

    scene bg ds_ext_train
    show us normal sport at center
    with dissolve
    "Вы вылазите из вагона и сбегаете с вокзала."
    "Никого поблизости не видно, так что вас никто и ничто не задерживает."

    scene bg ds_ext_bus_town
    with dissolve
    "Около станции оказывается автобусная остановка. При ней - автобус."
    show us smile sport at center
    with dissolve
    us "О, садимся туда!"
    window hide
    menu:
        "Cесть в автобус":
            window show
        "Не садиться":
            window show
            me "Нет, нас так поймают. Лучше пойдём в лес, будем как отшельники жить!"
            show us laugh sport at center
            with dspr
            us "Давай! Давай!"
            jump ds_end_escape_with_us
    scene bg int_bus
    with dissolve
    show us normal sport at center with dissolve
    "Вы с Ульяной садитесь в автобус."
    play sound_loop sfx_bus_interior_moving
    "Тут же автобус закрыл двери и тронулся с места."
    show us grin sport at center with dissolve
    us "Давай, пока едем, в города!"
    me "Давай..."
    us "Москва!"
    me "Архангельск..."
    us "Калинин!"
    play sound ds_sfx_int
    enc "Так в Советском Союзе называется Тверь."
    me "Новгород..."
    window hide
    $ renpy.pause(3.0)
    $ persistent.sprite_time = 'sunset'
    scene bg ds_int_bus_sunset with dspr
    window show
    stop sound_loop
    "Так проходит время, и тут автобус останавливается."
    show us smile sport at center with dissolve
    us "Приехали! Приехали! И куда же мы приехали?"
    play sound ds_sfx_mot
    per_eye "В окне ты видишь знакомую надпись... {w}Это «Совёнок»!"
    "Ты хотел было сказать об этом Ульяне..."
    show mt rage pioneer at center with dissolve
    show us surp2 sport at left with dspr
    mt "И куда это вы собрались?!"
    play sound ds_sfx_mot
    res "Ольга Дмитриевна?!"
    mt "Пёрсунов! Советова! Мы вас обыскались, а вы тут на автобусах катаетесь?!"
    us "Ой... извините, мы не хотели!"
    mt "Ага, случайно забрели в город, сели на автобус и поехали! Что вы мне тут сказки рассказываете!"
    mt "В общем, сегодня без дискотеки! А теперь выходите!"
    scene bg ds_ext_camp_entrance_sunset
    show us sad sport at center
    show mt rage pioneer at right
    with dissolve
    mt "Итак. Вы пойдёте в библиотеку. Там надо закончить разбирать книги, пока я буду писать объяснительные администрации."
    mt "Вы поняли меня?!"
    me "Да..."
    us "Поняли..."
    jump ds_day3_us_library

label ds_day3_stage_dv:
    $ ds_whom_helped = 'dv'
    $ persistent.sprite_time = "day"
    scene bg ext_stage_normal_day 
    with dissolve

    python:
        for i in range(1, 31):
            volume(0.15 + (d3_volume - 0.15) * (i / 30), "music")
            renpy.pause(1 / 30)

    window show
    "Выйдя к концертной площадке, ты видишь на сцене Алису."
    window hide

    scene cg ds_day3_dv_guitar
    with dissolve

    window show
    play sound ds_sfx_int
    con "Девочка вся отдаётся музыке – глаза закрыты, одну ногу она поставила на колонку и всем телом покачивается в такт."
    if skillcheck('encyclopedia', lvl_easy, passive=True):
        play sound ds_sfx_int
        enc "{result}Она играет «Взвейтесь кострами». Гимн пионеров."
        window hide
        menu:
            "Начать подпевать":
                window show
                enc "Тебе вспоминаются и слова... по крайней мере первого куплета."
                me "{i}Взвейтесь кострами, синие ночи!{/i}"
                me "{i}Мы пионеры, дети рабочих!{/i}"
                me "{i}Близится эра светлых годов,{/i}"
                me "{i}Клич пионеров - Всегда будь готов!{/i}"
            "Молча слушать":
                window show
    else:
        play sound ds_sfx_int
        enc "Мелодию ты узнать не можешь, хотя точно уверен, что слышал её раньше."
        play sound ds_sfx_int
        lgc "Что-то из советского рока, наверное."
        enc "Навскидку ты можешь перечислить с десяток названий групп этого жанра, но в их творчестве разбираешься плохо."
    play sound ds_sfx_mot
    inf "На слух песня кажется на удивление простой, буквально три аккорда."
    inf "Возможно, даже ты, немного потренировавшись, смог бы её сыграть."
    play sound ds_sfx_int
    lgc "Интересно, где Алиса научилась играть?"
    lgc "В советское время подобная музыка не пользовалась всенародным уважением."
    "Будущая рок-звезда же тебя не замечает."
    if skillcheck('conceptualization', lvl_easy, passive=True):
        con "{result}Она словно пытается слиться с музыкой, стать каждой нотой, каждым квадратом, каждой триолью."
        con "Сразу вспоминаются рок-герои восьмидесятых – многие из них так же сильно отдавались музыке."
        con  "Одень её вместо пионерской формы во что-нибудь более подходящее веяниям тогдашней эпохи, никто и не заметит подмены."
    stop music fadeout 5
    "Выступление подходит к концу."
    "Взяв несколько последних аккордов, Алиса наконец смотрит в твою сторону."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_stage_normal_day 
    with dissolve

    show dv normal pioneer at center   with dissolve
    window show
    dv "Понравилось?"
    play sound ds_sfx_mot
    com "Кажется, она совсем не удивилась тебе."
    window hide
    menu:
        "Одобрить":
            window show
            me "Да, весьма неплохо."
        "Раскритиковать":
            window show
            me "Да ну, это слишком просто! Не сможешь же ничего сложнее сыграть!"
            show dv rage pioneer at center with dspr
            dv "Вот как, значит?! Смогу! Но не для тебя! Вали, пока живой!"
            $ ds_lp['dv'] -= 2
            me "Ну и пойду!"
            scene bg ext_square_day
            with dissolve
            play sound ds_sfx_psy
            emp "Художника может обидеть каждый..."
            emp "А ты прям осудил её! Ты как, вообще в здравом уме?!"
            emp "Как можно было до такого додуматься?! Всё, я пас!"
            jump ds_day3_house_mt
    show dv grin pioneer at center   with dspr
    dv "Как будто можешь лучше!"
    "Алиса хитро улыбается."
    if skillcheck('authority', lvl_easy, passive=True):
        play sound ds_sfx_psy
        aut "{result}Она пытается тебя зацепить! Не позволяй ей этого!"
        window hide
        menu:
            "Согласиться":
                window show
                me "Я и не говорю, что могу лучше.{w} Я в музыке не спец."
                show dv normal pioneer at center   with dspr
                dv "Кто бы сомневался."
                me "Такие дела."
            "Возразить":
                window show
                me "А может, могу? Откуда ты знаешь?"
                dv "Вот как? Покажешь?"
                me "Не сейчас... я не готов."
                $ ds_skill_points['authority'] += 1
    else:
        me "Я и не говорю, что могу лучше.{w} Я в музыке не спец."
        show dv normal pioneer at center   with dspr
        dv "Кто бы сомневался."
        me "Такие дела."
    rhe "О чём с ней говорить дальше?"
    if (not ds_beat_dv) and (not ds_betray_dv) and (ds_lp['dv'] >= 15):
        "Ты уже собирался было уходить."
        show dv shy pioneer at center   with dspr
        dv "Подожди."
        me "Что?"
        dv "Слышал про вечернюю дискотеку?"
        me "Я думал, что это просто танцы…"
        show dv angry pioneer at center   with dspr
        dv "Дискотека, танцы – какая разница?"
        me "Слышал, а что?"
        show dv normal pioneer at center   with dspr
        dv "Собираешься идти?"
        "Бросив эти слова, она отворачивается."
        if skillcheck('empathy', lvl_medium, passive=True):
            play sound ds_sfx_psy
            emp "{result}Похоже, у неё {i}свои{/i} планы на тебя."
        window hide
        menu:
            "Иду":
                window show
                me "Ну да, иду. А что?"
            "Не иду":
                window show
                me "Нет, конечно! А ты?"
            "Не решил":
                window show
                me "Я пока не решил… А ты?"
        show dv smile pioneer at center   with dspr
        dv "Что там делать-то? Смотреть на толпу дебилов?"
        play sound ds_sfx_psy
        emp "Может, в словах Алисы и была доля правды, но такое наигранное пренебрежение тебя удивляет."
        emp "Ясно, что ей не нравится не дискотека как таковая."
        window hide
        menu:
            "Начать выяснять причины":
                window show
                me "А почему?"
                show dv normal pioneer at center   with dspr
                dv "Что почему?"
                me "Ну, почему ты не хочешь идти?{w} Дискотека – это же весело…"
                show dv angry pioneer at center   with dspr
                dv "Ты так считаешь?"
                emp "В её голосе мелькает раздражение. Осторожно."
                me "Не знаю.{w} Но я думал, что для тебя…"
                show dv normal pioneer at center   with dspr
                dv "Никогда их не любила."
                "Перебивает она тебя."
                show dv angry pioneer at center   with dspr
                dv "Совершенно там нечего делать!"
            "Не спрашивать":
                window show
        play sound ds_sfx_int
        rhe "Поддерживай разговор. Спроси про планы."
        me "Ясно…{w} И чем планируешь заняться тогда?"
        show dv normal pioneer at center   with dspr
        dv "Буду репетировать дальше. Это было для разминки, а вообще другое буду!"
        window hide
        menu:
            "Расспросить":
                window show
                me "А что ты репетируешь?"
                show dv rage pioneer at center   with dspr
                dv "Песню, придурок! Ты же слышал!"
                play sound ds_sfx_mot
                res "Так это же было типа разминочное..."
                play sound ds_sfx_fys
                hfl "Алиса совсем вышла из себя, так что ещё пара неудачных вопросов – и придётся спасаться бегством."
                me "А чья это песня?"
                show dv angry pioneer at center   with dspr
                dv "Моя!"
                me "Сама придумала?"
                dv "Сама!"
                me "Круто…"
            "Не расспрашивать":
                window show
        "В воздухе повисло неловкое молчание."
        me "Ладно, тогда…"
        show dv shy pioneer at center   with dspr
        dv "Не хочешь послушать?"
        window hide
        menu:
            "Cогласиться":
                window show
                me "Да, давай, сыграй!"
            "Сказать, что уже слышал":
                window show
                me "Я, кажется, уже слышал."
                show dv guilty pioneer at center   with dspr
                dv "Я не про это!"
                "Она надувает губы."
                show dv normal pioneer at center   with dspr
                dv "Целиком! Это же только пробная репетиция."
                me "Ааа… Ну, давай, играй…"
            "Отказаться":
                window show
                me "Да нет, что-то не хочется..."
                show dv angry pioneer at center with dspr
                dv "А чего припёрся тогда?! Кому ты тут сказки рассказываешь?!"
                play sound ds_sfx_int
                dra "Она права, мессир - если бы вы не хотели послушать, не пришли бы сюда."
                me "Ну ладно, сыграй..."
        show dv smile pioneer at center   with dspr
        dv "Сейчас не хочу."
        me "Тогда не играй…"
        rhe "И чего она от тебя добивается?"
        show dv sad pioneer at center   with dspr
        dv "Значит, не хочешь?"
        play sound ds_sfx_psy
        emp "Похоже, ты её расстроил."
        play sound ds_sfx_fys
        hfl "После такого логично было бы ожидать удара гитарой в лоб или ещё чего похуже."
        "Но Алиса всего лишь делает обиженное лицо."
        me "Я же говорю – хочу."
        show dv normal pioneer at center   with dspr
        dv "Тогда приходи сюда вечером – я для тебя сыграю."
        play sound ds_sfx_psy
        sug "«Для тебя»?{w} Как трогательно."
        sug "Кажется, ты кое-кого зацепил."
        play sound ds_sfx_psy
        vol "Между позором на танцах и бешеными умениями Двачевской на гитаре лучше выбрать второе."
        window hide
        menu:
            "Cогласиться":
                window show
                me "Приду обязательно. Спасибо за приглашение!"
                show dv smile pioneer at center   with dspr
                dv "Вот и отлично."
                $ ds_lp['dv'] += 1
                $ ds_dv_invite = True
                "Она как-то странно улыбается."
            "Отказаться":
                window show
                th "Такое развитие событий никак не входит в мои планы."
                me "Нет, извини."
                show dv guilty pioneer at center   with dspr
                dv "Да и надо больно!"
                $ ds_lp['dv'] -= 1
                "Она обиженно фыркает и отворачивается."
            "Cказать про танцы":
                window show
                me "Вечером же танцы."
                show dv angry pioneer at center   with dspr
                dv "Ты же сказал, что не пойдёшь!"
                hfl "Хотя идти тебе действительно не хочется, но без крайне веской причины с ДваЧе лучше не связываться."
                me "Ольга Дмитриевна не поймёт…"
                show dv rage pioneer at center   with dspr
                dv "Да плевать на неё!"
                "Говорит Алиса в сердцах."
                rhe "Она ждёт ответа. Конкретного. Да. Или нет."
                window hide
                menu:
                    "Cогласиться":
                        window show
                        me "Приду обязательно. Спасибо за приглашение!"
                        show dv smile pioneer at center   with dspr
                        dv "Вот и отлично."
                        $ ds_lp['dv'] += 1
                        $ ds_dv_invite = True
                        "Она как-то странно улыбается."
                    "Отказаться":
                        window show
                        th "Такое развитие событий никак не входит в мои планы."
                        me "Нет, извини."
                        show dv guilty pioneer at center   with dspr
                        dv "Да и надо больно!"
                        $ ds_lp['dv'] -= 1
                        "Она обиженно фыркает и отворачивается."
                    "{check=suggestion:15}Пригласить на танцы":
                        if skillcheck('suggestion', lvl_heroic):
                            window show
                            play sound ds_sfx_psy
                            sug "{result}Есть идея лучше. Ты хотел бы видеть её на танцах. Не в качестве танцорши - в качестве музыкального сопровождения."
                            $ ds_skill_points['suggestion'] += 1
                            me "Слушай. Есть идея получше. Ты можешь показать свои навыки всем. Столь классное исполнение услышать должны обязательно!"
                            show dv surprise pioneer at center with dspr
                            dv "В плане? Ты о чём?"
                            me "Я думаю, никто не откажется от живой музыки на танцах. Вот ты и покажешь класс!"
                            play sound ds_sfx_mot
                            com "Для неё твоё предложение стало неожиданностью."
                            show dv shy pioneer at center with dspr
                            dv "Эм... ну, в принципе, можно..."
                            emp "Сказать, что она смущена - ничего не сказать."
                            $ ds_dance_dv = True
                            $ ds_lp['dv'] += 2
                        else:
                            window show
                            play sound ds_sfx_psy
                            sug "{result}Давай. Пригласи её на танцы. Любой девушке понравится, когда парень приглашает её на танцы."
                            $ ds_skill_points['suggestion'] += 1
                            me "Может, лучше на танцы со мной сходишь?"
                            show dv angry pioneer at center with dspr
                            dv "Ты издеваешься?! Я же сказала - НЕ ХОЧУ Я НА ТАНЦЫ!"
                            $ ds_lp['dv'] -= 1
                            dv "Отвечай немедленно - танцы или я?"
                            window hide
                            menu:
                                "Cогласиться":
                                    window show
                                    me "Ладно, я приду..."
                                    show dv smile pioneer at center   with dspr
                                    dv "Вот и отлично."
                                    $ ds_lp['dv'] += 1
                                    $ ds_dv_invite = True
                                    "Она как-то странно улыбается."
                                "Отказаться":
                                    window show
                                    th "Такое развитие событий никак не входит в мои планы."
                                    me "Нет, извини."
                                    show dv guilty pioneer at center   with dspr
                                    dv "Да и надо больно!"
                                    $ ds_lp['dv'] -= 1
                                    "Она обиженно фыркает и отворачивается."
            "{check=suggestion:15}Пригласить на танцы":
                if skillcheck('suggestion', lvl_heroic):
                    window show
                    play sound ds_sfx_psy
                    sug "{result}Есть идея лучше. Ты хотел бы видеть её на танцах. Не в качестве танцорши - в качестве музыкального сопровождения."
                    $ ds_skill_points['suggestion'] += 1
                    me "Слушай. Есть идея получше. Ты можешь показать свои навыки всем. Столь классное исполнение услышать должны обязательно!"
                    show dv surprise pioneer at center with dspr
                    dv "В плане? Ты о чём?"
                    me "Я думаю, никто не откажется от живой музыки на танцах. Вот ты и покажешь класс!"
                    play sound ds_sfx_mot
                    com "Для неё твоё предложение стало неожиданностью."
                    show dv shy pioneer at center with dspr
                    dv "Эм... ну, в принципе, можно..."
                    emp "Сказать, что она смущена - ничего не сказать."
                    $ ds_dance_dv = True
                    $ ds_lp['dv'] += 2
                else:
                    window show
                    play sound ds_sfx_psy
                    sug "{result}Давай. Пригласи её на танцы. Любой девушке понравится, когда парень приглашает её на танцы."
                    $ ds_skill_points['suggestion'] += 1
                    me "Может, лучше на танцы со мной сходишь?"
                    show dv angry pioneer at center with dspr
                    dv "Ты издеваешься?! Я же сказала - НЕ ХОЧУ Я НА ТАНЦЫ!"
                    $ ds_lp['dv'] -= 1
                    dv "Отвечай немедленно - танцы или я?"
                    window hide
                    menu:
                        "Cогласиться":
                            window show
                            me "Ладно, я приду..."
                            show dv smile pioneer at center   with dspr
                            dv "Вот и отлично."
                            $ ds_lp['dv'] += 1
                            $ ds_dv_invite = True
                            "Она как-то странно улыбается."
                        "Отказаться":
                            window show
                            th "Такое развитие событий никак не входит в мои планы."
                            me "Нет, извини."
                            show dv guilty pioneer at center   with dspr
                            dv "Да и надо больно!"
                            $ ds_lp['dv'] -= 1
                            "Она обиженно фыркает и отворачивается."

        stop music fadeout 3
        play sound sfx_dinner_jingle_normal

        hide dv  with dissolve
        play sound2 ds_sfx_mot
        per_hea "Обед!"
        "Ты смотришь в сторону столовой."
        play sound ds_sfx_fys
        edr "Пожалуй, уже действительно пора – голод не тётка."
        "Обернувшись в сторону сцены, ты хочешь позвать Алису с собой."
        "Но она как сквозь землю провалилась."
        con "Знать, когда вовремя уйти, должен любой музыкант."
        window hide
    else:
        "И ты уходишь. Алиса никак не реагирует на это."

    jump ds_day3_lunch

label ds_day3_house_mt:
    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day 
    with dissolve

    $ volume(d3_volume,"music")

    play music music_list["get_to_know_me_better"] fadein 5

    window show
    "Ты возвращаешься к домику вожатой."
    "Ольга Дмитриевна вальяжно развалилась на шезлонге и читает книжку."
    show mt normal pioneer at center   with dissolve
    mt "Семён! А ты что здесь делаешь?"
    play sound ds_sfx_psy
    aut "Это тебе бы стоило спросить."
    me "Да я забыл кое-что…{w} Вот и вернулся."
    if not ds_was_on_lineup:
        show mt surprise pioneer at center   with dspr
        mt "На линейку ты так и не пришёл!"
        me "Да, извините…"
        show mt normal pioneer at center   with dspr
    mt "Ладно.{w} Это всё равно не отменяет того, что ты должен сегодня заняться чем-нибудь полезным."
    play sound ds_sfx_psy
    vol "Ты и планировал.{w} Только полезным для себя, а не для окружающих."
    me "Например?"
    mt "Ну, смотри..."
    mt "Можешь пойти на площадь помочь убраться. Там за главную Славя."
    play sound ds_sfx_mot
    res "Пару минут назад на площади же никого не было."
    mt "Или зайти к ребятам в кибернетический кружок - им что-то надо было."
    mt "Можешь помочь спортивному клубу."
    mt "А можешь пойти к Мику, ей нужна помощь с подготовкой к сегодняшней дискотеке."
    mt "Ещё Жене надо было чем-то помочь в библиотеке."
    mt "Ну, и мне надо разобраться в ваших документах, твоя помощь как парня, который должен разбираться в ЭВМ, была бы неоценима."
    aut "Почему она всегда пытается нагрузить тебя какой-то работой?"
    aut "Серьёзно – кроме Слави, никто здесь особо не перетруждается, а отдельные личности, и того больше, в полной мере наслаждаются молодостью и тунеядством."
    play sound ds_sfx_psy
    ine "Все попытки вожатой занять тебя чем-то, кажется, преследуют одну цель – не дать тебе понять, где ты находишься."
    ine "Ведь действительно, когда ты ловко орудуешь метлой, борясь с мусорной армадой, экзистенциальные мысли отходят на второй план."
    ine "В твоём случае такая трудотерапия могла бы пойти на пользу, но, как больной гангреной будет до последнего отказываться от ампутации, так и ты до последнего будешь защищать свой образ мыслей."
    me "Знаете, у меня, вообще-то, свои планы были."
    show mt smile pioneer at center   with dspr
    mt "Да? Это какие же?"
    me "Ну…"
    play sound ds_sfx_int
    dra "Не можете же вы ей в самом деле рассказать всё, что у вас на уме!"
    vol "С одной стороны, почему бы и нет?"
    play sound ds_sfx_fys
    hfl "Но, с другой – это может быть опасно!"
    th "По крайней мере сейчас сохраняется какое-то хрупкое равновесие, и мне ничего не угрожает.{w} Хотя бы с виду."
    show mt normal pioneer at center   with dspr
    mt "Так я и думала!"
    play sound ds_sfx_psy
    emp "Что именно {i}думала{/i} вожатая было понятно и так."
    mt "Видимо, ты ещё до конца не понял, как важно участвовать в общественной жизни.{w} Ведь только так ты сможешь стать образцовым пионером."
    vol "Ещё одной длинной лекции на эту тему ты не переживёшь. Соглашайся на предложенные варианты."
    ine "В конце концов, ответы в этом мире можно найти в самых неожиданных местах.{w} Наверное..."
    show mt surprise pioneer at center   with dspr
    mt "Ну? Или мне за тебя выбрать?"
    "Голос вожатой не терпит возражений."
    me "Уж как-нибудь сам..."
    $ ds_karma += 10

    stop music fadeout 3
    window hide
    menu:
        "Помочь Славе":
            window show
            me "Пожалуй, я помогу Славе."
            mt "Отлично!"
            jump ds_day3_help_sl
        "Помочь кибернетикам":
            window show
            me "Думаю, помогу ребятам-кибернетикам..."
            mt "Как скажешь."
            jump ds_day3_help_cyber
        "Помочь спортклубу":
            window show
            me "Ладно, я помогу спортивному клубу."
            mt "Хорошо, иди туда сейчас же!"
            jump ds_day3_help_sport
        "Помочь Жене":
            window show
            me "Я обещал Жене помочь ей в библиотеке..."
            mt "Да, давай!"
            jump ds_day3_help_mz
        "Помочь Мику":
            window show
            me "Мне бы хотелось помочь Мику..."
            show mt laugh pioneer at center with dspr
            mt "Что, понравилась японочка?"
            jump ds_day3_help_mi
        "Помочь вожатой":
            window show
            me "А давайте я вам помогу!"
            mt "О, спасибо, Семён!"
            $ ds_lp['mt'] += 1
            jump ds_day3_help_mt
        "Предложить помочь Яне" if ds_met['ya'] > 0:
            window show
            me "Слушайте... а не нужна ли помощь Яне, вожатой 6-го отряда?"
            show mt surprise pioneer at center with dspr
            mt "Ох... я даже не знаю... лучше у неё спроси сам..."
            mt "Она вроде как сейчас на пляже с детьми..."
            me "Хорошо, я пойду, спасибо!"
            jump ds_day3_help_ya

label ds_day3_help_sl:
    window show
    $ ds_whom_helped = 'sl'
    $ ds_lp['sl'] += 1
    th "Из двух – ну или из пяти – зол надо выбрать меньшее."
    th "Славя злом в принципе не являлась – поэтому и выбор очевиден."
    play sound ds_sfx_psy
    vol "Любой нормальный человек хочет жить в чистоте, но обычно уборка казалась тебе сродни занятиям в тренажёрном зале – полезно, но не для меня."
    vol "Однако красить лавки, перебирать бумажки, книжки или находиться в обществе двух будущих гениев советской науки ещё хуже."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_square_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "На площади собралось человек 10 пионеров."
    th "Странно, и откуда они вдруг понабежали?"
    "Ты подходишь к Славе."
    show sl normal pioneer at center   with dissolve
    me "Привет!"
    sl "Ой, привет! Ты помочь пришёл?"
    window hide
    menu:
        "Я пришёл помочь..."
        "По своему желанию":
            window show
            me "Да! Помочь {i}тебе{/i}."
            show sl smile pioneer at center with dspr
            sl "Ой, как мило!"
            $ ds_lp['sl'] += 1
        "Не по своей воле":
            window show
            me "Ну, не по своей воле, конечно…"
            show sl smile pioneer at center   with dspr
            sl "Понятно."
    show sl normal pioneer at center   with dspr
    sl "Бери метлу, твой участок – рядом с памятником."
    hide sl  with dissolve
    play sound ds_sfx_int
    vic "На самом деле, убирать там особо нечего, всё и так кажется довольно чистым."
    play sound ds_sfx_mot
    per_eye "Однако кое-где мусор всё же валяется."
    "..."
    window hide

    with fade2

    play music music_list["smooth_machine"] fadein 5

    scene bg ds_ext_square2_day
    show sl normal pioneer at center
    with dissolve

    window show
    "Помахав метлой некоторое время, ты возвращаешься к Славе, которая села отдохнуть на скамеечку."
    me "Хороший сегодня денёк…"
    sl "Да, только жарко."
    "Она прикрывает глаза ладонью и смотрит на небо."
    window hide
    menu:
        "Cделать комплимент":
            window show
            me "Ты прямо ударница коммунистического труда!"
            show sl shy pioneer at center   with dspr
            sl "Да брось ты! Я просто люблю помогать другим."
            $ ds_lp['sl'] += 1
            me "Это хорошо."
            show sl normal pioneer at center   with dspr
            sl "А ты?"
            me "Что я?"
            sl "Ну, я так понимаю, что тебя несколько тяготит общественная работа?"
            play sound ds_sfx_int
            dra "Врать бессмысленно - она {i}чувствует{/i} вас, мессир."
            me "Да, наверное."
            sl "Почему?"
            play sound ds_sfx_psy
            vol "Хороший вопрос, на самом деле."
            me "Не знаю…"
            show sl sad pioneer at center   with dspr
            sl "Может, ты не любишь компанию?"
            play sound ds_sfx_psy
            esp "Есть у тебя такое..."
            me "Вполне возможно."
            vol "Что-то в словах Слави было правдой.{w} Наверное, она неплохо разбирается в людях."
            vol "По крайней мере – в тебе."
            vol "Хотя как это возможно, если ты сам порой себя с трудом понимаешь?"
        "Промолчать":
            window show
            "Но Славя молчать не собирается."
    show sl normal pioneer at center   with dspr
    sl "Чем займёшься, когда смена закончится?"
    me "В смысле?"
    show sl smile pioneer at center   with dspr
    sl "Ну, в институт будешь готовиться? Или какую-то специальность хочешь освоить?"
    vol "Все твои специальности – просмотр аниме и интернет-зависимость – уже освоены в совершенстве."
    me "Не знаю… А ты?"
    sl "У нас дома небольшое хозяйство, хочу родителям помогать."
    play sound ds_sfx_mot
    res "Так, стоп, какое хозяйство при советской власти, когда кругом колхозы?"
    play sound ds_sfx_int
    lgc "Это же, судя по всему (да хотя бы по Генде), альтернативный Советский Союз. Здесь вполне могли разрешить единоличное хозяйство."
    show sl normal pioneer at center   with dspr
    sl "А твои родители кем работают?"
    if ds_know_parents:
        me "Мои родители - дипломаты, работают в Японии!"
    else:
        play sound ds_sfx_int
        con "Cкажи первое, что придёт в голову."
        me "Папа – в горкоме, мама – учителем."
        dra "Вы соврали, мессир.{w} Хотя ваши слова, в общем-то, недалеки от правды."
    show sl smile2 pioneer at center   with dspr
    sl "Здорово."
    play sound ds_sfx_psy
    emp "Похоже, ей действительно это кажется весьма прикольным."
    me "Наверное…"
    play sound ds_sfx_mot
    com "Диалог зашёл в тупик, поэтому ты пытаешься отвести от Слави глаза – смотришь то себе под ноги, то в небо, то по сторонам."
    show sl normal pioneer at center   with dspr
    sl "Знаешь, мне кажется, у тебя в жизни всё тоже будет хорошо!"
    play sound ds_sfx_psy
    vol "К чему вообще она это сказала?"
    vol "И почему «тоже»?"
    vol "Но всё же приятно!"
    $ ds_up_morale()
    me "С-спасибо…"
    me "Но что ты имеешь в виду?"
    show sl smile2 pioneer at center   with dspr
    sl "Мне кажется, ты иногда очень пессимистично смотришь на жизнь."
    sl "Я не знаю, почему. Наверное, тебе довелось пережить сильную потерю..."
    sl "Но надо двигаться вперёд!"
    me "Возможно."
    sl "У тебя всё наладится обязательно!"
    me "Возможно."
    ine "От этого разговора тебе становится несколько не по себе."
    ine "С одной стороны, в её словах не было ничего особенного."
    ine "В принципе, почти любой человек на месте Слави мог бы сделать подобные выводы."
    ine "Тем не менее кажется, что она видит тебя насквозь."
    me "Ладно, надо дальше убираться."
    show sl smile pioneer at center   with dspr
    sl "Ага."
    "Она улыбается и тоже берётся за метлу."

    play sound_loop sfx_broom_sweep fadein 2

    hide sl  with dissolve
    th "Никогда не думал, что уборка может доставлять столько удовольствия."
    vol "Нет, ты не расстроился из-за разговора со Славей, даже наоборот – тебе было приятно услышать от неё подобное."
    vol "Пожалуй, впервые кто-то, рассуждая о твоей жизни, не ругал тебя, не давал глупых советов, основанных лишь на собственном опыте, не лез копаться у тебя в голове и не делал после этого каких-то далеко идущих выводов."
    vol "Тебе просто приятно, что тебя кто-то поддержал."
    th "Нет, не так!"
    th "Мне было приятно, что это сделала именно Славя."
    window hide

    stop sound_loop

    stop music fadeout 3

    with fade

    window show

    play sound sfx_dinner_jingle_normal

    "Вскоре по лагерю заиграла музыка, призывающая на обед, и ты, с облегчением и чувством выполненного долга отложив метлу в сторону, направляешься в столовую."
    window hide
    jump ds_day3_lunch

label ds_day3_help_cyber:
    $ ds_whom_helped = 'el'
    $ persistent.sprite_time = "day"
    scene bg ext_clubs_day 
    with dissolve

    window show
    vol "А какой смысл лишний раз пересекаться со странноватыми любителями научной фантастики периода начала-середины XX века?"
    play sound ds_sfx_int
    enc "Но вдруг от них получится что-то узнать?"
    enc "Можно хотя бы попробовать."
    "Стоя на пороге клуба, ты несколько замялся, но, отбросив в сторону сомнения, открываешь дверь и входишь внутрь."
    window hide

    play sound sfx_open_door_clubs

    $ renpy.pause(1)

    $ persistent.sprite_time = "day"
    scene bg int_clubs_male_day 
    with dissolve

    play ambience ambience_clubs_inside_day fadein 3

    show sh normal pioneer at cright 
    show el normal pioneer at cleft 
    with dissolve
    window show
    "Электроник и Шурик согнулись над столом и что-то пристально рассматривают."
    play sound ds_sfx_int
    rhe "Будь максимально дружелюбным."
    me "Привет, кибернетики! Как жизнь?"
    el "Привет! А мы тебя ждали!"
    $ ds_lp['el'] += 1
    me "Я и не сомневался."
    th "И правда – Электроник ведь знал все события наперёд."
    me "Ну, и что вам нужно?"
    sh "Поможешь робота доделать."
    me "Каким образом?{w} Я в подобных вещах не силён."
    show sh serious pioneer at cright   with dspr
    sh "А мы тебе сейчас всё покажем, расскажем.{w} Не умеешь – научим, не хочешь…"
    show el smile pioneer at cleft   with dspr
    el "Заставим!"
    "Радостно заканчивает за Шурика Электроник."
    play sound ds_sfx_int
    lgc "Возможно, они могут что-то знать про путешествия во времени. Во всяком случае, спросить их можно."
    window hide
    menu:
        "Помочь с роботом":
            window show
            me "А давайте! Приступим!"
            el "Тогда сходи в кладовку, принеси оттуда ящик с инструментами."
            me "Хорошо..."
            scene bg int_clubs_male2_night
            with dissolve
            "Ты заходишь в кладовку."
            th "Так, где тут у них инструменты?.."
            if skillcheck('shivers', lvl_easy, passive=True):
                play sound ds_sfx_fys
                shi "{result}Не спрятано ли тут ничего? Такое ощущение, что да, скрыто..."
                window hide
                menu:
                    "Обыскать":
                        window show
                        $ ds_skill_points['shivers'] += 1
                        "Ты начинаешь осматривать все ящики... ища то, не знаю что."
                        th "Что же тут такое?.."
                        play sound ds_sfx_mot
                        per_eye "А это что?"
                        "Перед тобой фотография. На ней изображена странная девочка..."
                        per_eye "А точнее - кошкодевочка!"
                        $ ds_seen_catgirl_photo = True
                        window hide
                        menu:
                            "Cпросить кибернетиков":
                                window show
                                th "Так-так, что это такое... сейчас узнаем..."
                                play sound ds_sfx_fys
                                hfl "Только будь начеку. А то вдруг ты открыл страшную тайну, за которую тебя закопают."
                                scene bg int_clubs_male_day 
                                with dissolve

                                show sh normal pioneer at cright 
                                show el normal pioneer at cleft 
                                with dissolve
                                me "А что это такое?"
                                "С этими словами ты демонстрируешь им фото."
                                show el shocked pioneer at cleft
                                show sh scared pioneer at cright
                                with dspr
                                sh "Ничего! Ничего такого!"
                                el "Ладно, слушай..."
                                el "Мы как-то гуляли по лесу с Шуриком... и увидели что-то странное."
                                sh "А у меня был фотоаппарат! И я сфотографировал... и увидел девочку-кошку!"
                                el "Мы сами не знаем, кто это такая! Она сразу же убежала!"
                                me "Ладно, это я понял... спасибо, что пояснили..."
                                show sh serious pioneer at cright
                                with dspr
                                sh "А инструменты?"
                                me "Да, точно... сейчас принесу."
                                "И ты возвращаешься в кладовку."
                                scene bg int_clubs_male2_night
                                with dissolve
                            "Не спрашивать":
                                window show
                                th "Пока запомним, но спрашивать не буду... а то мало ли..."
                    "Не обыскивать":
                        window show
            "Вскоре ты находишь инструменты и возвращаешься."
            scene bg int_clubs_male_day 
            with dissolve
            show el smile pioneer at cleft
            show sh serious pioneer at cright
            with dspr
            "Но тут оказывается, что они как раз закончили работу и собираются уже идти обедать."
            el "Отлично поработали!"
            sh "Согласен!"
            $ ds_lp['el'] += 1
            sh "Можешь идти!"
            el "Только вернись после обеда!"
            me "Ладно-ладно... Пока!"
        "Отказаться и уйти":
            window show
            me "Да знаете, у меня тут есть другие дела..."
            el "Какие такие дела?"
            me "Очень важные!"
            show el upset pioneer at cleft with dspr
            el "Жаль... иди тогда..."
            $ ds_lp['el'] -= 1
            "И ты выходишь из клуба."
            stop ambience fadeout 2
            jump ds_day3_help_un
        "Cпросить про путешествия во времени":
            window show
            me "Это, конечно, всё замечательно, ребята, но я с вами вот о чём хотел поговорить…{w} У меня тут мысль родилась, и, думаю, это как раз по вашему адресу."
            show sh normal pioneer at cright   with dspr
            sh "Что за мысль?"

            stop ambience fadeout 2

            play music music_list["just_think"] fadein 3

            me "Как вы думаете, возможны ли путешествия во времени?"
            show el normal pioneer at cleft   with dspr
            el "С чего это ты вдруг о таком задумался?"
            "Электроник как-то неожиданно становится серьёзным."
            me "Да нет, просто…"
            window hide
            menu:
                "{check=conceptualization:6}Придумать историю":
                    if skillcheck('conceptualization', lvl_trivial):
                        window show
                        play sound ds_sfx_int
                        con "{result}Взял книжку в библиотеке и прочитал. Прям такая есть - «Машина времени», Герберт Уэллс."
                        me "Я вчера книжку взял в библиотеке – «Машина времени» Уэллса. Читали, наверное? Вот, собственно, и заинтересовался."
                    else:
                        window show
                        play sound ds_sfx_int
                        con "{result}Сложно придумать правдоподобный повод..."
                        me "Да просто так, пришла мысль в голову!"
                    $ ds_skill_points['conceptualization'] += 1
                    show sh serious pioneer at cright   with dspr
                    sh "Ааа…"
                    show el smile pioneer at cleft   with dspr
                    el "Решил сгонять в будущее, посмотреть как там?"
                    me "Да нет.{w} Меня больше интересуют путешествия в прошлое."
                    el "Это почему?"
                    me "Не знаю даже.{w} Просто…"
                "Рассказать правду":
                    window show
                    me "Да просто я уснул у себя.. в будущем... и проснулся вот тут..."
                    show el surprise pioneer at cleft
                    show sh surprise pioneer at cright
                    with dspr
                    play sound ds_sfx_psy
                    emp "Они сражены такой историей... в нехорошем смысле..."
                    sh "Э... ты точно здоров? Не перегрелся?"
                    play sound ds_sfx_psy
                    aut "Поздравляю, ты выставил себя посмешищем! Сумасшедшим."
                    $ ds_damage_morale()
                    me "Вроде да..."
                    el "Будем считать это шуткой... наверное..."
                    el "Но всё-таки зайди к медсестре..."
                    me "Так что с путешествиями во времени?"
            me "Ну, об этом вы что думаете?"
            show sh normal_smile pioneer at cright   with dspr
            sh "Общая теория относительности допускает существование червоточин, то есть туннелей в пространстве.{w} Но ты этого всё равно не поймёшь."
            play sound ds_sfx_int
            enc "Скорее всего и правда не поймёшь."
            sh "Да и при любой гипотезе мы сталкиваемся с целым рядом парадоксов."
            sh "Например, если ты вернёшься в прошлое и убьёшь себя, то получается, что {i}ты{/i} из настоящего уже не можешь существовать."
            me "Эээ… Наверное…"
            show el normal pioneer at cleft   with dspr
            el "Короче, это всё слишком антинаучно."
            me "Ясно, но если это было бы возможно?.."
            me "Я имею в виду: для того, чтобы оказаться в прошлом, нужна какая-то машина, устройство, установка?"
            me "Или достаточно просто заснуть и проснуться уже в другом времени и в другом месте?"
            show sh serious pioneer at cright   with dspr
            sh "Могу тебе сказать, что наука ещё не дошла до той стадии развития, при которой возможен ответ на этот вопрос."
            rhe "Прямо строчки из журнала «Техника-Молодёжи».{w} Наверное, и у тебя на антресоли завалялась пара номеров."
            me "Ясно."
            vol "Похоже, прийти сюда было плохой идеей…"
            sh "Однако если предположить, что известные нам законы физики неверны…{w} Или наоборот – законы верны, но мы не всё о них знаем..."
            sh "Тогда такой вариант возможен."
            me "Так…"
            el "И кто-то, например раса более разумная, чем люди, обладает превосходящими знаниями о природе бытия."
            me "Так…"
            sh "Они могут построить машину времени или каким-то другим способом путешествовать сквозь время."
            me "Так..."
            play sound ds_sfx_psy
            ine "Получается, в прошлое тебя закинули старшие братья по разуму?"
            ine "Интересная идея.{w} И, если подумать, она не лишена смысла."
            me "А как можно найти этих вот… о ком вы говорите… если уже оказался в прошлом?"
            show el laugh pioneer at cleft 
            show sh laugh pioneer at cright 
            with dspr
            el "Откуда же мы знаем?!"
            "Они оба громко рассмеялись."
            me "Ладно, ребята, спасибо вам!"
            "Ты уже собирался было уходить."
            show el normal pioneer at cleft 
            show sh normal pioneer at cright 
            with dspr
            el "Подожди! А как же робот?.."

            stop music fadeout 3

            me "С ним всё будет хорошо – я уверен!"
            window hide

            $ persistent.sprite_time = "day"
            scene bg ext_clubs_day 
            with dissolve

            window show
            play sound ds_sfx_int
            lgc "Юные кибернетики рассуждают весьма логично, но это, к сожалению, опять же никоим образом не приближает тебя к разгадке твоего попадания в этот мир."
        "Cказать Электронику про Женю" if ds_know_mz_el:
            window show
            me "Cлушай, Электроник. Я вчера зашёл в библиотеку..."
            show el surprise pioneer at cleft
            with dspr
            el "Зачем?"
            me "Неважно. Просто прогуливался. И увидел там кое-что..."
            show el scared pioneer at cleft
            with dspr
            el "Что? Что такое?"
            me "Послание от Жени. Тебе. Любовное."
            show el surprise pioneer at cleft
            with dspr
            el "Вот как..."
            if ds_lp['el'] >= 0:
                show el smile pioneer at cleft
                with dspr
                el "Спасибо за информацию! Я побежал!"
                hide el with dissolve
                sh "А робот?.."
                "Но Электроник уже убежал."
                show sh angry pioneer at cright
                with dspr
                sh "Вот зачем ты это сделал?"
                me "Я? Я ничего, просто сказал ему..."
                sh "Эх, ладно..."
                $ ds_lp['el'] += 1
                $ ds_el_mz_relation = True
            else:
                show el laugh pioneer at cleft
                with dspr
                el "Классная шутка, конечно! Но я же знаю, что Женя не может испытывать ничего ко мне!"
                play sound ds_sfx_psy
                emp "Не поверил он тебе. Меньше он верит только в себя."
                show el normal pioneer at cleft
                with dspr
                el "Но всё-таки, не разыгрывай меня так, пожалуйста. Это тема... не самая приятная для меня."
                $ ds_lp['el'] -= 1
                emp "Что логично."
                play sound ds_sfx_mot
                res "Как ты не додумался взять с собой письмо?!"
                th "Я думал, он мне и так поверит..."
                res "Но, как видишь, не поверил. В следующий раз имей при себе вещественные доказательства!"
                "На этом ты выходишь из клуба."
                stop ambience fadeout 2
                jump ds_day3_help_un
    play sound sfx_dinner_jingle_normal

    "Вскоре по лагерю заиграла музыка, призывающая на обед, и ты направляешься в столовую."
    window hide
    jump ds_day3_lunch

label ds_day3_help_sport:
    $ ds_whom_helped = 'us'
    window show
    play sound ds_sfx_psy
    vol "Под предлогом помощи спортивному клубу, возможно, получится улизнуть от работы."
    play sound ds_sfx_int
    lgc "У них и так наверняка хватает народу, и без лишней пары рук они вполне обойдутся."
    vol "Однако дойти до спортивной площадки всё же следует – хотя бы чтобы отметиться."
    play sound ds_sfx_fys
    hfl "А то вдруг Ольга Дмитриевна потом узнает, что её образцовый пионер тунеядствует, пренебрегая общественно полезной деятельностью!"
    hfl "Мало ли у них тут есть наказания похуже выволочки на партсобрании..."
    hfl "Такое развитие событий никак не входит в твои планы."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_playground_day 
    with dissolve

    play ambience ambience_soccer_play_background fadein 2

    window show
    "Однако вместо уборки, покраски, починки и прочего ремонта на футбольном поле вовсю идёт матч!"

    play music music_list["eat_some_trouble"] fadein 5

    play sound ds_sfx_int
    vic "Играют 5 на 6."
    window hide

    scene cg d3_soccer 
    with dissolve

    window show
    play sound ds_sfx_mot
    per_eye "Ты приглядываешься к участникам и узнаёшь Ульяну."
    per_eye "Команды явно неравны по силам."
    per_eye "Одна из них состояла полностью из малышей, детей лет по двенадцать."
    per_eye "В другой были сплошь ребята постарше."
    per_eye "И к тому же за неё играла Ульянка."
    play sound ds_sfx_fys
    phi "Ну и ладно – что может один человек, тем более девочка…"
    svf "Но вскоре ты понимаешь, что ошибся."
    svf "Ульянка технично работает с мячом, обыгрывая соперников одного за другим."
    play sound ds_sfx_psy
    esp "Ей, конечно, не хватает умения играть на команду..."
    svf "но на таком уровне этого и не требуется – голы она забивала регулярно."
    "Ты подходишь поближе к полю."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_playground_day 
    with dissolve

    show us surp1 sport far at center    with dissolve   
    window show
    us "Эй! Давай с нами! У них одного человека не хватает."
    window hide
    menu:
        "{check=savoir_faire:6}Cогласиться":
            window show
            me "Давайте!"
            if not ds_play_football:
                th "Ну, раз отказался в прошлый раз, то сейчас, пожалуй, сыграю."
        "Cпросить про работу":
            window show
            me "Так вот как вы тут занимаетесь общественной работой!"
            show us dontlike sport at center   with dissolve
            us "А мы уже всё сделали!"
            "Обиженно возражает Ульянка."
            "Ты оглядываешь спортивную площадку – лавочки покрашены, сетка новая натянута."
            th "Когда только успели?"
            show us laugh sport at center   with dspr
            us "Заходи за них!"
            window hide
            menu:
                "Согласиться":
                    window show
                    me "Давайте!"
                    if not ds_play_football:
                        th "Ну, раз отказался в прошлый раз, то сейчас, пожалуй, сыграю."
                "Отказаться":
                    window show
                    me "Нет уж, спасибо!"
                    "И ты уходишь."
                    stop music fadeout 3
                    stop ambience fadeout 3
                    jump ds_day3_help_sugar
        "Отказаться":
            window show
            me "Нет уж, спасибо!"
            "И ты уходишь."
            stop music fadeout 3
            stop ambience fadeout 3
            jump ds_day3_help_sugar
    $ ds_lp['us'] += 1
    hide us  with dissolve
    window hide

    with fade

    window show
    "Мяч на центре поля. Начинает ваша команда."

    if skillcheck('savoir_faire', lvl_trivial):
        play sound sfx_soccer_ball_kick
        play sound2 ds_sfx_mot
        svf "{result}Ты первым же касанием аккуратным ударом кладёшь мяч в девятку ворот соперника."
        svf "На самом деле, это не составляет особого труда – поле в длину от силы метров пятьдесят, а вратарь чужой команды даже не достаёт до перекладины."
    else:
        play sound ds_sfx_mot
        svf "{result}Ты замахиваешься, но умудряешься промахнуться по мячу."
        "Ульянка пользуется твоим во всех смыслах промахом и отбирает мяч, легко забивая его в ворота."
        $ ds_damage_morale()
    window hide
    menu:
        "Играть одному за всех":
            window show
            "Ты решаешь не возиться с малышнёй вокруг тебя и пытается в одно лицо играть за всех."
            play sound ds_sfx_psy
            esp "Однако, ты недооценил силу команды."
            play sound ds_sfx_mot
            svf "Ульяна со своей командой вшестером тебя (не без труда, конечно) всё-таки обыгрывают."
            "И, хотя ты и сумел забить голов 7-8 - они забили ещё пять голов."
            play sound sfx_dinner_jingle_processed
            show us laugh sport at center with dissolve
            us "Победа! Победа! Победа!"
            "Сигнал к обеду автоматически означает конец матча."
            play sound ds_sfx_psy
            vol "Победой команды Ульяны."
            jump ds_day3_lunch
        "{check=esprit:10}Организовать игру команды":
            if skillcheck('esprit', lvl_medium):
                window show
                play sound ds_sfx_psy
                esp "{result}Так, давай. Собери свою команду воедино. И у вас всё получится."
                me "Так, перерыв! Нам надо обсудить тактику."
                "Ульяна, явно уверенная в себе, даже не возражает."
                esp "Ты собираешь возле себя своих и объясняешь им свой тактический замысел."
                me "Мы готовы!"
                window hide
                $ renpy.pause(1.0)
                window show
                play sound ds_sfx_psy
                esp "Спустя какое-то время счёт становится уже равным, хотя в начале твоя команда отставала на семь или восемь голов."
                esp "Справедливости ради надо отметить, что и команда Ульянки забила парочку мячей за это время."
                esp "Точнее, забила она."
                play sound ds_sfx_mot
                svf "Нельзя сказать, что в её арсенале был набор финтов Рональдиньо или филигранные удары Бэкхема – она просто прокидывала мяч в стороны и, подходя в упор к воротам, била, что называется, «с пыра»."
                esp "Но ты сумел организовать игру своей команды так, что одна Ульяна никак не могла выстоять против них. А её товарищи на поверку оказались плохой подмогой."
                $ ds_skill_points['esprit'] += 1
                "Когда счёт оказывается 15:9 в вашу пользу, Ульяна воскликает:"
            else:
                window show
                play sound ds_sfx_psy
                esp "{result}Ты пытаешься привести к порядку свою команду по ходу игры, но безуспешно."
                esp "Тебе приходится вытягивать игру одному."
                $ ds_skill_points['esprit'] += 1
                play sound ds_sfx_fys
                phi "А так как ты больше и сильнее их - всё-таки это оказывается реально."
                play sound ds_sfx_psy
                esp "Спустя какое-то время счёт становится уже равным, хотя в начале твоя команда отставала на семь или восемь голов."
                esp "Справедливости ради надо отметить, что и команда Ульянки забила парочку мячей за это время."
                esp "Точнее, забила она."
                play sound ds_sfx_mot
                svf "Нельзя сказать, что в её арсенале был набор финтов Рональдиньо или филигранные удары Бэкхема – она просто прокидывала мяч в стороны и, подходя в упор к воротам, била, что называется, «с пыра»."
                svf "Однако такая нехитрая тактика приносит свои плоды. Я не мог уследить одновременно за всеми игроками команды противников, а мои товарищи были плохой подмогой."
                phi "Но играешь гораздо лучше их всех и, в принципе, можешь забить столько, сколько бы захотел."
                play sound ds_sfx_psy
                vol "Но тебе это кажется неспортивным. Тем более, главное же не победа, а участие?"
    show us laugh sport at center   with dissolve
    us "Пенальти бьём.{w} Кто выиграет, тот и победил в матче."
    play sound ds_sfx_psy
    vol "Ты проигрывать совсем не хочешь."
    window hide
    menu:
        "Согласиться":
            window show
            me "Ладно..."
        "Отказаться":
            window show
            me "Нет! Наша команда {i}уже{/i} выиграла."
            show us dontlike sport at center with dspr
            us "И ничего не выиграла! Я же сказала - пенальти!"
            window hide
            menu:
                "{check=authority:8}Настоять":
                    if skillcheck('authority', lvl_easy):
                        play sound ds_sfx_psy
                        aut "{result}Ты всем своим видом показываешь, что лучше с тобой не спорить."
                        show us fear sport at center with dspr
                        us "Ладно-ладно, выиграли вы..."
                        $ ds_lp['us'] -= 1
                        play sound sfx_dinner_horn_processed

                        window show
                        "И тут заиграла музыка, призывающая пионеров на обед."
                        show us laugh2 sport at center   with dspr
                        us "Ладно, ещё отыграюсь!"
                        hide us  with dissolve

                        stop music fadeout 3

                        "Она рассмеялась, помахала мне рукой и побежала в сторону столовой."
                    else:
                        play sound ds_sfx_psy
                        aut "{result}Ты пытаешься настоять на своём."
                        me "Я сказал - мы выиграли."
                        show us laugh sport at center with dspr
                        us "Да какая разница, что ты сказал! Давай пенальти!"
                        play sound ds_sfx_psy
                        esp "Твоя команда не настроена спорить с Ульяной. Так что придётся играть пенальти."
                        $ ds_damage_morale()
    us "Вставай на ворота, я тебе буду бить, потом – ты мне."
    me "По одному удару?"
    us "Да."
    "Ты встаёшь на линию."

    play sound sfx_soccer_ball_catch

    "Она разбежалась и…{w} ударила прямо по центру мне в руки."
    show us sad sport at center   with dspr
    us "Так нечестно!"
    me "Что нечестно?"
    show us angry sport at center   with dspr
    us "Я перебью."
    window hide
    menu:
        "Разрешить":
            window show
            me "Перебей."
            "Улыбаешься ты."
        "Отказать":
            window show
            me "Не-не-не!"
            "Но она и не собирается слушать тебя и бьёт по мячу."

    play sound sfx_soccer_ball_gate

    "Второй удар у неё вышел совсем в молоко."
    me "Ещё хочешь?"
    nvl clear
    show us dontlike sport at center   with dspr
    us "Нет уж!"
    us "Но ты мне точно не забьёшь!"
    me "Посмотрим…"
    hide us  with dissolve

    if skillcheck('coordination', lvl_easy, passive=True):

        play sound sfx_soccer_ball_kick
        play sound2 ds_sfx_mot
        cor "{result}Аккуратным ударом ты кладёшь мяч в правую от неё шестерку."
        "Ульяна даже не дёргается."
        play sound ds_sfx_mot
        svf "Впрочем, незачем – такие пенальти не берутся."

        stop ambience fadeout 4
        $ ds_skill_points['coordination'] += 1

        show us sad sport at center   with dissolve
        me "Получается, я выиграл."
        "Она молчит и лишь обиженно смотрит на меня."
        window hide
        menu:
            "Разрядить ситуацию":
                window show
                me "Да ты не расстраивайся!{w} Я же просто…"
            "Промолчать":
                pass
        window hide
    else:
        play sound sfx_soccer_ball_kick
        play sound2 ds_sfx_mot

        cor "{result}Впрочем, ты, как и она ранее, тоже бьёшь не туда."
        show us laugh sport at center with dissolve
        us "Ладно, соглашусь на ничью, так уж и быть!"
        me "Но..."
    with fade

    stop music fadeout 3

    play sound sfx_dinner_horn_processed

    window show
    "И тут заиграла музыка, призывающая пионеров на обед."
    show us laugh2 sport  at center   with dissolve
    us "Ладно, ещё отыграюсь!"
    hide us  with dissolve

    stop music fadeout 3

    "Она смеётся, машет тебе рукой и бежит в сторону столовой."
    "Ты направляешься за ней."
    window hide

    jump ds_day3_lunch

label ds_day3_help_un:
    $ ds_whom_helped = 'un'
    $ persistent.sprite_time = 'day'
    scene bg ext_clubs_day
    with dissolve

    "Ты выходишь из клуба."
    th "Так, ладно, надо бы к кому-нибудь пойти..."

    show un normal pioneer at center
    with dissolve
    play sound ds_sfx_mot
    res "Лена? Что ей тут надо?"

    show un surprise pioneer at center
    with dspr
    un "Привет..."
    me "Привет, Лена!"
    show un shy pioneer at center
    with dspr
    un "А мальчики там?"
    window hide
    menu:
        "Спросить, зачем они":
            window show
            me "Там, а что случилось?"
            show un normal pioneer at center
            with dspr
            un "Да так... к вожатой нужно сходить, поговорить..."
        "Просто ответить":
            window show
            me "Ну да, они там!"
            show un normal pioneer at center
            with dspr
            un "Хорошо, спасибо..."
            hide un
            with dissolve
            play sound sfx_open_door_clubs
            window hide
            $ renpy.pause(1.5)
            show un sad pioneer at center
            with dspr
            window show
            "Лена возвращается так быстро, что ты не замечаешь прошедшего времени."
            me "Ну как?"
            un "Можешь мне помочь сходить к вожатой?"
    window hide
    menu:
        "Согласиться":
            window show
            me "Идём!"
            $ ds_lp['un'] += 2
            show un smile pioneer at center
            with dspr
            un "Cпасибо, Семён!"
            play sound ds_sfx_psy
            vol "А на что ты собственно подписался?"
            play sound ds_sfx_psy
            sug "Ну, вряд ли на что-то противозаконное. Это же не Алиса, это тихоня Лена!"
            show un normal pioneer at center
            with dspr
            un "Просто, понимаешь... мне нравится рисовать..."
            play sound ds_sfx_int
            con "Вот как: она - художница? Неплохо-неплохо."
            un "А теперь обернись."

            scene bg ds_ext_another_club_day
            show un normal pioneer at center
            with dissolve
            play sound ds_sfx_mot
            per_eye "Ранее ты не обращал внимания на этот домик. Он явно давно не использовался. Но выглядит новым."
            un "Я хотела бы приспособить этот домик под... типа студии рисования."
            con "Интересная идея, очень даже... Мы {i}должны{/i} принять в ней участие!"
            window hide
            menu:
                "Одобрить":
                    window show
                    me "Классная идея!"
                    show un shy pioneer at center
                    with dspr
                    un "Спасибо..."
                    $ ds_lp['un'] += 1
                "Отреагировать нейтрально":
                    window show
                    me "Неплохо..."
                "Раскритиковать":
                    window show
                    me "Да кому это нужно вообще?!"
                    show un sad pioneer at center
                    with dspr
                    un "Извини, что побеспокоила..."
                    $ ds_lp['un'] -= 2
                    show un cry pioneer:
                        xalign 0.5
                        yalign 0.5
                        linear 0.2 xanchor 1.0 xpos 0.0
                    with dissolve
                    "Лена в слезах убегает."
                    play sound ds_sfx_psy
                    emp "Определённо, ты очень сильно расстроил её."
                    window hide
                    
                    scene bg ext_clubs_day
                    with dissolve
                    $ renpy.pause(1.0)
                    play sound sfx_dinner_horn_processed
                    window show
                    "Ты сидишь около клуба, пока вскоре не звучит сигнал на обед."
                    jump ds_day3_lunch
        "Спросить, зачем":
            window show
            me "А что случилось?"
            show un shy pioneer at center
            with dspr
            un "Просто, понимаешь... мне нравится рисовать..."
            play sound ds_sfx_int
            con "Вот как: она - художница? Неплохо-неплохо."
            un "А теперь обернись."

            scene bg ds_ext_another_club_day
            show un shy pioneer at center
            with dissolve
            play sound ds_sfx_mot
            per_eye "Ранее ты не обращал внимания на этот домик. Он явно давно не использовался. Но выглядит новым."
            un "Я хотела бы приспособить этот домик под... типа студии рисования."
            con "Интересная идея, очень даже... Мы {i}должны{/i} принять в ней участие!"
            window hide
            menu:
                "Согласиться":
                    window show
                    me "Классная идея! Идём!"
                    show un smile pioneer at center
                    with dspr
                    un "Спасибо..."
                    $ ds_lp['un'] += 1
                "Отказаться":
                    window show
                    me "Ну нет, у меня нет времени - и желания - ходить к вожатой!"
                    show un sad pioneer at center
                    with dspr
                    un "Ладно, я пойду туда... никто не хочет мне помочь..."
                    $ ds_lp['un'] -= 1
                    hide un with dissolve
                    window hide
                    
                    scene bg ext_clubs_day
                    with dissolve
                    $ renpy.pause(1.0)
                    play sound sfx_dinner_horn_processed
                    window show
                    "Ты сидишь около клуба, пока вскоре не звучит сигнал на обед."
                    jump ds_day3_lunch
        "Отказать":
            window show
            me "Ну нет, у меня нет времени - и желания - ходить к вожатой!"
            show un sad pioneer at center
            with dspr
            un "Ладно, я пойду туда... никто не хочет мне помочь..."
            $ ds_lp['un'] -= 1
            hide un with dissolve
            window hide
            
            scene bg ext_clubs_day
            with dissolve
            $ renpy.pause(1.0)
            play sound sfx_dinner_horn_processed
            window show
            "Ты сидишь около клуба, пока вскоре не звучит сигнал на обед."
            jump ds_day3_lunch
    window hide
    scene bg ext_houses_day
    show un shy pioneer at center
    with dissolve
    $ renpy.pause(0.5)
    scene bg ext_house_of_mt_day
    show un scared pioneer at center
    with dissolve
    window show

    un "Давай ты постучишься, я боюсь..."
    window hide
    menu:
        "Постучаться":
            window show
            me "Да, хорошо."
        "Заставить Лену":
            window show
            me "Нет уж, стучись ты. Тут ничего страшного!"
            show un sad pioneer at center
            with dspr
            un "Ладно..."
            $ ds_lp['un'] -= 1
    play sound sfx_knocking_door_2
    "Но никто не открывает."
    play sound ds_sfx_mot
    res "Точно! Вожатая же занята в администрации..."
    window hide
    menu:
        "Сказать Лене":
            window show
            me "Ольга Дмитриевна же в администрацию ушла, у неё там дела..."
            show un normal pioneer at center
            with dspr
            un "Вот как? Пойдём туда, значит..."
            me "Идём..."
            $ ds_lp['un'] += 1
        "Не говорить":
            window show
            me "Cтранно... значит, в другой раз зайдём."
            show un sad pioneer at center
            with dspr
            un "Ладно... жаль..."
            hide un with dissolve
            play sound sfx_dinner_horn_processed
            "Как только Лена скрывается, звучит сигнал на обед."
            jump ds_day3_lunch
    window hide
    scene bg ext_houses_day
    show un shy pioneer at center
    with dissolve
    $ renpy.pause(0.5)
    scene bg ds_ext_admin_day
    show un scared pioneer at center
    with dissolve
    
    window show
    "Вы подходите к административному зданию."
    show mt normal pioneer far at right
    with dissolve
    "Ольга Дмитриевна как раз выходит оттуда."
    show mt normal pioneer at center
    show un scared pioneer at left
    with dspr
    mt "Привет, ребята. Вы что-то хотели?"
    window hide
    menu:
        "{check=rhetoric:8}Рассказать самому":
            if skillcheck('rhetoric', lvl_easy):
                window show
                play sound ds_sfx_int
                rhe "{result}Говори. Акцентируй внимание на необходимости поддерживать юные дарования."
                me "Ольга Дмитриевна! Тут Лена, оказывается, очень хорошо рисует."
                me "И мы считаем, что нужно её поддержать в этом!"
                me "Для чего предлагаем использовать пустующее здание напротив клуба кибернетиков."
            else:
                window show
                play sound ds_sfx_int
                rhe "{result}Тебе трудно подобрать слова, чтобы начать... Извечная проблема..."
                me "Понимаете... тут Лена хочет открыть место для рисования..."
                me "В неиспользуемом домике напротив клуба кибернетиков..."
            $ ds_lp['un'] += 1
            $ ds_skill_points['rhetoric'] += 1
        "{check=suggestion:12}Заставить Лену рассказать":
            if skillcheck('suggestion', lvl_challenging):
                window show
                play sound ds_sfx_psy
                sug "{result}Подбодри Лену. Всё хорошо. Возьми её за руку."
                "Ты шепчешь Лене на ухо."
                me "Расскажи ей сама. Твоя же идея. Всё будет хорошо - вожатая любит, когда пионеры при деле."
                show un shy pioneer at left
                with dspr
                un "Хорошо, Семён..."
                show un smile pioneer at left
                with dspr
                un "Я хочу открыть в пустом здании напротив кибернетиков художественную студию!"
                un "Фух, я это сказала..."
                $ ds_lp['un'] += 2
            else:
                window show
                play sound ds_sfx_psy
                sug "{result}Пусть она говорит, вот и всё!"
                me "Расскажи ей, Лена."
                show un shy pioneer at left
                un "Ладно..."
                un "Ольга Дмитриевна... я хочу... хочу..."
                show mt surprise pioneer at center
                with dspr
                mt "Что такое, Лена?"
                show un cry pioneer at center
                with dspr
                un "Рисовать хочу! В здании пустом!"
                un "Извините, я не могу, мне страшно!"
                $ ds_lp['un'] -= 1
            $ ds_skill_points['suggestion'] += 1
    show mt smile pioneer at center
    with dspr
    mt "Отличная идея! Можете прямо после обеда получить у меня ключи и заняться обустройством!"
    show un surprise pioneer at center
    with dspr
    un "Правда?"
    mt "Да, конечно. Это полезное дело!"
    show un normal pioneer at center
    with dspr
    un "Спасибо..."
    $ ds_un_club = True
    play sound sfx_dinner_horn_processed
    "Тут звучит призыв на обед, и вы идёте в столовую."
    jump ds_day3_lunch

label ds_day3_help_sugar:
    $ ds_whom_helped = 'fz'
    $ persistent.sprite_time = 'day'
    scene bg ds_ext_storage_day
    with dissolve
    play ambience ambience_camp_center_day

    "Ты уходишь со спортплощадки в сторону площади."
    show fz normal uniform at center
    with dissolve
    fzp "А ну стоять, пионер!"
    play sound ds_sfx_fys
    hfl "Ничего хорошего его голос тебе не предвещает."
    window hide
    menu:
        "Выслушать":
            window show
            $ ds_karma += 5
        "{check=savoir_faire:12}Сбежать":
            if skillcheck('savoir_faire', lvl_challenging):
                window show
                play sound ds_sfx_mot
                svf "{result}Беги!"
                scene bg ext_square_day:
                    zoom 1.05 anchor (48,27)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (25,25)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (-25,25)
                    repeat
                with dissolve
                "Тебе удаётся убежать из-под носа этого мужика."
                scene bg ext_clubs_day:
                    zoom 1.05 anchor (48,27)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (25,25)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (-25,25)
                    repeat
                with dissolve
                scene bg ext_clubs_day
                with dspr
                svf "Для пущей верности ты убегаешь на другую сторону лагеря, к клубам."
                $ ds_skill_points['savoir_faire'] += 1
                me "Фух..."
                $ ds_karma -= 10
                play sound sfx_dinner_horn_processed
                "Тут звучит призыв на обед, и ты идёшь в столовую."
                jump ds_day3_lunch
            else:
                window show
                play sound ds_sfx_mot
                show fz angry uniform at center
                with dspr
                svf "{result}Ты пытаешься сбежать, но он своим громадным телом перекрывает тебе путь."
                $ ds_skill_points['savoir_faire'] += 1
                fzp "И куда это ты собрался?!"
                $ ds_karma -= 10
        "{check=authority:12}Предъявить претензии":
            if skillcheck('authority', lvl_challenging):
                window show
                play sound ds_sfx_psy
                aut "{result}Он же физрук? А почему это он свои обязанности не исполняет? Зарядку там не проводит..."
                me "Что вам надо? Вы свои обязанности-то выполнили?"
                show fz angry uniform at center
                with dspr
                fzp "Ты как себе позволяешь разговаривать?"
                aut "Продолжай. Он ничего тебе не сделает."
                me "А вы знали, что физрук лагеря должен каждое утро зарядку проводить?"
                show fz rage uniform at center
                with dspr
                fzp "Ты... ты совсем берега потерял, юнец?!"
                me "Да! Может, поделиться этой ценной информацией с администрацией лагеря?.."
                show fz angry uniform at center
                with dspr
                fzp "Так, надоел ты мне! Раз хочешь - будет тебе зарядка каждое утро! Прям в 6 утра!"
                fzp "А теперь вали отсюда, и чтоб сегодня я тебя не видел."
                aut "Отлично! Теперь ты свободен!"
                $ ds_skill_points['authority'] += 1
                $ ds_morning_exercise = True
                scene bg ext_square_day
                with dissolve
                play sound sfx_dinner_horn_processed
                "Как раз когда ты подходишь к площади, раздаётся сигнал на обед."
                jump ds_day3_lunch
            else:
                window show
                play sound ds_sfx_psy
                aut "{result}Вообще, ты свободная личность."
                me "А вот не буду стоять! Делайте свою работу сами!"
                show fz rage uniform at center
                with dspr
                fzp "Нет, это как раз твоя работа! Ходишь тут, прохлаждаешься, пока остальные трудятся! А ну сюда!"
                aut "Ты не решаешься ослушаться - слишком грозен его голос."
                $ ds_karma -= 10
                $ ds_skill_points['authority'] += 1
    show fz serious uniform at center
    with dspr
    fzp "Так, будешь относить мешки с сахаром!"
    play sound ds_sfx_mot
    svf "Cбежать не получится - физрук слишком огромный, закрывает собой путь полностью."
    me "Ладно..."
    $ ds_karma += 5
    $ ds_sugar = 1
    show fz smile uniform at center
    with dspr
    fzp "Отлично! Вот мешки, рядом со складом. Приступай!"
    hide fz with dissolve
    svf "Он ушёл. Теперь можно попробовать уйти и тебе."
    window hide
    menu:
        "Уйти":
            window show
            "Ты, насвистывая, уходишь, будто ничего тебе делать не надо."
            $ ds_karma -= 10
            scene bg ext_dining_hall_away_day
            with dissolve
            play sound sfx_dinner_jingle_normal
            "Как раз когда ты подходишь к столовой, звучит горн к обеду."
            jump ds_day3_lunch
        "{check=physical_instrument:14}Потаскать мешки":
            window show
            th "Ладно, потаскаем мешки..."
    window hide
    if skillcheck('physical_instrument', lvl_legendary):
        window show
        play sound ds_sfx_fys
        phi "{result}Не без труда, но ты поднимаешь мешок и грузишь его себе на спину."
        $ ds_skill_points['physical_instrument'] += 1
        me "Дааа! Я самый сильный!"
        $ ds_up_morale()
        "Ты начинаешь двигаться в сторону столовой."
        window hide
        scene bg ext_dining_hall_away_day
        with dissolve2
        $ renpy.pause(2.0)
        window show
        "Ты подходишь к столовой..."
        phi "Давай! Давай! Давай!"
        window hide
        scene bg ext_dining_hall_near_day
        with dissolve
        $ renpy.pause(1.0)
        window show
        "Ты с трудом забираешься на ступеньки..."
        scene bg int_dining_hall_day
        show ck normal at center
        with dissolve
        ck "Ой, какой молодец! Неси на кухню!"
        $ ds_karma += 10
        scene bg ds_int_kitchen_day
        with dissolve
        "Наконец, ты опускаешь мешок."
        $ ds_sugar = 2
        me "Фууууух..."
        play sound ds_sfx_fys
        edr "Ты очень устал, тебе неплохо было бы пообедать."
        show ck smile at center
        with dissolve
        ck "Можешь идти в столовую, получишь обед первым!"
        play sound ds_sfx_psy
        vol "Как раз и время пришло."
    else:
        window show
        play sound ds_sfx_fys
        phi "{result}Ты изо всех сил пытаешься поднять мешок."
        me "Рааааз!"
        phi "Но как бы ты ни надрывался, мешок даже не думает оторваться от земли."
        $ ds_skill_points['physical_instrument'] += 1
        if not skillcheck('pain_threshold', lvl_heroic, passive=True):
            play sound ds_sfx_fys
            pat "{result}Максимум, чего ты добился - это того, что у тебя заболела спина."
            $ ds_damage_health()
        play sound ds_sfx_psy
        vol "Оставь эту гиблую затею. Пусть силач-физрук сам таскает мешки. Ты не потянешь."
        play sound sfx_dinner_horn_processed
        "Благо у тебя появляется легитимный повод уйти - обед."
        "Ты направляешься в столовую."
        $ ds_karma -= 5
    jump ds_day3_lunch

label ds_day3_help_mt:
    $ ds_whom_helped = 'mt'
    show mt smile pioneer at center
    with dissolve
    mt "Идём в административный корпус."
    "Вы направляетесь в сторону администрации."
    scene bg ds_ext_admin_day
    show mt normal pioneer at center
    with dissolve
    mt "Ну что ж, заходи!"
    window hide
    menu:
        "Войти самому":
            window show
            "Ты заходишь. Ольга Дмитриевна за тобой."
        "Пропустить Ольгу Дмитриевну вперёд":
            window show
            me "Нет, вы проходите!"
            "И ты открываешь дверь как джентльмен."
            show mt smile pioneer at center
            with dissolve
            mt "Благодарю!"
            $ ds_lp['mt'] += 1
            $ ds_karma += 5
            "Ты идёшь вслед за вожатой."
    scene bg ds_int_admin_corridor
    show mt normal pioneer at center
    with dissolve
    mt "Нам сюда."
    "Она показывает в сторону одного из кабинетов."
    "Вы проходите туда."
    scene bg ds_int_admin_day_boxes2
    show mt normal pioneer at center
    with dissolve
    mt "Так. Во-первых, нам нужно разобрать все эти коробки."
    mt "Далее - видишь папки? В них личные дела всех пионеров лагеря. Их нужно перебрать и внести данные в ЭВМ."
    mt "Самые основные - фамилия, имя, дата рождения, откуда прибыл, отряд."
    mt "Приступай, Семён!"
    window hide
    menu:
        "Спросить про неё":
            window show
            me "А вы?"
            mt "А я... а у меня дела другие есть! В соседнем кабинете!"
        "{check=authority:10}Начать протестовать":
            if skillcheck('authority', lvl_medium):
                window show
                play sound ds_sfx_psy
                aut "{result}Чего это она вздумала тебя впрягать и в таскание коробок? Ты на это не подписывался!"
                me "Ольга Дмитриевна, вы же говорили только про документы, не про коробки..."
                show mt smile pioneer at center
                with dspr
                mt "Но я же не сказала, что тебе надо будет только этим заниматься."
                show mt angry pioneer at center
                with dspr
                mt "И вообще, хочешь мешки с сахаром таскать?!"
                $ ds_skill_points['authority'] += 1
                $ ds_lp['mt'] -= 1
                $ ds_karma -= 5
                window hide
                menu:
                    "Согласиться":
                        window show
                        me "Да! Давайте!"
                        show mt surprise pioneer at center
                        with dspr
                        mt "Ну, как скажешь... сейчас отведу тебя к складам."
                        jump ds_day3_help_sugar_mt
                    "Отказаться":
                        window show
                        me "Не буду я мешки таскать!"
                        mt "Тогда займись, наконец, своим заданием!"
            else:
                window show
                play sound ds_sfx_psy
                aut "{result}Не высовывайся. Она тут главная. И ты сам согласился."
                me "Ладно, как скажете..."
        "Приступить молча":
            window show
    hide mt with dissolve
    "Ольга Дмитриевна выходит, оставляя тебя наедине с коробками."
    th "Ну что ж, приступим..."
    "Ты берёшь лежащий на столе канцелярский ножик и вскрываешь коробку за коробкой."
    "В коробках книги, журналы, папки, канцелярия. Ты раскладываешь их по шкафам."
    play sound ds_sfx_int
    lgc "Похоже, всё это недавно привезли. А значит, сюда кто-то приезжал."
    th "Почему же я не заметил этого?"
    play sound ds_sfx_mot
    per_eye "Потому что ты невнимателен!"
    th "Ладно, приступим дальше..."
    window hide
    $ renpy.pause(2.0)
    window show
    scene bg ds_int_admin_day_boxes1
    with dissolve
    th "Так, теперь, по всей видимости, пришло время разобраться с документами..."
    show mt normal pioneer at center
    with dissolve
    mt "Как дела, Семён?"
    me "Нормально... приступаю к документам..."
    show mt smile pioneer at center
    with dspr
    mt "Молодец, Семён, так держать! Продолжай!"
    hide mt with dissolve
    "Ты садишься за компьютер."
    if skillcheck('encyclopedia', lvl_up_medium, passive=True):
        play sound ds_sfx_int
        enc "{result}Местные компьютеры напоминают тебе первые «Макинтоши». Такие же слитные системный блок и монитор, причём монитор сверху. Естественно, плоских экранов здесь не наблюдается."
        $ ds_skill_points['encyclopedia'] += 1
    me "Приступим..."
    "Ты открываешь первую папку, и одновременно с этим файл «Список пионеров.БД»"
    play sound ds_sfx_mot
    per_eye "Ф.И.: ДВАЧЕВСКАЯ АЛИСА\nД.Р.: 03/IV/1972\nН.П.: пгт. Работино\nОТР.: I"
    play sound ds_sfx_int
    lgc "Ф.И. - фамилия, имя. Д.Р. - дата рождения. Н.П. - населённый пункт. ОТР. - отряд."
    "Ты вносишь данные в нужные столбики таблицы."
    per_eye "Ф.И.: УНЫЛОВА ЕЛЕНА\nД.Р.: 25/IX/1972\nН.П.: пгт. Работино\nОТР.: I"
    per_eye "Ф.И.: ФЕОКТИСТОВА СЛАВЯНА\nД.Р.: 12/V/1972\nН.П.: дер. Мятусово\nОТР.: I"
    per_eye "Ф.И.: СОВЕТОВА УЛЬЯНА\nД.Р.: 08/XII/1975\nН.П.: г. Ленинград\nОТР.: I"
    per_eye "Ф.И.: ХАЦУНЕ МИКУ\nД.Р.: 31/VIII/1972\nН.П.: г. Токио (Япония)\nОТР.: I"
    per_eye "Ф.И.: СЫРОЕЖКИН СЕРГЕЙ\nД.Р.: 23/III/1972\nН.П.: г. Москва\nОТР.: I"
    per_eye "Ф.И.: МИЦГОЛ ЕВГЕНИЯ\nД.Р.: .../.../1972\nН.П.: г. Одесса\nОТР.: I"
    per_eye "Ф.И.: ДЕМЬЯНЕНКО АЛЕКСАНДР\nД.Р.: .../.../1972\nН.П.: г. Москва\nОТР.: I"
    per_eye "Ф.И.: ПЁРСУНОВ СЕМЁН\nД.Р.: .../.../1972\nН.П.: г. Ленинград\nОТР.: I"
    play sound ds_sfx_mot
    res "О, это ты!"
    "На этом папка заканичвается. Ты переходишь к следующей."
    per_eye "Ф.И.: УНЫЛОВА АЛЁНА\nД.Р.: 25/IX/1974\nН.П.: пгт. Работино\nОТР.: II"
    "..."
    scene black with dissolve2
    window hide
    $ renpy.pause(1.0)
    window show
    scene bg ds_int_admin_day
    with dissolve2
    "Наконец, ты заканчиваешь."
    show mt normal pioneer at center
    with dissolve
    mt "Я смотрю, ты уже закончил, Семён."
    me "Да, Ольга Дмитриевна..."
    mt "Молодец! А теперь пора пообедать!"
    me "Да, спасибо..."
    play sound ds_sfx_fys
    edr "Ты измотан монотонной работой, так что с радостью воспринимаешь предложение вожатой."
    scene bg ds_ext_admin_day
    with dissolve
    "И вы идёте на обед."
    jump ds_day3_lunch

label ds_day3_help_sugar_mt:
    $ ds_whom_helped = 'fz'
    $ persistent.sprite_time = 'day'
    scene bg ds_ext_storage_day
    show mt normal pioneer at right
    with dissolve

    "Вы подходите к складу"
    show fz normal uniform at center
    with dissolve
    mt "Вот, я вам привела пионера."
    fzp "Отлично!"
    play sound ds_sfx_fys
    hfl "Ничего хорошего его голос тебе не предвещает."
    window hide
    menu:
        "Выслушать":
            window show
        "{check=savoir_faire:12}Сбежать":
            if skillcheck('savoir_faire', lvl_challenging, modifiers=[('True', -2, 'Ольга Дмитриевна видит')]):
                window show
                play sound ds_sfx_mot
                svf "{result}Беги!"
                scene bg ext_square_day:
                    zoom 1.05 anchor (48,27)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (25,25)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (-25,25)
                    repeat
                with dissolve
                "Тебе удаётся убежать из-под носа этих двоих."
                scene bg ext_clubs_day:
                    zoom 1.05 anchor (48,27)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (25,25)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (-25,25)
                    repeat
                with dissolve
                scene bg ext_clubs_day
                with dspr
                svf "Для пущей верности ты убегаешь на другую сторону лагеря, к клубам."
                $ ds_skill_points['savoir_faire'] += 1
                me "Фух..."
                $ ds_karma -= 10
                play sound sfx_dinner_horn_processed
                "Тут звучит призыв на обед, и ты идёшь в столовую."
                jump ds_day3_lunch
            else:
                window show
                play sound ds_sfx_mot
                show fz angry uniform at center
                show mt angry pioneer at right
                with dspr
                svf "{result}Ты пытаешься сбежать, но он своим громадным телом перекрывает тебе путь. И Ольга Дмитриевна мешает"
                $ ds_skill_points['savoir_faire'] += 1
                fzp "И куда это ты собрался?!"
                $ ds_karma -= 10
        "{check=authority:12}Предъявить претензии":
            if skillcheck('authority', lvl_challenging):
                window show
                play sound ds_sfx_psy
                aut "{result}Он же физрук? А почему это он свои обязанности не исполняет? Зарядку там не проводит..."
                me "Что вам надо? Вы свои обязанности-то выполнили?"
                show fz angry uniform at center
                show mt surprise pioneer at center
                with dspr
                fzp "Ты как себе позволяешь разговаривать?"
                aut "Продолжай. Он ничего тебе не сделает."
                me "А вы знали, что физрук лагеря должен каждое утро зарядку проводить?"
                show fz rage uniform at center
                with dspr
                fzp "Ты... ты совсем берега потерял, юнец?!"
                show mt normal pioneer at right
                with dspr
                mt "Ну, раз ты настаиваешь, Семён..."
                mt "Будет тебе зарядка! А то администрации расскажу!"
                me "Вот так-то!"
                mt "Но это тебя не освобождает от перетаскивания сахара!"
                th "Блин..."
                $ ds_skill_points['authority'] += 1
                $ ds_morning_exercise = True
            else:
                window show
                play sound ds_sfx_psy
                aut "{result}Вообще, ты свободная личность."
                me "А вот не буду стоять! Делайте свою работу сами!"
                show fz rage uniform at center
                show mt angry pioneer at right
                with dspr
                fzp "Нет, это как раз твоя работа! Ходишь тут, прохлаждаешься, пока остальные трудятся! А ну сюда!"
                aut "Ты не решаешься ослушаться - слишком грозен его голос."
                $ ds_karma -= 10
                $ ds_skill_points['authority'] += 1
    show mt normal pioneer at right
    with dspr
    mt "Ладно, я пойду."
    hide mt with dissolve
    show fz serious uniform at center
    with dspr
    fzp "Так, будешь относить мешки с сахаром!"
    play sound ds_sfx_mot
    svf "Cбежать не получится - физрук слишком огромный, закрывает собой путь полностью."
    me "Ладно..."
    $ ds_karma += 5
    $ ds_sugar = 1
    show fz smile uniform at center
    with dspr
    fzp "Отлично! Вот мешки, рядом со складом. Приступай!"
    hide fz with dissolve
    svf "Он ушёл. Теперь можно попробовать уйти и тебе."
    window hide
    menu:
        "Уйти":
            window show
            "Ты, насвистывая, уходишь, будто ничего тебе делать не надо."
            $ ds_karma -= 10
            scene bg ext_dining_hall_away_day
            with dissolve
            play sound sfx_dinner_jingle_normal
            "Как раз когда ты подходишь к столовой, звучит горн к обеду."
            jump ds_day3_lunch
        "{check=physical_instrument:14}Потаскать мешки":
            window show
            th "Ладно, потаскаем мешки..."
    window hide
    if skillcheck('physical_instrument', lvl_legendary):
        window show
        play sound ds_sfx_fys
        phi "{result}Не без труда, но ты поднимаешь мешок и грузишь его себе на спину."
        $ ds_skill_points['physical_instrument'] += 1
        me "Дааа! Я самый сильный!"
        $ ds_up_morale()
        "Ты начинаешь двигаться в сторону столовой."
        window hide
        scene bg ext_dining_hall_away_day
        with dissolve2
        $ renpy.pause(2.0)
        window show
        "Ты подходишь к столовой..."
        phi "Давай! Давай! Давай!"
        window hide
        scene bg ext_dining_hall_near_day
        with dissolve
        $ renpy.pause(1.0)
        window show
        "Ты с трудом забираешься на ступеньки..."
        scene bg int_dining_hall_day
        show ck normal at center
        with dissolve
        ck "Ой, какой молодец! Неси на кухню!"
        $ ds_karma += 10
        scene bg ds_int_kitchen_day
        with dissolve
        "Наконец, ты опускаешь мешок."
        $ ds_sugar = 2
        me "Фууууух..."
        play sound ds_sfx_fys
        edr "Ты очень устал, тебе неплохо было бы пообедать."
        show ck smile at center
        with dissolve
        ck "Можешь идти в столовую, получишь обед первым!"
        play sound ds_sfx_psy
        vol "Как раз и время пришло."
    else:
        window show
        play sound ds_sfx_fys
        phi "{result}Ты изо всех сил пытаешься поднять мешок."
        me "Рааааз!"
        phi "Но как бы ты ни надрывался, мешок даже не думает оторваться от земли."
        $ ds_skill_points['physical_instrument'] += 1
        if not skillcheck('pain_threshold', lvl_heroic, passive=True):
            play sound ds_sfx_fys
            pat "{result}Максимум, чего ты добился - это того, что у тебя заболела спина."
            $ ds_damage_health()
        play sound ds_sfx_psy
        vol "Оставь эту гиблую затею. Пусть силач-физрук сам таскает мешки. Ты не потянешь."
        play sound sfx_dinner_horn_processed
        "Благо у тебя появляется легитимный повод уйти - обед."
        "Ты направляешься в столовую."
        $ ds_karma -= 5
    jump ds_day3_lunch

label ds_day3_help_mi:
    $ ds_whom_helped = 'mi'
    $ persistent.sprite_time = 'day'
    scene bg ext_musclub_day
    with dissolve
    "Ты подходишь к музклубу."

    scene bg int_musclub_day
    show mi smile pioneer
    with dissolve

    mi "Ой, привет-привет, Семён-кун, ты пришёл мне помочь с наведением порядка?"
    me "Ну да..."
    play sound ds_sfx_mot
    com "Тебе с трудом удаётся выдерживать её словесный артобстрел."
    mi "Ну смотри тогда. Мы с тобой сейчас пойдём в гардероб позади тебя, там надо будет разобрать вещи."
    if ds_lp['mi'] > 0:
        mi "Заодно подберём тебе что-нибудь нарядное!"
        window hide
        menu:
            "Согласиться":
                window show
                me "Ладно..."
            "Отказаться":
                window show
                me "Зачем мне наряд? Не надо мне никакого наряда! Свой есть!"
                show mi serious pioneer at center
                with dspr
                mi "Да ладно тебе: я подберу такой, что ты будешь выглядеть сногсшибательно, Семён-кун! Ни одна девушка не оторвёт от тебя глаз!"
                if ds_lp['mi'] > 5:
                    mi "А ещё все поймут, что против меня у них нет ни одного шанса!"
                mi "В общем, не спорь!"
    
    $ persistent.sprite_time = 'night'
    scene bg ds_int_wardrobe
    show mi normal pioneer at center
    with dissolve

    play sound ds_sfx_mot
    per_eye "Здесь царит полутьма. Ты с трудом различаешь даже Мику, стоящую в двух шагах от тебя."
    if skillcheck('instinct', lvl_easy, passive=True):
        play sound ds_sfx_fys
        ins "{result}Отличный шанс! Возьми эту тяночку! Если потребуется - силой!"
        play sound ds_sfx_psy
        vol "Лучше не надо! Насильников не любят нигде!"
        window hide
        menu:
            "Начать приставать к Мику":
                window show
                me "Слушай, а может ну его, уборку, а мы с тобой займёмся более {i}приятными{/i} вещами?"
                show mi surprise pioneer at center
                with dspr
                mi "Ты о чём, Семён?"
                me "Ты такая красивая... и милая тяночка... я {i}хочу{/i} тебя..."
                show mi dontlike pioneer at center
                with dspr
                mi "Не рановато ли ты хочешь, Семён-кун? Не заслужил ещё! Вот когда-нибудь потом, когда влюбишь меня в себя, тогда может быть, а сейчас - ни-ни-ни!"
                $ ds_lp['mi'] -= 1
                $ ds_damage_morale()
                $ ds_skill_points['instinct'] += 1
                show mi normal pioneer at center
                with dspr
                mi "А теперь давай приступим!"
            "{check=physical_instrument:8}Изнасиловать Мику":
                if skillcheck('physical_instrument', lvl_easy):
                    window show
                    play sound ds_sfx_fys
                    phi "{result}Жребий брошен. Ты поваливаешь её на пол, срываешь с неё одежду..."
                    show mi scared pioneer at center
                    with dspr
                    mi "Что... что ты делаешь, Семён?"
                    me "То, что давно хотел! Я тебя хочу! И никто меня не остановит!"
                    phi "Она пыталась было закричать, но ты закрываешь ей рот."
                    show mi cry pioneer at center
                    with dspr
                    ins "И одновременно с этим, обнажив её и себя, входишь в неё."
                    scene black with dissolve2
                    jump ds_end_mi_rape
                else:
                    window show
                    play sound ds_sfx_fys
                    phi "{result}Ты пытаешься свалить Мику на пол..."
                    with hpunch
                    phi "Но она даёт тебе отпор и даёт пощёчину! Ногой!"
                    play sound ds_sfx_fys
                    pat "Тебе очень, ОЧЕНЬ больно!"
                    $ ds_damage_health()
                    $ ds_damage_morale()
                    vol "Потому что нехер насиловать!"
                    show mi rage pioneer at center
                    with dspr
                    mi "Я сделаю вид, что ничего не было, если ты поработаешь как следует!"
                    $ ds_lp['mi'] = min(ds_lp['mi'], 0)
                    $ ds_skill_points['instinct'] += 1
                    $ ds_skill_points['physical_instrument'] += 1
            "Отбросить мысль":
                window show
                th "Я не насильник! Когда придёт время - тогда случится это, а сейчас нужно подождать и склонить её к себе."
    show mi normal pioneer at center
    with dspr
    mi "Так, смотри, Семён-кун. Надо перебрать всю хранящуюся тут одежду и весь реквизит. То, что негодно, выкидываешь, то, что годно - оставляешь."
    mi "После этого отсортируешь одежду под разновидностям и разложишь по коробкам. Рубашки - сюда, брюки - сюда, платья - сюда, костюмы - сюда."
    mi "Если ты меня понял - молодец, а я побежала наводить порядок в клубе. Как закончишь - позови меня."

    hide mi with dissolve
    th "Ну что ж, посмотрим..."
    "Ты открываешь первую коробку."
    play sound ds_sfx_mot
    per_eye "Рубашка. Целая. Клади на место."
    per_eye "Штаны. С дыркой на самом неприличном месте. Выкидываем."
    per_eye "Cнова рубашка. Оторваны пуговицы. Выкидываем."
    "..."
    scene black with dissolve2
    window hide
    $ renpy.pause(2.0)
    window show
    scene bg ds_int_wardrobe
    with dissolve
    th "Вот и всё!"
    window hide
    menu:
        "Позвать Мику":
            window show
        "Просто уйти":
            window show
            "Ты выходишь через чёрный ход."
            scene ext_musclub_day
            with dissolve
            $ persistent.sprite_time = 'day'
            play sound sfx_dinner_horn_processed
            "Как раз звучит сигнал на обед. Ты идёшь в столовую."
            $ ds_lp['mi'] -= 1
            jump ds_day3_lunch
    scene bg int_musclub_day
    with dissolve
    me "Мику, я закончил!"
    show mi smile pioneer at center
    with dissolve
    mi "Ой, молодец, Семён-кун! Я тоже как раз закончила!"
    if ds_lp['mi'] <= 0:
        mi "Нам как раз пора обедать!"
        play sound sfx_dinner_horn_processed
        "Сигнал с улицы подтверждает её слова."
        me "Идём..."
        jump ds_day3_lunch
    mi "Ну что, пойдём наводить на тебе красоту, Cемён-кун?"
    window hide
    menu:
        "Согласиться":
            window show
            me "Да, давай!"
            mi "Идём!"
            $ ds_lp['mi'] += 1
        "Отказаться":
            window show
            me "Нет, я как-то не готов..."
            show mi sad pioneer at center
            with dspr
            mi "Ну как так, Семён-кун? Я же так готовилась, ещё со вчера..."
            mi "Ты точно-точно не хочешь?"
            me "Неа..."
            show mi angry pioneer at center
            with dspr
            mi "Тогда иди!"
            $ ds_lp['mi'] -= 1
            show mi normal pioneer at center
            with dspr
            mi "Приятного аппетита и удачи тебе, Семён-кун!"
            if skillcheck('empathy', lvl_trivial, passive=True):
                play sound ds_sfx_psy
                emp "{result}Ты её обидел. Она пытается не подать виду, но безуспешно."
            me "Пока..."
            scene bg ext_musclub_day
            with dissolve
            play sound sfx_dinner_horn_processed
            "Тут и обед наступает."
            $ ds_lp['mi'] -= 1
            jump ds_day3_lunch
    $ persistent.sprite_time = 'night'
    scene bg ds_int_wardrobe
    show mi smile pioneer at center
    with dissolve

    play sound ds_sfx_mot
    com "Она направляется к шкафам уверенно. Будто уже знает, что взять."

    show mi normal pioneer far at left
    with dspr
    mi "Так-так... {w}это не подойдёт... {w}это тоже... {w}вот, нашла!"

    show mi normal pioneer at center
    with dspr
    mi "Так, надень. Хотя погоди, я выйду, и ты переоденешься."
    window hide
    menu:
        "Отпустить":
            window show
            me "Хорошо."
            hide mi with dissolve
        "Предложить остаться":
            window show
            me "Да ты можешь остаться, я не стесняюсь!"
            show mi smile pioneer at center
            with dspr
            mi "Ну ладно, как скажешь. Просто я хочу, чтобы ты не чувствовал себя неудобно, но раз тебе удобно - постою тут."
            show mi normal pioneer at center
            with dspr
    "Ты скидываешь с себя пионерскую форму и надеваешь предложенный тебе костюм."
    play sound ds_sfx_int
    con "Отличный тебе костюм подобрали. И удобно - и стильно."
    show mi normal pioneer at center
    with dspr
    mi "Ну что, как тебе, Семён-кун?"
    window hide
    menu:
        "Одобрить":
            window show
            me "Мне нравится!"
            show mi smile pioneer at center
            with dspr
            mi "Я очень рада этому! Будешь выглядеть на танцах лучше всех!"
            $ ds_lp['mi'] += 1
        "Раскритиковать":
            window show
            me "Не, мне как-то не очень..."
            show mi sad pioneer at center
            with dspr
            mi "Ну как так? Ну ладно, Семён-кун, раз не нравится - подберём что-нибудь ещё!"
            $ ds_lp['mi'] -= 1
            $ ds_mi_costume = True
        "Одобрить, но не брать":
            window show
            me "Мне нравится костюм... но я его не возьму."
            show mi surprise pioneer at center
            with dspr
            mi "Почему, Семён-кун?"
            me "Не могу! Мы ещё не настолько знакомы, чтобы одежду друг другу дарить."
            show mi sad pioneer at center
            with dspr
            mi "Ну ладно, не хочешь - не надо. Потом подберём что-нибудь... когда готов будешь."
    show mi normal pioneer at center
    with dspr
    mi "А сейчас обедать пора уже! Как раз только что прозвенел горн!"
    th "И то верно..."
    $ persistent.sprite_time = 'day'
    scene bg int_musclub_day
    show mi normal pioneer at center
    with dissolve
    jump ds_day3_lunch

label ds_day3_help_mz:
    $ ds_whom_helped = 'mz'
    $ persistent.sprite_time = 'day'
    scene bg ext_library_day
    with dissolve
    "Ты идёшь в сторону библиотеки."
    th "И зачем я обрёк себя на встречу с Женей? Она же точно не будет мне рада..."

    scene bg int_library_day
    show mz sceptic glasses pioneer at center
    with dissolve
    "Ты заходишь."
    mz "О, всё-таки пришёл!"
    me "Да, как видишь, я пришёл!"
    show mz normal glasses pioneer at center
    with dspr
    mz "Ну и славно! Так, значит, я не могу дотянуться до верхних полок, поэтому давай ты! Снимаешь книгу - протираешь - возвращаешь точно не место!"
    mz "Ты меня понял?"
    me "Ну да..."
    mz "Приступай!"
    show mz normal glasses pioneer far at right
    with dspr

    "Ты подходишь к шкафу и берёшь книгу с самой верхней полки."
    "Протираешь её и кладёшь на место."
    play sound ds_sfx_int
    rhe "Может, пока поговоришь с Женей?"
    window hide
    menu ds_day3_mz_dialogue:
        set ds_menuset
        "{check=rhetoric:10}Cказать комплимент":
            if skillcheck('rhetoric', lvl_medium):
                rhe "{result}Волосы - беспроигрышный вариант. Тем более, тут они цветные!"
                me "Кстати, Жень, красивые волосы у тебя! Такие насыщенно-синие... обожаю синий цвет!"
                show mz bukal glasses pioneer far at right
                with dspr
                mz "Ты там книги протирай, а не сочиняй похвалы!"
                $ ds_lp['mz'] += 1
            else:
                rhe "{result}У тебя не получается придумать ничего красивого."
                me "Хорошо выглядишь!"
                show mz bukal glasses pioneer far at right
                with dspr
                mz "Книгами занимайся!"
            me "Ладно-ладно..."
            $ ds_skill_points['rhetoric'] += 1
            window hide
            jump ds_day3_mz_dialogue
        "Спросить про её характер":
            window show
            me "Слушай, а почему ты так злишься на весь мир?"
            show mz angry glasses pioneer far at right
            with dspr
            mz "Не твоё дело! Книгами занимайся, не мной! Я сама разберусь!"
            play sound ds_sfx_psy
            emp "Будь осторожнее. Она не откроется тебе только потому, что ты захотел."
            me "Я не хочу тебе зла... просто выяснить хочу."
            mz "Да вы все так говорите, а потом..."
            play sound ds_sfx_mot
            res "Что потом?"
            emp "Лучше воздержись от выяснения этого сейчас."
            window hide
            menu:
                "Выяснять дальше":
                    window show
                    me "Что потом? С тобой что-то случилось?"
                    show mz shyangry glasses pioneer far at right
                    with dspr
                    mz "Да, случилось... но это не твоё дело!"
                    me "Ну я же должен знать, что мне приписывают..."
                    show mz angry glasses pioneer far at right
                    with dspr
                    mz "Никто тебе ничего не приписывает! Отвянь!"
                    me "Ну скажи..."
                    mz "Не скажу! Книгами занимайся!"
                    me "Не буду, пока не скажешь!"
                    mz "Тогда катись отсюда! Доброхот мне нашёлся, тоже тут!"
                    me "Я правда хочу тебе помочь..."
                    mz "А ты мне кто? Мать, отец... а хотя даже эти не помогают..."
                    emp "Родители не помогли? Что же там было такое?"
                    me "Как так?"
                    mz "А вот так! Если у тебя такие заботливые родители, то не у всех это так!"
                    mz "Тем более, вам, парням, проще - от вас никто не требует противоречивых вещей."
                    play sound ds_sfx_int
                    enc "Похоже на риторику феминисток."
                    me "Ты о чём?"
                    mz "Да знаешь - быть непорочной, но при этом обслуживать мужика по первому зову!"
                    mz "Всегда быть красивой - но не привлекать внимания других!"
                    mz "И так далее!"
                    mz "А если не будешь соблюдать - изнасилуют, и сделают тебя виноватой!"
                    me "Причём тут изнасилование?"
                    mz "Притом! Вам, носителям болтов между ног, этого понять не дано!"
                    if skillcheck('logic', lvl_challenging, passive=True):
                        play sound ds_sfx_int
                        lgc "{result}Как будто тема с изнасилованием для неё {i}личная{/i}."
                        th "То есть, либо её знакомую изнасиловали, либо..."
                        lgc "Да. Именно."
                        emp "Поэтому отставить! Сейчас тебе, мужику, в подобные вещи лучше не лезть."
                    show mz normal glasses pioneer far at right
                    with dspr
                    mz "Cлушай - тебе правда очень повезло не пережить то, что довелось пережить мне и многим женщинам. Радуйся этому!"
                "Отступить":
                    window show
                    me "Ладно, извини... но если что - я всегда готов поговорить."
                    show mz bukal glasses pioneer far at right
                    with dspr
                    mz "Ага, всенепременно воспользуюсь."
            window hide
            jump ds_day3_mz_dialogue
        "Cпросить про послание" if ds_know_mz_el:
            window show
            me "Слушай... я вчера, когда уходил к себе, нашёл письмо..."
            show mz shyangry glasses pioneer far at right
            with dspr
            mz "Чего?! Что ты лезешь, куда не просят?!"
            $ ds_lp['mz'] -= 1
            me "Но всё-таки... что там было между вами с Электроником?"
            mz "Не твоё дело! Мне это важно, а к тебе никакого отношения не имеет!"
            me "Мне казалось, что вы с Электроником не особо близки..."
            show mz sad glasses pioneer far at right
            with dspr
            mz "Это да, но..."
            show mz angry glasses pioneer far at right
            with dspr
            mz "Это. Не. Твоё. Дело."
            if skillcheck('drama', lvl_medium, passive=True):
                play sound ds_sfx_int
                dra "{result}Cкажи ей про то, что Электроник влюблён в неё. И боится идти на контакт. Кажется, у неё есть чувства к нему."
                play sound ds_sfx_psy
                emp "А если нет? Тогда ты жестоко обманешь её!"
            window hide
            menu:
                "Соврать во благо" if ds_last_skillcheck and (ds_last_skillcheck.result):
                    window show
                    me "Знаешь, я тут говорил с ним... и мне кажется, ты ему небезразлична..."
                    show mz hope glasses pioneer far at right
                    with dspr
                    mz "Д-думаешь?"
                    me "Да! Он сам мне сказал."
                    show mz excitement glasses pioneer far at right
                    with dspr
                    mz "Так, закончишь тут с книгами сам? Мне надо бежать."
                    me "Куда?"
                    mz "Не твоё собачье дело!"
                    hide mz with dissolve
                    $ ds_lp['mz'] += 2
                    $ ds_lp['el'] += 1
                "Расспрашивать дальше":
                    window show
                    me "И всё-таки? Что там такое было?"
                    show mz rage glasses pioneer at center
                    with dspr
                    mz "ОТВЯНЬ ОТ МЕНЯ НАКОНЕЦ!"
                    me "Да ладно тебе... я же помочь хочу..."
                    show mz angry glasses pioneer at center
                    with dspr
                    mz "Все вы помочь хотите! А потом лезете, куда не надо, и ломаете всю жизнь!"
                    play sound ds_sfx_mot
                    res "Это она о чём?"
                    play sound ds_sfx_psy
                    emp "Похоже, ей довелось пережить что-то по-настоящему серьёзное."
                    me "Я никуда лезть не буду, не переживай..."
                    show mz sceptic glasses pioneer at center
                    with dspr
                    mz "А с чего я должна тебе поверить?"
                    mz "Слушай, если бы ты пережил то же, что и я - ты бы тоже никому не верил!"
                    mz "Так что не суй нос не в своё собачье дело!"
                "Отступить":
                    window show
                    me "Ладно, извини... но если что - я всегда готов поговорить."
                    show mz bukal glasses pioneer far at right
                    with dspr
                    mz "Ага, всенепременно воспользуюсь."
            window hide
            jump ds_day3_mz_dialogue
        "Молча протирать книги":
            window show
            th "Она только злиться и умеет, наверное!"
            "С этими словами ты берёшь вторую книгу. Протираешь. Кладёшь."
            "Затем третью. Четвёртую."
            "..."
            scene black with dissolve
            window hide
            $ renpy.pause(2.0)
            scene bg int_library_day
            show mz normal glasses pioneer at center
            with dissolve
            window show
    me "Я всё!"
    mz "Отлично! Можешь идти обедать!"
    mz "И приди после обеда - мы со Славей будем наводить порядок в базе данных, нужна твоя помощь!"
    play sound sfx_dinner_horn_processed
    me "Приду..."
    jump ds_day3_lunch

label ds_day3_help_ya:
    $ ds_whom_helped = 'ya'
    $ persistent.sprite_time = 'day'
    scene bg ext_beach_day
    with dissolve
    "Ты подходишь к пляжу."
    play sound ds_sfx_mot
    per_eye "В воде плещутся и играют друг с другом дети."
    th "Так, а где же Яна?.."
    show ya normal pioneer far at fright
    with dissolve
    per_eye "Она рядом с тобой. Сидит тихонько, читает книгу."
    play sound ds_sfx_psy
    emp "Старается не привлекать внимания."
    th "А ей точно нужна помощь?"
    "Cловно отвечая на твой вопрос, один из мальчиков толкает второго в воду."
    "Тому это не понравилось, и он начинает кричать, набрасываясь на первого с кулаками."
    ya "Успокойтесь..."
    play sound ds_sfx_mot
    per_hea "Голос Яны слишком тихий - даже тебе непросто расслышать её слова."
    window hide
    menu:
        "{check=authority:6}Потребовать успокоиться":
            if skillcheck('authority', lvl_trivial):
                window show
                play sound ds_sfx_psy
                aut "{result}Ты набираешь воздуха в грудь и громко, чётко произносить."
                me "ТИШИНА!"
                "Все оборачиваются на тебя."
                $ ds_lp['ya'] += 1
                $ ds_skill_points['authority'] += 1
                ya "Cпасибо..."
            else:
                window show
                play sound ds_sfx_psy
                aut "{result}Тебе даже на детей не хватает смелости прикрикнуть..."
                me "Успокойтесь, пожалуйста..."
                "Но шум и гам продолжаются."
                $ ds_skill_points['authority'] += 1
                hide ya with dissolve
                "Яне приходится заходить в воду и разделять их - что для неё оказывается непросто."
                "Но через некоторое время она наконец выходит из воды."
                show ya normal pioneer at center with dissolve
                ya "Cпасибо..."
        "{check=savoir_faire:10}Разнять детей":
                play sound ds_sfx_mot
                svf "{result}Сделаем по-другому. Забегай в воду и растащи их."
                "Ты вбегаешь в воду (благо дети не заходят далеко) и пытаешься их разнять."
                if skillcheck('savoir_faire', lvl_medium):
                    svf "Это не вызывает у тебя затруднений - это же маленькие дети."
                    me "Я сказал - успокойтесь."
                    "С этими словами ты выводишь их из воды."
                    $ ds_skill_points['savoir_faire'] += 1
                    $ ds_lp['ya'] += 1
                else:
                    svf "{result}Мальчики оказываются проворными, а их кулаки летают хаотично - тебе сложно их поймать."
                    with red_flash
                    play sound ds_sfx_fys
                    pat "В итоге тебе прилетает удар."
                    $ ds_damage_health()
                    "Но это заставляет их остановиться."
                    # ...
                    "Ты выходишь из воды, выводя мальчиков."
                    $ ds_lp['ya'] += 1
        "Молча наблюдать":
            window show
            hide ya with dissolve
            "Яна заходит в воду и аккуратно пытается разнять дерущихся."
            "У неё это занимает немало времени, но в итоге она справляется."
        "Призвать Яну быть решительнее":
            window show
            me "Скажи им громче! Они не слышат тебя!"
            show ya shy pioneer far at fright
            with dspr
            ya "Ладно... Прекратите!"
            play sound ds_sfx_mot
            per_hea "Не то, чтобы она сказала сильно громче."
            hide ya with dissolve
            "Ей приходится заходить в воду."
            "Немалых трудов ей стоило разнять детей, но в итоге у неё получается."
    show ya normal pioneer at center
    with dissolve
    ya "Тяжело с детьми..."
    me "Да, соглашусь."
    play sound ds_sfx_int
    lgc "А почему, интересно, она в принципе пытается быть вожатой, будучи явным флегматиком?"
    window hide
    menu:
        "Спросить про характер":
            window show
            me "А почему ты... скажем так, вожатая? Твоему характеру это же явно не подходит..."
            ya "Ну... мне сказали, что надо. Я и пошла."
            play sound ds_sfx_psy
            emp "Партия сказала «надо» - комсомол ответил «есть». Она - живое воплощение этого принципа."
            me "То есть, ты просто следуешь чужим инструкциям."
            ya "Ну да..."
            me "Понятно..."
        "Приободрить":
            window show
            me "Неплозо справляешься! Тебе бы чуть больше решимости - и вообще будешь идеальной вожатой."
            show ya smile pioneer at center
            with dspr
            ya "Спасибо..."
            $ ds_lp['ya'] += 1
        "Молча понаблюдать":
            window show
            "Ты просто смотришь вдаль."
            "Ни ты, ни Яна не проявляете стремления к разговору."
            show blink
            "В какой-то момент ты засыпаешь."
            scene black
            window hide
            $ renpy.pause(2.0)
            window show
            scene bg ext_beach_day
            hide blink
            show unblink
            show ya normal pioneer at center
            with dissolve
            ya "Уже обедать пора..."
            me "А, да? Идём!"
            "Ты подрываешься и идёшь в сторону столовой."
            jump ds_day3_lunch
    ya "Но я не понимаю, зачем меня назначили?.. И зачем вообще я нужна?.."
    play sound ds_sfx_psy
    emp "Экзистенциальный кризис, как он есть. Причём, похоже, перманентный."
    me "Ты о чём?"
    ya "Кто я такая? Зачем я в этом мире? Постоянно задаю себе эти вопросы..."
    play sound ds_sfx_int
    con "Да она философ!"
    ya "Зачем вообще все мы нужны? В чём смысл жизни?"
    play sound ds_sfx_psy
    vol "Её вопросы напоминают тебе о твоих потерях... о твоих переживаниях..."
    vol "И что-то неведомое {i}вынуждает{/i} тебя озвучить свои мысли."
    me "Я тоже задаюсь подобными вопросами... особенно после..."
    show ya surprise pioneer at center
    with dspr
    ya "После чего?"
    me "После разлуки..."
    show ya normal pioneer at center
    with dspr
    ya "Разлуки с кем?"
    me "C девушкой... которую я любил..."
    show ya guilty pioneer at center
    with dspr
    ya "А каково это - любовь? Никогда не испытывала подобного чувства..."
    emp "Такое ощущение, что она в принципе не видит необходимости в общении с людьми, в обществе. Ей лучше всего одной."
    me "Как, совсем никого не любила?"
    ya "Только... своего отца... и мать."
    show ya sad pioneer at center
    with dspr
    ya "Но мать я никогда не видела..."
    me "Ничего себе..."
    show ya normal pioneer at center
    with dspr
    ya "А ты уверен, что твоя девушка тебя любила?"
    me "Да, наверное... и она должна по-прежнему любить меня!"
    ya "Ты уверен? Может, лучше отбросить это?"
    me "Возможно, ты и права... Но я не могу!"
    me "Отношения с ней были всем для меня!"
    show ya surprise pioneer at center
    with dspr
    ya "Вот как... значит, так выглядит любовь?"
    me "Наверное, так..."
    show ya normal pioneer at center
    with dspr
    ya "Приятное чувство, наверное... может, и у меня получится его испытать..."
    me "Так ты же говорила про родителей..."
    ya "Да... но это не то, что ты описываешь..."
    me "И то верно."
    ya "Пора обедать уже..."
    play sound sfx_dinner_horn_processed
    "Её слова подтверждаются звуками горна."
    play sound ds_sfx_psy
    ine "Разговор с ней оставил у тебя неизгладимое впечатление... что-то странное, загадочное в ней есть..."
    th "Кто же она такая на самом деле?"
    "С этими мыслями ты идёшь на обед."
    jump ds_day3_lunch

label ds_day3_lunch:
    stop ambience fadeout 2

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_people_day 
    with dissolve

    play ambience ambience_dining_hall_full fadein 3

    window show
    play sound ds_sfx_int
    con "«Кто шагает дружно в ряд? Пионерский наш отряд!»"
    con "{i}Дружно{/i} в лагере «Совёнок» пионеры шагают в основном в столовую."
    "Столовая битком."
    show mt normal pioneer at center   with dissolve
    "На входе стоит Ольга Дмитриевна."
    con "Как почётный караул у Вечного огня."
    mt "Ну что, Семён, как сегодня потрудился?"
    me "Неплохо."
    show mt smile pioneer at center   with dspr
    mt "Молодец, молодец! То ли ещё будет!"
    play sound ds_sfx_fys
    edr "Да уж…"
    mt "Ладно, садись к девочкам."
    "Она показывает на столик рядом с колонной.{w} За ним уже сидят Славя, Ульяна и Лена."
    window hide
    menu:
        "Сесть к девочкам":
            window show      
            th "Неплохая компания.{w} По крайней мере не самая плохая..."
            play sound ds_sfx_fys
            ins "Тем более {i}девочки{/i}."
            hide mt  with dissolve
        "Сесть одному":
            window show
            play sound ds_sfx_mot
            per_eye "А нет мест больше!"
            th "Чёрт, снова придётся сидеть с кем-то..."
    "Ты берёшь обед и подходишь к ним."
    show sl normal pioneer at right, ds_seated
    show us laugh sport at center, ds_seated
    show un normal pioneer at left, ds_seated
    with dissolve
    me "Не возражаете, если я присяду?"
    play sound ds_sfx_int
    rhe "Так как садиться больше некуда, твои слова звучат наиграно."
    show sl smile pioneer at right
    with dspr
    sl "Да, конечно!"
    us "Будь любезен."
    "Лена молчит."
    "Сегодня обед состоит из борща (возможно, даже с мясом), мяса птицы (по всей видимости, курицы обыкновенной) с картошкой жареной и традиционного компота."
    play sound ds_sfx_mot
    per_tas "С каждым разом еда здесь нравится тебе всё больше."
    play sound ds_sfx_psy
    vol "Впрочем, выбирать особо не из чего, а в таком случае и нечего жаловаться на то, что есть."
    play sound ds_sfx_fys
    edr "Благо есть {i}что{/i} есть."
    show sl normal pioneer at right   with dspr
    sl "Пойдёшь сегодня на танцы?"
    if ds_dv_invite:
        th "И что делать? Я ведь договорился с Алисой..."
    window hide
    menu:
        "Ответить положительно":
            window show
            me "Ну да, пойду."
            $ ds_promise_sl = True
            show sl smile pioneer at right
            with dspr
            sl "Это хорошо!"
        "Ответить отрицательно":
            window show
            me "Нет, не хочется как-то..."
            if ds_promise_un:
                $ ds_lp['un'] -= 2
                $ ds_promise_un = False
                show un sad pioneer at left
                with dspr
                play sound ds_sfx_psy
                emp "Ты же обещал Лене прийти... она, мягко говоря, обиделась на такой поворот событий."
        "Сказать про Алису" if ds_dv_invite:
            window show
            me "У меня другие планы на вечер. С Алисой будем играть на гитаре!"
            show sl serious pioneer at right
            with dspr
            sl "То есть, она тоже не идёт?"
            play sound ds_sfx_psy
            sug "Ну ты даёшь... подставил на ровном месте Алису..."
            show sl normal pioneer at right
            with dspr
            sl "А впрочем ладно - не хочет, не надо. Проблем меньше будет!"
            sl "Но ты ведь пойдёшь?"
        "Ответить неопределённо":
            window show
            me "Не знаю..."

    show us laugh2 sport at center   with dspr
    us "Пойдёт, пойдёт! Куда он денется!"
    "Радостно вставляет Ульяна."
    me "Ты-то точно пойдёшь…"
    show us surp1 sport at center   with dspr
    us "Конечно! Не упущу случая посмотреть, как ты опростоволосишься."
    play sound ds_sfx_psy
    aut "Она попала в точку."
    $ ds_damage_morale()
    if skillcheck('composure', lvl_medium, passive=True):
        play sound ds_sfx_mot
        com "{result}Не подавай виду. Переведи внимание, например, на Лену."
    else:
        me "Ах ты... Да как ты смеешь?!"
        show sl serious pioneer at right
        with dspr
        sl "Успокойтесь!"
        "Ты решаешь обратить внимание на Лену."
    me "А ты?"
    show us laugh sport at center   with dspr
    show un smile pioneer at left   with dspr
    un "Да…"
    show sl smile pioneer at right   with dspr
    sl "Видишь, значит, и тебе тоже стоит пойти."
    aut "Славя словно не оставляет тебе выбора."
    show us grin sport at center   with dspr
    us "Не забудь фрак надеть."
    play sound ds_sfx_int
    rhe "Ульяна, видимо, так довольна своей шуткой, что громко рассмеялась."
    if not ds_mi_costume:
        play sound ds_sfx_psy
        sug "Но ведь тебе действительно нечего надеть."
        sug "Весь твой гардероб состоит из пионерской формы и зимней одежды, которая даже вечером вряд ли покажется уместной."
    window hide
    menu:
        "Сказать про костюм Мику" if ds_mi_costume:
            window show
            me "У меня есть замечательный костюм. От Мику, между прочим."
            show us laugh sport at center
            with dspr
            us "Так я и поверила!"
            us "И вообще, я же говорю - фрак наденешь!"
        "Изобразить, будто есть костюм" if not ds_mi_costume:
            window show
            me "Вообще-то у меня есть просто сногсшибательный костюм..."
            show us laugh sport at center
            with dspr
            us "Ну я же говорю - фрак наденешь!"
            us "Цилиндр ещё не забудь!"
        "{check=rhetoric:8}Подцепить в ответ":
            if skillcheck('rhetoric', lvl_easy):
                window show
                play sound ds_sfx_int
                rhe "{result}Нет ничего проще - спроси про {i}её{/i} одежду."
                me "Ты-то в чём придёшь, массовик-затейник?"
                show us laugh2 sport at center   with dspr
                us "Се-к-рет!"
                me "Платьице как на детском утреннике небось?"
                show us angry sport at center   with dspr
                rhe "Ульяна краснеет от злости – похоже, ты смог её задеть."
            else:
                window show
                play sound ds_sfx_int
                rhe "{result}Но ты не находишь, что ответить."
                me "И ничего не во фраке я пойду! В нормальной одежде!"
                me "Как будто тебе до этого есть дело."
                show us laugh2 sport at center
                with dspr
                us "Ну я же о тебе забочусь..."
                play sound ds_sfx_int
                dra "Саркастичный тон явно даёт понять - не заботится она о вас, мессир, просто издевается."
            $ ds_skill_points['rhetoric'] += 1
        "Промолчать":
            window show
            "Ты делаешь вид, будто её нет."
            show us dontlike pioneer at center
            with dspr
            us "Ну, чего молчишь как рыба?"
            show us laugh2 pioneer at center
            with dspr
            us "Ответить-то и нечего?"
            show us grin pioneer at center
            with dspr
            us "Или - о нет! - тебе вообще нечего надеть?"
            if skillcheck('composure', lvl_up_medium):
                window show
                com "{result}Держись дальше."
                show us dontlike pioneer at center
                with dspr
                us "Приём-приём! Ну не молчи!"
                $ ds_lp['us'] -= 1
            else:
                window show
                com "{result}Это оказывается последней каплей для тебя."
                me "Ах ты!"
                "Ты дёргаешься в её сторону."
    show sl serious pioneer at right   with dspr
    show un normal pioneer at left   with dspr
    sl "Ребята, хватит! Не ссорьтесь!"
    show us surp1 sport at center   with dspr
    us "Знаешь, я надену-ка костюм химзащиты, от греха подальше!"
    me "Зачем это?"
    us "А чтоб не заразиться!"
    me "Чем это ты собралась заражаться?"
    us "Слабоумием, конечно же!"
    play sound ds_sfx_psy
    emp "Похоже, Ульянка опять очень довольна своим, на её взгляд, искромётным ответом."
    window hide
    menu:
        "Развернуть против неё":
            window show
            me "Знаешь, если ты уже болеешь гриппом, то простудиться не получится."
            aut "В эту игру могут играть двое."
            show us dontlike sport at center   with dspr
            us "Это ты на что намекаешь?"
            me "Да так, ни на что…"
            "Ты хитро отводишь взгляд."
        "Отмолчаться":
            window show
            "Ты делаешь вид, будто тебя заинтересовали трещины на потолке."
            show us dontlike sport at center
            with dspr
            us "Да что ты молчишь? Правда слабоумный, что ли?"
            me "Да так, знаешь, лезут тут некоторые, мешают..."
    show us angry sport at center   with dspr
    us "То есть ты хочешь сказать?.."
    "Она опять краснеет."
    me "Я ничего не хочу сказать."
    show un surprise pioneer at left   with dspr
    un "Ребята…"
    play sound ds_sfx_psy
    vol "Если в разговор вмешивается даже Лена, то, значит, дело правда начинает принимать плохой оборот."
    us "Ты допросишься!"
    me "Чего? Что ты поумнеешь наконец?"
    hide sl 
    hide un 
    with dissolve
    window hide

    play sound sfx_borshtch

    with vpunch

    pause(1)

    show us laugh2 sport at center, ds_get_up_fast
    with dspr
    window show
    "Вместо ответа Ульянка берёт свою тарелку борща и опрокидывает тебе на голову."
    "Эндшпиль заканчивается неожиданным финалом…"
    me "Ах ты, маленькая…"

    play music music_list["awakening_power"] fadein 2

    hide us  with dissolve
    "Она вскакивает из-за стола и пытается убежать."
    window hide
    menu:
        "Побежать за ней":
            window show
        "{check=composure:13}Не реагировать":
            if skillcheck('composure', lvl_formidable):
                window show
                play sound ds_sfx_mot
                com "{result}Держись спокойно. Будь умнее. Погнавшись за ней, только навлечёшь на себя проблем."
                "Ты встаёшь и идёшь к раковинам, чтобы умыться."
                hide sl
                hide un with dissolve
                show us upset sport at center
                with dissolve
                us "Эй! Ты даже не побежишь за мной?!"
                me "Отстань!"
                us "Ну и ладно! Не очень-то и хотелось!"
                $ ds_lp['us'] -= 1
                $ ds_skill_points['composure'] += 1
                "Умывшись, ты выходишь из столовой."
                stop ambience fadeout 2
                stop music fadeout 2
                jump ds_day3_after_lunch
            else:
                window show
                play sound ds_sfx_mot
                com "{result}Ты ну никак не можешь стерпеть подобного оскорбления!"

    if skillcheck('savoir_faire', lvl_easy, passive=True):
        scene cg d3_us_dinner 
        with dissolve
        window show
        play sound ds_sfx_mot
        svf "{result}Но в этот раз у неё ничего не вышло – ты хватаешь её за руку."
        play sound ds_sfx_psy
        vol "Ну а дальше что? Не головой же её об стол!"
        "Немая сцена продолжается несколько секунд."
        window hide

        play sound sfx_throw_compote

        $ renpy.pause(1)

        window show
        "Вдруг Ульяна ловко хватает компот и плещет им тебе в лицо."
        "От неожиданности ты отпускаешь её руку."
        window hide
        $ ds_skill_points['savoir_faire'] += 1

    $ persistent.sprite_time = "day"
    scene black 
    show bg int_dining_hall_people_day :
        linear 0.05 pos (-5,-5)
        linear 0.05 pos (0,0)
        linear 0.05 pos (5,5)
        linear 0.05 pos (0,5)
        linear 0.05 pos (5,0)
        linear 0.05 pos (0,0)
        linear 0.05 pos (-5,-5)
        linear 0.05 pos (0,0)
        linear 0.05 pos (5,5)
        linear 0.05 pos (0,5)
        linear 0.05 pos (5,0)
        linear 0.05 pos (0,0)
        linear 0.05 pos (-5,-5)
        linear 0.05 pos (0,0)
        linear 0.05 pos (5,5)
        linear 0.05 pos (0,5)
        linear 0.05 pos (5,0)
        linear 0.05 pos (0,0)
        linear 0.05 pos (-5,-5)
        linear 0.05 pos (0,0)
        linear 0.05 pos (5,5)
        linear 0.05 pos (0,5)
        linear 0.05 pos (5,0)
        linear 0.05 pos (0,0)
        repeat
    with dissolve

    window show
    "Она бежит куда-то в сторону буфета, а ты – за ней."
    "Результатами вашей гонки становятся несколько опрокинутых столов, гора разбитой посуды, пять в разной степени покалеченных пионеров и полное изнеможение обеих сторон."
    th "Можно сказать, ничья."
    vol "Боевая ничья.{w} Слишком боевая ничья."
    $ ds_karma -= 10

    stop music fadeout 3

    scene bg int_dining_hall_people_day 

    "Вы стоите друг напротив друга и тяжело дышите."
    show us sad sport at center   with dissolve
    me "Больше не будешь так?!"
    show us shy sport at center   with dspr
    us "А ты?!"
    show mt angry pioneer at right   with dissolve
    "Сзади к вам незаметно подкрадывается Ольга Дмитриевна."
    th "Действительно, такой погром не мог пройти без последствий."
    mt "Ну что, довольны собой?"
    play sound ds_sfx_mot
    com "Её голос звучит спокойно, но ты уверен, что она вот-вот готова взорваться."
    show mt rage pioneer at right   with dspr
    mt "И кто всё это должен убирать теперь?!"
    com "Так и произошло."
    mt "Кто, я спрашиваю, кто?!"
    show us surp3 sport at center   with dspr:
        linear 0.2 xalign 0.4
        linear 0.2 xalign 0.5
    us "Он!"
    "Совершенно невозмутимо отвечает Ульянка."
    window hide
    menu:
        "Свалить вину на Ульяну":
            window show
            if skillcheck('authority', lvl_challenging, passive=True):
                play sound ds_sfx_psy
                aut "{result}Будь уверенным. Тогда ты будешь более убедительным."
                me "Это всё она!"
                "Уверенно заявляешь ты."
                $ ds_skill_points['authority'] += 1
            else:
                me "Она..."
                "Менее уверенно говоришь ты."
            $ ds_lp['us'] -= 1
            mt "Оба!"
            "Ставит жирную точку в не успевшем начаться споре вожатая."
            window hide
            menu:
                "{check=suggestion:15}Убедить вожатую":
                    if skillcheck('suggestion', lvl_heroic, modifiers=[('ds_last_skillcheck and (ds_last_skillcheck.result)', 1, 'Держишься уверенно'), ('ds_karma >= 50', 3, 'Вожатая доверяет тебе'), ('ds_karma <= -50', -4, 'Вожатая не доверяет тебе')]):
                        window show
                        play sound ds_sfx_psy
                        sug "{result}Говори чётко. Уверенно."
                        me "Ещё раз повторяю: я тут не причём. Это Ульяна меня спровоцировала. Я не хотел, так случайно вышло."
                        show mt normal pioneer at right
                        with dspr
                        mt "Ладно! Но только потому, что ты у меня на хорошем счету!"
                        mt "Иди!"
                        hide mt with dissolve
                        $ ds_skill_points['suggestion'] += 1
                        $ ds_lp['us'] -= 1
                        window hide
                        menu:
                            "Посмеяться над Ульяной":
                                window show
                                me "Удачи в уборке!"
                                show us dontlike sport at center
                                with dspr
                                us "Эй!"
                                hide us with dissolve
                                "Но ты её не слушаешь и выходишь"
                            "Молча уйти":
                                window show
                                show us dontlike sport at center
                                with dspr
                                us "Эй! Так нечестно! Ты должен мне помочь!"
                                hide us with dissolve
                                "Ты выходишь, не слушая возмущения Ульяны."
                        stop ambience fadeout 2
                        jump ds_day3_after_lunch
                    else:
                        window show
                        play sound ds_sfx_psy
                        sug "{result}Ну что ж, попробуй. Но вряд ли вожатая изменит свою позицию."
                        me "Ещё раз повторяю: это всё она! Это не я!"
                        show mt angry pioneer at right
                        with dspr
                        mt "Я всё сказала! Не пытайся меня переубедить: это бесполезно!"
                        hide mt with dissolve
                        me "Да как так-то!"
                        show us laugh sport at center
                        with dspr
                        us "А вот так!"
                        $ ds_skill_points['suggestion'] += 1
                "Отступить":
                    window show
                    th "Ну ладно..."
        "Взять вину на себя":
            window show
            me "Извините... это я вывел из себя Ульяну, вот она и взбесилась."
            $ ds_lp['us'] += 1
            mt "Без разницы! Убирать будете всё равно вы оба!"
        "Промолчать":
            mt "Ты тоже поучаствовала! Так что убирать будете оба!"
    "Ульянка, кажется, вовсе не считает себя виноватой."
    show us surp2 sport at center   with dspr
    us "Вот ещё!{w} Не буду я ничего убирать!"
    us "Это он всё! Он начал!"
    me "Вот и нет!"
    show us dontlike sport at center   with dspr
    us "Вот и да!"
    show mt angry pioneer at right   with dspr
    mt "Я не собираюсь разбираться в этих глупостях!"
    mt "Семён, иди возьми швабру, совочек, тряпку и так далее в кладовке, а ты!!!"
    show mt rage pioneer at right   with dspr
    play sound ds_sfx_psy
    emp "Она смотрит на Ульяну таким взглядом, что девочку можно только пожалеть."
    show us fear sport at center   with dspr:
        parallel:
            linear 0.5 yalign -0.2
        parallel:
            linear 0.5 xalign 0.4
    mt "Ты!!!{w} Немедленно начинай собирать разбитую посуду!"
    "Ольга Дмитриевна отдышалась немного и продолжает."
    show mt angry pioneer at right   with dspr
    mt "От тебя одни проблемы!{w} Сколько раз я тебе говорила…"
    window hide
    menu:
        "Дослушать":
            window show
            mt "...что пионерка должна соблюдать правила, должна быть примером для подрастающего поколения."
            mt "Ну кто возьмёт в жёны такую непослушную егозу?"
            play sound ds_sfx_int
            dra "Ольга Дмитриевна явно не учитывает, что такое привлечение внимания характерно для детей."
            mt "Ты мне объясни, зачем ты это творишь? Почему бы не заняться чем-нибудь созидательным?"
            mt "Даже твоя подружка Алиса - и та играет на гитаре! А ты?"
            mt "Я же тебе даже спортклуб отдала, чтобы ты могла выпустить свою энергию!"
            mt "Почему все дети твоего отряда как дети, а ты?.."
            play sound ds_sfx_int
            lgc "Кажется, вожатая забыла про то, что в отряде Ульяна намного младше остальных."
            mt "Короче, всё, иди!"
            "Ульяна плетётся убирать осколки, а ты идёшь в кладовую."
        "Уйти":
            window show
    hide mt 
    hide us 
    with dissolve
    jump ds_day3_punishment1

label ds_day3_punishment1:
    $ persistent.sprite_time = 'day'
    scene bg ds_int_dininghall_door_day
    with dissolve
    $ ds_punished = True
    "Пока Ольга Дмитриевна, отчитав Ульяну, выходит, ты идёшь в кладовку, которая находится рядом с выходом."
    play sound ds_sfx_mot
    svf "А может сбежать?"
    play sound ds_sfx_psy
    vol "Ольга Дмитриевна уже вас поймала."
    play sound ds_sfx_psy
    sug "Но ты-то ни в чём не виноват."
    sug "Конечно, «образцовый пионер» - это не про тебя, но по сравнению с Ульянкой..."
    play sound ds_sfx_int
    lgc "В любом случае всё спишут на неё."

    window hide
    menu:
        "{check=savoir_faire:14}Сбежать одному":
            if skillcheck('savoir_faire', lvl_legendary, modifiers=[("ds_lp[['us'] < 0", -2, 'Ульяна палит')]):
                window show
                play sound ds_sfx_mot
                svf "{result}Тебе удаётся незаметно прошмыгнуть в дверь, даже не хлопнув ею."
                scene bg ext_dining_hall_near_day
                with dissolve
                th "Получается, всё? Я свободен?"
                $ ds_skill_points['savoir_faire'] += 1
                "И ты идёшь куда-нибудь."
                $ ds_lp['us'] -= 1
                $ ds_karma -= 10
                jump ds_day3_after_lunch
            else:
                window show
                play sound ds_sfx_mot
                svf "{result}Ты рвёшься в сторону двери..."
                show us angry sport at center
                with dissolve
                us "Куда собрался? А помогать мне кто будет?"
                show us dontlike sport at center
                with dissolve
                us "И даже не позвал меня с собой сбежать!"
                me "Пусти меня!"
                show ck serious far at left
                with dissolve
                ck "Она права. Ты должен поработать вместе с ней!"
                $ ds_karma -= 10
                $ ds_lp['us'] -= 1
                $ ds_skill_points['savoir_faire'] += 1
                hide us
                hide ck
                with dissolve
                th "Не прокатило..."
        "{check=savoir_faire:16}Сбежать с Ульяной":
            window show
            me "Ульян! Пс!"
            "Ты говоришь максимально тихо."
            show us surprise sport at center
            with dissolve
            us "Что такое?"
            me "Я предлагаю сбежать!"
            show us smile2 sport at center
            with dspr
            us "О, давай! Веди!"
            $ ds_lp['us'] += 1
            th "Так..."
            if skillcheck('savoir_faire', lvl_godly):
                window show
                play sound ds_sfx_mot
                svf "{result}Вам удаётся незаметно прошмыгнуть в дверь, даже не хлопнув ею."
                scene bg ext_dining_hall_near_day
                show us laugh sport at center
                with dissolve
                us "Получилось! Получилось!"
                $ ds_skill_points['savoir_faire'] += 1
                me "Ты потише!.."
                show us smile sport at center
                with dspr
                us "Ладно-ладно!"
                us "Я побежала! Пока!"
                hide us with dissolve
                "Ты тоже идёшь куда-нибудь."
                $ ds_karma -= 10
                $ ds_skill_points['savoir_faire'] += 1
                jump ds_day3_after_lunch
            else:
                window show
                play sound ds_sfx_mot
                svf "{result}Ты рвёшься в сторону двери..."
                show ck serious far at left
                with dissolve
                ck "Куда это вы собрались?!"
                show us upset sport at center
                with dspr
                us "Ну вот, не вышло..."
                ck "Так, давайте убираться!"
                $ ds_karma -= 10
                $ ds_skill_points['savoir_faire'] += 1
                hide us
                hide ck
                with dissolve
                th "Не прокатило..."
        "Остаться с Ульяной":
            window show
            th "Лучше всё же останусь и помогу Ульяне."
            play sound ds_sfx_psy
            emp "Тем более, что и твоя вина есть."
            play sound ds_sfx_mot
            com "Потому что ты не удержался от пробежки!"
    play sound sfx_open_cupboard

    pause(1)

    window show
    "Открыв шкаф, ты берёшь метлу, швабру и совок."
    show us sad sport at center   with dissolve
    me "Она ушла?"
    show us dontlike sport at center   with dspr
    us "Как видишь!"
    play sound ds_sfx_psy
    emp "Ульянка выглядит расстроеной, весь её детский задор куда-то исчез."
    me "Ладно, подожди, сначала пойду отмоюсь."
    hide us  with dissolve
    "Ты бросаешь на неё злобный взгляд и направляешься к выходу."
    window hide

    with fade

    window show
    "Смыв с себя остатки обеда, ты возвращаешься в столовую."
    me "Ну, ничего не поделаешь – придётся убираться."
    show us angry sport at center   with dspr
    us "Это всё из-за тебя!"
    play sound ds_sfx_mot
    com "Она смотрит так, что у тебя невольно мурашки побежали по всему телу."
    me "Конечно!"
    me "Я во всём виноват!{w} Я же у нас местное стихийное бедствие."
    show us sad sport at center   with dspr
    us "Помолчи уж…"
    play sound ds_sfx_int
    lgc "Странно, что она не отлынивает от уборки."
    lgc "Ульянка могла спокойно оставить тебя одного и убежать, но почему-то, напротив, старательно собирает осколки тарелок, моет пол, поднимает стулья и столы."
    "Она делает всё так быстро, что ты еле успеваешь за ней."
    me "Что-то ты чересчур стараешься."
    show us dontlike sport at center   with dspr
    us "А чтобы побыстрее закончить, дурень!"
    "Голос её звучит всё так же недовольно."
    play sound ds_sfx_psy
    aut "Используй свой авторитет. Объясни ей, что так вести себя нехорошо."
    window hide
    menu:
        "Начать воспитывать":
            window show
            me "Слушай, ну ты же понимаешь, что нельзя себя так вести…{w} По крайней мере доводить до подобного…"
            show us surp1 sport at center   with dspr
            us "А я ничего такого и не делала!{w} Это же ты меня ребёнком обозвал."
            hide us  with dissolve
            "Ульяна берёт ведро с тряпкой и уходит в дальний конец столовой."
            emp "Похоже, обиделась."
            $ ds_lp['us'] -= 1
            play sound ds_sfx_int
            vic "Окинув взглядом гору битой посуды, ты понимаешь, что дел вы действительно натворили."
            th "Хорошо, хотя бы ложки и вилки металлические – если что, будет чем есть.{w} Но вот только из чего..."
        "Промолчать":
            window show
        "Похвалить":
            window show
            me "Неплохо ты придумала!"
            "Молчание становится ответом тебе."
            th "Обиделась..."
    $ ds_after_lunch_who = 'us'
    us "Слушай…"
    "Кричит тебе Ульяна."
    "Ты подходишь к ней поближе."
    show us shy2 sport at center   with dissolve

    stop ambience fadeout 2

    play music music_list["two_glasses_of_melancholy"] fadein 1

    us "А почему ты меня так не любишь?"
    show us normal sport at center   with dspr
    window hide

    $ renpy.pause(1)

    window show
    emp "Её лицо становится настолько серьёзным, что ты уже готов поверить – это не просто очередной розыгрыш."
    me "Почему ты так решила?"
    show us shy2 sport at center   with dspr
    us "Не знаю, поэтому и спрашиваю."
    window hide
    menu:
        "Это неправда":
            window show
            me "Я тебя не не люблю.{w} Просто иногда ты себя так ведёшь…{w} Ну, сама знаешь."
            show us surp3 sport at center   with dspr
            us "Как?{w} Не знаю."
            "Она поднимает на тебя полные любопытства глаза."
            me "Ну, зачем, скажем, было обливать меня компотом?"
            show us grin sport at center   with dspr
            us "Так ты же сам напросился."
            "Впервые за всё время уборки она улыбается."
            $ ds_lp['us'] += 1
            me "Да, точно..."
            me "Ну, и какой реакции ты тогда ждёшь от окружающих?"
            us "Никакой."
        "Из-за поведения":
            window show
            me "Просто ты так себя ведёшь..."
            show us supr3 sport at center
            with dspr
            us "Как?"
            me "Отвратительно! Ну как так себя можно вести?!"
            show us upset sport at center
            with dspr
            us "Мне скучно просто! Вечно какие-то дела, дела, дела, а развлечений толком нет!"
            us "Вот я и развлекаю себя!"
            emp "Что естественно для ребёнка."
            me "Но ты же должна понимать, что есть правила, и за их несоблюдение наказывают..."
            show us dontlike sport at center
            with dspr
            us "Вот и соблюдай свои скучные правила!"
            $ ds_lp['us'] -= 1
        "Сама по себе":
            window show
            me "Просто не нравишься ты мне! Не в моём вкусе!"
            show us sad sport at center
            with dspr
            us "В смысле? Я тебе не нравлюсь?!"
            show us cry sport at center
            with dspr
            emp "А вот тут ты её расстроил по-настоящему."
            emp "Впрочем, она ребёнок, должна отойти вскоре."
            me "Ульян..."
            us "Отстань! Не хочу видеть тебя!"
            $ ds_lp['us'] -= 2
    hide us  with dissolve
    "В разговоре была поставлена жирная точка, и ты молча продолжаешь убираться."
    window hide

    with fade

    jump ds_day3_punishment

label ds_day3_punishment2:
    $ persistent.sprite_time = 'day'
    scene bg int_dining_hall_day
    show ck smile at center
    show us sad sport at right
    with dissolve

    ck "А вот и помощнички пришли!"
    us "Угу..."
    show ck normal at center
    with dspr
    ck "Значит так. Идите на кухню, там мешки с картошкой. Вам нужно её начистить."
    play sound ds_sfx_mot
    res "Чего?"
    show us dontlike sport at right
    with dspr
    us "Чего? Не буду я картошку чистить!"
    ck "Надо, моя милая, надо."
    hide ck with dissolve
    play sound ds_sfx_mot
    svf "А может сбежать?"
    play sound ds_sfx_psy
    vol "Идея так себе - тебя уже поймали, просто накажут сильнее."

    window hide
    menu:
        "{check=savoir_faire:14}Сбежать одному":
            if skillcheck('savoir_faire', lvl_legendary, modifiers=[("ds_lp[['us'] < 0", -2, 'Ульяна палит')]):
                window show
                play sound ds_sfx_mot
                svf "{result}Тебе удаётся незаметно прошмыгнуть в дверь, даже не хлопнув ею."
                scene bg ext_dining_hall_near_day
                with dissolve
                th "Получается, всё? Я свободен?"
                $ ds_skill_points['savoir_faire'] += 1
                "И ты идёшь куда-нибудь."
                $ ds_lp['us'] -= 1
                $ ds_karma -= 10
                jump ds_day3_after_lunch
            else:
                window show
                play sound ds_sfx_mot
                svf "{result}Ты рвёшься в сторону двери..."
                show us angry sport at center
                with dissolve
                us "Куда собрался? А помогать мне кто будет?"
                show us dontlike sport at center
                with dissolve
                us "И даже не позвал меня с собой сбежать!"
                me "Пусти меня!"
                show ck serious far at left
                with dissolve
                ck "Она права. Ты должен поработать вместе с ней!"
                $ ds_karma -= 10
                $ ds_lp['us'] -= 1
                $ ds_skill_points['savoir_faire'] += 1
                hide us
                hide ck
                with dissolve
                th "Не прокатило..."
        "{check=savoir_faire:16}Сбежать с Ульяной":
            window show
            me "Ульян! Пс!"
            "Ты говоришь максимально тихо."
            show us surprise sport at center
            with dissolve
            us "Что такое?"
            me "Я предлагаю сбежать!"
            show us smile2 sport at center
            with dspr
            us "О, давай! Веди!"
            $ ds_lp['us'] += 1
            th "Так..."
            if skillcheck('savoir_faire', lvl_godly):
                window show
                play sound ds_sfx_mot
                svf "{result}Вам удаётся незаметно прошмыгнуть в дверь, даже не хлопнув ею."
                scene bg ext_dining_hall_near_day
                show us laugh sport at center
                with dissolve
                us "Получилось! Получилось!"
                $ ds_skill_points['savoir_faire'] += 1
                me "Ты потише!.."
                show us smile sport at center
                with dspr
                us "Ладно-ладно!"
                us "Я побежала! Пока!"
                hide us with dissolve
                "Ты тоже идёшь куда-нибудь."
                $ ds_karma -= 10
                $ ds_skill_points['savoir_faire'] += 1
                jump ds_day3_after_lunch
            else:
                window show
                play sound ds_sfx_mot
                svf "{result}Ты рвёшься в сторону двери..."
                show ck serious far at left
                with dissolve
                ck "Куда это вы собрались?!"
                show us upset sport at center
                with dspr
                us "Ну вот, не вышло..."
                ck "Так, давайте убираться!"
                $ ds_karma -= 10
                $ ds_skill_points['savoir_faire'] += 1
                hide us
                hide ck
                with dissolve
                th "Не прокатило..."
        "Остаться с Ульяной":
            window show
            th "Лучше всё же останусь и помогу Ульяне."
            play sound ds_sfx_psy
            emp "Тем более, что и твоя вина есть."
    $ ds_after_lunch_who = 'us'
    scene bg ds_int_kitchen_day
    show us upset sport at center
    with dissolve
    us "Ну и где тут эта картошка?"
    play sound ds_sfx_mot
    per_eye "Она прямо рядом с вами."
    me "Да вот она."
    us "Ну что ж, давай приступать..."
    play sound ds_sfx_psy
    emp "Весь её задор пропал. Она явно не планировала сегодня чистить картошку. Ребёнок же - хочется развлечений."
    play sound ds_sfx_int
    vic "Картошки тут килограммов пять, не меньше. Вы тут явно до вечера просидите."

    scene cg ds_day3_us_potato_1
    with dissolve
    "Вы усаживаетесь: Ульяна на стул, ты на ящик - и приступаете к чистке картошки."
    play sound ds_sfx_psy
    vol "Работа на редкость монотонная - почистил картофелину, бросил в таз, взял новую. И так до бесконечности."
    vol "Немудрено, что ни ты, ни Ульяна не испытываете удовольствия от подобной работы."
    us "Сколько там ещё этой картошки?.."
    me "Много..."
    us "Ну вот почему ты мне не позволил убежать?"
    me "Потому что это небезопасно... да и думаешь, тебе было бы легче, когда бы тебя поймали?"
    us "Меня бы не поймали, если бы не ты!"
    me "Ага, конечно...  Поезд так-то куда-то едет, а не в небытие!"
    me "И вообще, увезли бы тебя куда-нибудь на Дальний Восток - что бы ты делала?"
    us "Уж точно не чистила бы картошку!"
    play sound ds_sfx_psy
    emp "Как бы ты её ни убеждал - её детская логика в любом случае сделает виноватым тебя."
    window hide
    menu:
        "Извиниться":
            window show
            me "Ладно, извини..."
            us "Да что толку от твоих извинений? Картошку лучше чисти быстрее!"
        "Промолчать":
            pass
    window hide
    $ renpy.pause(1.5)
    window show
    us "Слушай, а давай кто быстрее?"
    play sound ds_sfx_psy
    sug "С одной стороны идея заманчивая - соревновательный элемент разбавит муторность процесса."
    play sound ds_sfx_psy
    aut "Заодно сможешь показать превосходство над ней!"
    play sound ds_sfx_psy
    vol "Но как бы вы дров не наломали в пылу борьбы!"
    window hide
    menu:
        "Согласиться":
            window show
            me "А давай!"
            us "Готов потерпеть поражение?"
            me "Нет, это ты проиграешь!"
            us "Нет, ты!"
            me "Старт!"
            $ ds_lp['us'] += 1
            "И вы начинаете чистить картошку на скорость."
            "Первой жертвой битвы пало качество работы - шкурки и ошмётки картошки начали лететь во все стороны. От каждой картофелины остаётся максимум половина."
            us "А я быстрее!"
            me "Нет, я быстрее!"
            "Вы совершенно не замечаете результатов вашего боя. Пока..."
            play sound sfx_brass_drop
            "Таз переворачивается, а вода из него разливается по полу."
            scene cg ds_day3_us_potato_2
            with dissolve
            us "Ой..."
            us "Это всё ты!"
            scene bg ds_int_kitchen_day
            show ck serious at center
            show us angry sport at right
            with dissolve
            "Ты хотел было возразить, но тут приходит повариха."
            ck "И что вы наделали?"
            us "Это всё он!"
            me "Это она..."
            ck "Неважно! Давайте убирайте за собой!"
            hide ck
            show us upset sport at center
            with dissolve
            us "Это всё ты!"
            me "Ты же предложила..."
            us "А ты... а ты..."
            play sound ds_sfx_int
            "Она не знает, что ответить."
            us "Давай убирайся уже!"
            "Вы приступаете к уборке."
            show us sad sport far at right
            with dspr
            "Ты берёшь швабру и принимаешься убирать воду, пока Ульяна ходит по кухне и собирает шкурки."
            show us sad sport far at center
            with dspr
            "А шкурки оказываются разбросаны по всей кухне, так что её работа оказывается непростой."
            show us sad sport far at left
            with dspr
            "Как и твоя - целый таз воды оказался на полу."
            show us sad sport far at center
            with dspr
            window hide
            $ renpy.pause(1.5)
        "Отказаться":
            window show
            me "Нет уж, давай просто почистим картошку!"
            us "Какой ты скучный... слов нет просто..."
            $ ds_lp['us'] -= 1
            us "А, я знаю - ты просто боишься!"
            if skillcheck('authority', lvl_easy, passive=True):
                aut "Она неправа. Прописью: она не-пра-ва."
                me "Ничего я не боюсь! Это ты боишься!"
                us "И чего же я боюсь по-твоему? Тебя?!"
                "Она заливается смехом."
                me "Подкроватного монстра. Или привидений!"
                us "Вообще-то я не пятилетка, чтобы бояться этого!"
                $ ds_skill_points['authority'] += 1
            else:
                me "Не боюсь я... просто не хочу..."
                us "Боишься-боишься! Ты просто трус!"
                $ ds_damage_morale()
            "На этом её вновь охватывает тоска, и она умолкает."
            "Вы продолжаете чистить картошку."
            window hide
            $ renpy.pause(2.0)
    scene bg ds_int_kitchen_day
    show us normal sport at center
    with dissolve
    window show
    "И вот вы заканчиваете работу. Уже подходит время ужина."
    us "Наконец-то... Всё, я пошла!"
    hide us with dissolve
    "И она уходит. Ты следуешь за ней."
    jump ds_day3_dinner

label ds_day3_punishment_return:
    $ persistent.sprite_time = 'day'
    scene bg int_dining_hall_day
    with dissolve
    window show
    th "Лучше вернусь - нехорошо как-то бросать Ульяну одну..."
    show us upset sport at center
    with dissolve
    us "Надо же, вернулся!"
    play sound ds_sfx_psy
    emp "Она обижена на тебя за то, что ты во-первых сбежал, а во-вторых, не потащил с собой её."
    me "Да, вернулся..."
    window hide
    menu:
        "Извиниться":
            window show
            me "Извини, что ушёл."
            show us smile sport at center
            with dspr
            us "Ладно, так уж и быть, прощу тебя! Я добрая сегодня!"
            $ ds_lp['us'] += 1
        "Промолчать":
            window show
    "Ты идёшь к шкафу, берёшь метлу и совок и идёшь убираться."
    window hide
    $ renpy.pause(3.0)
    jump ds_day3_punishment

label ds_day3_punishment:
    window show
    $ ds_after_lunch_who = 'us'
    "Вам потребовалось несколько часов, чтобы навести в столовой марафет."
    "И вот наконец вся битая посуда собрана, столы и стулья расставлены, пол вымыт."
    show us normal sport at center   with dissolve
    "Вы с Ульянкой сидите рядом с буфетом и отдыхаете."
    me "Вот видишь, сколько приходится потратить сил из-за одной глупой выходки."
    us "А я совсем и не устала!"
    play sound ds_sfx_int
    vic "Пот, струящийся по её лицу, говорит совершенно об обратном."
    me "Что же, рад за тебя…"
    us "Чем займёмся дальше?"
    me "Ты – не знаю, а я пойду…"
    show us surp3 sport at center   with dspr
    us "Нет! Ещё не всё!"
    us "Ты должен…"
    show us shy2 sport at center   with dspr
    "Она заминается."
    show us surp1 sport at center   with dspr
    us "Мне ещё помочь!"
    me "Придумываешь очередную глупость?"
    show us laugh2 sport at center   with dspr
    us "Точно!"
    "Она широко улыбается."
    me "Тут я тебе не помощник.{w} Мне на сегодня одного наказания уже хватит."
    show us laugh sport at center   with dspr
    us "А давай так!{w} Если ты поможешь мне сейчас, я больше не буду над тобой прикалываться!"
    th "Вариант, конечно, выглядит заманчиво"
    play sound ds_sfx_int
    dra "Но, кажется, эта дева обмануть вас хочет, мессир."
    th "Ради интереса можно и спросить."
    me "И в чём же состоит твой хитрый план?"
    show us grin sport at center   with dspr
    us "Давай украдём конфеты!"
    me "Что?!"
    play sound ds_sfx_int
    lgc "Чего-то такого от неё и стоило ожидать."
    th "Конфеты – детям…"
    show us laugh sport at center   with dspr
    us "Сейчас как раз повариха пойдёт мусор выбрасывать, так что нас никто не заметит!"
    window hide
    menu:
        "{check=interfacing:10}Согласиться":
            window show
            me "А давай! Только потом поделим поровну?"
            show us grin sport at center
            with dspr
            $ ds_lp['us'] += 1
            us "Как скажешь!"
            hide us with dissolve
            "Пока Ульяна дежурит у двери, ты подходишь к шкафу..."
            window hide
            if skillcheck('interfacing', lvl_medium):
                window show
                inf "{result}И резкими чёткими движениями распахиваешь шкаф, хватаешь конфеты, кладёшь их себе в карман и закрывааешь дверь, будто всё так и было."
                $ ds_skill_points['interfacing'] += 1
                $ ds_lp['us'] += 1
                "Ты подходишь к Ульяне."
            else:
                window show
                inf "{result}Ты открываешь дверцу и начинешь искать конфеты... но безуспешно."
                us "Быстрее давай! Сюда идут!"
                me "Да не могу я найти."
                show us dontlike sport at center
                with dspr
                us "Эх ты... давай я!"
                "Вы меняетесь местами. Ульяне быстро удаётся найти нужный кулёк."
                "Она подпрыгивает к тебе и всучивает его тебе в карман за секунду до появления поварихи."
            me "И что мы будем делать?"
            show us laugh sport at center
            with dspr
            us "Догоняй!"
            "И прежде чем ты успеваешь как-либо отреагировать, она выхватывает у тебя конфеты и выбегает из столовой."
            th "Вот же зараза..."
            window hide
            menu:
                "Погнаться за ней":
                    window show
                    play sound ds_sfx_fys
                    edr "У девочки приличная фора, но ты вкладываешь в погоню все силы."

                    stop ambience fadeout 2
                    if not ds_caught_us:
                        th "Второй раз я ей не проиграю!"
                    else:
                        th "Догоним её на бис!"
                    window hide
                "Доложить поварихе":
                    window show
                    "Ты кричишь что есть мочи."
                    me "Тут конфеты украли!"
                    show ck serious at center
                    with dspr
                    ck "Что случилось? Кто украл?"
                    me "Та несносная красноволосая девчонка!"
                    ck "Вот как... и чего же ты её не догоняешь?"
                    me "Да я не догоню её..."
                    show ck serious at center
                    with dspr
                    ck "Ольга Дмитриевна разберётся... вот только победитель вчерашнего турнира останется без конфет."
                    play sound ds_sfx_mot
                    res "Конфеты были призом за турнир? Да, неудача..."
                    "Тем временем в столовой собираются люди. Подходит время ужина."
                    jump ds_day3_dinner
                "Забить":
                    window show
                    "Ты остаёшься в столовой. Подходит время ужина."
                    window hide
                    $ persistent.sprite_time = "day"
                    scene bg int_dining_hall_people_day 
                    with dissolve

                    play ambience ambience_dining_hall_full fadein 3

                    window show
                    "Постепенно народу прибавляется."
                    "Ты начинаешь прикидывать, куда можешь присесть."
                    show ck serious at center
                    with dissolve
                    ck "Пионер, а ты не видел конфеты? Лежали в шкафу, а теперь их нет."
                    window hide
                    menu:
                        "{check=drama:10}Изобразить непонимание":
                            if skillcheck('drama', lvl_medium):
                                window show
                                dra "{result}У вас получается убедительно изобразить, будто вы впервые об этих конфетах слышите."
                                me "Понятия не имею, о каких вы конфетах."
                                $ ds_skill_points['drama'] += 1
                                show ck normal at center
                                with dspr
                                ck "Ясно... Похоже, победитель вчерашнего турнира останется без приза."
                                hide ck with dissolve
                                play sound ds_sfx_mot
                                res "Так это приз был?"
                            else:
                                window show
                                dra "{result}Ваше лицо, мессир, - оно как открытая книга. Вся ваша ложь отчётливо видна."
                                me "Я не знаю..."
                                ck "Ага, как же... Наверное, ты и украл."
                                $ ds_skill_points['drama'] += 1
                                $ ds_karma -= 5
                                me "Не крал я ничего!"
                                ck "Разберётся Ольга Дмитриевна."
                                ck "А пока я могу сказать лишь то, что победитель турнира останется без приза."
                                play sound ds_sfx_mot
                                res "Так это приз был?"
                        "Взять вину на себя":
                            window show
                            me "Да знаете... это я их съел, пока убирался..."
                            ck "Вот как? Ты же понимаешь, что оставил победителя турнира без приза?"
                            play sound ds_sfx_mot
                            res "Без приза?"
                            ck "Ладно, это уже дело твоей вожатой. А пока иди ужинай!"
                            hide ck with dissolve
                            $ ds_karma -= 10
                        "Сказать, что не знаешь":
                            window show
                            me "Я не видел... просто заметил, что конфеты пропали, и всё!"
                            ck "Учитывая, что тут были только двое... это или ты, или ты рыжеволосая девчонка!"
                            play sound ds_sfx_int
                            lgc "Тут не нужно быть Сократом, чтобы сделать вывод, кто тогда украл конфеты."
                            ck "В общем, я скажу Ольге Дмитриевне, она разберётся."
                            ck "А ты иди ужинать!"
                            hide ck with dissolve
                        "Оговорить Алису":
                            window show
                            me "Знаю, знаю! Вы видели рыжеволосую девушку, с хвостиками."
                            show ck normal at center
                            with dspr
                            ck "Конечно, видела, припоминаю такую..."
                            me "Ну так вот, пока мы убирались, она пролезла в окно, выкрала конфеты и убежала!"
                            ck "Вот как... Значит, она лишила победителя турнира приза!"
                            ck "Вожатая разберётся, в общем."
                            $ ds_framed_dv = True
                            $ ds_lp['dv'] -= 2
                        "{check=conceptualization:11}Назвать фантастичную причину":
                            if skillcheck('conceptualization', lvl_up_medium):
                                window show
                                play sound ds_sfx_int
                                con "{result}Нашествие инопланетян! Вторжение империалистов! У тебя столько идей!"
                                $ ds_skill_points['conceptualization'] += 1
                                me "Вы не поверите, что тут произошло!"
                                me "Вот убираемся мы тут с Ульяной. И тут - бац!"
                                me "Заходит шпион! Американский! Чернокожий, в костюме, с портфелем."
                                me "Открывает свой чемодан, кладёт туда конфеты, в потом облучает нас какой-то штукой, от чего мы не могли ему противодействовать. И был таков!"
                                show ck laugh at center
                                with dspr
                                ck "Я не знаю, как на это реагировать! Такое уморительное враньё! Может, тебе в писатели податься?"
                                show ck serious at center
                                with dspr
                                ck "А если серьёзно - поздравляю, победитель турнира остался без приза! Не знаю, что с этим вожатая делать будет."
                                show ck smile at center
                                with dspr
                                ck "Наверное, в КГБ позвонит со словами: «в стратегический объект «Совёнок» проникли империалистические разведчики и выкрали стратегически важные конфеты»."
                                hide ck with dissolve
                            else:
                                window show
                                play sound ds_sfx_int
                                con "{result}Ничего складного в голову не приходит... не выйдет захватывающей истории, увы."
                                me "Да так, знаете... инопланетяне сюда зашли и украли конфеты... мы ничего не смогли поделать..."
                                show ck laugh at center
                                with dspr
                                ck "Интересная история... долго придумывал?"
                                show ck serious at center
                                with dspr
                                ck "Поздравляю, победитель турнира остался без приза! Не знаю, что с этим вожатая делать будет."
                            $ ds_karma -= 10
                            play sound ds_sfx_psy
                            sug "А теперь серьёзно - зачем это было?"
                            th "Не знаю... просто посмеяться!"
                        "Сдать Ульяну":
                            window show
                            me "Это всё та девочка! Красноволосая!"
                            ck "Почему-то я так и подумала..."
                            ck "Ладно, с ней будет Ольга Дмитриевна разбираться... как и с призом для турнира."
                            $ ds_lp['us'] -= 2
                            play sound ds_sfx_mot
                            res "С призом?"
                    hide ck with dissolve
                    jump ds_day3_dinner
        "Привлечь внимание поварихи":
            window show
            "Ты громко кричишь."
            me "Тут воруют! Конфеты украсть хотят!"
            show us angry sport at center
            with dspr
            us "Предатель! Ну ничего..."
            $ ds_lp['us'] -= 2
            "И тут она бросается к шкафу и в мгновение ока выхватывает конфеты оттуда."
            hide us
            show ck normal far at right
            with dissolve
            "К тому времени, как повариха подходит к тебе, её уже и след простыл."
            show ck serious at center
            with dspr
            ck "Что случилось?"
            window hide
            menu:
                "Побежать за Ульяной":
                    window show
                    me "Я сейчас! Я всё верну!"
                    "И ты выбегаешь из столовой."
                "Остаться и рассказать":
                    window show
                    me "Это всё та девочка! Красноволосая! Украла конфеты!"
                    ck "Вот как... и чего же ты её не догоняешь?"
                    me "Да я не догоню её..."
                    ck "Плохо, конечно... с ней будет Ольга Дмитриевна разбираться... как и с призом для турнира."
                    $ ds_lp['us'] -= 2
                    play sound ds_sfx_mot
                    res "С призом?"
        "Отказаться тихо":
            window show
            me "Я в этом участвовать не буду!"
            show us dontlike sport at center   with dspr
            us "Ну и ладно!"
            "Она фыркает и отворачивается."
            us "Тогда я сама!"

            stop music fadeout 3

            play ambience ambience_dining_hall_full fadein 3

            me "И тебя я не…"
            hide us  with dissolve
            "Ты не успеваешь закончить фразу, а Ульянка уже ловко перепрыгивает через стенку буфета, подходит к шкафу, открывает его и начинает рыться там."
            me "Да подожди ты!{w} Мало тебе, что ли, проблем с Ольгой Дмитриевной!"
            "Она не отвечает."
            me "За такое тебя не просто убираться заставят."
            "Ульянка закрывает шкаф.{w} В её руках ты видишь большой пакет с конфетами."
            me "А ну, положи на место!"
            "Она показывает тебе язык и выбегает через заднюю дверь."
            play sound ds_sfx_psy
            aut "Это нельзя просто так оставлять!"
            window hide
            menu:
                "Погнаться за ней":
                    window show
                    play sound ds_sfx_fys
                    edr "У девочки приличная фора, но ты вкладываешь в погоню все силы."

                    stop ambience fadeout 2

                    th "Второй раз я ей не проиграю!"
                    window hide
                "Доложить поварихе":
                    window show
                    "Ты кричишь что есть мочи."
                    me "Тут конфеты украли!"
                    show ck serious at center
                    with dspr
                    ck "Что случилось? Кто украл?"
                    me "Та несносная красноволосая девчонка!"
                    ck "Вот как... и чего же ты её не догоняешь?"
                    me "Да я не догоню её..."
                    show ck serious at center
                    with dspr
                    ck "Ольга Дмитриевна разберётся... вот только победитель вчерашнего турнира останется без конфет."
                    play sound ds_sfx_mot
                    res "Конфеты были призом за турнир? Да, неудача..."
                    "Тем временем в столовой собираются люди. Подходит время ужина."
                    jump ds_day3_dinner
                "Забить":
                    window show
                    "Ты остаёшься в столовой. Подходит время ужина."
                    window hide
                    $ persistent.sprite_time = "day"
                    scene bg int_dining_hall_people_day 
                    with dissolve

                    play ambience ambience_dining_hall_full fadein 3

                    window show
                    "Постепенно народу прибавляется."
                    "Ты начинаешь прикидывать, куда можешь присесть."
                    show ck serious at center
                    with dissolve
                    ck "Пионер, а ты не видел конфеты? Лежали в шкафу, а теперь их нет."
                    window hide
                    menu:
                        "{check=drama:10}Изобразить непонимание":
                            if skillcheck('drama', lvl_medium):
                                window show
                                dra "{result}У вас получается убедительно изобразить, будто вы впервые об этих конфетах слышите."
                                me "Понятия не имею, о каких вы конфетах."
                                $ ds_skill_points['drama'] += 1
                                show ck normal at center
                                with dspr
                                ck "Ясно... Похоже, победитель вчерашнего турнира останется без приза."
                                hide ck with dissolve
                                play sound ds_sfx_mot
                                res "Так это приз был?"
                            else:
                                window show
                                dra "{result}Ваше лицо, мессир, - оно как открытая книга. Вся ваша ложь отчётливо видна."
                                me "Я не знаю..."
                                ck "Ага, как же... Наверное, ты и украл."
                                $ ds_skill_points['drama'] += 1
                                $ ds_karma -= 5
                                me "Не крал я ничего!"
                                ck "Разберётся Ольга Дмитриевна."
                                ck "А пока я могу сказать лишь то, что победитель турнира останется без приза."
                                play sound ds_sfx_mot
                                res "Так это приз был?"
                        "Взять вину на себя":
                            window show
                            me "Да знаете... это я их съел, пока убирался..."
                            ck "Вот как? Ты же понимаешь, что оставил победителя турнира без приза?"
                            play sound ds_sfx_mot
                            res "Без приза?"
                            ck "Ладно, это уже дело твоей вожатой. А пока иди ужинай!"
                            hide ck with dissolve
                            $ ds_karma -= 10
                        "Сказать, что не знаешь":
                            window show
                            me "Я не видел... просто заметил, что конфеты пропали, и всё!"
                            ck "Учитывая, что тут были только двое... это или ты, или ты рыжеволосая девчонка!"
                            play sound ds_sfx_int
                            lgc "Тут не нужно быть Сократом, чтобы сделать вывод, кто тогда украл конфеты."
                            ck "В общем, я скажу Ольге Дмитриевне, она разберётся."
                            ck "А ты иди ужинать!"
                            hide ck with dissolve
                        "Оговорить Алису":
                            window show
                            me "Знаю, знаю! Вы видели рыжеволосую девушку, с хвостиками."
                            show ck normal at center
                            with dspr
                            ck "Конечно, видела, припоминаю такую..."
                            me "Ну так вот, пока мы убирались, она пролезла в окно, выкрала конфеты и убежала!"
                            ck "Вот как... Значит, она лишила победителя турнира приза!"
                            ck "Вожатая разберётся, в общем."
                            $ ds_framed_dv = True
                            $ ds_lp['dv'] -= 2
                        "{check=conceptualization:11}Назвать фантастичную причину":
                            if skillcheck('conceptualization', lvl_up_medium):
                                window show
                                play sound ds_sfx_int
                                con "{result}Нашествие инопланетян! Вторжение империалистов! У тебя столько идей!"
                                $ ds_skill_points['conceptualization'] += 1
                                me "Вы не поверите, что тут произошло!"
                                me "Вот убираемся мы тут с Ульяной. И тут - бац!"
                                me "Заходит шпион! Американский! Чернокожий, в костюме, с портфелем."
                                me "Открывает свой чемодан, кладёт туда конфеты, в потом облучает нас какой-то штукой, от чего мы не могли ему противодействовать. И был таков!"
                                show ck laugh at center
                                with dspr
                                ck "Я не знаю, как на это реагировать! Такое уморительное враньё! Может, тебе в писатели податься?"
                                show ck serious at center
                                with dspr
                                ck "А если серьёзно - поздравляю, победитель турнира остался без приза! Не знаю, что с этим вожатая делать будет."
                                show ck smile at center
                                with dspr
                                ck "Наверное, в КГБ позвонит со словами: «в стратегический объект «Совёнок» проникли империалистические разведчики и выкрали стратегически важные конфеты»."
                                hide ck with dissolve
                            else:
                                window show
                                play sound ds_sfx_int
                                con "{result}Ничего складного в голову не приходит... не выйдет захватывающей истории, увы."
                                me "Да так, знаете... инопланетяне сюда зашли и украли конфеты... мы ничего не смогли поделать..."
                                show ck laugh at center
                                with dspr
                                ck "Интересная история... долго придумывал?"
                                show ck serious at center
                                with dspr
                                ck "Поздравляю, победитель турнира остался без приза! Не знаю, что с этим вожатая делать будет."
                            $ ds_karma -= 10
                            play sound ds_sfx_psy
                            sug "А теперь серьёзно - зачем это было?"
                            th "Не знаю... просто посмеяться!"
                        "Сдать Ульяну":
                            window show
                            me "Это всё та девочка! Красноволосая!"
                            ck "Почему-то я так и подумала..."
                            ck "Ладно, с ней будет Ольга Дмитриевна разбираться... как и с призом для турнира."
                            $ ds_lp['us'] -= 2
                            play sound ds_sfx_mot
                            res "С призом?"
                    hide ck with dissolve
                    jump ds_day3_dinner
    $ persistent.sprite_time = "day"
    scene bg ext_square_day:
        zoom 1.05 anchor (48,27)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (25,25)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (-25,25)
        repeat 
    with dissolve

    play music music_list["always_ready"] fadein 5

    window show
    "Вы пробегаете по площади…"
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_musclub_day:
        zoom 1.05 anchor (48,27)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (25,25)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (-25,25)
        repeat  
    with dissolve

    window show
    "Сворачиваете к зданию музыкального кружка…"
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_path2_day:
        zoom 1.05 anchor (48,27)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (25,25)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (-25,25)
        repeat  
    with dissolve

    window show
    "И выбегаете на лесную тропинку."
    "Ты уже почти догнал Ульянку, как вдруг она останавливается…"
    if skillcheck('reaction_speed', lvl_legendary, passive=True):
        play sound ds_sfx_mot
        res "{result}Тормози!"
        "У тебя получается остановиться так, чтобы её не зацепить."
        show us laugh sport at center
        with dissolve
        us "Не догнал! Не догнал! Я победила!"
        res "Ты пытаешься её схватить..."

        window hide
        show us laugh sport at right
        with dspr
        $ renpy.pause(0.5)
        show us laugh sport at left
        with dspr
        $ renpy.pause(0.5)
        show us laugh sport at right
        with dspr
        $ renpy.pause(0.5)
        show us laugh sport at left
        with dspr
        $ renpy.pause(0.5)
        show us laugh2 sport at center
        with dspr
        window show

        res "...но она оказывается слишком юркой, и ты ничего не можешь поделать."
        if not ds_caught_us:
            play sound ds_sfx_psy
            aut "Снова поражение от этой девчонки..."
    else:
        play sound ds_sfx_mot
        res "{result}У тебя же так резко затормозить не получилось, и ты сбиваешь её с ног."
        window hide

        stop music fadeout 3

        play sound sfx_fall_grass

        with vpunch

        pause(1)

        window show
        "Вы повалились на траву..."
        $ ds_damage_health()

        scene cg ds_day3_us_caught_f1
        $ renpy.pause(0.1, hard=True)
        scene cg ds_day3_us_caught_f2
        $ renpy.pause(0.1, hard=True)
        scene cg ds_day3_us_caught_f3

        play music music_list["eternal_longing"] fadein 5

        window show
        me "Догнал!"
        us "И ничего не догнал…"
        "Смущённо отвечает она."
        "Ульяна лежит под тобой."
        "Её лицо – совсем рядом с твоим."
        play sound ds_sfx_mot
        per_toc "Ты чувствуешь прерывистое дыхание и жар тела."
        play sound ds_sfx_fys
        ins "Конечно, сейчас она ещё ребёнок, но скоро станет женщиной."
        play sound ds_sfx_mot
        com "Всё это тебя сильно смущает."
        us "Насиловать будешь?"
        "Немного придя в себя, говорит она."
        play sound ds_sfx_fys
        hfl "Бутылка зовёт... Твой зад рефлекторно сжимается от осознания возможных последствий."
        play sound ds_sfx_int
        dra "Всё-таки в данной ситуации это больше детская игра."
        hfl "Но лучше быть осторожным."
        me "А ты хочешь?"
        us "А то!"
        "Она хитро улыбнулась и тихо хрюкает.{w} Или тебе просто показалось."
        me "А вот я что-то не очень…"
        us "Ну и ладно!"
        window hide

        stop music fadeout 3

        play sound sfx_punch_medium

        with vpunch

        pause(1)

        scene bg black 
        with dissolve

        window show
        play sound ds_sfx_fys
        pat "Ульянка больно кусает тебя за нос."
        com "От неожиданности ты немного привстаёшь."
        window hide

        $ persistent.sprite_time = "day"
        scene bg ext_path2_day 
        with dissolve

        play ambience ambience_forest_day fadein 2

        show us grin sport at center   with dissolve
        window show
        "Этих мгновений как раз хватает ей, чтобы вырваться и отбежать на несколько метров."
        show us laugh sport far at center   with dissolve
        us "Смотри!{w} Потом пожалеешь!"
    hide us  with dissolve
    "Она громко смеётся и скрывается в лесу."
    "Пакет с конфетами же остаётся лежать на земле рядом с тобой."
    th "Интересно, она специально их бросила?"
    play sound ds_sfx_psy
    vol "Время близится к ужину, так что нужно поскорее вернуть конфеты."
    play sound ds_sfx_fys
    hfl "И желательно (очень желательно) остаться незамеченным."
    play sound ds_sfx_int
    rhe "Конечно, ты можешь объяснить всю ситуацию, что их украла Ульяна…"
    rhe "Но кто тебе поверит?"
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_near_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 2

    show mt normal pioneer at center   with dissolve
    window show
    "На входе в столовую тебя уже ждёт Ольга Дмитриевна…"
    show mt smile pioneer at center   with dspr
    mt "Молодец, Семён!"
    me "Это вы про что?"
    "Пакет с конфетами ты прячешь за спиной."
    "Он прозрачен, да и таких размеров, что в карман не запихнёшь!"
    mt "Я про уборку.{w} Всё чисто и аккуратно!"
    me "А, да…"
    show mt normal pioneer at center   with dspr
    mt "А Ульяна где?"
    play sound ds_sfx_int
    lgc "Ты бы и сам хотел знать!"
    me "Она… скоро придёт…"
    mt "Хорошо. Ну, иди ужинать тогда."
    $ ds_karma += 5
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_people_day 
    with dissolve

    play ambience ambience_dining_hall_full fadein 3

    window show
    "Ты заходишь в столовую."
    "Там, что неудивительно, полно народу."
    "Как вернуть пакет так, чтобы тебя не заметили, ты и представить не можешь."
    th "Конечно, можно вечером, но сейчас-то куда мне его девать?!"
    sl "Семён!"
    show sl normal pioneer at center   with dissolve
    "Ты оборачиваешься.{w} Перед тобой стоит Славя."
    sl "Ой, а что это у тебя?"
    "Она смотрит на пакет, который ты не успеваешь спрятать за спину."
    play sound ds_sfx_psy
    aut "Раскрыт, разоблачён, опозорен и раздавлен!"
    play sound ds_sfx_int
    dra "Врать бессмысленно."
    me "Это…{w} конфеты…"
    sl "А откуда?"
    window hide
    menu:
        "Сказать про Ульяну":
            window show
            me "Ульяна отдала."
            if ds_lp['sl'] >= 0:
                show sl smile pioneer at center   with dspr
                sl "Понятно. Значит, она опять за своё."
                me "Опять?"
                sl "Ну, она уже не первый раз ворует конфеты."
                th "И почему я не удивлён?"
                show sl normal pioneer at center   with dspr
                sl "Давай я их отнесу."
                me "Спасибо…"
                play sound ds_sfx_psy
                vol "Славя в очередной раз спасает тебя."
                th "Какая же она замечательная..."
                "Она берёт пакет и направляется к буфету."
                hide sl  with dissolve
                "А ты быстро бегаешь глазами и ногами по столовой в поисках свободного места."
            else:
                show sl angry pioneer at center
                with dspr
                sl "Вот как, значит... Украл конфеты?"
                me "И ничего я не крал! Это всё она!"
                show sl serious pioneer at center
                with dspr
                sl "Ольга Дмитриевна разберётся... а вот и она, кстати!"
                show mt normal pioneer at right
                with dissolve
                mt "А что случилось?"
                sl "Да так, тут Семён на пару с Ульяной конфеты похитили!"
                show mt angry pioneer at right
                with dspr
                mt "Вот как, значит? А я тебя похвалила ещё..."
                me "Да не делал я ничего!"
                mt "Но не уследил за Ульяной! Хотя должен был!"
                aut "С чего это вдруг?"
                mt "Всё, не хочу в этом разбираться! Вот и доверяй вам! Иди ужинать!"
                $ ds_lp['mt'] -= 1
                $ ds_karma -= 10
        "Прикрыть Ульяну":
            window show
            me "Так получилось... я взял конфеты, пока убирался..."
            show sl serious pioneer at center
            with dspr
            sl "Ну, хоть честно..."
            $ ds_lp['sl'] -= 1
            if ds_lp['sl'] >= 10:
                show sl normal pioneer at center
                with dspr
                sl "Ладно, не буду тебя в этот раз сдавать Ольге Дмитриевне... но больше так не делай!"
                me "Спасибо…"
                play sound ds_sfx_psy
                vol "Славя в очередной раз спасает тебя."
                th "Какая же она замечательная..."
                "Она берёт пакет и направляется к буфету."
                hide sl  with dissolve
                "А ты быстро бегаешь глазами и ногами по столовой в поисках свободного места."
            else:
                sl "Вот как, значит... Украл конфеты?"
                sl "Да как ты мог?!"
                show sl serious pioneer at center
                with dspr
                sl "Ольга Дмитриевна разберётся... а вот и она, кстати!"
                show mt normal pioneer at right
                with dissolve
                mt "А что случилось?"
                sl "Да так, тут Семён на пару с Ульяной конфеты похитили!"
                show mt angry pioneer at right
                with dspr
                mt "Вот как, значит? А я тебя похвалила ещё..."
                me "Извините..."
                mt "Вот и доверяй вам! Иди ужинать!"
                $ ds_lp['mt'] -= 1
                $ ds_karma -= 10
    jump ds_day3_dinner

label ds_day3_after_lunch:
    $ persistent.sprite_time = 'day'
    scene bg ext_dining_hall_away_day
    with dissolve

    window show
    th "Так, и куда бы мне пойти?"

    window hide
    $ disable_all_zones_ds_small()
    $ set_zone_ds_small("house_me_mt", "ds_day3_home")
    $ set_zone_ds_small("library", "ds_day3_library")
    $ set_zone_ds_small("music_club", "ds_day3_music")
    $ set_zone_ds_small("clubs", "ds_day3_cyber")
    if ds_punished:
        $ set_zone_ds_small("forest", "ds_day3_forest")
    $ set_zone_ds_small("medic_house", "ds_day3_medic")
    if ds_punished:
        $ set_zone_ds_small("dining_hall", "ds_day3_punishment_return")
    $ show_small_map_ds()

label ds_day3_music:
    $ ds_after_lunch_who = 'mi'
    $ persistent.sprite_time = 'day'
    scene bg ext_musclub_day
    with dissolve

    "Ты направляешься в сторону музклуба."
    th "Интересно, Мику там? А если там Алиса?"
    play sound ds_sfx_fys
    hfl "В последнем случае могут случиться неприятности..."
    play sound ds_sfx_psy
    emp "Да вряд ли. С чего бы ей напакостить тебе?"
    hfl "Да просто так! В общем, будь наготове."
    play sound ds_sfx_int
    con "А как же Мику? Никого не интересует Мику?"
    hfl "Мику не шлёпнет тебя по спине внезапно."
    play sound ds_sfx_mot
    com "Ага, она скорее словами тебя затопит."
    "С роем мыслей в голове ты заходишь в домик."

    play sound sfx_open_door_1
    scene bg int_musclub_day
    show mi normal pioneer at left
    show dv normal pioneer2 at right
    with dissolve
    "Ничего неожиданного - в клубе две его постоянные участницы: Мику и Алиса."
    show mi smile pioneer at left
    with dspr
    mi "Ой, привет-привет, Семён-кун, а мы тут тебя очень-очень ждали. И ты всё-таки пришёл!"
    dv "Привет."
    me "Привет. Так, мне уже пора идти, не скучайте без меня!"
    window hide
    menu:
        "Сделать комплимент Мику":
            window show
            me "Классно выглядишь, Мику!"
            show mi shy pioneer at center
            show dv sad pioneer2 far at fright
            with dspr
            mi "Ой, спасибочки, Семён-кун!"
            hide dv with dissolve
            "И ты даже не заметил, как Алиса вышла."
            $ ds_lp['dv'] -= 1
        "{check=suggestion:12}Сделать комплимент Алисе":
            if skillcheck('suggestion', lvl_challenging):
                window show
                play sound ds_sfx_psy
                sug "{result}Внешность - этап пройденный. Лучше скажи что-нибудь про её музыкальные умения."
                me "Почему-то я уверен, что ты классно играешь, Алиса! Сыграешь что-нибудь?"
                show dv smile pioneer2 far at fright
                with dspr
                dv "Неа! У меня дела! Потом, может."
                "И она выходит."
            else:
                window show
                play sound ds_sfx_psy
                sug "{result}Ты впечатлён её фигурой. Так ей и скажи."
                me "Какая... восхитительная фигура. Так бы и прижал тебя к себе, Алиса..."
                show dv angry pioneer2 far at fright
                with dspr
                dv "Что ты несёшь?!"
                hide dv with dissolve
                play sound ds_sfx_psy
                emp "Она это восприняла как домогательство, а не комплимент."
                $ ds_skill_points['suggestion'] += 1
        "Сделать комплимент обеим":
            window show
            me "Прекрасно выглядите!"
            show mi smile pioneer at left
            show dv angry pioneer2 at right
            with dspr
            dv "Ты это к чему вообще?"
            show dv normal pioneer2 far at fright
            with dspr
            dv "Ладно, не суть, я пошла!"
            hide dv with dissolve
        "Предложить Алисе остаться":
            window show
            me "Может, останешься?"
            dv "Нет, у меня дела."
            hide dv with dissolve
        "Отмолчаться":
            window show
            hide dv with dissolve
            "И Алиса выходит."
    if ds_dv_invite:
        "Но через пару секунд она вновь заглядывает."
        dv "Не забудь о наших планах на вечер!"
        "И уходит уже окончательно."
    window hide
    menu:
        "Догнать Алису":
            scene bg ds_ext_musclub_veranda_day
            show dv normal pioneer2 at center
            with dissolve
            me "Погоди, Алиса, я с тобой!"
            show dv grin pioneer2 at center
            with dspr
            dv "Куда? Ко мне в домик лежать?"
            window hide
            menu:
                "Ответить утвердительно":
                    window show
                    me "Ага!"
                    show dv laugh pioneer2 at center
                    with dspr
                    dv "Ну уж нет, тебе спать со мной нельзя! Рановато ещё!"
                "Отступить":
                    window show
                    me "А..."
            if ds_dv_invite:
                show dv smile pioneer2 at center
                with dspr
                dv "Не переживай ты так: мы ещё сегодня вечером же с тобой сидим!"
                show dv angry pioneer2 at center
                with dspr
                dv "Или уже забыть успел? Или решил не пойти?"
                me "Да нет, не забыл..."
            elif ds_dance_dv:
                show dv smile pioneer2 at center
                with dspr
                dv "И вообще, мы же сегодня вечером на танцах увидимся. По твоей инициативе!"
                show dv normal pioneer2 at center
                with dspr
                dv "Так что лучше договорись с Мику насчёт моего выступления!"
            dv "Я пошла! Бывай!"
            hide dv with dissolve
            me "Пока..."
            window hide
            menu:
                "Вернуться в музклуб":
                    window show
                    "Ты возвращаешься обратно."
                "Уйти":
                    window show
                    th "Мне тут без Алисы делать нечего, наверное..."
                    $ ds_lp['mi'] -= 1
                    $ disable_current_zone_ds_small()
                    jump ds_day3_after_lunch
        "Остаться с Мику":
            window show
    show mi happy pioneer at center
    with dissolve
    mi "А что тебя привело сюда, Семён?"
    if ds_lp['mi'] > 0:
        mi "Может, хочешь послушать, как я играю? Или же ты сыграешь?"
    if ds_dv_invite and skillcheck('conceptualization', lvl_medium, passive=True):
        play sound ds_sfx_int
        con "Есть идея! Мику наверняка сможет помочь тебе с сочинением песни. А потом ты представишь её Алисе на сегодняшем вечере. Это покорит её!"
    window hide
    menu ds_day3_music_mi_dialogue:
        set ds_menuset
        "Послушать игру Мику":
            window show
            me "Да! Я очень хотел бы послушать, как ты играешь! Это должно быть чудесно!"
            show mi smile pioneer at center
            with dspr
            mi "Ой, мне так приятно, Семён-кун! Сейчас всё будет!"
            $ ds_lp['mi'] += 2
            scene cg ds_day3_mi_piano_1
            with dissolve
            "Она садится за рояль."
            mi "Назови число от 1 до 5."
            window hide
            menu:
                "1":
                    play sound3 ds_mi_piano_1
                "2":
                    play sound3 ds_mi_piano_2
                "3":
                    play sound3 ds_mi_piano_3
                "4":
                    play sound3 ds_mi_piano_4
                "5":
                    play sound3 ds_mi_piano_5
            window show
            "Мику начинает играть."
            scene cg ds_day3_mi_piano_2
            play sound ds_sfx_psy
            emp "Видно, как ей доставляет удовольствие музыка - она закрывает глаза."
            play sound ds_sfx_int
            con "Мелодия словно льётся из её пальцев - так нежно, плавно, так прекрасно!"
            con "Определённо, она долго занималась. Её руки будто порхают от клавиши к клавише. Ни одной ошибки, ни одной малейшей погрешности!"
            window hide
            $ renpy.pause(5.0)
            window show
            show blink
            con "Ты склоняешь голову и закрываешь глаза."
            window hide
            $ renpy.pause(5.0)
            hide blink
            show unblink
            stop sound3 fadeout 5
            scene cg ds_day3_mi_piano_1
            with dissolve
            window show
            "Наконец, Мику заканчивает играть."
            scene bg int_musclub_day
            show mi smile pioneer at center
            with dissolve
            mi "Как тебе, Семён-кун?"
            window hide
            menu:
                "Похвалить":
                    window show
                    me "Мне очень, очень понравилось!"
                    show mi shy pioneer at center
                    with dspr
                    mi "Ой, ну ладно тебе, не льсти! Но мне очень приятно! Но ты не нахваливай меня так!"
                    $ ds_lp['mi'] += 1
                "Раскритиковать":
                    window show
                    me "Как-то не очень... так себе получилось..."
                    show mi dontlike pioneer at center
                    with dspr
                    mi "Да кто бы говорил! Ты-то сам умеешь играть? Ну вообще, я нигде не ошиблась! Да как ты смеешь вообще!"
                    show mi cry pioneer at center
                    with dspr
                    mi "Иди отсюда, бака!"
                    $ ds_lp['mi'] -= 4
                    window hide
                    menu:
                        "Извиниться":
                            window show
                            me "Извини..."
                            "Но она не слышит тебя."
                            play sound ds_sfx_psy
                            emp "Или же не хочет слышать."
                        "Молча выйти":
                            window show
                    "И ты выходишь."
                    scene bg ds_ext_musclub_veranda_day
                    with dissolve
                    th "Да, неудобно вышло... но куда теперь идти? До ужина далеко..."
                    $ disable_current_zone_ds_small()
                    jump ds_day3_after_lunch
            mi "Что-нибудь ещё, Семён-кун? Можешь и ты поиграть. Не умеешь - я покажу!"
            window hide
            jump ds_day3_music_mi_dialogue
        "{check=interfacing:15}Сыграть самому":
            window show
            me "А давай лучше я сыграю? Для тебя!"
            show mi shy pioneer at center
            with dspr
            mi "Ой, давай, конечно, мне так приятно будет. А то всё я играю - а тут для меня! Это так мило! И очаровательно!"
            $ ds_lp['mi'] += 2
            me "А где тут гитара?"
            show mi smile pioneer at center
            with dspr
            mi "Вот, держи!"
            "Мику передаёт тебе электрогитару, ты берёшь её в руки и начинаешь вспоминать, как же на ней играть."
            $ ds_played_guitar = True
            window hide
            if skillcheck('interfacing', lvl_heroic):
                window show
                play sound ds_sfx_mot
                inf "{result}Твои пальцы сами помнят, как играть. И начинают играть. Тебе даже не приходится осознанно ими управлять."
                # TODO: CG: игра Семёна в присутствии Мику
                # TODO: подобрать мелодию
                show mi surprise pioneer at center
                with dissolve
                play sound ds_sfx_psy
                emp "Твои навыки игры впечатляют Мику."
                emp "Более того - кажется, она собирается запеть."
                "И то верно - она собирается с мыслями и начинает тебе подпевать."
                "Что-то на японском с вкраплениями английского."
                play sound ds_sfx_int
                lgc "Видимо, ей играемая тобой песня знакома."
                mi "{i}Plastic lies, мицумэру дакэ да митасарэта,{/i}"
                mi "{i}Paper heart, ано коро нива модорэнай кара...{/i}"
                window hide
                $ renpy.pause(1.0)
                window show
                mi "{i}Хитоме аната ни айтакутэ коэ га кикитакутэ{/i}"
                mi "{i}Татисукуму эен ёри нагай исюн{/i}"
                mi "{i}Ицумо аната но тонари де хасягу ватаси га ита ё нэ{/i}"
                mi "{i}Хитоцу мата хитоцу киэру ватаси дакэ но басё{/i}"
                mi "{i}Plastic night, фэнсу-госи но ёдзора ни мита{/i}"
                mi "{i}Paper moon, цуметай цукиакари ни нагэку{/i}"
                mi "{i}Утиёсэру унэри ёри кураку юреру омой дакисимэтэ сакэбу но.{/i}"
                mi "{i}Still I love you...{/i}"

                play sound ds_sfx_mot
                res "Это к чему было? Не тебя же она продолжает любить!"
                show mi happy pioneer at center
                with dspr
                mi "Ты так классненько сыграл... но, похоже, ты всё-таки давно не занимался! Давай я с тобой позанимаюсь!"
                window hide
                menu:
                    "Согласиться":
                        window show
                        me "Давай!"
                        show mi smile pioneer at center
                        with dspr
                        mi "Как хорошо!"
                    "Спросить про текст песни":
                        window show
                        me "А что это ты такое пела?"
                        show mi surprise pioneer at center
                        with dspr
                        mi "То, что ты играл. Ты чего, текста не знаешь?"
                        me "Да как-то не особо владею японским... расскажи, про что там?"
                        show mi sad pioneer at center
                        with dspr
                        mi "Да так, ничего особого..."
                        if skillcheck('empathy', lvl_easy, passive=True):
                            play sound ds_sfx_psy
                            emp "{result}Как раз таки {i}особо{/i}... похоже, ты задел что-то очень личное для неё. Переживание."
                            if skillcheck('logic', lvl_up_medium, passive=True):
                                play sound ds_sfx_int
                                lgc "{result}А если учесть английские слова (а английский ты знаешь), то из них явно следует, что это имеет отношение к любви. Возможно, даже неразделённой."
                                if skillcheck('encyclopedia', lvl_medium, passive=True):
                                    play sound ds_sfx_int
                                    enc "{result}Да и песня... В ней речь идёт о неразделённой любви. По крайней мере, кажущейся неразделённой."
                                    th "Наверное, и я её выбрал поэтому..."
                        show mi smile pioneer at center
                        with dspr
                        mi "А почему ты выбрал именно эту песню?"
                        play sound ds_sfx_psy
                        vol "И правда - почему именно эту?"
                        th "Да не знаю, честно говоря... как-то само получилось..."
                        me "Да просто что вспомнил первое - то и сыграл."
                        show mi normal pioneer at center
                        with dspr
                        mi "Вот как... ну ладно!"
                        show mi smile pioneer at center
                        with dspr
                        mi "Вообще, тебе бы немного практики, всё-таки, похоже, ты давно не играл. Но я это могу исправить! Только скажи - и я займусь тобой!"
                        window hide
                        jump ds_day3_music_mi_dialogue
                    "Предложить своё":
                        window show
                        me "Слушай, а может лучше..."
                        window hide
                        jump ds_day3_music_mi_dialogue
            else:
                play sound ds_sfx_mot
                inf "{result}А ты вообще держал в руках гитару когда-нибудь? Похоже, что нет - потому что ты вообще ничего не можешь сыграть."
                "Ты пытаешься взять хотя бы один аккорд - но безуспешно. Получается форменная какофония."
                show mi dontlike pioneer at center
                with dspr
                "Об этом красноречиво говорит лицо Мику."
                show mi normal pioneer at center
                with dspr
                mi "Классненько играешь... но давай я тебе покажу, как улучшить твою игру!"
                if skillcheck('rhetoric', lvl_easy, passive=True):
                    play sound ds_sfx_int
                    rhe "{result}На самом деле она хочет сказать, что ты играл отвратительно. Лишь японское воспитание мешает ей озвучить это прямо."
                    $ ds_skill_points['rhetoric'] += 1
                window hide
                menu:
                    "Согласиться":
                        window show
                        me "Давай!"
                        show mi smile pioneer at center
                        with dspr
                        mi "Как хорошо!"
                    "Предложить своё":
                        window show
                        me "Слушай, а может лучше..."
                        window hide
                        jump ds_day3_music_mi_dialogue
        "Попросить урок игры":
            window show
        "Попросить помочь с сочинением" if ds_last_skillcheck and (ds_last_skillcheck.result):
            window show
            jump ds_day3_music_mi_compose
        "Сказать насчёт выступления Алисы" if ds_dance_dv and not ds_mi_accept_dv:
            window show
            me "Слушай, Мику... ты же организуешь музыку на сегодняшнем вечере?"
            show mi smile pioneer at center
            with dspr
            mi "Да, я! А что случилось?"
            me "Понимаешь, тут Алиса хочет выступить. На гитаре сыграть."
            mi "Ой, как же это чудесненько! Конечно, пусть выступит! Я верю в неё, у неё всё получится!"
            me "Отлично, спасибо."
            $ ds_mi_accept_dv = True
            show mi normal pioneer at center
            with dspr
            mi "Так чем ты хочешь заняться?"
            window hide
            jump ds_day3_music_mi_dialogue
        "Отказаться и уйти":
            window show
            me "Да знаешь... я сюда по ошибке зашёл... я пойду. Извини и удачи!"
            scene bg ds_ext_musclub_veranda_day
            with dissolve
            "И ты выбегаешь из клуба раньше, чем Мику успевает что-либо понять."
            $ ds_lp['mi'] -= 1
            th "Ладно, пойдём в другую локацию..."
            $ disable_current_zone_ds_small()
            jump ds_day3_after_lunch
    jump ds_day3_music_mi_teaching

label ds_day3_music_mi_teaching:
    scene bg int_musclub_day
    show mi serious pioneer at center
    with dissolve
    mi "Так-так, значит смотри. Возьми гитару в руки. Вот так."
    scene cg ds_day3_mi_teaching
    with dissolve
    mi "Нет-нет-нет, возьми гриф левой рукой, а корпус - правой. Да, правильно, молодец."
    mi "А теперь возьми вот эту штучку - медиатор. Взял? Умница! Теперь им начинай дёргать за струны."
    "Мику тебя обхватывает своими ручками, чтобы правильно разместить твои пальцы на гитаре."
    "А для большего своего удобства она прижимается к тебе сзади всем телом."
    play sound ds_sfx_fys
    ins "Вполне предсказуемо твоё тело - особенно {i}нижняя{/i} часть - откликается на это. Тебя возбуждает близость японской тян!"
    mi "Так, Семён, расставь пальцы вот так и проведи по струнам медиатором."
    "Тебе удаётся, следуя инструкциям Мику, извлечь более-менее приемлемый звук."
    mi "Отлично получилось, Семён-кун! Теперь давай вот так."
    "С этими словами она перемещает твои пальцы в другую конфигурацию. Ты снова проводишь медиатором по струнам. Получается новый аккорд."
    mi "Давай теперь сам."
    play sound ds_sfx_int
    con "Благодаря указаниям японки ты теперь можешь извлекать звуки из гитары более аккуратно."
    mi "Так, теперь смотри..."
    window hide
    $ renpy.pause(3.0)
    scene bg int musclub_day
    show mi smile pioneer at center
    with dissolve
    window show
    "Спустя пару часов проб и ошибок ты откладываешь гитару."
    mi "У тебя отлично получается! Если продолжишь заниматься дальше - будешь вообще самым лучшим гитаристом! И даже сможешь выступить на концерте в последний день!"
    th "Точно, концерт..."
    show mi shy pioneer at center
    with dspr
    mi "Ты же поучаствуешь? Нам не хватает бас-гитариста! А ты подойдёшь туда идеально!"
    $ ds_played_guitar = True
    window hide
    menu:
        "Согласиться":
            window show
            me "Да, я приму участие!"
            show mi happy pioneer at center
            with dspr
            mi "Отлично-отлично, Семён-кун! Только теперь тебе надо будет каждый день готовиться! Ты готов?"
            me "Да..."
            $ ds_lp['mi'] += 1
            $ ds_member['music'] = True
            $ ds_concert_part = True
            mi "Тогда жду тебя завтра тут же! А сейчас идём ужинать!"
        "Отказаться":
            window show
            me "Не... я как-то не готов..."
            show mi sad pioneer at center
            with dspr
            mi "Как же так? У тебя так прекрасно получается? Что же нам делать?"
            me "Не знаю... я не смогу, извините."
            mi "Ладно... иди ужинать тогда, я не держу тебя..."
            $ ds_lp['mi'] -= 1
            play sound ds_sfx_psy
            emp "Она определённо рассчитывала на тебя."
    if ds_punished:
        jump ds_day3_mt_interrogate
    else:
        jump ds_day3_dinner

label ds_day3_music_mi_compose:
    scene bg int_musclub_day
    show mi normal pioneer at center
    with dspr
    me "Слушай, Мику, у меня тут такое дело..."
    mi "Что случилось, Семён-кун? Расскажи мне всё, я помогу тебе всем чем смогу!"
    me "Я планирую сегодня с Алисой вечер провести... и хотел бы сыграть что-нибудь своего сочинения, чтобы её поразить!"
    show mi smile pioneer at center
    with dspr
    mi "Отличная идея, Алисе-тян это точно понравится! Так давай придумаем что-нибудь!"
    me "Вот за этим я и пришёл, ты же такая классная музыкантша!"
    show mi shy pioneer at center
    with dspr
    mi "Ой, не надо мне льстить, Семён-кун! Давай лучше приступим!"
    show mi serious pioneer far at left
    with dspr
    "Мику подходит к столу и достаёт оттуда листы, уже размеченные для нот."
    mi "Так, нет, давай не ноты, давай попроще - табулатуры!"
    play sound ds_sfx_int
    enc "В табулатурах, в отличие от нот, обозначается явно, где надо зажать струну гитары."
    "Она достаёт новые листы, уже с шестилинейным станом, и приносит тебе. В начале каждой строки буквы TAB явно обозначают, что это не ноты."
    show mi normal pioneer at center
    with dspr
    mi "Cмотри сюда. Эти линии соотвествуют струнам гитары. А циферки - тому, какой лад надо зажать. То есть, где тебе надо поместить пальчик, начиная с конца!"
    me "Ну, это и ежу понятно... что с сочинением?"
    mi "Ой, сейчас всё будет! Ты хочешь же что-нибудь романтичное, Семён-кун?"
    play sound ds_sfx_int
    dra "Давай лучше трагичное. Выложим всю нашу изнывающую от боли душу в эти ноты, то бишь цифры!"
    play sound ds_sfx_psy
    vol "Нет, надо показать свой настрой! Вперёд и с песней! Весёлой, торжественной!"
    play sound ds_sfx_psy
    aut "Тогда уж марш! Угрожающий! Чтоб эта Алиса даже не смела на тебя рыпаться!"
    window hide
    menu:
        "Сочинить романтическую песню":
            window show
            me "Да, ты правильно поняла мою идею."
            show mi smile pioneer at center
            with dspr
            mi "Тогда приступим!"
            $ ds_composition_type = 1
        "Сочинить трагичную песню":
            window show
            me "Не совсем. Я хочу драмы! Трагедии! Давай сочиним что-нибудь разрывающее сердце!"
            show mi shocked pioneer at center
            with dspr
            mi "Сомневаюсь, что это понравится Алисе-тян, не в её характере подобное..."
            me "Ну ладно, тогда давай то, что ты скажешь."
            $ ds_composition_type = 2
        "Сочинить весёлую песню":
            window show
            me "Надо бы что-нибудь весёленкое! Согласно духу Алисы!"
            show mi serious pioneer at center
            with dspr
            mi "Ну, насчёт духа Алисы, мне кажется, всё не так просто. Но вообще можно, думаю, хорошо-хорошо получится!"
            $ ds_composition_type = 3
        "Сочинить марш":
            window show
            me "Надо бы показать силу Алисе! Давай марш напишем! Прям грозный!"
            show mi shocked pioneer at center
            with dspr
            mi "Что тебе Алиса-тян такого сделала? Разве что пошутила пару раз, наверное..."
            mi "Только марши плохо подходят под гитару..."
            $ ds_composition_type = 4
    me "Что ж, попробуем."
    mi "Хорошо."
    "Она берёт гитару и наигрывает первую строфу."
    "Ещё раз."
    "И ещё."
    "Пока ты не запомнил."
    mi "Справишься?"
    "Ты киваешь и берёшь в руки гитару."
    mi "И?"
    play sound ds_sfx_mot
    inf "После нескольких попыток у тебя получается извлечь из инструмента нечто, похожее на мелодию."
    mi "Отлично!"
    "Мику хватает карандаш и строчит по бумаге с табулатурой."
    play sound ds_sfx_mot
    per_eye "Заглядывая ей за плечо, ты можешь увидеть ряды чисел с чертами."
    per_eye "7-7-7-7-7-7 - и так много семёрок, потом внезапно 4 выше, потом снова семёрки..."
    show mi sad pioneer with dspr
    "Потом останавливается и перечёркивает всё."
    mi "Не то. Нет, не то."
    "Бормочет она себе под нос."
    mi "И это тоже."
    mi "Семён-кун, давай и ты поучаствуешь?"
    me "Да, конечно. Что такое?"

    call ds_day3_compose

    show mi happy pioneer at center
    with dspr
    mi "Иди, Семён-кун, покоряй Алису-тян! Ей должно понравиться!"
    window hide
    menu:
        "Поблагодарить":
            window show
            me "Cпасибо, Мику!"
            "И ты выходишь."
        "Похвалить":
            window show
            me "Классно вышло!"
            show mi shy pioneer at center
            with dspr
            mi "Да ладно тебе! Мы же вместе это сочинили."
            $ ds_lp['mi'] += 1
            "Пока, в общем! И спасибо."
            "И ты выходишь."
        "Молча выйти":
            window show
            "Ты выходишь, ничего не говоря Мику."
            $ ds_lp['mi'] -= 1
    if ds_punished:
        jump ds_day3_mt_interrogate
    else:
        jump ds_day3_dinner

label ds_day3_forest:
    window show
    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_near_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "Выйдя на улицу, ты замешкиваешься на пару секунд и сталкиваешься с Электроником."
    show el normal pioneer at center   with dissolve
    play sound ds_sfx_int
    lgc "Похоже, он идёт в свой кружок."
    el "Куда спешишь?"
    window hide
    menu:
        "Пойти с Электроником":
            window show
            me "Никуда..."
            show el smile pioneer at center
            with dspr
            el "О, идём тогда со мной!"
            me "Я как раз это и хотел предложить..."
            $ ds_lp['el'] += 1
            el "Тогда иди, а я позже подойду!"
            hide el with dissolve
            me "Ладно..."
            jump ds_day3_clubs
        "Продолжить путь":
            window show
    if skillcheck('conceptualization', lvl_medium, passive=True):
        play sound ds_sfx_int
        con "{result}Скажи красиво. Удиви его!"
        me "Я?..{w} Мой шаттл отбывает через десять минут."
        $ ds_skill_points['conceptualization'] += 1
        show el shocked pioneer at center   with dspr
        el "Чего?{w} Эй, подожди!"
    else:
        me "По делам!"
        "И ты убегаешь."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_square_day 
    with dissolve

    window show
    "Слова Электроника растворяются в воздухе."
    "Ты выбегаешь на площадь."
    play sound ds_sfx_fys
    hfl "Явно не самое удачное место, чтобы спрятаться."
    th "Куда дальше?{w} Дальше куда?.."
    play sound ds_sfx_int
    lgc "Самым удачным местом, несомненно, то, где меньше людей."
    lgc "Соответственно, это лес."
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "day"
    scene bg ext_polyana_day 
    with dissolve

    play ambience ambience_forest_day fadein 3

    window show
    "Через полминуты ты уже сидишь на пеньке рядом с лесной тропинкой и отдыхаешь."
    play sound ds_sfx_psy
    svf "Удачно убежал-то, однако!"
    play sound ds_sfx_psy
    aut "Это должно научить Ульянку, как надо себя вести! Ведь уже не ребёнок!"
    th "И правда…{w} Уже не ребёнок…"
    play sound ds_sfx_psy
    vol "А может быть, ты поступил не совсем правильно?"
    vol "В любом случае немалая часть посуды на твоей совести."
    play sound ds_sfx_mot
    com "Да и начнём с того, что можно было вообще не начинать."

    play music music_list["take_me_beautifully"] fadein 5

    sl "Как погодка?"
    show sl normal pioneer at center   with dissolve
    "Перед тобой стоит Славя."
    svf "Как незаметно подкралась!{w} Хорошо хоть не Ольга Дмитриевна."
    me "Ничего…"
    play sound ds_sfx_psy
    vol "Только и можешь ответить ты."
    show sl smile pioneer at center   with dspr
    sl "А я так и думала, что найду тебя здесь."
    me "Почему?"
    sl "Не знаю, просто…"
    show sl normal pioneer at center   with dspr
    "Она смотрит на небо."
    sl "Здесь меньше людей."
    play sound ds_sfx_mot
    res "Неужели Славя считает тебя социофобом?!"
    play sound ds_sfx_psy
    sug "Впрочем, основания у неё есть."
    me "А ты… что здесь делаешь?"
    show sl smile2 pioneer at center   with dspr
    sl "Тебя ищу."
    play sound ds_sfx_psy
    emp "Она вновь улыбается, но в этот раз как-то по-другому, приветливее, что ли."
    me "Меня? Зачем?"
    show sl smile pioneer at center   with dspr
    sl "Не догадываешься?"
    vol "Ты уже приготовился выслушать в свой адрес несколько ласковых."
    show sl normal pioneer at center   with dspr
    sl "Понимаю, что ты виноват меньше, чем Ульяна."
    aut "Тебя оправдывает помощница вожатой!{w} От этого чувствуешь себя ещё более жалким."
    aut "Нет, ну серьёзно, у нас же тут не {i}плохой и хороший полицейский{/i}!"
    show sl smile pioneer at center   with dspr
    sl "Но раз уж не стал помогать ей, то поможешь мне."
    "Сказав это, Славя вновь смотрит на небо."
    th "Интересно, что она там ищет?"
    me "И в чём помощь заключается?"
    show sl normal pioneer at center   with dspr
    sl "Нужно перебрать книги в библиотеке."
    vol "Это куда лучше, чем каторжные работы с Ульянкой. Лучше соглашайся."
    window hide
    menu:
        "Согласиться":
            window show
            $ ds_forest_accept_sl = 1
        "Отказаться":
            window show
            $ ds_forest_accept_sl = -1
            me "Нет уж! Я не пойду! У меня есть дела!"
            show sl angry pioneer at center
            with dspr
            sl "Плохо... очень плохо..."
            sl "Ладно уж, иди по своим делам!"
            hide sl with dissolve
            th "И пойду!"
            $ disable_current_zone_ds_small()
            jump ds_day3_after_lunch
    me "Весь в вашем распоряжении, мадемуазель. Или мадам?"
    show sl laugh pioneer at center   with dspr
    "Она смеётся."

    stop ambience fadeout 2

    sl "Тогда пройдёмте со мной, месье!"
    $ ds_lp['sl'] += 1
    window hide
    jump ds_day3_library

label ds_day3_library:
    $ ds_after_lunch_who = 'mz'
    $ persistent.sprite_time = "day"
    scene bg ext_library_day 
    with dissolve

    if ds_forest_accept_sl == 1:
        show sl normal pioneer at center   with dissolve
    window show
    "Через несколько минут ты оказываешься у библиотеки."
    if ds_punished:
        play sound ds_sfx_fys
        hfl "Всю дорогу ты с опаской озираешься по сторонам, боясь встретить Ольгу Дмитриевну."
        if ds_forest_accept_sl == 1:
            play sound ds_sfx_mot
            com "Славя, кажется, не замечала этого."
            th "И вообще, весьма странно, что она не отругала меня."
            th "Конечно, Славя уж точно полицейский добрый."
    window hide

    stop music fadeout 3

    $ persistent.sprite_time = "day"
    scene bg int_library_day 
    with dissolve

    play ambience ambience_library_day fadein 3

    window show
    play sound ds_sfx_int
    con "Внутри библиотеку освещает яркий солнечный свет, в котором купаются мириады пылинок."
    con "Особая библиотечная пыль с особым запахом, который ни с чем не спутаешь."
    con "Микроскопические кусочки отживающих свой век собраний сочинений классиков марксизма-ленинизма."
    th "Интересно, одинаково ли пахнет пыль рядом с полками художественной литературы и с книгами по физике и химии?"
    show sl normal pioneer at center
    show mz normal pioneer at right
    with dissolve
    $ ds_lp['mz'] += 1
    if ds_forest_accept_sl != -1:
        $ ds_lp['sl'] += 1
        $ ds_helped_sl = True
    if ds_forest_accept_sl == 0:
        sl "Ой, привет, Семён!"
        me "Привет..."
    mz "Так. Садись за машину. И открой базу данных библиотеки."
    "Ты садишься за компьютер. Рассудив, что «КНИГИ.БД» - это и есть искомая база данных, ты открываешь файл."
    "Женя тем временем обращается к Славе."
    mz "Давай ты начнёшь с тех рядов."
    "Она показывает на книжный шкаф около бюста Ленина."
    me "А что конкретно делать надо?"
    show mz bukal pioneer at right
    mz "Какой ты недогадливый! Славя будет снимать книги и называть их, ты - проверять, есть ли они в базе данных."
    mz "Если книги не окажется - Славя принесёт её тебе, и ты вобьёшь все данные с книги."
    mz "А мне надо будет отойти по делам. Приступайте, да пошевеливайтесь побыстрее!"
    play sound ds_sfx_int
    vic "Судя по количеству пыли, чтение – явно не самое любимое занятие пионеров."
    hide sl
    hide mz
    with dissolve
    "Вы принимаетесь за работу."
    "Славя берёт первую книгу, кричит тебе название."
    me "Есть!"
    "Затем вторая, третья, и так книга за книгой..."
    sl "Л.И. Брежнев «Воспоминания»"
    me "Нету..."
    show sl smile pioneer at center
    with dissolve
    "Славя передаёт тебе книгу, ты забиваешь автора, название, издательство, год выпуска и прочие данные и возвращаешь книгу ей."
    sl "Ну как?"
    me "Нормально, работаем потихонечку."
    me "А ты читала что-нибудь из этого?"
    sl "Из чего?"
    me "Ну, про коммунизм…"
    sl "Нет, мне больше историческая литература нравится.{w} Приключения ещё."
    me "И мне…"
    th "Историческую литературу я не очень люблю, но по сравнению с классовой борьбой!"
    sl "Ты не обижайся на Ульяну."
    me "Не обижаюсь..."
    aut "Действительно, случившееся в столовой уже не так больно задевает твоё самолюбие."
    vol "К тому же до библиотеки ты успел отмыться от остатков обеда в лесном озере."
    sl "Она не со зла всё это."
    me "Со зла или нет, но надо думать, что делаешь!{w} Впрочем, ладно..."
    "Вы обрабатываете книгу за книгой. Практически никого из авторов ты не знаешь, не говоря об их нетленках."
    play sound ds_sfx_int
    enc "Через минуту ты уже забудешь, кто они, а о чём они писали, так и не узнаешь никогда."
    enc "Такова судьба многих писателей – стать безвестным набором букв в толстом переплёте на полке библиотеки несуществующего пионерлагеря."
    show sl normal pioneer at center   with dissolve
    sl "Так, я не могу дотянуться до верху... Помоги, пожалуйста!"
    play sound ds_sfx_psy
    emp "В этот раз её улыбка показалась тебе несколько игривой."
    play sound ds_sfx_int
    vic "Даже с твоим немаленьким ростом книги не достать."
    me "Сейчас!{w} Стул только принесу."
    hide sl  with dissolve
    "Ты встаёшь на стул, снимаешь книги и передаёшь их Славе, которая складывает их на полу."
    "Через некоторое время остаётся всего десяток-другой в дальнем конце полки."
    if skillcheck('visual_calculus', lvl_challenging, passive=True):
        vic "{result}Не пытайся дотянуться. Упадёшь!"
        window hide
        menu:
            "Переставить стул":
                window show
                $ ds_skill_points['visual_calculus'] += 1
                "Ты переставляешь стул и снимаешь книги."
                sl "Отлично! Давай их обработаем и пойдём ужинать!"
                "Ты забиваешь оставшиеся книги в базу данных. После чего вы возвращаете их на место."
                show mz normal pioneer at center
                with dissolve
                mz "Сделали всё? Отлично! Спасибо!"
                $ ds_lp['mz'] += 1
                $ volume(0.6, "music")

                $ volume(0.7, "sound")

                play sound sfx_dinner_jingle_speaker
                play sound ds_sfx_mot
                per_hea "Музыка! Пора на ужин!"
                sl "Ужин."
                me "Угу…"
                sl "Пойдём?"
                me "Пойдём…"
                window hide

                stop ambience fadeout 2

                $ persistent.sprite_time = "day"
                scene bg ext_dining_hall_away_day 
                with dissolve

                play ambience ambience_camp_center_day fadein 3

                window show
                "Всю дорогу до столовой ты молчишь."
                play sound ds_sfx_psy
                vol "Славя болтает о каких-то повседневных лагерных делах, но, так как это по сути монолог, не возникает желания вслушиваться."
                window hide

                $ persistent.sprite_time = "day"
                scene bg ext_dining_hall_near_day 
                with dissolve

                $ volume(1.0, "sound")
                $ volume(1.0, "music")

                if ds_punished:
                    jump ds_day3_mt_interrogate
                else:
                    jump ds_day3_dinner
            "Дотянуться":
                window show
    th "Кажется, дотянуться будет несложно."
    play sound ds_sfx_psy
    vol "Ты всегда предпочитаешь побольше схватить за раз, чем ходить дважды.{w} И достать так, чем передвигать стул."
    vol "Это стало роковой ошибкой…"
    window hide

    play sound sfx_chair_fall

    with vpunch

    play sound2 sfx_bodyfall_1

    $ renpy.pause(1)

    scene cg d3_sl_library 
    with fade

    stop ambience fadeout 2

    play music music_list["eternal_longing"] fadein 5

    window show
    "Открыв глаза, ты понимаешь, что лежишь на Славе."
    $ ds_lay_on_sl = True
    if skillcheck('reaction_speed', lvl_challenging, passive=True):
        play sound ds_sfx_mot
        res "{result}Быстрее вскакивай! Иначе проблем не оберёшься, если кто увидит!"
    window hide
    menu:
        "Поинтересоваться самочувствием":
            window show
            me "Ты не… Я тебя не… Жива?!"
            "Ты не на шутку испугался."
            th "Хоть мне сейчас и 17 лет, но упасть со стула на девочку!"
            sl "Жива."
            "Её лицо буквально в паре сантиметров от твоего."
            me "Ничего не сломала?"
            sl "Вроде нет."
            sl "Из тебя плохой каскадер выйдет."
            "Она смеётся."
            me "Точно."
            "Ты смотришь в её глаза.{w} Просто смотришь."
            play sound ds_sfx_psy
            sug "Не зная, что сказать..."
            play sound ds_sfx_psy
            emp "А Славя то ли тоже не знает..."
            play sound ds_sfx_fys
            ins "То ли решила предоставить инициативу тебе!"
            play sound ds_sfx_psy
            vol "И ты бы, может, что и сделал..."
        "Проявить инициативу":
            play sound ds_sfx_fys
            ins "Такими темпами может случиться что-то…"
            ins "Её губы так близко!"
            ins "У тебя появились вполне естественные желания... Воплоти их!"
            "И ты целуешь Славю."
            play sound ds_sfx_psy
            emp "На её лице читается удивление..."
            if ds_lp['sl'] >= 15:
                emp "...и тут она улыбается и поглаживает тебя по щеке."
                $ ds_lp['sl'] += 2
                "Затем она мягко отодвигает тебя от себя..."
                sl "Семён... мне приятно... но не при Жене давай..."
                me "Ладно..."
            else:
                play sound ds_sfx_fys
                with hpunch
                pat "И тут тебе прилетает пощёчина."
                sl "Что ты себе позволяешь?! При Жене ко мне лезешь?!"
                $ ds_lp['sl'] -= 2
                me "Извини..."
        "Отскочить от Слави":
            window show
            "Ты быстро собираешься с мыслями и перекатываешься так, чтобы не лежать {i}на{/i} Славе."
            me "Ты как? Всё нормально?"
            sl "Да, кажется... не переживай."
        "Продолжать лежать":
            window show
            vol "Ты, может, и хочешь встать, но не можешь."
            "Славя же просто лежит молча и смотрит тебе в глаза."
        "Вскочить на ноги" if ds_last_skillcheck and (ds_last_skillcheck.result):
            window show
            "Ты вскакиваешь со Слави как ни в чём не бывало."
            $ ds_lay_sl = False
            scene bg int_library_day 
            show sl surprise pioneer at center
            with dissolve
            me "Всё нормально?"
            sl "Ну да... наверное..."
    if ds_lay_on_sl:
        mz "А что это вы тут разлежались?!"
        th "Женя... Что теперь будет?"
        mz "Вы вообще обнаглели мне тут устраивать ТАКОЕ в библиотеке?!"
        sl "Жень, ты не так всё поняла?.."
        mz "Ну ладно этот обалдуй, но ты-то, Славя?! От тебя такого я не ожидала?!"
        sl "Да Семён просто упал на меня, вот и всё..."
        mz "Да вечно у мужиков миллион оправданий..."
        $ ds_lp['mz'] -= 2
    $ volume(0.6, "music")

    $ volume(0.7, "sound")

    play sound sfx_dinner_jingle_speaker
    play sound ds_sfx_mot
    per_hea "Музыка! Пора на ужин!"
    sl "Ужин."
    me "Угу…"

    if ds_lay_on_sl:
        sl "Пойдём?{w} Или ещё полежим?"
        "Она опять улыбнулась, и на этот раз её улыбка показалась мне хитрой, словно намекающей на что-то."
    else:
        sl "Пойдём?"
    me "Пойдём…"
    if ds_lay_on_sl:
        "Я не сдвинулся с места."
        sl "Чтобы пойти, нужно сначала встать."
        me "Очевидно…"
        "Словно какая-то неведомая сила не давала мне сдвинуться с места."

        stop music fadeout 3

        play ambience ambience_library_day fadein 3

        "Славя, похоже, поняла это и аккуратно выползла из-под меня."
        window hide

        $ persistent.sprite_time = "day"
        scene bg int_library_day 
        with dissolve

        stop sound fadeout 2

        window show
        sl "Так и будешь лежать?"
        "Она рассмеялась."
        show sl smile2 pioneer at center   with dissolve   
        "Тут наконец я окончательно пришёл в себя и встал."
        me "Прости…"
        sl "Да ничего."
    sl "Только мы не закончили.{w} Надо будет потом остальное перебрать."
    me "Да, конечно."
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_away_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "Всю дорогу до столовой ты молчишь."
    play sound ds_sfx_psy
    vol "Славя болтает о каких-то повседневных лагерных делах, но, так как это по сути монолог, не возникает желания вслушиваться."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_near_day 
    with dissolve

    $ volume(1.0, "sound")
    $ volume(1.0, "music")

    if ds_punished:
        jump ds_day3_mt_interrogate
    else:
        jump ds_day3_dinner

label ds_day3_cyber:
    $ ds_after_lunch_who = 'el'
    $ persistent.sprite_time = 'day'
    scene bg ext_clubs_day
    with dissolve
    "Через пару минут ты оказываешься у здания кружков."
    play sound sfx_open_door_clubs
    scene cg d5_clubs_robot
    with dissolve
    play ambience ambience_clubs_inside_day fadein 2
    "В клубе ты видишь Электроника, Шурика и..."
    play sound ds_sfx_mot
    per_eye "И робота-кошкодевочку!"
    me "Привет, кибернетики!"
    el "Эм... привет..."
    sh "Да, привет..."
    play sound ds_sfx_psy
    emp "Они крайне смущены."
    scene bg int_clubs_male_day
    show el surprise pioneer at right
    show sh surprise pioneer at left
    with dissolve
    window hide
    menu:
        "Спросить про робота":
            window show
            me "Это что?"
            el "Да так... мы тут робота строим..."
            me "Какой-то уж {i}необычный{/i} робот..."
            el "Помнишь, мы рассказывали об увиденной кошкодевочке?"
            if ds_seen_catgirl_photo:
                me "Да припоминаю фотку..."
            else:
                me "Неа, вы не рассказывали!"
                sh "Ну, значит, считай, что рассказали."
            el "В общем, мы решили смоделировать... роботом... для изучения?"
            play sound ds_sfx_fys
            ins "Все мужчины любят кошкодевочек! Какая высокотехноличная секс-кукла!"
        "Промолчать":
            window show
            me "Ладно, я вижу, чем вы тут занимаетесь..."
    el "Cлушай... а может, поможешь нам?"
    window hide
    menu:
        "Cогласиться":
            window show
            me "Давайте!"
        "Отказаться":
            window show
            me "Ну нет... я не готов..."
            show el upset at right
            with dspr
            el "Ну ладно..."
            "И ты идёшь куда-нибудь в другую локацию."
            $ disable_current_zone_ds_small()
            stop ambience fadeout 2
            jump ds_day3_after_lunch
    show el smile pioneer at center
    show sh normal pioneer at center
    with dspr
    el "Отлично! Вот смотри, тут..."
    scene cg ds_day3_robot_fail
    with dissolve
    play sound ds_sfx_mot
    per_eye "Ты не заметил, как не закрыл дверь. Чёрный кот воспользовался этим и прошмыгнул в помещение."
    "И мало того, что прошмыгнул - он запрыгнул на стол, где лежит робот. и пробежался по нему."
    play sound ds_sfx_mot
    res "И надо же было такому случиться - на столе стояла чашка чая. Именно что стояла - теперь весь чай оказался на роботе."
    play sound ds_sfx_fys
    hfl "Роботу тут уже не поможешь. Вам бы о самих себе побеспокоиться."
    window hide
    menu:
        "Спасать робота":
            window show
            "Ты берёшь робота за руку..."
            play sound_loop ds_electrocution
            el "Семён..."
            play sound ds_sfx_psy
            vol "Поздно - взявшись за провод, ты уже не можешь оторвать руку от него."
            play sound ds_sfx_fys
            edr "Последнее, что ты чувствуешь перед тем, как пасть - разряд, прокатившийся по твоему телу и сковавший твои движения."
            scene black with dissolve2
            stop sound_loop fadeout 2
            stop ambience fadeout 2
            jump ds_end_electrocution
        "Бежать":
            window show
            me "СПАСАЙСЯ КТО МОЖЕТ!"
            scene bg ext_clubs_day
            with dissolve
            stop ambience
            "С истошным воплем ты выбегаешь из клуба."
            "Отдышаться у тебя получается только на улице."
            show el surprise pioneer at left
            show sh normal pioneer at right
            with dissolve
            el "Ты чего, Семён?"
            me "Там робот! Он сейчас взорвётся!"
            sh "Не переживай. Там нечему взрываться. Тем более, мы отключили его от сети."
            me "А... ну хорошо."
            show el normal pioneer at left
            with dspr
            el "Ну что, поможешь нам отремонтировать робота?"
            window hide
            menu:
                "Согласиться":
                    window show
                    me "Да, помогу конечно!"
                    $ ds_lp['el'] += 1
                    show el smile pioneer at left
                    show sh smile pioneer at right
                    with dspr
                    el "Отлично, идём!"
                    "И вы возвращаетесь в клуб."
                    scene int_clubs_male_day
                    show el normal pioneer at left
                    show sh normal pioneer at right
                    with dissolve
                    play ambience ambience_clubs_inside_day fadein 2
                "Отказаться":
                    window show
                    me "Нет уж! Я не хочу погибнуть!"
                    show el upset pioneer at left
                    with dspr
                    el "Ну ладно..."
                    $ ds_lp['el'] -= 1
                    hide el
                    hide sh
                    with dissolve
                    "И они заходят в клуб."
                    "Ты же думаешь, куда тебе двигаться дальше."
                    $ disable_current_zone_ds_small()
                    jump ds_day3_after_lunch
        "{check=visual_calculus:8}Отключить электричество":
            if skillcheck('visual_calculus', lvl_easy):
                window show
                play sound ds_sfx_int
                vic "{result}Видишь кабель? Теперь видишь розетку? Вытащи кабель из розетки - и дело с концом."
                "Ты хладнокровно вытаскиваешь провод питания из розетки. Теперь можно безопасно работать с роботом."
                scene bg int_clubs_male_day
                show el smile pioneer at left
                show sh normal pioneer at right
                with dissolve
                el "Молодец!"
                sh "Да, справился."
                el "Как настоящий кибернетик!"
                me "Cпасибо..."
                sh "Так, теперь давайте чинить робота."
            else:
                window show
                play sound ds_sfx_int
                vic "{result}Ты не можешь разобраться в куче проводов и совершенно не понимаешь, что делать."
                scene bg int_clubs_male_day
                show el normal pioneer at left
                show sh normal pioneer at right
                with dissolve
                "Пока ты думаешь, Шурик спускается под стол и отключает питание."
                sh "Вот и всё. Теперь давайте ремонтировать робота."
                me "Давайте..."
        "Стоять и смотреть":
            window show
            "Ты стоишь, выпучив глаза и пытаясь понять, что же тебе делать."
            scene bg int_clubs_male_day
            show el normal pioneer at left
            show sh normal pioneer at right
            with dissolve
            "Пока ты думаешь, Шурик спускается под стол и отключает питание."
            sh "Вот и всё. Теперь давайте ремонтировать робота."
            me "Давайте..."
    sh "Так-так... все микросхемы сгорели... мда..."
    show el sad pioneer at left
    show sh upset pioneer at right
    with dspr
    el "Что, всё совсем плохо?"
    sh "Ага... Семён, посмотри, пожалуйста, в кладовой, что там есть."
    me "Ладно..."
    scene bg int_clubs_male2_night
    with dissolve
    stop ambience fadeout 2
    th "Так-так, и где тут микросхемы?"
    play sound ds_sfx_mot
    per_eye "Начни осматривать ящики."
    "Ты начинаешь перебирать ящики."
    th "Тут нет... и тут нет... и тут тоже нет!"
    per_eye "Ты нигде не видишь ничего похожего на микросхемы."
    window hide
    $ renpy.pause(3.0)
    window show
    "Не найдя ничего в ящиках и полках на виду, ты решаешь залезть за занавеску."
    scene cg ds_day3_hatch
    with dissolve
    play sound ds_sfx_mot
    per_eye "Тут люк!"
    play sound ds_sfx_int
    enc "Что же там? Интересно!"
    play sound ds_sfx_fys
    hfl "Скорее всего, там опасно... Лучше не лезь."
    window hide
    menu:
        "Открыть люк":
            window show
            play sound sfx_open_metal_hatch
            "Ты пытаешься открыть люк... но безуспешно."
            play sound ds_sfx_fys
            shi "Ещё не время..."
        "Не трогать":
            window show
    th "Интересно, а кибернетики знают что-нибудь об этом люке?"
    window hide
    menu:
        "Cпросить у кибернетиков":
            scene bg int_clubs_male_day
            show el normal pioneer at left
            show sh normal pioneer at right
            with dissolve
            window show
            play ambience ambience_clubs_inside_day fadein 2
            me "Слушайте... а вот там в кладовке люк, он зачем?"
            show el scared pioneer at left
            show sh scared pioneer at right
            with dspr
            el "Чего? Какой люк?"
            show sh normal pioneer at right
            with dspr
            sh "Мы сами с самого прибытия в лагерь задаёмся этим вопросом."
            sh "Ключей ни у кого нет. Мы выясняли. Видимо, уже давно не исползовался."
            me "Понятно..."
            show el normal pioneer at left
            with dspr
            el "Скорее всего, там какие-то тайные разработки! Эх, вот бы забраться туда..."
            sh "Мечты-мечты..."
            me "Понятно..."
        "Не спрашивать":
            scene bg int_clubs_male2_night
            with dissolve
            "Ты продолжаешь искать нужные детали - но всё ещё безуспешно."
            scene bg int_clubs_male_day
            show el normal pioneer at left
            show sh normal pioneer at right
            with dissolve
            play ambience ambience_clubs_inside_day fadein 2
            "Наконец, ты возвращаешься к кибернетикам - с пустыми руками."
    show el upset pioneer at left
    with dspr
    el "А где детали?"
    me "А нет деталей..."
    show sh upset pioneer at right
    with dspr
    sh "Ясно... придётся пойти завтра в старый лагерь..."
    show el scared pioneer at left
    with dspr
    el "Шур, ты уверен?"
    sh "Да. Нам больше ничего не остаётся."
    me "А там есть микросхемы?"
    sh "Там есть всё! Это опасный путь, но я его пройду!"
    el "Ну ладно... будь осторожен!"
    show sh smile pioneer at right
    with dspr
    sh "Да ладно вам!.. Завтра пойду!"
    play sound ds_sfx_psy
    emp "Успокоившийся было Электроник напрягся снова."
    el "Может, не надо, тут найдём?"
    sh "Нет, я пойду туда и точка!"
    window hide
    menu:
        "Отговорить":
            window show
            me "Мне тоже кажется, что лучше не стоит."
            sh "Нам ничего больше не остаётся. Придётся идти!"
            me "Ну ладно, как скажешь..."
            $ ds_lp['el'] += 1
        "Поддержать":
            window show
            me "Да, правильно, так и надо! Я уверен, что всё получится!"
            sh "Спасибо за поддержку."
        "Промолчать":
            window show
    play sound sfx_dinner_horn_processed
    show el smile pioneer at left
    with dspr
    el "Идём ужинать!"
    sh "Да, идём."
    me "Идём..."
    stop ambience fadeout 5
    if ds_punished:
        jump ds_day3_mt_interrogate
    else:
        jump ds_day3_dinner

label ds_day3_medic:
    $ ds_after_lunch_who = 'cs'
    $ persistent.sprite_time = 'day'
    scene bg ext_aidpost_day
    with dissolve
    "Ты выходишь к медпункту."
    if ds_health < 0:
        play sound ds_sfx_fys
        edr "Тебе явно не лишним будет взять каких-нибудь таблеток - чувствуешь ты себя не очень."
    
    play sound sfx_open_dooor_campus_1
    scene cg ds_day3_cs_waiting
    with dissolve
    play sound ds_sfx_int
    lgc "Кажется, ты тут ожидаемый гость."
    play sound ds_sfx_fys
    ins "И {i}желанный{/i}!"
    play music ds_cs_theme
    cs "Ну привет... пионер. Решил вновь навестить... одинокую женщину?"
    play sound ds_sfx_int
    rhe "Она так нарочито делает паузы и говорит таким нарочито томным голосом... как будто намекает на что-то."
    ins "Не намекает, а говорит прямо: «я хочу тебя!»"
    ins "Заметь, кстати, какая у неё привлекательная попка... так выпячена."
    play sound ds_sfx_fys
    edr "Так, всё, {i}hör auf{/i}! Довольно пошлостей, нам нужны лекарства!"
    scene bg int_aidpost_day
    show cs normal medic2 glasses at center
    with dissolve
    "Наконец, Виола встаёт и смотрит на тебя суровым пристальным взглядом."
    cs "Ну-с, чего изволите, молодой человек?"
    window hide
    menu:
        "Попросить лекарств" if ds_health < 0:
            window show
            me "Мне бы таблеток... голова болит сильно."
            show cs sorrow medic2 glasses at center
            with dspr
            cs "Сейчас будут... пионер."
            hide cs with dissolve
            play sound ds_sfx_psy
            emp "На лице и в голосе читается некоторое разочарование."
            show cs serious medic3 glasses at center
            with dissolve
            cs "Вот, держи, пионер."
            "Ты берёшь таблетку и принимаешь её."
            $ ds_restore_health()
            play sound ds_sfx_fys
            edr "Уже через пару минут тебе становится лучше."
            cs "Это всё?"
            window hide
            menu:
                "Остаться":
                    window show
                    me "Нет, конечно, ещё мне нужны {i}вы{/i}!"
                "Уйти":
                    window show
                    me "Да... спасибо."
                    show cs normal medic2 glasses at center
                    with dspr
                    cs "Ну как скажешь... пионер. Если что надо - приходи в любое время."
                    $ ds_lp['cs'] -= 1
                    scene bg ext_aidpost_day
                    with dissolve
                    th "Так, куда теперь?"
                    $ disable_current_zone_ds_small()
                    jump ds_day3_after_lunch
        "Предложить провести время вместе":
            window show
            me "А знаете... я ради {i}вас{/i} пришёл!"
        "Уйти":
            window show
            me "Ой, извините, я ошибся! Я пойду, пожалуй."
            show cs sorrow medic2 glasses at center
            with dspr
            cs "Ну ладно... пионер."
            scene bg ext_aidpost_day
            with dissolve
            th "Так, куда теперь?"
            $ disable_current_zone_ds_small()
            jump ds_day3_after_lunch
    show cs shy medic2 glasses at center
    with dspr
    cs "То есть, пионер пришёл скрасить одиночество такой женщины как я?"
    me "Ну да... а почему бы и нет?"
    $ ds_lp['cs'] += 1
    show cs smile medic1 glasses at center
    with dspr
    "Она снимает очки и откладывает их на стол."
    show cs smile medic2 at center
    with dspr
    cs "И чем же займёмся? Может, чаю выпьем?"
    me "Давайте..."
    # TODO: CG: чай с Виолой
    "Вы садитесь за стол. Виола разливает чай, и вы приступаете."
    cs "И как твоя жизнь пионерская?"
    me "Да нормально, не жалуюсь. А у вас как дела?"
    cs "Знаешь, мне так {i}одиноко{/i}."
    play sound ds_sfx_int
    rhe "На слове «одиноко» она делает особый акцент. Будто подталкивает к действию."
    play sound ds_sfx_mot
    per_toc "Хорошее замечание насчёт «подталкивает». Потому что ты чувствуешь её ногу кое-где между твоих."
    play sound ds_sfx_fys
    ins "Именно там, где надо. Судя по реакции твоего маленького друга - уж точно."
    per_tas "Вкусный чай!"
    ins "Не сейчас! Тут происходят вещи и повкуснее!"
    play sound ds_sfx_psy
    vol "Ситуация, мягко говоря, некомфортная. Лучше всего будет продолжать пить чай как ни в чём не бывало."
    window hide
    menu:
        "{check=coordination:12}Ответить взаимностью":
            if skillcheck('coordination', lvl_challenging):
                window show
                play sound ds_sfx_mot
                cor "{result}Ты, скинув обувь, естественно, тоже попадаешь своей ногой в точку."
                $ ds_skill_points['coordination'] += 1
                ins "Хотелось бы сказать «в точку G», но до неё не дошло - пока."
                "На лице Виолы отражается точное попадание."
                cs "Ах... ну ты даёшь, пионер..."
                $ ds_lp['cs'] += 2
                "Ты тем временем продолжаешь двигать своей ногой между её. Как и она - между твоими."
            else:
                window show
                play sound ds_sfx_mot
                cor "{result}Сняв обувь с ноги, ты пытаешься сделать ей то же самое."
                cor "Но вместо этого ты попадаешь по ноге."
                $ ds_skill_points['coordination'] += 1
                cs "Ой... немного не туда, пионер."
                "C этими словами она аккуратно поправляет твою ногу, чтобы она оказалась в нужном месте."
                $ ds_lp['cs'] += 1
                ins "Ну уж тут-то ты сообразишь!"
                th "Да я знаю..."
                "И ты шевелишь своими пальцами между её ног, пока она проделывает манипуляции своей у тебя."
        "Попросить прекратить":
            window show
            me "Прекратите, пожалуйста."
            cs "Ладно, как хочешь... пионер."
            play sound ds_sfx_psy
            emp "Видно, что она погрустнела."
            $ ds_lp['cs'] -= 1
            me "Ладно... давайте допивать чай, и я пойду..."
            cs "Как скажешь, пионер."
            window hide
            $ renpy.pause(5.0)
            window show
            play sound sfx_dinner_horn_processed
            "Вскоре звучит сигнал на ужин, и ты пытаешься, не подавая виду, уйти."
            scene bg ext_aidpost_day
            with dissolve
            play sound ds_sfx_mot
            com "Но получается откровенно плохо - более-менее собраться у тебя получается лишь на улице."
            th "Ладно, идём в столовую!"
            if ds_punished:
                jump ds_day3_mt_interrogate
            else:
                jump ds_day3_dinner
        "Закатить скандал":
            window show
            me "Да что вы себе позволяете вообще?! Среди бела дня домогаетесь до пионеров! Я буду жаловаться!"
            $ ds_lp['cs'] -= 2
            scene bg int_aidpost_day
            show cs irritated medic2 at center
            with dissolve
            cs "Не ори ты так, ничего я тебе не сделала ведь."
            me "Да я..! Да вы..! Да вы домогаетесь меня!"
            show cs normal medic2 at center
            with dspr
            cs "И ничего я не домогаюсь. Ну, случайно положила ногу, с кем не бывает?"
            play sound ds_sfx_int
            dra "А её так просто не проведёшь, однако! Причём, так спокойно говорит."
            play sound ds_sfx_psy
            sug "Нет, без шансов. Никого ты не убедишь, что она тебя домогалась."
            window hide
            menu:
                "Остаться":
                    window show
                    me "Ладно... давайте допивать чай, и я пойду..."
                    cs "Как скажешь, пионер."
                    window hide
                    $ renpy.pause(5.0)
                    window show
                    play sound sfx_dinner_horn_processed
                    "Вскоре звучит сигнал на ужин, и ты пытаешься, не подавая виду, уйти."
                    scene bg ext_aidpost_day
                    with dissolve
                    play sound ds_sfx_mot
                    com "Но получается откровенно плохо - более-менее собраться у тебя получается лишь на улице."
                    th "Ладно, идём в столовую!"
                    if ds_punished:
                        jump ds_day3_mt_interrogate
                    else:
                        jump ds_day3_dinner
                "Уйти":
                    window show
                    me "Я пошёл! Счастливо оставаться!"
                    $ ds_lp['cs'] -= 1
                    play sound sfx_close_door_1
                    scene bg ext_aidpost_day
                    with dissolve
                    "И ты выходишь, хлопнув дверью напоследок."
                    th "Надо убираться отсюда поскорее..."
                    $ disable_current_zone_ds_small()
                    jump ds_day3_after_lunch
        "Никак не реагировать":
            window show
            "Ты делаешь вид, будто ничего, ну совсем ничего не происходит."
            "Хотя это и становится труднее - Виола же начинает двигать у тебя между ног, натирая твой ствол."
    per_toc "Вскоре ты чувствуешь влажную теплоту между твоих ног."
    play sound ds_sfx_mot
    com "Как неудобно вышло! Тебе {i}срочно{/i} нужно выйти!"
    scene bg int_aidpost_day
    show cs grin medic2 at center
    with dissolve
    me "Извините... мне нужно отойти."
    cs "Что, уже {i}всё{/i}, пионер?"
    play sound ds_sfx_fys
    ins "В определённом смысле - да, всё."
    me "Я скоро приду!"
    scene bg ext_aidpost_day
    with dissolve
    stop music fadeout 3
    "С этими словами ты выбегаешь из медпункта в сторону ближайшего туалета."
    window hide
    $ renpy.pause(1.0)
    scene bg ds_int_toilet_day
    with dissolve
    window show
    play sound ds_sfx_psy
    ine "Тебя уже в который раз удивляет, насколько тут чистый туалет - ведь лагерные туалеты ты представлял себе по-другому."
    th "Ага, в «совке» настоящем туалет ничуть не «совковый»."
    play sound ds_sfx_int
    enc "Ну, не считая «чаш Генуя» вместо унитазов."
    "Ты подходишь к ближайшей раковине, приспускаешь штаны и трусы, чтобы смыть с себя последствия времяпровождения с Виолой."
    th "Лишь бы никто не зашёл, лишь бы никто не зашёл..."
    play sound ds_sfx_psy
    aut "Ага, щас. По закону подлости именно сейчас сюда заходит человек."
    show un scared pioneer far at center
    with dissolve
    th "Лена?!"
    play sound ds_sfx_mot
    res "Быстро натягивай штаны!"
    play sound ds_sfx_psy
    emp "Ну, это надо сделать, хоть и поздно уже - Лену определённо впечатлило увиденное. И не то, чтобы в хорошем смысле."
    show un scared pioneer at center
    with dspr
    un "Cемён... а ты что делаешь тут?"
    $ ds_lp['un'] -= 1
    me "Да так... запачкался, вот и отмываюсь..."
    show un serious pioneer at center
    with dspr
    un "И как ты {i}там{/i} запачкался?"
    me "Это... личное."
    show un shocked pioneer at center
    with dspr
    un "Ты прям тут... в лагере... {i}этим{/i} занимаешься?"
    if skillcheck('rhetoric', lvl_trivial, passive=True):
        play sound ds_sfx_int
        rhe "{result}Она имеет ввиду мастурбацию."
        play sound ds_sfx_fys
        ins "А у нас было кое-что покруче!"
    me "Нет, ты не так всё поняла!"
    show un serious pioneer at center
    with dspr
    un "Вот же вы, мужчины..."
    res "А типа в этом СССР подростки в принципе {i}говорят{/i} об этом? И знают?"
    window hide
    menu:
        "Cпросить":
            window show
            me "Подожди... а ты откуда знаешь о том, чем мужчины занимаются?"
            show un shy pioneer at center
            with dspr
            un "Так ведь... я была в седьмом классе, честно отсидела все уроки биологии."
            un "И... это... «половое просвещение» там было..."
            play sound ds_sfx_int
            lgc "Значит, в этом Союзе и уроки секспросвета тоже ввели."
            play sound ds_sfx_int
            enc "В то время, как в «нашем» домиинировало «в СССР секса нет!»"
            play sound ds_sfx_int
            dra "На которых и вы должны были отсидеть в рамках этого мира, мессир. Так что не палите контору!"
            me "А... точно... уже забыл совсем."
        "Не спрашивать":
            window show
    show un shy pioneer at center
    with dspr
    un "В общем... я пойду... не буду мешать тебе в твоём важном деле!"
    hide un with dissolve
    "И Лена убегает. Ты же возвращаешься к Виоле."
    scene bg ext_aidpost_day
    with dissolve
    play sound sfx_dinner_horn_processed
    "Но тут звучит сигнал на ужин, и ты перенаправляешься в сторону столовой."
    if ds_punished:
        jump ds_day3_mt_interrogate
    else:
        jump ds_day3_dinner

label ds_day3_home:
    $ ds_after_lunch_who = 'me'
    $ persistent.sprite_time = 'day'
    scene bg ext_house_of_mt_day
    with dissolve
    play sound ds_sfx_int
    con "«Дом, милый дом». А милый ли? И дом ли?"
    th "Неважно, в любом случае я сейчас живу тут."
    scene bg int_house_of_mt_day
    with dissolve
    play sound ds_sfx_fys
    edr "Перед тобой кровать. Возможно, тебе не помешало бы поспать."
    window hide
    menu:
        "Вздремнуть":
            window show
            th "Да, хорошая идея."
            show blink
            "Ты ложишься на кровать и закрываешь глаза..."
            scene black
        "Отбросить мысль":
            window show
            th "Мне ещё столько надо сделать! Некогда почивать!"
            scene bg ext_house_of_mt_day
            with dissolve
            "С этими мыслями ты выходишь из дома и прикидываешь, куда бы тебе пойти."
            $ disable_current_zone_ds_small()
            jump ds_day3_after_lunch
    play music ds_papers_please fadein 5
    scene bg ds_papers_please_back
    show ds_papers_please_front zorder 1
    with dissolve2
    $ ds_num_faults_pp = 0
    play sound ds_sfx_psy
    vol "Перед тобой инструкция. Прочти её."
    moa "Добро пожаловать на ваше место работы, инспектор."
    moa "Вы должны тщательно проверить все документы согласно инструкции."
    moa "Вы можете пропустить въезжающего только при полном соответствии всех документов, во всех остальных случаях отказ."
    moa "Если имеются признаки подделки документов, или человек находится в розыске, он должен быть арестован."
    moa "В случае нарушения вы будете оштрафованы."
    moa "Хорошо вам потрудиться, инспектор."
    moa "Слава Арстотцке!"
    th "Значит, теперь я угодил на пограничный пункт... ясно..."
    show dv normal modern at center
    with dissolve
    me "Ваши документы!"
    "Девушка протягивает тебе документы."
    # TODO: CG: документы Алисы
    me "Цель визита?"
    dvg "Навестить родителей."
    me "Время пребывания?"
    dvg "Один год, там же всё написано!"
    play sound ds_sfx_mot
    per_eye "Право на въезд просрочено. Оно 1978 года, а сейчас 1989."
    me "Ваше право на въезд истекло."
    show dv angry modern at center
    with dspr
    dvg "Вы издеваетесь?! Я сюда так долго шла не для того, чтобы на пороге развернуться!"
    window hide
    menu:
        "Разрешить":
            window show
            play sound ds_stamp
            "Cкрепя сердце ты ставишь зелёную печать в паспорт девушки."
            me "Обновите право немедленно."
            show dv smile modern at center
            with dspr
            dvg "Cпасибо и до свидания!"
            hide dv with dissolve
            $ ds_num_faults_pp += 5
            moa "МВ: ЗАМЕЧАНИЕ\nПраво на въезд истекло\nНАЛОЖЕН ШТРАФ - [ds_num_faults_pp] КРЕДИТОВ"
            $ ds_approved_pp['dv'] = True
        "Отказать":
            window show
            play sound ds_stamp
            "Ты всё же решаешь развернуть её."
            me "Простите."
            dvg "Как так?!"
            show dv cry modern at center
            with dspr
            dvg "Что, я не увижу родителей больше?"
            me "Оформите все документы как надо - и увидите."
            show dv rage modern at center
            dvg "Не поеду я больше к вам!"
            hide dv with dissolve
    th "И почему эта девушка так похожа на Алису?.. Ещё и зовут её точно так же..."
    play sound ds_sfx_psy
    ine "Всему своё время, Семён..."
    me "Cледующий!"
    show sl normal modern at center
    with dissolve
    slg "Здравствуйте!"
    me "Ваши документы."
    slg "Вот, пожалуйста."
    "Она протягивает тебе бумаги."
    th "Как будто бы всё в порядке..."
    me "Цель визита?"
    slg "Работа."
    me "Время пребывания?"
    slg "Три месяца."
    window hide
    menu:
        "Разрешить":
            window show
            play sound ds_stamp
            me "Добро пожаловать в Арстотцку!"
            show sl smile modern at center
            with dspr
            slg "Cпасибо! Хорошего дня вам, инспектор!"
            hide sl with dissolve
            th "Это было просто."
            $ ds_approved_pp['sl'] = True
        "Отказать":
            window show
            play sound ds_stamp
            "Почему-то ты решаешь, что с ней что-то не так, и ставишь красную печать."
            show sl surprise modern at center
            with dspr
            slg "Как отказано? У меня же всё в порядке."
            me "Cказано, что въезд запрещён - значит запрещён."
            show sl angry modern at center
            with dspr
            slg "До свидания!"
            hide sl with dissolve
            $ ds_num_faults_pp += 5
            moa "МВ: ЗАМЕЧАНИЕ\nВъезд разрешён\nНАЛОЖЕН ШТРАФ - [ds_num_faults_pp] КРЕДИТОВ"
    show mi normal modern at center
    with dissolve
    mig "Доброго дня вам, инспектор-сан!"
    me "Ваши документы."
    "Вместо обычного права на въезд вместе с паспортом она протягивает «Дипломатический статус»."
    play sound ds_sfx_int
    enc "Согласно инструкции в нём должна быть заявлена Арстотцка."
    play sound ds_sfx_mot
    per_eye "А тут этого нет."
    me "У вас нет дипломатического статуса в Арстотцке."
    show mi sad modern at center
    with dspr
    mig "Как так? Видимо, опечатка. Я поправлю обязательно, инспектор-сан!"
    window hide
    menu:
        "Разрешить":
            window show
            play sound ds_stamp
            me "Ладно... только не создавайте проблем."
            show mi smile modern at center
            with dspr
            mig "Ой, спасибочки, инспектор-сан!"
            hide mi with dissolve
            $ ds_num_faults_pp += 5
            moa "МВ: ЗАМЕЧАНИЕ\nОтсутствует дипломатический статус в Арстотцке\nНАЛОЖЕН ШТРАФ - [ds_num_faults_pp] КРЕДИТОВ"
            $ ds_approved_pp['mi'] = True
        "Отказать":
            play sound ds_stamp
            me "Вот когда поправите - тогда и приезжайте. Всего доброго."
            show mi dontlike modern at center
            with dspr
            mig "Вот же бака!"
            hide mi with dissolve
    moa "ОБНОВЛЕНИЕ ПРОТОКОЛА\nДля приезжающих из Объединённой Федерации обязательно наличие прививки от ВИЧ.\nВакцина должна быть действительна. В случае отсутствия - отказ.\nCлава Арстотцке!"
    show el normal modern at center
    with dissolve
    elg "Здравствуйте, товарищ инспектор!"
    "С этими словами он протягивает документы."
    play sound ds_sfx_mot
    per_eye "Он из Объединённой Федерации. И даже вакцина от ВИЧ есть. Только вот же незадача - она просрочена."
    me "У вас просрочена вакцина."
    show el scared modern at center
    with dspr
    elg "Чего? Проверьте ещё раз. В любом случае я ничем не болею!"
    window hide
    menu:
        "Разрешить":
            window show
            play sound ds_stamp
            me "Ладно, проезжайте. Но вакцину сделайте!"
            show el normal modern at center
            with dspr
            elg "Обязательно, товарищ инспектор!"
            hide el with dissolve
            $ ds_num_faults_pp += 5
            moa "МВ: ЗАМЕЧАНИЕ\nСрок действия вакцины от ВИЧ истёк\nНАЛОЖЕН ШТРАФ - [ds_num_faults_pp] КРЕДИТОВ"
            $ ds_approved_pp['el'] = True
        "Отказать":
            window show
            play sound ds_stamp
            me "Не надо тащить к нам ваши болячки! Когда сделаете прививку - тогда приходите снова."
            show el upset modern at center
            with dspr
            elg "Вот же незадача..."
            hide el with dissolve
    show mt normal dress at center
    with dissolve
    mtg "Добрый день, инспектор! Вот мои документы."
    "C этими словами она протягивает тебе паспорт и личную карту гражданина Арстотцки."
    play sound ds_sfx_mot
    per_eye "Проблем нет."
    window hide
    menu:
        "Разрешить":
            window show
            play sound ds_stamp
            me "Cлава Арстотцке!"
            mtg "Cлава Арстотцке, инспектор!"
            mtg "А вы Двачевскую Алису не видели случаем?"
            if ds_approved_pp['dv']:
                me "Да, видел, я её пропустил парой человек раньше."
                show mt smile dress at center
                with dspr
                mtg "Ой, отлично, спасибо. Вы сделали доброе дело, инспектор!"
            else:
                me "Да, у неё не было действительных документов, поэтому во въезде ей было отказано."
                show mt angry dress at center
                with dspr
                mtg "Зря вы это сделали, инспектор... вы сломали ей жизнь!"
            hide mt with dissolve
            th "И зачем ей Алиса понадобилась?"
            $ ds_approved_pp['mt'] = True
        "Отказать":
            window show
            play sound ds_stamp
            show mt surprise dress at center
            with dspr
            mtg "Вы не имеете права! Я гражданка Арстотцки! У меня всё нормально!"
            me "Имею право. Так будет безопаснее."
            show mt angry dress at center
            with dspr
            mtg "Я пожалуюсь в вышестоящие инстанции! Счастливо оставаться!"
            hide mt with dissolve
            $ ds_num_faults_pp += 5
            moa "МВ: ЗАМЕЧАНИЕ\nВъезд разрешён\nНАЛОЖЕН ШТРАФ - [ds_num_faults_pp] КРЕДИТОВ"
    show us normal sport at center
    with dissolve
    usg "Здасьте!"
    "И она бросает тебе паспорт. Только лишь паспорт."
    me "Ваше право на въезд?"
    show us surp1 sport at center
    with dspr
    usg "Какое право на въезд?"
    me "Обычное. Дающее право на въезд в Арстотцку."
    show us upset sport at center
    with dspr
    usg "Нет у меня ничего такого, только паспорт!"
    window hide
    menu:
        "Разрешить":
            window show
            me "В последний раз пропускаю."
            show us grin sport at center
            with dspr
            usg "Как скажете, гражданин начальник!"
            hide us with dissolve
            $ ds_num_faults_pp += 5
            moa "МВ: ЗАМЕЧАНИЕ\nОтсутствует право на въезд\nНАЛОЖЕН ШТРАФ - [5 * ds_num_faults_pp] КРЕДИТОВ"
            $ ds_approved_pp['us'] = True
        "Отказать":
            window show
            me "Без права на въезд нельзя. Приходите в другой раз."
            show us dontlike sport at center
            with dspr
            usg "Какой же ты бука!"
            hide us with dissolve
    show un normal modern at center
    with dissolve
    ung "Здравствуйте..."
    me "Ваши документы."
    "Она отдаёт тебе паспорт."
    play sound ds_sfx_int
    enc "Колечия. Враждебная Арстотцке страна. Оттуда постоянно пытаются проникнуть террористы."
    moa "ОБНОВЛЕНИЕ ПРОТОКОЛА\nДосматривать всех граждан Колечии. Без исключений.\nCлава Арстотцке!"
    me "Цель визита?"
    ung "Мимо проезжаю..."
    me "Время пребывания?"
    ung "Неделя..."
    window hide
    menu:
        "Досмотреть":
            window show
            me "Повернитесь лицом к сканеру."
            "Из принтера вылезает снимок голой девушки. А на нём видны заряды."
            th "Плохо дело..."
            window hide
            menu:
                "Разрешить":
                    window show
                    play sound ds_stamp
                    me "Добро пожаловать в Арстотцку!"
                    show un evil_smile modern at center
                    with dspr
                    ung "Cпасибо, инспектор."
                    hide un with dissolve
                    $ ds_approved_pp['un'] = True
                "Отказать":
                    window show
                    play sound ds_stamp
                    me "Провоз контрабанды запрещён."
                    show un rage modern at center
                    with dspr
                    ung "Вы пожалеете об этом, инспектор! Горько пожалеете!"
                    hide un with dissolve
                "Арестовать":
                    window show
                    me "Подождите."
                    show un scared modern at center
                    with dspr
                    ung "Что вы делаете?"
                    voice "Пройдёмте!"
                    hide un with dissolve
        "Разрешить":
            window show
            play sound ds_stamp
            me "Добро пожаловать в Арстотцку!"
            show un evil_smile modern at center
            with dspr
            ung "Cпасибо, инспектор."
            hide un with dissolve
            $ ds_approved_pp['un'] = True
        "Отказать":
            window show
            play sound ds_stamp
            me "Вы из Колечии. Колечианцам в Арстотцке не рады."
            show un rage modern at center
            with dspr
            ung "Вы пожалеете об этом, инспектор! Горько пожалеете!"
            hide un with dissolve
    th "Кажется, Лена из Колечии более агрессивная, чем Лена из СССР..."
    if ds_approved_pp['un']:
        moa "МВ: ЗАМЕЧАНИЕ"
        with hpunch
        stop music
        play sound2 ds_bombing
        play sound_loop ds_alert
        play sound ds_sfx_mot
        scene black with dissolve
        res "Взрыв! Это теракт!"
        play sound ds_sfx_int
        lgc "Лена оказалась не такой простой!"
        "Ты выбегаешь на улицу с пистолетом в руке."
        scene bg ds_papers_please_teract
        show pi at center
        with dissolve
        pi "Ну привет, Семён."
        me "Кто ты такой?!"
        pi "Я - это ты. А ты - это я."
        me "А взрывать тут всё зачем было?"
        show pi smile at center
        with dspr
        pi "Ты так и не понял? Ты во сне! Ну какая Арстотцка, ну какая граница?"
        me "А почему я во сне оказался тут?! В вымышленной стране!"
        show pi at center
        with dspr
        pi "А ты не заметил никаких пересечений с реальностью?"
        me "Я заметил, что прошедшие через границу люди уж очень напоминают тех, кто в «Совёнке»!"
        pi "Вот, правильно мыслишь..."
        me "Но Лена не устроила бы вот этот теракт!"
        pi "Кто знает, кто знает..."
        me "Да она же тихоня!"
        pi "В тихом омуте черти водятся..."
        me "Да ты можешь мне объяснить, что тут происходит!"
        arb "Это порождение твоего подсознания."
        lim "А почему оно такое? Уж извини - мы тебе подсказать не можем. Не сейчас."
        lim "Возможно, это обманка. Возможно, это предвидение."
        pi "Твои друзья уже всё сказали. Я же добавлю - присмотрись к рыжеволосой девушке."
        me "К Алисе?!"
        pi "Я не помню, как её зовут. Но она тебе нужна. Как и ты ей. Просто вы ещё этого не поняли."
        pi "А теперь прощай."
        hide pi with dissolve
        play sound ds_bombing
        with vpunch
        "Вдруг раздаётся новый взрыв, и ты падаешь на землю."
        stop sound_loop fadeout 2
        window hide
        scene black with dissolve2
        $ renpy.pause(2.0)
    else:
        show pi at center
        with dissolve
        pi "Привет, Семён."
        me "Ваши документы."
        pi "Очнись. Это сон! Ну какая Арстотцка, ну какая граница?"
        me "А... а ты кто такой?"
        pi "Я - это ты. А ты - это я."
        me "Как я оказался тут?"
        pi "А ты не заметил никаких пересечений с реальностью?"
        me "Я заметил, что прошедшие через границу люди уж очень напоминают тех, кто в «Совёнке»!"
        pi "Вот, правильно мыслишь..."
        me "Да ты можешь мне объяснить, что тут происходит!"
        arb "Это порождение твоего подсознания."
        lim "А почему оно такое? Уж извини - мы тебе подсказать не можем. Не сейчас."
        lim "Возможно, это обманка. Возможно, это предвидение."
        pi "Твои друзья уже всё сказали. Я же добавлю - присмотрись к рыжеволосой девушке."
        me "К Алисе?!"
        pi "Я не помню, как её зовут. Но она тебе нужна. Как и ты ей. Просто вы ещё этого не поняли."
        pi "А теперь прощай."
        hide pi with dissolve
        play sound sfx_hell_alarm_clock
        window hide
        stop music fadeout 2
        $ renpy.pause(2.0)
    if ds_num_faults_pp == 0:
        call ds_achievement('arstotzka')
    scene bg int_house_of_mt_day
    hide blink
    stop sound
    show unblink
    show mt surprise pioneer at center
    with dissolve
    window show
    mt "Доброе утро, Семён! Точнее, уже добрый вечер!"
    me "И вам того же, Ольга Дмитриевна."
    if ds_punished:
        play music music_list["revenga"] fadein 2

        show mt rage pioneer at cleft 
        with dissolve
        window show
        mt "Ничего не хотите мне сказать, молодой человек?"
        play sound ds_sfx_psy
        vol "А ты и правда кое-что забыл…"
        me "Нет…"
        mt "Как уборка прошла?"
        me "Хорошо…"
        mt "А мне Ульяна сказала, что не очень."
        me "Так это она виновата!"
        mt "Я что тебе сказала?"
        mt "Чтобы вы вместе убрались!{w} А ты?!"
        $ ds_lp['mt'] -= 1
        play sound ds_sfx_psy
        aut "Так-то она права. Раньше протестовать надо было."
        show mt angry pioneer at cleft   with dspr
        mt "В общем, останешься без ужина!"
        if skillcheck('rhetoric', lvl_up_medium, passive=True):
            play sound ds_sfx_int
            rhe "{result}Это неправомерно. А если пригрозить ей вышестоящими инстанциями?"
        window hide
        menu:
            "Протестовать":
                window show
                me "Как, почему?!"
                play sound ds_sfx_psy
                aut "Твой протест больше походит на требование добавки в тюремной столовой – дерзко, опасно, но глупо и бесполезно."
                mt "В следующий раз будешь знать, что бывает с теми, кто меня не слушается!"
                play sound ds_sfx_psy
                ine "Ольга Дмитриевна представляется тебе не вожатой пионеротряда, а командующей древнеримскими легионами."
                play sound ds_sfx_int
                rhe "Ты просто не знаешь, что ей возразить."
            "Промолчать":
                window show
            "Пригрозить администрацией" if ds_last_skillcheck and (ds_last_skillcheck.result):
                window show
                me "А если я доложу куда надо о вашем самоуправстве?"
                show mt surprise pioneer at center
                with dspr
                mt "Э... ну ладно... иди ужинать..."
                me "Вот то-то же!"
                show mt rage pioneer at center
                with dspr
                mt "Иди уже, пока не передумала!"
                $ ds_lp['mt'] -= 2
                $ ds_skill_points['rhetoric'] += 1
                jump ds_day3_dinner
        mt "Я всё сказала! Свободен!"
        hide mt
        with dissolve
        th "Печально..."
        jump ds_day3_no_dinner
        stop music fadeout 3
    else:
        show mt normal pioneer at center
        with dissolve
        mt "Пора ужинать уже."
        me "А, да, уже иду..."
        scene bg ext_house_of_mt_day
        with dissolve
        "Быстро собравшись, ты направляешься в сторону столовой."
        jump ds_day3_dinner

label ds_day3_mt_interrogate:
    play music music_list["revenga"] fadein 2

    scene bg ext_dining_hall_near_day
    show mt rage pioneer at cleft 
    show sl normal pioneer at cright 
    with dissolve
    window show
    "Подойдя к столовой, ты видишь на крыльце Ольгу Дмитриевну."
    mt "Ничего не хотите мне сказать, молодой человек?"
    play sound ds_sfx_psy
    vol "А ты и правда кое-что забыл…"
    me "Нет…"
    mt "Как уборка прошла?"
    me "Хорошо…"
    mt "А мне Ульяна сказала, что не очень."
    me "Так это она виновата!"
    mt "Я что тебе сказала?"
    mt "Чтобы вы вместе убрались!{w} А ты?!"
    $ ds_lp['mt'] -= 1
    play sound ds_sfx_psy
    aut "Так-то она права. Раньше протестовать надо было."
    if ds_helped_sl:
        show sl sad pioneer at cright   with dspr
        sl "Не ругайте его!{w} Семён мне помог в библиотеке."
        mt "Правда?"
        sl "Правда!"
        show mt angry pioneer at cleft   with dspr
        mt "Это, конечно, замечательно, но…{w} В общем, останешься без ужина!"
        window hide
        menu:
            "Протестовать":
                window show
                me "Как, почему?!"
                play sound ds_sfx_psy
                aut "Твой протест больше походит на требование добавки в тюремной столовой – дерзко, опасно, но глупо и бесполезно."
                mt "В следующий раз будешь знать, что бывает с теми, кто меня не слушается!"
                play sound ds_sfx_psy
                ine "Ольга Дмитриевна представляется тебе не вожатой пионеротряда, а командующей древнеримскими легионами."
                play sound ds_sfx_int
                rhe "Ты просто не знаешь, что ей возразить."
            "Промолчать":
                window show
        sl "Простите его!{w} Под мою ответственность!"
        "Вожатая задумывается."
        show mt normal pioneer at cleft   with dspr
        mt "Ладно уж!"
        show sl smile pioneer at cright   with dspr
        sl "Спасибо!"
    elif (ds_lp['sl'] >= 10) and (ds_forest_accept_sl != -1):
        show sl sad pioneer at cright   with dspr
        sl "Простите его!{w} Под мою ответственность!"
        sl "Я присутствовала при этом, и он правда не был виноват!"
        "Вожатая задумывается."
        show mt normal pioneer at cleft   with dspr
        mt "Ладно уж!"
        show sl smile pioneer at cright   with dspr
        sl "Спасибо!"
    else:
        show mt angry pioneer at cleft   with dspr
        mt "В общем, останешься без ужина!"
        if skillcheck('rhetoric', lvl_up_medium, passive=True):
            play sound ds_sfx_int
            rhe "{result}Это неправомерно. А если пригрозить ей вышестоящими инстанциями?"
        window hide
        menu:
            "Протестовать":
                window show
                me "Как, почему?!"
                play sound ds_sfx_psy
                aut "Твой протест больше походит на требование добавки в тюремной столовой – дерзко, опасно, но глупо и бесполезно."
                mt "В следующий раз будешь знать, что бывает с теми, кто меня не слушается!"
                play sound ds_sfx_psy
                ine "Ольга Дмитриевна представляется тебе не вожатой пионеротряда, а командующей древнеримскими легионами."
                play sound ds_sfx_int
                rhe "Ты просто не знаешь, что ей возразить."
            "Промолчать":
                window show
            "Пригрозить администрацией" if ds_last_skillcheck and (ds_last_skillcheck.result):
                window show
                me "А если я доложу куда надо о вашем самоуправстве?"
                show mt surprise pioneer at center
                with dspr
                mt "Э... ну ладно... иди ужинать..."
                me "Вот то-то же!"
                show mt rage pioneer at center
                with dspr
                mt "Иди уже, пока не передумала!"
                $ ds_lp['mt'] -= 2
                $ ds_skill_points['rhetoric'] += 1
                jump ds_day3_dinner
        mt "Я всё сказала! Свободен!"
        hide mt
        hide sl
        with dissolve
        th "Печально..."
        jump ds_day3_no_dinner
    stop music fadeout 3

    me "Спасибо…"
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_people_day 
    with dissolve

    play ambience ambience_dining_hall_full fadein 3

    window show
    "Вы быстро заходите в столовую."
    show sl smile pioneer at center   with dissolve
    sl "Ладно, я к девочкам сяду, мы с ними договорились.{w} Не скучай!"
    "Она улыбается и машет тебе рукой."
    hide sl  with dissolve
    lgc "Действительно, что бы ты без неё делал!"
    play sound ds_sfx_psy
    vol "Рядом со Славей свободных мест не нашлось, да и её подружек ты не знаешь."
    jump ds_day3_dinner

label ds_day3_dinner:
    $ persistent.sprite_time = 'day'
    scene bg int_dining_hall_people_day
    with dissolve
    play sound ds_sfx_int
    vic "Похоже, тебе предстоит ужинать с Электроником и Шуриком."
    vic "Сесть всё равно больше негде."
    show el normal pioneer at cleft, ds_seated 
    show sh normal pioneer at cright, ds_seated 
    with dissolve
    if skillcheck('authority', lvl_trivial, passive=True):
        play sound ds_sfx_psy
        aut "{result}Когда ты общаешься с ними, у тебя то и дело возникает желание подколоть или просто сказать что-нибудь забавное и смешное."
        me "Приветствую, господа!"
        play sound ds_sfx_fys
        hfl "Может быть, в твоём положении вести себя так несколько рискованно."
        play sound ds_sfx_psy
        vol "Но {i}братья-электроники{/i} служат для тебя источником позитива."
    else:
        me "Добрый вечер."
    window hide
    menu:
        "Спросить, как дела":
            window show
            me "Как ваши дела?"
            el "Неплохо, а твои?"
            me "С переменным успехом."
            sh "Что-то случилось?"
            me "Да много всего случилось."
            el "Расскажешь?"
            if (ds_whom_helped == 'el') and (ds_after_lunch_who == 'el'):
                me "Да вы и так знаете, я же с вами весь день провёл..."
                show el smile pioneer at cleft
                with dspr
                el "И то правда!"
                sh "Спасибо за помощь, кстати."
                el "Да, спасибо!"
            else:
                window hide
                menu:
                    "Рассказать":
                        window show
                        if ds_whom_helped == 'dv':
                            me "Сначала я пришёл на сцену. Оказывается, Алиса превосходно играет на гитаре!"
                            el "Ну, это мы знаем!"
                            sh "При всех её недостатках музыкального таланта у неё не отнять."
                        elif ds_whom_helped == 'un':
                            me "Когда я вышел от вас, я встретил Лену."
                            if ds_un_club:
                                me "Как итог - у нас теперь будет художественный клуб!"
                                show el smile pioneer at cleft
                                with dspr
                                el "Ух ты как классно!"
                            else:
                                me "Она хотела открыть клуб, но не сложилось..."
                                show el surprise pioneer at cleft
                                with dspr
                                el "Почему?"
                                me "Она испугалась предлагать это Ольге Дмитриевне."
                                show el normal pioneer at cleft
                                with dspr
                                el "Вот как..."
                        elif ds_whom_helped == 'sl':
                            me "Сначала со Славей подметал..."
                        elif ds_whom_helped == 'mz':
                            me "Помог нашей библиотекарше Жене с уборкой..."
                            show el smile pioneer at cleft
                            with dspr
                            el "Молодец!"
                            if skillcheck('empathy', lvl_trivial, passive=True):
                                play sound ds_sfx_psy
                                emp "{result}Он не может скрыть своих чувств к ней - всё как на ладони."
                                $ ds_skill_points['empathy'] += 1
                        elif ds_whom_helped == 'us':
                            me "Поиграли в футбол с Ульянкой..."
                        elif ds_whom_helped == 'esc':
                            me "А мы с Ульяной сегодня сбежать попытались! Правда, безуспешно..."
                            show el surprise pioneer at cleft
                            show sh surprise pioneer at cright
                            with dspr
                            el "Ничего себе, а как ты потом от Ольги Дмитриевны живой ушёл?"
                            me "Это следующая часть моей истории..."
                        elif ds_whom_helped == 'mt':
                            me "Сперва в администрации бумажки перебирал..."
                        elif ds_whom_helped == 'ya':
                            me "Вы знаете вожатую младшего отряда, Яну?"
                            el "Не-а!"
                            me "Ну, я ей помогал с детьми."
                            el "Вот это да..."
                        elif ds_whom_helped == 'mi':
                            me "Сперва помог Мику в музклубе."
                            if ds_mi_costume:
                                me "Она ещё такой костюм мне дала на вечер!"
                                el "Классно, везёт!"
                                if skillcheck('empathy', lvl_trivial, passive=True):
                                    play sound ds_sfx_psy
                                    emp "{result}А у него с отношениями немного не складывается."
                                    $ ds_skill_points['empathy'] += 1
                        if ds_punished:
                            if ds_whom_helped == 'esc':
                                me "В общем, заставили нас с Ульяной чистить картошку..."
                            else:
                                me "Потом Ульяна во время обеда меня спровоцировала, а Ольга Дмитриевна возьми и накажи нас обоих!"
                                el "Да, несправедливо..."
                            if ds_after_lunch_who != 'us':
                                me "Но я сбежал!"
                                sh "Да ты прям нарушитель..."
                        if ds_after_lunch_who == 'mi':
                            me "После обеда мы играли с Мику."
                            el "Ого, и ты тоже умеешь играть музыку?"
                            me "Ну... не особо на самом деле..."
                        elif ds_after_lunch_who == 'cs':
                            me "Зашёл к медсестре за таблетками... а она оказалась..."
                            if skillcheck('volition', lvl_legendary, passive=True):
                                me "В общем, она начала домогаться меня!"
                                sh "Ну, что сказать... это Виола. Мы все прошли через это."
                                $ ds_skill_points['volition'] += 1
                            else:
                                play sound ds_sfx_psy
                                vol "{result}Ты не находишь сил рассказать о произошедшем - слишком стыдно. Да и не надо."
                                me "В общем, неважно."
                                el "Ну ладно, не хочешь - не рассказывай."
                        elif ds_after_lunch_who == 'mz':
                            me "После обеда помогал Славе и Жене сортировать книги в библиотеке."
                            show el serious pioneer at cleft
                            with dspr
                            el "Ты там аккуратнее с Женей..."
                            if skillcheck('half_light', lvl_trivial, passive=True):
                                play sound ds_sfx_fys
                                hfl "{result}Он увидел в тебе угрозу. Угрозу его счастью с Женей. Аккуратней с этой темой."
                                $ ds_skill_points['half_light'] += 1
                        elif ds_after_lunch_who == 'me':
                            me "После обеда я вздремнул... и мне сон приснился, где вы все были."
                            show el smile pioneer at cleft
                            with dspr
                            el "Ну, бывает! Видимо, настолько лагерь понравился!"
                            me "Ага..."
                    "Отказаться":
                        window show
                        me "Как-нибудь в другой раз."
                        sh "Как хочешь."
                        "Он разводит руками."
        "Промолчать":
            window show
    show el smile pioneer at cleft   with dspr
    el "После ужина танцы!"
    "Электроник хихикает."
    me "Я в курсе."
    show el normal pioneer at cleft   with dspr
    el "Кого хотел бы пригласить?"
    window hide
    menu:
        "Алису" if ds_dance_dv:
            window show
            me "Алису Двачевскую!"
            show el upset pioneer at cleft
            show sh surprise pioneer at cright
            with dspr
            "Электроник поперхнулся чаем от твоих слов. Шурик тоже впечатлён."
            el "Чего?! Я не ослышался?"
            me "Нет вроде, Алису я пригласить хочу."
            el "Ты уверен?"
            me "Аб-со-лют-но! Она сыграет для нас всех на танцах!"
            show sh normal pioneer at cright
            with dspr
            sh "Неплохо."
        "Лену":
            window show
            me "Лену..."
            el "Ну давай, успехов с ней."
        "Славю":
            window show
            me "Славю хочу пригласить."
            sh "Хороший выбор, мне кажется."
        "Ульяну":
            window show
            me "А чего бы и не Ульянку?"
            show el laugh pioneer at cleft
            with dspr
            el "И как это будет выглядеть с вашей разницей в росте?"
            sh "Лучше подумай ещё. А то другие подумают не того."
            play sound ds_sfx_int
            rhe "Он беспокоится, что тебя в педофилии обвинят."
        "{check=half_light:10}Женю":
            window show
            me "Женю приглашу."
            show el angry pioneer at cleft
            with dspr
            if skillcheck('half_light', lvl_medium):
                play sound ds_sfx_fys
                hfl "{result}Берегись Электроника!"
                "Ты уворачиваешься от летящей в тебя пощёчины."
            else:
                play sound ds_sfx_fys
                with hpunch
                hfl "{result}Прежде чем ты успеваешь как-либо отреагировать, Электроник бьёт тебе по лицу."
                $ ds_damage_health()
            $ ds_skill_points['half_light'] += 1
            el "НЕ СМЕЙ!"
            hfl "Он не на шутку взбесился от твоей реплики. Ты и не мог подумать, что он может быть настолько злым."
            $ ds_lp['el'] -= 2
            me "Ладно-ладно, успокойся."
        "Яну":
            window show
            me "Да вон, думаю с вожатой младшего отряда потанцевать."
            el "Интересный выбор..."
        "Мику":
            window show
            me "Мику позову!"
            show el surprise pioneer at cleft
            with dspr
            el "Так она же занята... В смысле, музыку обеспечивает."
            me "Ну... разберёмся!"
            el "Как скажешь..."
        "Не решил":
            window show
            me "Я ещё не думал над этим."
        "Это секрет":
            window show
            me "А это, друзья, большой-большой секрет!"
            show el laugh pioneer at cleft
            show sh smile pioneer at cright
            with dspr
            el "Ну ладно, как скажешь!"
    window hide
    menu:
        "Спросить в ответ":
            window show
            me "А ты?"
            show el shocked pioneer at cleft   with dspr
            el "Я… Ну я…"
            rhe "Он не ожидал такого вопроса."
            window hide
            menu:
                "{check=conceptualization:11}Предложить свои варианты":
                    if skillcheck('conceptualization', lvl_up_medium):
                        window show
                        play sound ds_sfx_int
                        con "{result}Всё логично. Электронику - Ульяну, Шурику - Алису."
                        me "Ульянку. Она обрадуется."
                        show el serious pioneer at cleft   with dspr
                        el "Ну уж нет!"
                        "Электроник неистово замахал руками."
                        me "А ты, Шурик, пригласи Алису."
                        show sh serious pioneer at cright   with dspr
                        sh "Я, пожалуй, воздержусь."
                        play sound ds_sfx_mot
                        com "Он выглядит спокойнее своего товарища."
                    else:
                        window show
                        play sound ds_sfx_int
                        con "{result}А чего бы им друг с другом не танцевать. Лето в пионерском галстуке, так сказать."
                        me "А давайте вы друг с другом!"
                        show el serious pioneer at cleft
                        show sh seerious pioneer at cright
                        with dspr
                        el "Чего?"
                        sh "Так, нет, там допустимы лишь пара М плюс Ж."
                "Приободрить":
                    window show
                    me "Да ладно вам, ребята, весело будет!"
                "Молча ждать":
                    window show
            el "И вообще!{w} У нас ещё дела!{w} Нам нужно робота доделывать!"
            window hide
            menu:
                "Предложить пригласить робота":
                    window show
                    me "Отличная идея!{w} Пригласите робота! Он у вас умеет танцевать?"
                    sh "Он ещё даже не ходит."
                    play sound ds_sfx_int
                    rhe "Шурик, кажется, не понял прикола."
                    show el smile pioneer at cleft   with dspr
                    el "А что! Будет прекрасная демонстрация наших достижений перед всем лагерем!"
                    show sh normal pioneer at cright   with dspr
                    sh "И что мы покажем?"
                    show el normal pioneer at cleft   with dspr
                    el "Тут ты прав."
                    "Они оба расстроенно утыкаются в тарелки."
                "Отступить":
                    window show
                    me "Ну ладно..."
                    "Вы все утыкаетесь в тарелки и молча ужинаете."
            hide el 
            hide sh 
            with dissolve
            window hide

            with fade2
        "Молча доесть ужин":
            window show
            "Ты решаешь не развивать разговор дальше, и вы утыкаетесь в тарелки."

    stop ambience fadeout 2
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg int_dining_hall_sunset 
    with dissolve2

    play ambience ambience_dining_hall_empty fadein 2

    window show
    "Ужин заканчивается, и пионеры начинают расходиться."
    if ds_framed_dv:
        show el surprise pioneer at left
        show sh surprise pioneer at right
        show dv rage pioneer at center
        with dspr
        dv "СЕМЁН! ТЫ МНЕ НИЧЕГО ОБЪЯСНИТЬ НЕ ХОЧЕШЬ?!"
        "От крика Алисы посуда на столе дребезжит."
        me "Ты чего, Алиса?"
        dv "Какие нахрен конфеты я украла?! Я впервые вообще о них слышу!"
        play sound ds_sfx_mot
        res "Да, ты же сказал, что это якобы она украла."
        dv "Ну. Я жду. Объяснений. Немедленно!"
        window hide
        menu:
            "Сказать, что это розыгрыш":
                window show
                me "Разыграть тебя решил! Во!"
                dv "КАКОЙ РОЗЫГРЫШ?! ТЫ ТАМ ВООБЩЕ С ДУБУ РУХНУЛ?!"
                dv "Мне и так хватает проблем с вожатой!"
                dv "Быстро пошёл и сказал вожатой, что это ты!"
            "Cказать про Ульяну":
                window show
                me "Да я Ульяну прикрывал..."
                show dv surprise pioneer at center
                with dspr
                play sound ds_sfx_psy
                aut "Она в ступоре. Оправдаться ей самой - подставить её подругу. И наоборот. Она не знает, как поступить."
            "Заявить о мести":
                window show
                me "Это месть тебе за твоё отношение ко мне!"
                if ds_dv_invite:
                    dv "За то, что я хотела с тобой вечер провести?!"
                else:
                    dv "И за что же?! За то, что я тебя в шутку по спине шлёпнула? Ты прям не пережил такого глубокого оскорбления своего величества?!"
        show mt rage pioneer at cright
        show dv angry pioneer at cleft
        with dspr
        mt "Куда убежала, Двачевская?! Мы ещё не разобрались с тобой насчёт конфет!"
        dv "Вот! Сейчас вам ваш любимчик всё расскажет!"
        window hide
        menu:
            "Сказать про Ульяну":
                window show
                me "Ну да, я оговорил Алису, чтобы прикрыть Ульяну."
                me "Это она украла конфеты."
                mt "Да ты просто гений, Семён! Прикрывая Ульяну, свалить вину на её подругу!"
                show mt normal pioneer at cright
                with dspr
                mt "А если серьёзно - извини, Алиса."
                show mt rage pioneer at cleft
                with dspr
                mt "Я же не думала, что Семён решит не по-пионерски оклеветать товарища!"
                dv "Да я тоже от него такого не ожидала!"
                if ds_dv_invite:
                    dv "Как ты понимаешь - о планах на вечер можешь забыть!"
                    $ ds_dv_invite = False
            "Взять вину на себя":
                window show
                me "Ну, украл конфеты, подумаешь. И сказал, что это Алиса."
                mt "Подумаешь?! Это не по-пионерски! Так нельзя делать!"
                mt "Всё, больше не хочу с тобой разговаривать! Мне противно!"
                show mt normal pioneer at cright
                with dspr
                mt "Извини, Алиса."
                show mt rage pioneer at cleft
                with dspr
                mt "Я же не думала, что Семён решит не по-пионерски оклеветать товарища!"
                dv "Да я тоже от него такого не ожидала!"
                if ds_dv_invite:
                    dv "Как ты понимаешь - о планах на вечер можешь забыть!"
                    $ ds_dv_invite = False
            "Настаивать на вине Алисы":
                window show
                me "Это Алиса. Теперь она пытается меня запугать за правду!"
                show dv rage pioneer at cleft
                with dspr
                dv "ЗА КАКУЮ ПРАВДУ?! ХВАТИТ ВРАТЬ УЖЕ!"
                mt "Алиса, уж если попалась - хотя бы признай."
                dv "Да не делала я ничего! Отстаньте от меня!"
                hide dv with dissolve
                $ ds_dv_invite = False
                $ ds_dance_dv = False
                show mt surprise pioneer at center
                with dspr
                mt "Ты уверен, Семён, что это она? Алиса, конечно, немало нарушает, но так бурно раньше не реагировала..."
                mt "Даже больше скажу - она свою вину всегда признавала, тут надо отдать ей должное. А тут вот так... Это точно она?"
                me "Ну... да..."
                show mt angry pioneer at center
                with dspr
                mt "Если узнаю, что обманул - будешь на линейке, при всех, на коленях извиняться перед ней!"
                hide mt with dissolve
    show el normal pioneer at cleft 
    show sh normal pioneer at cright 
    with dissolve
    window hide
    menu:
        "Спросить про одежду":
            window show
            me "А вы как на бал оденетесь?"
            el "А нам особо нечего – так и пойдём."
            "Он показывает на свою пионерскую форму."
            play sound ds_sfx_int
            con "Кажется, их совсем не волнует внешний вид."
            if not ds_mi_costume:
                play sound ds_sfx_psy
                vol "Что же ты тогда беспокоишься!"
                vol "В зимней одежде всё равно идти не вариант, так что пойдёшь как есть."
            else:
                con "А у тебя есть костюм, да не простой, а от Мику!"
            me "И во сколько начало?"
            el "После девяти."

            stop ambience fadeout 2

            me "Ясно."
            window hide
        "Спросить про робота":
            window show
            me "Так как, вы роботом заниматься будете?"
            show el upset pioneer at cleft
            with dspr
            el "Эх, если бы... явка на танцы обязательна."
            me "Вот как..."
            me "И во сколько начало?"
            el "После девяти."

            stop ambience fadeout 2

            me "Ясно."
            window hide
        "Спросить про время":
            window show
            me "И во сколько начало?"
            el "После девяти."

            stop ambience fadeout 2

            me "Ясно."
            window hide
        "Молча уйти":
            pass
    $ sunset_time()

    $ persistent.sprite_time = "sunset"
    scene bg ext_dining_hall_away_sunset 
    with dissolve

    play ambience ambience_camp_center_evening

    window show
    "Ты выходишь из столовой и полной грудью вдыхаешь вечерний воздух."
    play sound ds_sfx_psy
    ine "Тебе сразу вспоминаются те редкие дискотеки, на которых приходилось бывать ещё в школе."
    ine "Неуверенность, стеснение и даже страх…"
    ine "Ты не умел танцевать, не знал, как правильно реагировать, если пригласят тебя, а сам кого-то приглашать не осмеливался."
    ine "В общем, чувствовал себя там крайне неуютно."
    ine "Тем неприятнее было тебе смотреть на чужое веселье."
    ine "Нет, это не зависть.{w} Скорее удивление от того, что люди могут получать удовольствие от чего-то совершенно мне непонятного."
    play sound ds_sfx_psy
    "До начала дискотеки ещё порядком времени, так что ты идёшь прогуляться."
    window hide
    jump ds_day3_bus

label ds_day3_no_dinner:
    $ persistent.sprite_time = 'day'
    scene bg ext_square_day
    with dissolve
    th "Ну и ладно, без ужина обойдусь!"
    play sound ds_sfx_psy
    vol "Ты настолько зол, что даже не разбираешь, куда идёшь. Просто идёшь."
    jump ds_day3_bus
    
label ds_day3_bus:
    $ persistent.sprite_time = "sunset"
    scene bg ds_ext_bus_sunset 
    with dissolve
    $ sunset_time()

    play music music_list["no_tresspassing"] fadein 3

    window show
    play sound ds_sfx_psy
    ine "Перед тобой стоит автобус.{w} Точно такой же, как и в первый день."
    play sound ds_sfx_mot
    com "Ты застыл в ступоре."
    me "Как, что, как, почему?.."
    ine "Мгновенно всплывают все теории о попадании в этот лагерь."
    play sound ds_sfx_fys
    hfl "Тут же, как ножом, режет мысль: за эти несколько дней ты слишком привык к местной жизни и уже стал забывать – всё, что здесь происходит, ой как далеко от нормального!"
    "Несколько минут ты просто стоял и смотрел на Икарус, затем пару раз хлопаешь себя по щекам, чтобы убедиться, что это не мираж, но автобус никуда не исчезает."
    window hide
    menu:
        "Забежать в автобус":
            window show
            th "Раз он здесь, то мне пора домой!"
            me "{i}Сайонара{/i}, пионеры!"
        "Отступить":
            window show
            play sound ds_sfx_psy
            vol "Что-то тебя держит. Ты не можешь уйти."
    "И ты бросаешься к двери…"
    window hide

    play sound sfx_energy_door_bus

    with vpunch

    with flash

    window show
    "И ты оказываешься за земле."
    play sound ds_sfx_fys
    pat "С больным носом."
    play sound ds_sfx_int
    lgc "Что же произошло?"
    th "Видимо, во что-то врезался..."
    play sound ds_sfx_mot
    per_toc "На ощупь автобус более чем реальный."
    "Ты пытаешься просунуть руку в дверь…{w} Но там словно стоит невидимая преграда."
    play sound ds_sfx_fys
    hfl "И тут меня обуял практически животный страх."
    hfl "Страх всего – лагеря, его обитателей, этого автобуса."
    th "Как я вообще сюда попал?"
    th "Что это за чёртов Икарус, в который не войти?{w} Почему всё это происходит именно со мной?!"

    play sound sfx_wind_gust

    "Вдруг дует настолько сильный ветер, что кажется, собьёт с ног."
    "Ты отворачиваешься и увидел под колесом автобуса маленький клочок бумаги."
    window hide
    menu:
        "Подобрать":
            window show
            ine "Там написано несколько слов."
            window hide

            scene white 
            with dissolve

            show urhere1 "Ты здесь не просто так" :
                xpos -0.5
                ypos 0.3
                linear 4.0 xpos 1.5
                repeat

            show urhere2 "Ты здесь не просто так" :
                xpos -0.5
                ypos 0.1
                linear 3.0 xpos 1.5
                repeat

            show urhere3 "Ты здесь не просто так" :
                xpos -0.5
                ypos 0.7
                linear 5.0 xpos 1.5
                repeat

            show urhere4 "Ты здесь не просто так" :
                xpos -0.5
                ypos 0.5
                linear 4.0 xpos 1.5
                repeat

            show urhere5 "Ты здесь не просто так" :
                xpos -0.5
                ypos 0.8
                linear 3.0 xpos 1.5
                repeat

            show urhere6 "Ты здесь не просто так" :
                ypos 0.1
                xpos 1.0
                linear 4.0 xpos -1.0
                repeat

            show urhere7 "Ты здесь не просто так" :
                ypos 0.3
                xpos 1.0
                linear 3.0 xpos -1.0
                repeat

            show urhere8 "Ты здесь не просто так" :
                ypos 0.8
                xpos 1.0
                linear 5.0 xpos -1.0
                repeat

            show urhere9 "Ты здесь не просто так" :
                ypos 0.6
                xpos 1.0
                linear 4.0 xpos -1.0
                repeat

            show urhere10 "Ты здесь не просто так" :
                ypos 0.4
                xpos 1.0
                linear 3.5 xpos -1.0
                repeat

            $ renpy.pause(5.0)

            window show
            "{i}Ты здесь не просто так{/i}."
            if skillcheck('visual_calculus', lvl_easy, passive=True):
                play sound ds_sfx_int
                vic "Это твой почерк!"
                th "Я послал себе записку из будущего! Точно!"
                th "Нет.{w} Или из прошлого…"
                th "Чёрт! Всё равно не понимаю!"
                play sound ds_sfx_int
                lgc "Но как бы там ни было, почерк явно твой."
                lgc "Конечно, подделать его – не большая проблема, но ты полностью уверен, что эту записку написал сам."
            else:
                play sound ds_sfx_int
                vic "Корявый почерк кажется знакомым. Но чей он - непонятно."
            window hide
        "Отложить":
            window show

    $ persistent.sprite_time = "sunset"
    scene bg ds_ext_bus_sunset
    with dissolve

    window show
    "Покрутив листок в руках, ты откладываешь его."
    window hide

    with fade

    menu:
        "Зайти в автобус снова":
            window show
            "Ты пытаешься зайти в автобус."
            play sound sfx_energy_door_bus
            "Но невидимый барьер по-прежнему не пускал меня внутрь."
            "Ты обходишь Икарус со всех сторон, стучишь по колёсам, заглядываешь внутрь через окно."
            play sound ds_sfx_int
            vic "Всё кажется абсолютно нормальным.{w} Но таковым не является."
        "Ударить по автобусу":
            window show
            play sound sfx_bus_window_hit
            "Ты подбираешь камень и бросаешь его в окно."
            "Увесистый камень с глухим стуком отскочил от стекла, не нанеся видимых повреждений."
            play sound ds_sfx_mot
            per_eye "Никакого эффекта, даже царапинки!"
        "Ничего не делать":
            window show
    scene bg ds_ext_camp_entrance_sunset
    with dissolve
    "Ты садишься на бордюр и обессиленно вздыхаешь."
    play sound ds_sfx_psy
    ine "Если вдуматься, то листок тебе намекает на что-то…"
    play sound ds_sfx_psy
    vol "Обернись!"

    scene bg ext_no_bus_sunset
    with dissolve

    window show
    "Автобус исчез…{w} Исчез так же внезапно, как и появился."
    play sound ds_sfx_mot
    com "Победный клич застревает в горле."
    th "ЧТО ЗА ЧЕРТОВЩИНА?!"
    sb "И снова здравствуй, Семён."
    th "Что вам надо от меня?"
    sb "Обернись."

    scene bg ds_camp_entrance_sunset
    show sub lim at center
    with dissolve

    me "Ты кто?!"
    sb "Твоё подсознание."
    show sub trs at center with dspr
    show sub arb at center with dspr
    sb "Видишь?"
    me "Моё подсознание... женского пола?"
    play sound ds_sfx_psy
    sb "Нет, конечно. Этот образ - порождение твоего мозга."
    sb "Я - это ты!"
    me "Почему ты продолжаешь меня мучать?"
    show sub trs at center with dspr
    show sub lim at center with dspr
    sb "Это ты себя мучаешь, Семён. Это ты не можешь выкинуть из головы отравляющие твою жизнь воспоминания."
    me "Твой образ как-то связан с воспоминаниями?!"
    sb "Безусловно."
    play sound ds_sfx_int
    vic "Эта девушка по внешности тебе немного напоминает Лену..."
    show sub trs at center with dspr
    show sub arb at center with dspr
    vic "...а теперь Алису."
    me "Да что такое происходит?! Почему я тут?!"
    sb "Сейчас ты спишь. Надеялся найти забвение."
    me "То есть, я проснусь... у себя?"
    show sub trs at center with dspr
    show sub lim at center with dspr
    sb "Кто знает, кто знает..."
    me "Почему вы раньше не показывались мне так?!"
    show sub trs at center with dspr
    show sub arb at center with dspr
    sb "Многие тайны подсознания неведомы человеку."
    sb "Сегодня мы такие... завтра будем другими."
    sb "Всё от тебя зависит - о чём больше всего думаешь, то и вылезает."
    show sub trs at center with dspr
    show sub lim at center with dspr
    sb "Тебе пора, Семён. Пора выбрать дальнейший путь."
    show sub trs at center with dspr
    show sub arb at center with dspr
    sb "Да. Тебе надо выяснить, почему же ты попал в лагерь."
    show sub trs at center with dspr
    show sub lim at center with dspr
    sb "Или же забить и наслаждаться жизнью. Двигаться вперёд, так сказать."
    show sub trs at center with dspr
    show sub arb at center with dspr
    sb "Но ты должен найти ответы. Кто знает, может это ловушка?"
    show sub trs at center with dspr
    show sub lim at center with dspr
    sb "Ну какая ловушка? Скорее {i}шанс{/i}. На счастье."
    show sub trs at center with dspr
    show sub arb at center with dspr
    sb "Никто не говорит, что это всё обязательно ловушка. Но разве тебе не интересно знать, как ты сюда попал?"
    show sub trs at center with dspr
    show sub lim at center with dspr
    sb "Короче. Решать тебе. Главное - не забывай..."
    hide sub with dissolve
    me "О ком?!"
    "Тишина тебе ответ."
    $ persistent.sprite_time = 'night'
    $ night_time()
    stop music fadeout 2
    scene black with dissolve
    scene bg ext_square_night_party 
    show unblink
    "Ты просыпаешься. Уже ночь."
    play sound ds_sfx_mot
    res "Пока ты спал, площадь уже подготовили к дискотеке!"
    th "Что это было?"
    play sound ds_sfx_int
    lgc "Похоже, ты уснул на скамейке. И тебе приснился такой вот сон."
    play sound ds_sfx_psy
    ine "И лучше тебе бы прислушаться к ней."

    th "Итак, ладно, мне надо на дискотеку..."
    if ds_dv_invite:
        play sound ds_sfx_psy
        vol "Но тебя ещё и Алиса пригласила... И куда пойдём?"
        if ds_to_help_un:
            play sound ds_sfx_psy
            sug "А ещё же Лена... ей надо помочь в медпункте..."
        th "И что вы мне прикажете делать?"
    window hide
    menu:
        "Пойти на дискотеку":
            window show
            th "Ладно, схожу на дискотеку..."
            if ds_dv_invite:
                $ ds_lp['dv'] -= 3
                $ ds_dumped_dv = True
        "Пойти к Алисе" if ds_dv_invite:
            window show
            play sound ds_sfx_psy
            emp "Ну нет, подводить Алису нехорошо. Она явно ждёт тебя."
            th "Вот и пойду к ней, значит. Вероятно, это будет интереснее дискотеки!"
            play sound ds_sfx_fys
            hfl "Только будь начеку."
            if ds_promise_un:
                $ ds_lp['un'] -= 3
            if ds_to_help_un:
                $ ds_lp['un'] -= 2
                $ ds_dumped_un = True
            if ds_promise_sl:
                $ ds_lp['sl'] -= 2
                $ day3_dv_evening = 1

            $ persistent.sprite_time = "night"
            scene bg ext_stage_big_night 
            with dissolve

            play ambience ambience_camp_center_evening fadein 2

            window show
            "Через пару минут ты подходишь к сцене."
            play sound ds_sfx_fys
            hfl "Может быть, зря согласился?"
            hfl "Ведь общение с Двачевской уже само по себе несёт опасность…"
            play sound ds_sfx_psy
            vol "С другой стороны, и на дискотеку идти совсем не хочется."
            if not skillcheck('authority', lvl_medium, passive=True):
                play sound ds_sfx_psy
                aut "{result}Что ты можешь там продемонстрировать?{w} Опозорюсь, и всё…"
            th "Нет! Лучше уж послушаю, как Алиса играет на гитаре."
            window hide

            stop ambience fadeout 2

            $ persistent.sprite_time = "night"
            scene bg ext_stage_normal_night 
            with dissolve

            play music music_list["glimmering_coals"] fadein 3

            window show
            "Подойдя ближе, ты видишь, что кто-то сидит на краю сцены, свесив ноги вниз."
            play sound ds_sfx_int
            lgc "И кто же это может быть?"
            jump ds_day3_evening_dv
        "Уйти прочь":
            window show
            th "Да пошло оно всё к чёрту!"
            "С этими словами ты направляешься к своему домику."
            if ds_dv_invite or ds_dv_dance:
                $ ds_lp['dv'] -= 3
                $ ds_dumped_dv = True
            if ds_promise_un:
                $ ds_lp['un'] -= 3
            if ds_to_help_un:
                $ ds_lp['un'] -= 2
                $ ds_dumped_un = True
            if ds_promise_sl:
                $ ds_lp['sl'] -= 2
            $ ds_karma -= 5
            jump ds_day3_evening_none
    jump ds_day3_disco

label ds_day3_disco:
    play ambience ambience_camp_center_evening fadein 2
    window show
    "Около памятника установили колонки и что-то вроде диджейского пульта, а на деревьях развесили гирлянды."
    play sound ds_sfx_int
    con "Такая типичная колхозная дискотека."
    play sound ds_sfx_psy
    vol "Итак, надо решить, с кем ты будешь танцевать. И будешь ли вообще."
    if ds_el_mz_relation:
        play sound ds_sfx_mot
        per_eye "Женя сразу отпадает, как и Электроник - они уже вместе."
    window hide
    menu:
        "Потанцевать с Алисой" if ds_dance_dv:
            window show
            jump ds_day3_dance_dv
        "Потанцевать с Леной":
            window show
            "Ты подходишь к Лене."
            show un surprise dress at center
            with dspr
            me "Потанцуем?"
            un "Ну... давай..."
            jump ds_day3_dance_un
        "{check=volition:10}Потанцевать со Славей":
            if skillcheck('volition', lvl_medium):
                window show
                play sound ds_sfx_psy
                vol "{result}Славя будет только рада тебе!"
                "Ты подходишь к Славе."
                show sl normal dress at center
                with dspr
                me "Потанцуем?"
                show sl smile dress at center
                with dspr
                sl "Да, давай, конечно, Семён!"
                $ ds_lp['sl'] += 1
                jump ds_day3_dance_sl
            else:
                window show
                play sound ds_sfx_psy
                vol "{result}Ты хотел бы подойти к Славе, но от страха тебя не слушаются ноги. Не в этот раз, извини."
        "Пригласить Мику":
            window show
            jump ds_day3_dance_mi
        "Подойти к Ульяне":
            window show
            jump ds_day3_evening_us
        "{check=volition:11}Пригласить Ольгу Дмитриевну":
            if skillcheck('volition', lvl_up_medium):
                window show
                play sound ds_sfx_psy
                vol "{result}Всё будет нормально. Ольга Дмитриевна тебе не откажет."
                "Ты подходишь к Ольге Дмитриевне."
                show mt smile dress at center
                with dissolve
                me "Ольга Дмитриевна... возможно, вам моё предложение покажется странным... но, может, вы станцуете со мной?"
                mt "Ничего странного, Семён! Давай, конечно!"
                jump ds_day3_dance_mt
            else:
                window show
                play sound ds_sfx_psy
                vol "{result}Глупая идея. Ты - пионер, она - вожатая. Вы несовместимы."
        "Пойти к Жене" if not ds_el_mz_relation:
            window show
            jump ds_day3_evening_mz
        "Пригласить Яну" if ds_met['ya'] > 0:
            window show
            jump ds_day3_dance_ya
        "Пригласить Электроника" if not ds_el_mz_relation:
            window show
            jump ds_day3_evening_el
        "Посидеть в сторонке":
            window show
    "Пионеров собралось довольно много, но никого из знакомых ты не видишь, поэтому садишься на лавочку и принимаешься ждать."
    play sound ds_sfx_psy
    vol "Может быть, тебе удастся просто посидеть и мило пообщаться с кем-нибудь."
    if (ds_lp['sl'] >= 10) and ((ds_whom_helped == 'sl') or ds_helped_sl_lib):
        show sl normal dress at center   with dissolve
        sl "Привет!"
        "Славя."
        me "Привет."
        "Она присаживается рядом."
        sl "Как тебе вечер?"
        me "Нормально."
        sl "Что ты такой грустный?"
        me "Да ничего…"
        sl "Может, станцуем? Вот увидишь, веселее станет!"
        window hide
        menu:
            "Потанцевать":
                window show
                me "Наверное…"
                show sl smile dress at center   with dspr
                sl "Тогда чего ты сидишь, идём!"
                jump ds_day3_dance_sl
            "Отказаться":
                window show
                me "Да не, чего-то не хочется пока..."
                sl "Ну ладно, как надумаешь, подходи!"
                show sl smile dress at center   with dspr
                sl "Только не забудь! Оставь один танец для меня!"
    "Она смеётся и бежит к музыкальной аппаратуре, за которой сидит Мику."
    play sound ds_sfx_int
    lgc "Похоже, просто отсидеться не получится."
    if ds_promise_un:
        show un normal dress at center   with dissolve
        un "Привет."
        "Ко мне подошла Лена."
        me "Ой, привет, и ты тут…"
        th "Хотя чего удивительного?"
        un "Да."
        window hide
        menu:
            "{check=rhetoric:12}Подбодрить":
                if skillcheck('rhetoric', lvl_challenging):
                    window show
                    play sound ds_sfx_int
                    rhe "{result}Лучше всего похвали её платье, и дальше не лезь."
                    me "Прекрасно выглядишь в этом платье!"
                    show un shy dress at center   with dspr
                    un "Cпасибо…"
                    "Лена покраснела и опустила глаза."
                    $ ds_lp['un'] += 1
                    $ ds_skill_points['rhetoric'] += 1
                    play sound ds_sfx_psy
                    emp "Ей твой, казалось бы, простенький комплимент, понравился."
                else:
                    window show
                    play sound ds_sfx_int
                    rhe "{result}Ты решаешь сострить."
                    me "Ясно…{w} Зажжёшь сегодняшний вечер?"
                    rhe "Острота прозвучала неумело."
                    $ ds_skill_points['rhetoric'] += 1
                    show un shy dress at center   with dspr
                    un "…"
                    "Лена покраснела и опустила глаза."
                    me "Ладно, может, и правда не стоит, а то все сгорим тут…"
                    un "Ладно, тогда я…"
                    me "Ага…"
            "Промолчать":
                window show
            "Потребовать отстать":
                window show
                me "Ты мне мешаешь! Уйди пожалуйста!"
                show un sad dress at center
                with dspr
                play sound ds_sfx_psy
                emp "Поздравляю, ты её обидел!"
                $ ds_lp['un'] -= 2
                un "Я-то уйду, но..."
        show un serious dress at center   with dissolve
        un "Может, пойдём?"
        if skillcheck('reaction_speed', lvl_medium, passive=True):
            play sound ds_sfx_mot
            res "{result}Она напоминает про медпункт."
            un "Хотя, если ты хочешь потанцевать..."
        else:
            me "Куда?"
            "Ты был так увлечён своими мыслями, что не понял, о чём она."
            un "В медпункт.{w} Если, конечно, ты хочешь остаться и потанцевать…"
            "Хотя вряд ли она действительно собиралась танцевать – весь вечер Лена стояла в сторонке."
        window hide
        menu:
            "Предложить потанцевать":
                window show
                me "Да, я бы не отказался с тобой потанцевать!"
                show un shy dress at center
                with dspr
                un "Ой... ну ладно... Как скажешь."
                jump ds_day3_dance_un
            "Пойти в медпункт":
                window show
                me "Нет, пожалуй, воздержусь!{w} Пойдём."
                th "Ну хоть не придётся здесь стоять как бедный родственник!"
                play sound ds_sfx_psy
                vol "Действительно, сидеть в углу и всеми силами стараться не отсвечивать не очень комфортно."
                if not skillcheck('savoir_faire', lvl_medium, passive=True):
                    play sound ds_sfx_mot
                    svf "{result}Даже слон в посудной лавке может быть куда более ловким, чем ты на танцполе!"

                stop music fadeout 3

                vol "К тому же никакого желания пускаться в пляс у тебя не было."
                jump ds_day3_un_medic
            "Отказать":
                window show
                me "Я никуда сейчас не пойду."
                show un sad dress at center
                with dspr
                un "Ну ладно... но я буду ждать тебя у медпункта..."
                $ ds_lp['un'] -= 1
    hide un  with dissolve
    "Она уходит."
    window hide

    with fade2

    window show
    if ds_dance_dv and not ds_mi_accept_dv:
        show dv angry dress at center
        with dissolve
        dv "Ну и что это за дела?! Почему это Мику вообще не в курсе наших планов?!"
        dv "Кто там обещал договориться и не договорился?!"
        $ ds_lp['dv'] -= 1
        me "И тебе добрый вечер, Алиса."
        dv "Короче, ты предложил - ты и иди сейчас к Мику и прямо СЕЙЧАС договаривайся!"
        window hide
        menu:
            "Согласиться":
                window show
                me "Ладно, как скажешь."
                show mi normal dress at center
                show dv angry dress at left
                with dspr
                mi "Ой, приветики, Семён-кун! А не подскажешь, про что такое Алиса говорила? Какая-то гитара, все дела... Я не понимаю..."
                me "Да это мы с ней задумали добавить живой музыки."
                show mi smile dress at center
                with dspr
                mi "Ой, как классненько! Давайте, конечно!"
                $ ds_mi_accept_dv = True
                dv "Спасибо."
                hide dv
                hide mi
                with dissolve
                play sound ds_sfx_psy
                emp "Она всё равно очень недовольна тем, что ты не выполнил обещание."
                th "Ну и ладно."
            "Отказаться":
                window show
                me "Никуда я не пойду! Тебе надо - ты и проси!"
                show dv rage dress at center
                with dspr
                dv "Нет, это {i}тебе{/i} надо было, придурок!"
                play sound ds_sfx_psy
                sug "Она права - инициатива исходила от тебя."
                show dv angry dress at center
                with dspr
                dv "Ладно, неважно. Счастливо оставаться!"
                "И Алиса уходит. Точнее, убегает."
                $ ds_lp['dv'] -= 2
    "Весь лагерь собрался на площади."
    "Пионеры стоят большими группами, о чём-то разговаривают, шутят и смеются."
    "Возле диджейского пульта Ульянка громко спорит с Ольгой Дмитриевной насчёт музыкального репертуара на сегодняшний вечер."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_square_night_party 
    with dissolve

    play music music_list["lightness"] fadein 2

    window show
    "И вот, момент настал.{w} Пластинка закрутилась."
    play sound ds_sfx_int
    enc "Что это была за группа и песня, ты не знаешь, но термин «классика советской эстрады» подходит для них как нельзя лучше."
    "Пионеры и пионерки некоторое время просто стоят, словно не слыша музыки."
    play sound ds_sfx_psy
    vol "Всегда трудно сделать первый шаг.{w} Особенно, когда уверен, что, кроме тебя, никто и не собирается…"
    window hide
    menu:
        "{check=volition:14}Зажечь танцпол":
            if skillcheck('volition', lvl_legendary):
                window show
                vol "{result}Но ты, по-видимому, первый преодолеваешь страх и выступаешь в середину площади."
                me "Давайте зажжём!"
                "И ты начинаешь танцевать."
                $ ds_skill_points['volition'] += 1
                $ ds_lp['mt'] += 1
                "После тебя первой оживляется Ульяна."
            else:
                window show
                vol "{result}Пока ты переминаешься с ноги на ногу, Ульяна перехватывает инициативу."
        "Не высовываться":
            window show
            vol "Но Ульянка, похоже, не знает этой простой истины."
    "Она выбегает на середину площади и кричит."
    us "Чего стоим?!"
    "И начинает нелепо кривляться."
    play sound ds_sfx_mot
    svf "Именно «кривляться».{w} Другое слово сложно подобрать."
    play sound ds_sfx_mot
    com "Это выглядит настолько глупо и забавно, что ты не удержался и начинаешь смеяться."
    "Она замечает."
    show us laugh dress far at center   with dissolve   
    us "Эй, Семён!"
    window hide
    menu:
        "Подойти":
            window show
            me "Чего тебе?"
            show us laugh dress at center
            with dspr
            us "А ничего! Давай танцуй! И все вы давайте танцуйте!"
        "Игнорировать":
            window show
            "Я сделал вид, что не слышу."
            show us surp1 dress far at center   with dspr
            $ ds_lp['us'] -= 1
            us "Не притворяйся! Иди-ка сюда."
            window hide
            menu:
                "Всё-таки подойти":
                    window show
                    me "Чего тебе?"
                    show us laugh dress at center
                    with dspr
                    us "А ничего! Давай танцуй! И все вы давайте танцуйте!"
                "Продолжать игнорировать":
                    window show
                    "Ты продолжаешь игнорировать её."
                    $ ds_lp['us'] -= 1
    hide us  with dissolve
    "Пионеры потихоньку понимают, что от них требуется на этом празднике жизни, и пускаются в пляс."
    play sound ds_sfx_int
    con "Выглядит в высшей степени глупо."
    play sound ds_sfx_mot
    svf "Трясти руками и ногами под давно забытые шлягеры?{w} Увольте!"
    if ds_lp['sl'] >= 10:
        sl "Семён, чего сидишь?{w} Потанцевать не хочешь?"
        show sl normal dress at center   with dissolve
        "Ты был так увлечён своими мыслями, что не заметил Славю."
        window hide
        menu:
            "Cогласиться":
                window show
                me "Ладно, может, чуть-чуть…"
                sl "Вот и правильно!"
                $ ds_lp['sl'] += 1
                jump ds_day3_dance_sl
            "Отказаться":
                window show
                me "Да что-то не хочется…"
                show sl smile dress at center   with dspr
                sl "Точно?"
                "Она улыбается."
                me "Попозже, может быть."
    th "Чёрт! Что я вообще здесь делаю?!"
    jump ds_day3_evening_none

label ds_day3_evening_dv:
    show dv normal pioneer at center   with dissolve
    dv "Значит, всё-таки пришёл!"
    "Алиса откладывает гитару в сторону и спрыгивает на землю."
    if skillcheck('perception', lvl_easy, passive=True):
        play sound ds_sfx_mot
        per_eye "{result}На её лице даже на долю секунды мелькает радость."
        play sound ds_sfx_int
        lgc "Впрочем, оно и понятно – играть для кого-то интереснее, чем репетировать в одиночестве."
    me "Как видишь…"
    dv "И что будем делать?"
    me "Как это что?.."
    show dv smile pioneer at center   with dspr
    dv "Вот я тебя и спрашиваю."
    me "Ну... ты же хотела..."
    play sound ds_sfx_fys
    hfl "Возможно, всё это – лишь очередной её розыгрыш и не стоит ждать никаких песен под гитару."
    if skillcheck('authority', lvl_easy, passive=True):
        play sound ds_sfx_psy
        aut "Покажи, что тебе не до шуток. Изобрази, будто уходишь."
    window hide
    menu:
        "Напомнить":
            window show
            me "Да как бы на гитаре играть."
            show dv laugh pioneer at center
            with dspr
            dv "Да что ты говоришь!"
            show dv grin pioneer at center
            with dspr
            dv "И вообще, я проверяла тебя!"
            if skillcheck('drama', lvl_medium, passive=True):
                play sound ds_sfx_psy
                dra "{result}Врёт. Она просто боялась проявить инициативу, и передала её вам, мессир. Вы справились."
        "Изобразить уход" if ds_last_skillcheck.result:
            window show
            me "Я иду спать, счастливо!"
            hide dv  with dissolve
            "Ты разворачиваешься и нарочито медленно машешь ей рукой."
            $ ds_skill_points['authority'] += 1
            dv "Эй!"
            "Алиса крепко хватает тебя за рукав."
            show dv shy pioneer at center   with dissolve
            me "Что?"
            dv "Не хочешь послушать?.."
            play sound ds_sfx_psy
            aut "Продолжай давить на неё."
            window hide
            menu:
                "Согласиться":
                    window show
                    me "Конечно, хочу! Мы как бы для этого тут и собрались!"
                "Подцепить её":
                    window show
                    me "Что слушать? Ты же сама не знаешь, что делать собираешься."
                    show dv angry pioneer  with dspr
                    dv "Всё я знаю!"
        "Уйти":
            window show
            me "Ну раз не знаешь - пока!"
            hide dv  with dissolve
            "Ты разворачиваешься и уходишь."
            dv "Эй!"
            "Алиса крепко хватает тебя за рукав."
            show dv shy pioneer at center   with dissolve
            me "Что?"
            dv "Не хочешь послушать?.."
            me "Я для этого сюда и пришёл вообще-то!"
        "{check=half_light:11}Изнасиловать Алису":
            if skillcheck('half_light', lvl_up_medium):
                window show
                play sound ds_sfx_fys
                show dv scared pioneer close at center
                with dspr
                hfl "{result}Ты резко набрасываешься на Алису так, что она ничего не успевает понять."
                me "Молчи, а то убью."
                hfl "Она в ступоре и не решается дать тебе отпор."
                play sound ds_sfx_fys
                ins "А твой инструмент в штанах уже готов к действию!"
                "Ты стягиваешь с себя одежду, задираешь ей юбку и приступаешь..."
                scene black with dissolve2
                jump ds_end_dv_rape
            else:
                window show
                play sound ds_sfx_fys
                hfl "{result}Ты подходишь к ней и прижимаешь её к сцене."
                show dv scared pioneer close at center
                with dspr
                dv "НА ПОМОЩЬ!!!"
                me "Молчи!"
                play sound ds_sfx_fys
                ins "А твой инструмент в штанах уже готов к действию!"
                "Ты стягиваешь с себя одежду, задираешь ей юбку и приступаешь..."
                show mt scared dress far at right
                show dv cry pioneer close at center
                with dissolve
                mt "ЭТО ЧТО ТУТ ПРОИСХОДИТ?!"
                th "Ольга Дмитриевна... Это конец..."
                mt "Ну, поздравляю тебя, Пёрсунов. Милицию я уже вызвала! Чтоб тебя расстреляли, мерзкое ты создание!"
                "Ты двигаешься в сторону Ольги Дмитриевны..."
                with vpunch
                "Как вдруг тебя Алиса со всей дури бьёт гитарой по голове."
                play sound ds_sfx_fys
                edr "Насмерть."
                scene black with dissolve2
                jump ds_end_dv_rape2
    "Она берёт гитару и несколько раз бьёт чем-то по струнам."
    if skillcheck('encyclopedia', lvl_trivial, passive=True):
        play sound ds_sfx_int
        enc "{result}Медиатором."
    show dv normal pioneer  with dspr
    dv "Иди садись рядом."
    window hide

    scene cg d3_dv_scene_2 
    with dissolve

    window show
    "Ты не стал возражать и через секунду уже сидишь рядом с Алисой."
    dv "Итак, сейчас я покажу тебе, как играется эта песня."
    window hide
    menu:
        "Продолжить молча":
            window show
        "Усомниться":
            window show
            me "Вот так вот сразу?"
            dv "Что сразу?"
            me "Ну, я давно гитару в руках не держал..."
            th "Наверное, ей лучше не знать, что, и когда держал, умения мои были курам на смех."
            dv "Да тут ничего сложного!"
            window hide
            menu:
                "{check=empathy:10}Присмотреться к Алисе":
                    window show
                    "Ты внимательно смотришь на Алису."
                    if skillcheck('empathy', lvl_medium):
                        play sound ds_sfx_psy
                        emp "По-видимому, она просто не умеет выражать эмоции."
                        emp "Или же осознанно пытается их скрыть."
                        emp "На секунду забудет про свой этот странный самоконтроль – и вот перед тобой нормальная, даже местами весёлая и приветливая девочка."
                        emp "А как только вновь включаются самоуверенность и нахальство – здравствуй, хабалка, как любила говорить мама о таких девушках."
                        th "И где же она настоящая?"
                    else:
                        play sound ds_sfx_psy
                        emp "Алиса как Алиса. Наглая и самоуверенная."
                    $ ds_skill_points['empathy'] += 1
                    dv "Эй!"
                    me "Что?"
                    dv "Не спи давай!"
                    me "А, да, извини..."
                    dv "Ну так что, смотришь?"
                    me "Смотрю."
                "Наблюдать за игрой":
                    window show
                    th "Наверное, оно и так..."
    window hide
    menu:
        "Спросить про песню":
            window show
            me "А что за песня?"
            dv "Которую я утром играла, конечно же!"
            me "Ааа… Хорошо, внимательно слушаю."
        "Просто слушать":
            window show
    "Алиса собралась с духом и начинает играть."
    window hide

    with fade

    window show
    dv "Вот так!{w} Всё понял?"
    if not skillcheck('volition', lvl_formidable, passive=True):
        play sound ds_sfx_psy
        vol "{result}Ну, понять ты, может, и понял, но вот повторить вряд ли сможешь."
    me "Как сказать…"
    dv "Ничего, результат приходит с практикой!"
    play sound ds_sfx_mot
    inf "Тут она несомненно права, только вот с практикой у тебя всю жизнь были проблемы."
    $ ds_dv_repeat_play = False
    window hide
    menu:
        "{check=interfacing:15}Согласиться":
            window show
            me "Ладно уж..."
        "Попросить повторить ещё":
            window show
            me "Можешь, пожалуйста, показать ещё?"
            dv "Ладно... смотри внимательно, в третий раз играть не буду!"
            window hide

            with fade

            window show
            $ ds_dv_repeat_play = True
            dv "Теперь сыграешь наконец?"
            window hide
            menu:
                "{check=interfacing:14}Согласиться":
                    window show
                    me "Ладно уж..."
                "Попросить повторить ещё":
                    window show
                    me "Можешь, пожалуйста, показать ещё?"
                    dv "Ты издеваешься надо мной?! Я же сказала: третьего раза не будет! Играй уже!"
                    $ ds_lp['dv'] -= 1
                    window hide
                    menu:
                        "{check=interfacing:14}Согласиться":
                            window show
                            me "Ладно уж..."
                        "Отказаться":
                            window show
                            me "Нет... я как-то не готов."
                            scene bg ext_stage_normal_night 
                            show dv angry pioneer at center
                            with dissolve
                            dv "Да ты издеваешься?! Я, значит, специально для тебя тут поишла, а ты вот так!"
                            dv "Иди отсюда уже!"
                            $ ds_lp['dv'] -= 2
                            hide dv with dissolve
                            "И она быстро уходит куда-то в кусты."
                            th "Ладно, пойдём отсюда..."
                            jump ds_day3_disco
                "Отказаться":
                    window show
                    me "Нет... я как-то не готов."
                    scene bg ext_stage_normal_night 
                    show dv angry pioneer at center
                    with dissolve
                    dv "Да ты издеваешься?! Я, значит, специально для тебя тут поишла, а ты вот так!"
                    dv "Иди отсюда уже!"
                    $ ds_lp['dv'] -= 2
                    hide dv with dissolve
                    "И она быстро уходит куда-то в кусты."
                    th "Ладно, пойдём отсюда..."
                    jump ds_day3_disco
        "Отказаться":
            window show
            me "Нет... я как-то не готов."
            scene bg ext_stage_normal_night 
            show dv angry pioneer at center
            with dissolve
            dv "Да ты издеваешься?! Я, значит, специально для тебя тут поишла, а ты вот так!"
            dv "Иди отсюда уже!"
            $ ds_lp['dv'] -= 2
            hide dv with dissolve
            "И она быстро уходит куда-то в кусты."
            th "Ладно, пойдём отсюда..."
            jump ds_day3_disco
    window hide

    scene cg d3_dv_scene_1 
    with dissolve

    window show
    "Ты берёшь у Алисы гитару..."
    $ ds_played_guitar = True
    window hide
    if skillcheck('interfacing', lvl_heroic, modifiers=[('ds_dv_repeat_play', 1, 'Повторение - мать учения')]):
        jump ds_day3_evening_dv_success
    else:
        jump ds_day3_evening_dv_failure

label ds_day3_evening_dv_success:
    window show
    play sound ds_sfx_mot
    inf "Твои пальцы как будто сами начинают играть то, что надо."
    inf "Ты безошибочно зажимаешь и дёргаешь нужные струны. Музыка словно льётся из пальцев."
    inf "Запечатлев в своей памяти то, как играла Алиса, ты сейчас точно повторяешь её движения. И всё получается!"
    $ ds_skill_points['interfacing'] += 1
    "Алису впечатляет твоё исполнение."
    dv "Ого, быстро справился!"
    me "Спасибо..."
    $ ds_up_morale()
    $ ds_lp['dv'] += 1
    play sound ds_sfx_int
    con "Ты и не то можешь! Впечатли её ещё больше - сыграй что-нибудь своё!"
    window hide
    menu:
        "Продемонстрировать свою песню" if ds_composition_type != 0:
            window show
            me "А ты посмотри вот на это! Вот чего я сочинил!"
            "И ты приступаешь к игре."
            window hide
            with fade

            window show
            me "Вот так-то!"
            play sound ds_sfx_psy
            aut "Алиса молчит - настолько она удивлена."
            me "Алло!"
            scene bg ext_stage_normal_night 
            show dv surprise pioneer at center
            with dissolve
            dv "Ничего себе... а я ещё сомневалась в тебе..."
            $ ds_lp['dv'] += 2
            dv "Так, в общем, ты будешь играть со мной на прощальном концерте! И это не обсуждается!"
            window hide
            menu:
                "Согласиться":
                    window show
                    me "Ну ладно."
                "Отказаться":
                    window show
                    me "Не-а."
                    show dv angry pioneer at center
                    with dspr
                    dv "А я тебя и не спрашиваю! Будешь и всё тут!"
                    $ ds_lp['dv'] -= 1
        "{check=conceptualization:18}Придумать экспромтом" if ds_composition_type == 0:
            if skillcheck('conceptualization', lvl_unimaginable):
                window show
                play sound ds_sfx_int
                con "Перед твоими глазами явственно всплывают нужные ноты. Ты начинаешь играть."
                $ ds_skill_points['conceptualization'] += 1
                window hide
                with fade

                window show
                me "Вот так-то!"
                play sound ds_sfx_psy
                aut "Алиса молчит - настолько она удивлена."
                me "Алло!"
                scene bg ext_stage_normal_night 
                show dv surprise pioneer at center
                with dissolve
                dv "Ничего себе... а я ещё сомневалась в тебе..."
                $ ds_lp['dv'] += 2
                dv "Так, в общем, ты будешь играть со мной на прощальном концерте! И это не обсуждается!"
                window hide
                menu:
                    "Согласиться":
                        window show
                        me "Ну ладно."
                    "Отказаться":
                        window show
                        me "Не-а."
                        show dv angry pioneer at center
                        with dspr
                        dv "А я тебя и не спрашиваю! Будешь и всё тут!"
                        $ ds_lp['dv'] -= 1
        "Отбросить мысль":
            window show
            th "Не, не буду - ещё опозорюсь..."
    dv "А теперь давай сюда!"
    scene cg d3_dv_scene_2 
    with dissolve

    window show
    "Она отбирает у тебя гитару и начинает играть."
    play sound ds_sfx_mot
    inf "Может быть, мастерство Алисы и не дотягивает до настоящих виртуозов, но тем не менее простые вещи, вроде этой, она играет уверенно."
    inf "Наверняка и практиковалась немало..."
    "Наконец, она заканчивает."
    scene bg ext_stage_normal_night 
    show dv normal pioneer at center
    with dissolve
    dv "Ну что, как тебе?"
    window hide
    menu:
        "Похвалить восхищённо":
            window show
            me "Превосходно! Отлично играешь!"
            show dv grin pioneer at center
            with dspr
            dv "А то!"
            $ ds_lp['dv'] += 1
            if skillcheck('empathy', lvl_easy, passive=True):
                play sound ds_sfx_psy
                emp "{result}Ей на самом деле приятна твоя похвала. Но она не подаёт виду - считает это ударом по самолюбию."
        "Похвалить формально":
            window show
            me "Ну, неплохо..."
            dv "Могу и лучше, между прочим. Просто поздно уже!"
        "Раскритиковать":
            window show
            me "Простенько как-то..."
            show dv angry pioneer at center
            with dspr
            dv "Простенько, говоришь?! Я тебе сейчас устрою «простенько»! Беги, пока живой!"
            $ ds_lp['dv'] -= 2
            play sound ds_sfx_fys
            hfl "Беги!"
            window hide
            menu:
                "Побежать":
                    scene bg ext_house_of_mt_night:
                        zoom 1.05 anchor (48,27)
                        ease 0.20 pos (0, 0)
                        ease 0.20 pos (25,25)
                        ease 0.20 pos (0, 0)
                        ease 0.20 pos (-25,25)
                        repeat
                    with dspr
                    window show
                    "Ты сбегаешь от разъярённой Алисы к домику Ольги Дмитриевны."
                    me "Уф..."
                    dv "Ну, погоди!"
                    jump ds_day3_mt_interrogate_2
                "Продолжать задирать":
                    window show
                    me "Что, жжёт критика?"
                    show dv rage pioneer at center
                    with dspr
                    dv "Да какая к чёрту критика?! Вот что тебе не понравилось?! Что?!"
                    dv "Я, значит, тебя пригласила, сыграла для тебя, выложившись по-максимуму, а ты нос воротишь!"
                    with hpunch
                    "С этими словами она даёт тебе пощёчину."
                    $ ds_damage_health()
                    $ ds_lp['dv'] -= 1
                    show dv cry pioneer at center
                    with moveoutleft
                    "И после этого убегает. Кажется, в слезах."
                    th "То есть, я её обидел?"
                    play sound ds_sfx_psy
                    emp "Это ОЧЕНЬ мягко сказано! Просто так обругать её главное увлечение..."
                "Извиниться":
                    window show
                    me "Извини, я не хотел тебя обидеть..."
                    dv "Но обидел! Счастливо оставаться!"
                    hide dv with dissolve
                    th "Ладно, и я пойду..."
    show dv normal pioneer at center
    with dspr
    dv "В общем, спать пора уже!"
    me "И то верно..."
    if skillcheck('suggestion', lvl_medium, passive=True):
        play sound ds_sfx_psy
        sug "{result}Предложи отвести её до домика. Девушкам это нравится."
        window hide
        menu:
            "Предложить проводить до домика":
                window show
                me "А давай я тебя провожу!"
                show dv laugh pioneer at center
                with dspr
                dv "Нет уж, спасибо! На отношения с тобой я не подписывалась..."
                $ ds_skill_points['suggestion'] += 1
                if skillcheck('empathy', lvl_easy, passive=True):
                    play sound ds_sfx_psy
                    emp "{result}Ей стоило некоторых усилий не оговориться «пока что»."
            "Положительно оценить времяпровождение":
                window show
                me "Классно посидели!"
                dv "Ага..."
            "Не предлагать":
                window show
    show dv normal pioneer at center
    with dspr
    dv "В общем, спокойной ночи!"
    show dv shy pioneer far at center
    with dspr
    dv "И да - с тобой интереснее, чем я думала изначально."
    hide dv with dissolve
    th "К чему это она?"
    if skillcheck('empathy', lvl_medium, passive=True):
        play sound ds_sfx_psy
        emp "К тому, что ты её зацепил. Понравился."
        th "Ну ладно..."
    jump ds_day3_mt_interrogate_2

label ds_day3_evening_dv_failure:
    window show
    play sound ds_sfx_mot
    inf "У тебя с трудом получается зажать хотя бы один аккорд – пальцы словно завязываются узлом и отчаянно не хотят принимать нужное положение."
    inf "Когда-то у тебя получалось лучше, но сейчас ты не смог бы сыграть, наверное, и «Кузнечика»."
    dv "Ну?"
    me "Сейчас, подожди..."
    dv "Да уж, рок-герой из тебя точно не выйдет!"
    "Она беззлобно смеётся."
    me "Может, и к лучшему..."
    "Шипишь ты себе под нос, тщетно пытаясь запомнить последовательность струн, которые нужно было зажимать."
    me "Ладно..."
    play sound ds_sfx_int
    con "Гитара начинает издавать дьявольские звуки, больше напоминающие стоны раненого динозавра."
    inf "Пальцы левой руки всё время промахиваются мимо нужных ладов, а правая била совершенно не в ритм."
    window hide
    menu:
        "Сделать хорошую мину":
            window show
            me "Ну, будем считать, что я сыграл нечто прогрессивное."
            dv "Прогрессивное? Ну-ну! Дай сюда!"
        "Сдаться":
            window show
            me "Да не получается у меня!"
            dv "Ладно, давай уже сюда!"
    window hide

    scene cg d3_dv_scene_2 
    with dissolve

    window show
    "Она отбирает у тебя гитару, и в её руках музыкальный инструмент звучит совсем по-иному."
    play sound ds_sfx_psy
    vol "Стыдно тебе за такую криворукость."
    play sound ds_sfx_mot
    inf "Может быть, мастерство Алисы и не дотягивает до настоящих виртуозов, но тем не менее простые вещи, вроде этой, она играет уверенно."
    inf "Наверняка и практиковалась немало..."
    dv "Понял?"
    "Закончив, она вновь протягивает тебе гитару."
    me "Ну..."
    window hide

    scene cg d3_dv_scene_1 
    with dissolve

    window show
    play sound ds_sfx_mot
    inf "Во второй раз получается получше, однако всё равно до уровня Алисы тебе далеко."
    inf "Как и до любого более-менее пристойного уровня."
    play sound ds_sfx_psy
    vol "Сейчас на её фоне – не знаю, именно на её или вообще – ты ощущаешь себя полным ничтожеством."
    $ ds_damage_morale()

    stop music fadeout 3

    th "Ведь всего-то – сыграть песню в три аккорда!"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_stage_normal_night 
    with dissolve

    play ambience ambience_camp_center_night fadein 2

    show dv normal pioneer at center   with dissolve
    window show
    dv "Хотя, конечно, мелодия слишком простая."
    "Ты откладываешь гитару в сторону."
    "Алиса на секунду задумалась."
    show dv smile pioneer at center   with dspr
    dv "Её бы и первоклассник сыграл!"
    me "Спасибо,{w} я старался!"
    show dv laugh pioneer  with dspr
    dv "Оно и видно!"
    play sound ds_sfx_psy
    aut "Похоже, она пытается как можно более явно доказать своё превосходство хотя бы в умении играть на гитаре."
    me "Не всем быть музыкантами, знаешь ли."
    show dv normal pioneer  with dspr
    dv "Ну почему же..."
    "Алиса поднимает глаза к небу."
    dv "Хотя тебе-то точно не суждено!"
    window hide
    menu:
        "Согласиться":
            window show
            me "Наверное..."
            show dv angry pioneer with dspr
            dv "Ты даже сдаёшься слишком легко!"
        "Спросить":
            window show
            me "Это почему ещё?"
            show dv laugh pioneer  with dspr
            dv "Ты бы себя со стороны послушал!"
        "Возразить":
            window show
            me "Неправда. Я потренируюсь, и всё получится!"
            show dv normal pioneer with dspr
            dv "Ну... всякие чудеса случаются. Иногда."
    vol "Ты уже начинаешь жалеть, что вообще пришёл сюда."
    play sound ds_sfx_int
    lgc "Но ладно ты – зачем это Алисе?{w} Ведь и так понятно, что гитарист из меня никудышный."
    me "Естественно.{w} Но если практиковаться..."
    show dv smile pioneer  with dspr
    dv "Будешь практиковаться, значит?"
    me "Не знаю... Может, и буду."
    play sound ds_sfx_psy
    vol "Внезапно ты чувствуешь обидную жалость к себе, апатию, появляется желание поскорее уйти отсюда, забыть сегодняшний вечер."
    vol "Эти чувства оставили противное ощущение и острую необходимость сделать (или на худой конец сказать) глупость."
    window hide
    menu:
        "{check=composure:16}Отреагировать спокойно":
            if skillcheck('composure', lvl_godly):
                window show
                play sound ds_sfx_mot
                com "{result}Не поддавайся. Держись спокойно."
                me "Да! Я справлюсь!"
                $ ds_skill_points['composure'] += 1
            else:
                window show
                play sound ds_sfx_mot
                com "{result}Нет. Ты слишком разъярён её словами."
                me "Как будто от этого что-то изменится!"
                show dv surprise pioneer  with dspr
                dv "От чего?"
                me "От того, что я научусь играть на гитаре!"
        "Сорваться":
            window show
            me "Как будто от этого что-то изменится!"
            show dv surprise pioneer  with dspr
            dv "От чего?"
            me "От того, что я научусь играть на гитаре!"
    show dv laugh pioneer  with dspr
    dv "Да ты и не научишься! Так, побренчишь пару дней и бросишь."
    vol "Слова Алисы ранят тебя в самое сердце."
    me "Ну знаешь что!"
    th "А ведь что она должна {i}знать{/i}? Какое ей, в сущности, до меня дело?"
    th "И я так реагирую, потому что это правда или потому что эту правду в слова обличила именно Алиса?"
    me "Человек не может всего уметь!"
    show dv grin pioneer  with dspr
    dv "Наверняка не может...{w} Но хоть что-то он уметь должен."
    me "То есть ты хочешь сказать, что я ничего не умею?"
    dv "Ну откуда же я знаю?"
    me "Да я..."
    th "Я что?"
    th "Рассказать ей про навыки работы с компьютером?{w} Про прочитанные книги или просмотренные фильмы?"
    me "Ладно, бессмысленный разговор."
    show dv laugh pioneer  with dspr
    dv "Само собой."
    me "Тебе бы только веселиться!"
    show dv angry pioneer  with dspr
    dv "А тебе бы только унывать."
    me "Ой, ладно!"
    hide dv  with dissolve
    "Ты спрыгиваешь со сцены и уверенными шагами направился прочь с концертной площадки."
    dv "Ну и иди-иди!"
    "Cлышится тебе вслед крик Алисы."
    me "Ну и иду-иду!"
    "Шипишь ты себе под нос."
    window hide

    $ persistent.sprite_time = "night"
    scene cg ds_day3_sl_clean
    with dissolve

    play sound_loop sfx_broom_sweep fadein 2

    window show
    "Дорога выводит тебя на площадь, посреди которой стоит Славя и весело размахивает метлой."
    if skillcheck('logic', lvl_trivial, passive=True):
        play sound ds_sfx_int
        lgc "{result}Видимо, прошло много времени. Уже не то, что дискотека закончилась - Славя успела переодеться в пионерскую форму."
    "Наконец, она замечает тебя и откладывает метлу."
    scene bg ext_square_night_party2
    show sl smile pioneer at center
    with dissolve
    sl "Ой, Семён, привет, а я думала, что все уже спят."
    me "Нет... А ты что делаешь?"
    show sl normal pioneer  with dspr
    sl "Убираюсь вот после дискотеки. А ты почему не пришёл?"
    window hide
    menu:
        "Рассказать про Алису":
            window show
            me "Да так, позорился с Алисой..."
            show sl surprise pioneer with dspr
            sl "В плане?"
            me "Ну, я безуспешно пытался играть на гитаре, а она смеялась надо мной."
            "Cлавя задумывается над твоими словами."
            show sl smile pioneer with dspr
            sl "Не суди её строго. Не думаю, что она всерьёз хотела тебя обидеть. Просто... у неё некоторые проблемы."
            if skillcheck('drama', lvl_easy, passive=True):
                play sound ds_sfx_int
                dra "{result}Славя что-то скрывает от тебя про Алису."
                window hide
                menu:
                    "Cпросить":
                        window show
                        me "Ты что-то про неё знаешь?"
                        show sl serious pioneer with dspr
                        sl "Конечно, знаю. Я же помощница вожатой. Но это очень личное. Я не вправе рассказывать об этом без её согласия."
                        me "Ну расскажи."
                        sl "Нельзя! Она сама расскажет, если захочет! И если заработаешь её доверие."
                        $ ds_skill_points['drama'] += 1
                    "Не спрашивать":
                        window show
                        me "Наверное, оно и так... Но обидно же!"
            else:
                me "Наверное, оно и так... Но обидно же!"
            sl "Я понимаю, что обидно. Такой уж она человек. Надеюсь, в будущем она исправится."
            sl "А ты не принимай это близко к сердцу. Даже если ты действительно плохо сыграл - это ничего, научишься. Ну, или займёшься чем-нибудь другим, что лучше получается."
            $ ds_up_morale()
        "Cослаться на прогулку":
            window show
            me "Да просто...."
            sl "А где был?"
            me "Я..."
            me "Гулял."
            show sl smile2 pioneer  with dspr
            sl "Понятно... Но тебе всё же стоило прийти – было весело."
            me "Рад за вас."
        "Сказать, что не захотел":
            window show
            me "Просто не захотел, и всё тут! Дискотеки - не моё!"
            show sl smile2 pioneer  with dspr
            sl "Зря ты так, очень зря... Тебе всё же стоило прийти – было весело."
            me "Рад за вас."
    play sound ds_sfx_fys
    edr "За сегодняшний день ты изрядно вспотел – то ли от волнения, то ли виной тому была душная ночь."
    window hide
    menu:
        "Пойти помыться":
            window show
        "Отбросить мысль":
            window show
            th "Ну нет, сейчас я хочу поскорее лечь спать. Помоюсь завтра!"
            me "Ладно, я спать пойду..."
            show sl normal pioneer with dspr
            sl "Хорошо, спокойной ночи, Семён!"
            me "Ага, спокойной ночи..."
            jump ds_day3_mt_interrogate_2
    me "Слушай, а ты не знаешь, где здесь можно помыться?"
    show sl normal pioneer  with dspr
    sl "Да, конечно. Сейчас идёшь прямо, потом чуть налево, по дорожке и направо, увидишь там баню."
    sl "Может, тебя проводить?"
    window hide
    menu:
        "Согласиться":
            window show
            me "Давай!"

            stop sound_loop fadeout 2

            show sl smile2 pioneer at center
            with dspr
            sl "Идём!"
            $ ds_lp['sl'] += 1
            
            window hide

            stop ambience fadeout 2

            $ persistent.sprite_time = "night"
            scene bg ext_path_night 
            show sl normal pioneer at center
            with dissolve

            play ambience ambience_forest_night fadein 2

            window show
            "Вы идёте по лесной тропинке."
            play sound ds_sfx_fys
            edr "Всё тело нестерпимо чешется."
            th "Интересно, и как я не замечал этого раньше?"
            th "И даже более интересно – что ещё я не замечал."
            play sound ds_sfx_int
            lgc "Если так дальше пойдёт, то придётся остаться в этом мире насовсем!"
            window hide

            $ persistent.sprite_time = "night"
            scene bg ext_bathhouse_night 
            show sl normal pioneer at center
            with dissolve

            window show
            "Из-за деревьев показывается здание бани."
            me "А почему пионеры моются именно здесь?"
            sl "А, душевые в ремонте."

            stop ambience fadeout 2

            me "Ладно, что уж теперь..."
            sl "Ну всё, я пойду, мне надо доубираться."
            window hide
            menu:
                "Предложить помыться вместе":
                    window show
                    me "А давай вместе помоемся!"
                    show sl laugh pioneer at center
                    with dspr
                    sl "Нет уж, не сейчас! Я занята! Как-нибудь в следующий раз, может быть..."
                "Поблагодарить":
                    window show
                    me "Cпасибо..."
                    show sl smile pioneer at center
                    with dspr
                    sl "Не за что, Семён!"
                "Молча отпустить":
                    window show
                    $ ds_lp['sl'] -= 1
            hide sl with dissolve
            window hide
        "Отказаться":
            window show
            me "Нет-нет, не надо, сам найду!"

            stop sound_loop fadeout 2
            
            window hide

            stop ambience fadeout 2

            $ persistent.sprite_time = "night"
            scene bg ext_path_night 
            with dissolve

            play ambience ambience_forest_night fadein 2

            window show
            "Ты идёшь по лесной тропинке примерно в том направлении, что указала Славя."
            play sound ds_sfx_fys
            edr "Всё тело нестерпимо чешется."
            th "Интересно, и как я не замечал этого раньше?"
            th "И даже более интересно – что ещё я не замечал."
            play sound ds_sfx_int
            lgc "Если так дальше пойдёт, то придётся остаться в этом мире насовсем!"
            window hide

            $ persistent.sprite_time = "night"
            scene bg ext_bathhouse_night 
            with dissolve

            window show
            "Из-за деревьев показывается здание бани."
            th "И почему пионеры моются именно здесь?"
            play sound ds_sfx_int
            enc "Кажется, Ольга Дмитриевна что-то говорила про ремонт душевых."

            stop ambience fadeout 2

            me "Ладно, что уж теперь..."
            window hide

    scene black 
    with dissolve

    $ renpy.pause(1)

    $ persistent.sprite_time = "night"
    scene bg ext_bathhouse_night 
    with dissolve

    play ambience ambience_forest_night fadein 2

    window show
    "Ты быстренько вымылся – благо в бане нашлось и мыло и чистые полотенца, – выходишь на улицу и полной грудью вдыхаешь заметно посвежевший ночной воздух."
    play sound ds_sfx_int
    con "Как же всё-таки состояние чистоты физической способствует очищению духовному!"
    play sound ds_sfx_psy
    vol "Все проблемы если не исчезли, то по крайней мере стали менее важными; словно грязь с тела, водой с души смыло тревогу."
    "Внезапно на тебя нападает сильная зевота и ты, вытирая навернувшиеся на глаза слёзы, медленно двигаешься по направлению к домику вожатой."

    play music music_list["two_glasses_of_melancholy"] fadein 3

    show dv shocked pioneer at center   with dissolve
    "Но не успеваешь ты сделать и пары шагов, как из кустов буквально в метре от меня выскакивает Алиса."
    dv "А ты... ты что здесь делаешь?"
    me "Мылся."
    show dv normal pioneer  with dspr
    "Несколько придя в себя, она продолжает."
    dv "Ну и?"
    me "Что?"
    show dv angry pioneer  with dspr
    dv "Не знаю что!"
    me "Зачем тогда говоришь, если не знаешь?"
    play sound ds_sfx_mot
    com "Вся твоя умиротворённость вмиг куда-то исчезает – остаётся лишь раздражение да усталость."
    window hide
    menu:
        "Выслушать":
            window show
            me "Я тебя слушаю. Очень внимательно!"
        "Идти дальше":
            window show
            me "Ладно, если ты не против..."
            show dv shy pioneer  with dspr
            dv "Подожди..."
            me "Что ещё?"
    dv "Если там на сцене ты подумал, что... ну... я не хотела тебя как-то обидеть или что-то такое..."
    window hide
    menu:
        "Ответить формально":
            window show
            me "Хорошо. Я на тебя не обижаюсь."
            show dv smile pioneer  with dspr
            dv "Но всё-таки играть ты не умеешь - это факт!"
        "Ответить пассивно-агрессивно":
            window show
            me "Всё нормально, я не обиделся. Я просто не умею играть на гитаре, и всё. В этом нет ничего страшного – многие люди не умеют."
            "В твоём голосе слишком явно звучат нотки недовольства, но остановиться ты никак не можешь – наоборот, хочется высказать ей всё прямо здесь и сейчас."
            show dv smile pioneer  with dspr
            dv "Не умеешь – это точно!"
        "Ответить примирительно":
            window show
            me "Да ты меня не обидела. Ну кто обижается на правду? Всё ты правильно сказала."
            me "А я действительно поработаю над своей игрой."
            show dv smile pioneer with dspr
            dv "Что-то не очень верится..."
    com "Алиса явно сдерживается, чтобы не засмеяться."
    window hide
    menu:
        "Уйти":
            window show
            me "Ой, ладно, надоело!"
            hide dv  with dissolve
            com "В этот раз она смогла тебя по-настоящему достать."
            com "Ещё немного – и ты бы сорвался на крик...{w} Или даже что похуже."
            dv "Подожди."
            me "Отстань уже, а!"
            "Алиса идёт за тобой, но в этот раз не пытается остановить."
        "Остаться":
            window show
            me "Что ещё скажешь?"
    dv "Но ведь я правда ничего такого не хотела..."
    show dv shy pioneer at center   with dissolve
    play sound ds_sfx_psy
    vol "Словно какая-то неведомая сила заставляет тебя развернуться к ней."
    play sound ds_sfx_int
    dra "Знай: это любовь!"
    play sound ds_sfx_psy
    aut "Да какая любовь? К Алисе-то?! Как её можно любить?!"
    play sound ds_sfx_psy
    ine "Ну... можно. Ты это уже показывал."
    th "Когда?!"
    ine "Лучше и не вспоминай об этом."
    window hide
    menu:
        "Принять извинения":
            window show
            me "Хорошо, будем считать, что ты извинилась. Я на тебя не обижаюсь."
            me "Теперь я могу идти?"
            dv "Да... Конечно..."
        "Ответить равнодушно":
            window show
            me "Хорошо. Теперь я могу идти?"
            dv "Да, конечно."
        "Поддержать":
            window show
            me "Я понимаю, что не хотела. Но в каком-то смысле ты всё же права."
            show dv grin pioneer at center
            with dspr
            dv "Конечно же права!"
            th "Да что с ней не так-то?! То извиняется, то снова насмехается..."
            if skillcheck('empathy', lvl_up_medium, passive=True):
                play sound ds_sfx_psy
                emp "{result}Она не понимает, как себя вести - вот и всё."
            if skillcheck('encyclopedia', lvl_medium, passive=True):
                play sound ds_sfx_int
                enc "{result}Здесь лучше всего подходит японское понятие «цундере». Очень похоже - девушка, чьё отношение резко меняется от высокомерного к нежному."
    show dv guilty pioneer at center
    with dspr
    play sound ds_sfx_int
    con "В свете Луны Алиса с виноватым выражением на лице выглядит очень красиво."
    aut "Действительно, если бы ей заклеить рот..."
    if skillcheck('instinct', lvl_easy, passive=True):
        play sound ds_sfx_fys
        ins "{result}Или заткнуть твоим стволом..."
    show dv angry pioneer  with dspr
    dv "Чего лыбишься?!"
    window hide
    menu:
        "Высказать про вежливость":
            window show
            me "Да нет, просто подумал, что если бы ты была повежливее..."

        "Похвалить внешность":
            window show
            me "Да так... засмотрелся на тебя..."
            show dv angry pioneer at center
            with dspr
            dv "Не отвлекайся! Нам договорить надо!"
            me "О чём?"
            dv "Ты и сам прекрасно догадываешься, о чём."
            me "Нет, не догадываюсь."
            dv "Слушай, я тебя не держу! Если не хочешь нормально разговаривать - иди уже!"
            window hide
            menu:
                "Уйти":
                    window show
                    me "Ну и пойду!"
                    "И ты действительно уходишь. Уже окончательно."
                    hide dv with dissolve
                    "Алиса даже не пытается тебя задержать."
                    $ ds_lp['dv'] -= 1
                    if skillcheck('empathy', lvl_medium, passive=True):
                        play sound ds_sfx_psy
                        emp "{result}Естественно. Она до последнего хотела с тобой поговорить, а ты так и не пошёл на контакт."
                        jump ds_day3_evening_dv_end
                "Продолжить разговор":
                    window show    
                    me "Так это не я поговорить захотел..."
                    me "Слушай. Вот была бы ты повежливее..."
        "Уйти":
            window show
            me "Неважно. Я пошёл! Удачи!"
            "И ты действительно уходишь. Уже окончательно."
            hide dv with dissolve
            "Алиса даже не пытается тебя задержать."
            $ ds_lp['dv'] -= 1
            if skillcheck('empathy', lvl_medium, passive=True):
                play sound ds_sfx_psy
                emp "{result}Естественно. Она до последнего хотела с тобой поговорить, а ты так и не пошёл на контакт."
            jump ds_day3_evening_dv
    stop music fadeout 3

    show dv surprise pioneer  with dspr
    dv "То что?"
    play sound ds_sfx_int
    rhe "Такие фразы обычно не принято заканчивать – каждый в состоянии додумать в меру своих интеллектуальных возможностей."
    me "То ничего."
    show dv angry pioneer  with dspr
    dv "Нет уж, раз начал, то договаривай!"
    me "Да нечего тут договаривать. К тому же я устал, спать пойду."
    hide dv  with dissolve
    dv "Ну-ка стой!"
    me "Не вынуждай меня бегать от тебя!"
    show dv angry pioneer at center   with dissolve
    dv "Всё равно не убежишь!"
    play sound ds_sfx_int
    edr "Возможно и так, ведь за сегодняшний день ты слишком устал, а уж после бани никакого желания бегать не возникало и подавно."
    dv "Ну так что?"
    me "Что?"
    show dv rage pioneer  with dspr
    dv "Если бы я была повежливее, то что?"
    me "Попробуй сама и узнаешь."
    dv "Да с какой стати я ради такого дурака, как ты..."
    me "Ну не пробуй тогда, не знаю, я-то тут при чём?"
    hide dv  with dissolve
    "Ты глубоко вздыхаешь и медленно плетёшься в сторону площади."
    dv "А ты бы тогда?"
    me "Что?"
    "Бросаешь ты ей, не оборачиваясь."
    dv "Ну, если бы я это, то ты бы?.."
    show dv shy pioneer far at center   with dissolve
    if skillcheck('empathy', lvl_challenging, passive=True):
        play sound ds_sfx_psy
        emp "{result}Она хочет услышать нечто про {i}ваши{/i} взаимоотношения."
        emp "А агрессия - от стеснения. Или страха. В общем, она опасается делать первые шаги, пытается защититься от чего-то."
        th "Но почему я?"
        emp "Потому что. Ты её за-ин-те-ре-со-вал. Если это взаимно - тебе придётся двигаться навстречу самому."
        th "А заинтересовала ли она меня?"
    window hide
    menu:
        "Поддержать Алису" if ds_last_skillcheck.result:
            window show
            me "Конечно! Так-то ты девушка интересная, очень даже! И на гитаре играешь чудесно... не то, что я."
            me "Да, будь немного повежливее и поаккуратнее - и всё у нас получится!"
            me "И играть я научусь тоже. Вот увидишь!"
            emp "Ну не так же резко двигаться навстречу!"
            $ ds_skill_points['empathy'] += 1
            $ ds_lp['dv'] += 1
            emp "Но всё-таки в глубине души ей понравилось сказанное тобой."
        "Показать непонимание, но согласиться":
            window show
            me "Не понимаю, о чём речь, но давай думать, что «я бы», если тебе так будет легче."
        "Показать непонимание и отказать":
            window show
            me "Не понимаю, о чём речь. А с такими вводными я соглашаться не намерен!"
            me "Скажи прямо: чего ты хочешь?"
        "Послать":
            window show
            me "Иди нафиг уже, задолбала!"
            $ ds_lp['dv'] -= 2
        "Проигнорировать":
            window show
            "Ты молча уходишь."
            $ ds_lp['dv'] -= 1
    show dv angry pioneer far at center   with dspr
    dv "Придурок!"
    hide dv  with dissolve

    stop ambience fadeout 2

    "Кричит Алиса и быстро шагает к бане."
    $ ds_day3_dv_conflict = True
    window hide

    jump ds_day3_evening_dv_end

label ds_day3_evening_dv_end:
    $ persistent.sprite_time = "night"
    scene bg ext_square_night 
    with dissolve

    play ambience ambience_camp_center_night fadein 2

    window show
    play sound ds_sfx_int
    con "Площадь сверкает чистотой немецких дорог."
    play sound ds_sfx_int
    enc "По преданиям тех лет их мыли с шампунем."
    th "Ну и Славя!"
    th "А я только спорил с Алисой, и всё..."
    play sound ds_sfx_psy
    vol "И зачем вообще, спрашивается?"
    vol "Как будто была в этом какая-то необходимость!"
    th "Да и её поведение..."
    if skillcheck('empathy', lvl_easy, passive=True):
        play sound ds_sfx_psy
        emp "{result}Дурак ты, Семён. Нравишься ты ей, нра-вишь-ся, а за подобным хамством Алиса просто скрывает это."
    th "Хотя сейчас совершенно не до этого!"
    play sound ds_sfx_psy
    ine "Может, она и не человек вовсе!"
    ine "Ну а если бы была человеком, и всё происходило в {i}реальном{/i} мире?.."
    play sound ds_sfx_int
    vic "Да вроде и этот мир вполне себе реальный. Просто другой."

    stop ambience fadeout 2

    "Ты решительно отгоняешь от себя эти мысли и направляешься к домику вожатой – усталость берёт своё."
    window hide
    jump ds_day3_mt_interrogate_2

label ds_day3_mt_interrogate_2:
    $ persistent.sprite_time = "night"
    scene bg ext_house_of_mt_night 
    with dissolve

    play music music_list["silhouette_in_sunset"] fadein 3

    window show
    play sound ds_sfx_psy
    vol "Возле двери тебя словно останавливает невидимое препятствие."
    vol "Ольга Дмитриевна точно сейчас поинтересуется, где ты был и почему пропустил дискотеку."
    play sound ds_sfx_fys
    hfl "Даже скорее устроит допрос с пристрастием."
    play sound ds_sfx_int
    lgc "Впрочем, учитывая отсутствие на танцах ещё и Алисы, нетрудно было догадаться, что прогуливали мы вместе."
    play sound ds_sfx_psy
    aut "С другой стороны, стоит ли вообще рассказывать, что вместо дискотеки Алиса упражнялась в гитарной игре, а ты – в саморефлексиях?"
    th "В принципе, ничего такого..."
    th "Если уж я и прогулял, то не столь важно по каким причинам."
    th "Так что…"
    play sound ds_sfx_psy
    sug "Но в то же время кажется, что лучше промолчать."
    th "Ладно, решу по обстоятельствам."
    "Ты глубоко вздыхаешь и тянешь ручку двери."
    window hide

    play sound sfx_open_dooor_campus_1

    $ persistent.sprite_time = "sunset"
    scene bg int_house_of_mt_night 
    with dissolve

    show mt normal dress at center   with dissolve
    window show
    "Внутри тебя уже ждёт Ольга Дмитриевна, одетая в платье."
    $ ds_karma -= 5
    $ ds_lp['mt'] -= 1
    show mt surprise dress at center   with dspr
    mt "Итак, Семён, где же ты был?"
    window hide

    menu:
        "Рассказать про Алису":
            window show
            me "По правде говоря, я с Алисой был на сцене."
            mt "И что же вы там делали?"
            me "Играли на гитаре…"
        "{check=drama:11}Придумать другое оправдание":
            $ ds_lp['dv'] += 1
            if skillcheck('drama', lvl_up_medium):
                window show
                play sound ds_sfx_int
                dra "{result}Вы помогали Виоле, мессир. Она же просила помочь - вот и помог. И неважно, что это неправда."
                me "Виоле помогал. Ей нужно было с лекарствами разобраться."
            else:
                window show
                play sound ds_sfx_int
                dra "{result}Просто гуляли, вот и всё."
                me "Я…{w} гулял."
                mt "Один?"
                me "Да…"
        "Нагрубить":
            window show
            me "Неважно! Не захотел - и не пришёл!"
            show mt angry dress at center
            with dspr
            mt "Ты повежливее разговаривай, пожалуйста!"
            $ ds_lp['mt'] -= 1

    show mt normal dress at center   with dspr
    mt "Ладно, не столь важно, где ты был, главное – почему не пришёл на дискотеку!"
    window hide
    menu:
        "Не захотел":
            window show
            me "Просто не захотел..."
        "Не люблю танцевать":
            window show
            me "Ну, знаете, честно говоря, я не люблю танцевать…"
        "Испугался":
            window show
            me "Да знаете... застеснялся просто..."
    show mt angry dress at center   with dspr
    mt "Ну и что?{w} Это же общелагерное мероприятие, а значит, на нём должны присутствовать все пионеры!"
    "Она внимательно смотрит на тебя."
    show mt surprise dress at center   with dspr
    mt "В крайнем случае посидел бы в сторонке."
    me "Извините…"
    "Ты вздыхаешь."
    show mt smile dress at center   with dspr
    mt "Ладно."
    "Смягчается вожатая."
    mt "А теперь быстро спать!"
    hide mt  with dissolve
    th "Кажется, всё обошлось."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_house_of_mt_night2 
    with dissolve2

    window show
    "Ты долго ворочаешься, и сон никак не идёт."
    "В голове крутятся мысли о музыке, гитаре и Алисе…"
    th "Интересно, смог бы я стать профессиональным музыкантом?"
    th "И так уж ли мне хочется им стать?"
    th "Хотя с чего вдруг {i}хочется{/i}?..{w} Конечно, весело бы было, но не более того."
    th "Или, может, всё дело в Алисе?"
    th "Она ведь правда как энергетический вампир – все соки высосет подчистую!"
    play sound ds_sfx_psy
    vol "Думаешь? А вот мне кажется, что она как раз таки пытается столкнуть тебя с насиженного места."
    th "Что-то не уверен..."
    window hide

    with fade

    window show
    "…"

    stop music fadeout 3

    "Вскоре глаза начинают закрываться, и через некоторое время ты проваливаешься в сон."
    window hide

    scene bg black 
    with fade3

    $ renpy.pause(3)

    jump ds_day3_dream

label ds_day3_dance_sl:
    $ ds_day3_evening_who = 'sl'
    $ ds_lp['sl'] += 1

    "Она протягивает тебе руку."
    "Вы стоите в середине танцующей толпы."
    "Точнее, стоишь ты, Славя же «разогревается» – пританцовывает в такт музыке."
    window hide
    menu:
        "{check=savoir_faire:8}Присоединиться":
            if skillcheck('savoir_faire', lvl_easy):
                window show
                play sound ds_sfx_mot
                svf "{result}Не забивай себе голову - от тебя никто не требует высокого мастерства. Просто танцуй."
                "Ты начинаешь танцевать. У тебя более-менее получается двигаться в ритм."
            else:
                window show
                play sound ds_sfx_mot
                svf "{result}От нервов ни руки, ни ноги тебя не слушаются. Ничего вразумительного у тебя не выходит."
        "Cтоять дальше":
            window show
            th "И зачем я только согласился?"
            th "Выйти-то я вышел, а дальше что?"
            "Ты оглядываешь танцующих пионеров вокруг себя."
            th "Нет, на такое я не готов."

    stop music fadeout 3

    "Вдруг музыка стихает."
    "Некоторые продолжают танцевать по инерции, но большинство всё же остановилось."
    mt "Без паники!"
    "Вожатая подоходит к диджейскому пульту и, преодолевая слабое сопротивление Мику, что-то там подкручивает."
    mt "Следующая песня – дамы приглашают кавалеров!"
    "Ты смотришь на Славю."
    "Она с улыбкой протягивает мне руку."
    play sound ds_sfx_psy
    sug "Что же, девушкам отказывать нельзя."
    window hide

    scene cg d3_sl_dance 
    with dissolve

    stop ambience fadeout 2

    play music music_list["confession_oboe"] fadein 2

    window show
    "Несколько минут вы кружитесь в танце."
    "Её грудь учащённо вздымается, а лицо всё больше краснеет."
    "Славя, не отрываясь, смотрит тебе в глаза."
    window hide
    menu:
        "Удерживать взгляд на Славе":
            window show
            "Ты отвечаешь ей взаимностью. Тоже смотришь на неё."
            "От этого она краснеет ещё больше."
            $ ds_lp['sl'] += 1
        "Отвести взгляд":
            window show
            "Ты пытаешься перевести взгляд то на танцующих рядом пионеров, то себе под ноги, то ещё куда-нибудь."
    play sound ds_sfx_psy
    vol "Странное чувство: по всему телу изредка пробегает дрожь, но это приятная дрожь, без намёка на неловкость или тем более стыд."
    vol "На душе удивительно спокойно."
    vol "Ты не хочешь отпускать эту девочку и готов кружиться с ней вместе в танце бесконечно!"
    play sound ds_sfx_mot
    res "Мимо вас вприпрыжку проскакивает Ульянка, на секунду останавливается и ехидно улыбается."
    play sound ds_sfx_int
    lgc "Возможно, показалось, конечно, но скорее она на {i}кое-что{/i} намекает."
    window hide
    menu:
        "Прикрикнуть на Ульяну":
            window show
            me "Не мешайся под ногами!"
            "Ульяна, не сказав ни слова, убегает."
        "Cкорчить гримасу":
            window show
            "Ты корчишь устрашающую гримасу, но Ульяна уже убежала."
        "Проигнорировать":
            window show
    sl "Что-то не так?"
    window hide
    menu:
        "Cказать про Ульяну":
            window show
            me "Да Ульянка мешается тут."
            sl "А, ну ничего!"
        "Сказать, что всё хорошо":
            window show
            me "Да нет, всё хорошо...{w} То есть отлично."
        "Сказать, что некомфортно":
            window show
            me "Да типа... знаешь... мне непривычно с девушками танцевать."
            sl "Ну, бывает. Хорошо танцуешь, кстати!"
    if not skillcheck('volition', lvl_medium, passive=True):
        play sound ds_sfx_psy
        vol "{result}Ты пока ещё не заикаешься, но уже близок к этому."
    sl "Ты так напряжён."
    window hide
    menu:
        "Признать":
            window show
            me "Есть немного."
        "Отрицать":
            window show
            me "Да нет, не особо."
    sl "Мальчики не любят танцевать."
    me "Пожалуй..."
    "Она ничего не отвечает, лишь улыбается."
    window hide

    with fade

    window show
    "Наконец песня заканчивается."

    stop music fadeout 3

    window hide
    menu:
        "Продолжить обнимать":
            window show
            "Ты по инерции продолжаешь обнимать Славю, но она легко освобождается из твоих рук."
        "{check=volition:12}Поцеловать Славю":
            if skillcheck('volition', lvl_challenging):
                window show
                play sound ds_sfx_psy
                vol "{result}Ты тянешься к её губам."
                $ ds_skill_points['volition'] += 1
                if ds_lp['sl'] >= 15:
                    "И Славя овтечает тебе взаимностью."
                    $ ds_lp['sl'] += 1
                    play sound ds_sfx_mot
                    per_toc "Ощущение от её губ прекрасно."
                    vol "Неземное блаженство."
                    "Но всё хорошее рано или поздно кончается. Славя отходит от тебя..."
                    "...погладив по щеке."
                else:
                    "Но Славя своей рукой легонько тебя отталкивает."
                    sl "Рановато потянулся, Семён!"
                    $ ds_lp['sl'] -= 1
            else:
                window show
                vol "{result}У тебя не хватает решимости на столь радикальный шаг."
                "Пока ты думаешь, Славя выбирается из твоих объятий."
        "Отойти от Слави":
            window show
            "На этом всё. Ты отходишь от Слави."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_square_night_party 
    with dissolve

    play ambience ambience_camp_center_evening

    show sl smile dress at center   with dissolve
    window show
    sl "Спасибо за танец!"
    show sl laugh dress at center   with dspr
    window hide
    menu:
        "Поблагодарить в ответ":
            window show
            me "Это тебе спасибо."
        "Промолчать":
            window show
    "Некоторое время ты просто стоишь и смотришь на неё."
    "Играет следующий трек."
    show sl normal dress at center   with dspr
    sl "Ещё?"
    $ ds_on_disco = False
    window hide
    menu:
        "Потанцевать ещё":
            window show
            me "Да, давай, конечно!"
            show sl smile dress at center
            with dspr
            sl "Вот, правильный настрой!"
            if ds_to_help_un:
                $ ds_lp['un'] -= 1
            "Вы вновь пускаетесь в пляс."
            scene cg d3_sl_dance 
            with dissolve
            "У Слави определённо хорошее настроение. Она решает заговорить с тобой."
            $ ds_on_disco = True
        "Сбежать":
            me "Нет, пожалуй, передохну."
            hide sl  with dissolve
            "Ты стараешься как можно скорее покинуть площадь."
            window hide

            $ persistent.sprite_time = "night"
            scene bg ext_beach_night 
            with dissolve

            play ambience ambience_lake_shore_night fadein 3

            window show
            th "Не помню, как оказался на пляже..."
            play sound ds_sfx_psy
            vol "Почему же ты всё-таки убежал?"
            play sound ds_sfx_psy
            aut "Ведь это выглядело именно как побег."
            vol "Вроде танец вышел неплохой, да и Славя осталась довольной."
            vol "Однако что-то не так, ты чувствуешь себя неловко при одном воспоминании о дискотеке."
            vol "Может быть, просто перестал контролировать ситуацию и поддался эмоциям?"
            vol "Такое случается с тобой крайне редко."
            vol "Что бы ни происходило, ты всегда старался держать себя в руках и трезво оценивать действительность.{w} А тут не получилось…"
            "Ты садишься на песок и смотришь на речку."
            "Над водой вдалеке нависает полная луна."
            if skillcheck('inland_empire', lvl_easy, passive=True):
                play sound ds_sfx_psy
                ine "{result}Тебе в голову приходят воспоминания."
                window hide

                with fade2

                stop ambience fadeout 2

                play music music_list["memories_piano_outdoors"] fadein 2

                window show
                ine "Тебе 6 лет. Ты с отцом на речке ловишь рыбу. Ты неумело забрасываешь удочку и ждёшь. Минуту, две, десять. Не клюёт. А папа тем временем таскает одну за одной."
                me "Как ты это делаешь?"
                ine "Он тебе объясняет. Но сейчас ты уже не помнишь всей технологии."
                ine "9 лет. Тёмный недостроенный дом на даче, в котором живут не то привидения, не то вампиры, не то просто бомжи. Хлипкая деревянная лестница на второй этаж, буквально покачивающаяся над бездной – дыркой в подвал."
                ine "Страшно, но ты всё равно изо дня в день лазаешь туда-сюда. Упавший на ногу кирпич. Сошёл ноготь."
                ine "12 лет. Первая победа на турнире по компьютерным играм. Мы играем в какую-то приставочную драчку. Победа оглушительная, мне рукоплещет весь зал выдуманных зрителей."
                ine "15 лет. Несколько красивых голов пяткой, с тридцати метров в девятку, головой…"
                ine "17 лет. Первая любовь. Мимолётный образ, тень ускользает от меня и скрывается в городской дымке. Поворот за поворотом, дом за домом – её не догнать…"
                vol "Не продолжай! Это воспоминание для тебя слишком болезненно! Ты не готов!"
                ine "Дальше воспоминания становятся более чёткими, но при этом гораздо менее яркими."
                ine "Картинки детства и юношества, проплывающие у тебя перед глазами, размыты, где-то не хватает деталей, где-то ты не можешь разобрать лиц людей, а где-то образы больше напоминают полотно, на которое случайно разлили несколько флаконов с красками."
                vol "Однако ощущение от этих неясных картин куда более тёплое, чем от предыдущих воспоминаний."

            stop music fadeout 3

            window hide

            with fade2

            window show

            sl "Вот ты где!"
            window hide

            scene cg d3_sl_evening 
            with dissolve

            play music music_list["forest_maiden"] fadein 2

            window show
            "Над тобой склонилась Славя."
            if skillcheck('composure', lvl_trivial, passive=True):
                play sound ds_sfx_mot
                com "{result}Ты совсем не испугался."
            else:
                me "Славя?! Как ты нашла меня?!"
            sl "Чего ты так быстро убежал?"
            me "Да просто захотелось побыть одному."
            play sound ds_sfx_psy
            vol "Ты словно забрался в панцирь – внешнего мира для тебя больше не существует."
            play sound ds_sfx_psy
            ine "А на его раздражители отвечают твои двойники.{w} Их всегда трое.{w} Один глухой, другой немой, третий слепой."
            sl "Красиво тут, да?"
            "Славя смотрит на речку."
            me "Красиво…"
            sl "Может, ещё пойдём потанцуем?"
            window hide
            menu:
                "Согласиться":
                    window show
                    me "Давай..."
                    sl "Только посидим тут ещё? Слишком уж тут хорошо!"
                    me "Ну ладно..."
                "Отказаться":
                    window show
                    me "Нет, мне и тут неплохо."
                    play sound ds_sfx_psy
                    emp "Не стоит себя так вести со Славей."
                    vol "Но тебя, как куклу, кто-то словно дёргает за верёвочки, заставляя говорить то, что ты бы при других обстоятельствах никогда не сказал."
        "Пойти помогать Лене" if ds_to_help_un:
            window show
            me "Слушай... мне тут надо Лене помочь."
            sl "А... ну ладно, иди."
            "И ты направляешься в сторону медпункта."
            jump ds_day3_un_medic
    sl "О чём думаешь?"
    me "Ни о чём…"
    sl "Нельзя ни о чём не думать!"
    "Она надувает губы, но тут же улыбается, давая понять, что не обижается на тебя всерьёз."
    sl "Ты всегда о чём-то думаешь, даже если и не замечаешь этого."
    me "Наверное."
    sl "Так о чём сейчас?"
    play sound ds_sfx_int
    con "Почему-то из головы не выходят совы."
    play sound ds_sfx_psy
    vol "И ты не можешь удержаться от того, чтобы поделиться этим со Славей. Всяко это лучше, чем ничего не отвечать."
    me "О совах."
    sl "А почему о совах?"
    "Она смеётся."
    me "Не знаю."
    sl "Ты когда-нибудь видел сов?"
    me "Конечно видел."
    play sound ds_sfx_int
    rhe "Что за глупые вопросы…"
    sl "И они тебе нравятся?"
    me "Птица как птица."
    sl "Ночная птица."
    play sound ds_sfx_int
    enc "Cпасибо, капитан Очевидность!"
    me "Да, ночная птица."
    th "Ночная птица..."
    play sound ds_sfx_psy
    ine "У тебя в голове возникает образ совы – небольшой ящичек с перьями, моргающий огромными глазами."
    sl "А ты похож на сову?"
    me "В смысле?"
    sl "Ну, знаешь, бывают же совы и жаворонки. Кто-то рано утром встаёт, а кто-то любит поспать."
    ine "Её слова несколько возвращают тебя к реальности."
    ine "Ты сразу представил свою пыльную комнату, заваленную всяким хламом, гору немытой посуды на столе, гитару, гниющую в углу, галстук, висящий на люстре, и как апофеоз всего – кучу грязных носков под кроватью."
    play sound ds_sfx_psy
    vol "Да, ты был совой.{w} Ночь – твоё время."
    vol "Однако в этом лагере у тебя каким-то образом получается нормально просыпаться по утрам."
    me "Знаю."
    sl "Так кто ты?"
    window hide
    menu:
        "Сова":
            window show
            me "Сова, наверное…{w} Люблю поспать."
            sl "А вот я жаворонок.{w} Чем раньше встанешь, тем больше успеешь сделать за день!"
            vol "Тебе обычно успевать нечего, так что и разницы особой между днём и ночью для тебя нет.{w} Ночью просто тише и спокойнее."
        "Жаворонок":
            window show
            me "Жаворонок... Во всяком случае, по утрам мне легко вставать!"
            sl "О, как и я! Тоже хочешь успеть побольше за день сделать?"
            vol "Не то, чтобы. Тебе обычно успевать нечего, так что и разницы особой между днём и ночью для тебя нет."
            me "Наверное..."
    if skillcheck('empathy', lvl_easy, passive=True):
        play sound ds_sfx_psy
        emp "{result}А вот такой хороший вопрос со звёздочкой: почему Славя такая радостная и всегда готова помочь?"
        window hide
        menu:
            "Cпросить":
                window show
                me "Славя, а у тебя вообще никаких проблем в жизни не бывает?"
                sl "Ты это о чём?"
                "Она удивилась."
                me "Ну, ты всегда такая радостная, всегда готова помочь, с лёгкостью за всё берёшься."
                me "Кажется, что тебя ничего не может расстроить…"
                sl "Почему же!"
                "Она рассмеялась."
                sl "Я обычный человек."
                th "Точно.{w} Совершенно обычный человек в совершенно необычном месте."
                me "А вот мне иногда кажется, что я здесь совсем чужой."
                sl "Тебе не нравится этот лагерь??"
            "Не спрашивать":
                window show
                "Впрочем, Славя не склонна молчать."
                sl "Знаешь, почему-то мне кажется, что ты чувствуешь себя как не в своей тарелке."
                play sound ds_sfx_int
                dra "Вот же прозорливая дама какая..."
                sl "Скажи честно: тебе не нравится этот лагерь?"
    else:
        window show
        "На некоторое время вы замолкаете."
        "Но Славя определённо хочет с тобой говорить и дальше."
        sl "Знаешь, почему-то мне кажется, что ты чувствуешь себя как не в своей тарелке."
        play sound ds_sfx_int
        dra "Вот же прозорливая дама какая..."
        sl "Скажи честно: тебе не нравится этот лагерь?"
    window hide
    menu:
        "Не нравится":
            window show
            me "Да, не особо как-то..."
            sl "А почему?"
            me "Ну не свой я тут, не свой! Лагеря - это не моё!"
        "Дело не в лагере":
            window show
            me "Ну, я не совсем про лагерь.{w} И в прошлой…"
            play sound ds_sfx_int
            rhe "Не стоит так напрямую говорить. Даже со Славей. Не поймёт тебя."
            me "И дома тоже.{w} Что я не такой, как все. Что мне здесь не место…"
        "Отрицать":
            window show
            me "Тебе показалось. Мне нравится лагерь."
            sl "Мне кажется, ты всё-таки что-то недоговариваешь."
            play sound ds_sfx_psy
            emp "Да, определённо у этой девочки хорошо так развита эмпатия."
            me "Да знаешь... просто я не очень хочу жаловаться другим на свою жизнь."
    sl "Да брось ты! Глупости это всё."
    play sound ds_sfx_psy
    vol "Только что ты отгородился от всего мира, а теперь изливаешь душу этой девочке."
    vol "Стоит ли продолжать?"
    window hide
    menu:
        "Продолжать":
            window show
            me "Нет, на самом деле.{w} При других обстоятельствах ты бы и не обратила на меня внимания.{w} Я ведь совсем не такой, как ты. Я ленивый, необщительный, особыми талантами не блещу."
            me "Из толпы в большом городе я бы был последним, кого ты бы заметила.{w} Впрочем, я вообще не так часто выхожу из дома."
            sl "Семён, ты меня пугаешь."
            "Она серьёзно смотрит на тебя."
            if skillcheck('composure', lvl_trivial, passive=True):
                play sound ds_sfx_mot
                com "{result}Ты смутился, но глаз не отвёл."
            else:
                play sound ds_sfx_mot
                com "{result}Ты рефлекторно отводишь взгляд."
            me "А что, я разве не прав?"
        "Прекратить":
            window show
            me "Как-то я не очень хочу об этом разговаривать."
            sl "Какой-то ты слишком... неуверенный. Я не настаиваю, но всё же тебе стоило бы поделиться. Вот увидишь: будешь легче!"
            me "Думаешь?"
            sl "Конечно!"
            me "Мне кажется, ты слишком много внимания уделяешь мне. Я же самый обычный человек. Ничем не примечательный. Разве не так?"
    sl "Конечно нет!{w} Ведь ты – это ты. Другого такого нет. Тебе надо просто чуточку уверенности в себе и терпения, и всё придёт!{w} Обязательно."
    $ ds_up_morale()
    window hide
    menu:
        "Принять":
            window show
            me "Думаешь?"
            sl "Конечно!"
            me "Ну, возможно... Возможно, я и постараюсь быть более уверенным."
            sl "Вот прямо сейчас и начнём!"
            $ ds_lp['sl'] += 1
        "Усомниться":
            window show
            me "Если бы всё было так просто…"
            sl "А ничего сложного и нет! Давай начнём прямо сейчас!"
    me "Что начнём?"
    sl "Меняться!"
    play sound ds_sfx_psy
    sug "Вот так, с ходу?"
    me "И как ты себе это представляешь?"
    sl "Надо сделать что-нибудь полезное!"
    me "Например?"
    sl "Ну…"
    "Она задумалась."
    sl "Пойдём уберёмся на площади.{w} Дискотека-то уже закончилась!"
    if ds_on_disco:
        "Оказывается, что пока вы мило беседовали со Славей, дискотека уже давно закончилась. Вы стоите посреди площади вдвоём."
    me "Вдвоём?"
    vol "Осилите ли вы с ней такой объём работы?"
    sl "Да там немного.{w} Главное – сделать первый шаг!"
    vol "Тут она права, не поспоришь, но на ночь глядя снимать гирлянды с деревьев, таскать на себе нелёгкую музыкальную аппаратуру и подметать…"
    window hide
    menu:
        "Cогласиться":
            window show
            me "Да, давай конечно! Приступим?"
            sl "Вот, правильный настрой! Быстро схватываешь!"
            $ ds_lp['sl'] += 1
            sl "Идём!"
            scene bg ext_square_night_party2
            show sl normal dress at center
            with dissolve
            "Вы присутпаете к уборке. Славя берёт на себя подметание площади, в то время как ты относишь аппаратуру и снимаешь гирлянды."
            sl "Я думаю, сейчас можно в стороне просто сложить это всё. А отнесём уже завтра!"
            me "Как скажешь."
            hide sl with dissolve
            "Впрочем, даже с указанием Слави твой труд оказывается тяжёлым. С тебя сходит семь потов."
            play sound ds_sfx_psy
            vol "Но тем не менее ты справляешься!"
            "Где-то за час вам удаётся более-менее привести площадь в порядок."
            me "Фух! Всё вроде бы!"
            show sl smile dress at center
            with dspr
            sl "Ага! Ты молодец! Вот видишь! Разве тебе не лучше становится от труда?"
            window hide
            menu:
                "Cогласиться":
                    window show
                    me "Да, тут ты и правда права!"
                    sl "Вот и хорошо!"
                "Оспорить":
                    window show
                    me "Ну, на самом деле не особо... Я чудовищно устал!"
                    sl "А... ну да, есть такое..."
            sl "Так, ладно, я побежала! А ты спать иди, поздно уже!"
            sl "Или лучше сходи помойся сначала! Баня в лесу, за умывальниками!"
            hide sl with dissolve
        "Предложить отложить на завтра":
            window show
            me "Может, завтра?{w} Вместе со всеми?"
            sl "Зачем до завтра откладывать?{w} Разве тебе не будет приятно с утра стоять на линейке на чистой площади?"
            play sound ds_sfx_psy
            vol "Ну, начнём с того, что тебе не то чтобы приятно стоять на линейке в принципе. Хоть на чистой, хоть на грязной площади."
            window hide
            menu:
                "Cказать, что это перебор":
                    window show
                    me "Слушай, я всё понимаю…{w} Но это слишком!"
                    sl "Да, пожалуй, ты прав."
                    play sound ds_sfx_psy
                    aut "И ты иногда бываешь прав!{w} А она иногда ошибается."
                    sl "Тогда…"
                    "Она потягивается и зевает."
                    sl "Пойдём спать! Утро вечера мудренее!"
                "Отвергнуть линейку":
                    window show
                    me "Да мне не то, чтобы хочется на линейке стоять..."
                    sl "Ну как так, Семён? Линейка - важная часть лагерной жизни!"
                    sl "Которую, хочешь или не хочешь, а нельзя пропускать. Или просыпать. Так что..."
                    sl "Пойдём спать! Утро вечера мудренее!"
                "Cмириться":
                    window show
                    me "Да, ты права, наверное..."
                    sl "Вот и пошли!"
                    scene bg ext_square_night_party2
                    show sl normal dress at center
                    with dissolve
                    "Вы присутпаете к уборке. Славя берёт на себя подметание площади, в то время как ты относишь аппаратуру и снимаешь гирлянды."
                    sl "Я думаю, сейчас можно в стороне просто сложить это всё. А отнесём уже завтра!"
                    me "Как скажешь."
                    hide sl with dissolve
                    "Впрочем, даже с указанием Слави твой труд оказывается тяжёлым. С тебя сходит семь потов."
                    play sound ds_sfx_psy
                    vol "Но тем не менее ты справляешься!"
                    "Где-то за час вам удаётся более-менее привести площадь в порядок."
                    me "Фух! Всё вроде бы!"
                    show sl smile dress at center
                    with dspr
                    sl "Ага! Ты молодец! Вот видишь! Разве тебе не лучше становится от труда?"
                    window hide
                    menu:
                        "Cогласиться":
                            window show
                            me "Да, тут ты и правда права!"
                            sl "Вот и хорошо!"
                        "Оспорить":
                            window show
                            me "Ну, на самом деле не особо... Я чудовищно устал!"
                            sl "А... ну да, есть такое..."
                    sl "Так, ладно, я побежала! А ты спать иди, поздно уже!"
                    sl "Или лучше сходи помойся сначала! Баня в лесу, за умывальниками!"
                    hide sl with dissolve
    window hide
    menu:
        "Согласиться":
            window show
            me "Да, пожалуй, пора бы и поспать..."
            sl "Тогда спокойной ночи, Семён! Мне приятно было провести с тобой время!"
        "{check=suggestion:12}Задержать Славю":
            window show
            me "А не рано…"
            sl "Не рано!"
            "Укоризненно возражает Славя."
            sl "Весь день потом проспишь."
            window hide
            if skillcheck('suggestion', lvl_challenging, passive=True):
                window show
                play sound ds_sfx_psy
                sug "Последний шанс - предложи проводить её до дома."
                me "Cлушай, а может я тебя до дома провожу?"
                sl "Ну... вообще, у меня есть ещё дела. Но спасибо, мне приятно!"
                $ ds_lp['sl'] += 1
                $ ds_skill_points['suggestion'] += 1
                th "Блин, не прокатило."
                sug "Но тем не менее ей понравилось."
            else:
                window show
                play sound ds_sfx_psy
                sug "Ты ляпаешь первое, что приходит в голову. Не особо удачное."
                me "Тогда расскажи мне сказку на ночь!"
                sl "Я знаю только те, что в книжках читала…{w} Ты наверняка их тоже знаешь."
                play sound ds_sfx_int
                rhe "Перевод: нет, я не собираюсь читать тебе сказки."
    sl "Пойдём? До твоего домика?"
    "Она протягивает тебе руку."
    window hide
    menu:
        "Cогласиться":
            window show
            me "Идём!"
            stop music fadeout 3

            window hide
            scene bg ext_houses_night
            show sl normal dress at center
            with dspr
            window show
            "Идёте к тебе в домик вы молча."
            play sound ds_sfx_psy
            vol "Поражение. Полное. Ты хочешь насладиться им сполна."
            th "Вот так всегда и получается – пытаешься завести нормальный разговор с девушкой, а выходит в итоге чёрти что…"
            $ ds_damage_morale()
            play sound ds_sfx_psy
            sug "Ну так кто же потратил годы своей жизни на рефлексии вместо того, чтобы учиться строить отношения?"
            th "И ничего я не тратил!"
            sug "Ну да. Тогда где твои попытки наладить {i}новые{/i} отношения? А нету их!"
            if ds_semtype >= 3:
                th "Много. Очень много. У меня столько девушек было!"
                vol "Я тебя разочарую - ни одна из них не считается. {i}One-night stand{/i} и полноценные отношения - это, как говорят в Одессе, две большие разницы. Первым ты убегал от второго."
                th "Да что за чушь?!"
            elif ds_semtype <= -3:
                th "А зачем пытаться? Ничего же не получится!"
                vol "Ну, если так думать - то конечно ничего не выйдет. Не вышло с одной - надо было дальше пробовать. И я тебе об этом говорил! Но кто же послушает?"
                th "Успокойся. Я знаю, что ничего не вышло бы. Ни тогда, ни сейчас."
            else:
                th "Я и не хотел!"
                vol "Самая тупая попытка оправдаться. Не хотел он... Уж своему сознанию-то не ври. Мы-то знаем, что хотел. Просто боялся."
                th "Отстань! И ничего я не боюсь."
            play sound ds_sfx_psy
            ine "Как бы то ни было, ты должен воспринимать своё попадание в «Совёнок» как благо. Это новый шанс для тебя. Кажется, в Славе это просматривается особо."
            $ persistent.sprite_time = "night"
            scene bg int_house_of_mt_noitem_night 
            show sl normal dress at center
            with dissolve
            "Тут оказывается, что вы со Славей уже дошли до домика."
            sl "Ну что ж, я побежала! Спокойной ночи!"
            hide sl with dissolve
        "Остаться ещё":
            window show
            me "Я ещё немного посижу, воздухом подышу."
            me "Ты иди! Спокойной ночи!"

            stop music fadeout 3

            sl "Спокойной!"
            window hide

            $ persistent.sprite_time = "night"
            scene bg ext_beach_night 
            with dissolve

            play ambience ambience_lake_shore_night fadein 3

            window show
            "Славя убегает."
            play sound ds_sfx_psy
            vol "Поражение. Полное. Ты хочешь насладиться им сполна."
            th "Вот так всегда и получается – пытаешься завести нормальный разговор с девушкой, а выходит в итоге чёрти что…"
            $ ds_damage_morale()
            "Ты уставился в ночное небо."
            "Звёзды, маленькие огоньки далёких солнц, задорно мигали, словно смеясь над тобой."
            play sound ds_sfx_psy
            sug "Ну так кто же потратил годы своей жизни на рефлексии вместо того, чтобы учиться строить отношения?"
            th "И ничего я не тратил!"
            sug "Ну да. Тогда где твои попытки наладить {i}новые{/i} отношения? А нету их!"
            if ds_semtype >= 3:
                th "Много. Очень много. У меня столько девушек было!"
                vol "Я тебя разочарую - ни одна из них не считается. {i}One-night stand{/i} и полноценные отношения - это, как говорят в Одессе, две большие разницы. Первым ты убегал от второго."
                th "Да что за чушь?!"
            elif ds_semtype <= -3:
                th "А зачем пытаться? Ничего же не получится!"
                vol "Ну, если так думать - то конечно ничего не выйдет. Не вышло с одной - надо было дальше пробовать. И я тебе об этом говорил! Но кто же послушает?"
                th "Успокойся. Я знаю, что ничего не вышло бы. Ни тогда, ни сейчас."
            else:
                th "Я и не хотел!"
                vol "Самая тупая попытка оправдаться. Не хотел он... Уж своему сознанию-то не ври. Мы-то знаем, что хотел. Просто боялся."
                th "Отстань! И ничего я не боюсь."
            play sound ds_sfx_psy
            ine "Как бы то ни было, ты должен воспринимать своё попадание в «Совёнок» как благо. Это новый шанс для тебя. Кажется, в Славе это просматривается особо."
            if not ds_on_disco:
                "Ты переворачиваешься и утыкаешься лицом в песок."
                play sound ds_sfx_fys
                edr "Не лучшая идея."
                "Ты встаёшь и, отплёвываясь, направляешься в сторону домика вожатой."
            else:
                "Ты решаешь двинуться в сторону домика Ольги Дмитриевны."
            window hide

            stop ambience fadeout 2

            scene bg black 
            with dissolve2

            window show
    play sound ds_sfx_fys
    edr "Всю дорогу дико чешется спина."
    edr "Да что там спина – всё тело."
    edr "Неудивительно – ты уже несколько дней не мылся, а днём здесь такая жара, что десять потов сойдёт."
    window hide
    menu:
        "Помыться":
            window show
        "Пойти спать":
            window show
            th "Впрочем, уже поздно. Завтра схожу помоюсь, а сейчас спать."
            edr "Тоже разумно."
            $ persistent.sprite_time = "night"
            scene bg int_house_of_mt_night2 
            with dissolve

            play ambience ambience_int_cabin_night fadein 2

            window show
            "Ольга Дмитриевна уже спит."
            "Ты не раздеваясь ложишься на кровать и накрываешься одеялом с головой."
            play sound ds_sfx_psy
            vol "Уснуть не удаётся долго – ты всё не можешь успокоиться после вечера со Славей. Ты давно так доверительно и близко не общался с девушками."
            if ds_semtype >= 3:
                vol "Так, потрахались и разбежались."
            else:
                vol "Да и вообще не общался."
            window hide

            stop ambience fadeout 2

            scene bg black 
            with fade3

            $ renpy.pause(3)
            jump ds_day3_dream
    th "Надо найти мыло, полотенце."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg int_house_of_mt_noitem_night 
    with dissolve

    play ambience ambience_camp_center_night fadein 2

    window show
    play sound ds_sfx_psy
    lgc "Всё это можно найти в домике Ольги Дмитриевны."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_square_night_party2 
    with dissolve

    window show
    "Через несколько минут ты вновь стоишь на площади с пакетиком, в котором лежат все необходимые банные принадлежности."
    th "Теперь надо найти баню."
    play sound ds_sfx_fys
    shi "Ты чувствуешь жар. Жар бани. Баня на опушке леса."
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "night"
    scene bg ext_bathhouse_night 
    with dissolve

    play ambience ambience_forest_night fadein 3

    window show
    "И правда - баня стоит на опушке леса."
    play sound ds_sfx_int
    con "Самое подходящее место для бани – прям как избушка на курьих ножках."
    con "Наверное, в ней не живёт Баба-яга, хотя свет внутри горит."
    me "И кому пришло в голову мыться в двенадцать ночи?"
    play sound ds_sfx_int
    lgc "Проблема лишь в том, кто внутри – мальчик или девочка."
    lgc "В первом случае можно ничего не бояться и спокойно помыться."
    vol "Общественные бани ты не очень любишь, но сейчас готов это пережить."
    lgc "Во втором же – тебе придётся либо ждать, либо всю ночь чесаться."
    th "А сколько ждать, непонятно…"
    play sound ds_sfx_fys
    ins "Ну, всегда можно залезть в окно. Прям к девушке! Авось и перепадёт чего!"
    window hide
    menu:
        "Просто ждать":
            window show
            "Ты располагаешься около двери и принимаешься ждать. Долго ждать."
            th "Интересно, а могло бы у меня выйти чего со Славей? Ну, отношения."
            play sound ds_sfx_psy
            vol "А почему бы нет? Во всяком случае, Славя настроена к тебе доброжелательно."
            vol "Вся проблема - ты слишком много думаешь о своих неудачах."
            play sound ds_sfx_psy
            ine "Вернее, об одной конкретной неудаче."
            th "И ничего я не думаю! Я стараюсь об этом забыть!"
            ine "Откровенно говоря, стараешься плохо. У тебя регулярно всплывают воспоминания о {i}ней{/i}."
            me "Да что вы с какой-то ней пристали ко мне?!"
            vol "Потому что тебе было бы неплохо наконец оставить прошлое в прошлом."
            ine "Вокруг тебя столько доброжелательных девушек! На любой вкус. А ты всё в неё вцепился!"
            th "Угу, особенно Двачевская доброжелательна..."
            play sound ds_sfx_psy
            emp "Ну... с ней всё немного сложнее, но всё же! Ты и без меня прекрасно всё понимаешь насчёт Алисы."
            th "В плане?"
            emp "Ты уже имел опыт общения с одной такой «Алисой». Близкого общения."
            vol "Так, всё, давайте заканчивать."
            show sl surprise pioneer at center
            with dissolve
            sl "Ой, Семён?"
            play sound ds_sfx_int
            vic "Так это Славя была в бане. И она как раз закончила мыться."
            me "Да, это я. Помыться пришёл."
            show sl smile pioneer at center
            with dissolve
            sl "Ой, тогда не смею тебя задерживать!"
            sl "Пока!"
            hide sl with dissolve
            me "Пока..."
            scene bg ds_int_bathhouse_steam
            with dissolve
            "Ты заходишь в баню, скидываешь с себя одежду и приступаешь к мытью."
            "После Слави тут остался пар, так что разжигать баню дополнительно не требуется."
            play sound ds_sfx_fys
            ins "Такой шанс упустил... Вот бы тут со Славей того..."
            play sound ds_sfx_fys
            edr "Шанс окочуриться? Секс в бане - идея очень плохая. Слишком велики нагрузки."
            ins "Да ну тебя, зануда!"
            "Ты заканчиваешь мыться и идёшь к себе домой."

            $ persistent.sprite_time = "night"
            scene bg ext_bathhouse_night 
            with dissolve

            play ambience ambience_forest_night fadein 3

            window show
            play sound ds_sfx_int
            con "Ночь как будто устроила собственную дискотеку, или скорее бал.{w} Звёзды – свет софитов; птицы и насекомые – настоящий оркестр, а ухающая вдалеке сова – дирижёр; ветер шумит в густых кронах высоких деревьев – аплодируют зрители."
            play sound ds_sfx_fys
            edr "И ещё прекраснее ночь кажется, когда стоишь в лесу, чистый и свежий."
            window hide

            play sound sfx_bush_leaves

            $ renpy.pause(1)

            window show
            play sound ds_sfx_mot
            per_hea "Внезапно в нескольких метрах от меня слышится шелест кустов."
            play sound ds_sfx_fys
            hfl "Ты вздрогнул, но особо не испугался."
            play sound ds_sfx_int
            lgc "Может быть, это просто белка или ещё какое животное."
            hfl "Однако стоит проверить."
            window hide
            menu:
                "Проверить":
                    window show
                    "Ты подходишь к кустам."
                    "Но ничего (и никого) подозрительного найти не удаётся."
                    th "Наверное, показалось..."
                "Проигнорировать":
                    window show
            "Чистый телом и умиротворённый духом я направился к домику вожатой."
            window hide

            stop ambience fadeout 2

            $ persistent.sprite_time = "night"
            scene bg int_house_of_mt_night2 
            with dissolve

            play ambience ambience_int_cabin_night fadein 2

            window show
            "Ольга Дмитриевна уже спит."
            "Ты не раздеваясь лёг на кровать и накрылся одеялом с головой."
            play sound ds_sfx_psy
            ine "Уснуть не удаётся долго – у тебя перед глазами стоит образ Слави в бане, голой, само собой."
            window hide

            stop ambience fadeout 2

            scene bg black 
            with fade3

            $ renpy.pause(3)
            jump ds_day3_dream
        "Заглянуть в окно":
            window show
            "Ты заглядываешь в окно.{w} Внутри ничего не видно из-за пара."

            stop ambience fadeout 2

            "И вдруг буквально в паре метров от меня словно из густого тумана выныривает Славя."
            window hide

            scene cg ds_day3_sl_bath 
            with dissolve

            play music music_list["eternal_longing"] fadein 2

            window show
            "Естественно, как и диктуют правила поведения в банях, голая."
            "Ты тупо уставился на неё."
            play sound ds_sfx_fys
            ins "Само собой, твой организм быстро отозвался."
            ins "Нервные импульсы от глаз через мозг спускаются ниже."
            vol "Кажется, ты уже вряд ли сойдёшь со своего наблюдательного пункта, даже если начнётся война."
            "Славя тебя как будто бы не замечает."
            "Она неспешно моется – ополаскивает голову, растирает тело мочалкой и обливается водой из ведра."
            "Затем настаёт черёд её длинных волос."
            play sound ds_sfx_int
            vic "Сколько времени нужно, чтобы промыть их полностью? Явно очень много."
            vol "Но для тебя минуты кажутся мгновениями – настолько не хочется оттуда уходить."
            window hide

            with fade

            window show
            "Наконец Славя заканчивает, удовлетворённо вздыхает и направляется к двери."

            stop music fadeout 3

            "Она выходит в предбанник."
            play sound ds_sfx_fys
            hfl "Тебе бы спрятаться. Вряд ли Славя обрадуется тому, что ты за ней наблюдал."
            window hide

            $ persistent.sprite_time = "night"
            scene bg ext_bathhouse_night 
            with dissolve

            play ambience ambience_forest_night fadein 3

            menu:
                "Cпрятаться в кустах":
                    "Ты покидаешь свой наблюдательный пост и прячешься в кустах неподалёку."
                    show sl normal pioneer far at center   with dissolve   
                    "Через секунду показывается Славя, некоторое время стоит на крыльце, видимо наслаждаясь ночной свежестью, и направляется в сторону твоего укрытия."
                    hfl "И как оправдываться будем?"
                    window hide
                    menu:
                        "Сидеть дальше":
                            window show
                            "Но она проходит мимо, даже не посмотрев на кусты, в которых ты сидишь."
                            hide sl  with dissolve
                            th "Кажется, пронесло..."
                        "Выскочить и оправдываться":
                            window show
                            show sl surprise pioneer at center
                            with dspr
                            "Ты выскакиваешь из кустов и начинаешь оправдываться перед Славей."
                            me "Я ничего не делал! Я совершенно точно не подглядывал! Просто ждал своей очереди!"
                            sl "Я не очень понимаю, о чём ты, Семён..."
                            me "О том! Не думай, что я изврат какой! Я просто сидел и ждал!"
                            sl "Я ничего такого о тебе и не думала... Но ладно, буду знать."
                            play sound ds_sfx_mot
                            res "Кажется, ты немного поспешил."
                            sl "Cпокойной ночи, Семён."
                            hide sl with dissolve
                    stop ambience fadeout 2

                    window hide
                    menu:
                        "Пойти помыться":
                            window show
                            "Ты, отойдя от произошедшего, заходишь в баню."
                            scene bg ds_int_bathhouse_steam
                            with dissolve
                            "Ты скидываешь с себя одежду и приступаешь к мытью."
                            "После Слави тут остался пар, так что разжигать баню дополнительно не требуется."
                            play sound ds_sfx_fys
                            ins "Такой шанс упустил... Вот бы тут со Славей того..."
                            play sound ds_sfx_fys
                            edr "Шанс окочуриться? Секс в бане - идея очень плохая. Слишком велики нагрузки."
                            ins "Да ну тебя, зануда!"
                            "Ты заканчиваешь мыться и идёшь к себе домой."

                            $ persistent.sprite_time = "night"
                            scene bg ext_bathhouse_night 
                            with dissolve

                            play ambience ambience_forest_night fadein 3

                            window show
                            play sound ds_sfx_int
                            con "Ночь как будто устроила собственную дискотеку, или скорее бал.{w} Звёзды – свет софитов; птицы и насекомые – настоящий оркестр, а ухающая вдалеке сова – дирижёр; ветер шумит в густых кронах высоких деревьев – аплодируют зрители."
                            play sound ds_sfx_fys
                            edr "И ещё прекраснее ночь кажется, когда стоишь в лесу, чистый и свежий."
                            window hide

                            play sound sfx_bush_leaves

                            $ renpy.pause(1)

                            window show
                            play sound ds_sfx_mot
                            per_hea "Внезапно в нескольких метрах от меня слышится шелест кустов."
                            play sound ds_sfx_fys
                            hfl "Ты вздрогнул, но особо не испугался."
                            play sound ds_sfx_int
                            lgc "Может быть, это просто белка или ещё какое животное."
                            hfl "Однако стоит проверить."
                            window hide
                            menu:
                                "Проверить":
                                    window show
                                    "Ты подходишь к кустам."
                                    "Но ничего (и никого) подозрительного найти не удаётся."
                                    th "Наверное, показалось..."
                                "Проигнорировать":
                                    window show
                            "Чистый телом и умиротворённый духом я направился к домику вожатой."
                            window hide

                            stop ambience fadeout 2

                            $ persistent.sprite_time = "night"
                            scene bg int_house_of_mt_night2 
                            with dissolve

                            play ambience ambience_int_cabin_night fadein 2

                            window show
                            "Ольга Дмитриевна уже спит."
                            "Ты не раздеваясь лёг на кровать и накрылся одеялом с головой."
                            play sound ds_sfx_psy
                            ine "Уснуть не удаётся долго – у тебя перед глазами стоит образ Слави в бане, голой, само собой."
                            window hide

                            stop ambience fadeout 2

                            scene bg black 
                            with fade3

                            $ renpy.pause(3)
                            jump ds_day3_dream
                        "Пойти к себе":
                            window show
                            "Ты осторожно, стараясь не шуметь, вылезаешь и направляешься к домику Ольги Дмитриевны."
                "Сбежать":
                    window show
                    "Ты максимально осторожно удаляешься в лес, стараясь, чтобы Славя тебя не заметила."
                "Продолжать ждать":
                    window show
                    "Ты продолжаешь стоять там, где стоял."
                    show sl surprise pioneer at center
                    with dissolve
                    sl "Ой, Семён, что ты тут делаешь?"
                    window hide
                    menu:
                        "Просто жду":
                            window show
                            me "Да так, пришёл помыться, вот и жду очереди. Кажется, она настала."
                            show sl smile pioneer at center
                            with dspr
                            sl "А, давай тогда! Спокойной ночи!"
                            me "Спокойной ночи."
                            hide sl with dissolve
                        "Смотрю за тобой":
                            window show
                            me "Да так, не удержался и посмотрел за тобой в бане! Классная фигура, кстати!"
                            "Cлавя удивилась не то твоей наглости, не то твоей честности."
                            sl "Э... ну... я рада, что тебе понравилось."
                            show sl normal pioneer at center
                            with dspr
                            sl "А хочешь ещё посмотреть?"
                            if skillcheck('half_light', lvl_trivial, passive=True):
                                play sound ds_sfx_fys
                                hfl "{result}Кэп подсказывает, что это попытка тебя поймать."
                            window hide
                            menu:
                                "Принять":
                                    window show
                                    me "Да, давай!"
                                    play sound sfx_face_slap
                                    with hpunch
                                    show sl angry pioneer at center
                                    with dspr
                                    sl "А может, тебе и отдаться сразу прям тут? Не обнаглели ли вы малость, товарищ Пёрсунов?"
                                    $ ds_lp['sl'] -= 1
                                    play sound ds_sfx_fys
                                    pat "Она могла этого и не говорить - боль от пощёчины тут красноречивее слов."
                                    $ ds_damage_health()
                                "Отклонить":
                                    window show
                                    me "Нет, пожалуй, откажусь..."
                                    show sl serious pioneer at center
                                    with dspr
                                    sl "Вот и подглядывать не надо!"
                            sl "Пока."
                            hide sl with dissolve
                    window hide
                    menu:
                        "Пойти помыться":
                            window show
                            "Ты, отойдя от произошедшего, заходишь в баню."
                            scene bg ds_int_bathhouse_steam
                            with dissolve
                            "Ты скидываешь с себя одежду и приступаешь к мытью."
                            "После Слави тут остался пар, так что разжигать баню дополнительно не требуется."
                            play sound ds_sfx_fys
                            ins "Такой шанс упустил... Вот бы тут со Славей того..."
                            play sound ds_sfx_fys
                            edr "Шанс окочуриться? Секс в бане - идея очень плохая. Слишком велики нагрузки."
                            ins "Да ну тебя, зануда!"
                            "Ты заканчиваешь мыться и идёшь к себе домой."

                            $ persistent.sprite_time = "night"
                            scene bg ext_bathhouse_night 
                            with dissolve

                            play ambience ambience_forest_night fadein 3

                            window show
                            play sound ds_sfx_int
                            con "Ночь как будто устроила собственную дискотеку, или скорее бал.{w} Звёзды – свет софитов; птицы и насекомые – настоящий оркестр, а ухающая вдалеке сова – дирижёр; ветер шумит в густых кронах высоких деревьев – аплодируют зрители."
                            play sound ds_sfx_fys
                            edr "И ещё прекраснее ночь кажется, когда стоишь в лесу, чистый и свежий."
                            window hide

                            play sound sfx_bush_leaves

                            $ renpy.pause(1)

                            window show
                            play sound ds_sfx_mot
                            per_hea "Внезапно в нескольких метрах от меня слышится шелест кустов."
                            play sound ds_sfx_fys
                            hfl "Ты вздрогнул, но особо не испугался."
                            play sound ds_sfx_int
                            lgc "Может быть, это просто белка или ещё какое животное."
                            hfl "Однако стоит проверить."
                            window hide
                            menu:
                                "Проверить":
                                    window show
                                    "Ты подходишь к кустам."
                                    "Но ничего (и никого) подозрительного найти не удаётся."
                                    th "Наверное, показалось..."
                                "Проигнорировать":
                                    window show
                            "Чистый телом и умиротворённый духом я направился к домику вожатой."
                            window hide

                            stop ambience fadeout 2

                            $ persistent.sprite_time = "night"
                            scene bg int_house_of_mt_night2 
                            with dissolve

                            play ambience ambience_int_cabin_night fadein 2

                            window show
                            "Ольга Дмитриевна уже спит."
                            "Ты не раздеваясь лёг на кровать и накрылся одеялом с головой."
                            play sound ds_sfx_psy
                            ine "Уснуть не удаётся долго – у тебя перед глазами стоит образ Слави в бане, голой, само собой."
                            window hide

                            stop ambience fadeout 2

                            scene bg black 
                            with fade3

                            $ renpy.pause(3)
                            jump ds_day3_dream
                        "Пойти к себе":
                            window show
                            "Ты осторожно, стараясь не шуметь, вылезаешь и направляешься к домику Ольги Дмитриевны."
        "Зайти в баню":
            window show
            "Ты открываешь дверь в баню - да, её не закрыли."
            "И вдруг буквально в паре метров от тебя словно из густого тумана выныривает Славя."
            window hide

            scene cg ds_day3_sl_bath 
            with dissolve

            play music music_list["eternal_longing"] fadein 2

            window show
            "Естественно, как и диктуют правила поведения в банях, голая."
            "Ты тупо уставился на неё."
            sl "Cемён?!"
            window hide
            menu:
                "Извиниться и уйти":
                    window show
                    me "Ой... я тут... я не хотел тебе мешать!"
                    "И ты выходишь."
                "{check=instinct:6}Начать приставать":
                    if skillcheck('instinct', lvl_trivial):
                        window show
                        ins "{result}Такой шанс! Не упусти его!"
                        ins "Само собой, твой организм быстро отозвался."
                        ins "Нервные импульсы от глаз через мозг спускаются ниже."
                        me "Знаешь, у тебя такое... прекрасное тело!"
                        me "Мне так хочется {i}тебя{/i}."
                        sl "Слушай, я всё понимаю, но я сюда помыться пришла. Будь добр, выйди, пожалуйста."
                        me "Ладно..."
                    else:
                        window show
                        ins "{result}Тебе настолько неловко, что даже в столь пикантной ситуации тело не откликается."
                    $ ds_skill_points['instinct'] += 1
                    "И ты выходишь."
                "Изнасиловать Славю":
                    window show
                    me "Я тут подумал... что хочу тебя! И возьму!"
                    sl "Ой..."
                    "Ты накидываешься на неё и бросаешь на пол. Раздевшись, ты приступаешь к делу."
                    scene black with dissolve2
                    jump ds_end_sl_rape
                "Начать располагаться":
                    window show
                    "Ты начинаешь как ни в чём не бывало раздеваться."
                    sl "Cемён? Может, дашь мне помыться?"
                    me "Давай вместе помоемся. Что такого?"
                    sl "Ничего, не считая того, что я бы хотела побыть наедине с собой."
                    me "А побудешь наедине со мной!"
                    $ ds_lp['sl'] -= 1
                    sl "На выход!"
                    "C этими словами она буквально выпихивает тебя из бани."
                    me "Ну Славя..."
                    sl "Жди тут!"
            stop music fadeout 3
            scene bg ext_bathhouse_night
            with dissolve
            window hide
            menu:
                "Сбежать":
                    window show
                    "Ты максимально осторожно удаляешься в лес, стараясь, чтобы Славя тебя не заметила."
                "Продолжать ждать":
                    window show
                    "Ты продолжаешь стоять там, где стоял."
                    show sl surprise pioneer at center
                    with dissolve
                    sl "Ой, Семён, что ты тут делаешь?"
                    window hide
                    menu:
                        "Просто жду":
                            window show
                            me "Да так, пришёл помыться, вот и жду очереди. Кажется, она настала."
                            show sl smile pioneer at center
                            with dspr
                            sl "А, давай тогда! Спокойной ночи!"
                            me "Спокойной ночи."
                            hide sl with dissolve
                        "Смотрю за тобой":
                            window show
                            me "Да так, не удержался и посмотрел за тобой в бане! Классная фигура, кстати!"
                            "Cлавя удивилась не то твоей наглости, не то твоей честности."
                            sl "Э... ну... я рада, что тебе понравилось."
                            show sl normal pioneer at center
                            with dspr
                            sl "А хочешь ещё посмотреть?"
                            if skillcheck('half_light', lvl_trivial, passive=True):
                                play sound ds_sfx_fys
                                hfl "{result}Кэп подсказывает, что это попытка тебя поймать."
                            window hide
                            menu:
                                "Принять":
                                    window show
                                    me "Да, давай!"
                                    play sound sfx_face_slap
                                    with hpunch
                                    show sl angry pioneer at center
                                    with dspr
                                    sl "А может, тебе и отдаться сразу прям тут? Не обнаглели ли вы малость, товарищ Пёрсунов?"
                                    $ ds_lp['sl'] -= 1
                                    play sound ds_sfx_fys
                                    pat "Она могла этого и не говорить - боль от пощёчины тут красноречивее слов."
                                    $ ds_damage_health()
                                "Отклонить":
                                    window show
                                    me "Нет, пожалуй, откажусь..."
                                    show sl serious pioneer at center
                                    with dspr
                                    sl "Вот и подглядывать не надо!"
                            sl "Пока."
                            hide sl with dissolve
                    window hide
                    menu:
                        "Пойти помыться":
                            window show
                            "Ты, отойдя от произошедшего, заходишь в баню."
                            scene bg ds_int_bathhouse_steam
                            with dissolve
                            "Ты скидываешь с себя одежду и приступаешь к мытью."
                            "После Слави тут остался пар, так что разжигать баню дополнительно не требуется."
                            play sound ds_sfx_fys
                            ins "Такой шанс упустил... Вот бы тут со Славей того..."
                            play sound ds_sfx_fys
                            edr "Шанс окочуриться? Секс в бане - идея очень плохая. Слишком велики нагрузки."
                            ins "Да ну тебя, зануда!"
                            "Ты заканчиваешь мыться и идёшь к себе домой."

                            $ persistent.sprite_time = "night"
                            scene bg ext_bathhouse_night 
                            with dissolve

                            play ambience ambience_forest_night fadein 3

                            window show
                            play sound ds_sfx_int
                            con "Ночь как будто устроила собственную дискотеку, или скорее бал.{w} Звёзды – свет софитов; птицы и насекомые – настоящий оркестр, а ухающая вдалеке сова – дирижёр; ветер шумит в густых кронах высоких деревьев – аплодируют зрители."
                            play sound ds_sfx_fys
                            edr "И ещё прекраснее ночь кажется, когда стоишь в лесу, чистый и свежий."
                            window hide

                            play sound sfx_bush_leaves

                            $ renpy.pause(1)

                            window show
                            play sound ds_sfx_mot
                            per_hea "Внезапно в нескольких метрах от меня слышится шелест кустов."
                            play sound ds_sfx_fys
                            hfl "Ты вздрогнул, но особо не испугался."
                            play sound ds_sfx_int
                            lgc "Может быть, это просто белка или ещё какое животное."
                            hfl "Однако стоит проверить."
                            window hide
                            menu:
                                "Проверить":
                                    window show
                                    "Ты подходишь к кустам."
                                    "Но ничего (и никого) подозрительного найти не удаётся."
                                    th "Наверное, показалось..."
                                "Проигнорировать":
                                    window show
                            "Чистый телом и умиротворённый духом я направился к домику вожатой."
                            window hide

                            stop ambience fadeout 2

                            $ persistent.sprite_time = "night"
                            scene bg int_house_of_mt_night2 
                            with dissolve

                            play ambience ambience_int_cabin_night fadein 2

                            window show
                            "Ольга Дмитриевна уже спит."
                            "Ты не раздеваясь лёг на кровать и накрылся одеялом с головой."
                            play sound ds_sfx_psy
                            ine "Уснуть не удаётся долго – у тебя перед глазами стоит образ Слави в бане, голой, само собой."
                            window hide

                            stop ambience fadeout 2

                            scene bg black 
                            with fade3

                            $ renpy.pause(3)
                            jump ds_day3_dream
                        "Пойти к себе":
                            window show
                            "Ты осторожно, стараясь не шуметь, вылезаешь и направляешься к домику Ольги Дмитриевны."

    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_square_night_party2 
    with dissolve

    play ambience ambience_camp_center_night fadein 3

    window show
    play sound ds_sfx_fys
    edr "Тебя одолевает сильная усталость – хочется лишь поскорее плюхнуться в кровать и отключиться."
    edr "Однако глаза ждать не планируют, то и дело закрываясь."
    play sound ds_sfx_fys
    hfl "Опасно даже моргать."
    hfl "В конце концов, ты ещё не настолько хорошо знаешь лагерь, чтобы ходить по нему вслепую."
    "Ты преднамеренно ходишь не по кратчайшему маршруту, стараясь минимизировать вероятность встречи со Славей."
    window hide

    with fade

    show sl normal pioneer at center   with dissolve

    window show
    "Однако..."
    "Вдруг словно из-под земли перед тобой возникает Славя."
    sl "Спать идёшь?"
    me "Ну... да..."
    if not skillcheck('composure', lvl_formidable, passive=True):
        play sound ds_sfx_mot
        com "{result}Тут же вспоминается зрелище в бане, и ты стыдливо отводишь взгляд."
    window hide
    menu:
        "Cпросить про Славю":
            window show
            me "А ты?"
            show sl smile pioneer  with dspr
            sl "А я вот порядок навожу!"
            "Она достаёт из-за спины метлу."
            play sound ds_sfx_psy
            ine "Ночью, посреди пустой площади, с метлой Славя похожа на колдунью из детских сказок."
            show sl surprise pioneer  with dspr
            sl "Что?"
            window hide
            menu:
                "Принять":
                    window show
                    me "Ничего."
                "Усомниться":
                    window show
                    me "Да ничего.{w} Думаешь, стоит после бани убираться?"

                    play music music_list["awakening_power"] fadein 2

                    sl "А откуда ты знаешь, что я в бане была?"
                    play sound ds_sfx_fys
                    hfl "Ты буквально физически чувствуешь страх, по спине бежит холодный пот, а мысли словно останавливаются, не позволяя придумать ни одного хоть сколь-нибудь правдоподобного оправдания."
                    "Славя всё так же удивлённо, непонимающе смотрит на тебя."
                    play sound ds_sfx_psy
                    vol "Кажется, что от ответа сейчас зависит твоя жизнь."
                    if skillcheck('visual_calculus', lvl_up_medium, passive=True):
                        play sound ds_sfx_int
                        vic "{result}Спокойствие, только спокойствие! У неё мокрые волосы, а по этому нетрудно установить, что она была в бане."
                        me "Ну, у тебя волосы мокрые..."
                        show sl smile2 pioneer  with dspr
                        sl "И правда."
                    else:
                        me "Ну... я шёл помыться, увидел, что ты заходишь, и ушёл."
                        show sl smile2 pioneer  with dspr
                        sl "А, ну бывает!"
                    vol "Тебе хочется провалиться под землю, исчезнуть из этого мира так же внезапно и необратимо, как исчез из {i}своего{/i}."
            sl "А ты тоже мыться пойдёшь?"
        "Промолчать":
            window show
            sl "Но ты же сначала мыться пойдёшь, правда?"
    me "Я... эээ..."
    "Славя смотрит на пакет у тебя в руках."
    window hide
    menu:
        "Подтвердить":
            window show
            me "Да, да! Так что спокойной ночи!"
            show sl surprise pioneer  with dspr

            stop ambience fadeout 2

            stop music fadeout 3

            "Я развернулся и быстрыми шагами направился назад к бане."
            window hide
        "Отвергнуть":
            window show
            me "Нет. Пожалуй, я пойду спать. Спокойной ночи!"
            show sl surprise pioneer  with dspr

            stop ambience fadeout 2

            stop music fadeout 3

            "Я развернулся и быстрыми шагами направился в сторону своего домика."
            scene bg ext_houses_night
            with dissolve
            window hide
            menu:
                "Сходить в баню":
                    window show
                    "А затем ты разворачиваешься и, стараясь обойти Славю, идёшь в баню."
                "Пойти домой":
                    scene bg ext_house_of_mt_night
                    with dissolve

                    "Ты подходишь к домику Ольги Дмитриевны. Тихо заходишь в него."

                    stop ambience fadeout 2

                    $ persistent.sprite_time = "night"
                    scene bg int_house_of_mt_night2 
                    with dissolve

                    play ambience ambience_int_cabin_night fadein 2

                    window show
                    "Ольга Дмитриевна уже спит."
                    "Ты не раздеваясь лёг на кровать и накрылся одеялом с головой."
                    play sound ds_sfx_psy
                    ine "Уснуть не удаётся долго – у тебя перед глазами стоит образ Слави в бане, голой, само собой."
                    window hide

                    stop ambience fadeout 2

                    scene bg black 
                    with fade3

                    $ renpy.pause(3)
                    jump ds_day3_dream

    $ persistent.sprite_time = "night"
    scene bg ext_bathhouse_night 
    with dissolve

    play ambience ambience_forest_night fadein 3

    window show
    th "Какой кошмар, какой позор..."
    play sound ds_sfx_psy
    vol "Идёшь ты медленно, стараясь как можно сильнее обругать себя за всё случившееся."
    th "Во-первых, не надо подглядывать."
    play sound ds_sfx_int
    dra "Но раз уж подглядывал, то потом надо быть внимательнее, заранее придумать оправдание хотя бы."

    stop ambience fadeout 2

    th "Эх..."
    window hide

    scene black 
    with dissolve

    window show
    "Помылся ты быстро."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_bathhouse_night 
    with dissolve

    play ambience ambience_forest_night fadein 3

    window show
    play sound ds_sfx_int
    con "Ночь как будто устроила собственную дискотеку, или скорее бал.{w} Звёзды – свет софитов; птицы и насекомые – настоящий оркестр, а ухающая вдалеке сова – дирижёр; ветер шумит в густых кронах высоких деревьев – аплодируют зрители."
    play sound ds_sfx_fys
    edr "И ещё прекраснее ночь кажется, когда стоишь в лесу, чистый и свежий."
    window hide

    play sound sfx_bush_leaves

    $ renpy.pause(1)

    window show
    play sound ds_sfx_mot
    per_hea "Внезапно в нескольких метрах от меня слышится шелест кустов."
    play sound ds_sfx_fys
    hfl "Ты вздрогнул, но особо не испугался."
    play sound ds_sfx_int
    lgc "Может быть, это просто белка или ещё какое животное."
    hfl "Однако стоит проверить."
    window hide
    menu:
        "Проверить":
            window show
            "Ты подходишь к кустам."
            "Но ничего (и никого) подозрительного найти не удаётся."
            th "Наверное, показалось..."
        "Проигнорировать":
            window show
    "Чистый телом и умиротворённый духом я направился к домику вожатой."
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "night"
    scene bg int_house_of_mt_night2 
    with dissolve

    play ambience ambience_int_cabin_night fadein 2

    window show
    "Ольга Дмитриевна уже спит."
    "Ты не раздеваясь лёг на кровать и накрылся одеялом с головой."
    play sound ds_sfx_psy
    ine "Уснуть не удаётся долго – у тебя перед глазами стоит образ Слави в бане, голой, само собой."
    window hide

    stop ambience fadeout 2

    scene bg black 
    with fade3

    $ renpy.pause(3)
    jump ds_day3_dream

label ds_day3_dance_un:
    $ ds_day3_evening_who = 'un'
    $ ds_lp['un'] += 2
    "Легко сказать. Лена оказывается не особо расположенной к танцам."
    play sound ds_sfx_psy
    emp "Вернее сказать, она слишком зажата. У неё не получается двигаться достаточно плавно и свободно."
    play sound ds_sfx_psy
    vol "И что хуже всего - это зажатость передаётся и тебе."
    show un shy dress at center
    with dspr
    "Наконец, Лена отходит от тебя. Она разочарована неудачей."
    un "Слушай... давай в медпункт пойдём..."
    window hide
    menu:
        "Согласиться":
            window show
            me "Да, давай."
            jump ds_day3_un_medic
        "{check=suggestion:14}Настоять на танцах":
            if skillcheck('suggestion', lvl_legendary):
                play sound ds_sfx_psy
                sug "{result}Убеди Лену, что всё получится с танцами."
                me "Не беспокойся. Всё у тебя получится с танцами."
                show un normal dress at center
                with dspr
                un "Думаешь?"
                me "Ну конечно!"
                un "Ладно..."
            else:
                play sound ds_sfx_psy
                sug "{result}Нет, Лена не хочет танцевать. Она хочет в медпункт."
                me "Точно не будешь танцевать дальше?"
                un "Не-а."
                me "Ладно, пойдём с тобой тогда..."
                jump ds_day3_un_medic
        "Отказаться":
            window show
            me "Так, нет, либо танцуем - либо иди сама!"
            show un sad dress at center
            with dspr
            un "Ладно... я пойду..."
            $ ds_lp['un'] -= 1
            hide un with dissolve
            play sound ds_sfx_psy
            emp "Зачем так грубо было-то?"
            jump ds_day3_evening_none
    scene cg ds_day3_dance_un
    with dissolve
    "Ты начинаешь тщательно показывать Лене каждое движение. Стараешься её подбодрить. Делаешь всё, чтобы у неё получилось."
    "К концу третьего трека тебе удаётся частично преодолеть зажатость Лены и более-менее уверенно станцевать вальс."
    scene bg ext_square_night_party
    show un normal dress at center
    with dspr
    mt "Дискотека окончена!"
    th "Да как так?!"
    if skillcheck('suggestion', lvl_medium, passive=True):
        play sound ds_sfx_psy
        sug "{result}Вы всегда можете продолжить. Скажем, на пристани."
        window hide
        menu:
            "Предложить":
                window show
                me "Давай, если ты не против, на пристани ещё потанцуем? Если ты не против, конечно."
                show un surprise dress at center
                with dspr
                un "Нет... не против..."
                $ ds_lp['un'] += 1
                jump ds_day3_dance_un_beach
            "Отбросить мысль":
                window show
                th "Да нет, я уже устал танцевать как-то..."
    un "Спасибо за танцы..."
    $ ds_lp['un'] += 1
    hide un with dissolve
    "И она убегает прежде, чем ты успеваешь что-либо сказать."
    th "Ладно..."
    window show
    "Ты направляешься к домику вожатой."
    play sound ds_sfx_fys
    hfl "Весь лагерь спит, так что вряд ли тебя может кто-то заметить."
    th "Да и что с того?{w} Ну гуляет пионер ночью один – эка невидаль!"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_house_of_mt_night 
    with dissolve

    play sound sfx_bush_leaves

    window show
    "Когда ты уже почти дошёл до двери, сзади слышится шорох."
    "Ветки кустов рядом с деревом позади тебя шуршат, словно в них кто-то запрыгнул."
    play sound ds_sfx_fys
    hfl "Диких животных здесь вроде как не водится…"
    hfl "Значит, кто-то следил за тобой!"
    window hide
    menu:
        "Проверить":
            window show
            "В то же мгновение ты бросаешься на звук, продираешься сквозь кусты и начинаешь озираться по сторонам."
            play sound ds_sfx_mot
            per_eye "Слишком темно, и ничего и, главное, никого в такой темноте не увидеть."
            play sound ds_sfx_int
            lgc "Идти дальше бессмысленно – если даже за тобой кто-то и следил, он уже давно убежал."
            "Ты возвращаешься к домику."
        "Забить":
            window show
            "Ты продолжаешь идти в сторону домика."
    "В окне горит свет."
    th "Значит, она ещё не спит."

    stop ambience fadeout 2

    window hide

    play sound sfx_open_dooor_campus_2

    pause(1)

    scene bg int_house_of_mt_night2 
    with dissolve2

    window show
    th "Сегодня был трудный во всех смыслах день."
    play sound ds_sfx_psy
    vol "Ты слишком устал, чтобы размышлять о произошедшем вечером, да и вряд ли в голову пришло бы что-то путное…"
    th "И главное – совершенно непонятно, как на всё это реагировать."
    th "На Лену, на лагерь, на весь этот мир..."
    play sound ds_sfx_psy
    sug "И Лена...{w} Время, проведённое с ней, было куда важнее для тебя, чем все попытки вернуться в {i}реальный{/i} мир."
    play sound ds_sfx_fys
    edr "Ты бы мог ещё долго накручивать себя, пытаясь понять, что же сделал не так, а что не сделал вообще, но усталость взяла своё..."
    window hide

    stop music fadeout 3

    scene black 
    with fade3

    $ renpy.pause(3)

    jump ds_day3_dream

label ds_day3_un_medic:
    $ persistent.sprite_time = "night"
    scene bg ext_dining_hall_away_night 
    with dissolve

    play music music_list["goodbye_home_shores"] fadein 3

    show un normal dress at center   with dissolve
    window show
    un "Ну что, пойдём в медпункт?"
    "Лена выводит тебя из раздумий."
    "Вы уже некоторое время просто молча стоите возле столовой."
    window hide
    menu:
        "Поблагодарить":
            window show
            me "Да, конечно… Спасибо тебе!"
            show un surprise dress at center   with dspr
            un "За что?"
            "Она посмотрела на меня с удивлением."
            me "Ну, за то, что забрала меня…"
            "Может быть, и не стоило говорить ей о том, что танцы – не мой конёк."
            me "А то там…{w} знаешь, так скучно!"
            show un normal dress at center   with dspr
            un "Ты не любишь танцевать, наверное?"
            "На её искреннем, немного даже детском лице не промелькнуло и тени сарказма."
            "Она, похоже, действительно не понимала."
            me "Да, совсем не люблю, не моё это как-то."
            show un shy dress at center   with dspr
            if ds_day3_evening_who == 'un':
                un "И я тоже.{w} Ты первый, кто меня пригласил."
            else:
                un "И я тоже.{w} Меня никогда никто не приглашает."
        "Молча пойти":
            window show
            "Вы выдвигаетесь."
            show un shy dress at center
            with dspr
            un "Знаешь, честно говоря, я не очень люблю танцевать."
            if ds_day3_evening_who == 'un':
                un "Ты первый, кто меня пригласил."
            else:
                un "Меня никогда никто не приглашает."
    "Сказав это, Лена краснеет и привычно уставляется себе под ноги."
    window hide
    menu:
        "Промолчать":
            window show
        "Усомниться":
            window show
            me "Странно."
            un "Что странно?"
            me "Ну… Что тебя не приглашают."
            show un surprise dress at center   with dspr
            un "Ты так думаешь?"
            "Она смотрит на тебя взглядом, полным искреннего непонимания и удивления."
            if ds_day3_evening_who == None:
                if skillcheck('rhetoric', lvl_medium, passive=True):
                    play sound ds_sfx_int
                    rhe "{result}Эффектным ходом будет сказать, что ты бы её пригласил."
                    window hide
                    menu:
                        "Cказать, что пригласил бы её":
                            window show
                            me "Ну, да! Конечно!{w} Если бы я любил танцевать, то обязательно бы тебя пригласил."
                            show un shy dress at center   with dspr

                            stop music fadeout 2

                            un "Спасибо…"
                            $ ds_lp['un'] += 1
                        "Просто подтвердить":
                            window show
                            me "Ну да..."
                else:
                    me "Ну да..."
    window hide

    $ ds_day3_evening_who = 'un'
    $ persistent.sprite_time = "night"
    scene bg ext_aidpost_night 
    with dissolve

    play ambience ambience_camp_center_night fadein 3

    window show
    "Остальную часть пути вы идёте молча."
    "Лена, очевидно, слишком смутилась от разговора, а ты просто не знаешь, что сказать, какую тему придумать для разговора."
    play sound ds_sfx_int
    con "Уже полностью стемнело, и мрачное здание медпункта, окутанное ночным туманом, больше походит на дом с привидениями."
    vol "Тебе вдруг захотелось развернуться и медленно, не создавая лишнего шума, уйти отсюда."
    window hide
    menu:
        "{check=savoir_faire:16}Уйти":
            if skillcheck('savoir_faire', lvl_godly):
                window show
                hide un with dissolve
                play sound ds_sfx_mot
                svf "{result}Тебе удаётся прошмыгнуть в ближайшие кусты, не привлекая внимание Лены."
                $ ds_lp['un'] -= 3
                $ ds_skill_points['savoir_faire'] += 1
                jump ds_day3_evening_none
            else:
                window show
                play sound ds_sfx_mot
                svf "{result}Ты направляешься в сторону ближайших кустов..."
                show un surprise dress at center
                with dissolve
                un "Ты куда, Семён?"
                me "Да так, никуда..."
                $ ds_skill_points['savoir_faire'] += 1
        "Идти дальше":
            window show

            show un normal dress at center   with dissolve
            "Ты украдкой бросаешь взгляд на Лену."
            play sound ds_sfx_psy
            emp "Она выглядит как обычно – застенчивой, скромной, неуверенной в себе, но никак не испуганной."
            play sound ds_sfx_psy
            aut "Тем больше тебе стало не по себе."
            aut "Да как это так – она не боится, а я..."

    play sound sfx_owl_far
    play sound2 ds_sfx_mot
    per_hea "Внезапно где-то рядом слышится уханье совы"
    play sound ds_sfx_mot
    com "Тебя буквально передёрнуло."
    "А Лена либо не слышит, либо не обращает внимания, либо ей и не было страшно вовсе."

    stop ambience fadeout 2

    if (ds_after_tour_who == 'un') and skillcheck('reaction_speed', lvl_easy, passive=True):
        play sound ds_sfx_mot
        res "{result}А вчера она совёнка испугалась! Что-то тут не так!"
    else:
        "В третий вариант верится с трудом."
        play sound ds_sfx_psy
        aut "Но и спрашивать, чтобы выдать свой испуг, не стоит."
    window hide
    menu:
        "Спросить":
            window show
            me "А ты не слышала совёнка?"
            show un surprise dress at center
            with dspr
            un "А? Нет..."
            th "Вроде всё, ничего подозрительного..."
            if skillcheck('drama', lvl_medium, passive=True):
                play sound ds_sfx_int
                dra "{result}Кажется, врут вам, мессир."
        "Не спрашивать":
            pass

    scene bg black 
    with dissolve

    play music music_list["goodbye_home_shores"] fadein 3

    window show
    "Войдя в медпункт, ты нащупываешь в темноте выключатель и включаешь свет."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_aidpost_night 
    with flash

    play ambience ambience_medstation_inside_night fadein 3

    show un normal dress at center   with dissolve
    window hide
    menu:
        "Спросить про медсестру":
            window show
            me "А медсестра позже придёт, да?"
            un "А она не придёт…"
            th "Не придёт, ясно, ну ладно…{w} Хотя подождите…{w} Не придёт?!"
            me "Ааа, ясно…"
            play sound ds_sfx_psy
            vol "Не то чтобы ты боялся оставаться с Леной один на один.{w} В закрытом помещении.{w} Ночью.{w} И поблизости ни души..."
            vol "Нет, в таких ситуациях что-то случается только в фильмах или там сериалах всяких."
            play sound ds_sfx_fys
            hfl "Просто с тобой именно Лена, а не, скажем, Ульяна или Славя."
            hfl "И это серьёзно меняет твоё отношение к происходящему."
        "Молча продолжить":
            window show
        "Изнасиловать Лену":
            window show
            scene bg ds_int_aidpost_night_nolight
            show un scared dress at center
            with dspr
            "Ты выключаешь свет."
            un "Семён?.. Что ты делаешь?.."
            me "Я... хочу тебя... И я тебя возьму..."
            show un cry dress at center
            with dspr
            un "Не надо..."
            me "Надо, Лена, надо..."
            "Ты поваливаешь её на кушетку, срываешь с неё платье и приступаешь к своему плану..."
            scene black with dissolve2
            jump ds_end_un_rape
        "Уйти":
            window show
            me "Ну всё, я тебя проводил, а теперь пошёл!"
            show un sad dress at center
            with dspr
            un "Не уходи..."
            "Но ты её не слушаешь и уходишь."
            $ ds_lp['un'] -= 2
            jump ds_day3_evening_none
    un "Вот эти коробки."
    "Она показывает на груду коробок, сваленных как попало."
    play sound ds_sfx_int
    vic "Их там по меньшей мере с дюжину."
    vic "За десять минут не управиться."
    hide un  with dissolve
    "Ты ставишь одну коробку перед собой на стол и начинаешь выкладывать содержимое."
    "Внутри оказываются только бинты – огромное количество небольших упаковочек с бинтами."
    show un normal dress at center   with dissolve
    un "Смотри. Тебе нужно внести всё это в ЭВМ."
    "Когда ты включил компьютер, то увидел, что там уже открыта база данных. Сначала нужно внести наименование, затем артикул (если есть), затем количество."
    hide un  with dissolve
    "Работа закипела."
    un "Семён…"
    show un normal dress at center   with dissolve
    me "Что?"
    "Ты поднимаешь взгляд на Лену."
    "Она несколько секунд пристально смотрит на тебя, словно решаясь на что-то, но потом опять опускает глаза."
    show un shy dress at center   with dspr
    un "Нет, ничего."
    vol "Тебе буквально физически тяжело всё время сидеть молча."
    window hide
    menu:
        "{check=rhetoric:12}Заговорить с Леной":
            show un normal dress at center   with dspr
            un "Семён…"
            me "Да?"
            un "Ты их по второму кругу считаешь."
            play sound ds_sfx_mot
            inf "И действительно, ты начал вынимать из коробки и заносить в базу данных те бинты, которые уже посчитал."
            me "Ой, прости."
            "Она ничего не отвечаешь. А ты судорожно начинаешь тыкать кнопку «отмена», чтобы не учесть бинты дважды."
            if skillcheck('rhetoric', lvl_challenging):
                window show
                play sound ds_sfx_int
                rhe "{result}Поинтересуйся тем, откуда она."
                me "Слушай, а ты откуда? Ну, то есть откуда приехала? В смысле где родилась? Точнее, где живёшь?"
                un "Ну, я…{w} Тут городок рядом есть…"
                me "Тут рядом – это где?"
                un "Ну... этот городок... Работино. Как ты можешь не знать, ты же должен был проезжать там..."
                play sound ds_sfx_int
                lgc "Проблема в том, что ты не через вокзал или аэропорт сюда попал."

            else:
                window show
                play sound ds_sfx_int
                rhe "{result}И о чём заговорить? Ты не можешь придумать подходящей темы."
    show un surprise dress at center   with dspr
    un "А тебе здесь что, не нравится?"
    play sound ds_sfx_int
    lgc "Интересно, как она из твоих слов сделала такой вывод?"
    window hide
    menu:
        "Подтвердить":
            window show
            me "Честно говоря, не особо."
            un "А почему?"
            me "Ну, я не любитель лагерей... Мне бы дома у себя сидеть..."
            un "Понимаю... я тоже не люблю общество..."
        "Отрицать":
            window show
            me "Нет, что ты! Конечно нравится!"
            play sound ds_sfx_int
            dra "Наигранная дружелюбность прозвучала фальшиво, резанув ухо."
    window hide
    menu:
        "Спросить мнение Лены":
            window show
            me "А тебе?"
            show un normal dress at center   with dspr
            un "Да.{w} Тут спокойно, в библиотеке много книг.{w} И люди здесь хорошие…"
            play sound ds_sfx_psy
            aut "Угу. Особенно некто Советова и Двачевская. Ну прям идеал!"
            window hide
            menu:
                "Согласиться":
                    window show
                    me "Наверное..."
                "Возразить":
                    window show
                    me "Хорошие… Да не все…"
                    un "Почему?"
                    me "Ну, как бы сказать…"
                    window hide
                    menu:
                        "Привести в пример Ульяну":
                            window show
                            me "Возьми Ульянку – батарейка с катастрофически смещённой точкой приложения силы."
                            show un surprise dress at center   with dspr
                            un "Ну... она ребёнок, такое поведение для неё естественно..."
                            play sound ds_sfx_psy
                            vol "И то верно. Тут возразить тебе нечего."
                        "Привести в пример Алису":
                            window show
                            me "Вот Алиса! «Пионер – всем ребятам пример!» – этот лозунг явно не про неё. Если все будут брать пример с Алисы, то лет через двадцать такое в стране будет…"
                            play sound ds_sfx_int
                            lgc "Хотя на момент начала XXI века можно сделать вывод, что в восьмидесятые все брали пример именно с Алисы Двачевской…"
                            show un normal dress at center   with dspr
                            un "На самом деле она не такая."
                            play sound ds_sfx_mot
                            res "В смысле?!"
                            play sound ds_sfx_psy
                            emp "В прямом. Сколько раз тебе об этом говорили?"
                            me "Не такая – это какая?"
                            un "Не такая, как ты о ней говоришь."
                            play sound ds_sfx_int
                            rhe "Ну, формально ты ничего о ней не сказал."
                            me "Начнём с того, что я ничего ещё не сказал.{w} Просто констатировал факт, что она явно не является примером для подражания."
                            show un smile dress at center   with dspr
                            un "Ну… Может быть."
                            me "Получается, ты её хорошо знаешь?"
                            show un normal dress at center   with dspr
                            un "Наверное."
                            rhe "Вопрос этот ты задал просто, чтобы поддержать разговор. Такого ответа никак не ожидал."
                            lgc "Алиса с Леной настолько не похожи, что возможность того, что они могут быть близко знакомы, просто не укладывается у тебя в голове."
                            un "Мы из одного города… Давние подруги."
                            play sound ds_sfx_psy
                            vol "Она как будто прочитала твой вопрос из головы."
                            me "Понятно. Но это немного странно.{w} То есть не так. Я просто удивился."
                            show un smile dress at center   with dspr
                            un "Все удивляются."
                            "Лена еле заметно улыбается."
                        "Отступить":
                            window show
                            me "А впрочем ладно, возможно, это я неправ насчёт людей!"
                            un "Возможно..."
        "Промолчать":
            window show
    hide un  with dissolve
    "Ты берёшь вторую коробку."
    "Анальгин, активированный уголь, анальгин, активированный уголь, физраствор, марганцовка, фурацилин, анальгин…"
    play sound ds_sfx_int
    rhe "Лена постоянно выражается односложно."
    rhe "Как выстроить с ней диалог, если каждый наш разговор через пару предложений скатывается в твой монолог, а намного чаще – в неловкое молчание?"
    rhe "Такое положение вещей тебя никак не устраивает."
    play sound ds_sfx_int
    dra "Словно застенчивость и стеснительность - это маска. И она что-то скрывает.{w} Но что?"
    if skillcheck('rhetoric', lvl_easy, passive=True):
        rhe "{result}Попробуй про книги спросить. Авось получиться."
        show un normal dress at center   with dissolve
        window hide
        menu:
            "Спросить про книги":
                window show
                me "Знаешь, я тут книжку недавно прочитал…{w} Ты любишь фантастику?"
                un "Не очень."
                rhe "Очередной промах."
                me "Ну, раз не любишь…{w} А какие вообще книги тебе нравятся?"
                un "Разные…"
                rhe "Разговор явно не клеится, и нужно как-то спасать ситуацию."
                $ ds_skill_points['rhetoric'] += 1
            "Промолчать":
                window show
    if skillcheck('suggestion', lvl_challenging, passive=True):
        play sound ds_sfx_psy
        sug "{result}Почему-то ты опять вспомнил про танцы."
        if not skillcheck('volition', lvl_formidable, passive=True):
            vol "{result}Чувство неловкости, неудобства и даже в какой-то степени стыда вновь охватывает тебя."
            vol "Наверное, ты и не сильно отличаешься от Лены в подобных вещах – тоже боишься и стесняюсь всего, что не умеешь, не понимаешь."
        sug "Возможно, стоит сначала самому преодолеть свои страхи."
        sug "И это поможет тебе лучше понять её."
        window hide
        menu:
            "Предложить потанцевать":
                window show
                me "У нас осталась всего пара коробок…"
                un "Да."
                me "Слушай, у меня идея возникла.{w} Может быть, когда закончим, пойдём в столовую?{w} Мне кажется, магнитофон после танцев отнесли как раз туда."
                play sound ds_sfx_psy
                sug "И чего ему делать в столовой?"
                show un surprise dress at center   with dspr
                un "Зачем?"
                play sound ds_sfx_psy
                emp "Её искренний взгляд ясно даёт понять, что она даже не догадывается о том, что ты хочу ей предложить."
                me "Может быть, я бы смог тебя отблагодарить, потанцевав с тобой."
                show un shy dress at center   with dspr
                un "Но я…"
                "Она на мгновение перестаёт перекладывать лекарства, краснеет и смотрит прямо тебе в глаза."
                if not skillcheck('composure', lvl_challenging, passive=True):
                    com "{result}Ты смутился."
                me "Нет, если ты не хочешь, конечно…{w} Я же не настаиваю!"
                un "А если нас кто-то увидит?.."
                sug "Да, эта мысль тебе в голову не пришла."
                play sound ds_sfx_psy
                vol "С одной стороны, ничего такого.{w} С другой…"
                window hide
                menu:
                    "Отступить":
                        window show
                        me "Ну да, ты права, наверное... Забудь!"
                        un "Ну ладно..."
                    "Настоять":
                        window show
                        me "Да все спят уже давно.{w} Тем более кто ночью пойдёт в столовую!"
                        show un normal dress at center   with dspr
                        un "А как мы туда попадём?"
                        sug "А вот об этом стоило подумать заранее."
                        me "Ну, эээ…"
                        if ds_sl_keys:
                            play sound ds_sfx_mot
                            inf "У тебя есть ключи Слави!"
                            sug "Но вдруг она подумает, что ты их украл?"
                        window hide
                        menu:
                            "Сказать про ключи" if ds_sl_keys:
                                window show
                                me "У меня тут ключи Слави есть... нашёл их и отдать не успел..."
                                show un serious dress at center
                                with dspr
                                un "Так нельзя! Эти ключи надо будет обязательно отдать! А то ещё влетит Славе из-за нас..."
                            "Предложить взломать дверь":
                                window show
                                me "Да вскрою я замок, и мы зайдём."
                                show un serious dress at center
                                with dspr
                                un "Так нельзя! Взламывать дверь - это нехорошо, нас потом накажут..."
                            "Отступить":
                                window show
                                me "Да, я об этом забыл как-то..."
                        play sound ds_sfx_int
                        rhe "В любом случае надо что-то сказать, как-то сменить неудобную тему разговора."
                        me "А какая музыка тебе нравится?"
                        un "Разная…{w} Я ей не особо увлекаюсь."
                        me "Давай тогда представим, что она играет…{w} Ну, то есть, что ты… мы её слышим."
                        show un surprise dress at center   with dspr
                        un "Как это?"
                        me "Ну, как будто она у тебя в голове играет!"
                        play sound ds_sfx_int
                        con "Ты довольно точно вспоминаешь мелодию, под которую танцевали пионеры.{w} Слова и музыка хорошо врезались в память."
                        un "Не уверена, что у меня получится."
                        me "Но можно же попробовать!"
                        show un normal dress at center   with dspr
                        un "Наверное…"
                        play sound ds_sfx_int
                        rhe "Согласие получено!"
                        rhe "Даже это «наверное» в случае с Леной можно рассматривать как «да»."
                        hide un  with dissolve
                        window hide

                        with fade2
                        $ ds_un_dance_accept = True
                        $ ds_lp['un'] += 2
            "Отбросить мысль":
                pass
    window show
    "Всё оставшееся время вы молча сортируете лекарства, записывали их названия и количество."
    if ds_un_dance_accept:
        play sound ds_sfx_psy
        sug "После такой удачи стоит ещё внимательнее относиться к каждому сказанному слову."
        sug "Впрочем, ты всё равно большую часть времени молчишь."
    "Вскоре с последней коробкой покончено."
    show un normal dress at center   with dspr
    play sound ds_sfx_int
    con "Ты уставился на Лену, как будто увидел снежного человека на одноколёсном велосипеде, жонглирующего поросятами.{w} Удивительно и страшно, а главное – завораживает."
    show un laugh dress at center   with dspr
    "Вдруг она смеётся."
    me "Что?!"
    un "У тебя такое выражение…"
    me "Какое?"
    un "Забавное."
    me "Да?.."
    if ds_un_dance_accept:
        show un smile dress at center   with dspr
        un "Ага. Так куда пойдём?"
        me "Куда?"
        if skillcheck('composure', lvl_medium, passive=True):
            play sound ds_sfx_mot
            com "{result}Она про танцы."
        else:
            play sound ds_sfx_mot
            com "{result}Её последние слова несколько выбили тебя из колеи, и ты совсем забыл, о чём вы говорили до этого."
            com "Да честно признаться, ты вообще на минуту выпал из реальности."
        show un shy dress at center   with dspr
        un "Ну, как же…{w} Танцы."
        "Лена мгновенно краснеет, а на её лице появляется стандартное выражение застенчивости, стеснительности и испуга."
        me "А, да! Прости, я задумался просто."
        if skillcheck('conceptualization', lvl_easy, passive=True):
            play sound ds_sfx_int
            con "{result}Вы пойдёте на пристань."
            con "На шального пионера ночью можно наткнуться на площади, в «жилом квартале», да хоть у столовой – но никак не на пристани."
            con "А ещё ночью (тем более сегодня, в полнолуние) огромная яркая луна красиво отражается в воде."
            me "Пойдём на пристань."
            me "Или, если тебе не нравится, мы можем…"
            show un normal dress at center   with dspr

            stop music fadeout 3

            un "Нет, хорошо, отличное место."
        else:
            un "Можем на пристани потанцевать... Там луна красивая сегодня, полная."
            play sound ds_sfx_psy
            vol "Соглашайся. Идей лучше у тебя нет."
            me "Идём..."
        window hide

        stop ambience fadeout 3

        $ persistent.sprite_time = "night"
        scene bg ext_aidpost_night 
        with dissolve

        play ambience ambience_camp_center_night fadein 3

        window show
        "Лена закрывает дверь на ключ, и вы направляетесь к пристани."
        "На лагерь опустилась ночь, он спит."
        show un normal dress at center   with dissolve
        un "Пойдём по дорожке?"
        window hide
        menu:
            "Согласиться":
                window show
                me "Да, по дорожке."

            "Предложить пойти через лес":
                me "Зачем? Через лес же быстрее, там есть хорошая тропинка."
                un "Ну, там может быть…"
                window hide
                menu:
                    "Посмеяться":
                        window show
                        me "Кто? Совёнок?"
                        show un surprise dress at center   with dspr
                        un "Ну, что ты…"
                        "На её лице мелькает тень недовольства."
                        $ ds_lp['un'] -= 1
                        me "Нет, ничего, прости!"
                        show un normal dress at center   with dspr
                    "Успокоить":
                        window show
                        me "Не переживай, со мной тебя никто не тронет."
                        un "Там темно."
                        me "Боишься?"
                        un "Ну, не то чтобы…"
                    "Промолчать":
                        window show
                me "Если хочешь…"
                un "Ладно…{w} Только можно…"
                window hide

                scene cg d3_un_forest 
                with dissolve

                window show
                "Она не заканчивает фразу и берёт тебя под руку."
                un "Можно… так?"
                play sound ds_sfx_mot
                com "Тут настаёт твоя очередь краснеть."
                window hide
                menu:
                    "Разрешить":
                        window show
                        me "Конечно!"
                        $ ds_lp['un'] += 1
                    "Отказать":
                        window show
                        me "Извини... я не готов."
                        "Но она всем своим видом даёт понять, что не отпустит тебя."
                        $ ds_lp['un'] -= 1
                        me "Ну ладно..."
                    "Отпихнуть":
                        window show
                        "Ты отпихиваешь Лену от себя."
                        scene bg ext_aidpost_night 
                        with dissolve
                        show un sad dress at center
                        with dspr
                        un "Ну пожалуйста..."
                        me "Давай в другой раз."
                        un "Ладно..."
                        $ ds_lp['un'] -= 2
                "Вы идёте через лес."
                play sound ds_sfx_int
                vic "Хотя лесом это сложно назвать.{w} Скорее небольшой пролесок между лагерем и пристанью."
                vic "В длину всего каких-то несколько сот метров."
                play sound ds_sfx_psy
                vol "Будь ты один, никогда бы не подумал, что здесь можно чего-то испугаться."
                vol "Однако сейчас страх как будто передаётся от Лены к тебе."
                play sound sfx_tree_branches

                "Над нами заколыхались ветки деревьев.{w} Ты невольно вздрогнул, а Лена тотчас же ещё сильнее вцепилась в твою руку."
                window hide
                menu:
                    "Успокоить":
                        window show
                        me "Не бойся, это белка, наверное, пробежала."

                        stop ambience fadeout 2

                        un "Угу…"
                        window hide
                    "Промолчать":
                        pass

        jump ds_day3_dance_un_beach
    else:
        show un normal dress at center
        with dspr
        un "Ладно, я пойду... пока..."
        window hide
        menu:
            "{check=suggestion:10}Проводить до домика":
                if skillcheck('suggestion', lvl_medium):
                    play sound ds_sfx_psy
                    sug "{result}Предлагай аккуратно - и всё получится."
                    me "Лен, может, тебя до домика провожу..."
                    show un smile dress at center
                    with dissolve
                    un "Да, давай..."
                    "И ты идёшь за ней до её домика."
                    show bg ds_ext_un_night
                    show un normal dress at center
                    with dissolve
                    un "Спасибо... И спокойной ночи..."
                    hide un with dissolve
                    "И она заходит в домик."
                else:
                    play sound ds_sfx_psy
                    sug "{result}Тебе очень неудобно предлагать это."
                    me "Лен... может, того..."
                    "Она не слышит тебя и уходит. Ты остаёшься стоять на площади."
            "Отпустить":
                window show
                me "Пока..."
    jump ds_day3_un_end

label ds_day3_dance_un_beach:
    $ persistent.sprite_time = "night"
    scene bg ext_boathouse_night 
    with dissolve

    play ambience ambience_boat_station_night fadein 3

    show un normal dress at center   with dissolve

    window show
    "Вы выходите на пристань."
    con "Ночь поистине прекрасна."
    "Ты подходишь ближе к реке и зовёшь Лену."
    me "Смотри!"
    "В воде отражался мостик, лодочный домик и луна."
    "Казалось, что это какой-то другой мир, а водная гладь – дверь в Зазеркалье.{w} Прыгни – и окажешься по ту сторону."
    me "Позвольте пригласить вас на танец!"
    "Ты подаёшь ей руку и неумело кланяешься."
    "Лена стоит в нерешительности."
    play sound ds_sfx_psy
    sug "Наверное, с манерностью ты переборщил."
    if skillcheck('suggestion', lvl_challenging, passive=True):
        sug "{result}Возможно, разумно сначала просто посидеть, полюбоваться природой. Так сказать, сближаться постепенно."
    window hide
    menu:
        "Поддержать":
            window show
            me "Не бойся, я тоже не умею."
            th "И почему «тоже»?{w} Она же не говорила, что не умеет танцевать, хотя это и было очевидно."

            stop ambience fadeout 2

            show un smile dress at center   with dspr
            un "Хорошо."
            $ ds_lp['un'] += 1
        "Ждать дальше":
            window show
            "Наконец, Лена собирается и протягивает тебе руку в ответ."
        "Наехать на Лену":
            window show
            me "Ну и чего ждём?!"
            show un scared dress at center
            with dspr
            un "Да-да, сейчас..."
            "И она с опаской протягивает тебе руку."
            $ ds_lp['un'] -= 1
        "Предложить просто посидеть" if ds_last_skillcheck.result:
            window show
            me "Если ты стесняешься - давай просто посидим вместе, посмотрим на луну."
            un "Давай..."
            scene cg ds_day3_un_fullmoon
            with dissolve
            play sound ds_sfx_int
            con "Полная луна озаряет водную гладь. И создаёт вокруг вас, наверное, самую романтическую обстановку, какую только можно придумать. Вдали пробегает грузовой поезд."
            "Лена прижимается к твоему плечу. Тебя согревает осознание этого. Ты приобнимаешь её - и она не сопротивляется этому."
            $ ds_lp['un'] += 2
            $ ds_skill_points['suggestion'] += 1
            "Наконец, она склоняется над твоим ухом и шепчет."
            un "Спасибо, что посидел... мне так хотелось полюбоваться ночным пейзажем вместе..."
            me "Не за что."
            un "Теперь давай потанцуем. Я готова..."
            me "Отлично!"
    window hide

    scene cg d3_un_dance 
    with dissolve

    play music music_list["a_promise_from_distant_days"] fadein 3

    window show
    "Лена подаёт тебе свою руку, ты отводишь её в сторону и нежно приобнимаешь девочку за талию."
    "Вы просто стоите в таком положении несколько секунд."
    un "А дальше что?"
    me "Ну, я не знаю…{w} Ты же помнишь ту песню?"
    un "С трудом…{w} Но помню."
    me "Вот и отлично! Давай, как в фильмах, вальсировать."
    un "А как это?"
    "Вместо ответа ты начинаешь очень медленно и осторожно описывать вместе с Леной нечто наподобие круга."
    me "Вот видишь, не так уж и сложно!"
    un "Ага…"
    "Несколько минут вы кружитесь в танце."
    play sound ds_sfx_mot
    svf "Или как это ещё можно назвать…"
    per_toc "Ты чувствуешь тепло, хотя вы и не были очень уж близко."
    "Её грудь учащённо вздымается, а лицо всё больше краснеет."
    "Лена не смотрит на тебя, отводя взгляд то в одну, то в другую сторону."
    play sound ds_sfx_psy
    ine "Внезапно ты ощущаешь, что никогда ещё не испытывал ничего подобного."
    ine "Нежность, затмевающая собой реальность – словно попал в какой-то другой, лучший мир."
    play sound ds_sfx_psy
    vol "Ты понимаешь, что не хочешь отпускать эту девочку и отдал бы всё, чтобы кружиться с ней вместе в этом танце бесконечно."
    "Ты прижимаешь Лену поближе к себе, и только тогда она впервые смотрит на меня."
    play sound ds_sfx_psy
    emp "В её глазах читается удивление, растерянность, но не испуг."
    "Она не боится и не отталкивает тебя."
    un "А ты говорил, что не умеешь танцевать."
    me "Так и не умею…"
    play sound ds_sfx_int
    rhe "От Лены можно было ждать какой угодно реакции, но только не этого."
    rhe "Неужели её стеснение куда-то само собой исчезло, смущение прошло, а вечный испуг улетучился?.."
    window hide
    menu:
        "Поблагодарить":
            window show
            me "Спасибо..."
        "Похвалить в ответ":
            window show
            me "Ты тоже… неплохо танцуешь…"
            un "А я знаю!"
            if skillcheck('perception', lvl_easy, passive=True):
                play sound ds_sfx_mot
                per_eye  "На её лице промелькнула лукавая улыбка."
                th "Но как такое возможно?"
                play sound ds_sfx_int
                dra "Образ вечно застенчивой и скромной Лены никак не вяжется с тем, что происходило сейчас."
                th "Что же сказать?{w} Что делать дальше?"
                play sound ds_sfx_psy
                vol "Ты можешь только на автомате вести её, не останавливая ни на секунду этот становящийся всё более и более странным танец."
        "Промолчать":
            window show

    stop music fadeout 3

    play ambience ambience_boat_station_night fadein 3

    mt "Семён! Семён, ты где?"
    play sound ds_sfx_mot
    per_hea "Голос доносится с опушки леса."
    play sound ds_sfx_mot
    res "Чёрт, как не вовремя!"
    mt "Семён!"
    per_hea"Это Ольга Дмитриевна."
    play sound ds_sfx_int
    lgc "Наверное, она беспокоится, потому что ты уже давно должен был вернуться."
    lgc "И ведь можно было догадаться, что неутомимая вожатая бросится на поиски {i}пропавшего{/i} пионера!"
    play sound ds_sfx_psy
    sug "Надо было её заранее предупредить."
    th "Эх! Что сейчас-то уже говорить..."
    sug "Извини."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_boathouse_night 
    with dissolve

    show un normal dress at center   with dissolve
    window show
    "Лена вопросительно смотрит на меня."
    un "Может, не стоит, чтобы нас видели вместе?"
    window hide
    menu:
        "Согласиться":
            window show
            me "Да, ты права, пожалуй..."
            hide un with dissolve
        "Возразить":
            window show
            me "Почему?{w} Пойдём скажем ей, что всё в порядке."
            un "Нет. Давай спрячемся, а потом вернёмся в лагерь."
            th "Странно, с чего это она?{w} Ведь всё так неплохо шло..."
            th "Только что-то начало получаться.{w} Вроде бы начало…"
            th "Но вот {i}что{/i}?.."
            me "Ладно, хорошо."
            hide un  with dissolve
        "Настоять на походе":
            window show
            me "Чего ты прячешься? Пойдём к вожатой!"
            show un angry dress at center
            with dspr
            un "Я никуда не пойду! Хочешь - иди сам!"
            me "Ладно..."
    "Ты не стал спорить – это неуместно в данной ситуации."
    "Ольга Дмитриевна, покричав-покричав, уходит."
    show un normal dress at center   with dissolve
    un "Ну, пойдём."

    stop ambience fadeout 3

    me "Да…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_path_night 
    with dissolve

    play ambience ambience_forest_night fadein 3

    show un normal dress at center   with dissolve
    window show
    "На обратном пути Лена не берёт тебя под руку."
    window hide
    menu:
        "{check=volition:11}Проявить инициативу":
            if skillcheck('volition', lvl_up_medium):
                window show
                vol "{result}Ты берёшь её за руку сам."
                "Краем глаза замечаешь лёгкую улыбку Лены."
                $ ds_lp['un'] += 1
            else:
                window show
                vol "{result}Ты не решаешься проявить инициативу."
            $ ds_skill_points['volition'] += 1
        "Смириться":
            window show
            th "Ну и ладно!"
        "Спросить, почему":
            window show
            me "Лен, а почему ты теперь не берёшь меня за руку."
            show un surprise dress at center
            with dspr
            un "А что? Надо было?"
            me "Да не, если не хочешь - не стоит."
    play sound ds_sfx_int
    rhe "Вы опять молчите – начинать разговор не в привычках Лены, а ты просто не знаешь, что сказать после всего случившегося. Да и все темы исчерпаны."
    "Всю дорогу она смотрит себе под ноги, сохраняя всё то же выражение «как всегда»."
    th "Какая же всё-таки странная перемена!"
    th "Или скорее странной была та улыбка на пристани и те слова Лены."

    stop ambience fadeout 3

    "..."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_square_night_party2 
    with dissolve

    play ambience ambience_camp_center_night fadein 3

    show un normal dress at center   with dissolve
    window show
    "На площади она останавливается."
    un "Ладно, мне пора."
    me "Да…"
    un "Спасибо тебе… за сегодня…"
    me "Да…"
    hide un  with dissolve
    "Лена разворачивается и идёт в сторону своего домика."
    window hide
    menu:
        "{check=suggestion:10}Проводить до домика":
            if skillcheck('suggestion', lvl_medium):
                play sound ds_sfx_psy
                sug "{result}Предлагай аккуратно - и всё получится."
                me "Лен, может, тебя до домика провожу..."
                show un smile dress at center
                with dissolve
                un "Да, давай..."
                "И ты идёшь за ней до её домика."
                show bg ds_ext_un_night
                show un normal dress at center
                with dissolve
                un "Спасибо... И спокойной ночи..."
                hide un with dissolve
                "И она заходит в домик."
            else:
                play sound ds_sfx_psy
                sug "{result}Тебе очень неудобно предлагать это."
                me "Лен... может, того..."
                "Она не слышит тебя и уходит. Ты остаёшься стоять на площади."
        "Отпустить":
            window show
    th "Так что же это такое было?"
    th "Этот танец, потом такая резкая смена настроения, а потом всё как обычно."
    play sound ds_sfx_int
    dra "Как будто тогда, в то короткое мгновение, вы обнимали совсем другую Лену, мессир."
    dra "Да! Тогда она не просто была не похожа на себя, а казалась вообще другим человеком."
    th "Может быть, я просто плохо её знаю?"
    dra "Может. Ведь и раньше было ощущение, что Лена вечно что-то скрывает под маской застенчивости."
    play sound ds_sfx_int
    lgc "Впрочем, за пару дней понять человека до конца просто невозможно."
    th "Чёрт! Что же делать дальше?!{w} Может, мне вообще всё это привиделось!"
    window hide
    jump ds_day3_un_end

label ds_day3_un_end:
    scene bg black 
    with dissolve

    window show
    "Ты направляешься к домику вожатой."
    play sound ds_sfx_fys
    hfl "Весь лагерь спит, так что вряд ли тебя может кто-то заметить."
    th "Да и что с того?{w} Ну гуляет пионер ночью один – эка невидаль!"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_house_of_mt_night 
    with dissolve

    play sound sfx_bush_leaves

    window show
    "Когда ты уже почти дошёл до двери, сзади слышится шорох."
    "Ветки кустов рядом с деревом позади тебя шуршат, словно в них кто-то запрыгнул."
    play sound ds_sfx_fys
    hfl "Диких животных здесь вроде как не водится…"
    hfl "Значит, кто-то следил за тобой!"
    window hide
    menu:
        "Проверить":
            window show
            "В то же мгновение ты бросаешься на звук, продираешься сквозь кусты и начинаешь озираться по сторонам."
            play sound ds_sfx_mot
            per_eye "Слишком темно, и ничего и, главное, никого в такой темноте не увидеть."
            play sound ds_sfx_int
            lgc "Идти дальше бессмысленно – если даже за тобой кто-то и следил, он уже давно убежал."
            "Ты возвращаешься к домику."
        "Забить":
            window show
            "Ты продолжаешь идти в сторону домика."
    "В окне горит свет."
    th "Значит, она ещё не спит."

    stop ambience fadeout 2

    window hide

    play sound sfx_open_dooor_campus_2

    pause(1)

    $ persistent.sprite_time = "sunset"
    scene bg int_house_of_mt_noitem_night 
    with dissolve

    play music music_list["smooth_machine"] fadein 3

    show mt surprise dress at center   with dissolve
    window show
    mt "Семён! Ты где был?!"
    me "Как это где?{w} Мы с Леной в медпункте сортировали лекарства. Я же вам говорил, что пойду вечером."
    mt "Да? Когда это? И столько времени к тому же! Да и я была в медпункте полчаса назад – закрыт он, свет не горит!"
    me "Ну… Ээээ… Мы решили немного прогуляться."
    mt "Я тут волнуюсь, а он прогуляться решил!"
    me "Ну извините…{w} В следующий раз предупрежу заранее."
    show mt normal dress at center   with dspr
    mt "Уж постарайся!{w} А теперь спать, уже поздно!"
    "В этом с вожатой сложно не согласиться."
    window hide

    scene bg int_house_of_mt_night2 
    with dissolve2

    window show
    th "Сегодня был трудный во всех смыслах день."
    play sound ds_sfx_psy
    vol "Ты слишком устал, чтобы размышлять о произошедшем вечером, да и вряд ли в голову пришло бы что-то путное…"
    th "И главное – совершенно непонятно, как на всё это реагировать."
    th "На Лену, на лагерь, на весь этот мир..."
    play sound ds_sfx_psy
    sug "И Лена...{w} Время, проведённое с ней, было куда важнее для тебя, чем все попытки вернуться в {i}реальный{/i} мир."
    play sound ds_sfx_fys
    edr "Ты бы мог ещё долго накручивать себя, пытаясь понять, что же сделал не так, а что не сделал вообще, но усталость взяла своё..."
    window hide

    stop music fadeout 3

    scene black 
    with fade3

    $ renpy.pause(3)

    jump ds_day3_dream

label ds_day3_evening_us:
    "Ты подходишь к Ульяне."
    show us smile dress at center
    with dissolve
    us "Чего грустишь?"
    show us laugh dress at center
    with dspr
    me "А что предложишь?"
    us "Пойдём танцевать!"
    window hide
    menu:
        "Согласиться":
            window show
            me "А давай!"
            show us surp1 dress at center
            with dspr
            us "А как ты без музыки танцевать собрался?"
            th "Вот же зараза..."
        "Отказаться":
            me "Рано ещё…{w} Даже музыка не играет."
            show us dontlike dress at center   with dspr
            us "Какой ты скучный!"
            hide us  with dissolve
            "И она убегает."
    th "А Ульянка таки надела что-то наподобие вечернего платья.{w} Забавно."

    if ds_dance_dv:
        scene cg ds_day3_disco_with_dv
        with dissolve
    else:
        scene cg d3_disco
        with dissolve

    window show
    "Пионеры продолжают танцевать."
    th "Ну хоть им дискотека по душе."
    "Танцует и Ольга Дмитриевна."
    play sound ds_sfx_psy
    aut "Вожатой всё-таки положено следить за порядком."
    aut "Тем более ей уже давно не 17 лет."
    "Ольга Дмитриевна словно чувствует, что кто-то осмелился усомниться в её профпригодности, и подходит ко мне."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_square_night_party 
    with dissolve

    show mt normal dress at center   with dissolve
    window show
    mt "Чего не танцуешь?"
    me "Не хочется что-то…"
    if ds_punished:
        show mt smile dress at center   with dspr
        mt "Ну, дело твоё."
        "Она хитро улыбнулась."
        mt "Тогда у меня для тебя есть занятие получше!"
        me "Например?"
        "Сейчас мне абсолютно любое занятие казалось лучше, чем танцы."
        show mt normal dress at center   with dspr
        mt "Вы сегодня, конечно, хорошо в столовой убрались, но всё же…{w} Думаю, вы ещё не полностью загладили свою вину."
        me "Эээ?"
        mt "Ульяна!"
        us "Что?!"
        mt "Подойди сюда."
        show us surp1 dress at right   with dissolve
        "Ульянка нехотя подошла."
        mt "Вижу, ты уже на год вперёд натанцевалась."
        us "А вот и нет!"
        "С неё стекали ручьи пота, так что вожатая была права."
        mt "У меня для тебя с Семёном поручение!"
        show us surp2 dress at right   with dspr
        us "Ну Ольга Дмитриевна!"
        us "Сейчас же танцы! Да и поздно уже!"
        mt "А это ненадолго.{w} Славя сегодня книги в библиотеке разбирала, но не закончила…"
        mt "Вам пара полок осталось."
        us "Но…"
        show mt angry dress at center   with dspr
        mt "Никаких но!"
        show us sad dress at right   with dspr
        window hide
        menu:
            "{check=authority:15}Оспорить":
                if skillcheck('authority', lvl_heroic):
                    window show
                    play sound ds_sfx_psy
                    aut "{result}Дважды за один проступок не наказывают."
                    me "Ольга Дмитриевна, но вы же уже наказали один раз нас. А второй раз наказывать нельзя!"
                    show mt surprise dress at center
                    with dspr
                    mt "Вот как... Ну ладно..."
                    mt "Поэтому я вас {i}попрошу{/i} разобрать книги в библиотеке."
                    mt "Вы же поможете любимому лагерю?"
                    play sound ds_sfx_int
                    rhe "Какой же она тонкий тролль... И не возразишь же!"
                    me "Но... как же танцы?.."
                    mt "Ну, кому-то же надо разобрать книги в библиотеке!"
                    me "Дела..."
                    show mt normal dress at center
                    with dspr
                    mt "В общем, удачи!"
                    hide mt with dissolve
                    $ ds_lp['us'] += 1
                    $ ds_skill_points['authority'] += 1
                    me "Ладно, пойдём убираться..."
                    jump ds_day3_us_library
                else:
                    window show
                    play sound ds_sfx_psy
                    aut "{result}Вожатая слишком властна. Ты не решаешься толком противостоять ей."
                    me "Но..."
                    mt "Всё, я сказала!"
                    $ ds_skill_points['authority'] += 1
                    hide mt with dissolve
                    show us smile dress at center
                    with dspr
                    us "Пойдём, Семён."
                    $ ds_lp['us'] += 1
                    jump ds_day3_us_library
            "Смириться":
                window show
                me "Ладно..."
                show us upset dress at center
                with dspr
                us "Ну вот..."
                jump ds_day3_us_library
            "Проявить энтузиазм":
                window show
                
                me "Я готов!"
                show mt smile dress at center   with dspr
                mt "Молодец, Семён! Молодец! Настоящий пионер! Видишь, Ульяна, бери пример!"
                $ ds_lp['mt'] += 1
                $ ds_lp['us'] -= 2
                play sound ds_sfx_psy
                emp "Ульянка такой пример для подражания явно не оценила."
                mt "Так что, давайте!{w} Весь лагерь на вас рассчитывает!"
                show us angry dress at right   with dspr
                us "Я тебе это ещё припомню!"

                stop music fadeout 3

                window hide
                jump ds_day3_us_library
    else:
        show mt grin dress at center with dspr
        mt "А со мной?"
        "Она хитро улыбается."
        th "Танцевать... с вожатой? Что?"
        me "Но... я... не..."
        show mt smile dress at center with dspr
        mt "Ну давай, не бойся. Всего лишь один танец."
        play sound ds_sfx_mot
        res "Вот не знаю от кого, но от Ольги Дмитриевны ты такого точно не ожидал."
        "Вожатая всё ещё стоит в ожидании твоего ответа."
        play sound ds_sfx_fys
        ins "Нужно заметить, что Ольга Дмитриевна очень красивая. И молодая!"
        play sound ds_sfx_psy
        aut "Но тут дело в вашем статусе – она вожатая, а ты пионер и со стороны это может показаться неправильным."
        window hide
        menu:
            "Согласиться":
                window show
                th "К чёрту! Живём один раз всё-таки, да и это просто танец."
                me "Ладно, но предупреждаю - я плохо танцую."
                $ ds_lp['mt'] += 1
                mt "Ничего, научим."
                "Она отвечает с энтузиазмом."
                mt "Только подожди."
                th "Что такое?"
                mt "Ульяна!"
                us "Что?!"
                mt "Подойди сюда."
                show us surp1 dress at right   with dissolve
                "Ульянка нехотя подходит."
                mt "Вижу, ты уже на год вперёд натанцевалась."
                us "А вот и нет!"
                "С неё стекали ручьи пота, так что вожатая была права."
                mt "У меня для тебя поручение!"
                show us surp2 dress at right   with dspr
                us "Ну Ольга Дмитриевна!"
                us "Сейчас же танцы! Да и поздно уже!"
                mt "А это ненадолго.{w} Славя сегодня книги в библиотеке разбирала, но не закончила…"
                mt "Вам пара полок осталось."
                us "Но…"
                show mt angry dress at center   with dspr
                mt "Никаких но!"
                show us sad dress at right   with dspr
                window hide
                menu:
                    "{check=authority:15}Заступиться за Ульяну":
                        if skillcheck('authority', lvl_heroic):
                            window show
                            play sound ds_sfx_psy
                            aut "{result}Дважды за один проступок не наказывают."
                            me "Ольга Дмитриевна, но вы же уже наказали один раз Ульяну. А второй раз наказывать нельзя!"
                            show mt surprise dress at center
                            with dspr
                            mt "Вот как..."
                            mt "Тогда ты и уберёшься!"
                            me "Но... как же танцы?.."
                            mt "Ну, кому-то же надо разобрать книги в библиотеке!"
                            me "Дела..."
                            show mt normal dress at center
                            with dspr
                            mt "В общем, удачи!"
                            hide mt with dissolve
                            show us smile dress at center
                            with dspr
                            us "Спасибо, Семён!"
                            $ ds_lp['us'] += 2
                            $ ds_lp['mt'] -= 2
                            $ ds_skill_points['authority'] += 1
                            me "Ага, иди танцевать..."
                            show us dontlike dress at center
                            with dspr
                            us "Не уж то ты думаешь, что я тебя брошу? Раз так вышло - я пойду с тобой!"
                            play sound ds_sfx_int
                            rhe "Спорить бессмысленно. Она не примет возражений."
                            me "Ладно..."
                            jump ds_day3_us_library
                        else:
                            window show
                            play sound ds_sfx_psy
                            aut "{result}Вожатая слишком властна. Ты не решаешься толком противостоять ей."
                            me "Но..."
                            mt "Всё, я сказала!"
                            mt "Пойдём, Семён?"
                            $ ds_skill_points['authority'] += 1
                            window hide
                            menu:
                                "Согласиться":
                                    window show
                                    me "Да, идём..."
                                    $ ds_lp['us'] -= 1
                                "Отказаться":
                                    window show
                                    me "Нет, я не пойду..."
                                    show mt angry dress at center
                                    with dspr
                                    mt "Тогда ты пойдёшь с Ульяной убираться!"
                                    me "Но..."
                                    mt "Никаких «но»!"
                                    hide mt with dissolve
                                    show us smile dress at center
                                    with dspr
                                    us "Пойдём, Семён."
                                    us "И спасибо, что попытался заступиться!"
                                    $ ds_lp['us'] += 1
                                    jump ds_day3_us_library
                    "Молча одобрить":
                        window show
                        "Ты смотришь на Ульяну свысока."
                        show us upset dress at center
                        with dspr
                        us "Ну вот..."
                        hide us with dissolve
                        mt "Пойдём, Семён."
                    "Одобрить словесно":
                        window show
                        me "Всё правильно. Ты сегодня крупно провинилась."
                        show us angry dress at center
                        with dspr
                        us "Молчи!"
                        mt "Так, Ульяна, марш в библиотеку!"
                        show us upset dress at center
                        with dspr
                        us "Ладно..."
                        hide us with dissolve
                        mt "Пойдём, Семён."
                jump ds_day3_dance_mt
            "Отказаться":
                window show
                me "Нет, я как-то не готов сегодня к танцам."
                mt "Тогда..."
                th "Что такое?"
                mt "Ульяна!"
                us "Что?!"
                mt "Подойди сюда."
                show us surp1 dress at right   with dissolve
                "Ульянка нехотя подходит."
                mt "Вижу, ты уже на год вперёд натанцевалась."
                us "А вот и нет!"
                "С неё стекали ручьи пота, так что вожатая была права."
                mt "У меня для тебя поручение!"
                show us surp2 dress at right   with dspr
                us "Ну Ольга Дмитриевна!"
                us "Сейчас же танцы! Да и поздно уже!"
                mt "А это ненадолго.{w} Славя сегодня книги в библиотеке разбирала, но не закончила…"
                mt "Вам пара полок осталось."
                us "Но…"
                show mt angry dress at center   with dspr
                mt "Никаких но!"
                show us sad dress at right   with dspr
                window hide
                menu:
                    "{check=authority:15}Оспорить":
                        if skillcheck('authority', lvl_heroic):
                            window show
                            play sound ds_sfx_psy
                            aut "{result}Дважды за один проступок не наказывают."
                            me "Ольга Дмитриевна, но вы же уже наказали один раз нас. А второй раз наказывать нельзя!"
                            show mt surprise dress at center
                            with dspr
                            mt "Вот как... Ну ладно..."
                            mt "Поэтому я вас {i}попрошу{/i} разобрать книги в библиотеке."
                            mt "Вы же поможете любимому лагерю?"
                            play sound ds_sfx_int
                            rhe "Какой же она тонкий тролль... И не возразишь же!"
                            me "Но... как же танцы?.."
                            mt "Ну, кому-то же надо разобрать книги в библиотеке!"
                            me "Дела..."
                            show mt normal dress at center
                            with dspr
                            mt "В общем, удачи!"
                            hide mt with dissolve
                            $ ds_lp['us'] += 1
                            $ ds_skill_points['authority'] += 1
                            me "Ладно, пойдём убираться..."
                            jump ds_day3_us_library
                        else:
                            window show
                            play sound ds_sfx_psy
                            aut "{result}Вожатая слишком властна. Ты не решаешься толком противостоять ей."
                            me "Но..."
                            mt "Всё, я сказала!"
                            $ ds_skill_points['authority'] += 1
                            hide mt with dissolve
                            show us smile dress at center
                            with dspr
                            us "Пойдём, Семён."
                            $ ds_lp['us'] += 1
                            jump ds_day3_us_library
                    "Смириться":
                        window show
                        me "Ладно..."
                        show us upset dress at center
                        with dspr
                        us "Ну вот..."
                        jump ds_day3_us_library

label ds_day3_us_library:
    $ persistent.sprite_time = "night"
    scene bg ext_house_of_dv_night 
    with dissolve

    play ambience ambience_camp_center_night fadein 3
    $ ds_day3_evening_who = 'us'
    "Вечерний лагерь красив.{w} Тишина и покой умиротворяют тебя."
    "Лишь далёкие звуки музыки, доносящиеся с площади, напоминают, что ты здесь не один."
    show us dontlike pioneer at center   with dissolve
    "И ещё Ульяна, которая только что вернулась."
    window hide
    menu:
        "Посмеяться":
            window show
            me "Могла бы и в платье убраться."
            "Я усмехнулся."
        "Промолчать":
            window show
    show us angry pioneer at center   with dspr
    us "Это ты, всё ты!"
    "Она так сопит, а лицо её было таким красным, что ты бы не удивился, если бы у Ульянки из ушей пошёл пар."
    us "Ты!{w} Это всё ты виноват!"
    me "Почему опять я?"
    us "Если бы ты просто молчал!"
    me "И что бы изменилось?{w} Она бы всё равно нас заставила."
    us "Ты…"
    "Она уже не может говорить и просто шипит."
    me "Ну, промолчал бы я, и что?{w} Думаешь, она бы отпустила тебя дальше развлекаться?"
    show us normal pioneer at center   with dspr
    "Ульянка смотрит на тебя."
    play sound ds_sfx_psy
    emp "Похоже, она немного успокоилась."
    us "Конечно! Тебя же это не интересует!{w} Ты и танцевать-то не умеешь!"
    me "А если даже и так, то что?"
    show us grin pioneer at center   with dspr
    us "Вот пошёл бы со мной танцевать…{w} Было бы весело!"
    "Она возвращается в своё привычное, «детское» состояние."
    me "Может, и пошёл бы…{w} Но, видишь, как получилось…"
    me "Всё равно проверить, кто из нас лучше танцует, уже не удастся."
    window hide

label ds_day3_us_library:
    $ persistent.sprite_time = "night"
    scene bg ext_library_night 
    with dissolve

    window show
    "Вы подходите к библиотеке.{w} К тому времени уже стемнело."
    th "Какая-то странная просьба Ольги Дмитриевны... или точнее приказ... ночью разбирать книги."

    stop ambience fadeout 2

    window hide

    $ persistent.sprite_time = "night"
    scene bg int_library_night 
    with dissolve

    window show
    "Внутри темно, да ко всему ещё и выключатель отказывается работать, лишь противно щёлкая при каждом нажатии."
    "Точнее, он, может, и работал, но свет не зажигается."
    show us normal pioneer at center   with dissolve
    us "Подожди, сейчас свечи принесу."
    hide us  with dissolve
    window hide

    pause(1)

    $ persistent.sprite_time = "sunset"
    scene bg int_library_night2 
    with dissolve

    play sound sfx_match_candle

    play music music_list["i_want_to_play"] fadein 3

    window show
    "Ты только хотел спросить, откуда она знает, где здесь свечи и спички, как на столе рядом со мной уже зажглись два ярких огонька."
    show us laugh pioneer at center   with dissolve
    us "Так-то лучше!"
    "Сказала Ульяна, довольная собой."
    window hide
    menu:
        "Спросить про свечи":
            window show
            me "А ты откуда знаешь, где свечи?"
            us "Так я уже все углы в лагере облазила!"
            th "А, ну логично..."
        "Продолжить":
            window show
    me "А дальше что?"
    show us normal pioneer at center   with dspr
    us "А что дальше?"
    "Она вопросительно смотрит на меня."
    me "Ну, что нам делать?"
    show us dontlike pioneer at center   with dspr
    us "Пфф, мне откуда знать?"
    me "Прекрасно."
    hide us  with dissolve
    "Ты обходишь шкафы."
    th "Ольга Дмитриевна что-то говорила про «пару полок»..."
    "Проведя рукой по книгам, ты удостоверился, что пыли на них нет."
    play sound ds_sfx_int
    lgc "Похоже, до тебя здесь кто-то хорошо поработал."
    lgc "Наверное, вожатая ошиблась."
    play sound ds_sfx_mot
    per_hea "Вдруг позади слышатся шаги."
    window hide

    play sound sfx_wood_floor_squeak

    pause(1)

    window show
    "Старый, растрескавшийся пол предательски скрипит, и это не позволило Ульяне подкрасться незамеченной."
    us "Бу!"
    "Ты разворачиваешься."
    show us laugh2 pioneer at center   with dissolve
    window hide
    menu:
        "Подыграть":
            window show
            me "А! Кто это?! Призрак?!"
            "Ульяна заливается смехом."
            $ ds_lp['us'] += 1
        "Поиздеваться":
            window show
            me "Очень страшно…"
            show us dontlike pioneer at center   with dspr
            us "Да ну тебя!"
            "Она обиженно отворачивается."
            $ ds_lp['us'] -= 1
        "Проигнорировать":
            window show
    me "В общем, здесь вроде и так чисто, поэтому…"
    play sound ds_sfx_psy
    ine "Освещённые тусклым светом ряды книг смотрят на тебя как будто с укоризной."
    play sound ds_sfx_int
    enc "Безвестные авторы давно минувших лет…"
    th "Интересно, помнит ли о них кто-нибудь ещё?{w} Женя наверняка помнит."
    th "Почему-то мне кажется, что она-то точно помнит вообще всё."
    show us normal pioneer at center   with dspr
    us "Ладно, садись."
    "Ульяна пододвигает к тебе стул.{w} Ты садишься"
    me "И дальше что?"
    show us surp1 pioneer at center   with dspr
    us "Будем рассказывать страшные истории.{w} У нас с тобой два стула и две свечки, соответственно, две истории – одна моя, одна твоя."
    window hide
    menu:
        "Согласиться":
            window show
        "Отказаться":
            window show
            me "Нет, спасибо."
            show us laugh pioneer at center
            with dspr
            us "Струсил?"
            me "Нет, просто не хочу."
            show us dontlike pioneer at center
            with dspr
            us "Ну и иди, такой скучный!"
            $ ds_lp['us'] -= 1
            "Ты и выходишь."
            scene bg ext_library_night
            with dissolve
            jump ds_day3_evening_none
    me "Давай."
    play sound ds_sfx_psy
    vol "Возвращаться на танцы совершенно не хочется, а ночью в лагере, по твоему опыту, делать особо нечего."
    play sound ds_sfx_int
    con "Тем более ты точно знаешь хотя бы пару неплохих историй, которые могли бы изрядно напугать Ульяну."
    th "И это просто замечательно."
    me "Начинай."
    us "Ладно."
    window hide

    scene cg d3_us_library_1 
    with dissolve

    window show
    "Она садится поудобнее, обхватывает руками спинку стула и подносит свечку как можно ближе к лицу."
    window hide

    with fade

    window show
    us "{i}Однажды в одной деревне жил-был один мальчик. Ну, обычный такой. Ходил в школу, играл с другими детьми. В общем, ничего особенного.{/i}"
    us "{i}И вот как-то раз поспорили они с другом, что мальчик этот испугается пойти в заброшенный дом…{/i}"
    "Ульяна делает длинную паузу."
    window hide
    menu:
        "Спросить":
            window show
            me "И что в этом доме?"
            us "Не перебивай!"
            me "На ходу придумываешь?"
            "Она надувает губы и продолжает."
        "Молча слушать":
            window show
    us "{i}Говорят, в том доме жила ведьма, а сейчас по ночам там иногда видят её призрак. Точно никто не знал, но боялась вся деревня.{/i}"
    us "{i}Мальчик сказал, что это всё чепуха, и он готов хоть целую ночь там провести. Так и произошло. Но наутро мальчик не вернулся.{/i}"
    us "{i}Его нашли повесившимся.{/i}"
    "Ульяна опять молчит."
    window hide
    menu:
        "Скептически уточнить":
            window show
            me "Захватывающе…{w} Он повесился на шнурках от ботинок?"
            "Она вновь насупилась."
        "Уточнить, конец ли":
            window show
            me "Это конец?"
            us "Нет же!"
        "Слушать дальше":
            window show
    "{i}И мальчика похоронили. Ну, как обычно хоронят. Гроб там, все дела.{/i}"
    "{i}Родственники и друзья горевали, но мальчика было уже не вернуть.{/i}"
    "{i}Однако через несколько дней в деревне стали исчезать люди. Никто не знал как и почему. Они просто пропадали без следа.{/i}"
    "{i}Жители уже хотели вызывать милицию, но тут друг мальчика рассказал, что видел того мальчика, который повесился в доме ведьмы. Ему сначала никто не поверил, но люди продолжали исчезать.{/i}"
    nvl clear
    "{i}Тогда жители решили выкопать гроб. А на его крышке изнутри были глубокие царапины от ногтей. Но мальчика там не было.{/i}"
    "{i}Куда же он исчез?{/i}"
    "Ульяна убирает свечку подальше от лица и делает страшное (по крайней мере на её взгляд) выражение лица."
    "{i}В итоге все жители деревни исчезли, и только люди, случайно оказавшиеся рядом с домом ведьмы, рассказывают, что видели там два призрака.{/i}"
    window hide

    scene black 
    with dissolve

    window show
    "Ульяна задувает свою свечку и молчит."
    window hide

    $ set_mode_adv()

    $ persistent.sprite_time = "sunset"
    scene bg int_library_night2 
    show us normal pioneer at center 
    with dissolve

    window show
    play sound ds_sfx_int
    lgc "Похоже, рассказ окончен."
    window hide
    menu:
        "Похвалить":
            window show
            me "Прекрасно!"
            window hide

            play sound sfx_simon_applause

            pause(1)

            window show
            "Я захлопал в ладоши."
            me "На Пулитцеровскую премию, конечно, не тянет, но…"
            show us grin pioneer at center   with dspr
            us "Страшно?{w} Испугался?"
            play sound ds_sfx_int
            dra "Ни капельки. И это по вам видно."
            me "Весь дрожу…"
            show us sad pioneer at center   with dspr
            us "Да ну тебя…{w} Давай свой рассказ.{w} Уверена, я даже не вздрогну!"
            window hide
        "Раскритиковать":
            window show
            me "И это всё?"
            us "Ну да."
            me "Пф, и ничего страшного!"
            show us sad pioneer at center   with dspr
            us "Да ну тебя…{w} Давай свой рассказ.{w} Уверена, я даже не вздрогну!"
            window hide
    menu:
        "{check=conceptualization:12}Придумать рассказ":
            if skillcheck('conceptualization', lvl_challenging):
                window show
                stop music fadeout 3

                window show

                play sound ds_sfx_int
                con "{result}Вспомни историю, которую читал... несколько месяцев назад, в блоге своего знакомого."
                th "Точно. Он был довольно-таки талантливым щелкопёром – по крайней мере мне его стиль нравился."
                con "Так что успех тебе практически гарантирован."
                con "Конечно, дословно ты историю не запомнил, так что перескажи своими словами."

                play music music_list["into_the_unknown"] fadein 3

                me "{i}Отдалённая космическая станция, можно сказать, последний рубеж человечества, расположенная на границе с враждебной цивилизацией. Третий месяц перемирия.{/i}"
                me "{i}Хотя миром это назвать сложно – скорее «невойной». Небольшая горстка выживших измучена многодневной осадой.{/i}"
                me "{i}С одной стороны, они не могут отступить, бросив аванпост, с другой – понимают, что в случае атаки противника не продержатся и минуты.{/i}"

                me "{i}Отчаяние – самое подходящее слово, чтобы описать их состояние.{/i}"
                me "{i}Провизия подходит к концу, а боеприпасов остаётся разве что на пару выстрелов, которые в случае начала боевых действий будут больше похожи на приветственный салют.{/i}"
                me "{i}В достатке только вода и воздух – спасибо регенерационным системам.{/i}"
                me "{i}Люди уже несколько недель не разговаривают друг с другом. Наверное, они просто не видят смысла тратить время на общение с себе подобными, когда смерть стоит за дверью.{/i}"
                me "{i}Точнее, за многометровой бронёй станции.{/i}"
                me "{i}Действительно, лучше просто ждать. Спасения или атаки врага. Оба исхода приведут к концу этой пытки.{/i}"

                me "{i}Ситуация напоминает шахматную партию с невидимым противником. А именно, её самую сложную часть – эндшпиль. Любой неверный ход приведёт к поражению. Как их, так и неприятеля.{/i}"
                me "{i}Неизвестно только, знает ли об этом противник. Может быть, он тоже боится сделать неправильный ход. В то же время земляне всегда могут двигать королём. Но только на клетку вперёд, а затем – на клетку назад.{/i}"
                me "{i}Любой другой ход автоматически приводит к проигрышу. Шаг вперёд – мнимая угроза нападения. И шаг назад – осознанная необходимость защиты. Игра была бы куда проще, если бы противник сидел перед тобой. Даже самый опытный шахматист никогда не сможет скрыть нервные движения глаз, случайную каплю пота или дрожание рук.{/i}"
                me "{i}С одной стороны, всё это бесполезно – каждый знает, что ситуация безвыходна, так как никто не решится на ход, означающий немедленное поражение.{/i}"

                me "{i}С другой же – видя перед собой живого оппонента, понимая, что он ничем не отличается от тебя и так же может ошибиться, проще пойти ва-банк. Возможно, такие же трудности испытывает и противник.{/i}"
                me "{i}В такой ситуации оказалась небольшая горстка мужчин и женщин на краю Вселенной. Приказов из штаба нет уже несколько дней.{/i}"
                me "{i}Впрочем, и те, что приходили раньше, не содержали в себе ничего ценного – лишь стандартные требования держать оборону.{/i}"
                me "{i}Шаг на клетку вперёд – шаг на клетку назад. Раскачивание идеального маятника.{/i}"
                me "{i}В начале четвёртого месяца командир принимает решение отступать.{/i}"
                me "{i}Он рассуждает, что жизни его солдат важнее мифических идеалов Человечества. И за это его никто не осудит.{/i}"

                me "{i}Тем более что они всё равно не в состоянии ничего изменить.{/i}"
                me "{i}Приготовления длятся недолго: самое ценное, что можно спасти с тонущего корабля, – своя жизнь.{/i}"
                me "{i}И вот уже весь экипаж станции в спасательном корабле. Идет предстартовый отсчёт. Три, два, один… И ничего. Ворота не открываются.{/i}"
                me "{i}На устранение неполадки отправляют механиков. Но те ничего не находят. Ворота должны открыться. Но не открываются они и во второй раз. И в третий тоже…{/i}"
                me "{i}Командир отдаёт приказ покинуть станцию в спасательных капсулах. Но и они не могут стартовать. Сначала всё списывают на технические неполадки. Экипаж пытается связаться со штабом, но безуспешно.{/i}"

                me "{i}Только спустя несколько дней старпом замечает, что на радарах ничего нет. Ничего в прямом смысле – ни планет, ни астероидов, ни кораблей противника. Просто сплошная тьма…{/i}"
                me "{i}Через месяц заканчивается еда. Всем кажется, что это конец. Но ни спустя день, ни спустя неделю люди не начинают умирать.{/i}"
                me "{i}Словно для поддержания человеческого существования пища не нужна.{/i}"
                me "{i}К тому моменту большинство экипажа сходит с ума. Кто-то просто сидит в своей каюте и читает молитвы, кто-то ходит туда-сюда по станции, кто-то пытается покончить с собой.{/i}"
                me "{i}Но ни выстрелы в упор из плазменного ружья, ни заплывы в гидрокамере, ни даже банальное вскрытие вен не приносят никакого эффекта.{/i}"

                me "{i}Проходят дни, месяцы, может, даже годы – никто не считает. Сумасшедшие возвращают себе рассудок, а нормальные обезумевают. И так множество раз.{/i}"
                me "{i}Наконец экипаж свыкается со своим положением.{/i}"
                me "{i}Они начинают придумывать себе различные занятия: театральные постановки, турниры по различным видам спорта, чтение книг, ими же написанных.{/i}"
                me "{i}Складывается множество семейных пар, ещё больше – распадается.{/i}"
                me "{i}Бесконечный поток времени, замкнутый круг человеческой жизни. И только темнота на радаре напоминает о том, что вокруг пустота. Но пустота – и внутри станции…{/i}"
                me "{i}В конце концов люди перестают жить – они просто лежат каждый в своей каюте и спят. Сначала не все 24 часа, но со временем они учатся входить в состояние транса.{/i}"
                me "{i}У каждого свои сны – кто-то возвращается в детство, кто-то вновь обретает утраченную любовь, кто-то с бластером наперевес защищает идеалы Человечества. А кто-то просто блуждает в пустоте…{/i}"

                me "{i}Спасательный корабль, потрёпанный в нескольких несерьёзных стычках с противником, пришвартовался к стыковочному доку. Десантная группа попала внутрь.{/i}"
                me "{i}Станция была похожа на кусок металлолома, который по крайней мере несколько тысячелетий летал в космосе. Реактор давно отключился, на стенах виднелись следы от лазерного оружия, вся аппаратура была разбита.{/i}"
                me "{i}Почти в каждой каюте спасательная команда нашла истлевшие скелеты людей. Они приняли ужасную смерть, защищая дальние рубежи Человечества.{/i}"
                me "{i}И только шифровка в штаб напоминала, что что-то не так:{/i}"

                me "{i}«Спасите!\n{/i} {i}Мы просто хотим умереть…»{/i}"

                window hide
                $ ds_lp['us'] += 2
            else:
                window show
                play sound ds_sfx_int
                con "{result}Кажется, ты ничего интересного не можешь ни придумать, ни вспомнить."
            $ ds_skill_points['conceptualization'] += 1
        "Отказаться":
            window show
            me "Пожалуй, воздержусь. А то ещё напугаю тебя!"
            show us dontlike pioneer at center
            with dspr
            us "Гони рассказ!"
            me "Нет."
            us "Тогда я пошла!"
            hide us with dissolve
            "И она выбегает из библиотеки. Обиженная."
            $ ds_lp['us'] -= 1
            scene bg ext_library_night
            "Ты тоже выходишь. Дискотека уже закончилась."
            $ persistent.sprite_time = "night"
            scene bg int_house_of_mt_night2 
            with dissolve

            play ambience ambience_int_cabin_night fadein 2

            window show
            "Ольга Дмитриевна уже спит."
            "Ты не раздеваясь лёг на кровать и накрылся одеялом с головой."
            play sound ds_sfx_psy
            ine "Уснуть не удаётся долго – у тебя перед глазами проигрывается рассказ Ульяны."
            th "А точно стоило её так отвергать?"
            play soudn ds_sfx_psy
            emp "Сомнительно. Но сделанного не воротишь."
            window hide

            stop ambience fadeout 2

            scene bg black 
            with fade3

            $ renpy.pause(3)
            jump ds_day3_dream

    stop music fadeout 3

    $ set_mode_adv()

    $ persistent.sprite_time = "sunset"
    scene bg int_library_night2 
    with dissolve

    play ambience ambience_music_club_night fadein 3

    window show
    "Ты заканчиваешь рассказ и смотришь на Ульяну."
    "Её лицо скрыто во тьме."
    me "Ну, вот такая история…"

    play sound sfx_blow_out_candle

    "Ты задуваешь огонёк."
    window hide

    scene cg d3_us_library_2 
    with dissolve

    window show
    "Ульяна кричит, вскакивает и кидается на меня."

    play sound sfx_fall_wood_floor

    "Вы падаете на пол."
    window hide

    scene cg d3_us_library_3 
    with dissolve

    window show
    me "Ты чего?"
    us "Ничего…"
    play sound ds_sfx_psy
    emp "Её голос звучит крайне испуганно."
    play sound ds_sfx_psy
    aut "Похоже, твоя история удалась."
    "Однако Ульянке явно не до веселья."
    "Она обнимает тебя, всё её тело дрожит, и слышатся тихие всхлипы."
    window hide
    menu:
        "Успокоить":
            window show
            me "Ты чего, глупенькая?"
            "Я погладил её по голове."
            me "Это же просто история.{w} Она не реальная."
        "Посмеяться":
            window show
            me "И чего ты так испугалась? Это же просто история!"
        "Промолчать":
            window show
    us "Тебе лишь бы всякие глупости рассказывать!"
    "Ульяна прижимается к тебе плотнее."
    me "Что, так испугалась?"
    us "Угу…"
    play sound ds_sfx_int
    rhe "По правде говоря, ты не ожидал от неё такого честного ответа."
    me "Ну, ничего-ничего."
    play sound ds_sfx_psy
    sug "В конце концов, время лечит – полежит и успокоится."
    us "Слушай, Семён…"
    me "Чего?"
    us "Ладно, ничего."
    "Она утыкается лицом тебе в грудь."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_library_night 
    with dissolve

    window show
    "Проходит несколько минут."
    me "Слушай, я всё понимаю… Но, может, пойдём уже?"
    window hide

    scene cg d3_us_library_4 
    with dissolve

    window show
    "Ты прислушиваешься.{w} Ульянка тихо посапывает."
    me "Эй! Не спи!"
    th "Интересно, как это так можно от испуга заснуть?"
    me "Не спи, кому говорят!"
    "Она не реагирует"
    "Ты пытаешься встать."
    play sound ds_sfx_fys
    phi "Конечно, Ульяна вряд ли весит больше сорока килограмм…"
    phi "Не так-то и просто подняться!"
    play sound ds_sfx_mot
    per_hea "Если бы не дыхание, можно было и правда подумать, что Ульянка умерла."
    phi "Конечно, можно приложить немного больше усилий..."
    play sound ds_sfx_psy
    vol "Но ведь тогда ты её разбудишь – и всё по новой!"
    th "Да уж, незавидное положение."
    vol "Хотя всегда есть вариант дождаться, пока она проснётся сама."
    vol "Не будет же она, в конце концов, спать до утра после таких рассказов?"
    "Ты смотришь через окно на звёздное небо."
    play sound ds_sfx_int
    con "Интересно, может быть, где-то там действительно есть далёкий аванпост с экипажем, состоящим из призраков…"
    window hide
    menu:
        "{check=physical_instrument:16}Подняться":
            if skillcheck('physical_instrument', lvl_godly):
                window show
                phi "{result}Тебе всё-таки удаётся подняться. С трудом, но удаётся."
                "Причём, Ульяна настолько крепко спит, что не замечает того, что ты вылез."
                window hide
                menu:
                    "Остаться с Ульяной":
                        window show
                        th "Ладно, посижу тут..."
                    "Уйти":
                        window show
                        scene bg ext_library_night
                        "Ты выходишь. Дискотека уже закончилась."
                        $ persistent.sprite_time = "night"
                        scene bg int_house_of_mt_night2 
                        with dissolve

                        play ambience ambience_int_cabin_night fadein 2

                        window show
                        "Ольга Дмитриевна уже спит."
                        "Ты не раздеваясь лёг на кровать и накрылся одеялом с головой."
                        play sound ds_sfx_psy
                        ine "Уснуть не удаётся долго – у тебя перед глазами проигрывается рассказ Ульяны."
                        th "А точно стоило её так отвергать?"
                        play soudn ds_sfx_psy
                        emp "Сомнительно. Но сделанного не воротишь."
                        window hide

                        stop ambience fadeout 2

                        scene bg black 
                        with fade3

                        $ renpy.pause(3)
                        $ ds_lp['us'] -= 1
                        jump ds_day3_dream
            else:
                window show
                phi "{result}Бесполезно - Ульяна слишком тяжёлая."
                th "Ладно..."
        "Остаться лежать":
            window show

    stop ambience fadeout 2

    "Глаза медленно закрываются, и через некоторое время ты проваливаешься в сон."
    window hide

    scene black 
    with fade3

    $ renpy.pause(3)

    jump ds_day3_dream

label ds_day3_dance_mt:
    stop music fadeout 3
    window hide
    scene bg black
    with fade
    $ renpy.pause(1)
    scene bg ext_square_night_party
    with dissolve
    window show
    "Вы выходите к остальным танцующим пионерам."
    play music music_list["waltz_of_doubts"] fadein 2
    "Музыка сменяется на более тихую."
    th "Вот и медляк подъехал."
    show mt smile dress at center with dissolve
    "Ольга Дмитриевна протягивает тебе руку."
    mt "В принципе, ничего сложного, просто надо левой ногой вот так, а правую ногу поставить сюда."
    "Она начинает объяснять движения, которые напоминают вальс."
    mt "А теперь давай вместе."
    window hide
    scene cg ds_day3_mt_dance
    with dissolve
    window show
    play sound ds_sfx_mot
    svf "Ты делаешь первый шаг, потом второй, третий, четвёртый...{w} В итоге у тебя начало неплохо получатся, как для первого раза. По крайней мере ты не наступил на ноги вожатой."
    play sound ds_sfx_psy
    ine "Вы кружитесь... Кружились так, словно планеты в бескрайнем космосе, а вокруг нас лишь маленькие искры далеких звёзд."
    play sound ds_sfx_mot
    per_eye "Краем глаза ты замечаешь подозрительные взгляды пионеров."
    play sound ds_sfx_psy
    aut "Но тебе уже всё равно."
    play sound ds_sfx_psy
    vol "Твоё внимание сконцентрировано лишь на одном человеке, который сейчас был в паре сантиметров от меня."
    vol "От улыбки Ольги Дмитриевны, где-то глубоко в душе, тебе становится тепло и приятно. Она внушала надежду, что всё может измениться и всё станет лучше."
    vol "Помимо этих чувств, есть ещё одно, странное, которое ты никак не можешь понять..."
    stop music fadeout 3
    window hide
    scene bg ext_square_night_party
    with dissolve
    window show
    "Музыка останавливается. Останавливаетесь и вы."
    show mt smile dress at center with dissolve
    window hide
    menu:
        "Одобрить танец":
            window show
            me "Спасибо за танец, мне даже понравилось."
            show mt laugh dress at center with dspr
            mt "Пожалуйста, ты неплохо справился."
            $ ds_up_morale()
            window hide
            menu:
                "Поблагодарить Ольгу Дмитриевну":
                    window show
                    me "Это всё благодаря вам."
                    show mt normal dress at center with dspr
                    "Ольга Дмитриевна отводит взгляд в сторону."
                    $ ds_lp['mt'] += 1
                "Промолчать":
                    window show
        "Сказать, что не понравилось":
            window show
            me "Честно говоря... мне всё ещё не особо понравилось танцевать."
            show mt normal dress at center
            with dspr
            mt "Ну... может, следующий понравится!"
            $ ds_lp['mt'] -= 1
        "Промолчать":
            window show
    play music music_list["lightness"] fadein 2 
    "Пионеры вновь начинают плясать под музыку с более быстрым темпом."
    mt "Ладно, я пойду тогда."
    show mt smile dress at center with dspr
    hide mt with dissolve
    "И она удаляется в сторону диджейского пульта, где Мику управляет музыкой."
    "Ты присаживаешься на скамейку и ждёшь окончания этого мероприятия."
    play sound ds_sfx_mot
    per_eye "Осмотрев толпу пионеров, я не нашёл Славю и Лену."
    play sound ds_sfx_int
    lgc "Лена наверное в медпункте помогает медсестре, а Славя куда ушла?"
    window hide
    stop music fadeout 3
    scene bg black
    with fade
    $ renpy.pause(1)
    scene bg ext_square_night_party
    with dissolve
    window show
    play ambience ambience_camp_center_night
    "Спустя некоторое время, музыка затихает и дискотека заканчивается."
    mt "Семён!"
    "Не успел ты сделать и пары шагов в сторону дома, как Ольга Дмитриевна окликивает меня."
    th "Рано радовался."
    show mt normal dress at center with dissolve
    mt "Помоги ребятам перенести аппаратуру на своё место."
    "Возле памятника Генды стояли Шурик и Электроник."
    window hide
    menu:
        "Cогласиться":
            window show
            me "Конечно помогу!"
            show mt smile dress at center
            with dspr
            mt "Вот, настоящий пионер!"
            $ ds_karma += 10
            $ ds_lp['mt'] += 1
        "{check=suggestion:14}Отказаться":
            if skillcheck('suggestion', lvl_legendary):
                window show
                play sound ds_sfx_psy
                sug "{result}Ты хочешь спать. Ты устал после дискотеки."
                me "Я спать! Хватит с меня работы на сегодня!"
                show mt angry dress at center with dspr
                mt "Семён!"
                me "Я сказал, что никуда не пойду!"
                mt "Тогда завтра отработаешь вдвойне!"
                # ...
            else:
                window show
                play sound ds_sfx_psy
                sug "{result}Они и сами справятся, наверное."
                me "Может они сами справятся..."
                show mt angry dress at center with dspr
                mt "Семён!"
                me "Ладно, ладно, спешу на помощь."
                show mt smile dress at center with dspr
                mt "Сразу бы так."
    hide mt with dissolve
    "Ты подходишь к кибернетикам."
    show el normal pioneer at cleft
    show sh normal pioneer at cright 
    with dissolve
    me "Ну и куда нужно всё это перетащить?"
    sh "Эти колонки надо отнести на сцену."
    "Шурик указывает пальцем на две левые колонки."
    el "Регуляторы громкости и остальные две колонки – в музыкальный клуб. Провода, столы и стулья – к нам в здание кружков."
    mt "Тогда я возьму провода и стулья, а вы разберёте всё остальное."
    hide el
    hide sh
    with dissolve
    show mt normal dress at center with dissolve 
    with dissolve
    play sound ds_sfx_mot
    res "Оказывается, сзади тебя была вожатая."
    play sound ds_sfx_int
    lgc "Она не ушла спать... Видимо, ты ошибался насчёт её чувства ответственности."
    hide mt with dissolve
    "Вы с Электроником взяли по колонке и направились в сторону сцены."
    stop ambience fadeout 3
    window hide
    scene bg black
    with fade
    $ renpy.pause(1)
    scene bg ext_stage_normal_night
    with dissolve
    window show
    play ambience ambience_camp_center_evening fadein 2
    "Нести колонку немного тяжеловато, но в основном терпимо."
    play sound ds_sfx_int
    vic "По Электронику не особо видно, что он устал."
    play sound sfx_hatch_drop
    "Вскоре колонки занимают своё законное место на сцене."
    "Ты усаживаешь на краю сцены."
    window hide
    menu:
        "Заговорить с Электроником":
            window show
            me "Ну и денёк сегодня."
            show el smile pioneer with dissolve
            el "Да, насыщенный день. Кстати вы с вожатой неплохо танцевали, большинство наблюдали за вами."
            play sound ds_sfx_psy
            aut "Да вы уже стали местными звёздами."
            window hide
            menu:
                "Согласиться":
                    window show
                    me "Да! Точно!"
                "Возразить":
                    window show
                    me "Возможно, но я не особо умею танцевать."
                    el "Я даже не заметил этого."
            window hide
            menu:
                "Спросить, не считает ли странным":
                    window show
                    me "А ты не считаешь это странным?"
                    show el normal pioneer with dspr
                    el "Что?"
                    me "То что я танцевал с Ольгой Дмитриевной."
                    el "Не думаю. А что здесь такого?"
                    th "Хмм... действительно, а что такого-то? Это же просто танец."
                "Cпросить, с кем танцевал":
                    window show
                    me "А ты с кем-то потанцевал? "
                    if not ds_el_mz_relation:
                        show el sad pioneer with dspr
                        el "Да... я не танцевал особо... не было с кем..."
                        th "Что значит «не было с кем»? На площади же было много пионерок или я чего-то не знаю?.."
                        if ds_know_mz_el:
                            play sound ds_sfx_int
                            lgc "Да с Женей он хотел потанцевать. А она не явилась."
                    else:
                        show el smile pioneer with dspr
                        el "C Женей! У меня всё получилось, представляешь!"
                        window hide
                        menu:
                            "Искренне порадоваться":
                                window show
                                "Ты улыбаешься."
                                me "Это классно!"
                            "Похвалить":
                                window show
                                me "Молодец!"
                            "Cухо отреагировать":
                                window show
                                me "Хорошо..."
                            "Промолчать":
                                window show
                        el "Это благодаря тебе, Семён!"
                        play sound ds_sfx_psy
                        vol "Тебе очень приятно. Ты ощущаешь, что {i}нужен{/i} кому-то."
                        $ ds_up_morale()
        "Посидеть молча":
            window show
    show el normal pioneer with dspr
    el "Ладно пойдём, а то нас там заждались, наверное. "
    "Вы направляетесь к остальным."
    stop ambience fadeout 3
    window hide
    scene bg black
    with fade
    $ renpy.pause(1)
    scene bg ext_square_night
    with dissolve
    window show
    play ambience ambience_camp_center_night fadein 2
    "Спустя некоторое время, вы смогли убрать музыкальную аппаратуру с площади."
    "К вам ещё попутно присоединилась Славя. Она подмела площадь."
    show mt smile dress with dissolve
    mt "Ребята, спасибо за помощь. Благодаря вам, наша площадь снова блестит от чистоты.{w} А теперь можете идти спать."
    hide mt with dissolve
    show el smile pioneer at left 
    show sh smile pioneer at right
    show sl smile2 pioneer at center
    with dissolve
    el "Спокойной ночи."
    hide el with dissolve
    sh "Увидимся."
    hide sh with dissolve
    sl "До завтра."
    hide sl with dissolve
    "Напоследок машет вам Славя."
    window hide
    menu:
        "Помахать в ответ":
            window show
            "Ты помахал им вслед."
        "Проигнорировать":
            window show
            $ ds_lp['sl'] -= 1
    th "Хотя бы Славя на меня не обижается."
    show mt smile dress with dissolve
    mt "Теперь и нам пора идти."
    me "Пожалуй."
    stop ambience fadeout 3
    window hide
    scene bg black
    with fade
    $ renpy.pause(1)
    scene cg d3_mt_walk
    with dissolve
    window show
    play music music_list["reminiscences"] fadein 2
    "Вы идёте между домиками в сторону вашего жилища."
    window hide
    menu:
        "{check=rhetoric:8}Заговорить с вожатой":
            if skillcheck('rhetoric', lvl_easy):
                window show
                play sound ds_sfx_int
                rhe "{result}Заведи разговор с ней. Расспроси про лагерь."
                me "Ольга Дмитриевна, а вы раньше бывали здесь?"
                mt "Да, я часто сюда ездила, когда мне было столько же сколько и вам сейчас."
                me "И вам нравилось?"
                mt "А почему я, по-твоему, устроилась здесь вожатой?"
                me "Значит нравилось."
                mt "А тебе?"
                me "Что?"
                mt "Нравится здесь?"
                me "Не знаю... пока не решил, но здесь определённо есть своя тёплая атмосфера."
                mt "Впереди у тебя ещё будет время, чтобы всё понять."
                th "Мне бы лучше понять, как я сюда попал и тогда хоть целый день мешки с сахаром могу таскать."
                me "А вы не знаете в каком году был построен «Совёнок»?"
                mt "Нет."
                "Она хитро улыбается."
                play sound ds_sfx_int
                dra "Такое ощущение, что Ольга Дмитриевна знает ответ, но специально не говорит его."
                play sound ds_sfx_int
                lgc "Или тебе просто кажется."
            else:
                window show
                play sound ds_sfx_int
                rhe "{result}Ну и о чём ты можешь с ней поговорить?"
                "Всю дорогу вы молчите."
        "Молча идти":
            window show
            "Всю дорогу вы молчите."
    stop music fadeout 3
    window hide
    scene bg ext_house_of_mt_night_without_light
    with dissolve
    window show
    play ambience ambience_camp_center_night fadein 2
    "Тем временем вы уже дошли до нашего треугольного домика."
    show mt normal dress with dissolve
    mt "Подожди минуту."
    hide mt with dissolve
    "Ольга Дмитриевна зашла внутрь."
    play sound ds_sfx_psy
    "И почему тебе нужно чего-то ждать?"
    play sound ds_sfx_int
    lgc "Ей нужно сбросить с себя вечернее платье, а твоё присутствие противоречило бы человеческим моральным принципам."
    window hide
    menu:
        "Зайти в домик":
            window show
            scene bg int_house_of_mt_night with dspr
            "Впрочем, Ольга Дмитриевна находится за дверцей шкафа. Ты ничего увидеть не можешь."
            mt "Семён, дай переодеться, пожалуйста."
            window hide
            menu:
                "Выйти":
                    window show
                    me "Извините."
                    scene bg ext_house_of_mt_night with dspr
                    "И ты выходишь."
                    "Вскоре ты слышишь."
                    mt "Входи."
                "Посмотреть на вожатую":
                    window show
                    "Ты заглядываешь за дверцу шкафа."
                    show mt angry swim far at left with dissolve
                    mt "CЕМЁН!"
                    $ ds_lp['mt'] -= 1
                    "C этими словами она буквально выпихивает тебя из домика."
                    scene bg ext_house_of_mt_night with dspr
                    play sound ds_sfx_fys
                    ins "Какая лепота!"
                    mt "Войдите!"
        "Подождать":
            window show
            scene bg ext_house_of_mt_night with dspr
            th "Здравствуй, шезлонг, давно не виделись."
            play sound sfx_wood_floor_squeak
            "Усевшись как можно поудобнее, я принялся ждать.{w} В голове всплывали разные мысли..."
            mt "Входи."
            "Но голос из домика не дал мне на них сконцентрироваться."
    stop ambience fadeout 3
    window hide
    scene bg int_house_of_mt_night
    with dissolve
    play sound sfx_open_dooor_campus_2
    pause(1)
    play sound sfx_close_door_1 
    window show
    "Войдя внутрь, ты обнаруживаешь, что Ольга Дмитриевна уже комфортно устроилась под одеялом."
    scene bg int_house_of_mt_night2 with dspr
    play sound sfx_bed_squeak1
    "Ты следуешь её примеру и поскорее лёг на кровать."
    window hide 
    scene bg black
    with fade
    $ renpy.pause(1)
    scene bg int_house_of_mt_night2 with dspr
    with dissolve
    window show
    play music music_list["trapped_in_dreams"] fadein 2
    play sound ds_sfx_psy
    vol "Мысли не дают мне покоя."
    window hide
    menu:
        "Спросить у вожатой":
            window show
            me "Ольга Дмитриевна, можно вопрос?"
            mt "Можно."
            me "Как вы думаете, на что способен человек?"
            mt "На многое. Человек имеет уникальный дар созидания и разрушения, благодаря чему можно достичь или изменить что угодно.{w} Но для этого нужно, или даже необходимо, чтобы сам человек изменился, а это порой очень трудно." 
            mt "Но в итоге, борьба противоположностей внутри нас приводит к развитию новых качеств характера и таким образом человек способен на новые возможности. Как-то так."
            "Закончив свой монолог, Ольга Дмитриевна зевает."
            mt "А теперь спать, завтра ещё поболтаем. Спокойной ночи."
            me "Спокойной..."
            vol "Слова вожатой вселяют в тебя надежду."
            play sound ds_sfx_psy
            ine "Может не всё так мрачно, как кажется, и ты сможешь отсюда выбраться, но для этого надо измениться..."
            play sound ds_sfx_int
            lgc "Но как? Ты что, должен стать «порядочным пионером» или «истинным коммунистом»?"
            play sound ds_sfx_psy
            sug "Ага, конечно, размечтались..."
        "Пожелать спокойной ночи":
            window show
            me "Спокойной ночи, Ольга Дмитриевна."
            mt "Спокойной ночи, Семён."
        "Промолчать":
            window show
    "Вскоре на тебя нахлынула усталость. Мозг уже не может нормально фокусироваться на мыслях, и ты не сопротивляешься, а просто поворачиваешься на бок и засыпаешь."
    stop music fadeout 3
    window hide
    scene bg black
    with fade3
    $ renpy.pause(3)
    jump ds_day3_dream

label ds_day3_dance_mi:
    $ ds_lp['mi'] += 1
    $ ds_day3_evening_who = 'mi'
    "На данной вечеринке Мику имеет, наверное, самое ответственное поручение - она отвечает за музыку."
    "Ты подходишь к ней."
    me "Привет."
    show mi shy dress at center with dissolve
    mi "Привет, Семён-кун! А что ты сюда пришёл? Тебе не нравится то, что сейчас играет? Только ведь сейчас ничего не играет? А, тебе тишина не нравится? Так давай чего-нибудь включу."
    play sound ds_sfx_int
    rhe "Её пулемётная очередь из слов сразу же сражает тебя наповал."
    me "Просто я..."
    window hide
    menu:
        "Cказать, что не любишь дискотеки":
            window show
            me "Просто я не люблю дискотеки."
            show mi normal dress at center with dspr 
            mi "Правда? Ты знаешь, я тоже!"
            mi "Я никогда не понимала всего этого! Зачем просто так кривляться! Тем более на людях! Если умеешь танцевать - другое дело! А я вот не умею..."
            play sound ds_sfx_mot
            res "Мику чего-то не умеет?"
            window hide
            menu:
                "Подтвердить":
                    window show
                    me "Ну вот и я не умею."
                "Усомниться":
                    window show
                    me "Как так? Я думал, ты прям всё-всё умеешь!"
                    show mi laugh dress at center with dspr
                    mi "Да ладно тебе, Семён-кун, не льсти мне! Как видишь - не всё. Например, я не умею решать дифференциальные уравнения или танцевать бальные танцы!"
                "Устыдить":
                    window show
                    me "Как так? Девушка - и не умеет танцевать?!"
                    show mi dontlike dress at center with dspr
                    $ ds_lp['mi'] -= 1
                    mi "И что в этом такого? Все мы чего-то не умеем! Вот ты не умеешь играть на флейте, например, а я - танцевать бальные танцы!"
            play sound ds_sfx_int
            lgc "Поразительно: ход её мыслей удивительно точно совпадает с твоим."
            play sound ds_sfx_psy
            vol "Я вдвойне рад, что есть человек, который хоть в чём-то думает так же, как и ты."
            play sound ds_sfx_psy
            sug "На мгновение тебе даже хочется её обнять."
            vol "Но лучше не стоит - не поймёт."
            window hide
            menu:
                "Обнять":
                    window show
                    show mi surprise dress close at center with dspr
                    "Ты тянешься к Мику. На удивление, она не сопротивляется."
                    mi "Cемён-кун?"
                    me "Мне очень приятно, что ты понимаешь меня..."
                    mi "Мне тоже... но давай не при людях, а то нас не поймут."
                    me "Ну ладно..."
                    show mi smile dress at center with dspr
                    $ ds_lp['mi'] += 1
                "Не обнимать":
                    window show
            if ds_whom_helped == 'mi':
                mi "Кстати, спасибо тебе ещё раз, что помог сегодня!"
                me "Да не стоит."
            play sound ds_sfx_psy
            sug "Cкрась ей конец этого дня. Потанцуй с ней."
            window hide
            menu:
                "{check=suggestion:12}Пригласить потанцевать":
                    pass
                "Отбросить мысль":
                    window show
                    me "Ну ладно, пока, Мику!"
                    show mi sad dress at center
                    with dspr
                    mi "Пока, Семён..."
                    hide mi with dissolve
                    jump ds_day3_evening_none
        "{check=suggestion:12}Пригласить потанцевать":
            pass
    if not skillcheck('suggestion', lvl_challenging, modifiers=[('ds_dance_dv', 2, 'Музыку обеспечит Алиса')]):
        window show
        sug "{result}Мику всё же слишком занята. Без шансов."
        mi "Ну ладно, хорошо провести тебе время, Семён! А мне надо музыкой управлять. Или руководить?"
        me "Пока, Мику..."
        hide mi with dissolve
        $ ds_skill_points['suggestion'] += 1
        jump ds_day3_evening_none
    sug "{result}Просто пригласи её потанцевать. Или ты думаешь, что ей правда оборудованеи интереснее?"
    $ ds_skill_points['suggestion'] += 1
    me "Слушай, а, может быть, потанцуем?"
    show mi shocked dress at center with dspr
    mi "Потанцевать? Так я же не умею... И ты сказал, что не умеешь... С чего ты вдруг?.."
    me "Ну, попробовать-то надо..."
    mi "А как же музыка..."
    if ds_dance_dv:
        me "Так вот, Алиса будет на гитаре играть!"
    else:
        me "Да кто-нибудь разберётся! Не переживай!"
    show mi shy dress at center with dspr
    mi "Вот как... Я не знаю... Ну давай попробуем!"
    if ds_mi_costume:
        show mi surprise dress at center with dspr
        mi "Только где же твой костюм, Семён-кун? Ну тот, который я тебе утром давала?"
        me "Не успел надеть..."
        mi "Ну так надень его! Ты будешь выглядеть очень-очень красиво!"
        window hide
        menu:
            "Сходить и надеть":
                window show
                me "Cейчас, подожди."
                "Ты бежишь в сторону своего домика."
                scene bg ext_house_of_mt_night
                with dissolve
                scene bg int_house_of_mt_night
                with dissolve
                "Костюм лежит там же, где ты его оставил. Ты его надеваешь и возвращаешься к Мику."
                scene bg ext_square_night_party
                show mi smile dress at center
                with dissolve
                me "Вот и я!"
                mt "Я же говорила, Семён-кун!"
                me "Ага..."
                $ ds_lp['mi'] += 1
            "Отказаться":
                window show
                me "Извини, давай в следующий раз... я сейчас буду бегать долго..."
                show mi sad dress at center
                with dspr
                mi "Ну ладно, как скажешь... только в следующий раз не забудь надеть!"

    "Ты протягиваешь Мику руку."
    me "Позвольте вас пригласить."
    show mi shy dress close at center with dspr
    "Она нерешительно протягивает в ответ свою, и вы закружились в танце."
    scene cg ds_day3_dance_mi
    with dissolve
    play sound ds_sfx_mot
    com "Не почувствовать её дрожь невозможно, равно как и твою."
    com "Её руки буквально впиваются в тебя, будто спасая её от падения в несуществующую пропасть, её глаза пытаются всеми силами избежать визуального контакта с тсоими, и даже в тусклом свете луны ты замечаешь, что она краснеет."
    com "Её растерянность доходит до того, что она несколько раз наступает тебе на ногу."
    mi "Ой, извини!"
    play sound ds_sfx_psy
    sug "Но тебя это заставляет скорее улыбаться, нежели раздражаться."
    play sound ds_sfx_int
    con "Более того, виноватое лицо Мику было, пожалуй, самой умилительной вещью, которую ты когда-либо видел."
    com "Совсем скоро вы перестаёте дрожать, и ваши движения становятся более уверенными."
    play sound ds_sfx_mot
    per_toc "Ты ощущаешь её горячее дыхание, которое вкупе с твоим раскаляет воздух между вами."
    "Её тело послушно следует за твоим."
    "Ваши лица так близко..."
    com "В тебе не осталось ни капли смущения."
    play sound ds_sfx_psy
    vol "Наоборот, ты совершенно спокойно смотришь на неё и начинаешь понимать."
    vol "Понимать, что ты действительно терял очень многое, когда убегал с дискотек."
    vol "Терял те волшебные моменты, во время которых весь мир останавливается, и остаётесь лишь ты и твоя партнёрша."
    vol "И не важно, что танцевать вы с Мику особо не умеете - вы просто наслаждаетесь этими моментами..."
    mi "Это ты так «не умеешь танцевать»?"
    "Она заливается смехом."
    window hide
    menu:
        "Похвалить Мику":
            window show
            me "Так ведь и ты умеешь. Только нервничаешь."
            mi "А что... Так заметно? Извини, просто я вот так первый раз танцую... Да и всё это так неожиданно..."
            me "Тебе не нравится?"
            mi "Нет, почему... Мне очень нравится, честно!"
            $ ds_lp['mi'] += 1
        "Принять":
            window show
            me "Ну... наверное... спасибо."
            mi "Мне очень нравится, как ты танцуешь!"
        "Промолчать":
            window show
    
    stop music fadeout 3
    
    "Наконец, музыка стихает."
    "Вы с Мику заметно подустали и усаживаетесь на лавочку, чтобы перевести дыхание."
    play sound ds_sfx_psy
    vol "Не хочется никуда уходить, не хочется ничего делать."
    "Мику кладёт голову тебе на плечо."
    show mi happy dress close at center with dspr
    mi "Я не знала, что танцевать - это так здорово!.. Спасибо тебе, что пригласил!"
    window hide
    menu:
        "Поблагодарить в ответ":
            window show
            me "И тебе, что согласилась."
            "Твои слова остаются без ответа."
        "Промолчать":
            window show
            me "Ага..."
    "Ты смотришь на неё и видишь, что её уже потихоньку клонит в сон."
    "Так что засиживаться смысла нет."
    "Я легонько тормошишь её."
    me "Не пора ли спать?"
    mi "А?.. Что?.. А... Ты прав, пора уже."
    me "Ну так идём?"
    mi "А... да... идём..."
    show mt angry dress at right
    show mi scared dress at center
    with dissolve
    mt "И никуда Хацуне не пойдёт! Почему это ты бросила аппаратуру?!"
    mi "Ой, извините..."
    window hide
    menu:
        "{check=authority:12}Заступиться за Мику":
            if skillcheck('authority', lvl_challenging):
                window show
                play sound ds_sfx_psy
                aut "{result}И что, теперь Мику не имеет права потанцевать?"
                me "Ну потанцевала Мику. Музыка же как-то управилась сама! И вообще, это же праздник для пионеров!"
                if ds_dance_dv:
                    mt "Как это ни странно, но вас Двачевская спасла! Которая музыку и вытягивала!"
                else:
                    mt "Cама?! Да я там пыталась с этой всей хитромудрой аппаратурой совладать!"
                show mt normal dress at center
                with dspr
                mt "Ладно. Хоть на дискотеке присутствовали, а не где-то там, и на том спасибо!"
                mt "Спокойной ночи!"
                hide mt with dissolve
                mi "Спасибо, Семён-кун, что не испугался вожатой!"
                $ ds_lp['mi'] += 1
                $ ds_skill_points['authority'] += 1
            else:
                window show
                play sound ds_sfx_psy
                aut "{result}Замечание вожатой правомерно. Ты ничего не можешь ему противопоставить."
                me "Ну Ольга Дмитриевна, простите Мику..."
                mt "В последний раз - прощу! И в следующий раз кого-нибудь другого назначу!"
                if ds_dance_dv:
                    mt "Уму непостижимо - Двачевская оказалась ответственнее тебя, Мику! А именно вытягивала музыку своей гитарной игрой!"
                mt "Спокойной ночи, в общем!"
                hide mt with dissolve
                $ ds_skill_points['authority'] += 1
        "Промолчать":
            window show
            mt "В последний раз - прощу! И в следующий раз кого-нибудь другого назначу!"
            if ds_dance_dv:
                mt "Уму непостижимо - Двачевская оказалась ответственнее тебя, Мику! А именно вытягивала музыку своей гитарной игрой!"
            mt "Спокойной ночи, в общем!"
            hide mt with dissolve
    window hide
    menu:
        "Предложить проводить до домика":
            window show
            me "Тебя проводить до домика?"
            show mi shy dress close at center
            with dspr
            mi "Ой, давай, конечно, Семён-кун, это так мило!"
            $ ds_lp['mi'] += 1
            scene bg ds_ext_un_night
            show mi smile dress at center
            with dissolve
            mi "Спокойной ночи, Семён-кун! Мне очень понравился сегодняшний вечер!"
            me "Cпокойной ночи."
            hide mi with dissolve
        "Попрощаться":
            window show
            me "Спокойной ночи, Мику."
            mi "И тебе!"
    "Ты тихо отступаешь в сторону своего домика."
    window hide
    
    play sound sfx_close_door_1
    
    stop ambience fadeout 1
    
    scene bg ext_house_of_mt_night
    with dissolve
    
    play ambience ambience_camp_center_night fadein 1
    
    window show
    "Ты неспешно идёшь к себе в домик, глубоко вдыхая прохладный ночной воздух."
    play sound ds_sfx_psy
    vol "Не хочется прощаться с этим днём, который выдался поистине замечательным."
    play sound ds_sfx_fys
    edr "Однако, за весь день ты дико устал, а в танец вложил все свои последние силы."
    edr "Так что ты очень хочешь спать."

    scene bg int_house_of_mt_night
    with dissolve
    
    "Рухнув на кровать, ты мысленно подводишь итоги этого дня."
    th "Безусловно, он был наполнен в основном очень приятными и запоминающимися моментами."
    th "Однако, за всё это время я так ничего и не разузнал о куда более масштабной проблеме - о том, как и с чьей лёгкой руки я попал сюда, и о том, как отсюда выбраться или хотя бы точно определить местоположение."
    th "Тем не менее, мне здесь начинает действительно нравиться."
    play sound ds_sfx_psy
    vol "Здесь тебе всё-таки было чему поучиться и что обрести, несмотря на то, что попал ты примерно на тридцать лет назад во времени."
    vol "Ведь ты уже начинаещб чувствовать, что, окажись я вдруг снова у себя дома, ты бы начал жить по-другому."
    th "А начал бы?"
    th "Возможно, мне это лишь кажется, и я бы продолжил вести свою невзрачную и пустую жизнь?"
    "В любом случае, слишком долго размышлять ты не можешь, и твои глаза закрываются сами собой."
    
    show blink
    
    pause (2)
    
    scene black
    
    "..."
    
    hide blink
    
    window hide
    
    stop ambience fadeout 1
    
    pause(3)

    jump ds_day3_dream

label ds_day3_evening_mz:
    play sound ds_sfx_mot
    per_eye "Но Жени ты не видишь."
    play sound ds_sfx_int
    lgc "Вполне ожидаемо, что она в библиотеке. Где же ей ещё быть?"
    "Ты неспешно направляешься в библиотеку."
    $ persistent.sprite_time = "night"
    scene bg ext_library_night 
    with dissolve
    "Ты подходишь к библиотеке и дёрнул ручку входной двери."
    play sound sfx_campus_door_rattle
    "Заперто."
    th "Ну тут уж самой судьбой уготовано, как говорится."
    "Ты вздыхаешь, оборачиваешь и только делаешь пару шагов..."
    play sound ds_sfx_mot
    per_hea "За дверью шорохи."
    mz "Разве неясно написано, что здесь уборка?"
    per_eye "Осмотр двери и близлежащих стен на предмет каких-нибудь надписей или табличек ничего не принёс."
    me "Но тут нет никаких надписей."
    mz "Что значит «нет»? Я тогда сейчас выйду и покажу, раз природа зрением обделила!"
    play sound sfx_unlock_door_campus
    "Дверь начали открывать."
    show mz angry glasses pioneer close at right with dissolve
    "Из приоткрытой двери выглядывает Женя, осмотрела наружную сторону двери, ничего не обнаружила, заинтересованно похлопала глазами, а затем перевела взгляд на меня."
    if ds_lp['mz'] >= 10:
        show mz bukal glasses pioneer close at right with dspr
        mz "А, это ты. Ну заходи."
    else:
        show mz angry glasses pioneer close at right  with dspr
        mz "Ты чего тут делаешь?"
        window hide
        menu:
            "Помочь":
                window show
                me "Ну... подумал, что помочь тебе надо..."
                show mz amazed glasses pioneer close at right  with dspr
                mz "Ну ладно, заходи..."
            "Посидеть с Женей":
                window show
                me "Да так, к тебе, посидеть..."
                show mz bukal glasses pioneer close at right with dspr
                mz "А я не хочу! Удачи!"
                "И она заходит обратно в библиотеку."
                th "Мда. Не вышло."
                jump ds_day3_evening_none
            "Сделать вид, что ошибся":
                window show
                me "Ой, извини, я ошибся..."
                mz "Ну и иди своей дорогой тогда!"
                hide mz with dissolve
                play sound sfx_lock_click
                "И она запирается в библиотеке."
                $ ds_lp['mz'] -= 1
                jump ds_day3_evening_none
    $ ds_lp['mz'] += 1
    play sound ds_sfx_psy
    emp "Не похоже, что она тебя ждала."
    play sound ds_sfx_psy
    vol "Не похоже, чтобы ты тоже собирался сюда приходить."
    play sound sfx_open_door_clubs_2
    "Женя отходит от двери и направляется к полкам с книгами. Ты заходишь в библиотеку и осматриваешься."
    
    scene bg int_library_night2
    with dissolve
    play music music_list["silhouette_in_sunset"] fadein 3
    
    "Внутри библиотеку освещает лишь небольшая лампа под самым потолком."
    play sound ds_sfx_mot
    per_sme "Особая библиотечная пыль с особым запахом, который ни с чем не спутаешь."
    per_sme "Микроскопические кусочки отживающих свой век собраний сочинений классиков марксизма-ленинизма."
    th "Интересно, одинаково ли пахнет пыль рядом с полками художественной литературы и с книгами по физике и химии?"
    per_eye "Проходя мимо стола, ты увидел на нём несколько пожелтевший тетрадный листок бумаги, приспособленный под табличку с аккуратно выведенным на нём «Не входить. Уборка»."
    window hide
    menu:
        "Показать Жене":
            window show
            show mz normal glasses pioneer at cleft with dspr
            "Ты поднимаешь листок и показываешь Жене. Она лишь слегка поводит бровью."
            mz "И где ты его взял?{w} Неважно, окажи услугу - повесь на дверь."
            window hide
            menu:
                "Выполнить":
                    window show
                    hide mz with dissolve
                    "Ты возвращаешься к двери, вешаешь листок на ручку и закрываешь дверь."
                    play sound sfx_close_door_campus_1
                    $ ds_lp['mz'] += 1
                "Cпросить":
                    window show
                    me "А зачем? Все же и так на дискотеке!"
                    show mz angry glasses pioneer at cleft with dspr
                    if ds_dv_invite:
                        mz "Не все. Я совершенно точно видела в окно рыжеволосую... как там её... {w}Двачевская вроде..."
                        mz "В общем, она на сцену шла! Вдруг решит и сюда залезть!"
                        play sound ds_sfx_int
                        lgc "Картина маслом: Алиса заходит в библиотеку почитать..."
                    else:
                        mz "Не знаю! Но как только начинается уборка - так вечно всё тут превращается в проходной двор!"
                    me "Ладно, повешу..."
                "Не вешать":
                    window show
                    "Ты просто откладываешь листок куда-нибудь. Женя как будто бы ничего не замечает."
                    $ ds_lp['mz'] -= 1
        "Забить":
            window show
            "Ты просто откладываешь листок в сторону."
    play sound ds_sfx_psy
    vol "Ну что же: теперь вас тут только двое и ближайшие, наверное, часа два нас никто не побеспокоит."
    play sound ds_sfx_fys
    ins "Такой шанс... ты {i}обязан{/i} его использовать!"
    show mz bukal glasses pioneer far at cleft with dspr
    play sound ds_sfx_int
    con "Вы одни в пустой библиотеке. Романтика?"
    play sound ds_sfx_psy
    aut "Чёрта с два: всё, что ты буду делать - перетаскивать туда-сюда толстенные книги. Женя вряд ли предложит что-то иное."
    th "Задерживаться тут не стоит."
    "Ты поворачиваешься к Жене. Она стоит к тебе спиной в центре библиотеки и протирает лысину на бюсте Ленина."
    window hide
    menu:
        "Спросить прямо":
            window show
            me "Какие указания?"
        "{check=savoir_faire:14}Свалить":
            if skillcheck('savoir_faire', lvl_legendary):
                window show
                play sound ds_sfx_mot
                svf "{result}Ну нафиг! Ты тихонько выходишь из библиотеки."
                scene bg ext_library_night
                with dissolve
                $ ds_lp['mz'] -= 2
                jump ds_day3_evening_none
            else:
                window show
                play sound ds_sfx_mot
                svf "{result}Ты направляешься в сторону двери..."
                show mz angry glasses pioneer far at cleft with dspr
                mz "Куда собрался?!"
                me "Да так, никуда..."
                $ ds_lp['mz'] -= 1
                me "Что делать?"
        "Ждать указаний":
            window show
    if ds_after_lunch_who == 'mz':
        mz "Значит, так. Базу данных вы сегодня со Славей сделали нормально, но вот сами книги..."
        mz "Полный бардак вы мне тут создали!"
    else:
        mz "Как это ни удивительно, Славя мне тут в книгах бардак навела, ну а про базу данных я вообще молчу! Мне её придётся самой делать!"
    mz "Поэтому..."
    mz "Видишь этот книжный шкаф?"
    "Она не отрывается от бюста Ленина, поэтому ты понимаешь не сразу, какой именно. Но затем она оборачивается и переводит взгляд на шкаф прямо перед собой."
    me "Ну, вижу."
    mz "Его не трогать."
    window hide
    menu:
        "Потрогать шкаф":
            window show
            "Ты подходишь к шкафу и трогаешь его."
            show mz angry glasses pioneer far at cleft with dspr
            mz "Ха-ха-ха, очень смешно. Я серьёзно!"
        "Принять":
            window show
            me "Хорошо."
        "Спросить":
            window show
            me "А почему?"
            mz "Потому что!"
            play sound ds_sfx_int
            rhe "Она не склонна вдаваться в подробные объяснения."
    mz "Видишь этот шкаф?"
    "Она мотает головой в сторону центрального шкафа."
    me "Вижу."
    mz "Его тоже не трогать."
    th "Ну, отлично... Что мне вообще тут делать."
    show mz normal glasses pioneer far at cleft with dspr
    "Женя оборачивается и спросила"
    mz "Ты чего ухмыляешься?"
    window hide
    menu:
        "Отговориться":
            window show
            me "Да ничего такого..."
        "Cказать прямо":
            window show
            me "А что мне собственно {i}трогать{/i}? В смысле, что делать?"
    "Она откладывает тряпку и поворачивается к тебе. А затем скрещивает руки и, оперевшись на полку, уставляется на меня."
    show mz smile glasses pioneer far at cleft with dissolve
    mz "Тебе достаётся третий шкаф, мне - второй. Твоя обязанность - достать книгу, посмотреть на название. Если ты прочитал название и ничего не понял, то просто поставь её обратно. Иначе скажи название мне. Возможно, её нужно будет переставить."
    play sound ds_sfx_int
    rhe "Что значит «прочитал и не понял название»?"
    window hide
    menu:
        "Спросить":
            window show
            me "В смысле?"
            show mz bukal glasses pioneer far at cleft with dspr
            "Женя практически не глядя достаёт из-за спины первую попавшуюся книгу и принялась вслух читать её название."
            mz "«Малыш А. И. - Формирование марксистской политической экономики». Понял что-нибудь?"
            rhe "Что за нагромождение слов?"
            me "Неа."
            mz "Вот это я и имeла ввиду."
        "Молча принять":
            window show
            me "Ладно..."
    show mz normal glasses pioneer close at cleft with dissolve
    "Она подходит ко мне и протягивает книгу."
    mz "Вот, поставишь в свой шкаф."
    hide mz with dissolve
    $ renpy.pause(2)
    show mz normal glasses pioneer far at cleft with dissolve
    "Женя немедля приступает к сортировке «по правилам»."
    hide mz with dissolve
    play sound ds_sfx_psy
    vol "И ты не медли."
    play ambience ambience_library_day fadein 2
    "Подойдя к полке, ты тянешься к ближнему нижнему углу и взял первую книгу."
    "«Нарский А. - Западноевропейская философия»"
    play sound ds_sfx_int
    enc "Не то, чтобы ты не понимал, что тут написано. Ты немного разбираешься в философии - философские треды на имиджбордах и полугодичный курс философии в универе, на который почти никто не ходил, оставили в тебе некоторый отголосок человеческой мудрости."
    play sound ds_sfx_int
    dra "Но Женя рассчитывает на то, что вы пионер семнадцати годов от роду. Понимания подобных тем от таких людей не ждут."
    play sound ds_sfx_int
    lgc "Что эта книга вообще тут делает? Они просто взяли первые попавшиеся книги и привезли их сюда? Кто вообще тут будет это читать? Люди и в большом возрасте, которые поумнее, стараются обходить такое стороной."
    enc "Имитация бурной деятельности по продвижению идеологии. Хоть тут Советский Союз и выглядит стабильнее «нашего», но с идеологий примерно та же история."
    window hide
    menu:
        "Озвучить книгу":
            window show
            me "«Западноевропейская философия»!"
            mz "Оставь её там, где взял!"
        "Молча вернуть":
            window show
    "Ты кладёшь книгу, откуда взял. Принимаешься за следующую."
    "«Иммануил Кант. Сборник сочинений»"
    enc "Классика!"
    window hide
    
    $ renpy.pause(2)
    
    window show
    "Пройдя полтора ряда, ты натыкаешься на что-то новое."
    "«Лечебные свойства овощей»"
    me "Женя, тут что-то про овощи. Про то, какие они полезные."
    mz "Оставляй там же."
    play sound ds_sfx_int
    vic "Литература становится разнообразнее."
    "Ты проходишь ещё мимо десятка книг и натыкаешься на что-то новое."
    "«Мифы Древней Греции»"
    me "Женя, тут мифы Древней Греции."
    "Женя некоторое время не отвечает."
    mz "Ты бы стал читать такое?"
    window hide
    menu:
        "Ответить положительно":
            window show
            me "Ну...{w} да. А тебе разве не было бы интересно?"
            mz "Я их уже прочитала. Просто не уверена, что такое интересно другим пионерам. Короче, неси сюда."
        "Ответить отрицательно":
            window show
            me "Не-а."
            mz "Тогда неси сюда!"
    "Ты относишь книгу Жене, а она ставит её среди стопки приключенческих книг."
    th "Дальше за работу..."
    window hide
    
    $ renpy.pause(1)
    
    $ night_time()
    
    $ persistent.sprite_time = "night"
    scene bg int_library_night2 
    with dissolve2
    
    window show
    stop ambience fadeout 2
    "Так продолжается некоторое время, пока ты не заканчиваешь со всеми книгами."
    show mz normal glasses pioneer close at cright with dissolve
    play sound sfx_open_journal
    "Ты подходишь к Жене. Кажется, она тоже закончила и пролистывает какую-то книгу, издали похожую на сборник чьих-то стихов."
    show mz bukal glasses pioneer close at cright with dissolve
    window hide
    menu:
        "Спросить":
            window show
            me "Что читаешь?"
        "Обратить на себя внимание":
            window show
            me "Я закончил!"
        "Тихо уйти":
            window show
            th "Что ж, я пойду..."
            "Но ты не успел сделать и пары шагов..."
        "Постоять и подождать":
            window show
    play sound sfx_punch_medium
    th "Женя захлопывает книгу, убирает её на полку и резко оборачивается на тебя."
    show mz normal glasses pioneer close at cright with dissolve
    mz "Чего тебе?"
    me "Я закончил."
    mz "А. Отлично."
    hide mz with dissolve
    $ renpy.pause(1)
    "Проходит некоторое время."
    show mz bukal pioneer close at cright with dissolve
    play sound ds_sfx_psy
    sug "Она уже некоторое время просто держит книгу в руках и безотрывно смотрит на тебя. Кажется. ты ей понравился."
    play sound ds_sfx_int
    lgc "Да нет. Она просто о чём-то задумалась и внимания на тебя она не обращает никакого."
    th "Интересно, о чём она думает?"
    con "И всё-таки Женя красивая. Ещё красивей она в очках, но сейчас она без них."
    con "И эта приятная стрижка. Вроде не особо аккуратная, да и локоны торчат во все стороны. Но это придаёт ей ещё больший шарм."
    play sound ds_sfx_psy
    aut "Ещё бы характер у неё был не такой скверный..."
    show mz sceptic pioneer close at cright with dspr
    mz "Ты чего на меня пялишься?"
    window hide
    menu:
        "Извиниться":
            window show
            me "А... извини."
            show mz angry pioneer close at cright with dspr
            mz "Вот и не пялься!"
        "Перевести на неё":
            window show
            me "Чего? Нет, это ты на меня пялилась!"
            show mz angry pioneer close at cright with dspr
            mz "Что? Мечтай!"
        "Сделать комплимент":
            window show
            me "Да так, просто ты красивая очень!"
            show mz scared pioneer close at cright with dspr
            mz "И что ты хочешь со мной сделать?"
            play sound ds_sfx_mot
            res "Наверное, это самая неортодоксальная реакция на комплимент."
            me "Да ничего..."
    "Она невозмутимо отводит взгляд вниз."
    show mz smile pioneer close at cright with dspr
    play sound ds_sfx_mot
    res "Ты вдруг замечаешь на её лице улыбку."
    th "Да, ситуация действительно нелепая."
    "Ты тоже улыбаешься."
    hide mz with dissolve
    window hide
    
    stop ambience fadeout 3
    stop music fadeout 3
    $ renpy.pause(2)

    me "Это... всё?"
    "Ты вздыхаешь и кое-как поднимаешься."
    if ds_lp['mz'] < 10:
        mz "Всё, можешь идти."
        "С этими словами она идёт хлопотать по чему-то. Наверное, закрывать библиотеку."
        scene black with dissolve
        jump ds_day3_evening_none
    window hide
    menu:
        "Начать уходить":
            window show
            me "Ну, я тогда пойду?"
            show mz bukal pioneer at center with dspr
            mz "Да, конечно..."
            hide mz with dissolve
            "Женя отвернулась и принялась что-то искать в книжной полке."
            th "Вот только куда я пойду?"
            "Перекидывая разные варианты в голове, я обнаружил, что у меня их всего два. И оба они мне не нравились."
            "Я так и стоял посреди библиотеки, не в состоянии сдвинутся с места. Сверлил взглядом библиотекаршу."
            show mz bukal pioneer far at center with dspr
            "Похоже, она это заметила и обернулась."
        "Уйти быстро":
            window show
            "Ты выбегаешь из библиотеки."
            scene ext_library_night
            with dissolve
            $ ds_lp['mz'] -= 1
            jump ds_day3_evening_none
        "Подождать":
            window show
            "Ты решаешь постоять в библиотеке ещё."
    mz "Ты чего-то ждёшь?"
    me "А, не... Я... Я пойду, наверное."
    "Я разворачиваешься и хаватаешься за ручку двери."
    mz "Постой."
    me "Да?"
    show mz hope pioneer far at center with dspr
    mz "Можешь тут посидеть ещё... Если хочешь, конечно же."
    "Неуверенно произнесла Женя."
    play sound ds_sfx_psy
    aut "Что, Женя не выгоняет тебя из библиотеки? Неожиданно."
    window hide
    menu:
        "Cогласиться":
            window show
        "Отказаться":
            window show
            me "Нет, я как-то не хочу отягощать тебя своим обществом."
            show mz bukal pioneer far at center with dspr
            mz "Ну и иди тогда!"
            scene bg ext_library_night
            with dissolve
            $ ds_lp['mz'] -= 2
            jump ds_day3_evening_none
    me "Ну если ты не против..."
    hide mz with dissolve
    "Ты придвигаешь стул ко столу Жени и садишься в ожидании."
    window hide
    
    $ renpy.pause(2)
    
    window show
    show mz bukal pioneer at center with dissolve
    me "Может, займёмся чем-нибудь?"
    mz "Чем?"
    me "Ну это же ты предложила тут остаться. И ты здесь заведуешь..."
    "Женя задумалась."
    $ renpy.pause(1.5)
    show mz normal pioneer at center with dspr
    mz "Можно книги отсортировать."
    play sound ds_sfx_psy
    vol "Ну нафиг!"
    "Ты вскакиваешь со стула."
    me "Я пожалуй пойду."
    show mz hope pioneer at center with dspr
    mz "Стой, это шутка же..."
    "Ты медленно присаживаешься обратно."
    
    $ renpy.pause(2)
    play music music_list["she_is_kind"] fadein 2
    show mz bukal pioneer at center with dspr
    mz "Есть у меня одна идея."
    me "Какая?"
    show mz normal pioneer at center with dspr
    mz "Ты ведь никому не расскажешь?"
    me "Не расскажешь что?"
    mz "Нет, сначала пообещай, что никому не расскажешь!"
    window hide
    menu:
        "Пообещать":
            window show
            me "Хорошо."
            show mz angry pioneer at center with dspr
            mz "Ты точно обещаешь?"
            me "Да точно, точно. Что у тебя там за идея?"
        "Пообещать, но сделать пальцы крестиком":
            window show
            th "Я ещё подумаю, сохранить ли в тайне... А сейчас пообещаю."
            me "Как скажешь."
            show mz angry pioneer at center with dspr
            mz "Ты точно обещаешь?"
            me "Да точно, точно. Что у тебя там за идея?"
        "Отказаться обещать":
            window show
            me "Не буду я обещать неведомо что! Вдруг мы тут бомбу делать будем!"
            show mz angry pioneer at center with dspr
            mz "Тогда иди отсюда!"
            me "Ну и пойду!"
            $ ds_lp['mz'] -= 1
            scene ext_library_night
            with dissolve
            play sound ds_sfx_psy
            emp "Скорее всего, для такой просьбы была причина. Зачем это упорство было?"
            jump ds_day3_evening_none
    show mz excitement pioneer at center with dspr
    "Женя расплывается в ехидной улыбке."
    play sound ds_sfx_int
    vic "Так улыбается Ульяна, когда задумывает какую-нибудь пакость."
    th "От Жени я такого не ожидал."
    show mz excitement pioneer at right with dissolve
    play sound sfx_open_cabinet_2
    $ renpy.pause(1)
    play sound sfx_salt_impact
    "Она подбегает к своему столу, открывает шкафчик и выставляет на стол два стакана."
    show mz normal pioneer at right with dspr
    mz "Значит так: ты сейчас берёшь стаканы и идёшь с ними к умывальникам. Там набираешь воды и возвращаешься."
    mz "И постарайся не попадаться никому на глаза."
    me "А это ещё зачем?"
    show mz excitement pioneer at right with dspr
    mz "Что ты постоянно вопросы всякие задаёшь? Скоро всё узнаешь, так что давай, поторапливайся."
    window hide
    menu:
        "Подчиниться":
            window show
        "Отказать":
            window show
            me "Нет, тебе надо - ты и иди!"
            show mz angry pioneer at right with dspr
            mz "Ты издеваешься?! Отправить женщину одну в ночь?!"
            mz "Всё отменяется! На выход!"
            $ ds_lp['mz'] -= 2
            scene bg ext_library_night
            with dissolve
            th "Что это было? Она так боится идти ночью?"
            play sound ds_sfx_int
            lgc "Видимо, небезосновательно. Возможно, есть неприятный опыт."
            jump ds_day3_evening_none
    play sound ds_sfx_psy
    vol "Не задерживайся."
    window hide
    
    scene black with dissolve
    $ renpy.pause(2)
    scene bg int_library_night2
    show mz bukal glasses pioneer far at right
    with dissolve
    
    window show
    "Через пару минут ты возвращаешься в библиотеку. Женя с чем-то химичит за своим столом."
    show mz bukal glasses pioneer at right with dspr
    "В руках у неё маленькое чайное ситечко, рядом лежит кипятильник, будильник и какая-то коробочка."
    me "Мы что, чай будем пить?"
    show mz excitement glasses pioneer at right with dspr
    mz "Ага!"
    "Она кладёт кипятильник в стакан, после чего берёт вилку в другую руку и смотрит на тебя."
    play sound ds_sfx_int
    rhe "Она спрашивает взглядом: «Ну что, начинаем?»"
    show mz bukal glasses pioneer at right with dspr
    "Вилка оказывается в розетке, кипятильник едва слышно гудит."
    play sound ds_sfx_int
    lgc "А почему Женя чаепитие пытается сокрыть?"
    window hide
    menu:
        "Спросить":
            window show
            me "И почему ты не хочешь никому про это рассказывать?"
            show mz amazed glasses pioneer at right with dspr
            mz "Ты что, кипятильник ведь - вещь многофункциональная! А тут лагерь, тут полно любителей взять то, что плохо лежит."
            th "Я даже знаю парочку таких."
            me "Им же потом и достанется, нет?"
            show mz confused glasses pioneer at right with dspr
            mz "Они просто скажут, что нашли его в лесу."
        "Молча ждать":
            window show
        "Отказаться и уйти":
            window show
            me "Знаешь, я как-то не хочу чай пить."
            show mz angry glasses pioneer at right with dspr
            mz "Ну и иди себе тогда!"
            $ ds_lp['mz'] -= 2
            scene bg ext_library_night
            with dissolve
            jump ds_day3_evening_none
    
    $ renpy.pause(2)
    
    play sound sfx_open_cabinet_1
    "Пока вода греется, она достаёт что-то из стола."
    play sound sfx_close_cabinet
    show mz bukal glasses pioneer at right with dspr
    mz "Семён, тебе сколько ложек сахара?"
    $ ds_day3_num_sugar = 0
    menu:
        "Не надо":
            me "Пью без сахара."
            "Женя качает головой."
            mz "Тяжеловато тебе, наверное, в столовой. Там-то только с сахаром дают."
            me "Не, нормально. Но я соскучился по обычному чаю."
        "Одну":
            $ ds_day3_num_sugar = 1
            me "Одну..."
            mz "Хорошо."
        "Две":
            $ ds_day3_num_sugar = 2
            me "Две..."
            mz "Хорошо."
        "Три":
            $ ds_day3_num_sugar = 3
            me "Три..."
            mz "Ну, хорошо..."
        "Четыре":
            $ ds_day3_num_sugar
            me "Четыре..."
            show mz sceptic glasses pioneer close with dspr
            "Женя с недоумением смотрит на тебя."
            mz "Что, на такой стакан четыре ложки?"
            me "А что такого?"
            play sound ds_sfx_int
            rhe "Она сейчас задаст фирменный вопрос «А не слипнется?»"
            "Но Женя лишь пожимает плечами."
            show mz bukal glasses pioneer close with dspr
            mz "Хорошо."
            
    "Она открывает стоящую рядом железную коробочку и достаёт оттуда пакетик с чаем, после чего высыпает чуть-чуть в ситечко для чая."
    "Затем устремляет взгляд на будильник."
    me "А..."
    show mz normal glasses pioneer at right with dspr
    mz "Тс."
    "Ты закрываешь рот."
    "Через несколько секунд Женя махом достаёт кипятильник и так же внезапно, но с долей осторожности, кладёт его в другой стакан."
    play sound ds_sfx_mot
    svf "Быстро."
    if day3_sugar_for_semen>0:
        "Затем она кладёт сахар к тебе в стакан. А потом и ситечко, после чего начинает его болтать там, пока содержимое стакана не становится похоже на чай."
    else:
        "Затем она кладёт ситечко в первый стакан, после чего начинает его болтать там, пока содержимое стакана не становится похоже на чай."
    mz "Опытным путём я выяснила, что кипятильник нужно в воде держать примерно 178 секунд."
    play sound ds_sfx_int
    vic "Какая точность, однако!"
    "Через десяток секунд она достаёт ситечко и протягивает тебе стакан. Ты берёшь его в руки."
    if skillcheck('pain_threshold', lvl_easy, passive=True):
        play sound ds_sfx_fys
        pat "{result}Горячий, но не обжигает."
    else:
        play sound ds_sfx_fys
        pat "{result}Горячо!"
    "Ты принимаешься пить чай маленькими глотками."
    window hide
    menu:
        "Cпросить, откуда чай":
            window show
            me "И где же ты отрыла всё это? Тоже в лесу?"
            show mz excitement glasses pioneer close
            mz "Хохохохо. Всё тебе скажи!"
            show mz smile glasses pioneer close with dspr
            mz "Да на самом деле, невелик труд. Просто подошла к Ольге Дмитриевне и попросила набор для чая. Я же тут каждый день сижу с утра до вечера. Так что перед ней был должок."
            show mz bukal glasses pioneer close with dspr
            "Ты глотаешь ещё раз. Женя тем временем готовит чай и себе."
            play sound ds_sfx_mot
            per_tas "Хороший чай. Конечно, не с горных склонов Шри-Ланки, но лучше того, что подают в столовой и на порядок лучше пакетиков с чаем за двадцать рублей, которые я пил дома."
            me "Спасибо, очень вкусно."
            show mz fun glasses pioneer close with dspr
            "Женя снова расплывается в ехидной улыбке."
            play sound ds_sfx_psy
            emp "Видимо, гордится собой, что у неё одной есть такой чайный набор."
            th "Не буду её отвлекать. Ей, кажется, очень приятно."
        "Поблагодарить":
            window show
            play sound ds_sfx_mot
            per_tas "Хороший чай. Конечно, не с горных склонов Шри-Ланки, но лучше того, что подают в столовой и на порядок лучше пакетиков с чаем за двадцать рублей, которые я пил дома."
            me "Спасибо, очень вкусно."
            show mz fun glasses pioneer close with dspr
            "Женя снова расплывается в ехидной улыбке."
            play sound ds_sfx_psy
            emp "Видимо, гордится собой, что у неё одной есть такой чайный набор."
            th "Не буду её отвлекать. Ей, кажется, очень приятно."
    hide mz with dissolve
    window hide
    $ renpy.pause(2)
    window show
    "Женя долго наслаждается чаем и глядит куда-то в окно, а когда делает последний глоток, то вздыхает и неожиданно возвращается к своему обычному состоянию."
    show mz normal glasses pioneer close with dspr
    mz "Отдохнул? Теперь иди и вымой стаканы."
    play sound ds_sfx_psy
    aut "Тебе хочется возразить."
    play sound ds_sfx_psy
    vol "Но всё таки ты в гостях."
    window hide
    menu:
        "Согласиться":
            window show
            "Ты идёшь в сторону умывальников."
        "Возразить":
            window show
            me "Не пойду. Тебе надо - ты и вымой!"
            show mz angry glasses pioneer with dspr
            mz "Да ты издеваешься?! Любишь кататься - люби и саночки возить!"
            mz "А раз не хочешь - больше и не заявляйся сюда!"
            $ ds_lp['mz'] -= 2
            scene bg ext_library_night
            with dissolve
            "C этими словами она выгоняет тебя из библиотеки."
            jump ds_day3_evening_none
    scene black with dissolve2
    $ renpy.pause(2)
    scene bg int_library_night2
    show mz bukal glasses pioneer at cright
    with dissolve2
    play sound sfx_close_cabinet
    "Вымыв стаканы, ты возвращаешься и отдаёшь их ей. Она убирает их куда-то в глубину стола."
    show mz normal glasses pioneer at cright with dspr
    mz "Теперь можешь идти на танцы, Семён."
    window hide
    menu:
        "Cпросить про неё":
            window show
            me "А ты собираешься?"
            show mz bukal glasses pioneer at cright with dspr
            mz "Собираюсь что?"
            me "Ну... На танцы идти."
            "Хотя, кажется, я и сам знал ответ."
            show mz normal glasses pioneer at cright with dspr
            mz "Нет. Делать мне там нечего."
            me "Неужели? А ведь это общелагерное мероприятие."
            mz "Оно добровольное, а я не заинтересована."
            "Уговаривать её на ещё одну какую-то безумную затею пионерского отряда не было смысла. Да я и сам не горел желанием туда идти."
            me "Тогда что же ты собираешься делать?"
            th "Может быть она может придумать что-нибудь получше, чем болтать конечностями под музыку?"
            mz "Спать пойду."
            th "Тоска и уныние."
        "Предложить пойти вместе":
            window show
            me "Может, вместе сходим?"
            show mz bukal glasses pioneer at cright with dspr
            mz "Нет."
            me "Почему? Это же общелагерное мероприятие."
            mz "Оно добровольное, а я не заинтересована."
            "Уговаривать её на ещё одну какую-то безумную затею пионерского отряда не было смысла. Да я и сам не горел желанием туда идти."
            me "Тогда что же ты собираешься делать?"
            th "Может быть она может придумать что-нибудь получше, чем болтать конечностями под музыку?"
            mz "Спать пойду."
            th "Тоска и уныние."
        "Уйти":
            window show
            me "Тогда пока!"
            show mz bukal glasses pioneer far at cright with dspr
            mz "Пока."
            scene bg ext_library_night
            with dspr
            jump ds_day3_evening_none
    window hide
    menu:
        "Съязвить":
            $ ds_lp['mz'] += 1
            me "Даже девяти часов нет, а ты собираешься спать?"
            show mz sceptic glasses pioneer at cright with dspr
            mz "Да. Что-то не устраивает?"
            me "Да так, ничего..."
            show mz angry glasses pioneer at cright with dspr
            mz "Нет, говори, раз уж начал!"
            me "Просто я думал, что ты придумаешь что-нибудь получше. А это как-то... обычно, наверное. И скучно."
            show mz amazed glasses pioneer at cright with dspr
            mz "Скучно?"
            show mz angry glasses pioneer at cright with dissolve
            show mz normal glasses pioneer at cright with dissolve
            "Женя мгновенно разозлилась. И так же мгновенно успокаивается."
            mz "Меня вообще не интересует, что ты там думаешь."
            mz "Иди, дрыгай руками на площади, как баран. Это уж очень оригинальное занятие."
            me "У меня самого не так много желания это делать. Но не в домике же прятаться! Прогулялась бы хоть."
            play sound ds_sfx_psy
            aut "Кот бы говорил... Ты же затворник ещё хуже неё."
            emp "С другой стороны, тебе ли не знать, насколько плох такой образ жизни. И желать ей того же не стоит."
            show mz confused glasses pioneer at cright with dissolve
            mz "Если честно... Вообще я это сделать и хотела."
            me "Тогда врёшь зачем?"
            show mz shyangry glasses pioneer at cright with dissolve
            mz "И ничего я не вру!"
            show mz bukal glasses pioneer at cright with dissolve
            mz "Просто... Если Ольга Дмтриевна узнает, то сразу причитать начнёт. Так что лучше не распространяться о таком."
            th "Уже интереснее."
            play sound ds_sfx_psy
            sug "Можно и вместе сходить, наверное."
            window hide
            menu:
                "Напроситься к ней":
                    play sound ds_sfx_psy
                    sug "А ведь если подумать, то неплохая ведь идея - прогуляться вечером по лагерю, пока пионеры всех мастей заняты на дискотеке."
                    sug "Да ещё и в компании милой библиотекарши? Что может быть лучше?"
                    me "Слушай, а можно с тобой на прогулку?"
                    show mz amazed glasses pioneer at cright with dissolve
                    $ renpy.pause(1.5)
                    mz "А, Что? Со мной?"
                    me "Если ты против, я пойму."
                    if ds_lp['mz'] >= 15:
                        $ ds_lp['mz'] += 1
                        mz "Нет-нет, можно, конечно! Я не против."
                        me "Тогда замётано."
                        show mz bukal glasses pioneer at cright with dissolve
                        mz "Что?"
                        me "Говорю, когда выдвигаемся?"
                        mz "А, сейчас. Я только закрою тут всё."
                        "Женя принялась что-то разгребать и перебирать. Я тем временем вышел на улицу."
                    else:
                        show mz angry glasses pioneer at cright with dspr
                        mz "Нет, нельзя! Ещё мне не хватало какого-то мужика рядом. Иди на танцы!"
                        me "Но..."
                        mz "На выход!"
                        scene bg ext_library_night
                        with dissolve
                        play sound ds_sfx_int
                        lgc "Такое ощущение, что ей чем-то мужчины конкретно насолили..."
                        th "Ага..."
                        jump ds_day3_evening_none
                    
                "Отбросить мысль":
                    th "Но затея так себе."
                    me "Ладно, гуляй. Я никому не скажу."
                    show mz angry glasses pioneer at cright with dissolve
                    mz "Точно? Я вас, пионеров, знаю. Смотри у меня, потом проблем не оберёшься!"
                    "Ты лишь улыбаешься."
                    show mz bukal glasses pioneer at cright with dissolve
                    me "Ладно, удачного вечера."
                    "Женя кивает тебе, после чего ты направляешься на выход."
                    window hide
                    scene black with dissolve2
                    jump ds_day3_evening_none
                
        
        "Уйти":
            th "Ну, спать так спать."
            play sound ds_sfx_int
            lgc "Если хорошенько подумать, ничего удивительного."
            play sound ds_sfx_psy
            vol "Но этот вариант не для тебя. Во-первых, потому что спать не хочется совершенно, а во-вторых, потому что на утро тебя будет ждать очередная тирада нравоучений от Ольги Дмитриевны."
            me "Ладно, тогда спокойной ночи, Женя. Ещё раз спасибо."
            "Женя кивает тебе, после чего ты направляешься на выход."
            window hide
            scene black with dissolve2
            jump ds_day3_evening_none
    window hide
    
    $ ds_day3_evening_who = 'mz'
    play sound sfx_open_door_clubs_2
    stop music fadeout 2
    scene bg ext_library_night
    with dissolve
    play ambience ambience_camp_center_night fadein 2
    $ renpy.pause(3)
    
    window show
    play sound ds_sfx_int
    con "Всё-таки тут невероятно красиво. Есть в этом лагере что-то такое нереальное и приятное."
    "Ты вдыхаешь полной грудью."
    play sound ds_sfx_mot
    per_sme "Откуда-то доносится запах росы и аромат полевых цветов."
    "Ты только приготовился было улететь куда-нибудь подальше в свои счастливые воспоминания, но вдруг из библиотеки выходит Женя."
    play sound sfx_close_door_1
    show mz normal glasses pioneer at cright with dissolve
    
    me "Пойдём?"
    mz "Да, пойдём."
    hide mz with dissolve
    $ renpy.pause(1)
    "Женя делает пару шагов вперёд, но потом останавливается и разворачивается."
    show mz amazed glasses pioneer at cright with dissolve
    mz "А куда мы пойдём?"
    me "Прогуливаться."
    show mz bukal glasses pioneer at cright with dspr
    mz "Нет, в смысле, куда именно?"
    me "Так это же твоя идея была."
    show mz shyangry glasses pioneer at cright with dspr
    mz "В смысле моя? Нет!"
    me "Ладно-ладно."
    mz "У тебя даже пожеланий нет никаких?"
    show mz bukal glasses pioneer at cright with dspr
    play sound ds_sfx_psy
    aut "Как быстро и легко инициатива перешла в твои руки."
    me "Ну, может..."
    play sound ds_sfx_int
    vic "Ты мысленно представил карту в голове."
    if ds_dv_invite:
        vic "Перед вами сцена - и там Алиса, которой ты обещал, что придёшь. И так и не пришёл."
    elif ds_whom_helped == 'dv':
        vic "Перед вами сцена. Вероятно, что там Алиса, способная испортить вам вечер."
    else:
        vic "Перед вами сцена."
    vic "Cправа от вас умывальники и лес."
    vic "А налево - площадь. Там появляться точно неразумно."
    window hide
    menu:
        "Пойти прямо":
            window show
            me "Идём прямо."
            scene bg ext_stage_normal_night
            show mz surprise glasses pioneer at center with dspr
            with dissolve
            mz "И на что мы сюда пришли?"
            if ds_dv_invite:
                show dv angry pioneer at left with dissolve
                dv "А это, видимо, наш Семён вспомнил об обещаниях, да?!"
                play sound ds_sfx_fys
                hfl "Алиса очень недовольна тобой."
                dv "А сейчас уже нашёл более миловидную девочку и решил, что на меня можно и забить!"
                show mz angry glasses pioneer at right with dspr
                mz "Что тут происходит, Семён?"
                window hide
                menu:
                    "Рассказать про Алису":
                        window show
                        me "Да тут, Жень, такое дело... Алиса хотела поиграть для меня, ну и чтобы она не обиделась..."
                        show dv rage pioneer at left with dspr
                        dv "Чтобы не обиделась?! Да иди ты куда подальше, Семён, с такими приколами!"
                        $ ds_lp['dv'] -= 1
                        hide dv with dissolve
                        play sound ds_sfx_psy
                        emp "Алисе очень обидно, что ты лишь из нежелания обидеть согласился с ней посидеть."
                        show mz normal glasses pioneer at center with dspr
                        mz "В общем, меня не интересуют ваши отношения с Двачевской... или как там её?"
                    "Притвориться шлангом":
                        window show
                        me "Да я без понятия, чего тут себе Двачевская придумала!"
                        show dv rage pioneer at left with dspr
                        dv "Ты издеваешься надо мной?! Валите отсюда!"
                        $ ds_lp['dv'] -= 2
                        hide dv with dissolve
                        show mz normal glasses pioneer at center with dspr
                        mz "В общем, меня не интересуют ваши отношения с Двачевской..."
                    "Остаться с Алисой":
                        window show
                        me "Извини, Женя, я вспомнил про то, что обещал с Алисой посидеть."
                        show mz bukal glasses pioneer at right with dspr
                        mz "Тогда я пошла! Хорошего вечера вам!"
                        $ ds_lp['mz'] -= 2
                        hide mz
                        with dissolve
                        jump ds_day3_evening_dv
                    "{check=savoir_faire:13}Cбежать":
                        window show
                        me "Извините, я пошёл!"
                        window hide
                        if skillcheck('savoir_faire', lvl_formidable):
                            window show
                            play sound ds_sfx_mot
                            svf "{result}И ты бежишь куда подальше. Аж до домика медсестры."
                            scene bg ext_aidpost_night
                            $ ds_skill_points['savoir_faire'] += 1
                            $ ds_lp['mz'] -= 2
                            $ ds_lp['dv'] -= 2
                            jump ds_day3_evening_none
                        else:
                            window show
                            play sound ds_sfx_mot
                            svf "{result}Ты пытаешься бежать, но спотыкаешься о ближайшую скамейку и падаешь."
                            play sound sfx_body_bump
                            with hpunch
                            $ ds_damage_health()
                            $ ds_skill_points['savoir_faire'] += 1
                            dv "Так, всё, я не желаю в этом цирке участвовать!"
                            hide dv with dissolve
                            show mz confused glasses pioneer at center with dspr
                            mz "Поднимайся."
                            "Ты поднимаешься."
        "Пойти направо":
            window show
            me "Идём направо."
            show mz amazed glasses pioneer at cright with dspr
            mz "Надо же, и сам сообразил!"
        "Пойти налево":
            window show
            me "Идём налево!"
            "Женя несколько удивлена, но соглашается пойти за тобой."
            scene ext_square_night_party
            show mz confused glasses pioneer at center with dspr
            with dissolve
            mz "И зачем мы сюда припёрлись?!"
            me "Ну..."
            show el angry pioneer at right
            show mz confused glasses pioneer at left with dspr
            with dissolve
            el "Вот как, значит, Семён? Я к тебе со всей добротой, а ты уводишь МОЮ Женю?!"
            $ ds_lp['el'] -= 2
            play sound ds_sfx_fys
            hfl "Так. Он настроен агрессивно. Нанеси упреждающий удар."
            play sound ds_sfx_psy
            aut "Поддерживаю. Покажи себя {i}настоящим{/i} мужчиной перед Женей."
            play sound ds_sfx_psy
            emp "Ну нет, может, сможем мирно решить?"
            hfl "Безполезно. Такие дела между самцами не решаются мирно."
            play sound ds_sfx_psy
            vol "Тут куча народу. Эскалация конфликта может привлечь нежелательное внимание."
            play sound ds_sfx_psy
            sug "Попробуй Электроника заболтать."
            play sound ds_sfx_fys
            phi "Ты должен показать, кто тут хозяин и мужик! Уж точно не он!"
            window hide
            menu:
                "{check=half_light:11}Атаковать первым":
                    if skillcheck('half_light', lvl_up_medium):
                        window show
                        play sound sfx_lena_hits_alisa
                        hfl "{result}Ты чёткими, резкими движениями даёшь Электронику оплеуху."
                        show el shocked pioneer at right
                        show mz rage glasses pioneer at left
                        with dspr
                        hfl "Он не ожидал такого развития событий."
                        $ ds_lp['el'] -= 2
                        $ ds_skill_points['half_light'] += 1
                        emp "Однако, ты забыл про Женю. Ваша игра в самцов её определённо не обрадовала."
                        mz "Что вы тут устроили, идиоты?!"
                        el "Это он первый начал!"
                        show mt rage dress at center
                        with dissolve
                        mt "Меня не интересует, кто тут первый начал! Виноваты оба! Что за драка посреди дискотеки?!"
                        mt "Кстати, Женя, почему я тебя только сейчас увидела?"
                        mz "Ну спасибо..."
                        play sound ds_sfx_int
                        rhe "Это в твою сторону."
                        $ ds_lp['mz'] -= 1
                        mt "Так, значит. Семён - в домик, Электроник - в клуб! Увижу вас рядом - будете весь день мешки с сахаром таскать!"
                        $ ds_karma -= 20
                        el "Но!"
                        mt "Никаких «но»! Я слышала, как ты проявлял агрессию к Семёну!"
                        hide mt with dissolve
                        show el angry pioneer at center
                        with dspr
                        el "Я ещё поквитаюсь с тобой, Семён..."
                        hide el with dissolve
                        jump ds_day3_evening_none
                    else:
                        window show
                        hfl "{result}К сожалению, ты недостаточно быстро атакуешь. Электронику удаётся перехватить инициативу и нанести удар тебе."
                        play sound sfx_lena_hits_alisa
                        with hpunch
                        $ ds_damage_health()
                        $ ds_skill_points['half_light'] += 1
                        show mz rage glasses pioneer at left
                        with dspr
                        mz "Что ты себе позволяешь, Электроник?!"
                        el "Я... я за тебя..."
                        mz "А я этого не просила!"
                        show mt rage dress at center
                        with dissolve
                        mt "Да, Сыроежкин, что это тут за драка?!"
                        show el upset pioneer at right
                        with dspr
                        el "Cемён тут..."
                        mt "Cемён просто пришёл на дискотеку с девушкой! А ты с кулаками на него!"
                        el "Но..."
                        mt "Но ты, Пёрсунов, тоже хорош! Тоже полез драться! Вы, мальчики, не можете не драться?!"
                        mz "Нет, не могут, видимо!"
                        mt "Кстати, Женя, почему я тебя только сейчас увидела?"
                        mz "Ну спасибо..."
                        play sound ds_sfx_int
                        rhe "Это в твою сторону."
                        $ ds_lp['mz'] -= 1
                        mt "Так, значит. Семён - в домик, Электроник - в клуб! Увижу вас рядом - будете весь день мешки с сахаром таскать!"
                        $ ds_karma -= 20
                        el "Но!"
                        mt "Никаких «но»! Я слышала, как ты проявлял агрессию к Семёну!"
                        hide mt with dissolve
                        show el angry pioneer at center
                        with dspr
                        el "Я ещё поквитаюсь с тобой, Семён..."
                        hide el with dissolve
                        jump ds_day3_evening_none
                "Позвать вожатую":
                    window show
                    me "ОЛЬГА ДМИТРИЕВНА!"
                    show el scared pioneer at right
                    with dspr
                    el "Подлый трус, чуть что - вожатую зовёшь..."
                    aut "Твои действия выглядят именно так."
                    $ ds_damage_morale()
                    show mt surprise dress at center
                    with dissolve
                    mt "Что случилось? Кто звал?"
                    me "А Электроник тут хотел меня побить!"
                    el "И ничего я не хотел... это он придумал!"
                    show mz bukal glasses pioneer at left
                    with dspr
                    mz "Хотел. Меня хотел себе присвоить!"
                    mt "Кстати, Женя, почему я тебя только сейчас увидела?"
                    mz "Ну спасибо..."
                    play sound ds_sfx_int
                    rhe "Это в твою сторону."
                    $ ds_lp['mz'] -= 1
                    mt "Так, значит. Семён - в домик, Электроник - в клуб! Увижу вас рядом - будете весь день мешки с сахаром таскать!"
                    $ ds_karma -= 20
                    el "Но!"
                    mt "Никаких «но»! Я слышала, как ты проявлял агрессию к Семёну!"
                    hide mt with dissolve
                    show el angry pioneer at center
                    with dspr
                    el "Я ещё поквитаюсь с тобой, Семён..."
                    hide el with dissolve
                    jump ds_day3_evening_none
                "{check=reaction_speed:13}Ждать дальнейшего развития событий":
                    window show
                    me "Ну и что дальше?"
                    "Электроника твоё спокойствие раззадоривает ещё больше."
                    window hide
                    if skillcheck('reaction_speed', lvl_formidable):
                        window show
                        play sound ds_sfx_mot
                        res "{result}Электроник пытается ударить тебя, но ты вовремя определяешь направление атаки и отражаешь её."
                        show el shocked pioneer at right
                        with dspr
                        el "Да ты..."
                        $ ds_skill_points['reaction_speed'] += 1
                        show mz rage glasses pioneer at left
                        with dspr
                        mz "Что ты себе позволяешь, Электроник?!"
                        el "Я... я за тебя..."
                        mz "А я этого не просила!"
                        show mt rage dress at center
                        with dissolve
                        mt "Да, Сыроежкин, что это тут за драка?!"
                        show el upset pioneer at right
                        with dspr
                        el "Cемён тут..."
                        mt "Cемён просто пришёл на дискотеку с девушкой! А ты с кулаками на него!"
                        el "Но..."
                        $ ds_lp['mz'] -= 1
                        mt "Так, значит. Электроник - в клуб! Увижу тебя рядом с Семёном - будешь весь день мешки с сахаром таскать!"
                        $ ds_karma -= 20
                        el "Но!"
                        mt "Никаких «но»!"
                        hide mt with dissolve
                        show el angry pioneer at center
                        with dspr
                        el "Я ещё поквитаюсь с тобой, Семён..."
                        hide el with dissolve
                        mt "А вы, так уж и быть, можете идти! Но чтобы позже вернулись!"
                        "Вы уходите в сторону столовой."
                        scene bg ext_dining_hall_away_night
                        show mz bukal glasses pioneer at center
                        with dissolve
                        mz "Ну, хоть танцевать не заставила, уже неплохо..."
                        me "Ага... куда идём?"
                    else:
                        window show
                        play sound ds_sfx_mot
                        res "{result}И тут Электроник внезапно атакует тебя. Ты не успеваешь среагировать"
                        play sound sfx_lena_hits_alisa
                        with hpunch
                        $ ds_damage_health()
                        show el smile pioneer at right
                        with dspr
                        el "Вот так-то!"
                        $ ds_skill_points['reaction_speed'] += 1
                        show mz rage glasses pioneer at left
                        with dspr
                        mz "Что ты себе позволяешь, Электроник?!"
                        show el surprise pioneer at right
                        with dspr
                        el "Я... я за тебя..."
                        mz "А я этого не просила!"
                        show mt rage dress at center
                        with dissolve
                        mt "Да, Сыроежкин, что это тут за драка?!"
                        show el upset pioneer at right
                        with dspr
                        el "Cемён тут..."
                        mt "Cемён просто пришёл на дискотеку с девушкой! А ты с кулаками на него!"
                        el "Но..."
                        $ ds_lp['mz'] -= 1
                        mt "Так, значит. Электроник - в клуб! Увижу тебя рядом с Семёном - будешь весь день мешки с сахаром таскать!"
                        el "Но!"
                        mt "Никаких «но»!"
                        hide mt with dissolve
                        show el angry pioneer at center
                        with dspr
                        el "Я ещё поквитаюсь с тобой, Семён..."
                        hide el with dissolve
                        mt "А вы, так уж и быть, можете идти! Но чтобы позже вернулись!"
                        "Вы уходите в сторону столовой."
                        scene bg ext_dining_hall_away_night
                        show mz bukal glasses pioneer at center
                        with dissolve
                        mz "Ну, хоть танцевать не заставила, уже неплохо..."
                        mz "С тобой-то всё нормально?"
                        me "Ага... куда идём?"
                "{check=suggestion:16}Уболтать Электроника":
                    if skillcheck('suggestion', lvl_godly):
                        window show
                        sug "{result}Говори о чём угодно. Главное - сбить темп."
                        me "Слушай, Электроник, а как там у вас с Шуриком дела?"
                        el "Какое тебе дело?!"
                        me "Ну, мне интересно, что там у вас с роботом."
                        el "Ты сейчас серьёзно?! Отбиваешь мою девушку, а теперь про робота спрашиваешь?!"
                        me "Твою девушку? У тебя есть девушка? Если так - поздравляю!"
                        el "Да, есть. И ты её у меня отбиваешь!"
                        me "Как так?! Я и не знал. Покорнейше прощу прощения."
                        me "Только кто же эта особа, покорившая сердце кибернетика?"
                        me "Погодь, а у тебя есть сердце? Не знал, не знал..."
                        el "Да, есть! И оно принадлежит Жене!"
                        me "ДА ЛАДНО?!"
                        play sound ds_sfx_int
                        dra "Вы это произносите максимально наигранно-удивлённым голосом."
                        me "Так это про Женю всё это время ты говорил?!"
                        el "Хватит мне тут зубы заговаривать!"
                        me "Я не заговариваю зубы. Я пытаюсь разобраться в ситуации."
                        me "Так ты говоришь, это Женю ты себе присвоил?"
                        el "Ну, она моя..."
                        me "Присвоил? А ты знаешь, что крепостное право уже отменили?"
                        el "Какое к чёрту крепостное право?!"
                        me "Вот и я не понимаю. Говоришь, что Женя твоя, не отпускаешь её."
                        el "Отпускаю! Правда, Жень?"
                        hide mz with dissolve
                        "Тут оказывается, что пока вы беседовали, Женя ушла."
                        el "Из-за тебя Женя ушла!"
                        hide el with dissolve
                        "Он бежит куда-то в сторону библиотеки."
                        "А тебе больше ничего не остаётся, кроме как проводить этот вечер одному."
                        $ ds_skill_points['suggestion'] += 1
                        $ ds_lp['mz'] -= 1
                        jump ds_day3_evening_none
                    else:
                        window show
                        sug "{result}Скажи ему, что тут ничего такого нет."
                        me "Да успокойся ты. Погулял просто с Женей, и всё..."
                        el "И ВСЁ?!"
                        "Вместо слов он заносит кулак и бьёт им тебе по лицу."
                        play sound sfx_lena_hits_alisa
                        with hpunch
                        $ ds_damage_health()
                        $ ds_skill_points['suggestion'] += 1
                        show el smile pioneer at right
                        with dspr
                        el "Вот так-то!"
                        $ ds_skill_points['reaction_speed'] += 1
                        show mz rage glasses pioneer at left
                        with dspr
                        mz "Что ты себе позволяешь, Электроник?!"
                        show el surprise pioneer at right
                        with dspr
                        el "Я... я за тебя..."
                        mz "А я этого не просила!"
                        show mt rage dress at center
                        with dissolve
                        mt "Да, Сыроежкин, что это тут за драка?!"
                        show el upset pioneer at right
                        with dspr
                        el "Cемён тут..."
                        mt "Cемён просто пришёл на дискотеку с девушкой! А ты с кулаками на него!"
                        el "Но..."
                        $ ds_lp['mz'] -= 1
                        mt "Так, значит. Электроник - в клуб! Увижу тебя рядом с Семёном - будешь весь день мешки с сахаром таскать!"
                        el "Но!"
                        mt "Никаких «но»!"
                        hide mt with dissolve
                        show el angry pioneer at center
                        with dspr
                        el "Я ещё поквитаюсь с тобой, Семён..."
                        hide el with dissolve
                        mt "А вы, так уж и быть, можете идти! Но чтобы позже вернулись!"
                        "Вы уходите в сторону столовой."
                        scene bg ext_dining_hall_away_night
                        show mz bukal glasses pioneer at center
                        with dissolve
                        mz "Ну, хоть танцевать не заставила, уже неплохо..."
                        mz "С тобой-то всё нормально?"
                        me "Ага... куда идём?"
                "{check=savoir_faire:11}Убежать одному":
                    if skillcheck('savoir_faire', lvl_up_medium):
                        window show
                        play sound ds_sfx_mot
                        svf "{result}Тикаем!"
                        scene bg ext_dining_hall_away_night:
                            zoom 1.05 anchor (48,27)
                            ease 0.20 pos (0, 0)
                            ease 0.20 pos (25,25)
                            ease 0.20 pos (0, 0)
                            ease 0.20 pos (-25,25)
                            repeat
                        with dissolve
                        "И ты убегаешь."
                        scene bg ext_dining_hall_away_night
                        th "Фух, драки удалось избежать..."
                        play sound ds_sfx_psy
                        vol "Только вот Женю ты бросил с ней..."
                        $ ds_damage_morale()
                        th "Ладно..."
                        jump ds_day3_evening_none
                    else:
                        window show
                        play sound ds_sfx_mot
                        svf "{result}Но ты спотыкаешься о землю и падаешь."
                        play sound sfx_body_fall
                        with vpunch
                        $ ds_damage_health()
                        $ ds_skill_points['savoir_faire'] += 1
                        "А тут ещё Электроник..."
                        show el laugh pioneer at right
                        with dspr
                        el "Ну как тебе, побежал, да даже сбежать не смог?"
                        $ ds_damage_morale()
                        show mz rage glasses pioneer at left
                        with dspr
                        mz "Так, прекращай!"
                        el "Ну как же, тут вот у нас неудачник!"
                        mz "Я пошла! Удачи!"
                        hide mz with dissolve
                        show el shocked pioneer at right
                        with dspr
                        el "Подожди, Жень..."
                        show el angry pioneer far at fright
                        with dspr
                        el "Я тебе припомню это..."
                        hide el with dissolve
                        jump ds_day3_evening_none
                "{check=savoir_faire:13}Убежать с Женей":
                    if skillcheck('savoir_faire', lvl_formidable):
                        window show
                        play sound ds_sfx_mot
                        svf "{result}Тикаем!"
                        me "Бежим, Женя!"
                        scene bg ext_dining_hall_away_night:
                            zoom 1.05 anchor (48,27)
                            ease 0.20 pos (0, 0)
                            ease 0.20 pos (25,25)
                            ease 0.20 pos (0, 0)
                            ease 0.20 pos (-25,25)
                            repeat
                        with dissolve
                        "И вы убегаете."
                        scene bg ext_dining_hall_away_night
                        show mz sad glasses pioneer at center
                        th "Фух, драки удалось избежать..."
                        mz "Да, чего-то он как-то слишком агрессивный... не таким я его знала..."
                        me "Да я тоже не ожидал..."
                        me "Куда пойдём?"
                    else:
                        window show
                        play sound ds_sfx_mot
                        svf "{result}Но ты спотыкаешься о землю и падаешь."
                        play sound sfx_body_fall
                        with vpunch
                        $ ds_damage_health()
                        $ ds_skill_points['savoir_faire'] += 1
                        "А тут ещё Электроник..."
                        show el laugh pioneer at right
                        with dspr
                        el "Ну как тебе, побежал, да даже сбежать не смог?"
                        $ ds_damage_morale()
                        show mz rage glasses pioneer at left
                        with dspr
                        mz "Так, прекращай!"
                        el "Ну как же, тут вот у нас неудачник!"
                        mz "Я пошла! Удачи!"
                        hide mz with dissolve
                        show el shocked pioneer at right
                        with dspr
                        el "Подожди, Жень..."
                        show el angry pioneer far at fright
                        with dspr
                        el "Я тебе припомню это..."
                        hide el with dissolve
                        jump ds_day3_evening_none
        "Cказать, что нет идей":
            window show
            me "Нет, никаких. Всё, что есть в этом лагере, лежит за площадью, у которой лучше не появляться."
            show mz bukal glasses pioneer at cright with dspr
            mz "Хм..."
            mz "Необязательно."
    mz "Иди за мной."
    hide mz with dissolve
    "Женя отправляется через пролесок в неизвестном направлении. Ты направляешься за ней."
    window hide
    
    scene bg ext_path_night with dissolve
    $ renpy.pause(1)
    scene bg ext_playground_night with dissolve
    
    window show
    "Перед вами открывается пустующая бадминтонная площадка."
    me "Бадминтон?"
    show mz bukal glasses pioneer at center with dissolve
    mz "Ну ты ведь хотел попасть куда-нибудь минуя площадь. Отсюда уже можно идти куда угодно."
    $ volume(0.35,"music")
    play music music_list["lightness"] fadein 2
    play sound ds_sfx_mot
    per_eye "Вдали заиграла музыка. Даже здесь её отлично слышно."
    me "Кажется, от дискотеки так просто не отвертеться."
    show mz fun glasses pioneer at center with dspr
    mz "Где твой боевой дух, Семён!"
    show mz smile glasses pioneer at center with dspr
    mz "Просто нам нужно отойти чуть дальше."
    me "Куда уж дальше?"
    mz "В лес."
    me "Гулять ночью в лесу?"
    show mz bukal glasses pioneer at center with dspr
    mz "Вечером. И тут не так темно, как ты думаешь."
    show mz fun glasses pioneer at center with dspr
    mz "К тому же, если мы потеряемся, то сможем выйти обратно в лагерь, следуя за музыкой."
    mz "Давай за мной."
    hide mz with dissolve
    "Женя быстрым шагом направляется в обратном направлении. Ты даже не успеваешь ей ничего сказать."
    window hide
    $ volume(0.3,"music")
    $ renpy.pause(2)
    $ volume(0.25,"music")
    window show
    "Через минуту вы стоите у забора, за которым виднеется лес."
    show mz normal glasses pioneer at center with dissolve
    mz "Окажешь помощь даме?"
    play sound ds_sfx_psy
    aut "Звучит, будто это совсем и не вопрос, а приказ. Полное пренебрежение дамским этикетом."
    window hide
    menu:
        "Помочь":
            window show
        "Переспросить":
            window show
            me "Ты перелезть хочешь?"
            show mz bukal glasses pioneer at center with dspr
            mz "Да."
            me "И что, здесь обычного прохода нигде нет?"
            mz "Здесь - нет."
            window hide
            menu:
                "Помочь":
                    window show
                "Отказать":
                    window show
                    me "Ну нет, мы через забор не полезем!"
                    show mz angry glasses pioneer at center with dspr
                    mz "Тогда мы никуда не пойдём!"
                    hide mz with dissolve
                    me "Женя?.."
                    mz "Иди на танцы!"
                    $ ds_lp['mz'] -= 2
                    jump ds_day3_evening_none
        "Отказать":
            window show
            me "Ну нет, мы через забор не полезем!"
            show mz angry glasses pioneer at center with dspr
            mz "Тогда мы никуда не пойдём!"
            hide mz with dissolve
            me "Женя?.."
            mz "Иди на танцы!"
            $ ds_lp['mz'] -= 2
            jump ds_day3_evening_none
    play sound ds_sfx_psy
    vol "Спорить с ней бесполезно."
    "Ты подходишь вплотную к забору и подставляешь руки."
    mz "Вот так бы сразу."
    
    hide mz with dissolve
    play sound sfx_bed_squeak1
    $ renpy.pause(1)
    play sound sfx_bodyfall_1
    "Она быстро запрыгивает на тебя и ловко перемахивает через забор. Ты даже моргнуть глазом не успеваешь."
    mz "Сам справишься?"
    play sound sfx_bed_squeak1
    $ renpy.pause(1)
    if skillcheck('savoir_faire', lvl_medium, passive=True):
        play sound ds_sfx_mot
        svf "{result}Ты угрюмо лезешь на забор и неожиданно для себя так же шустро перелезаешь."
        play sound sfx_bodyfall_1
        svf "Видимо, сказывается то, что я сижу в теле семнадцатилетнего пацана."
    else:
        play sound ds_sfx_mot
        svf "{result}Однако, перелезаешь через забор ты с трудом."
        svf "В итоге ты кубарем скатываешься на землю."
        play sound sfx_bodyfall_1
        with vpunch
        $ ds_damage_health()
    "Женя уже нашла какую-то тропинку и уходит куда-то вглубь леса."
    "Миновав несколько деревьев, ты выходишь на ту же тропинку."
    window hide
    
    $ persistent.sprite_time = "night"
    scene bg ext_path_night with dissolve
    play sound sfx_bush_leaves
    stop music fadeout 5
    $ renpy.pause(1)
    
    window show
    "Женя была права - тут действительно светло, как и во всё остальном лагере."
    th "Интересно, такая яркая луна - это тоже причуды лагеря или нет? Ничего подобного в своём прошлом я вспомнить не могу."
    play sound ds_sfx_int
    enc "Скорее дело в том, что тут воздух более чистый, нежели в мегаполисе. Намного более чистый."
    window hide
    menu:
        "Идти дальше":
            window show
        "Спросить о направлении":
            window show
            show mz bukal glasses pioneer close with dissolve
            me "И куда ты меня тащишь?"
            show mz sceptic glasses pioneer close with dspr
            mz "Во-первых, ты сам за мной поплёлся."
            mz "А во-вторых, сначала сам назвал меня скучной, а теперь сам ведёшь себя как зануда."
            window hide
            menu:
                "Отступить":
                    window show
                "Возразить":
                    window show
                    me "Ну не ночью же гулять по лесу."
                    show mz bukal glasses pioneer close with dspr
                    mz "А когда?"
                    me "Утром."
                    mz "Я в библиотеке."
                    me "А днём?"
                    mz "Я в библиотеке."
                    me "И вечером?"
                    "Она лишь пожимает плечами."
                    window hide
                    menu:
                        "Оценить времяпровождение в библиотеке положительно":
                            window show
                            me "Ну знаешь... Не так уж это плохо."
                            me "Мне такое по душе. Может даже перестали бы меня так бешено гонять по лагерю."
                            show mz laugh glasses pioneer close with dspr
                            mz "Не перестанут."
                            show mz fun glasses pioneer close with dspr
                            mz "И вообще, не мужское это дело - штаны просиживать, когда столько девушек вокруг, которым нужна помощь."
                            mz "На кого ты нас оставишь, Семён? На кибернетиков?"
                        "Оценить времяпровождение в библиотеке отрицательно":
                            window show
                            me "Как скучно... Целый день в библиотеке!"
                            mz "Именно."
                            play sound ds_sfx_mot
                            res "Ей {i}неинтересно{/i} сидеть в библиотеке?"
                            me "В смысле? Тебе не по душе сидеть в библиотеке?"
                        "Промолчать":
                            window show
                    $ renpy.pause(2)
                    show mz bukal glasses pioneer close with dspr
                    mz "Может, мне тоже бы было это по душе, если бы я сама выбрала такой режим дня."
                    me "А разве это не твой выбор?"
                    mz "В библиотеке я сижу уж точно не по своему желанию, а просто потому, что больше некого послать. Нет никого, кто был бы хоть немного ответственным и разбирался в книгах."
                    mz "Но я сюда отдыхать приехала. Мне так же интересно иногда прогуляться по лагерю. И с людьми поговорить."
                    $ volume(1,"music")
                    window hide
                    menu:
                        "Cпросить про круг общения":
                            window show
                            me "И с кем ты общаешься?"
                            mz "Славя. Потом...{w} Виола Церновна! А ещё..."
                            show mz confused glasses pioneer close with dissolve
                            play sound ds_sfx_int
                            rhe "Больше она никого назвать не может."
                            me "Ясно."
                        "Усомниться в общительности":
                            window show
                            me "Не похоже, чтобы ты была разговорчивой."
                            show mz normal glasses pioneer close with dspr
                            mz "О чём ты?"
                            me "Ну, ты второй день подряд вместо того, чтобы вместе со всеми проводить время, куда-то убегаешь."
                            mz "Просто не люблю, когда шумно. И не интересно мне."
                            show mz hope glasses pioneer close with dspr
                            mz "Это же не значит, что я не могу с другими людьми разговаривать. Просто у нас интересы разные."
                            me "Я бы так не сказал."
                            show mz normal glasses pioneer close with dspr
                            mz "Тогда скажи по-другому."
                            me "Если у тебя и других людей нет общих интересов, то о чём ты собираешься с ними говорить?"
                            show mz fun glasses pioneer close with dspr
                            mz "Как это о чём? О чём угодно!"
                            me "И как, получается? Сколько у тебя собеседников в лагере?"
                            show mz excitement glasses pioneer close with dspr
                            mz "Славя. Потом...{w} Виола Церновна! А ещё..."
                            show mz confused glasses pioneer close with dissolve
                            play sound ds_sfx_int
                            rhe "Больше она никого назвать не может."
                            me "Ясно."
                        "Cказать про себя":
                            window show
                            me "А я вот не знаю насчёт разговоров с людьми... Мне и поговорить-то не с кем!"
                    show mz hope glasses pioneer close with dspr
                    mz "Ну с тобой же я общаюсь сейчас."
                    show mz sad glasses pioneer close with dspr
                    mz "Или тебе не нравится?"
                    window hide
                    menu:
                        "Cказать, что нравится":
                            window show
                            me "Мне нравится!"
                        "Cказать, что устраивает":
                            window show
                            me "Меня всё устраивает!"
                        "Ответить отрицательно":
                            window show
                            me "Ну, знаешь..."
                            "Она как будто не воспринимает тебя."
                    show mz laugh glasses pioneer close with dspr
                    mz "Ну вот, видишь!"
                    hide mz with dissolve

                    play sound ds_sfx_psy
                    vol "И не возразишь."
                    vol "Она права, ведь интересы у вас по понятным причинам разнятся. Но вот мы с ней общаемся, вполне легко."
                    vol "И странно, что ты не чувствуешь рядом с ней никакого напряжения. Хотя она меня и водит по всяким лесам. И чуть ли не шипит иногда как кошка."
                    vol "Но ты как будто..."
                    play sound ds_sfx_int
                    con "Как такой маленький островок спокойствия и адекватности среди аттракциона безумия."
                    play sound ds_sfx_psy
                    ine "В этом плане Женя переворачивает все ожидания. Да и не только в этом."
                    ine "Ведь что обычно при слове «библиотекарша» представляется? Какая-нибудь не очень приятная и совсем нелюдимая женщина лет за 40, помешанная на книгах. Проводит все дни в изоляции в окружении книг и потихоньку теряет связь с социумом. И с манерами."
                    play sound ds_sfx_psy
                    emp "И Женя производит ровно такое же впечатление своей резкостью."
                    emp "Но если попытаешься выслушать её, то начинаешь понимать, что она такая же девушка, просто слегка бесцеремонная."
                    emp "Да, она не совсем общительна, но это не потому, что она настолько ненавидит людей, а просто мало понимает их, а они - её."
                    play sound ds_sfx_fys
                    hfl "Или же она их {i}боится{/i}."
                    play sound ds_sfx_psy
                    vol "Тем не менее, вот он ты, гуляешь с ней по лесу, болтаешь о всяком. Можно ведь."
                    emp "Пусть она резка в общении и совсем не видит в этом проблемы."
                    if ds_semtype <= -3:
                        vol "Видимо, ты просто равняешь обитателей лагеря по себе. Ведь это ты застенчивый парень, который не выходит из своей крепости и погружён в виртуальную реальность. И который почти потерял все навыки общения в реальном мире. Но не Женя."
                    elif ds_semtype >= 3:
                        vol "Видимо, ты просто равняешь обитателей лагеря по себе. Ведь это ты циничный парень, который просто использует других людей для своих целей. И который почти потерял все навыки дружеского общения в реальном мире. Но не Женя."
                    else:
                        vol "Видимо, ты просто равняешь обитателей лагеря по себе. Ведь это ты необщительный парень, который увлечён работой и не идёт ни с кем на контакт. И который почти потерял все навыки общения в реальном мире. Но не Женя."
                    emp "Или Ольга Дмитриевна со Славей. Тебе всю мою жизнь было мало дела до других людей, поэтому тебе даже в голову не придёт мысль, что они и правда пытаются обо мне заботится, а не просто скинуть на меня всю работу."
                    emp "Или Алиса. Тебе сразу взбрело в голову, что она социопатка, но вдруг это не так? Она ведь даже ничего плохого сделать не успела. Шуточный шлепок по спине не в счёт. Вдруг на самом деле она не отбитая пацанка, а милая девушка в глубине души?"
                    vol "И так много с кем и чем. Самое страшное - ты никогда не узнаешь, в отношении чего ты ошибаешься, пока не столкнёшься с последствиями."
                    window hide

    $ set_mode_adv()

    stop music fadeout 2
    $ persistent.sprite_time = "night"
    scene bg ext_polyana_night 
    with dissolve2
    play music music_list["raindrops"]
    
    window show
    "Незаметно для тебя вы вышли на какую-то поляну."
    play sound ds_sfx_int
    con "В лунном свете она выглядит очень красиво. Блики от света луны прыгали с одного листочка на другой, с одной росинки на другую, поблёскивая разными цветами."
    window hide
    menu:
        "Прислушаться к природе":
            window show
            "Ты останавливаешься и закрываешь глаза."
            window hide
            
            show blink
            play sound sfx_tree_branches fadein 3
            
            window show
            play sound ds_sfx_psy
            ine "Мягкий шелест листьев приносит с собой умиротворение, знакомое разве что просветлённым монахам. От пронизывающего прохладного ветерка становится приятно до мурашек."
            ine "Давно ты не чувствовал себя настолько хорошо."
            th "Напомните мне, почему я так редко бываю на природе?"
            scene black
            hide blink
            play sound ds_sfx_int
            enc "Наверное, потому, что природы как таковой у тебя в округе мало. Особенно такой: яркой, ароматной и доброжелательной."
            play sound ds_sfx_psy
            vol "Вдвойне приятно не быть одному в такой момент."
            play sound ds_sfx_psy
            sug "В том мире ты едва ли найдёшь хоть одного человека, кто способен разделить с тобой подобные переживания."
            sug "А если и способен, то у всех нынче дела, с которыми они не могут расстаться, потому что на самом деле не хотят."
            vol "А и если такой свободный человек найдётся, ты сам всё спусишь на тормозах, отказываясь выходить из своего дома."
            th "Какой-то замкнутый круг."
        "Обратить внимание на Женю":
            window show
    
    scene bg ext_polyana_night 
    show mz bukal glasses pioneer far
    with dissolve2
    
    "Тем временем ты смотришь на свою спутницу. Она стоит посреди поляны и разглядывает звёздное небо. Ты подходишь поближе."
    window hide 
    
    scene stars
    
    window show
    th "Минуту назад я был восхищён природой и даже не думал, что что-то в этом мире может быть лучше.{w} Может. Это было поистине восхитительно. Столько звёзд на небе я, кажется, не видел за всю свою жизнь."
    th "Почему я раньше не обращал внимание на это? Солнце ведь несколько часов назад закатилось."
    "Женя оборачивается к тебе и жестом предлагает прилечь на траву."
    window hide
    menu:
        "Прилечь на траву":
            window show
            "Ты не отказываешься."
        "Постоять":
            window show
            me "Нет, я постою."
            mz "Ну, как хочешь."
    me "И часто ты тут бываешь?"
    mz "В первый раз."
    mz "Видишь, сколько интересного можно найти в лагере? А ты хочешь в библиотеке запереться."
    window hide
    $ renpy.pause(2)
    window show
    play sound ds_sfx_int
    enc "Разглядывая очередное скопление, ты вдруг пожалел, что не увлекаешься астрономией."
    play sound ds_sfx_psy
    ine "Но если подумать, как знание астрономии поможет тебе лучше созерцать звёздное небо? Разве глаз недостаточно?"
    window hide
    menu:
        "Cпросить Женю":
            window show
            me "Женя, а ты разбираешься в астрономии?"
            mz "Неделю назад нашла книжку в библиотеке. Прочитала половину, мало что запомнила. Что-то про карликов и гигантов."
            mz "А в одну из ночей взяла её с собой и стала соизмерять ночное небо с картой в книге. Было интересно, но не более. Больше отвлекаешься."
            me "И что запомнила оттуда?"
            mz "Хмм...{w} Ты знаешь, что чем больше температура в атмосфере звезды, тем светлее она? Самые холодные, до шести тысяч градусов, светят нам оранжевым светом. К примеру, наше солнце. Потом, где-то в районе десяти тысяч градусов, они начинают светить белым. А дальше, вплоть до шестидесяти тысяч градусов, их свечение обретает синий оттенок."
            "Я уже читал что-то подобное раньше, но решил, что в конце 80-х подобное должно быть дико интересно для любого пионера, так что тактично промолчал. Не стоит портить момент."
            mz "Однако это не всё. Помимо самих звёзд вокруг многих из них образуются туманности, которые переливаются всеми цветами радуги."
            mz "И чем дальше все эти звёзды, тем дольше согласно теории относительности их излучение движется до нас. Огромное количество тех звёзд, что мы видим сейчас на небе, уже давно мертвы."
            "Женя просто заваливала меня разрозненными фактами из книжки. Но я был не против. Половину от этого я всё равно не знал. К тому же всё это наводило меня на разные мысли."
            "Например, что я, может быть, такая же далёкая звезда, которая уже давно мертва в своей пустой квартире, а то, что сейчас лежит на этой поляне и наблюдает за звёздами, лишь остаточный слепок сознания, расслабленно растворяющийся в эфире."
            "Или что люди вот так же меняются, начинают излучать совершенно разные чувства, в зависимости от температуры их сердец."
            th "Что-то меня потянуло на графоманию, стыдно даже."
            "Я решил отчистить свой разум и просто наблюдать за звёздным небом."
        "Молча наблюдать":
            window show
    window hide
    
    $ renpy.pause(3)
    
    window show
    play sound ds_sfx_fys
    shi "Вам лучше сейчас вернуться в лагерь, иначе проблем от вожатой вам будет..."
    me "Ну что, может вернёмся?"
    "Женя никак не реагирует."
    th "Неужели спит?"
    "Ты приподнимаешься и смотришь на неё."
    scene bg ext_polyana_night
    show mz bukal glasses pioneer close at cright
    with dspr
    th "Нет, не спит."
    show mz smile glasses pioneer close at cright
    "Она с ухмылкой смотрит на тебя, потом приподнимается и улыбается."
    mz "Да, пойдём."
    "Вы поднимаетесь с травы, ещё раз смотрите на звёздное небо и отправляетесь обратно в лагерь"
    window hide
    
    stop music fadeout 4
    window hide
    scene _ext_houses_night with dissolve2

    window show
    "По какой-то неизвестной мне тропинке вы выходите к домикам."
    play sound ds_sfx_int
    vic "Кажется, здесь живёт Лена."
    $ renpy.pause(2)
    scene bg ext_house_of_mt_night_without_light with dissolve
    "Ещё несколько шагов, и вот вы уже у твоего домика."
    window hide
    menu:
        "Молча уйти":
            window show
            "А Женя возвращается к себе."
        "Пожелать спокойной ночи":
            window show
            me "Ну, спокойной ночи, Женя."
            "Сказал я неловко."
            "Женя лишь кивнула и пошла дальше."
        "Обнять Женю":
            window show
            "Ты пытаешься приобнять Женю..."
            "Но тут её настроение резко меняется. Она испугалась чего-то!"
            show mz scared glasses pioneer close at center
            with dspr
            mz "Не лезь! Отстань!"
            "И она убегает!"
            th "Да что с ней не так?"
            $ ds_lp['mz'] -= 2
    hide mz with dissolve
    "Ты поднимаешься на порог домика."
    play sound ds_sfx_psy
    ine "Но вместо того, чтобы открыть дверь и зайти внутрь, пытаешься представить, что тебя за ней ждёт."
    play sound ds_sfx_int
    lgc "Свет не горит, но это ведь ещё ничего не означает. Наверняка ведь не спит со своим синдромом вахтёра и ждёт."
    lgc "Или наоборот: с радостью забыла даже, что с ней живёт какой-то там пионер, и мирно посапывает."
    play sound ds_sfx_psy
    vol "А если всё же нет? Может что-нибудь придумать? Или правду сказать?"
    th "Ладно, решу по обстоятельствам."
    "Ты глубоко вздыхаешь и потягиваешь ручку двери."
    window hide

    play sound sfx_open_dooor_campus_1

    stop ambience fadeout 2

    $ persistent.sprite_time = "night"
    scene bg int_house_of_mt_night2 
    with dissolve

    play ambience ambience_int_cabin_night fadein 2

    window show
    "Ольга Дмитриевна уже спит."
    th "Кажется, всё обошлось."
    "Ты тихо раздеваешься, ложишься в кровать и пытаешься заснуть."
    window hide 
    pause(2)
    window show
    "Но у тебя ничего не получается. Вместо этого ты долго ворочаешься, и сон никак не идёт."
    play sound ds_sfx_psy
    ine "В голове крутятся мысли о прошедшем дне. О поляне, о завораживающем звёздном небе. О Жене, о которой ты сегодня так много узнал…"
    th "Всё таки, никогда не знаешь, как жизнь потом повернётся?"
    th "Взять бы вот этот лагерь. Такое вообще наукой не объяснить. А вот я лежу здесь и чувствую себя живее всех живых."
    window hide

    with fade

    window show
    "…"

    stop music fadeout 3

    "Вскоре глаза начинают закрываться, и через некоторое время ты проваливаешься в сон."
    window hide

    scene bg black 
    with fade3

    $ renpy.pause(3)

    jump ds_day3_dream

label ds_day3_dance_dv:
    show dv normal dress at center
    with dissolve
    "Ты подходишь к Алисе. Она занята настройкой гитары."
    play sound ds_sfx_int
    con "Алиса в платье... выглядит очень необычно."
    show dv normal dress at center
    with dspr
    window hide
    menu:
        "Поздороваться":
            window show
            me "Привет."
            show dv angry dress at center
            with dspr
            dv "И тебе привет. Не мешай!"
        "Cпросить на платье":
            window show
            me "Ты - и в платье?"
            show dv angry dress at center
            with dspr
            dv "Вот же неожиданность, что я девушка, правда?"
            me "Да не... я про то, что ты..."
            dv "Я?"
            me "Немного не по-женски ведёшь себя."
            dv "И что? Я всё ещё девушка! И платье у меня есть!"
            me "Я понял..."
        "Похвалить платье":
            window show
            me "Классно выглядишь в платье!"
            dv "Спасибо... а теперь не мешай!"
        "Спросить про музыку":
            window show
            me "И что ты сыграешь?"
            dv "Ну... я ещё не думала. Будет музыка, не переживай! Поэтому не мешай!"
        "Пригласить потанцевать":
            window show
            me "А может ты того... станцуешь со мной?"
            dv "Не сейчас! Сейчас я буду играть!"
        "Молча наблюдать":
            window show
    "Алиса вновь принимается за гитару."
    show mi smile dress at left with dissolve
    "К ней подбегает Мику и что-то шепчет на ухо."
    dv "Поняла."
    hide mi with dissolve
    "Мику удовлетворена ответом."
    "Алиса вскидывает гитару на плечо, примеряется к струнам и..."

    "И приступает к игре."
    play sound ds_sfx_int
    con "В умении Алисы играть на гитаре сомневаться не приходится - её исполнение безупречно."
    play sound ds_sfx_mot
    com "В ней нет ни капли неуверенности. Она абсолютно поглощена игрой и ни на секунду не задумывается о возможности неудачи."
    play sound ds_sfx_psy
    aut "Тебе бы так, как этой {i}девушке{/i}! Яйца-то у тебя, а не у неё."
    play sound ds_sfx_psy
    ine "Так Алиса тебе ещё более явственно напоминает рок-звезду. У неё есть все шансы стать таковой."
    play sound ds_sfx_psy
    sug "Только не забудь это отметить, когда она закончит."
    aut "А стоит ли? Думаешь, она заслуживает такого внимания к себе? Давай не будем забывать о том, какая она агрессивная."
    play sound ds_sfx_psy
    emp "Но мы не знаем {i}причины{/i} этой агрессивности. Возможно, она не просто отбитая пацанка-социопатка."
    "Алиса совершенно не замечает тебя, и уж подавно не знает о твоих мыслях. Она играет - независимо от тебя."
    aut "А если бы не ты - сыграла бы она? Нет."
    "Наконец, она заканчивает."
    scene bg ext_square_night_party
    show dv smile dress at center
    with dissolve
    play sound sfx_simon_applause
    "Раздаются оглушительные аплодисменты."
    show mt smile dress at right
    show dv grin dress at center
    with dissolve
    mt "Давайте поблагодарим Двачевскую Алису за прекрасное - без шуток - исполнение."
    play sound ds_sfx_psy
    emp "Алиса очень довольна."
    window hide
    menu:
        "Присоединиться к аплодисментам":
            window show
            "Ты тоже начинаешь хлопать."
        "{check=volition:8}Сделать комплимент лично":
            if skillcheck('volition', lvl_easy):
                window show
                vol "{result}Ты решительно подходишь к ней."
                me "Отлично сыграла, Алиса!"
                dv "Я знаю!"
                show dv smile dress at center
                with dspr
                dv "Всё, довольно аплодисментов!"
                $ ds_skill_points['volition'] += 1
            else:
                window show
                vol "{result}Ты стесняешься привлекать внимание к себе."
                vol "Потому выкрикиваешь из толпы."
                me "Ты молодец, Алиса!"
                "Но она тебя не слышит."
                $ ds_skill_points['volition'] += 1
        "{check=authority:10}Напомнить о своей роли":
            if skillcheck('authority', lvl_medium):
                window show
                aut "{result}А ты? Напомни этой зазнавшейся особе, что если бы не ты..."
                me "Ты, конечно, молодец, Алиса, но кто организовал это дело?"
                show dv angry dress at center
                with dspr
                dv "А сыграл кто?! Я и сама могла бы договориться! Просто ты первый влез!"
                $ ds_lp['dv'] -= 1
                play sound ds_sfx_int
                dra "Пытается сохранить лицо, мессир. Ей ваше замечение не понравилось."
                $ ds_skill_points['authority'] += 1
            else:
                window show
                aut "{result}Ты не решаешься лезть к Алисе, купающейся в лучах славы."
        "Молча ждать":
            window show
    "Тут Алиса подходит к тебе."
    show dv shy dress at center
    with dspr
    "Очень близко к тебе."
    dv "Спасибо, что организовал это... На самом деле, если бы не ты..."
    "Она старается говорить как можно тише."
    window hide
    menu:
        "Похвалить":
            window show
            me "Да ладно тебе... Главное-то, кто играл."
            me "А играла ты! И это было восхитительно!"
            show dv grin dress at center
            with dspr
            dv "Я знаю! Но спасибо за похвалу!"
            $ ds_lp['dv'] += 1
        "Покичиться":
            window show
            me "Вот то-то же! Если бы не я..."
            show dv angry dress at center
            with dspr
            dv "А ты не зазнавайся!"
        "{check=instinct:8}Потребовать оплаты натурой":
            if skillcheck('instinct', lvl_easy):
                window show
                ins "{result}Она должна расплатиться с тобой. А чем девушка может мужчине отплатить?"
                me "Ну... поиграешь на моей кожаной флейте за это."
                show dv surprise dress at center
                with dspr
                play sound ds_sfx_int
                rhe "Она не поняла твоей метафоры."
                show dv angry dress at center
                with dspr
                dv "Что за чушь? Выражайся понятнее! Я не Лев Толстой!"
                me "Отсосёшь мне, говорю!"
                show dv rage dress at center
                with dspr
                dv "ТЫ ТАМ СОВСЕМ ОХРЕНЕЛ?!"
                $ ds_lp['dv'] -= 4
                dv "А не пойти ли тебе в место на букву Ж?"
                hide dv with dissolve
                play sound ds_sfx_psy
                vol "Поздравляю, ты на ровном месте всё запорол."
                ins "Да чего они все строят из себя правильных? Ведь наверняка день на шестой сами будут прыгать в койку!"
                play sound ds_sfx_int
                enc "Совершенно внезапно, это Советский Союз. Где, как известно, «секса нет»."
                play sound ds_sfx_int
                lgc "И наличие полового просвещения этого не меняет."
                jump ds_day3_evening_none
            else:
                window show
                ins "{result}Ты не находишь уместным требовать у неё секса. Или же тебя просто не привлекает Алиса."
                me "Ну... хорошо..."
        "Принять формально":
            window show
            me "Хорошо."
        "Промолчать":
            window show
            "Ты молчишь."
            show dv angry dress at center
            with dissolve
            dv "Алло! Я с тобой разговариваю, придурок!"
            me "А, да, я тут. Что такое?"
            dv "Проехали!"
            $ ds_lp['dv'] -= 1
    show dv shy dress at center
    with dspr
    "Алиса не уходит."
    play sound ds_sfx_psy
    emp "Уж не хочет ли она с тобой время провести?"
    play sound ds_sfx_psy
    sug "В любом случае, это твой шанс!"
    window hide
    menu:
        "{check=volition:11}Пригласить потанцевать":
            if skillcheck('volition', lvl_up_medium):
                window show
                play sound ds_sfx_psy
                vol "{result}Давай. Пригласи её."
                me "Может... не знаю... станцуешь со мной?"
                $ ds_skill_points['volition'] += 1
                show dv grin dress at center
                with dspr
                dv "Ну и зачем мне это?"
                play sound ds_sfx_psy
                aut "Ну раз не хочет - то и не надо. Не вздумай показывать слабость и умолять её."
                emp "Она на самом деле хочет с тобой потанцевать. Просто не хочет показывать этого."
                window hide
                menu:
                    "Начать умолять":
                        window show
                        me "Ну пожалуйста..."
                        show dv laugh dress at center
                        with dspr
                        dv "Чтобы позориться, танцуя с таким хлюпиком?"
                        $ ds_lp['dv'] -= 1
                        dv "Удачи!"
                        hide dv with dissolve
                        aut "А тебе говорили: не показывай себя слабаком. Особенно с Двачевской."
                        jump ds_day3_evening_none
                    "Демонстративно уйти":
                        window show
                me "Не хочешь - как хочешь!"
                "Ты разворачиваешься и собраешься уходить."
                "Но Алиса тебя дёргает за рукав."
                show dv shy dress at center
                with dspr
                dv "Давай..."
                $ ds_lp['dv'] += 1
            else:
                window show
                play sound ds_sfx_psy
                vol "{result}У тебя не хватает решимости. Вдруг Алиса откажет?"
                me "Алиса... а может... ну..."
                show dv angry dress at center
                with dspr
                dv "Что?"
                me "Ну не знаю... того..."
                dv "Я тоже не знаю!"
                dv "Придурок и неудачник!"
                $ ds_lp['dv'] -= 1
                hide dv with dissolve
                $ ds_damage_morale()
                sug "Она тоже хотела с тобой потанцевать. Но ждала именно твоей инициативы. А ты упустил её."
                th "Да как так-то?!"
                $ ds_skill_points['volition'] += 1
                jump ds_day3_evening_none
        "Попросить сыграть ещё":
            window show
            me "А может сыграешь ещё? Знаешь, у тебя так классно получилось!"
            show dv smile dress at center
            with dspr
            dv "А давай! Я побежала! Бывай!"
            hide dv with dissolve
            "И она вновь подбегает к «сцене»."
            "Схватив гитару, она приступает к игре."
            "А тебе остаётся только смотреть."
            jump ds_day3_evening_none
        "Спросить, зачем стои́т":
            window show
            me "Чего стоим, кого ждём?"
            show dv angry dress at center
            with dspr
            dv "Никого не ждём, придурок!"
            hide dv with dissolve
            $ ds_lp['dv'] -= 1
            play sound ds_sfx_psy
            emp "Она разозлилась на твою недогадливость."
            th "Да в смысле?! Уж не хочешь ли ты сказать..?"
            emp "Именно. Она ждала {i}твоего{/i} приглашения на танцы."
            th "А я упустил..."
            jump ds_day3_evening_none
        "Промолчать":
            window show
            me "Ты молча ждёшь, пока Алиса скажет чего-нибудь ещё."
            show dv angry dress at center
            with dspr
            dv "Приём! Я вообще-то тут стою, перед тобой!"
            me "А, да?"
            dv "Да! Ничего сказать не хочешь?"
            me "Да вроде не особо..."
            dv "Придурок!"
            hide dv with dissolve
            $ ds_lp['dv'] -= 1
            play sound ds_sfx_psy
            emp "Она разозлилась на твою недогадливость."
            th "Да в смысле?! Уж не хочешь ли ты сказать..?"
            emp "Именно. Она ждала {i}твоего{/i} приглашения на танцы."
            th "А я упустил..."
            jump ds_day3_evening_none
    "Ты берёшь левой рукой правую Алисину, а свою правую кладёшь ей на талию."
    play sound ds_sfx_mot
    res "У неё возникло мимолётное рефлекторное желание оттолкнуть тебя, но она подавила его."
    play music music_list["lightness"] fadein 3
    "Начинает играть музыка. И вы приступаете к танцу."

    scene cg ds_day3_dance_dv_shy
    with dissolve
    play sound ds_sfx_psy
    emp "На лице Алисы отчётливо читается смущение от ситуации. Ей непривычно с кем-либо танцевать."
    play sound ds_sfx_mot
    svf "Собственно, и движения это выдают - скованные, нерешительные. А вкупе с твоим не особо высоким умением танцевать это производит катастрофу."
    "Действительно, вы поочерёдно наступаете друг другу на ноги, после чего кроете последними словами. Точнее, кроет Алиса."
    scene cg ds_day3_dance_dv_normal
    with dissolve
    me "Ай!"
    dv "Ай!"
    me "Ой!"
    dv "Куда ногу ставишь, идиот?!"
    me "Я?! А ты куда? Ой!"
    dv "Это ты свои ноги под мои подсовываешь, придурок!"
    me "И ничего я не подсовываю!"
    dv "Ай! Танцуй уже нормально!"
    me "Да не могу!"
    dv "Я тоже не могу танцевать с таким увальнем!"
    me "Это я-то увалень?"
    dv "Да! Не умеешь - не берись!"
    "Решительно весь лагерь наблюдает за вашим танцем - танцем на граблях."
    dv "Так, давай уже соберись и танцуй нормально! Не хочу быть посмешищем!"
    me "Сейчас-сейчас..."
    play sound ds_sfx_psy
    vol "Ты пытаешься сконцентрироваться на танце. Но получается так себе."
    scene cg ds_day3_dance_dv_grin
    with dissolve
    play sound ds_sfx_fys
    hfl "Кажется, Алиса что-то задумала. У неё появляется заговорщическая улыбка на лице. Будь начеку!"
    dv "Слушай, мне это надоело! У меня есть идея получше!"
    me "Какая?"
    scene bg ext_square_night_party
    show dv smile dress at center
    with dissolve
    dv "Дуй на сцену и тащи гитару! И побыстрее!"
    window hide
    menu:
        "Спросить, зачем":
            window show
            me "А зачем?"
            show dv angry dress at center
            with dspr
            dv "Какой же ты непробиваемый... Ну очевидно же - играть будем!"
            window hide
            menu:
                "Согласиться":
                    window show
                    me "Хорошо, я сейчас!"
                    dv "Давай!"
                "Отказаться":
                    window show
                    me "Ну нет, мне как-то не хочется играть..."
                    dv "Ну и позорься тогда дальше один!"
                    hide dv with dissolve
                    jump ds_day3_evening_none
        "Согласиться":
            window show
            me "Хорошо, я сейчас!"
            dv "Давай!"
        "Отказаться":
            window show
            me "Ну нет, мне как-то не хочется играть..."
            dv "Ну и позорься тогда дальше один!"
            hide dv with dissolve
            jump ds_day3_evening_none
    scene bg ext_scene_normal_night
    with dissolve
    "Ты прибегаешь на сцену и приступаешь к поиску гитары."
    play sound ds_sfx_mot
    per_eye "Гитара лежит прямо перед тобой."
    "Ты подбираешь гитару и собираешься возвращаться на площадь."
    play sound ds_sfx_int
    dra "Может, вам стоит «потеряться», мессир. В действительности же вы прибережёте гитару для себя. Изольёте душу."
    play sound ds_sfx_psy
    ine "Ну нет. Душу-то излить лишним не будет, но лучше покажи её перед народом."
    window hide
    menu:
        "Вернуться на площадь":
            window show
            "Ты направляешься в сторону площади."
        "{check=interfacing:16}Остаться на сцене":
            window show
            th "Разумная идея. Как раз сбежал с танцев и теперь могу попробовать сыграть что-нибудь..."
            if skillcheck('interfacing', lvl_godly):
                window show
                play sound ds_sfx_mot
                inf "{result}Ты берёшь в руки гитару и извлекаешь первые аккорды."
                inf "Твои пальцы как будто сами начинают играть то, что надо."
                inf "Ты безошибочно зажимаешь и дёргаешь нужные струны. Музыка словно льётся из пальцев."
                $ ds_skill_points['interfacing'] += 1
                th "Получается..."
                play sound ds_sfx_int
                con "Да, получается. И получается очень недурная песня."
                play sound ds_sfx_mot
                per_eye "Похоже, твою игру услышали. Так как краем глаза ты замечаешь, что кто-то идёт к сцене."
                scene bg ext_scene_normal_night
                show dv angry dress at center
                with dissolve
                dv "Значит, мы все там тебя ждём, а ты играешь тут?! Один?!"
                me "Ну... типа того."
                dv "А ну быстро иди на площадь! Все уже заждались!"
                show dv smile dress at center
                with dspr
                dv "Кстати, неплохо получилось."
                $ ds_up_morale()
                show dv smile dress at center
                with dissolve
                dv "Так что тем более иди!"
                window hide
                menu:
                    "Пойти на площадь":
                        window show
                        me "Идём..."
                    "Отказаться":
                        window show
                        me "Не пойду я! Не хочу!"
                        show dv rage dress at center
                        with dspr
                        dv "Вот как?! Ты бы хотя бы честно сказал изначально, а не сбежал, как крыса!"
                        $ ds_lp['dv'] -= 2
                        $ ds_karma -= 5
                        dv "Удачи!"
                        hide dv with dissolve
                        jump ds_day3_evening_none
            else:
                window show
                play sound ds_sfx_mot
                inf "{result}У тебя с трудом получается зажать хотя бы один аккорд – пальцы словно завязываются узлом и отчаянно не хотят принимать нужное положение."
                inf "Когда-то у тебя получалось лучше, но сейчас ты не смог бы сыграть, наверное, и «Кузнечика»."
                th "Ладно, наверное, в другой раз лучше попробовать..."
                $ ds_skill_points['interfacing'] += 1
                play sound ds_sfx_mot
                per_eye "Кто-то идёт сюда."
                scene bg ext_scene_normal_night
                show dv angry dress at center
                with dissolve
                dv "Значит, мы все там тебя ждём, а ты играешь тут?! Один?!"
                me "Ну... типа того."
                dv "Знаешь, ещё минуту назад я бы потребовала пойти на площадь..."
                dv "Но, услышав твою божественную игру, я решила, что мы недостойны этого слышать!"
                if skillcheck('rhetoric', lvl_easy, passive=True):
                    play sound ds_sfx_int
                    rhe "{result}Она стебётся над тобой."
                else:
                    play sound ds_sfx_int
                    rhe "{result}О как, она тебя похвалила!"
                    me "Cпасибо, я старался!"
                    dv "Ты вообще что ли отсталый?! Элементарного не понял - ты сыграл отвратительно!"
                dv "В общем, всё, счастливо оставаться! Сама лучше сыграю!"
                $ ds_lp['dv'] -= 1
                window hide
                menu:
                    "{check=suggestion:14}Убедить допустить до исполнения":
                        if skillcheck('suggestion', lvl_legendary):
                            window show
                            play sound ds_sfx_psy
                            sug "{result}Ты просто репетировал. Перед публикой ты сыграешь лучше - намного."
                            me "Ну, логично, что плохо сыграл - это репетиция была. Первый подход к снаряду."
                            show dv normal dress at center
                            with dspr
                            dv "Ладно... иди уже!"
                            $ ds_skill_points['suggestion'] += 1
                        else:
                            window show
                            play sound ds_sfx_psy
                            sug "{result}Попроси её, чтобы она пустила. Она наверняка одумается и позволит."
                            me "Ну давай я сыграю..."
                            dv "Нет! Не вздумай портить инструмент своей поганой игрой!"
                            dv "Научись играть - а только потом выступай! Удачи!"
                            hide dv with dissolve
                            $ ds_skill_points['suggestion'] += 1
                            jump ds_day3_evening_none
                    "{check=authority:12}Пойти вопреки мнению Алисы":
                        if skillcheck('authority', lvl_challenging):
                            window show
                            play sound ds_sfx_psy
                            aut "{result}Не давай ей собой помыкать. Будешь ли ты играть или нет - зависит не от неё."
                            "Ты идёшь на площадь, не обращая внимания на Алису."
                            scene bg ext_scene_big_night
                            show dv angry dress at center
                            with dissolve
                            dv "Куда пошёл?! Не слышал, что я сказала?!"
                            me "Я пойду и сыграю независимо от твоего мнения."
                            dv "Да будет так! Опозоришься - не мои проблемы!"
                            $ ds_skill_points['authority'] += 1
                        else:
                            window show
                            play sound ds_sfx_psy
                            aut "{result}Алиса вселяет в тебя некоторый ужас - и ты не решаешься её ослушаться."
                            dv "В общем, посиди, поиграй ещё. Когда научишься - тогда и будешь на публике выступать!"
                            hide dv with dissolve
                            $ ds_skill_points['authority'] += 1
                            jump ds_day3_evening_none
                    "Cмириться":
                        window show
                        me "Ну ладно..."
                        dv "Вот же слабак и неудачник..."
                        $ ds_lp['dv'] -= 1
                        dv "Прощай!"
                        hide dv with dissolve
                        $ ds_damage_morale()
                        jump ds_day3_evening_none
        "Уйти":
            window show
            th "Да пошла вся эта музыка куда подальше!"
            "И ты уходишь."
            scene bg ext_scene_big_night
            with dissolve
            jump ds_day3_evening_none
    scene bg ext_square_night_party
    show dv normal dress at right
    show mi smile dress at left
    with dissolve
    dv "В общем, смотри, исполни что-нибудь простенькое. Ты вообще что-нибудь знаешь?"
    if ds_after_lunch_who == 'mi':
        mi "Не переживай, Алисочка, Семён сегодня подготовился со мной! Между прочим, он предложил."
        dv "Да, хоть ума хватило сходить в нужное место..."
    else:
        me "Ну... да..."
    dv "Отлично, попробуем."
    "C этими словами Алиса бросает тебе листок бумаги."
    "Развернув его, ты видишь, что это табулатура. Несложная."
    th "Ну что ж, сыграем."
    $ ds_played_guitar = True
    play sound ds_sfx_mot
    inf "Тебе удаётся совладать с гитарой и сыграть согласно табулатуре."
    inf "По сути твоя задача - аккмопанировать Алисе, исполняющей основную партию. И с этой задачей ты справляешься."
    play sound ds_sfx_mot
    per_eye "Мельком она посматривает на тебя. Кажется, улыбнулась."
    "Вся площадь обращена на вас."
    play sound ds_sfx_mot
    com "Но тебя это не волнует - ты просто играешь."
    "Наконец, вскоре мелодия заканчивается. «Зрительский зал» разражается аплодисментами."
    show mt smile dress at center
    with dissolve
    mt "Наши пионеры Двачевская Алиса и Пёрсунов Семён показали высочайший класс исполнения! За что мы все им благодарны!"
    mt "На этом дискотека окончена!"
    hide mt with dissolve
    "Пионеры расходятся."
    show dv shy dress at center
    with dissolve
    dv "Ну что ж... вышло неплохо..."
    window hide
    menu:
        "Похвалить Алису":
            window show
            me "Благодаря тебе!"
            show dv grin dress at center
            with dspr
            dv "А то! Но и ты тоже был неплох!"
            show dv laugh dress at center
            with dspr
            dv "Хоть и не дотягиваешь до моего уровня, конечно!"
            show dv shy dress at center
            with dspr
            dv "Однако же... не такой уж ты и неудачник."
            $ ds_up_morale()
            show dv normal dress at center
            with dspr
            dv "Чтоб сыграл не хуже на концерте в конце смены!"
        "Похвалиться":
            window show
            me "Вот, видишь, какой я! Как я сыграл!"
            show dv angry dress at center
            with dspr
            dv "Не зазнавайся!"
            dv "То, что ты сыграл и правда неплохо, ещё недостаточно! Можешь и лучше!"
            show dv normal dress at center
            with dspr
            dv "И да - тебе придётся сыграть получше, так как концерт в конце смены!"
        "Промолчать":
            window show
        "Покритиковать Алису":
            window show
            me "Ага, благодаря мне. И если бы не кое-кто..."
            show dv angry dress at center
            with dspr
            dv "Что ты сказал?!"
            me "Я говорю, что ты могла бы и лучше сыграть! А то мешала мне!"
            show dv rage dress at center
            with dspr
            dv "Тебе там от славы совсем крышу снесло?!"
            dv "Ты играл лишь бас-партию, самую простую! Вся основная мелодия была на мне! Ты не мог вытягивать выступление!"
            $ ds_lp['dv'] -= 1
            play sound ds_sfx_int
            enc "Она права - ты исполнял лишь аккомпанемент. Именно что за ней была главная роль в выступлении."
            show dv normal dress at center
            with dspr
            dv "Ладно, сегодня я добрая, не побью тебя за сказанную тобой глупость!"
    show dv smile dress at center
    with dspr
    dv "А теперь спокойной ночи!"
    window hide
    menu:
        "Предложить проводить Алису":
            window show
            me "Слушай, а может, я тебя до домика провожу."
            show dv laugh dress at center
            with dspr
            dv "Нет уж! Пока ещё не заслужил! В будущем - может быть, но не сейчас."
            $ ds_lp['dv'] += 1
            play sound ds_sfx_int
            rhe "«Пока»... «В будущем»... Похоже, она уже начинает присматриваться к возможности отношений с тобой."
            play sound ds_sfx_psy
            sug "Постарайся этот шанс не упустить."
            dv "Бывай!"
            hide dv with dissolve
        "Попрощаться":
            window show
            me "Спокойной ночи."
            hide dv with dissolve
    "Ты тоже направляешься к себе в домик."
    scene bg ext_house_of_mt_night
    show mt smile dress at center
    with dissolve
    mt "А вы молодцы, однако! Кто инициатор выступления?"
    window hide
    menu:
        "Забрать все лавры себе":
            window show
            me "Я!"
            mt "Так держать, Семён! Сумел направить энергию Двачевской в положительное русло!"
            $ ds_karma += 10
            $ ds_lp['mt'] += 1
        "Отдать инициативу Алисе":
            window show
            me "Это всё Алиса!"
            show mt surprise dress at center
            with dspr
            mt "Ничего себе... Двачевская начала предпринимать и что-то полезное для лагеря..."
            mt "Надо будет её как-нибудь отметить..."
            $ ds_lp['dv'] += 1
        "Разделить инициативу":
            window show
            me "Это была наша совместная идея."
            mt "Классно придумали! Надо будет вас с Алисой отблагодарить как-нибудь."
            $ ds_karma += 10
            $ ds_lp['mt'] += 1
        "Сказать, что инициировала Мику":
            window show
            me "Это вообще Мику предложила!"
            show mt normal dress at center
            with dspr
            mt "Ну... неудивительно, Мику такая деятельная, когда дело доходит до музыки."
            mt "Она же сама и вызвалась быть диджеем. И организовала столь успешный концерт."
            mt "Надо будет её наградить!"
            $ ds_lp['mi'] += 1
        "Отказаться отвечать":
            window show
            me "А какая разница? Главное - сыграли."
            show mt laugh dress at center
            with dspr
            mt "Ну, не хотите признаваться - ваше право."
    show mt normal dress at center
    with dspr
    mt "А теперь идём спать."
    play sound ds_sfx_fys
    edr "Она права - ты смертельно устал после сегодняшнего вечера."
    show bg int_house_of_mt_night
    with dissolve
    "Вы заходите, и ты сразу падаешь на кровать."
    th "Интересно повернулось, конечно..."
    play sound ds_sfx_int
    con "А главное - Алиса оказалась с настоящим талантом! Наверное, это главное открытие дня."
    play sound ds_sfx_psy
    sug "А ещё, похоже, ты её заинтересовал. Тебе надо удержать это достижение!"
    th "Ага, обязательно..."
    "Ты проваливаешься в сон."
    show blink
    scene black with dissolve

    jump ds_day3_dream

label ds_day3_evening_el:
    show el smile pioneer at center
    with dspr
    "Ты подходишь к скучающему в одиночестве Электронику."
    "Завидев тебя, он сразу оживляется."
    el "О, Семён, ты-то мне и нужен!"
    me "Что такое?"
    el "Ну как же, робота дальше делать!"
    me "Вот как..."
    play sound ds_sfx_psy
    vol "Лучше не лезь со своими предложениями танцев. Не поймут."
    play sound ds_sfx_int
    enc "Так-то в Союзе и статья была за мужеложество."
    play sound ds_sfx_psy
    sug "Самое разумное, чтобы провести время с ним - согласиться на робота."
    window hide
    menu:
        "Согласиться":
            window show
            me "Идём!"
            show el grin pioneer at center
            with dspr
            el "Отлично!"
            $ ds_lp['el'] += 1
        "Предложить потанцевать":
            window show
            me "А давай потанцуем?"
            show el shocked pioneer at center
            with dspr
            play sound ds_sfx_psy
            emp "Он удивлён твоим предложением."
            play sound ds_sfx_fys
            hfl "Вернее даже напуган."
            el "Эм... мне кажется, ты меня с кем-то путаешь..."
            me "Да нет, я хочу именно что с тобой станцевать!"
            el "Извини, но я, пожалуй, откажусь... я как-то хотел бы с девушкой танцевать..."
            show el scared pioneer at center
            with dspr
            el "Да и вообще, не поймут!"
            hide el with dissolve
            "Cтремглав он убегает от тебя."
            $ ds_lp['el'] += 2
            if skillcheck('empathy', lvl_formidable, passive=True):
                play sound ds_sfx_psy
                emp "{result}Такое ощущение, что ты попал {i}куда надо{/i}. Но он пока что боится признать свою {i}такую{/i} сторону."
            jump ds_day3_evening_none
        "Отказаться":
            window show
            me "Нет, спасибо, у меня... дела."
            show el upset pioneer at center
            with dspr
            el "Ну, может, поможешь?"
            me "Нет, я не хочу."
            el "А если..."
            play sound ds_sfx_int
            rhe "Он не договаривает. У него нет идей, что предложить тебе."
            me "Ладно, я пойду."
            show el sad pioneer at center
            with dspr
            el "Пока..."
            hide el with dissolve
            jump ds_day3_evening_none
    el "Идём!"
    scene bg ext_clubs_night
    show el serious pioneer at center
    with dissolve
    el "Так, только подождём тут немного... Шурик попросил выйти, так как у него дела."
    if skillcheck('instinct', lvl_easy, passive=True):
        play sound ds_sfx_fys
        ins "{result}Ага, дела... наверняка натирает себе стержень. Только почему без Электроника?"
        play sound ds_sfx_int
        th "А причём тут Электроник?"
        ins "Да я умоляю, какая девушка? Ему наврядли интересны девушки."
        th "А парни типа интересны?"
        ins "Ну, подумай... сидят постоянно с Электроником в своём клубе..."
        play sound ds_sfx_mot
        inf "Как будто бы они робота там пилят."
        ins "Ой, да это отговорка просто, чтобы им не мешали!"
    window hide
    menu:
        "Подождать с Электроником":
            window show
        "Войти в клуб":
            window show
            show el surprise pioneer at left
            with dspr
            me "Я пошёл!"
            play sound sfx_knock_door6_closed
            "Закрыто."
            window hide
            menu:
                "Постучаться":
                    window show
                    play sound sfx_knocking_door_outside
                    "Ты стучишься в дверь."
                    sh "Подожди ты там, сейчас выйду..."
                "Начать барабанить в дверь":
                    window show
                    play sound_loop sfx_knocking_door_2
                    "Ты начинаешь стучать в дверь."
                    if skillcheck('reaction_speed', lvl_medium, passive=True):
                        play sound ds_sfx_mot
                        res "{result}Осторожно! Шурик выходит."
                        stop sound_loop
                        play sound sfx_open_door_clubs
                        "Как раз в момент, когда ты прекращаешь стучать, дверь открывается, и оттуда выходит Шурик."
                        show sh rage pioneer at center
                        with dissolve
                        sh "Сказано же было: подождите!"
                        play sound sfx_close_door_clubs_nextroom
                        hide sh with dissolve
                        "И он вновь закрывается."
                    else:
                        play sound sfx_open_door_clubs
                        "Тут дверь открывается, и ты попадаешь кулаком по Шурику."
                        show sh rage pioneer at center
                        with dissolve
                        sh "Вы тут и дерётесь ещё?! Подождите, сказано вам!"
                        play sound sfx_close_door_clubs_nextroom
                        hide sh with dissolve
                        "И он вновь закрывается."
                "Вломиться в дверь":
                    window show
                    play sound sfx_open_door_strong
                    "Ты с разбегу вбегаешь в дверь, но она не поддаётся."
                    play sound ds_sfx_fys
                    phi "Дверь слишком прочная - её голыми руками не возьмёшь."
                    play sound ds_sfx_fys
                    pat "Всё, что ты заработал - синяки и ушибы."
                    $ ds_damage_health()
                "Отступить":
                    window show
                    "Ты отходишь от двери."
        "Пойти прочь":
            window show
            me "А, ну я тогда пошёл! Не могу ждать!"
            show el upset pioneer at center
            with dspr
            el "Но..."
            me "Удачи!"
            "И ты уходишь."
            scene bg ext_houses_night
            with dissolve
            jump ds_day3_evening_none
    play sound ds_sfx_psy
    ine "А почему Электроник не на дискотеке? Разве ему совсем-совсем не с кем потанцевать?"
    play sound ds_sfx_int
    lgc "Так робот же... И вообще он, похоже, увлечён наукой."
    play sound ds_sfx_psy
    emp "Есть ещё кое-что. Похоже на неразделённую любовь."
    window hide
    menu:
        "Спросить про дискотеку":
            window show
            me "А почему вы не на дискотеке?"
            show el surprise pioneer at center
            with dspr
            "Электроник вопроса не ожидал."
            el "Ну... так ведь... я же говорил про робота..."
            play sound ds_sfx_mot
            com "Замялся. Что-то есть."
            window hide
            menu:
                "Принять":
                    window show
                    me "И правда... ладно."
                    "И дальше вы молчите."
                "Начать выяснять":
                    window show
                    me "Это только из-за робота?"
                    show el angry pioneer at center
                    with dspr
                    el "Да! Что ты ко мне привязался с этим?"
                    play sound ds_sfx_psy
                    emp "Он не оценил твоего напора."
                    show el upset pioneer at center
                    with dspr
                    el "Ну, вообще, есть кое-кто, с кем я бы хотел потанцевать... и кто не пришёл..."
                    emp "Это глубоко личное. Лучше не лезть."
                    window hide
                    menu:
                        "Спросить":
                            window show
                            me "А кто это, если не секрет?"
                            show el angry pioneer at center
                            with dspr
                            el "Секрет!"
                            "Далее он не склонен разговаривать."
                            $ ds_lp['el'] -= 1
                        "Отстать":
                            window show
                            me "Ну ладно..."
        "Спросить про ход работы":
            window show
            me "Слушай, а как у вас продвигаются дела с роботом?"
            show el sad pioneer at center
            with dspr
            el "Честно говоря, неважно..."
            el "Готов он был процентов на десять... а тут ещё этот инцидент с чаем, из-за которых половину деталей менять..."
            el "В итоге Шурик завтра пойдёт в старый лагерь... как я его ни отговаривал..."
            play sound ds_sfx_psy
            sug "Опасное мероприятие..."
            el "В общем, вот так! Скорее всего, до конца смены так и не доделаем его!"
            window hide
            menu:
                "Подбодрить":
                    window show
                    me "Да ладно вам, вы справитесь! Точнее, мы вместе, втроём, справимся!"
                    show el smile pioneer at center
                    with dspr
                    el "Думаешь?"
                    me "Ага!"
                "Согласиться":
                    window show
                    me "Похоже на то..."
                "Промолчать":
                    window show
                    "Ты решаешь никак не комментировать."
        "Молча ждать":
            window show
            "Вы молча ждёте."
    show sh normal pioneer at center
    show el normal pioneer at left
    with dissolve
    sh "Заходите."
    scene bg int_clubs_male_night
    show el normal pioneer at left
    show sh normal pioneer at right
    with dissolve
    sh "Итак, смотрите. Ваша задача - перебрать все детали."
    sh "Печатные платы, на которых есть чай - убрать."
    sh "Затем берёте тряпочки и протираете корпус."
    sh "Всё поняли."
    show el smile pioneer at left
    with dspr
    el "Так точно!"
    sh "Отлично, я в кладовой."
    hide sh with dissolve
    show el serious pioneer at center
    with dspr
    el "Ну что, приступим?"
    me "Ага..."
    play sound ds_sfx_mot
    inf "Ты берёшь в руки первую печатную плату. Кажется, она чистая."
    inf "А вот следующая вся залита чаем. К тому же на ней сгорела половина деталей."
    el "Так, давай сюда. Сейчас выпишем, что сгорело!"
    "Он берёт первый попавшийся листок и выписывает на нём что-то."
    if skillcheck('instinct', lvl_medium, passive=True):
        play sound ds_sfx_fys
        ins "{result}А ты никогда не думал, что можешь быть того? Ну, по парням?"
        th "Н-нет..."
        ins "Никогда не поздно начать! Вон, как раз парень рядом с тобой в интимной обстановочке."
        "Электроник тем временем наклонился, отклянчив свой афедрон."
        ins "Это твой шанс. Прояви {i}внимание{/i} к нему!"
        window hide
        menu:
            "Схватить за зад":
                window show
                "Ты аккуратно берёшь его ягодицу в свою руку."
                $ ds_skill_points['instinct'] += 1
                $ ds_homo_traits += 1
                show el surprise pioneer at center
                with dspr
                "Электроник не понимает, что происходит."
                "А потом как понимает!"
                show el shocked pioneer at center
                with dspr
                el "Это... что?"
                me "Это я!"
                el "А что ты делаешь, позволь спросить."
                window hide
                menu:
                    "Продвигаться дальше":
                        window show
                        me "Как что? Я просто проявляю к тебе побольше {i}внимания{/i}."
                        me "Намекаю на то, что нам было бы неплохо сблизиться..."
                        "С этими словами ты перемещаешь свою руку в сторону того, что у него между ног."
                        show el scared pioneer at center
                        with dspr
                        el "Слушай... я всё понимаю, конечно, что ты много ездил по заграницам..."
                        el "Но типа..."
                        "С этими словами он убирает твою руку."
                        if skillcheck('perception', lvl_medium, passive=True):
                            play sound ds_sfx_mot
                            per_toc "{result}Ты успеваешь почувствовать кончиками своих пальцев, что его член привстал от твоих манипуляций."
                        el "В Советском Союзе как-то не принято между мужчинами... того..."
                        play sound ds_sfx_int
                        enc "Как это ни печально сознавать - это правда. СССР - не очень толерантное государство."
                        show el serious pioneer at center
                        with dspr
                        el "Давай приступать к работе!"
                        $ ds_lp['el'] += 1
                        "Ты решаешь не лезть к нему и продолжить разбираться с роботом."
                    "Признаться и отступить":
                        window show
                        me "Извини. Это был знак внимания."
                        show el surprise pioneer at center
                        with dspr
                        el "Какой знак внимания?"
                        me "Ну... такой."
                        el "Не очень понимаю тебя... давай роботом займёмся."
                        "Ты решаешь не лезть к нему и продолжить разбираться с роботом."
                    "Притвориться, что случайно":
                        window show
                        me "Извини, это случайно вышло."
                        "Ты убираешь руку."
                        show el serious pioneer at center
                        with dspr
                        el "Давай роботом займёмся."
                        "И вы приступаете к роботу."
            "{check=rhetoric:12}Сделать комплимент":
                if skillcheck('rhetoric', lvl_challenging):
                    play sound ds_sfx_int
                    rhe "{result}Похвали его работоспособность. Это уж точно «его»."
                    me "Меня так впечатляет твоё трудолюбие."
                    "Ты произносишь «так» с придыханием."
                    show el surprise pioneer at center
                    with dspr
                    el "Не очень понимаю, к чему ты это..."
                    me "Ну, знаешь... похвалить тебя захотелось!"
                    show el smile pioneer at center
                    with dspr
                    el "Давай работай лучше!"
                else:
                    play sound ds_sfx_int
                    rhe "{result}Ты не знаешь, что сказать."
                    "Поэтому ты молча продолжаешь работать."
            "Отбросить мысль":
                window show
                th "Нет, я всё же предпочитаю девушек, наверное..."
                "С этими мыслями ты продолжаешь работать."
    window hide
    $ renpy.pause(5.0)
    window show
    "Cпустя пару часов вы заканчиваете убирать повреждённые детали."
    show el smile pioneer at left
    show sh normal pioneer at right
    with dspr
    el "Всё, теперь можно и спать ложиться! Завтра надо будет доделать!"
    sh "Ага, я схожу за деталями и сделаем."
    show el serious pioneer at left
    with dspr
    el "Я всё же настаиваю, что не стоит!"
    sh "Надо!"
    window hide
    menu:
        "Поддержать Электроника":
            window show
            me "Да, я согласен с Электроником."
            el "Вот, видишь, Семён тоже считает, что не стоит!"
            sh "Всё же надо."
            show el upset pioneer at left
            with dspr
            el "Вот же упёртый..."
        "Согласиться с Шуриком":
            window show
            me "Думается мне, Шурик всё же прав."
            el "Нет! Нельзя же так!"
            sh "Надо. Не переживай, Эл, всё будет нормально."
        "Не вмешиваться":
            window show
    show sh smile pioneer at right
    with dspr
    sh "Ладно, спасибо, Семён."
    "Он протягивает тебе руку."
    window hide
    menu:
        "Пожать руку":
            window show
            "Ты пожимаешь её."
        "Не пожимать руку":
            window show
    scene bg ext_clubs_night
    show el smile pioneer at center
    with dissolve
    el "Спокойной ночи, Семён, и спасибо за помощь!"
    me "Ага, и тебе..."
    "Ты направляешься к себе. Дискотека уже давно закончилась."
    scene bg ext_house_of_mt_night
    with dissolve
    "В домике погашены окна. Ольга Дмитриевна, похоже, уже спит."
    play sound ds_sfx_fys
    hfl "А вдруг она сидит в засаде и только ждёт, как ты зайдёшь, чтобы накинуться с вопросами?"
    "Ты всё же заходишь."
    scene bg int_house_of_mt_night
    with dissolve
    "Ольга Дмитриевна спит."
    th "Отлично..."
    "Ты скидываешь с себя одежду и ложишься в кровать."
    "Пытаешься уснуть, но что-то тебя гложет..."
    th "А что, если правда попробовать не с девушкой, а с Электроником?"
    play sound ds_sfx_fys
    ins "Да, вдруг получится?"
    play sound ds_sfx_psy
    vol "В местном обществе (впрочем, и в современной тебе России тоже) это не одобряется, не забывай!"
    th "Ладно, я подумаю ещё..."
    show blink
    scene black with dissolve
    "С этими мыслями ты проваливаешься в сон."

    jump ds_day3_dream

label ds_day3_dance_ya:
    show ya surprise dress at center
    with dissolve
    "Ты подходишь к Яне. Она как всегда с вверенными ей детьми."
    show ar normal at left
    show dn normal at center
    show vt normal at right
    with dissolve
    "Мальчики как обычно выясняют друг с другом отношения."
    play sound ds_sfx_fys
    phi "Как и положено будущим мужикам - устанавливают, кто из них главный."
    "Яна пытается их разнять, но они её даже не слышат - настолько тихо она разговаривает."
    window hide
    menu:
        "{check=authority:10}Разогнать детей":
            if skillcheck('authority', lvl_medium):
                window show
                play sound ds_sfx_psy
                aut "{result}Доминировать будешь ты! Покажи им, кто тут хозяин."
                me "А ну успокоились!"
                show ar dontlike at left
                show dn surprise at center
                show vt scared at right
                with dspr
                "Ребята не решаются перечить тебе и умолкают."
                me "Мне нужно поговорить с вашей вожатой. Сидите тихо!"
                dnp "Как скажете..."
                $ ds_skill_points['authority'] += 1
                $ ds_lp['ya'] += 1
            else:
                window show
                play sound ds_sfx_psy
                aut "{result}Впрочем, решимости у тебя не больше, чем у Яны."
                me "Пожалуйста, успокойтесь..."
                show ar laugh at left
                show dn dontcare at center
                show vt laugh at right
                with dspr
                "Им всё равно. Они лишь смеются над тобой."
                vtp "Кажется, кому-то наша вожатая понравилась!"
                arp "Не будем вам мешать!"
                $ ds_skill_points['authority'] += 1
                $ ds_damage_morale()
        "Увести Яну":
            window show
        "Уйти":
            window show
            me "Извини, что побеспокоил."
            ya "Ладно..."
            hide ya
            hide ar
            hide dn
            hide vt
            with dissolve
            jump ds_day3_evening_none
    me "Так, Яна, идём, нам нужно поговорить."
    show ya normal dress close at center
    with dspr
    ya "Идём... только дети..."
    me "С ними всё будет отлично!"
    "И ты уводишь её."
    hide ar
    hide dn
    hide vt
    with dissolve
    ya "Ты чего, Семён?"
    me "Да так... хочу с тобой станцевать!"
    show ya shy dress at center
    with dspr
    ya "Ты? Со мной?"
    me "Ну да!"
    show ya shy2 dress at center
    with dspr
    ya "Ну давай..."
    play sound ds_sfx_psy
    emp "Ей очень, очень приятно, что ты обратил на неё внимание."
    play music music_list['lightness'] fadein 2
    "Начинает играть музыка. Ты протягиваешь руку Яне. Она не решается её взять."
    me "Ну... возьми руку..."
    show ya surprise dress at center
    with dspr
    ya "А... да... прости, задумалась..."
    window hide
    menu:
        "Cпросить, о чём":
            window show
            me "А о чём ты задумалась?"
            show ya normal dress at center
            with dspr
            ya "Да так... я всё думаю о том, почему именно меня назначили..."
            play sound ds_sfx_int
            lgc "Вопрос, кстати, хороший - а почему её, явно не склонную к общению, отправили возиться с детьми?"
            window hide
            menu:
                "{check=logic:8}Предложить свои варианты":
                    if skillcheck('logic', lvl_easy):
                        window show
                        lgc "{result}Хотя ответ-то прост - головотяпство руководства."
                        $ ds_skill_points['logic'] += 1
                        me "Да просто руководство не думает, когда назначает. В итоге все страдают!"
                        show ya sad dress at center
                        with dspr
                        ya "Ты думаешь... из-за меня страдают дети?"
                        play sound ds_sfx_psy
                        emp "Ляпнул ты, конечно, так ляпнул..."
                        $ ds_lp['ya'] -= 1
                        window hide
                        menu:
                            "{check=rhetoric:14}Переформулировать":
                                window show
                                me "Я не это имею ввиду. Я имею ввиду, что..."
                                if skillcheck('rhetoric', lvl_legendary):
                                    window show
                                    play sound ds_sfx_int
                                    rhe "{result}Ты имел ввиду, что она и не хочет заниматься с детьми - это ведь не её."
                                    me "...начальство назначило тебя, не поинтересовавшись тем, чего ты хочешь!"
                                    show ya surprise dress at center
                                    with dspr
                                    ya "А чего я хочу?"
                                    rhe "Э... а вот этого ты никак не ожидал!"
                                    me "Ну, с детьми же ты не хочешь заниматься?"
                                    ya "Я не знаю... никогда не думала об этом... Мне сказали - я и делаю..."
                                    th "Дела..."
                                else:
                                    window show
                                    play sound ds_sfx_int
                                    rhe "{result}Она не пригодна к работе с детьми. Объективно."
                                    me "...ну ты же не умеешь обращаться с детьми!"
                                    ya "Но я... я стараюсь..."
                                    $ ds_lp['ya'] -= 1
                                    ya "Вероятно, ты прав..."
                                    ya "А что я тогда умею?"
                                    window hide
                                    menu:
                                        "Предложить выяснить вместе":
                                            window show
                                            me "Давай вместе выяснять!"
                                            show ya surprise dress at center
                                            with dspr
                                            ya "Давай, как скажешь..."
                                        "Сказать, что не знаешь":
                                            window show
                                            me "Ну, мне-то откуда знать."
                                            ya "Да... тебе неоткуда..."
                            "Извиниться":
                                window show
                                me "Извини, я не хотел тебя обидеть!"
                                ya "Хорошо... я прощаю тебя..."
                                "Она сказала это равнодушным голосом."
                            "Подтвердить":
                                window show
                                me "Да, страдают!"
                                ya "Ну... похоже на то... наверное, я ни на что не гожусь."
                                window hide
                                menu:
                                    "Согласиться":
                                        window show
                                        me "Да, видимо."
                                        ya "Иди. Я тебя не держу."
                                        $ ds_lp['ya'] -= 1
                                        play sound ds_sfx_psy
                                        vol "Она говорит это настолько ледяным голосом, что ты не решаешься ослушаться."
                                        hide ya with dissolve
                                        jump ds_day3_evening_none
                                    "Отвергнуть":
                                        window show
                                        me "Нет! Что-то ты точно умеешь, я уверен!"
                                        show ya surprise dress at center
                                        with dspr
                                        ya "Думаешь?"
                                        me "Конечно!"
                                        ya "Как скажешь..."
                    else:
                        window show
                        lgc "{result}У тебя нет объяснений этой странности."
                        th "Лучше промолчу..."
                        $ ds_skill_points['logic'] += 1
                "Посочувствовать":
                    window show
                    me "Да, тяжело тебе, наверное..."
                    ya "Наверное..."
                    ya "Я не понимаю - а на что я гожусь тогда, если тут справиться не могу?"
                    window hide
                    menu:
                        "Предложить выяснить вместе":
                            window show
                            me "Давай вместе выяснять!"
                            show ya surprise dress at center
                            with dspr
                            ya "Давай, как скажешь..."
                        "Сказать, что не знаешь":
                            window show
                            me "Ну, мне-то откуда знать."
                            ya "Да... тебе неоткуда..."
                "Позлорадствовать":
                    window show
                    me "Я не знаю! Но раз назначили - трудись!"
                    ya "Хорошо... я и так стараюсь..."
        "Начать танцевать":
            window show
    "Она берёт твою руку, и вы приступаете к танцу."
    scene cg ds_day3_dance_ya
    with dissolve
    "Фактически весь ваш танец держится на тебе - Яна просто покорно следует за тобой."
    "Её лицо выглядит максимально равнодушным и незаинтересованным."
    play sound ds_sfx_psy
    emp "Ей просто сказали потанцевать - она и танцует."
    th "У неё вообще бывают какие-то желания?"
    play sound ds_sfx_psy
    ine "Такое ощущение, что нет. Она равнодушна к окружающему её миру. Может, оно и к лучшему?"
    play sound ds_sfx_int
    dra "Скууука!"
    window hide
    menu:
        "Спросить":
            window show
            me "Слушай, Яна... А ты совсем-совсем ничего не хочешь?"
            ya "Не... понимаю тебя..."
            me "Ну, мне просто кажется, что ты лишь следуешь чужим инструкциям. Где твои собственные желания?"
            ya "Не знаю... Я просто делаю то, что говорят..."
            window hide
            menu:
                "Мотивировать Яну":
                    window show
                    me "Но так же нельзя! Так жить нельзя! Тебе нужно жить для себя, а не для кого-то!"
                    ya "Я так не могу..."
                    me "Надо! Хочешь, я тебе помогу?"
                    ya "Ну... давай..."
                    me "C этого дня ты будешь принимать решения сама. Договорились?"
                    ya "Как скажешь..."
                    window hide
                    menu:
                        "Удовлетвориться этим":
                            window show
                            me "Вот и отлично."
                        "Потребовать перефразировать":
                            window show
                            me "Ну кто так говорит? Я же сказал - следуй своим желаниям."
                            ya "Ладно..."
                            play sound ds_sfx_psy
                            vol "Ну не сможешь ты в один момент перековать её. На это нужно время. Много времени."
                            $ ds_lp['ya'] += 1
                "Сделать комплимент":
                    window show
                    me "Знаешь, а мне нравится! Так мило это!"
                    ya "Хорошо..."
                "Отступить":
                    window show
                    me "Ладно..."
        "Не спрашивать":
            window show
    stop music fadeout 5
    "Наконец, музыка заканчивается."
    scene bg ext_square_night_party
    show ya normal dress at center
    with dissolve
    ya "Ладно, я пойду... спасибо за танец..."
    hide ya with dissolve
    "И она словно испаряется."
    jump ds_day3_evening_none

label ds_day3_evening_none:
    th "Ладно, пойдём куда-нибудь..."
    "И ты идёшь куда глаза глядят."
    scene bg ext_path_night
    with dissolve
    "Ты забредаешь в лес."
    th "Тут точно никто меня не найдёт..."
    play sound ds_sfx_fys
    edr "Ты устал - присядь и отдохни."
    "Тут как раз лежит бревно. Ты присаживаешься на него."
    play sound ds_sfx_psy
    vol "И чего ты добился за три дня в лагере? Ничего."
    th "А чего я должен был добиться?"
    vol "Ну, вероятно, хотя бы попытаться выяснить, как ты попал сюда? И для чего?"
    play sound ds_sfx_psy
    ine "Ну, похоже на то, что с попаданием сюда судьба тебе подкинула подарок. Который ты отвергаешь."
    th "Да что вы от меня хотите?! Ну не получается у меня с девушками?"
    play sound ds_sfx_fys
    shi "Думаешь? Прислушайся, прочувствуй происходящее вокруг..."
    window hide
    menu:
        "{check=shivers:11}Прислушаться к лагерю":
            if skillcheck('shivers', lvl_up_medium):
                window show
                shi "{result}Практически все собрались на дискотеке."
                shi "Особое внимание привлекает Славя. Она танцует, изображая веселье, но без особого энтузиазма."
                play sound ds_sfx_psy
                emp "Похоже, она хотела станцевать с тобой. Независимо от того, каковы у вас отношения."
                shi "У памятника стоит Мику. Она вынуждена проводить время в одиночестве - ей нужно следить за оборудованием и ставить музыку."
                if ds_dance_dv:
                    shi "Рядом с Мику - Алиса. Она играет на гитаре. Без особой радости. Словно ожидала кого-то, а он не пришёл."
                elif ds_dv_invite:
                    shi "Уйдём отсюда. На сцене сидит Алиса и бренчает на гитаре. Без особой радости. Словно ожидала кого-то, а он не пришёл."
                else:
                    shi "Уйдём отсюда. В домике сидит Алиса и скучает. Немудрено - её подружка Ульяна пляшет, а больше ей пообщаться-то и не с кем."
                    emp "Правильнее сказать, она неосознанно отталкивала от себя всех остальных."
                shi "А в медпункте сидит Лена. Она вынуждена перебирать лекарства одна. Ведь больше некому оказалось этого сделать."
                shi "В библиотеке сидит Женя, а в клубе - Электроник. Ты чувствуешь притяжение между ними... но они не сближаются!"
                shi "А Ольга Дмитриевна желала отдохнуть, но вынуждена бегать по лагерю. Она кричит «Семён!» - тебя ищет."
                th "Есть ли что-нибудь ещё? Какие-то ответы?"
                shi "Чу! {w}Ты слышишь слабый лязг двери где-то далеко. Где-то {i}под{/i} лагерем."
                shi "Вскоре раздаётся некое гудение. Оно словно грозит поглотить лагерь. Но пока что этого не случится."
                play sound ds_sfx_int
                lgc "Что это?"
                shi "Непонятно. Пока что ты этого понять не можешь. Но по крайней мере теперь ты знаешь, в каком направлении двигаться."
                th "Это может быть опасно?"
                shi "Конечно, это опасно. Настолько опасно, что это грозит разрушить мир. Или, что, возможно, ещё хуже - разрушить границу между вселенными."
                shi "И это может случиться скоро. Возможно, даже во время этой смены. Так что поторопись выяснить."
                th "Ладно..."
                $ ds_skill_points['shivers'] += 1
            else:
                window show
                shi "{result}К сожалению, тебе не хватает остроты чувств, чтобы уловить слабые сигналы лагеря."
        "Выдвигаться дальше":
            window show
    "Ты встаёшь с бревна и идёшь дальше."
    scene bg ds_ext_abyss_night
    with dissolve
    "Ты выходишь к обрыву. Внизу озеро."
    if ds_semtype <= -3:
        th "А может, покончить уже с моим бессмысленным существованием?"
        window hide
        menu:
            "Сброситься с обрыва":
                window show
                "Ты подходишь к обрыву... {w}делаешь шаг... {w}и летишь..."
                th "Ну вот и всё..."
                scene black with dissolve2
                jump ds_end_suicide
            "Отбросить мысль":
                window show
                play sound ds_sfx_psy
                vol "Держись!"
                "Ты отступаешь от обрыва."
    play sound ds_sfx_int
    con "Вид на озеро прекрасен. Он вдохновляет тебя на свершения - правда, ты пока не знаешь, какие."
    play sound ds_sfx_mot
    per_eye "Вдали ты видишь огни. Похоже на некий населённый пункт."
    th "То есть, тут поблизости есть люди?"
    per_eye "Да."
    play sound ds_sfx_psy
    vol "Может, попробовать добраться туда?"
    th "Да, надо идти."
    show mt angry dress at center
    with dissolve
    mt "Семён! Ты куда ушёл?! Почему не был на дискотеке?!"
    me "Да я прогуляться решил..."
    mt "Всё, погулял?! А теперь идём домой, спать пора!"
    me "Как, дискотека уже кончилась?"
    mt "Да, ты всё пропустил! Идём!"
    "Ты решаешь не сопротивляться и идти."
    th "Всё равно ночью выдвигаться неразумно."

    scene bg ext_house_of_mt_night
    show mt normal dress at center
    with dissolve
    "Вы подходите к домику."
    window hide
    menu:
        "Пропустить Ольгу Дмитриевну":
            window show
            me "Проходите."
            "И с этими словами ты открываешь дверь."
            show mt smile dress at center
            with dspr
            mt "Ой, спасибо."
            hide mt with dissolve
            "И она проходит в домик. Ты за ней."
            $ ds_lp['mt'] += 1
        "Пройти вперёд самому":
            window show
            "Ты открываешь дверь и заходишь."
    scene bg int_house_of_mt_night
    show mt normal dress at center
    with dissolve
    mt "Всё, ложись спать. Спокойной ночи."
    hide mt with dissolve
    "Ты снимаешь с себя одежду и укладываешься в кровать."
    play sound ds_sfx_psy
    ine "Тебе не дают покоя увиденные тобой огни."
    th "Что же там? Стоит ли туда идти?"
    "У тебя закрываются глаза, и ты засыпаешь."
    jump ds_day3_dream

label ds_day3_dream:
    scene black with dissolve
    play music ds_dream fadein 3
    arb "Ну что, как у тебя дела?"
    window hide
    menu:
        "Всё отлично":
            window show
            me "Да всё замечательно!"
            arb "Думаешь?"
            lim "Или же ты пытаешься просто себя убедить в этом?"
        "Дела не очень":
            window show
            me "Как-то не очень... Я так и не понял, как мне выбраться отсюда."
            arb "А нужно ли тебе отсюда выбираться?"
            lim "Ага, не лучше ли продолжать пребывать тут... Кажется, тут у тебя больше шансов чего-то достичь."
    lim "Кстати, а ты помнишь тот мир, откуда ты прибыл сюда?"
    me "Помню... {w}кажется... {w}подождите!"
    me "А собственно что со мной было до лагеря? Я помню лишь поездку на автобусе!"
    arb "Может, лучше и не вспоминать?"
    lim "Похоже, ты уже не можешь остановить этот процесс... На тебя нахлынули новые расплывчатые воспоминания."
    lim "Они становятся всё более явными по мере обдумывания тобой этого. Останови ход мыслей!"
    play sound ds_sfx_psy
    vol "Нет. Ты не в силах. Единожды начав думать, ты не можешь просто взять и выбросить мысль из головы."

    play music ds_dream2 fadein 3
    scene bg ds_spb_dream1 at ds_thunder
    show fx ds_rain:
        alpha 0.2
        xysize (1920, 1080)
    with dissolve2
    play ambience ds_ambience_spb_weather
    "Перед тобой проявляется образ некоего города. Здесь идёт дождь, периодически слышны раскаты грома, а глаза ослепляют молнии."
    th "Кажется, это мой родной город..."
    arb "Да. Именно. Ты вспомнил свою малую родину."
    play sound ds_sfx_int
    enc "Санкт-Петербург. Ты родился в Санкт-Петербурге."
    me "И зачем я попал сюда?"
    lim "Узнаешь... Всему своё время..."
    vol "Вперёд. Тебе нужно идти вперёд."
    scene bg ds_spb_dream2 at ds_thunder
    show fx ds_rain:
        alpha 0.2
        xysize (1920, 1080)
    with dissolve
    "Образ становится яснее. Ты обнаруживаешь себя на мосту."
    play sound ds_sfx_mot
    per_eye "На фонарном столбе развевается нечто похожее на... пионерский галстук?"
    play sound ds_sfx_int
    lgc "Уж не знак ли это?"
    me "Знак чего?"
    lgc "Тебе нужно туда."
    arb "Остановись и подумай. Ты действительно хочешь узнать, что там?"
    lim "Ты уже не сможешь выбросить из головы то, что узнаешь. Один раз получилось..."
    lim "Но во второй раз ничего не выйдет!"
    me "Подождите. Я что... стёр себе память."
    arb "Немного не так. Ты пытался нечто очень болезненное забыть. И забыл... вместе со всем остальным."
    enc "Хоть имя своё не забыл, и как разговаривать - и то неплохо."
    lim "Но воспоминания вернулись... Тебе, похоже, не уйти от них."
    me "Какие воспоминания?"
    lim "Вспомни свои прошлые сны. Они именно об этом. А теперь иди вперёд."
    arb "Да. Тебе придётся пойти вперёд. Выход - только там."
    scene bg ds_spb_dream3 at ds_thunder
    show fx ds_rain:
        alpha 0.2
        xysize (1920, 1080)
    with dissolve
    vol "Ты идёшь по улице. Какая-то неведомая сила тянет тебя именно туда."
    play sound ds_sfx_fys
    shi "Это ощущение... дома?"
    me "Дома?! Я иду домой?"
    lim "Продолжай идти. Ответы тебя ждут..."
    "Ты продвигаешься дальше по улице. Кажется, она бесконечна."
    me "Куда я иду?"
    arb "Куда надо..."
    me "А куда надо?"
    lim "Не торопи события, Семён."
    me "Я хочу понять, что происходит! Почему я попал в лагерь? Почему я всё забыл?"
    me "Я позабыл дом, позабыл родителей! Я не могу понять, что за воспоминания у меня всплывают!"
    show ag normal far at center
    with dissolve
    "Словно отвечая тебе, перед тобой появляется некий мужчина."
    play sound ds_sfx_psy
    ine "Кажется, ты его знаешь. Более того - ты чувствуешь в нём что-то родное. {w}Родное и одновременно отчуждённое."
    show ag happy at center
    with dspr
    ag "Привет, Семён. Не ожидал тебя увидеть."
    me "Кто ты?"
    show ag grin at center
    with dspr
    ag "Ты должен знать, кто я... должен..."
    me "Разве? Я не понимаю!"
    arb "Всё ты понимаешь. Просто боишься это признать."
    me "Что я боюсь признать?"
    lim "Это порождение твоей глубинной травмы. Одной из травм."
    lim "Ты хотел бы избавиться от этого груза... но не можешь. Как ни пытаешься."
    me "Так ты..."
    ag "Да, Семён. Я - твой отец."
    me "Отец?! Нет! Нет! Нет-нет-нет!"
    ag "Да, да, да..."
    lim "Как тебе и предрекали - это оказывается для тебя потрясением."
    show ag rage at center
    with dspr
    ag "А ну прекрати ныть!"
    "Ты успокаиваешься."
    me "Но... почему?"
    show ag normal at center
    with dspr
    ag "Почему что?"
    me "Почему... ты тут?"
    ag "Я ухожу."
    me "К-куда?"
    ag "Не «куда», а «откуда». От тебя, Семён."
    me "Зачем? Зачем ты от меня уходишь?"
    show ag angry at center
    with dspr
    ag "Потому что ты подвёл нас. Меня и мать - своих родителей."
    me "Я не понимаю... Как я вас подвёл?"
    ag "Привёл в свою жизнь ту! И разрушил всё, что мы в тебя вкладывали!"
    me "Кого? Причём тут она?"
    show ag rage at center
    with dspr
    ag "{i}Её{/i}. Пока в твоей жизни не появилась она - ты был настоящим идеалом!"
    ag "А потом... Потом эта твоя любовь поглотила всё! Ты пал, низко пал!"
    me "Но..."
    ag "Что «но»?! Мы сколько раз говорили тебе, что ни к чему хорошему это не приведёт! А ты не слушал! Ты наплевал на нас!"
    ag "Мы в тебя столько вложили, а ты..."
    show ag tired at center
    with dspr
    ag "Уже неважно. Живи свою жизнь дальше сам."
    me "Не уходите... Не оставляйте меня одного!"
    ag "Ты сделал свой выбор. Теперь вкушай последствия."
    me "А... а где мама?.."
    ag "Она уже ушла. Она изначально говорила, что ты безнадёжен, а я верил... и ошибся..."
    me "Почему... я безнадёжен?"
    ag "Ты разрушил своё светлое будущее. Разрушил ради {i}неё{/i} - а {i}она{/i} тебя просто использовала."
    me "Я смогу! Я исправлю всё!"
    ag "Ты уже ничего не исправишь. Как и мы. Остаётся только признать - всё, что мы в тебя вложили, было впустую."
    me "Не бросай меня! У меня больше никого нет!"
    ag "Ты {i}уже{/i} один."
    show ag ok at center
    with dspr
    ag "Ты же во сне! Всё уже случилось! И изменить ты никак не можешь. Ни-че-го!"
    show ag tired at center
    with dspr
    ag "Раньше надо было думать. А теперь ты всё. Сам себя утопил."
    ag "Прощай, Семён."
    me "Я прошу... помоги мне!"
    show ag grin far at center
    with dspr
    ag "Cам, Семён, сам..."
    hide ag with dissolve
    "И он уходит. Ты же остаётся сидеть в луже."
    me "Что происходит? Почему это происходит со мной?!"
    lim "Тебя переполняет чувство вины. Ты не можешь остановиться в обвинениях даже во сне."
    arb "Поэтому ты и видишь, и чувствуешь всё это."
    me "Так... мне надо прекратить винить себя?"
    lim "Легко сказать. А вот сможешь ли ты это сделать?"
    play sound ds_sfx_psy
    vol "Должен справиться! Тебе дали шанс на новую жизнь. И тут тебе рады и хотят тебе помочь. Тебе остаётся лишь принять помощь."
    show sl smile pioneer:
        alpha 0.5
    with dissolve
    me "Например, Славя. Несмотря ни на что, она пытается меня поддержать!"
    hide sl
    show un sad pioneer:
        alpha 0.5
    with dissolve
    me "Или Лена. Такая вечно грустная и потому милая..."
    hide un
    show mi smile pioneer:
        alpha 0.5
    with dissolve
    me "Или вот Мику. Всегда рада поговорить даже со мной."
    hide mi
    show us laugh sport:
        alpha 0.5
    with dissolve
    me "А ещё Ульянка... Хоть и проказница, но добродушная, и хочет придать веселья мне."
    hide us
    show mz angry glasses pioneer:
        alpha 0.5
    with dissolve
    me "Ещё есть Женя... которая, видимо, тоже пережила нечто ужасное... и при этом держится."
    hide mz
    show mt normal pioneer:
        alpha 0.5
    with dissolve
    me "А Ольга Дмитриевна... Она кажется строгой, но, возможно, она по-настоящему хочет обо мне позабоиться."
    hide mt
    show cs normal medic1:
        alpha 0.5
    with dissolve
    me "Как и Виола."
    hide cs
    show el normal pioneer:
        alpha 0.5
    with dissolve
    me "А Электроник? Несмотря на мои насмешки он стремится привлечь меня к делу..."
    if ds_met['ya'] > 0:
        hide el
        show ya normal pioneer:
            alpha 0.5
        with dissolve
        me "Яна... Что-то в ней есть... С ней всегда становится спокойнее, хоть она и сама крайне замкнута..." 
        hide ya with dissolve
    else:
        hide el with dissolve
    play sound ds_sfx_psy
    ine "Всё ты верно говоришь... Вот только кое-кого ты забыл."
    me "Кого?!"
    show dv grin pioneer:
        alpha 0.5
    with dissolve
    me "Да... есть ещё Алиса... Но она же воплощение агрессии!"
    ine "Ты уверен?"
    me "Ну... наверное."
    show dv angry pioneer at center
    with dissolve
    me "Вечно на кого-то злится и не идёт на контакт! Ну, может быть, иногда разве что..."
    ine "А тебе это {i}никого{/i} не напоминает?"
    me "Кого?"
    ine "Ну... есть один человек, который тоже оказался покинут всеми и из-за этого отгородился от мира."
    vol "Да. Как и Алиса."
    dv "Послушай хоть раз своих друзей, придурок! Один раз уже всё упустил - не упусти во второй!"
    hide dv with dissolve
    me "Каких друзей?"
    arb "Своё сознание. Своё подсознание. Всех нас."
    me "Я не понимаю..."
    vol "Рука помощи. Вернее, десять рук помощи. Тебе нужно выбрать одну."
    lim "И выбор не так прост, как кажется... Подумай хорошенько, Семён..."
    lim "Ты хочешь найти ответы - а ответы лежат именно в людях. В тех, кто окружает тебя. В тех, кто тебе дорог."
    lim "Кто тебе дорог, Семён? С кем ты пойдёшь дальше?"
    arb "Или, может, всё ложь - и тебя все только отвлекают? Ты ведь так ничего и не понял, не выяснил... Останешься сидеть тут, один?"
    lim "Или же выберешься из своего кокона?"
    me "Я... я не знаю..."
    vol "Выбирай, Семён! Ты должен решить для себя сам! Мы можем лишь подсказать тебе - но выбираешь ты."
    play sound sfx_hell_alarm_clock
    arb "C добрым утром, Семён! Пора вставать!"
    scene black with dissolve2
    jump ds_day4_morning
