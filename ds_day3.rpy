# DISCO SOVENOK
# ОБЩИЙ РУТ. ДЕНЬ 3

init:
    $ mods["disco_sovenok"] = u'Disco Sovenok'
    $ ds_was_on_lineup = False
    $ ds_accept_mz = False
    $ ds_understood_mz_reason = False
    $ ds_promise_un = False
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

label ds_day3_morning:
    $ ds_restore_health()
    $ ds_restore_morale()

    $ backdrop = "days"
    $ new_chapter(3, u"Disco Sovenok. День 3")
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
            res "Вообще-то, ты самолично вчера предложил по утрам заниматься!"
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
            "Притвориться, что не можешь":
                if skillcheck('drama', lvl_challenging):
                    window show
                    dra "У вас болит... скажем, живот, мессир."
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
                    dra "Вы и пытаетесь изобразить, что у вас что-то болит, мессир, но ничего внятного не получается."
                    me "Ах... у меня всё болит..."
                    show sl angry sport at center with dspr
                    sl "Врать нехорошо, Семён! Сказал бы, что просто не хочешь!"
                    sl "А так делать нехорошо... да и вообще, зачем тогда сам предлагал?!"
                    sl "Ладно, я пойду! Удачного дня!"
                    $ ds_lp_sl -= 2
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
                    "Отцепить ключ":
                        if skillcheck('interfacing', lvl_easy):
                            window show
                            inf "Это легче лёгкого, благо тебе и скрываться не надо!"
                            $ ds_some_key = True
                            "Ты кладёшь в карман отцепленный ключ."
                        else:
                            window show
                            inf "Ты пытаешься отсоединить ключ от кольца, но ничего не выходит!"
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
                    "Отцепить ключ себе":
                        if skillcheck('interfacing', lvl_godly):
                            window show
                            inf "Ты ловко двигаешь пальцами у себя в кармане... "
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
                            inf "Но ключи слишком громко шумят, и Славя обращает внимание."
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
        "Продолжить бежать":
            if skillcheck('endurance', lvl_challenging):
                window show
                edr "У тебя открывается второе дыхание! Беги дальше!"
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
                edr "Ты пытаешься побежать... но от усталости падаешь."
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
        ins "Тебе очень хочется посмотреть на её девичью красу..."
        play sound ds_sfx_psy
        vol "Но стоит ли? Только испортишь отношения с ней."
        window hide
        menu:
            "Подглянуть":
                if skillcheck('savoir_faire', lvl_legendary):
                    window show
                    svf "Тебе удаётся воспользоваться тем, что дверцы закрываются неплотно."
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
                    svf "Ты начинаешь смотреть сверху дверцы, и Славя предсказуемо тебя замечает."
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
    play sound ds_sfx_psy
    sug "Похвали волосы! Ей будет приятно, и это улучшит её отношение к тебе."
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
        "Просто поздороваться":
            window show
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
        "Попытаться избежать":
            if skillcheck('drama', lvl_heroic):
                window show
                play sound ds_sfx_int
                dra "Изобразите, что у вас болит живот."
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
                dra "У вас не хватает фантазии придумать и изобразить, что вы {i}не можете{/i} пойти на линейку."
                me "Ну Ольга Дмитриевна, давайте я сегодня..."
                show mt angry pioneer at center with dspr
                mt "Нет, Семён, посещение линейки обязательно!"
                $ ds_karma -= 5
                me "Ладно..."
                show mt normal pioneer at center with dspr
                mt "Так, идём!"
                jump ds_day3_lineup
        "Протестовать":
            if skillcheck('authority', lvl_godly):
                window show
                play sound ds_sfx_psy
                aut "Ты свободная личность! И никуда ты не пойдёшь!"
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
                aut "У тебя не хватит решимости пойти против вожатой."
                $ ds_skill_points['authority'] += 1
                me "Ну Ольга Дмитриевна, давайте я сегодня..."
                show mt angry pioneer at center with dspr
                mt "Нет, Семён, посещение линейки обязательно!"
                $ ds_karma -= 5
                me "Ладно..."
                show mt normal pioneer at center with dspr
                mt "Так, идём!"
                jump ds_day3_lineup
        "Улизнуть":
            if skillcheck('savoir_faire', lvl_heroic):
                window show
                play sound ds_sfx_mot
                svf "Ты резко срываешься с места и бросаешься в дверь."
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
                svf "Ты пытаешься сбежать, бросаешься в дверь..."
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
        emp "Разве что Алиса, похоже, не очень-то горит желанием танцевать."
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
        per_hea "Ты можешь услышать, как вожатая говорит шёпотом: «прости господи»."
        $ ds_skill_points['perception'] += 1
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
        "Позавтракать с Леной":
            if skillcheck('volition', lvl_easy):
                window show
                play sound ds_sfx_psy
                vol "Ты решительно направляешься в её сторону."
                $ ds_skill_points['volition'] += 1
                play sound ds_sfx_mot
                svf "Но тут тебя хватают за руку!"
                show mz normal glasses pioneer at center   with dissolve
                "Женя, вчерашняя библиотекарша."
                mz "Бери завтрак и садись, есть разговор."
                if not skillcheck('composure', lvl_medium, passive=True):
                    play sound ds_sfx_mot
                    com "Ты несколько растерялся и молчишь."
                    show mz bukal glasses pioneer at center   with dspr
                    mz "Чего стоишь?"
                else:
                    $ ds_skill_points['composure'] += 1
                me "Извини, но не слишком ли это… резко?"
                show mz normal glasses pioneer at center   with dspr
                mz "А что такого-то? Бери завтрак и садись."
                play sound ds_sfx_psy
                aut "Похоже, для неё такое поведение совершенно нормально."
                window hide
                menu:
                    "Пойти к Лене":
                        if skillcheck('volition', lvl_medium):
                            window show
                            play sound ds_sfx_psy
                            vol "Ты уверен, что Лена будет не против твоей компании."
                            vol "А Женя... вряд ли у неё что-то срочное."
                            $ ds_lp['un'] += 1
                            $ ds_skill_points['volition'] += 1
                            jump ds_day3_breakfast_un
                        else:
                            window show
                            play sound ds_sfx_psy
                            vol "Нет, у тебя не хватает воли уйти от Жени к Лене."
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
        com "Ты несколько растерялся и молчишь."
        show mz bukal glasses pioneer at center   with dspr
        mz "Чего расселся?"
    else:
        $ ds_skill_points['composure'] += 1
    window hide
    menu:
        "Сделать замечание":
            me "Извини, но не слишком ли это… резко?"
            show mz normal glasses pioneer at center   with dspr
            mz "А что такого-то?"
            play sound ds_sfx_psy
            aut "Похоже, для неё такое поведение совершенно нормально."
        "Сделать комплимент":
            if skillcheck('suggestion', lvl_challenging):
                window show
                sug "Скажи ей про её волосы. Или про лицо."
                me "А у тебя прекрасные волосы. Такие густые, и цвет красивый!"
                $ ds_lp['mz'] += 1
                show mz shy glasses pioneer at center with dspr
                mz "Это хорошо, что ты так считаешь... но разговор не ждёт!"
            else:
                window show
                sug "Тебе не приходит в голову хороших комплиментов."
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
            rhe "Спроси её про год! Про что-нибудь!"
            window hide
            menu:
                "Cпросить":
                    window show
                    me "Слушай, а какой сейчас год, что-то совсем со счёта сбился?"
                    show zh sceptic glasses pioneer at center  with dspr
                    mz "Как будто ты не знаешь, какой сейчас год. Что ты мне глупые вопросы задаёшь."
                    me "Я бы не спрашивал, если бы знал."
                    show zh bukal glasses pioneer at center with dspr
                    mz "А ты не знаешь?"
                    me "Нет. У меня память плохая. Так какой сейчас год?"
                    "Ты мило улыбаешься."
                    show zh normal glasses pioneer at center  with dspr
                    mz "Не понимаю, куда ты клонишь."
                    mz "Можешь просто прибавить количество прожитых лет к году рождения. Если у тебя в этом году дня рождения ещё не было, то отними один."
                    th "Разве тебе не было бы проще ответить, какой год, чем всю эту тираду проговаривать?"
                    "Но ответила она правильно, так что перефразировать вопрос я не мог. Ладно, придумаем что-нибудь другое."
                    me "А ты случайно не знаешь, что у нас тут за речка протекает? Или это и не речка вовсе?"
                    "Градус недоумения накалялся."
                    $ renpy.pause(1)
                    show zh fun glasses pioneer at center with dspr
                    mz "Ты разговор так что ли хочешь поддержать?"
                    show zh bukal glasses pioneer at center  with dspr
                    mz "Обычно в такой ситуации задают другие вопросы. \"Как дела\", там, \"как настроение\",..."
                    "Бесполезно."
                    me "Ладно, тогда как у тебя дела?"
                    show zh sceptic glasses pioneer at center  with dspr
                    $ renpy.pause(2)
                    hide zh with dissolve
                    "Женя лишь покачала головой, допила компот и ушла."
                "Не спрашивать":
                    window show
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
        "Восстановить просьбу Жени":
            if skillcheck('logic', lvl_medium, modifiers=[('ds_was_on_lineup', 2)]):
                window show
                play sound ds_sfx_int
                lgc "Она, скорее всего, хочет, чтобы ты ей помог. В библиотеке. В рамках общественно-полезного труда, упомянутого вожатой утром."
                me "Да, я понял: нужно помочь тебе в библиотеке."
                show mz normal glasses pioneer at center with dspr
                mz "Отлично, тогда до встречи!"
                hide mz with dissolve
                me "Ладно..."
                hide mz with dissolve
                "Женя встаёт и направляется к выходу."
                if skillcheck('reaction_speed', lvl_trivial, passive=True):
                    play sound ds_sfx_mot
                    res "Она же не доела!"
                    $ ds_skill_points['reaction_speed'] += 1
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
                lgc "Однако, у тебя не получается ничего подходящего придумать."
                $ ds_skill_points['logic'] += 1
                play sound ds_sfx_int
                dra "Более того, ваше выражение лица выдаёт, что вы не понимаете происходящего."
                show mz angry glasses pioneer at center with dspr
                mz "Ты не слушаешь!"
        "Притвориться, что понял":
            if skillcheck('drama', lvl_up_medium):
                window show
                play sound ds_sfx_int
                dra "Вы, мессир, прекрасно всё поняли и уж точно ничего не забыли!"
                $ ds_skill_points['drama'] += 1
                me "Хорошо, я тебя понял."
                $ ds_accept_mz = True
                show mz normal glasses pioneer at center with dspr
                mz "Отлично, тогда до встречи!"
                hide mz with dissolve
                "Женя встаёт и направляется к выходу."
                if skillcheck('reaction_speed', lvl_trivial, passive=True):
                    play sound ds_sfx_mot
                    res "Она же не доела!"
                    $ ds_skill_points['reaction_speed'] += 1
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
                dra "На вашем лице, мессир, всё написано, как в книге."
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
        enc "Вообще, «хунта» - это группировка, обычно военная, захватившая власть насильственно."
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
                rhe "Согласись с ней, а затем спроси"
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
        res "Она же не доела!"
        $ ds_skill_points['reaction_speed'] += 1
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
        "Заговорить с Леной":
            if skillcheck('rhetoric', lvl_easy, modifiers=[('ds_was_on_lineup', 1)]):
                window show
                rhe "Танцы! Сегодня танцы! Поговори о них."
                $ ds_skill_points['rhetoric'] += 1
            else:
                window show
                rhe "Тебе не приходит в голову никаких тем для разговора."
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
        sug "Ты склонишь её к себе (ещё больше), если скажешь, что пойдёшь только с ней."
    window hide
    menu:
        "Иду на танцы":
            window show
            me "Конечно же иду!"
            show un smile pioneer at center with dspr
            un "Хорошо."
            window hide
            menu:
                "Пригласить Лену":
                    if skillcheck('suggestion', lvl_challenging):
                        window show
                        play sound ds_sfx_psy
                        sug "Скажи, что она выглядит прекрасно, и что ты хочешь видеть её на танцах."
                        me "Ты так прекрасно выглядишь, кстати... тебе обязательно нужно прийти на танцы!"
                        show un shy pioneer at center with dspr
                        un "Хорошо... спасибо..."
                        $ ds_lp['un'] += 1
                        $ ds_skill_points['suggestion'] += 1
                    else:
                        window show
                        play sound ds_sfx_psy
                        sug "Вперёд, приглашай!"
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
        "Пойду только с тобой" if ds_last_skillcheck:
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
        scene bg ext_dining_hall_day
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
        "Сослаться на помощь Ольге Дмитриевне":
            if skillcheck('drama', lvl_challenging):
                play sound ds_sfx_int
                dra "Ты выполняешь очень ответственное поручение для Ольги Дмитриевны! Помогаешь ей разобрать документы пионеров, скажем."
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
                dra "Врать тут вряд ли стоит."
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
    if skillcheck('logic', lvl_up_medium, passive=True, modifiers=[('ds_was_on_lineup', 1)]):
        play sound ds_sfx_int
        lgc "Так ведь Алиса вроде как играет на гитаре... скорее всего, это она."
        $ ds_skill_points['logic'] += 1
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
        "Запрыгнуть":
            if skillcheck('savoir_faire', lvl_formidable):
                window show
                play sound ds_sfx_mot
                svf "Ты с лёгкостью прыгаешь и цепляешься за тот же вагон, что и Ульяна."
                svf "После этого вы забираетесь внутрь."
                $ ds_skill_points['savoir_faire'] += 1
                $ ds_lp['us'] += 1
                jump ds_day3_us_escaped
            else:
                window show
                play sound ds_sfx_mot
                svf "Ты пытаешься зацепиться за вагон... но срываешься и падаешь!"
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
        "Снять Ульяну":
            if skillcheck('reaction_speed', lvl_legendary):
                window show
                play sound ds_sfx_mot
                res "Ты успеваешь метнуться к вагону как раз вовремя и сорвать с него Ульяну."
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
                svf "Ты пытаешься схватить Ульяну... но поезд оказывается быстрее, и он увозит её."

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

label ds_day3_stage_dv:
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
        enc "Она играет «Взвейтесь кострами». Гимн пионеров."
        $ ds_skill_points['encyclopedia'] += 1
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
    con "Она словно пытается слиться с музыкой, стать каждой нотой, каждым квадратом, каждой триолью."
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
        aut "Она пытается тебя зацепить! Не позволяй ей этого!"
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
            emp "Похоже, у неё {i}свои{/i} планы на тебя."
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
                    "Пригласить на танцы":
                        if skillcheck('suggestion', lvl_godly):
                            window show
                            play sound ds_sfx_psy
                            sug "Есть идея лучше. Ты хотел бы видеть её на танцах. Не в качестве танцорши - в качестве музыкального сопровождения."
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
                            sug "Давай. Пригласи её на танцы. Любой девушке понравится, когда парень приглашает её на танцы."
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
            "Пригласить на танцы":
                if skillcheck('suggestion', lvl_godly):
                    window show
                    play sound ds_sfx_psy
                    sug "Есть идея лучше. Ты хотел бы видеть её на танцах. Не в качестве танцорши - в качестве музыкального сопровождения."
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
                    sug "Давай. Пригласи её на танцы. Любой девушке понравится, когда парень приглашает её на танцы."
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
            scene bg ds_int_clubs_pantry
            with dissolve
            "Ты заходишь в кладовку."
            th "Так, где тут у них инструменты?.."
            if skillcheck('shivers', lvl_easy, passive=True):
                play sound ds_sfx_fys
                shi "Не спрятано ли тут ничего? Такое ощущение, что да, скрыто..."
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
                                scene bg ds_int_clubs_pantry
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
                "Придумать историю":
                    if skillcheck('conceptualization', lvl_trivial):
                        window show
                        play sound ds_sfx_int
                        con "Взял книжку в библиотеке и прочитал. Прям такая есть - «Машина времени», Герберт Уэллс."
                        me "Я вчера книжку взял в библиотеке – «Машина времени» Уэллса. Читали, наверное? Вот, собственно, и заинтересовался."
                    else:
                        window show
                        play sound ds_sfx_int
                        con "Сложно придумать правдоподобный повод..."
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

label ds_day3_help_sport:
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
        "Cогласиться":
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
                    jump ds_day3_help_sugar
        "Отказаться":
            window show
            me "Нет уж, спасибо!"
            "И ты уходишь."
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
        svf "Ты первым же касанием аккуратным ударом кладёшь мяч в девятку ворот соперника."
        svf "На самом деле, это не составляет особого труда – поле в длину от силы метров пятьдесят, а вратарь чужой команды даже не достаёт до перекладины."
    else:
        play sound ds_sfx_mot
        svf "Ты замахиваешься, но умудряешься промахнуться по мячу."
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
        "Организовать игру команды":
            if skillcheck('esprit', lvl_medium):
                window show
                play sound ds_sfx_psy
                esp "Так, давай. Собери свою команду воедино. И у вас всё получится."
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
                esp "Ты пытаешься привести к порядку свою команду по ходу игры, но безуспешно."
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
                "Настоять":
                    if skillcheck('authority', lvl_easy):
                        play sound ds_sfx_psy
                        aut "Ты всем своим видом показываешь, что лучше с тобой не спорить."
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
                        aut "Ты пытаешься настоять на своём."
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
    show us sad pioneer at center   with dspr
    us "Так нечестно!"
    me "Что нечестно?"
    show us angry pioneer at center   with dspr
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
    show us dontlike pioneer at center   with dspr
    us "Нет уж!"
    us "Но ты мне точно не забьёшь!"
    me "Посмотрим…"
    hide us  with dissolve

    if skillcheck('coordination', lvl_easy, passive=True):

        play sound sfx_soccer_ball_kick
        play sound2 ds_sfx_mot
        cor "Аккуратным ударом ты кладёшь мяч в правую от неё шестерку."
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

        cor "Впрочем, ты, как и она ранее, тоже бьёшь не туда."
        show us laugh sport at center with dissolve
        us "Ладно, соглашусь на ничью, так уж и быть!"
        me "Но..."
    with fade

    stop music fadeout 3

    play sound sfx_dinner_horn_processed

    window show
    "И тут заиграла музыка, призывающая пионеров на обед."
    show us laugh2 pioneer at center   with dissolve
    us "Ладно, ещё отыграюсь!"
    hide us  with dissolve

    stop music fadeout 3

    "Она смеётся, машет тебе рукой и бежит в сторону столовой."
    "Ты направляешься за ней."
    window hide

    jump ds_day3_lunch

label ds_day3_help_un:
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
    scene bg ds_ext_admin_night
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
        "Рассказать самому":
            if skillcheck('rhetoric', lvl_easy):
                window show
                play sound ds_sfx_int
                rhe "Говори. Акцентируй внимание на необходимости поддерживать юные дарования."
                me "Ольга Дмитриевна! Тут Лена, оказывается, очень хорошо рисует."
                me "И мы считаем, что нужно её поддержать в этом!"
                me "Для чего предлагаем использовать пустующее здание напротив клуба кибернетиков."
            else:
                window show
                play sound ds_sfx_int
                rhe "Тебе трудно подобрать слова, чтобы начать... Извечная проблема..."
                me "Понимаете... тут Лена хочет открыть место для рисования..."
                me "В неиспользуемом домике напротив клуба кибернетиков..."
            $ ds_lp['un'] += 1
            $ ds_skill_points['rhetoric'] += 1
        "Заставить Лену рассказать":
            if skillcheck('suggestion', lvl_challenging):
                window show
                play sound ds_sfx_psy
                sug "Подбодри Лену. Всё хорошо. Возьми её за руку."
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
                sug "Пусть она говорит, вот и всё!"
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
    $ persistent.sprite_time = 'day'
    scene bg ds_ext_storage_day
    with dissolve

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
        "Сбежать":
            if skillcheck('savoir_faire', lvl_challenging):
                window show
                play sound ds_sfx_mot
                svf "Беги!"
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
                svf "Ты пытаешься сбежать, но он своим громадным телом перекрывает тебе путь."
                $ ds_skill_points['savoir_faire'] += 1
                fzp "И куда это ты собрался?!"
                $ ds_karma -= 10
        "Предъявить претензии":
            if skillcheck('authority', lvl_challenging):
                window show
                play sound ds_sfx_psy
                aut "Он же физрук? А почему это он свои обязанности не исполняет? Зарядку там не проводит..."
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
                aut "Вообще, ты свободная личность."
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
        "Потаскать мешки":
            window show
            th "Ладно, потаскаем мешки..."
    window hide
    if skillcheck('physical_instrument', lvl_legendary):
        window show
        play sound ds_sfx_fys
        phi "Не без труда, но ты поднимаешь мешок и грузишь его себе на спину."
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
        phi "Ты изо всех сил пытаешься поднять мешок."
        me "Рааааз!"
        phi "Но как бы ты ни надрывался, мешок даже не думает оторваться от земли."
        $ ds_skill_points['physical_instrument'] += 1
        if not skillcheck('pain_threshold', lvl_heroic, passive=True):
            play sound ds_sfx_fys
            pat "Максимум, чего ты добился - это того, что у тебя заболела спина."
            $ ds_damage_health()
        else:
            $ ds_skill_points['pain_threshold'] += 1
        play sound ds_sfx_psy
        vol "Оставь эту гиблую затею. Пусть силач-физрук сам таскает мешки. Ты не потянешь."
        play sound sfx_dinner_horn_processed
        "Благо у тебя появляется легитимный повод уйти - обед."
        "Ты направляешься в столовую."
        $ ds_karma -= 5
    jump ds_day3_lunch

label ds_day3_help_mt:
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
        "Начать протестовать":
            if skillcheck('authority', lvl_medium):
                window show
                play sound ds_sfx_psy
                aut "Чего это она вздумала тебя впрягать и в таскание коробок? Ты на это не подписывался!"
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
                aut "Не высовывайся. Она тут главная. И ты сам согласился."
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
        enc "Местные компьютеры напоминают тебе первые «Макинтоши». Такие же слитные системный блок и монитор, причём монитор сверху. Естественно, плоских экранов здесь не наблюдается."
        $ ds_skill_points['encyclopedia'] += 1
    me "Приступим..."
    "Ты открываешь первую папку, и одновременно с этим файл «Список пионеров.БД»"
    play sound ds_sfx_mot
    per_eye "Ф.И.: ДВАЧЕВСКАЯ АЛИСА{n}Д.Р.: 03/IV/1972{n}Н.П.: пгт. Работино{n}ОТР.: I"
    play sound ds_sfx_int
    lgc "Ф.И. - фамилия, имя. Д.Р. - дата рождения. Н.П. - населённый пункт. ОТР. - отряд."
    "Ты вносишь данные в нужные столбики таблицы."
    per_eye "Ф.И.: УНЫЛОВА ЕЛЕНА{n}Д.Р.: 25/IX/1972{n}Н.П.: пгт. Работино{n}ОТР.: I"
    per_eye "Ф.И.: ФЕОКТИСТОВА СЛАВЯНА{n}Д.Р.: 12/V/1972{n}Н.П.: дер. Мятусово{n}ОТР.: I"
    per_eye "Ф.И.: СОВЕТОВА УЛЬЯНА{n}Д.Р.: 08/XII/1975{n}Н.П.: г. Ленинград{n}ОТР.: I"
    per_eye "Ф.И.: ХАЦУНЕ МИКУ{n}Д.Р.: 31/VIII/1972{n}Н.П.: г. Токио (Япония){n}ОТР.: I"
    per_eye "Ф.И.: СЫРОЕЖКИН СЕРГЕЙ{n}Д.Р.: 23/III/1972{n}Н.П.: г. Москва{n}ОТР.: I"
    per_eye "Ф.И.: МИЦГОЛ ЕВГЕНИЯ{n}Д.Р.: .../.../1972{n}Н.П.: г. Одесса{n}ОТР.: I"
    per_eye "Ф.И.: ДЕМЬЯНЕНКО АЛЕКСАНДР{n}Д.Р.: .../.../1972{n}Н.П.: г. Москва{n}ОТР.: I"
    per_eye "Ф.И.: ПЁРСУНОВ СЕМЁН{n}Д.Р.: .../.../1972{n}Н.П.: г. Ленинград{n}ОТР.: I"
    play sound ds_sfx_mot
    res "О, это ты!"
    "На этом папка заканичвается. Ты переходишь к следующей."
    per_eye "Ф.И.: УНЫЛОВА АЛЁНА{n}Д.Р.: 25/IX/1974{n}Н.П.: пгт. Работино{n}ОТР.: II"
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
    scene ds_ext_admin_day
    with dissolve
    "И вы идёте на обед."
    jump ds_day3_lunch

label ds_day3_help_sugar_mt:
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
        "Сбежать":
            if skillcheck('savoir_faire', lvl_challenging, modifiers=[('True', -2)]):
                window show
                play sound ds_sfx_mot
                svf "Беги!"
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
                svf "Ты пытаешься сбежать, но он своим громадным телом перекрывает тебе путь. И Ольга Дмитриевна мешает"
                $ ds_skill_points['savoir_faire'] += 1
                fzp "И куда это ты собрался?!"
                $ ds_karma -= 10
        "Предъявить претензии":
            if skillcheck('authority', lvl_challenging):
                window show
                play sound ds_sfx_psy
                aut "Он же физрук? А почему это он свои обязанности не исполняет? Зарядку там не проводит..."
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
                aut "Вообще, ты свободная личность."
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
        "Потаскать мешки":
            window show
            th "Ладно, потаскаем мешки..."
    window hide
    if skillcheck('physical_instrument', lvl_legendary):
        window show
        play sound ds_sfx_fys
        phi "Не без труда, но ты поднимаешь мешок и грузишь его себе на спину."
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
        phi "Ты изо всех сил пытаешься поднять мешок."
        me "Рааааз!"
        phi "Но как бы ты ни надрывался, мешок даже не думает оторваться от земли."
        $ ds_skill_points['physical_instrument'] += 1
        if not skillcheck('pain_threshold', lvl_heroic, passive=True):
            play sound ds_sfx_fys
            pat "Максимум, чего ты добился - это того, что у тебя заболела спина."
            $ ds_damage_health()
        else:
            $ ds_skill_points['pain_threshold'] += 1
        play sound ds_sfx_psy
        vol "Оставь эту гиблую затею. Пусть силач-физрук сам таскает мешки. Ты не потянешь."
        play sound sfx_dinner_horn_processed
        "Благо у тебя появляется легитимный повод уйти - обед."
        "Ты направляешься в столовую."
        $ ds_karma -= 5
    jump ds_day3_lunch

label ds_day3_help_mi:
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
        ins "Отличный шанс! Возьми эту тяночку! Если потребуется - силой!"
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
            "Изнасиловать Мику":
                if skillcheck('physical_instrument', lvl_easy):
                    window show
                    play sound ds_sfx_fys
                    phi "Жребий брошен. Ты поваливаешь её на пол, срываешь с неё одежду..."
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
                    phi "Ты пытаешься свалить Мику на пол..."
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
                emp "Ты её обидел. Она пытается не подать виду, но безуспешно."
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
    jump ds_day3_mz_dialogue

label ds_day3_mz_dialogue:
    $ ds_said_compl = False
    window hide
    menu:
        "Cказать комплимент" if not ds_said_compl:
            if skillcheck('rhetoric', lvl_medium):
                rhe "Волосы - беспроигрышный вариант. Тем более, тут они цветные!"
                me "Кстати, Жень, красивые волосы у тебя! Такие насыщенно-синие... обожаю синий цвет!"
                show mz bukal glasses pioneer far at right
                with dspr
                mz "Ты там книги протирай, а не сочиняй похвалы!"
                $ ds_lp['mz'] += 1
            else:
                rhe "У тебя не получается придумать ничего красивого."
                me "Хорошо выглядишь!"
                show mz bukal glasses pioneer far at right
                with dspr
                mz "Книгами занимайся!"
            me "Ладно-ладно..."
            $ ds_skill_points['rhetoric'] += 1
            $ ds_said_compl = True
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
                    play sound ds_sfx_enc
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
                        lgc "Как будто тема с изнасилованием для неё {i}личная{/i}."
                        th "То есть, либо её знакомую изнасиловали, либо..."
                        lgc "Да. Именно."
                        $ ds_skill_points['logic'] += 1
                        emp "Поэтому отставить! Сейчас тебе, мужику, в подобные вещи лучше не лезть."
                    show mz normal glasses pioneer far at right
                    with dspr
                    mz "Cлушай - тебе правда очень повезло не пережить то, что довелось пережить мне и многим женщинам. Радуйся этому!"
                    "Тут оказывается, что за разговором ты всё протёр."
                "Отступить":
                    window show
                    me "Ладно, извини... но если что - я всегда готов поговорить."
                    show mz bukal glasses pioneer far at right
                    with dspr
                    mz "Ага, всенепременно воспользуюсь."
                    "Ты продолжаешь протирать книги, пока они не заканчиваются."
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
                dra "Cкажи ей про то, что Электроник влюблён в неё. И боится идти на контакт. Кажется, у неё есть чувства к нему."
                play sound ds_sfx_psy
                emp "А если нет? Тогда ты жестоко обманешь её!"
            window hide
            menu:
                "Соврать во благо" if ds_last_skillcheck:
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
                    th "Ладно, и я пойду..."
                    play sound sfx_dinner_horn_processed
                    "Как раз и призыв на обед звучит."
                    jump ds_day3_lunch
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
                    "За разговором оказывается, что ты протёр все книги."
                "Отступить":
                    window show
                    me "Ладно, извини... но если что - я всегда готов поговорить."
                    show mz bukal glasses pioneer far at right
                    with dspr
                    mz "Ага, всенепременно воспользуюсь."
                    "Ты продолжаешь протирать книги, пока они не заканчиваются."
        "Молча протирать книги":
            window show
            th "Ещё не хватало... она только злиться и умеет, наверное!"
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
        "Потребовать успокоиться":
            if skillcheck('authority', lvl_trivial):
                window show
                play sound ds_sfx_psy
                aut "Ты набираешь воздуха в грудь и громко, чётко произносить."
                me "ТИШИНА!"
                "Все оборачиваются на тебя."
                $ ds_lp['ya'] += 1
                $ ds_skill_points['authority'] += 1
                ya "Cпасибо..."
            else:
                window show
                play sound ds_sfx_psy
                aut "Тебе даже на детей не хватает смелости прикрикнуть..."
                me "Успокойтесь, пожалуйста..."
                "Но шум и гам продолжаются."
                $ ds_skill_points['authority'] += 1
                hide ya with dissolve
                "Яне приходится заходить в воду и разделять их - что для неё оказывается непросто."
                "Но через некоторое время она наконец выходит из воды."
                show ya normal pioneer at center with dissolve
                ya "Cпасибо..."
        "Разнять детей":
                play sound ds_sfx_mot
                svf "Сделаем по-другому. Забегай в воду и растащи их."
                "Ты вбегаешь в воду (благо дети не заходят далеко) и пытаешься их разнять."
                if skillcheck('savoir_faire', lvl_medium):
                    svf "Это не вызывает у тебя затруднений - это же маленькие дети."
                    me "Я сказал - успокойтесь."
                    "С этими словами ты выводишь их из воды."
                    $ ds_skill_points['savoir_faire'] += 1
                    $ ds_lp['ya'] += 1
                else:
                    svf "Мальчики оказываются проворными, а их кулаки летают хаотично - тебе сложно их поймать."
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
    show sl normal pioneer at right
    show us laugh sport at center
    show un normal pioneer at left 
    with dissolve
    me "Не возражаете, если я присяду?"
    play sound ds_sfx_int
    rhe "Так как садиться больше некуда, твои слова звучат наиграно."
    show sl smile pioneer at right   with dspr
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
        com "Не подавай виду. Переведи внимание, например, на Лену."
        $ ds_skill_points['composure'] += 1
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
        "Подцепить в ответ":
            if skillcheck('rhetoric', lvl_easy):
                window show
                play sound ds_sfx_int
                rhe "Нет ничего проще - спроси про {i}её{/i} одежду."
                me "Ты-то в чём придёшь, массовик-затейник?"
                show us laugh2 sport at center   with dspr
                us "Се-к-рет!"
                me "Платьице как на детском утреннике небось?"
                show us angry sport at center   with dspr
                rhe "Ульяна краснеет от злости – похоже, ты смог её задеть."
            else:
                window show
                play sound ds_sfx_int
                rhe "Но ты не находишь, что ответить."
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
                com "Держись дальше."
                show us dontlike pioneer at center
                with dspr
                us "Приём-приём! Ну не молчи!"
                $ ds_lp['us'] -= 1
            else:
                window show
                com "Это оказывается последней каплей для тебя."
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

    show us laugh2 sport at center   with dspr
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
        "Не реагировать":
            if skillcheck('composure', lvl_formidable):
                window show
                play sound ds_sfx_mot
                com "Держись спокойно. Будь умнее. Погнавшись за ней, только навлечёшь на себя проблем."
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
                jump ds_day3_after_lunch
            else:
                window show
                play sound ds_sfx_mot
                com "Ты ну никак не можешь стерпеть подобного оскорбления!"

    if skillcheck('savoir_faire', lvl_easy, passive=True):
        scene cg d3_us_dinner 
        with dissolve
        window show
        play sound ds_sfx_mot
        svf "Но в этот раз у неё ничего не вышло – ты хватаешь её за руку."
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
                "Убедить вожатую":
                    if skillcheck('suggestion', lvl_heroic, modifiers=[('ds_last_skillcheck', 1), ('ds_karma >= 50', 3), ('ds_karma <= -50', -4)]):
                        window show
                        play sound ds_sfx_psy
                        sug "Говори чётко. Уверенно."
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
                        jump ds_day3_after_lunch
                    else:
                        window show
                        play sound ds_sfx_psy
                        sug "Ну что ж, попробуй. Но вряд ли вожатая изменит свою позицию."
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
        "Сбежать одному":
            if skillcheck('savoir_faire', lvl_legendary, modifiers=[("ds_lp[['us'] < 0", -2)]):
                window show
                play sound ds_sfx_mot
                svf "Тебе удаётся незаметно прошмыгнуть в дверь, даже не хлопнув ею."
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
                svf "Ты рвёшься в сторону двери..."
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
        "Сбежать с Ульяной":
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
                svf "Вам удаётся незаметно прошмыгнуть в дверь, даже не хлопнув ею."
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
                svf "Ты рвёшься в сторону двери..."
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
        "Сбежать одному":
            if skillcheck('savoir_faire', lvl_legendary, modifiers=[("ds_lp[['us'] < 0", -2)]):
                window show
                play sound ds_sfx_mot
                svf "Тебе удаётся незаметно прошмыгнуть в дверь, даже не хлопнув ею."
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
                svf "Ты рвёшься в сторону двери..."
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
        "Сбежать с Ульяной":
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
                svf "Вам удаётся незаметно прошмыгнуть в дверь, даже не хлопнув ею."
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
                svf "Ты рвёшься в сторону двери..."
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
            scene bg ds_int_kitchen_day
            show us surp1 sport at center
            with dissolve
            us "Ой..."
            show us angry sport at center
            with dspr
            us "Это всё ты!"
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
        "Согласиться":
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
                inf "И резкими чёткими движениями распахиваешь шкаф, хватаешь конфеты, кладёшь их себе в карман и закрывааешь дверь, будто всё так и было."
                $ ds_skill_points['interfacing'] += 1
                $ ds_lp['us'] += 1
                "Ты подходишь к Ульяне."
            else:
                window show
                inf "Ты открываешь дверцу и начинешь искать конфеты... но безуспешно."
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
                        "Изобразить непонимание":
                            if skillcheck('drama', lvl_medium):
                                window show
                                dra "У вас получается убедительно изобразить, будто вы впервые об этих конфетах слышите."
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
                                dra "Ваше лицо, мессир, - оно как открытая книга. Вся ваша ложь отчётливо видна."
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
                        "Назвать фантастичную причину":
                            if skillcheck('conceptualization', lvl_up_medium):
                                window show
                                play sound ds_sfx_int
                                con "Нашествие инопланетян! Вторжение империалистов! У тебя столько идей!"
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
                                con "Ничего складного в голову не приходит... не выйдет захватывающей истории, увы."
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
                        "Изобразить непонимание":
                            if skillcheck('drama', lvl_medium):
                                window show
                                dra "У вас получается убедительно изобразить, будто вы впервые об этих конфетах слышите."
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
                                dra "Ваше лицо, мессир, - оно как открытая книга. Вся ваша ложь отчётливо видна."
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
                        "Назвать фантастичную причину":
                            if skillcheck('conceptualization', lvl_up_medium):
                                window show
                                play sound ds_sfx_int
                                con "Нашествие инопланетян! Вторжение империалистов! У тебя столько идей!"
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
                                con "Ничего складного в голову не приходит... не выйдет захватывающей истории, увы."
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
        res "Тормози!"
        "У тебя получается остановиться так, чтобы её не зацепить."
        $ ds_skill_points['reaction_speed'] += 1
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
        res "У тебя же так резко затормозить не получилось, и ты сбиваешь её с ног."
        $ ds_skill_points['reaction_speed'] += 1
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
    if ds_member['music']:
        $ set_zone_ds_small("music_club", "ds_day3_music")
    if ds_member['cyber']:
        $ set_zone_ds_small("clubs", "ds_day3_cyber")
    $ set_zone_ds_small("forest", "ds_day3_forest")
    $ set_zone_ds_small("medic_house", "ds_day3_medic")
    if ds_punished:
        $ set_zone_ds_small("dining_hall", "ds_day3_punishment_return")
    $ show_small_map_ds()