# DISCO SOVENOK
# ОБЩИЙ РУТ. ДЕНЬ 3

init:
    $ mods["disco_sovenok"] = u'Disco Sovenok'
    $ ds_was_on_lineup = False
    $ ds_accept_mz = False
    $ ds_understood_mz_reason = False

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
                        $ ds_lp['mz'] += 1
                        jump ds_day3_breakfast_un
                    "Остаться с Женей":
                        $ ds_lp['un'] += 1
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

    jump day3_main2