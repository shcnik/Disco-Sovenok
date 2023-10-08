# DISCO SOVENOK
# ОБЩИЙ РУТ. ДЕНЬ 3

init:
    $ mods["disco_sovenok"] = u'Disco Sovenok'
    $ ds_was_on_lineup = False
    $ ds_accept_mz = False
    $ ds_understood_mz_reason = False
    $ ds_promise_un = False
    $ ds_dance_dv = False

label ds_day3_morning:
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
    $ renpy.pause(1.0)
    window show
    play sound ds_sfx_fys
    pat "В душе вода не такая холодная. Ты можешь даже нормально помыться!"
    window hide
    $ renpy.pause(1.0)
    play sound sfx_close_water_sink
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
    lfc "Хотя не проще ли завести часы?"

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
            stop music fadeout 2
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
                jump ds_day3_punishment
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
        "Не садиться":
            window show

label ds_day3_stage_dv:
    $ persistent.sprite_time = "day"
    scene bg ext_stage_normal_day 
    with dissolve

    $ volume(d3_volume,"music")

    play music music_list["kostry"] fadein 5

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
    if (not ds_beat_dv) and (not ds_betray_dv) and (ds_lp['dv'] > 10):
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
        play sound ds_sfx_int
        rhe "Поддерживай разговор. Спроси про планы."
        me "Ясно…{w} И чем планируешь заняться тогда?"
        show dv normal pioneer at center   with dspr
        dv "Буду репетировать дальше."
        window hide
        menu:
            "Расспросить":
                window show
                me "А что ты репетируешь?"
                show dv rage pioneer at center   with dspr
                dv "Песню, придурок! Ты же слышал!"
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
                play sound ds_sfx_mot
                res "Ты такого не говорил…"
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
                                me "Приду обязательно. Спасибо за приглашение!"
                                show dv smile pioneer at center   with dspr
                                dv "Вот и отлично."
                                $ ds_lp['dv'] += 1
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
                        me "Приду обязательно. Спасибо за приглашение!"
                        show dv smile pioneer at center   with dspr
                        dv "Вот и отлично."
                        $ ds_lp['dv'] += 1
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
        edr "Пожалуй, уже действительно пора – голод не тетка."
        "Обернувшись в сторону сцены, ты хочешь позвать Алису с собой."
        "Но она как сквозь землю провалилась."
        th "Знать, когда вовремя уйти, должен любой музыкант."
        window hide
    else:
        "И ты уходишь. Алиса никак не реагирует на это."

    jump ds_day3_lunch