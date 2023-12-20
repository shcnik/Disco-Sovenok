# DISCO SOVENOK
# ОБЩИЙ РУТ. ДЕНЬ 4
# +КОРНИ РУТОВ АЛИСЫ, ЛЕНЫ, СЛАВИ, МИКУ
init python:
    ds_mine_map = {
                    "1":{
                        "1":["3","2"],
                        "2":["3","2"],
                        "3":["3","2"]
                        },
                    "2":{
                        "1":["4","13"],
                        "4":["13","1"],
                        "13":["1","4"]
                        },
                    "3":{
                        "1":["halt","5"],
                        "5":["1","halt"],
                        "halt":["5","1"]
                        },
                    "4":{
                        "2":["5","6"],
                        "5":["6","2"],
                        "6":["2","5"]
                        },
                    "5":{
                        "3":["7","4"],
                        "4":["3","7"],
                        "7":["4","3"]
                        },
                    "6":{
                        "4":["9","12"],
                        "9":["12","4"],
                        "12":["4","9"]
                        },
                    "7":{
                        "5":["10","8"],
                        "8":["5","10"],
                        "10":["8","5"]
                        },
                    "8":{
                        "7":["10","9"],
                        "9":["7","10"],
                        "10":["9","7"]
                        },
                    "9":{
                        "8":["11","6"],
                        "6":["8","11"],
                        "11":["6","8"]
                        },
                    "10":{
                        "7":["halt","8"],
                        "8":["7","halt"],
                        "halt":["8","7"]
                        },
                    "11":{
                        "9":["exit","12"],
                        "12":["9","exit"]
                        },
                    "12":{
                        "13":["6","11"],
                        "6":["11","13"],
                        "11":["13","6"]
                        },
                    "13":{
                        "2":["12","coalface"],
                        "12":["coalface","2"],
                        "coalface":["2","12"]
                        }
            }
    
    def mine_eval(direction):
        
        global ds_point
        global ds_previous_point
        global ds_halt_visited
        global ds_coalface_visited
        global ds_back_to_start
        global ds_mine_route
        global ds_first_turn
        
        if direction == "left":
            old_point = ds_point
            
            ds_point = ds_mine_map[point][previous_point][0]
            ds_previous_point = old_point
        elif direction == "right":
            old_point = ds_point
            
            ds_point = ds_mine_map[point][previous_point][1]
            ds_previous_point = old_point
        
        if point == "exit":
            renpy.jump("ds_"+mine_route+"_day4_mine_exit")
        elif point == "coalface":
            point = "13"
            previous_point = "coalface"
            renpy.jump("ds_"+mine_route+"_day4_mine_coalface")
        elif point == "halt":
            if previous_point == "10":
                point = "3"
                previous_point = "halt"
            elif previous_point == "3":
                point = "10"
                previous_point = "halt"
            renpy.jump("ds_"+mine_route+"_day4_mine_halt")
        elif back_to_start and point == "1":
            if mine_route == "me":
                renpy.jump("ds_day4_alone_mine_return")
            else:
                renpy.jump("ds_day4_girls_mine_return")
        else:
            ds_back_to_start = True
            renpy.jump("ds_day4_mine_crossroad")

label ds_day4_morning:
    $ backdrop = "days"

    $ new_chapter(4, u"Disco Sovenok. День 4.")
    $ save_name = u"Disco Sovenok. Общий рут. День 4."

    if ds_day3_evening_who == 'us':
        jump ds_day4_us_morning

    $ day_time()

    scene bg int_house_of_mt_day  with fade:
        linear 0.1 pos (-5,-5)
        linear 0.1 pos (0,0)
        linear 0.1 pos (5,5)
        linear 0.1 pos (0,5)
        linear 0.1 pos (5,0)
        linear 0.1 pos (0,0)
        repeat

    window show
    "Ты просыпаешься от адского звона в голове."
    "Кажется, этот звук идёт откуда-то из глубин сознания."
    window hide

    $ renpy.pause(2)

    window show
    play sound ds_sfx_int
    lgc "Однако, несколько придя в себя, ты понимаешь, что виной всему – будильник."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_house_of_mt_day 
    with dissolve

    play ambience ambience_int_cabin_day fadein 2

    window show
    play sound ds_sfx_mot
    per_eye "Часы показывают полвосьмого утра."
    if ds_sl_workouts:
        jump ds_day4_sl_workout
    elif ds_morning_exercise:
        jump ds_day4_morning_exercise
    play sound ds_sfx_psy
    vol "Ольга Дмитриевна, похоже, уже ушла, а значит, на линейку идти тебя никто не заставит. Тем более, что ты её благополучно проспал."
    window hide
    menu:
        "Встать":
            window show
            th "Но я всё же лучше туда схожу."
            vol "Однако, перед этим, очевидно, стоит умыться."
        "Поспать ещё":
            window show
            th "Следовательно, можно ещё поспать."
            "Ты закрываешь глаза..."
            play sound ds_sfx_fys
            edr "Но твоё сознание уже переключилось в дневной режим – получается, пора вставать."
            vol "Стоит распланировать день – в конце концов, хоть сегодня необходимо что-то выяснить!"
            th "Надо окончательно проснуться, а заодно и заняться утренним туалетом."
    window hide

    stop ambience fadeout 2

    jump ds_day4_washing

label ds_day4_washing:
    $ persistent.sprite_time = "day"
    scene bg ext_houses_day 
    with dissolve

    play music music_list["everyday_theme"] fadein 3

    show mz normal glasses pioneer at center   with dissolve
    window show
    "По дороге к умывальникам ты встречаешь Женю."
    me "Чего это ты в такую рань?"
    show mz angry glasses pioneer at center   with dspr
    mz "А что такого?"
    "Она смотрит на тебя так, как будто ты её чем-то обидел."
    me "Ничего, просто спросил."
    mz "Вот и иди куда шёл!"
    hide mz  with dissolve
    play sound ds_sfx_psy
    emp "Конечно, Женя и в лучшем настроении не очень приветлива, но сегодня она кажется чересчур озлобленной."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_washstand_day 
    with dissolve

    window show
    play sound ds_sfx_fys
    edr "Холодная вода немного взбодрила тебя, туман в голове рассеивается, а мысли начинают потихоньку вставать на места."

    if ds_skill_list['perception'].check(lvl_easy, passive=True).result():

        play sound sfx_bush_leaves
        $ renpy.pause(0.5)
        play sound ds_sfx_mot
        per_hea "{result}Ты почистил зубы и уже собирался было уходить, как вдруг со стороны кустов доносится тихий шорох."
        play sound ds_sfx_int
        lgc "Наверное, белка или ещё какой зверёк."
        per_hea "Шорох раздаётся вновь, но уже чуть дальше."
        window hide
        menu:
            "Проверить":
                window show

                $ persistent.sprite_time = "day"
                scene bg ext_path2_day 
                with dissolve

                window show
                "Ты проходишь с десяток метров по лесной тропинке в поисках источника звука."

                stop music fadeout 4

                "Но никого и ничего найти не удаётся – лишь утренний лес вокруг, такой, каким он и должен быть."
                window hide

                $ persistent.sprite_time = "day"
                scene bg ext_washstand_day 
                with dissolve

                play music music_list["so_good_to_be_careless"] fadein 3

                show mi normal pioneer far at center   with dissolve
                window show
                "Ты возвращаешься назад и около умывальников видишь Мику, которая что-то высматривает в траве."
                show mi normal pioneer at center   with dissolve
                "Заметив тебя, она оживляется, улыбается и подскакивает ко мне."
                mi "Ой, привет, доброе утро! А я тут, знаешь, зубной порошок рассыпала, вот теперь собрать пытаюсь."
                play sound ds_sfx_int
                vic "Покрытая росой трава этому явно не способствует."
                me "А ты уверена, что это хорошая идея?"
                show mi upset pioneer at center   with dspr
                mi "Ну, как же! Как же! У меня ведь больше нет! Это был последний!"
                "Мику надувает губки."
                play sound ds_sfx_psy
                ine "Как ребёнок, у которого отняли любимую игрушку."
                window hide
                menu:
                    "Предложить свой порошок":
                        window show
                        me "Возьми мой."
                        $ ds_lp['mi'] += 1
                        "Ты лезешь в пакет, который лежал рядом с умывальником."
                        "Но порошка там не оказывается."
                        play sound ds_sfx_mot
                        res "Так ведь ты только что его туда положил!{w} Отошёл буквально на минутку, а он исчез…"
                        play sound ds_sfx_psy
                        sug "Не стоит ей говорить, что порошок пропал. Зная её впечатлительность, можно предположить, что исчезающие средства гигиены могут вызвать у неё такую бурю эмоций, что твой мозг уйдёт на перезагрузку во избежание перегрева."
                        window hide
                        menu:
                            "Сказать, что забыл":
                                window show
                                me "Слушай, похоже, я его забыл…"
                                mi "Ну ничего страшного тогда, Семён-кун, бывает, попрошу порошок у кого-нибудь ещё."
                            "Сказать правду":
                                window show
                                me "А тут порошок пропал. Вот буквально на минуту отвернулся - и нет порошка."
                                show mi scared pioneer at center with dspr
                                mi "Как так? Кто же украл порошок? Кому мог понадобиться твой порошок? Кто же этот воришка зубных порошков?.."
                                sug "Как и было предсказано - ты с трудом выносишь поток её мыслей."
                                mi "...Нет, нам нужно обязательно выяснить, кто же совершил такую подлость по отношению к тебе, ко мне, к нам!"
                        me "Ладно, я пойду тогда…"
                        show mi smile pioneer at center   with dspr
                        mi "Да, конечно! Ты заходи к нам… Будем тебе всегда…"
                        hide mi  with dissolve
                    "Начать собирать порошок" (skill='interfacing', level=lvl_unimaginable):
                        if ds_last_skillcheck.result():
                            window show
                            inf "{result}Ты наклоняешься и начинаешь отделять зёрна от плевел - то бишь порошок от земли."
                            inf "Половина порошка уже растворилась в росе, но невероятной точностью пальцев тебе удаётся вытащить остальное."
                            me "Вот... то, что я собрал..."
                            $ ds_lp['mi'] += 2
                            show mi surprise pioneer at center
                            with dspr
                            mi "Ого... Ты так перебирал пальцами... Тебе точно надо играть на чём-нибудь!"
                            show mi smile pioneer at center
                            with dspr
                            mi "В общем, заходи к нам! Будем тебе всегда..."
                        else:
                            window show
                            inf "{result}Ты наклоняешься и вслед за Мику пытаешься собрать порошок."
                            inf "Однако, не менее половины порошка уже растворилась в росе, а остальная часть смешалась с землёй и непригодна к использованию."
                            inf "Вcё, что тебе удаётся спасти - жалкие крупицы."
                            me "Вот... то, что я собрал..."
                            $ ds_lp['mi'] += 1
                            show mi smile pioneer at center
                            with dspr
                            mi "Всё равно спасибо, Семён-кун! На один раз тут хватит, а потом я попрошу у Ольги Дмитриевны-сан новый порошок."
                            me "Ладно, я пойду тогда…"
                            show mi smile pioneer at center   with dspr
                            mi "Да, конечно! Ты заходи к нам… Будем тебе всегда…"
                            hide mi  with dissolve
                        
                    "Посочувствовать":
                        window show
                        me "Печально..."
                        show mi sad pioneer at center
                        with dspr
                        mi "Да... придётся идти, искать Ольгу Дмитриевну-сан и просить у неё порошка..."
                        me "Ладно, я пойду тогда…"
                        hide mi with dissolve
                    "Посмеяться":
                        window show
                        me "Вот ты растяпа! Как так можно было!"
                        show mi angry pioneer at center
                        with dspr
                        mi "Я на тебя посмотрю, когда ты потеряешь порошок и точно так же будешь лазить в земле, а все остальные будут смеяться над тобой! Я всё припомню тебе, Семён!"
                        play sound ds_sfx_int
                        rhe "Она не применила суффикс вежливости «-кун». Определённо, ты её сильно разозлил."
                        show mi dontlike pioneer at center
                        with dspr
                        mi "Я пошла просить новый порошок, а ты смейся тут один!"
                        hide mi with dissolve
                        $ ds_lp['mi'] -= 2
                    "Молча уйти":
                        window show
                        "Ты разворачиваешься и уходишь."
                        $ ds_lp['mi'] -= 1

                stop music fadeout 4

                "Голос Мику растворяется в свежести летнего утра далеко позади тебя."
            "Забить":
                window show
                "Ты уходишь, не обращая внимания на звук."
        window hide
    else:
        "Ты уходишь в сторону домика Ольги Дмитриевны."

    $ persistent.sprite_time = "day"
    scene bg int_house_of_mt_day 
    with dissolve

    play music music_list["sweet_darkness"] fadein 5

    window show
    inf "Проверь мобильный телефон."
    window hide
    menu:
        "Проверить":
            window show
            "Ты достаёшь мобильник и смотришь на индикатор батареи."
            play sound ds_sfx_int
            lgc "Судя по всему, жить ему оставалось не более суток."
            lgc "Конечно, здесь он мне особо не поможет, но всё же…"
            lgc "А найти в восьмидесятых годах зарядку от сотового телефона – почти то же самое, что изобрести его."
    play sound ds_sfx_psy
    ine "Несмотря ни на что утро прекрасно."
    ine "Яркое солнце освещает пионерлагерь «Совёнок», согревает его обитателей и придаёт им силы провести этот день с пользой."
    play sound ds_sfx_psy
    vol "Или в моём случае, быть может, угробить его на тщетные попытки найти разгадку всего происходящего."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_away_day 
    with dissolve

    play sound_loop ambience_medium_crowd_outdoors fadein 2

    play ambience ambience_camp_center_day fadein 4

    window show
    "У столовой необычайно многолюдно."
    "Конечно, на завтрак, обед и ужин местные обитатели спешат как на пожар, но зачем же толпиться в дверях?.."
    "Ты подходишь поближе и пытаешься узнать, что происходит."
    window hide

    stop music fadeout 3

    jump ds_day4_sh_lost

label ds_day4_us_morning:

    scene bg black 

    window show
    play sound ds_sfx_mot
    per_toc "Во сне ты ощутил тепло."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_library_day 
    with dissolve

    play ambience ambience_music_club_day fadein 3

    window show
    "Такое часто бывает – мозг ещё не включился, но ты всё равно чувствуешь, как солнце бьёт в глаза, и когда просыпаешься, некоторое время щуришься, чтобы привыкнуть к яркому свету."
    play sound ds_sfx_psy
    ine "Прекрасное утро.{w} На улице воркуют птички, воздух свеж и прян, и весь мир купается в лучах наступающего дня."
    play sound ds_sfx_psy
    vol "Ты бы с удовольствием полежал ещё..."
    play sound ds_sfx_fys
    hfl "Но что-то не так!"
    ine "Все события минувшего вечера за секунду пролетают у тебя перед глазами."
    ine "Страшные и не очень истории, Ульяна…"
    window hide

    stop ambience fadeout 2

    scene cg d4_us_morning 
    with fade

    play music music_list["i_want_to_play"] fadein 3

    window show
    "Которая крепко обнимает тебя и совсем не по-детски храпит."
    play sound ds_sfx_mot
    com "Но ты ничуть не волнуешься."
    play sound ds_sfx_int
    lgc "В конце концов, время ещё раннее – вряд ли больше семи или восьми утра."
    lgc "Ну кому понадобится идти в библиотеку в такой час?"
    "Ты откидываешься назад и смотришь в окно."
    play sound ds_sfx_int
    vic "Судя по всему, буквально через пару минут солнце займёт такое положение, что будет бить Ульянке в глаза."
    th "Вот тогда ты и проснёшься!"
    th "Интересно, как же она так крепко смогла меня обнять?"
    th "Ведь действительно, вырваться никак не получается…"
    phi "А может попробовать снова?"
    window hide
    menu:
        "Подняться" (skill='physical_instrument', level=lvl_godly):
            if ds_last_skillcheck.result():
                window show
                phi "{result}И раз! Ты поднимаешься..."
                phi "И два! Давай!"
                "У тебя получается подняться, и ты уже собираешься уходить..."
                
                play sound ds_sfx_mot
                per_hea "Но тут слышатся шаги."
                window hide
                menu:
                    "Сбежать":
                        window show
                        play sound ds_sfx_mot
                        svf "Ты выпрыгиваешь в окно и следуешь прямо к умывальникам."
                        play sound ds_sfx_fys
                        edr "Действительно - тебе было бы неплохо умыться."
                        $ ds_lp['us'] -= 1
                        jump ds_day4_washing
                    "Спрятаться":
                        window show
                    "Стоять на месте":
                        window show
                        jump ds_day4_us_captured
            else:
                window show
                phi "{result}Безнадёжно. Твои рывки ни к чему не приводят, Ульяна не двигается ни на миллиметр."
                play sound ds_sfx_mot
                per_hea "К тому же ты внезапно слышишь шаги."
        "Остаться лежать":
            window show

            play sound ds_sfx_fys
            edr "В принципе, ты был бы готов пролежать так ещё час или два."
            play sound ds_sfx_mot
            per_hea "Ещё и шаги!"

    stop music fadeout 3

    play ambience ambience_music_club_day fadein 3

    play sound ds_sfx_fys
    hfl "Дело пахнет керосином!"
    me "Вставай! Слышишь?! Просыпайся!"
    "Ты аккуратно, но в то же время настойчиво начинаешь трясти Ульяну за плечи, пытаешься ослабить захват, но безуспешно."
    "А в это время шаги всё приближаются."
    hfl "Спасаться во что бы то ни стало!"
    window hide
    menu:
        "Ползти" (skill='savoir_faire', level=lvl_legendary):
            if ds_last_skillcheck.result():
                window show
                svf "{result}Встать не получится, поэтому ты ползёшь."
            else:
                window show
                svf "{result}Однако, всё настолько плохо, что ты не можешь даже с места сдвинуться!"
                jump ds_day4_us_captured
            play sound ds_sfx_int
            con "Твои манёвры очень напоминают военные сборы, на которых ты никогда не был, – солдат тащит за собой раненого командира под миномётным обстрелом."
            con "Командир без сознания, солдат измотан, а кругом – колючая проволока…"
            window hide

            scene cg day4_us_morning 
            with dissolve

            window show

            play sound sfx_open_door_clubs_2

            "Ты только и успеваешь, что заползти за шкаф и перевернуть Ульяну так, чтобы её не было видно, как дверь в библиотеку распахнулась."
            "На пороге стоит Женя."
            play sound ds_sfx_int
            lgc "Похоже, она слишком уж трепетно относится к своей работе, раз приходит сюда с первыми петухами."
            el "… подожди!"
            con "Вот, собственно, наверное, и первые петухи пожаловали…"
            mz "Почему это нельзя было сделать вчера? Или сегодня, но попозже?"
            el "Потому что наука не терпит промедлений!"
            mz "Наука…"
            mz "Сейчас, подожди, я поищу."

            "Она направляется в вашу сторону."
            menu:
                "Сместиться дальше":
                    window show
                    "Ты из последних сил переворачиваещь Ульянку так, чтобы она оказалась у тебя на спине, кое-как встаёшь на четвереньки и пользёшь к соседнему шкафу, где падаешь и пытаешься отдышаться."
                "Оставаться на месте":
                    window show
                    "Впрочем, Женя останавливается так, что вас всё ещё не видно."
            mz "Как ты говорил? Кибернетическая математика?..{w} Или математическая кибернетика?.."
            hfl "Похоже, она вас не заметила."
            el "Мне бы что-нибудь про «Теорию автоматов»…"
            mz "Откуда у нас тут про оружие? Ты что, сдурел?!"
            el "Так это не про оружие совсем…"
            if ds_skill_list['encyclopedia'].check(lvl_challenging, passive=True).result():
                play sound ds_sfx_int
                enc "{result}Он говорит про математический объект «автомат»."
            "Какое-то время они оба молчат."
            el "Жень…"
            mz "Чего ещё?"
            el "А пойдём сегодня вечером на речку…"
            mz "Это зачем?"
            el "Ну…{w} Просто…"
            if ds_el_mz_relation:
                mz "Ладно, пойдём."
                el "Отлично, тогда до встречи!"
                play sound sfx_close_door_clubs_nextroom
                "Дверь закрывается."
            else:
                mz "У меня здесь дел много…{w} А ты иди давай, робот твой тебя ждёт."
                el "Ладно…"
                play sound sfx_close_door_clubs_nextroom
                play sound2 ds_sfx_int
                dra "Звук закрывающейся двери звучит эпитафией любовным страданиям Электроника."

            stop ambience fadeout 2

            play music music_list["i_want_to_play"] fadein 3

            hfl "Тебе предстоит как-то выбраться отсюда незамеченными."
            play sound ds_sfx_mot
            svf "Самое простое решение - дождаться, когда Женя уйдёт завтракать."
            play sound ds_sfx_mot
            edr "Всё же она ударница коммунистического труда, а не один из мифических роботов Электроника, поэтому потребность в пище для неё никто не отменял."
            "Ульяна тем временем и не думает просыпаться."
            th "Хорошо хоть храпеть перестала."
            "В библиотеке тихо."
            "Что делает Женя, ты не видишь, но такое положение вещей до определённой степени тебя устраивает."

            play sound sfx_radio_tune

            play sound2 ds_sfx_mot
            per_hea "Вдруг со стороны её стола доносятся непонятные звуки: щёлканье, шипение и…{w} играет музыка."
            play sound ds_sfx_int
            enc "Точнее, гимн!"
            th "Приехали."
            play sound ds_sfx_int
            con "И всё бы ничего, если бы Женя не начала подпевать!"
            mz "Союз нерушимый…"
            play sound ds_sfx_psy
            vol "Её чувству патриотизма остаётся только позавидовать."
            con "Хотя с голосом у неё явные проблемы – советская эстрада в её лице уж точно не потеряла талантливую певицу."
            "После гимна чей-то голос рассказывает о перевыполнении плана по уборке зерновых."
            if ds_skill_list['logic'].check(lvl_trivial, passive=True).result():
                play sound ds_sfx_int
                lgc "{result}Очевидно, Женя включила радио."
            window hide
            menu:
                "Вслушаться":
                    window show
                    "Ты внимательно вслушиваешься – возможно, удастся что-нибудь узнать."
                    "Однако после сводок с полей голос диктора начинает пропадать, а через некоторое время исчезает вовсе."
                    th "Может быть, помехи…"
                "Проигнорировать":
                    window show
            "Женя встаёт и направляется в нашу сторону."
            "Ситуация становилась критической."
            if ds_skill_list['physical_instrument'].check(lvl_legendary, passive=True).result():
                play sound ds_sfx_fys
                phi "{result}Титаническим усилием воли тебе всё же удаётся разжать захват Ульянки."
                play sound ds_sfx_fys
                edr "Теперь ты свободен, но настолько измотан всеми этими поползновениями, что не чувствуешь в себе сил даже встать."
            th "Пора готовиться к худшему и заранее придумать оправдания…"
            "Но внезапно шаги стихают."
            "Судя по всему, Женя останавливается с другой стороны шкафа, за которым лежите вы."
            "Слышится шуршание книг."
            th "Наверное, что-то ищет."
            "Взяв книгу, она возвращается к столу."

            play sound sfx_open_door_strong

            "В этот момент с грохотом распахивается дверь."
            mt "Семён?!{w} Не видела?"
            "Ольга Дмитриевна явно сильно запыхалась."
            mt "Ульяна?!"
            mz "Нет…"
            window hide
            menu:
                "Вылезти":
                    window show
                    scene bg int_library_day
                    show mt surprise pioneer at left
                    show mz amazed glasses pioneer at right
                    with dissolve
                    me "Здрасьте, а вот и я!"
                    show mt angry pioneer at left
                    show mz rage glasses pioneer at right
                    with dspr
                    mt "А что ты тут делаешь, Семён?!"
                    mz "Да! Как ты сюда проник и что забыл?!"
                    mt "И где Ульяна?! Я вас вместе отправляла сюда!"
                    show mz angry glasses pioneer at right
                    with dspr
                    mz "Вы сюда этих обалдуев отправили, Ольга Дмитриевна?!"
                    mt "Так надо было! Не лезь!"
                    window hide
                    menu:
                        "Сказать про Ульяну":
                            window show
                            me "Да она тут... спит... а я за ней слежу..."
                        "Скрыть Ульяну":
                            window show
                            me "Да вы знаете, Ульяна сбежала, библиотеку заперла, вот мне и пришлось сидеть тут."
                            show mz sceptic glasses pioneer far at fright
                            with dspr
                            "Однако, Женя не поверила и заглянула туда, откуда ты вылез."
                            mz "Ольга Дмитриевна, а не её ли вы ищете?"
                            show mt surprise pioneer at left
                            with dspr
                            mt "Ульяна?!"
                            $ ds_karma -= 10
                            $ ds_lp['mt'] -= 1
                    mt "УЛЬЯНА, ПОДЪЁМ!"
                    "С этими словами она трясёт девочку так сильно, что она вынуждена проснуться."
                    show us calml pioneer at center
                    with dspr
                    us "А... что происходит?.."
                    show mz rage glasses pioneer at right
                    with dspr
                    mz "Что с тобой это отродье человечества сделало?!"
                    us "Да ничего... посидели, порассказывали друг другу истории... а потом я испугалась и отрубилась..."
                    show mt normal pioneer at left
                    with dspr
                    mt "Ох, ну слава тебе господи! А то тут Женя нарассказывала мне..."
                    show mz confused glasses pioneer at fleft
                    with dspr
                    mz "Ну, да, повезло в этот раз..."
                    mt "Жень, тебе было бы неплохо извиниться перед Семёном."
                    show mz sceptic glasses pioneer at fleft
                    with dspr
                    mz "Извини!"
                    play sound sfx_close_door_1
                    hide mz with dissolve
                    "И Женя уходит, хлопнув дверью."
                    show mt angry pioneer at left
                    show us surp1 pioneer at right
                    with dspr
                    mt "А теперь, когда мы выяснили, что УК тут не нарушали, вы мне не хотите ничего объяснить?!"
                    if ds_skill_list['authority'].check(lvl_medium, passive=True).result():
                        play sound ds_sfx_psy
                        aut "{result}Держись ровно, спокойно. Просто ответь."
                    window hide
                    menu:
                        "Спокойно ответить" if ds_last_skillcheck.result():
                            window show
                            me "Ну, мы сидели в библиотеке, как вы и велели, ну и уснули..."
                            mt "Вообще замечательно: вы уснули, а я потом бегай отвечай за вас!"
                            show mt normal pioneer at left
                            with dspr
                            mt "Хотя, с другой стороны, и я должна была проверить библиотеку в первую очередь, сама ведь вас послала..."
                            show mt angry pioneer at left
                            with dspr
                            mt "В общем, дуйте умываться! У меня и без вас забот полон рот!"
                        "Театрально покаяться" (skill='drama', level=lvl_up_medium):
                            if ds_last_skillcheck.result():
                                window show
                                dra "{result}Вы наиграно бросаетесь ей в ноги."
                                me "Не велите казнить, велите миловать, государыня-надёжа!"
                                show mt rage pioneer at left
                                show us laugh pioneer at right
                                with dspr
                                mt "Что это за цирк ты тут устроил?!"
                                dra "Протестую: это не цирк, это театр!"
                                play sound ds_sfx_psy
                                emp "А вот Ульяна твоё представление оценила."
                                $ ds_lp['us'] += 1
                                mt "Я и не собиралась тебя казнить! Иди мыться и завтракать, и ты, Ульяна, тоже!"
                            else:
                                window show
                                dra "{result}Вам не удаётся обыграть это красиво."
                                me "Извините, пожалуйста, Ольга Дмитриевна, больше такого не повторится!"
                                mt "Я надеюсь! А теперь дуйте умываться!"
                            
                        "Извиниться":
                            window show
                            me "Извините..."
                            mt "В общем, всё, идите умываться, а потом собираемся около столовой!"
                        "Улизнуть" (skill='savoir_faire', level=lvl_godly):
                            if ds_last_skillcheck.result():
                                window show
                                play sound ds_sfx_mot
                                svf "{result}Ты резко срываешься с места, обегаешь Ольгу Дмитриевну и выбегаешь на улицу."
                                scene bg ext_library_day:
                                    zoom 1.05 anchor (48,27)
                                    ease 0.20 pos (0, 0)
                                    ease 0.20 pos (25,25)
                                    ease 0.20 pos (0, 0)
                                    ease 0.20 pos (-25,25)
                                    repeat
                                with dspr
                                mt "СТОЯТЬ!"
                                "Ты бежишь дальше."
                                scene bg ext_square_day
                                with dissolve
                                "Лишь выбежав на площадь, ты останавливаешься. Кажется, Ольга Дмитриевна тебя не преследует."
                                
                                $ ds_lp['us'] -= 1
                                $ ds_karma -= 10
                                $ ds_lp['mt'] -= 1
                                "Ты идёшь умываться."
                                jump ds_day4_washing
                            else:
                                window show
                                svf "{result}Однако, ты утыкаешься прямо в Ольгу Дмитриевну."
                                show mt angry pioneer close at center
                                with dspr
                                mt "А ну куда пошёл?!"
                                
                                $ ds_karma -= 5
                                $ ds_lp['mt'] -= 1
                                show mt angry pioneer at left
                                with dspr
                                mt "Ладно, дуйте умываться! У меня и без вас забот полон рот!"
                    scene bg ext_library_day
                    show us smile pioneer at center
                    with dissolve
                    play sound ds_sfx_psy
                    vol "Между прочим, Ульяна спасла тебя от ужасной кары."
                    play sound ds_sfx_psy
                    aut "Ага, только она сама чуть не навлекла её на тебя."
                    window hide
                    menu:
                        "Поблагодарить Ульяну":
                            window show
                            me "Спасибо..."
                            show us surp2 pioneer at center
                            with dspr
                            us "За что?"
                            me "За то, что прикрыла меня от обвинений..."
                            show us laugh pioneer at center
                            with dspr
                            us "А, это да! Ну, в общем-то зачем мне было бы на тебя клеветать!"
                            $ ds_lp['us'] += 1
                        "Просто попрощаться":
                            window show
                    me "Ладно, я пойду!"
                    us "Ага, до встречи!"
                    hide us with dissolve
                    "И она убегает. А ты идёшь умываться."
                    jump ds_day4_washing
                "Сидеть дальше":
                    window show

            play sound sfx_close_door_1

            "Дверь хлопает, так же громко, как и в первый раз."
            play sound ds_sfx_fys
            hfl "Похоже, вас уже ищут, и сейчас Женя начнёт обход библиотеки…"

            play sound sfx_dinner_horn_processed

            "Однако в этот момент вдалеке играет музыка, призывающая пионеров на завтрак."
            "Женя, как и подобает пунктуальному человеку, не задерживается, и через минуту в библиотеке вы вновь остаётесь вдвоём – ты и Ульяна."
            play sound ds_sfx_psy
            vol "Теперь предстоит решить, что делать с ней…"
            hfl "Уже можешь не бояться, что тебя кто-то услышит."
            window hide
            menu:
                "Разбудить Ульяну":
                    window show
                "Уйти":
                    window show
                    "Ты просто уходишь, оставив Ульяну досыпать."
                    scene bg ext_library_day
                    with dissolve
                    $ ds_lp['us'] -= 1
                    th "Так, уже пора идти позавтракать..."
                    $ persistent.sprite_time = "day"
                    scene bg ext_dining_hall_away_day 
                    with dissolve

                    play sound_loop ambience_medium_crowd_outdoors fadein 2

                    window show
                    "У столовой необычайно многолюдно."
                    play sound ds_sfx_int
                    lgc "Конечно, на завтрак, обед и ужин местные обитатели спешат как на пожар, но зачем же толпиться в дверях?.."
                    "Ты подходишь поближе в надежде узнать, что происходит."
                    window hide

                    jump ds_day4_sh_lost
            me "Проснись и пой!"
            window hide
        "Оставаться на месте":
            window show
            jump ds_day4_us_captured

    $ persistent.sprite_time = "day"
    scene bg int_library_day 
    with dissolve

    show us fear pioneer at center   with dissolve
    window show
    "Она мгновенно вскакивает и начинает спросонья озираться по сторонам."
    show us normal pioneer at center   with dspr
    "Заметив тебя, Ульяна удивилась."
    show us surp3 pioneer at center   with dspr
    us "А что ты здесь делаешь?"
    me "Играю в разведчиков."
    us "А?"
    me "Неважно… Выспалась?"
    show us surp1 pioneer at center   with dspr
    us "Да…"
    play sound ds_sfx_psy
    emp "Кажется, она ещё не совсем пришла в себя."
    me "Завтракать?"

    stop music fadeout 3

    us "Да…"
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_library_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "Вы выходите из библиотеки."
    th "Наконец-то!"
    play sound ds_sfx_psy
    sug "Теперь уж точно не придётся никому объяснять, что, как и почему я делал с Ульяной там всю ночь…"
    show us shy pioneer at center   with dissolve
    us "Ты прости, что я так вот заснула…"
    window hide
    menu:
        "Принять":
            window show
            me "Да ничего."
            play sound ds_sfx_int
            rhe "Похоже, твои слова прозвучали слишком скептически, потому что она смотрит на тебя с недоверием."
        "Начать отчитывать":
            window show
            me "Просто «прости»?! Да мне из-за тебя пришлось всю ночь с тобой провести, ещё и рискуя быть обвинённым в чёи-нибудь нехорошем!"
            $ ds_lp['us'] -= 1
    show us normal pioneer at center   with dspr
    us "Подожди-ка…{w} А что ты всё время там делал?"
    me "Ты не поверишь…"
    show us surp1 pioneer at center   with dspr
    us "Подожди-ка…{w} То есть…"
    show us laugh pioneer at center   with dspr
    "Ульянка хихикает, отбегает от тебя на пару метров и звонко кричит."
    show us laugh pioneer far at center    with dissolve
    us "А я первая на завтрак!"
    hide us  with dissolve
    me "После такого-то пит-стопа немудрено…"
    play sound ds_sfx_int
    vic "Ульяна уже не может тебя слышать, так как убежала далеко."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_away_day 
    with dissolve

    play sound_loop ambience_medium_crowd_outdoors fadein 2

    window show
    "У столовой необычайно многолюдно."
    play sound ds_sfx_int
    lgc "Конечно, на завтрак, обед и ужин местные обитатели спешат как на пожар, но зачем же толпиться в дверях?.."
    "Ты подходишь поближе в надежде узнать, что происходит."
    window hide

    jump ds_day4_sh_lost

label ds_day4_us_captured:
    $ ds_caught_in_lib = True
    play sound sfx_open_door_clubs_2
    scene bg int_library_day
    show mz angry glasses pioneer at left
    with dissolve
    "На пороге стоит Женя."
    play sound ds_sfx_int
    lgc "Похоже, она слишком уж трепетно относится к своей работе, раз приходит сюда с первыми петухами."
    show el normal pioneer at right
    with dissolve
    el "… подожди!"
    mz "Что ты тут делаешь?! И как ты сюда попал?!"
    "Тут она замечает и Ульяну."
    show mz scared glasses pioneer at left
    with dspr
    mz "Ещё и с девочкой?! ЧТО ТЫ С НЕЙ ДЕЛАЛ ТУТ, ИРОД?!"
    $ ds_lp['mz'] -= 5
    if ds_skill_list['rhetoric'].check(lvl_easy, passive=True).result():
        rhe "{result}Она ведёт к тому, что ты изнасиловал Ульяну."
    me "Успокойся... Я ничего с ней не делал..."
    show mz rage glasses pioneer at left
    show el surprise pioneer at right
    with dspr
    mz "Ага, так я тебе и поверила! Так, я иду к Ольге Дмитриевне!"
    show mt angry pioneer at center
    with dissolve
    mt "Можешь не идти: я сама пришла. Что тут происходит?!"
    th "Только этого не хватало..."
    show mt rage pioneer at center
    with dspr
    mt "Так, значит, Семён, ты в библиотеке всю ночь провёл, значит?!"
    mt "Я, значит, всю ночь его ждала, а он..."
    mz "Да он тут и девочек насилует по ночам!"
    show mt shocked pioneer at center
    with dspr
    mt "ЧЕГО?!"
    th "ЧЕГО?!"
    mt "Ты уверена, Женя?"
    if ds_karma >= 50:
        mt "Семён же прилежный пионер, и он станет насиловать?"
        mz "Да все мужики притворяются приличными, а потом..!"
    elif ds_karma <= -50:
        mt "Я, конечно, понимаю, что Семён далеко не пример для подражания, но всё же..."
        mz "Да, уверена, все мужики одинаковые!"
    else:
        mt "Ну, не знаю... не похоже на него..."
        mz "Да, уверена, все мужики одинаковые!"
    show us calml pioneer at fright
    with dissolve
    us "Что тут происходит..?"
    show mt scared pioneer at right
    show el shocked pioneer at left
    show mz rage glasses pioneer at fleft
    with dspr
    mt "Ты как, Ульяна? С тобой всё хорошо?"
    us "Да вроде да..."
    mz "Что с тобой этот выродок сделал?!"
    play sound ds_sfx_psy
    aut "Что она себе позволяет?!"
    window hide
    menu:
        "Возмутиться":
            window show
            me "И ничего я не выродок!"
            mz "МОЛЧИ!"
        "Промолчать":
            window show
    us "Да ничего он не делал... просто рассказывали друг другу страшные истории, потом я испугалась и отрубилась..."
    show mt normal pioneer at right
    with dspr
    mt "Ох, ну слава тебе господи! А то тут Женя нарассказывала мне..."
    show mz confused glasses pioneer at fleft
    with dspr
    mz "Ну, да, повезло в этот раз..."
    mt "Жень, тебе было бы неплохо извиниться перед Семёном."
    show mz sceptic glasses pioneer at fleft
    with dspr
    mz "Извини!"
    play sound sfx_close_door_1
    hide mz with dissolve
    "И Женя уходит, хлопнув дверью."
    show el upset pioneer at left
    with dspr
    el "Жень, подожди, а как же..."
    play sound sfx_close_door_clubs_nextroom
    hide el with dissolve
    "Электроник убегает за ней."
    show mt angry pioneer at left
    show us surp1 pioneer at right
    with dspr
    mt "А теперь, когда мы выяснили, что УК тут не нарушали, вы мне не хотите ничего объяснить?!"
    if ds_skill_list['authority'].check(lvl_medium, passive=True).result():
        play sound ds_sfx_psy
        aut "{result}Держись ровно, спокойно. Просто ответь."
    window hide
    menu:
        "Спокойно ответить" if ds_last_skillcheck.result():
            window show
            me "Ну, мы сидели в библиотеке, как вы и велели, ну и уснули..."
            mt "Вообще замечательно: вы уснули, а я потом бегай отвечай за вас!"
            show mt normal pioneer at left
            with dspr
            mt "Хотя, с другой стороны, и я должна была проверить библиотеку в первую очередь, сама ведь вас послала..."
            show mt angry pioneer at left
            with dspr
            mt "В общем, дуйте умываться! У меня и без вас забот полон рот!"
        "Театрально покаяться" (skill='drama', level=lvl_up_medium):
            if ds_last_skillcheck.result():
                window show
                dra "{result}Вы наиграно бросаетесь ей в ноги."
                me "Не велите казнить, велите миловать, государыня-надёжа!"
                show mt rage pioneer at left
                show us laugh pioneer at right
                with dspr
                mt "Что это за цирк ты тут устроил?!"
                dra "Протестую: это не цирк, это театр!"
                play sound ds_sfx_psy
                emp "А вот Ульяна твоё представление оценила."
                $ ds_lp['us'] += 1
                mt "Я и не собиралась тебя казнить! Иди мыться и завтракать, и ты, Ульяна, тоже!"
            else:
                window show
                dra "{result}Вам не удаётся обыграть это красиво."
                me "Извините, пожалуйста, Ольга Дмитриевна, больше такого не повторится!"
                mt "Я надеюсь! А теперь дуйте умываться!"
            
        "Извиниться":
            window show
            me "Извините..."
            mt "В общем, всё, идите умываться, а потом собираемся около столовой!"
        "Улизнуть" (skill='savoir_faire', level=lvl_godly):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_mot
                svf "{result}Ты резко срываешься с места, обегаешь Ольгу Дмитриевну и выбегаешь на улицу."
                scene bg ext_library_day:
                    zoom 1.05 anchor (48,27)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (25,25)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (-25,25)
                    repeat
                with dspr
                mt "СТОЯТЬ!"
                "Ты бежишь дальше."
                scene bg ext_square_day
                with dissolve
                "Лишь выбежав на площадь, ты останавливаешься. Кажется, Ольга Дмитриевна тебя не преследует."
                
                $ ds_lp['us'] -= 1
                $ ds_karma -= 10
                $ ds_lp['mt'] -= 1
                "Ты идёшь умываться."
                jump ds_day4_washing
            else:
                window show
                svf "{result}Однако, ты утыкаешься прямо в Ольгу Дмитриевну."
                show mt angry pioneer close at center
                with dspr
                mt "А ну куда пошёл?!"
                
                $ ds_karma -= 5
                $ ds_lp['mt'] -= 1
                show mt angry pioneer at left
                with dspr
                mt "Ладно, дуйте умываться! У меня и без вас забот полон рот!"
    scene bg ext_library_day
    show us smile pioneer at center
    with dissolve
    play sound ds_sfx_psy
    vol "Между прочим, Ульяна спасла тебя от ужасной кары."
    play sound ds_sfx_psy
    aut "Ага, только она сама чуть не навлекла её на тебя."
    window hide
    menu:
        "Поблагодарить Ульяну":
            window show
            me "Спасибо..."
            show us surp2 pioneer at center
            with dspr
            us "За что?"
            me "За то, что прикрыла меня от обвинений..."
            show us laugh pioneer at center
            with dspr
            us "А, это да! Ну, в общем-то зачем мне было бы на тебя клеветать!"
            $ ds_lp['us'] += 1
        "Просто попрощаться":
            window show
    me "Ладно, я пойду!"
    us "Ага, до встречи!"
    hide us with dissolve
    "И она убегает. А ты идёшь умываться."
    jump ds_day4_washing

label ds_day4_morning_exercise:
    show mt normal pioneer at center
    with dissolve
    mt "Доброе утро, Семён!"
    th "Ольга Дмитриевна?"
    me "Доброе утро..."
    mt "Так, давай, поднимайся, зарядка!"
    play sound ds_sfx_mot
    res "Физрук всё же исполнил свою угрозу..."
    play sound ds_sfx_mot
    svf "И ты не сбежишь - ты даже не вылез из-под одеяла."
    window hide
    menu:
        "Пойти смирно":
            window show
            me "Идёмте..."
        "Спросить про умывание":
            window show
            me "А умыться?"
            mt "Нет времени, после зарядки умоешься!"
            me "Ладно..."
        "Отказаться" (skill='authority', level=lvl_unimaginable):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_psy
                aut "{result}Покажи ей всем своим видом, что никуда ты идти не собираешься."
                me "Отстаньте, никуда я не пойду! Мне нужно ещё поспать!"
                "Ты строишь максимально свирепое выражение лица."
                show mt shocked pioneer at center
                with dspr
                mt "Эм... ну ладно... так уж и быть..."
                hide mt with dissolve
                $ ds_lp['mt'] -= 2
                $ ds_karma -= 10
                
                th "Теперь можно ещё поспать."
                "Ты закрываешь глаза..."
                show blink
                scene black
                window hide
                $ renpy.pause(5.0)
                window show
                hide blink
                show unblink
                scene bg int_house_of_mt_day  with fade
                play sound ds_sfx_fys
                edr "Но твоё сознание уже переключилось в дневной режим – получается, пора вставать."
                vol "Стоит распланировать день – в конце концов, хоть сегодня необходимо что-то выяснить!"
                th "Надо окончательно проснуться, а заодно и заняться утренним туалетом."
                th "Отлично, сейчас быстро пойдём, умоемся и позавтракаем..."
                jump ds_day4_washing
            else:
                window show
                play sound ds_sfx_psy
                aut "{result}Маловато твёрдости. Ты слишком нерешительно говоришь."
                me "Извините, но я никуда не пойду..."
                show mt angry pioneer at center
                with dspr
                mt "Пойдёшь как миленький!"
                $ ds_karma -= 5
                
                me "Ясно, ну ладно..."
        "Притвориться больным" (skill='drama', level=lvl_challenging):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_int
                dra "{result}Вы хватаетесь за голову, старательно изображая боль в ней."
                me "Извините... никак не смогу... голова болит почему-то..."
                show mt surprise pioneer at center
                with dspr
                mt "Наверное, это из-за вчерашней дискотеки... ладно, полежи ещё, отдохни..."
                hide mt with dissolve
                
                th "Теперь можно ещё поспать."
                "Ты закрываешь глаза..."
                show blink
                scene black
                window hide
                $ renpy.pause(5.0)
                window show
                hide blink
                show unblink
                scene bg int_house_of_mt_day  with fade
                play sound ds_sfx_fys
                edr "Но твоё сознание уже переключилось в дневной режим – получается, пора вставать."
                vol "Стоит распланировать день – в конце концов, хоть сегодня необходимо что-то выяснить!"
                th "Надо окончательно проснуться, а заодно и заняться утренним туалетом."
                th "Отлично, сейчас быстро пойдём, умоемся и позавтракаем..."
                jump ds_day4_washing
            else:
                window show
                play sound ds_sfx_int
                dra "{result}Станиславский бы сказал: «не верю»."
                me "Ах, как у меня болит голова..."
                show mt angry pioneer at center
                with dspr
                dra "Ольга Дмитриевна тоже верить не собирается, мессир."
                mt "Так, притворяться не надо, вперёд!"
                $ ds_karma -= 10
                $ ds_lp['mt'] -= 1
                
                me "Ладно-ладно..."
        "Сбежать":
            window show
            "Ты пытаешься сбежать, но запутываешься в одеяле."
            play sound sfx_bodyfall_1
            with vpunch
            $ ds_health.damage()
            show mt surprise pioneer at center
            with dspr
            mt "Ты как, жив-здоров?"
            window hide
            menu:
                "Сказать честно":
                    window show
                    me "Да, просто упал..."
                    show mt normal pioneer at center
                    with dspr
                    mt "Вот и отлично, идём!"
                    me "Идём..."
                "Соврать" (skill='drama', level=lvl_up_medium):
                    if ds_last_skillcheck.result():
                        window show
                        play sound ds_sfx_int
                        dra "{result}Вы хватаетесь за ногу, старательно изображая боль в ней."
                        me "Кажется, я ногу ушиб... нет, сегодня зарядка без меня, завтра обязательно приду!"
                        show mt surprise pioneer at center
                        with dspr
                        mt "Так, полежи и отдохни, значит... если не пройдёт - к медсестре!"
                        hide mt with dissolve
                        th "Теперь можно ещё поспать."
                        "Ты закрываешь глаза..."
                        show blink
                        scene black
                        window hide
                        $ renpy.pause(5.0)
                        window show
                        hide blink
                        show unblink
                        scene bg int_house_of_mt_day  with fade
                        play sound ds_sfx_fys
                        edr "Но твоё сознание уже переключилось в дневной режим – получается, пора вставать."
                        vol "Стоит распланировать день – в конце концов, хоть сегодня необходимо что-то выяснить!"
                        th "Надо окончательно проснуться, а заодно и заняться утренним туалетом."
                        th "Отлично, сейчас быстро пойдём, умоемся и позавтракаем..."
                        jump ds_day4_washing
                    else:
                        window show
                        play sound ds_sfx_int
                        dra "{result}Станиславский бы сказал: «не верю»."
                        me "Ах, как у меня болит нога..."
                        show mt angry pioneer at center
                        with dspr
                        dra "Ольга Дмитриевна тоже верить не собирается, мессир."
                        mt "Не придуривайся! Я же вижу, что у тебя максимум синяк там! Идём!"
                        $ ds_karma -= 10
                        $ ds_lp['mt'] -= 1
                        me "Ладно-ладно..."
    scene bg ext_square_day
    show fz normal uniform at center
    with dissolve
    "Весь лагерь уже собрался на площади и выстроился в четыре ряда. Физрук стоит в центре."
    fzp "Так, опаздывающие на месте, начинаем!"
    show fz serious uniform at center
    with dspr
    fzp "Десять отжиманий! Всем!"
    window hide
    menu:
        "Cделать честно" (skill='endurance', level=lvl_up_medium):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_fys
                edr "{result}Впрочем, для тебя сделать десять отжиманий оказывается легче лёгкого."
                "Ты быстро делаешь отжимания и вскакиваешь."
                fzp "Так, раз так быстро справился - ещё десять отжиманий!"
                th "Да он издевается?"
            else:
                window show
                play sound ds_sfx_fys
                edr "{result}После пары отжиманий ты падаешь на землю."
                show fz angry uniform at center
                with dspr
                fzp "Так, давай, слабак, вставай и делай нормально!"
                $ ds_morale.damage()
            
        "Сфилонить":
            window show
            "Ты становишься на руки и изображаешь, будто старательно отжимаешься, на самом деле лишь немного сгибая конечности."
            "Однако, эта гора мышц всё видит."
            show fz rage uniform at center
            with dissolve
            fzp "Так, это что за отжимания такие? Будешь делать двадцать раз сверху! Не вздумай меня обманывать!"
    window hide
    menu:
        "Принять":
            window show
            th "Ладно, чего уж там, сделаем..."
            "Ты пытаешься исполнить указание физрука, но безуспешно - уже вымотался."
            play sound ds_sfx_psy
            vol "Нужно, однако, заметить, что с указаниями этого мистера Мускула не может справиться никто. Так что ты ещё неплох!"
        "Прикинуться шлангом":
            window show
            "Ты старательно изображаешь, что физрук обращается не к тебе."
            "Однако, он обращается именно что к тебе."
            show fz rage uniform at center
            with dspr
            fzp "Так, я с кем разговариваю! Вышел из строя!"
            window hide
            menu:
                "Выйти из строя":
                    window show
                    "Ты выходишь."
                    fzp "Тридцать отжиманий! Выполнять!"
                    "Ты послушно склоняешься и начинаешь делать."
                    "И при этом видишь, что решительно все пионеры уже выбились из сил."
                "Остаться стоять":
                    window show
                    "Ты остаёшься стоять на месте."
                    fzp "Ты издеваешься надо мной?! Вы все издеваетесь надо мной?!"
                    "Тут он замечает, что, в общем-то, успехов на ниве физической культуры не наблюдается ни у кого."
        "Начать протестовать":
            window show
            me "Вы издеваетесь? Посмотрите, ни у кого не выходит ничего!"
            play sound ds_sfx_mot
            per_eye "Что чистая правда - все пионеры уже выбились из сил и отжимаются на последнем издыхании."
            show fz smile uniform at center
            with dspr
            fzp "Да? А вспомни, благодаря кому все тут занимаются?"
            play sound ds_sfx_int
            rhe "Ты же сам вчера потребовал зарядки утренней..."
            play sound ds_sfx_psy
            emp "Впрочем, все настолько вымотались, что им уже безразлично, что этот мужик говорит."
            play sound ds_sfx_psy
            aut "Так что и травли не будет... наверное."
    show fz angry uniform at center
    with dspr
    fzp "Какие же вы слабаки! Не могу смотреть на этот позор советского народа!"
    fzp "Всё, пусть проводит зарядку кто-нибудь другой! Желающие!"
    show sl normal sport at left
    with dissolve
    "Желающий лишь один. Предсказуемо, им оказывается Славя."
    sl "Я проведу зарядку, товарищ физический руководитель!"
    show fz normal uniform at center
    with dspr
    fzp "Отлично, я пошёл!"
    show mt scared pioneer at right
    with dissolve
    "Однако, прежде чем он успевает уйти, а Славя - объявить первое упражнение, появляется перепуганная Ольга Дмитриевна."
    mt "Так, извините, Борис Александрович, что прерываю зарядку, но у нас тут возникли неотложные обстоятельства."
    mt "Все бегом к столовой!"
    hide mt with dissolve
    play sound ds_sfx_mot
    per_eye "Только сейчас ты обращаешь внимание, что на зарядке не было ни Электроника, ни Шурика."
    show fz serious uniform at center
    with dspr
    fzp "Вы слышали приказ? Зарядка окончена, шагом марш к столовой!"
    "Все идут в сторону столовой, при этом перешёптываясь о том, что же могло случиться."
    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_away_day 
    with dissolve

    play sound_loop ambience_medium_crowd_outdoors fadein 2

    window show
    "У столовой собирается столько народу, сколько его не было никогда."
    play sound ds_sfx_int
    lgc "Хотя и был-то ты тут лишь три дня..."
    "Ты подходишь поближе в надежде узнать, что происходит."
    window hide

    jump ds_day4_sh_lost

label ds_day4_sl_workout:
    show sl normal sport at center
    with dissolve
    sl "Доброе утро, Семён! Ну что, снова тренировка?"
    me "Доброе утро..."
    window hide
    menu:
        "Пойти":
            window show
            me "Идём, только я соберусь сейчас!"
            show sl smile sport at center with dspr
            sl "Отлично!"
            $ ds_lp['sl'] += 1
        "Отказаться":
            window show
            me "Знаешь, я передумал... не хочется что-то, да и лень..."
            show sl sad sport at center with dspr
            sl "Вот как... ну ладно... до встречи тогда."
            hide sl with dissolve
            "Она выходит."
            $ ds_lp['sl'] -= 1
            th "Так, теперь пойдём умоемся - и на завтрак!"
            jump ds_day4_washing
        "Притвориться, что не можешь" (skill='drama', level=lvl_challenging):
            if ds_last_skillcheck.result():
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
                th "Так, теперь пойдём умоемся - и на завтрак!"
                jump ds_day4_washing
            else:
                window show
                dra "{result}Вы и пытаетесь изобразить, что у вас что-то болит, мессир, но ничего внятного не получается."
                me "Ах... у меня всё болит..."
                show sl angry sport at center with dspr
                sl "Врать нехорошо, Семён! Сказал бы, что просто не хочешь!"
                sl "А так делать нехорошо... да и вообще, зачем тогда сам предлагал?!"
                sl "Ладно, я пойду! Удачного дня!"
                $ ds_lp['sl'] -= 2
                th "Так, теперь пойдём умоемся - и на завтрак!"
                jump ds_day4_washing
    scene bg ext_house_of_mt_day
    show sl normal sport at center
    with dspr
    "Быстро надев на себя спортивную форму, ты выходишь."
    sl "Сегодня мы с тобой пробежимся до спортплощадки, а потом сделаем зарядку!"
    window hide
    menu:
        "Согласиться":
            window show
            me "Как скажешь!"
            show sl smile sport at center
            with dspr
            sl "Вот и хорошо!"
        "Отказаться":
            window show
            me "Ну нет, давай как вчера - пробежку просто..."
            show sl smile sport at center
            with dspr
            sl "Ну давай, как скажешь. Но побежим сегодня по большому кругу."
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
    scene bg ext_dining_hall_away_day:
        zoom 1.05 anchor (48,27)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (25,25)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (-25,25)
        repeat
    show sl normal sport at center
    with dissolve
    $ renpy.pause(3.0, hard=True)
    scene bg ds_ext_storage_day:
        zoom 1.05 anchor (48,27)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (25,25)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (-25,25)
        repeat
    show sl normal sport at center
    with dissolve
    window show
    play sound ds_sfx_mot
    per_eye "Ты примечаешь толпу пионеров возле столовой."
    "Но Славя бежит дальше. Ты тоже пока что не останавливаешься."
    window hide
    $ renpy.pause(3.0, hard=True)
    scene bg ext_playground_day:
        zoom 1.05 anchor (48,27)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (25,25)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (-25,25)
        repeat
    show sl normal sport at center
    with dissolve
    $ renpy.pause(1.0)
    show mt scared pioneer at right
    with dissolve
    mt "Ой, Славя и Семён, вы тут спортом занимаетесь?"
    "Вы с ней останавливаетесь."
    scene bg ext_playground_day
    show sl surprise sport at left
    show mt scared pioneer at right
    with dspr
    stop music fadeout 3
    sl "Да, Ольга Дмитриевна, что-то случилось?"
    mt "Да, случилось! Все срочно к столовой!"
    hide mt with dissolve
    sl "Ну чего, побежали?"
    play sound ds_sfx_fys
    edr "Тебе в любом случае не лишним будет позавтракать. Пробежка тебя вымотала."
    me "Ага..."
    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_away_day 
    with dissolve

    play sound_loop ambience_medium_crowd_outdoors fadein 2

    window show
    "Вы подбегаете к столовой, где, как ты видел ранее, очень много народа."
    "Ты подходишь поближе в надежде узнать, что происходит."
    window hide

    jump ds_day4_sh_lost

label ds_day4_sh_lost:
    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_near_day 
    with dissolve

    window show
    "На пороге, кажется, собрался весь лагерь: и все знакомые тебе девочки, и Ольга Дмитриевна, и Электроник."
    "Они что-то оживлённо обсуждают."
    "Ты подходишь поближе."
    show mt normal pioneer at right 
    show el normal pioneer at left 
    with dissolve

    stop sound_loop fadeout 2

    stop ambience fadeout 2

    play music music_list["silhouette_in_sunset"] fadein 3

    if (ds_day3_evening_who == 'us') and not ds_caught_in_lib:
        show mt angry pioneer at right   with dspr
        mt "И где же ты был?!{w} Я тебя всю ночь ждала! И ищу с самого раннего утра!{w} Ульяна сказала, что вы вчера вечером вместе уходили из библиотеки."
        show us surp1 pioneer at center   with dissolve
        "Я посмотрел на Ульянку.{w} Она ехидно улыбается."
        window hide
        menu:
            "Начать оправдываться":
                window show
                me "И ничего..."
                "Но Ольга Дмитриевна и не собирается тебя слушать."
            "Промолчать":
                window show
        mt "Ладно, с этим позже разберёмся!"
        hide us  with dissolve
        show mt normal pioneer at right   with dspr
    mt "Ты не видел сегодня Шурика?"
    me "Нет, а что такое?"
    mt "Мы его с утра не можем найти!"
    play sound ds_sfx_fys
    hfl "Исчезновение пионеров – это что-то новенькое."
    mt "Но вчера же он был с тобой?"
    play sound ds_sfx_int
    rhe "Она обращается к Электронику."
    el "Был…"
    mt "А утром ты проснулся, а его нет?"
    el "Нет…"
    mt "И почему ты сразу не пошёл ко мне?"
    show el upset pioneer at left   with dspr
    el "Ну, я подумал, что, может, он раньше проснулся и умываться пошёл или ещё куда…"
    show sl normal pioneer at center   with dissolve
    sl "А он вчера ничего такого не говорил?"
    el "Например?"
    sl "Что собирается куда-то, например?"
    el "Нет…"
    if (ds_after_lunch_who == 'el') or (ds_day3_evening_who == 'el'):
        play sound ds_sfx_int
        enc "Шурик говорил, что он собирается в старый лагерь..."
        play sound ds_sfx_psy
        sug "Наверное, об этом следует сказать."
    window hide
    menu:
        "Сказать про старый лагерь" if (ds_after_lunch_who == 'el') or (ds_day3_evening_who == 'el'):
            window show
            me "Кажется, Электроник немного позабыл. Вчера Шурик говорил, что он пойдёт в старый лагерь за деталями."
            show el smile pioneer at left
            with dspr
            el "Да, точно, вспомнил!"
            show mt shocked pioneer at right
            with dspr
            mt "Точно? Может, он всё-таки просто погулять пошёл?"
            $ ds_karma += 20
            $ ds_have_guess_sh = True
        "Выдвинуть «обоснованные» предположения" (skill='logic', level=lvl_medium):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_int
                lgc "{result}Шурик же кибернетик. Вероятно, он пошёл искать то ли литературу, то ли детали."
                lgc "Но в библиотеке он вряд ли - иначе Женя уже сказала бы. Значит, он ищет детали."
                me "А где, теоретически, могут быть радиодетали?"
                show mt surprise pioneer at right
                with dspr
                mt "Ты о чём?"
                sl "Ну, либо склад... либо ещё какое подсобное помещение."
                mt "Значит, надо будет посмотреть все склады в лагере! Может быть, Шурик поранился или был придавлен!"
                el "Или старый лагерь! Да, он говорил об этом!"
                $ ds_have_guess_sh = True
            else:
                window show
                play sound ds_sfx_int
                lgc "{result}Да сто процентов гулять пошёл просто и скоро вернётся!"
                me "Я думаю, он просто загулялся и скоро сам придёт."
        "Вслушаться в окружающую среду" (skill='shivers', level=lvl_legendary):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_fys
                shi "{result}До тебя доходят тонкие вибрации. Где-то к югу от лагеря есть старое здание. Оттуда веет древностью и разрухой. Там раздаётся скрип - кто-то бродит там."
                shi "Затем раздаётся хруст и удар. Кто-то упал. И ударился, больно."
                me "У меня есть предчувствие, что Шурик забрёл куда-то и упал."
                show mt scared pioneer at right
                show el scared pioneer at left
                show sl scared pioneer at center
                with dspr
                mt "С чего ты взял, Семён?!"
                el "Cтоп, ведь Шурик что-то говорил про старый лагерь..."
                $ ds_karma += 10
                $ ds_have_guess_sh = True
            else:
                window show
                play sound ds_sfx_fys
                shi "{result}Как ты ни пытаешься - не даёт тебе природа ответа."
            
        "Спросить, что такого":
            window show
            me "А что такого страшного-то произошло?{w} Время только девять утра. Может, он прогуляться решил."
            show sl serious pioneer at center   with dspr
            sl "Ты не знаешь Шурика."
            "Она серьёзно смотрит на тебя."
            me "Не знаю, да…"
            hfl "Но в то же время ничего подозрительного в этой ситуации ты не видишь."
        "Промолчать":
            window show
    mt "Ладно, не будем паниковать. Наверняка найдётся!"
    show us grin pioneer at right   with dissolve:
        xpos 1.2
        linear 0.5 xpos 0.65
    us "Чтобы он пропустил завтрак…"
    "Усмехнулась Ульянка."
    show dv normal pioneer at left   with dissolve:
        xpos -0.2
        linear 0.5 xpos -0.1
    dv "Точно! Пора уже и есть идти."
    hide us 
    hide dv 
    hide sl 
    hide el 
    if day3_us_evening != 1:
        hide mt 
    with dissolve

    "Пионеры зашли в столовую."

    if (ds_day3_evening_who == 'us') and not ds_caught_in_lib:
        show mt normal pioneer at right   with dspr
        "А тебя останавливает Ольга Дмитриевна."
        mt "Семён, а ты постой-ка."
        me "Да?"
        show mt angry pioneer at right   with dspr:
            linear 1.0 xalign 0.5
        mt "Изволишь объясниться, где ты был ночью?"
        me "Ну…"
        play sound ds_sfx_psy
        vol "Вот об этом ты как-то не подумал…"
        play sound ds_sfx_psy
        sug "Действительно, подобное не могло остаться незамеченным, и мне стоило бы придумать годное объяснение."
        vol "Но ты не придумал…"
        window hide
        menu:
            "Начать оправдываться":
                window show
                me "А я…{w} А мы с Ульяной в библиотеке книги расставляли, а потом она убежала и меня закрыла! И я сидел там до утра!"
                mt "Я была сегодня в библиотеке!{w} А вот тебя там не видела."
                play sound ds_sfx_int
                lgc "Да ты в курсе."
                me "Ну…{w} Я незаметно ушёл."
                mt "А почему Ульяна говорит совсем другое?"
                play sound ds_sfx_int
                rhe "И что же, интересно, она говорит?"
                me "Вы же её знаете!"
                if ds_karma >= 50:
                    show mt normal pioneer at center
                    with dspr
                    mt "Ну ладно, тут ты прав, пожалуй..."
                    mt "Ладно, иди."
                elif ds_karma <= -50:
                    show mt angry pioneer at center
                    with dspr
                    mt "Я знаю тебя! Ты постоянно что-нибудь нарушаешь!"
                    mt "В общем, поговорим позже - сейчас надо найти Шурика!"
                    mt "А сейчас иди!"
                else:
                    show mt normal pioneer at center   with dspr
                    mt "Да, пожалуй…"
                    show mt angry pioneer at center   with dspr
                    mt "Но ты не думай, что я тебе поверю!"
                    th "Я и не думал…"
                    show mt normal pioneer at center   with dspr
                    mt "Разберёмся с этим позже, я не забуду!{w} А сейчас есть дела поважнее – найти Шурика."
                    me "Да…"
                    mt "Иди уж…"
            "Прошмыгнуть в столовую" (skill='savoir_faire', level=lvl_formidable):
                if ds_last_skillcheck.result():
                    window show
                    play sound ds_sfx_mot
                    svf "{result}Ты быстрыми резкими движениями пробегаешь мимо Ольги Дмитриевны, и прежде чем она успеет отреагировать, ты оказываешься в столовой."
                    
                else:
                    window show
                    play sound ds_sfx_mot
                    svf "{result}Однако, ты врезаешься прямо в Ольгу Дмитриевну и опрокидываешь её."
                    show mt rage pioneer at center
                    with dspr
                    "Ольга Дмитриевна поднимается очень злая на тебя."
                    $ ds_lp['mt'] -= 1
                    $ ds_karma -= 10
                    
                    mt "КУДА СОБРАЛСЯ?! Мы ещё не договорили!"
                    me "Ну... не договорили..."
                    mt "Короче, с тобой мы разберёмся потом! А сейчас нужно искать Шурика!"
                    show mt angry pioneer at center
                    with dspr
                    mt "Иди в столовую!"
            "Извиниться":
                window show
                me "Извините..."
                mt "Ты думаешь, что отделаешься одними извинениями?!"
                mt "Ты будешь... будешь..."
                play sound ds_sfx_int
                rhe "Похоже, у неё нет идей для наказания."
                mt "Так, когда найдём Шурика - тогда придумаю тебе наказание!"
                mt "А сейчас свободен!"
            "Стоять молча" (skill='composure', level=lvl_heroic):
                if ds_last_skillcheck.result():
                    window show
                    play sound ds_sfx_mot
                    com "{result}Ты стоишь с невозмутимым лицом, пока Ольга Дмитриевна возмущается."
                    show mt rage pioneer at center
                    with dspr
                    mt "Ну и чего, будем в молчанку играть?!"
                    "Ты продолжаешь молчать."
                    mt "Так, короче, потом с тобой разберёмся! Шурика искать надо!"
                    mt "Иди отсюда!"
                    "И ты довольный уходишь."
                    th "Отлично!"
                    
                else:
                    window show
                    play sound ds_sfx_mot
                    com "{result}Однако, ты слишком нервничаешь, и Ольга Дмитриевна это видит."
                    mt "Я же вижу, как ты боишься чего-то! Давай говори, что натворил!"
                    me "Не было ничего..."
                    mt "Ладно, потом поговорим! Надо Шурика искать!"
                    mt "Иди отсюда!"
        hide mt  with dissolve
    stop music fadeout 3

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_people_day 
    with dissolve

    play ambience ambience_dining_hall_full fadein 3

    window show
    "Выбрать, куда приткнуться, не вышло – единственные свободные места за столом Алисы и Ульяны."
    show us laugh pioneer at cright, ds_seated 
    show dv normal pioneer at cleft, ds_seated 
    with dissolve
    us "Садись."
    "Она показывает на стул рядом с собой."
    "Ты садишься."
    if ds_dumped_dv:
        play sound ds_sfx_psy
        emp "Алиса выглядит как обычно и, похоже, не собирается устраивать тебе разнос за то, что ты обещал вчера вечером прийти на сцену, но не пришёл."
        play sound ds_sfx_psy
        vol "Если она об этом не говорит - тебе поднимать эту тему уж точно не следует."
        window hide
        menu:
            "Заговорить с Алисой":
                window show
                me "Слушай... я вчера не пришёл..."
                show dv angry pioneer at cleft
                with dspr
                dv "Лучше молчи..."
                window hide
                menu:
                    "Отступить":
                        window show
                    "Извиниться":
                        window show
                        me "Извини, пожалуйста..."
                        dv "Прощаю я тебя! А теперь отстань!"
                        window hide
                        menu:
                            "Отстать":
                                window show
                            "Продолжать приставать":
                                window show
                                me "Ну послушай, я правда не хотел тебя обидеть..."
                                show dv rage pioneer at cright
                                with dspr
                                dv "Я кому сказала отвять?! Ты вообще человеческого языка не понимаешь?!"
                                $ ds_lp['dv'] -= 2
                                hide dv with dissolve
                                "И Алиса выбегает из столовой, хлопнув дверью."
                                $ ds_dv_breakfast_absent
                    "Сказать про помощь Лене" if ds_to_help_un and not ds_dumped_un:
                        window show
                        me "Просто понимаешь... мне надо было помочь Лене с..."
                        show dv rage pioneer at cleft, ds_get_up_fast
                        dv "И как, классно вы время провели?!"
                        "Алиса аж вскочила со стула от гнева."
                        emp "Определённо, её стриггерило именно упоминание Лены в подобном контексте."
                        me "Да мы просто..."
                        dv "Что «просто»? Обнимались?! Целовались?! Трахались?!"
                        mt "Двачевская, не матерись!"
                        dv "Одно и то же ВСЕГДА! Да пошли вы все!"
                        hide dv with dissolve
                        "И Алиса, хлопнув дверью, выходит из столовой."
                        $ ds_lp['dv'] -= 5
                        $ ds_dv_breakfast_absent = True
                        $ ds_triggered_dv = True
                        show us sad pioneer at cright
                        with dspr
                        us "Ну ты и кашу заварил, Семён..."
                        window hide
                        menu:
                            "Спросить":
                                window show
                                me "Ты о чём?"
                                us "Ну... Лену упоминать было лишним..."
                                show us fear pioneer at cright
                                with dspr
                                us "Ой... я тебе ничего не говорила, если что!"
                                me "Может, скажешь?"
                                if ds_lp['us'] > 0:
                                    show us smile pioneer at cright
                                    with dspr
                                    us "Ладно! Но проболтаешься - получишь жуков себе в подушку!"
                                    show us sad pioneer at cright
                                    with dspr
                                    us "Хоть Лена и подружка Алисы, но Алиса, типа... завидует ей."
                                    us "Думает, что Лена отбирает у неё внимание. Потому Алиска и такая бука!"
                                    me "Вот как..."
                                    us "А после того, что ты наговорил... даже у меня нет идей, как помочь."
                                else:
                                    us "Не скажу! Буду как партизан молчать!"
                                    play sound ds_sfx_psy
                                    sug "Она совершенно точно ничего не скажет."
                                    me "Да я и не буду тебя пытать..."
                            "Проигнорировать":
                                window show
                    "Сказать про помощь медсестре" if ds_to_help_un and not ds_dumped_un:
                        window show
                        me "Просто понимаешь... меня внезапно впрягли помогать медсестре..."
                        dv "Что ж, сочувствую тебе!"
                        dv "А ещё запомню, что ты настолько бесхребетный, что не можешь отказать - причём, даже не вожатой! - имея планы с девушкой!"
                        dv "Думаю, ты отлично и без меня развлечёшься!"
                        $ ds_lp['dv'] -= 2
                    "Сказать про танцы":
                        window show
                        me "Ну... дискотека же... обязательная... и там классно было!"
                        dv "Я рада, что ты повеселился!"
                        if ds_skill_list['empathy'].check(lvl_easy, passive=True).result():
                            play sound ds_sfx_psy
                            emp "{result}Она очень зла, что ты предпочёл дискотеку ей. И, в общем-то, оправданно."
                        dv "А теперь дай мне поесть!"
                        $ ds_lp['dv'] -= 3
                    "Сказать, что не захотел":
                        window show
                        me "Ну не захотел и не пришёл!"
                        dv "Надеюсь, ты классно провёл время... Дальше тоже без меня!"
                        $ ds_lp['dv'] -= 3
            "Промолчать":
                window show
                th "Ну, раз она не хочет об этом говорить, то и мне не стоит."
    us "Может, всё же возьмешь еду?"
    th "Точно!{w} Об этом я и не подумал как-то…"
    "Завтрак, вроде бы такой же, как вчера, сегодня как будто выглядит аппетитнее."
    play sound ds_sfx_fys
    edr "Может быть, просто очень хочется есть."
    play sound ds_sfx_fys
    hfl "А может, я пытался побыстрее покончить с ним, чтобы не нарваться на очередную Ульянкину выходку."
    us "Пойдёшь сегодня с нами на пляж?"
    me "Когда?"
    us "После завтрака."
    if ds_dv_breakfast_absent:
        us "Заодно Алиска отойдёт, и ты можешь попробовать извиниться! Наверное."
    vol "Вообще говоря, развлечения сегодня не входят в твои планы, но в то же время отчего бы час-два не поваляться на солнышке и подумать?"
    window hide
    menu:
        "Принять":
            window show
            me "Пойду, почему нет…"
            show us laugh2 pioneer at cright
            with dspr
            us "Вот и отлично!"
            "Она мило улыбается."
        "Отвергнуть":
            window show
            me "Нет, я как-то не планировал..."
            show us dontlike pioneer at cright
            with dspr
            us "Да чего ты? Пойдём, отдохнёшь..."
            $ ds_d4_us_accept = False
        "Ответить неопределённо":
            window show
            me "Можно мне подумать?"
            show us laugh2 pioneer at cright
            with dspr
            us "Нет, нельзя! Твоё решение нужно сейчас!"
    if ds_skill_list['half_light'].check(lvl_trivial, passive=True).result():
        play sound ds_sfx_fys
        hfl "{result}Внимание! Похоже, Ульяна что-то задумала!"
        window hide
        menu:
            "Спросить":
                window show
                me "Опять небось что-нибудь замышляешь?"
                show us surp2 pioneer at cright   with dspr
                us "Нет, ты что!"
                "Ульяна замахала руками."
                if not ds_dv_breakfast_absent:
                    show dv smile pioneer at cleft   with dspr
                    dv "Наверняка!"
                    "Ухмыляется Алиса."
                    dv "Она такая!"
                    show us surp3 pioneer at cright   with dspr
                    us "А вот и нет!"
                    me "Я склонен с ней согласиться."
                    show us grin pioneer at cright   with dspr
                    us "Да никто и не сомневался!"
            "Отбросить страхи":
                window show

    if ds_day3_dv_conflict:
        play sound ds_sfx_psy
        ine "Ты внимательно смотришь на Алису и тут же вспоминаешь вчерашний вечер."
        ine "Её странное поведение, вашу ссору."
        ine "Но сейчас она кажется такой же, как и всегда."
        th "Может, и не стоит тогда ничего говорить?"
        play sound ds_sfx_psy
        vol "Хотя ты и не собирался."
        ine "В конце концов, за ночь произошедшее перестало казаться чем-то действительно необычным, как будто тебе всё это приснилось."
    show us smile pioneer at cright, ds_get_up
    "Ульянка берёт поднос с грязной посудой и встаёт."
    us "Приятного аппетита!"
    hide us  with dissolve
    play sound ds_sfx_fys
    hfl "Она сказала это так, что ты полностью уверился в том, что ничего хорошего сегодня на пляже тебя не ждёт."
    if ds_dv_breakfast_absent:
        stop ambience fadeout 2
        jump ds_day4_after_breakfast_reject
    show dv normal pioneer at cleft   with dspr:
        linear 0.5 xalign 0.5
    "Вы остаётесь наедине с Алисой."
    window hide
    menu:
        "Передумать идти" if ds_d4_us_accept:
            window show
            me "Знаешь, я всё же, наверное, с вами не пойду."
            show dv normal pioneer at center   with dspr
            dv "А что так?"
            window hide
            menu:
                "Cказать, что есть дела":
                    window show
                    me "Ну, дела кое-какие…"
                    show dv surprise pioneer at center   with dspr
                    dv "И что же у тебя за дела?"
                    if not ds_skill_list['composure'].check(lvl_challenging, passive=True).result():
                        play sound ds_sfx_mot
                        com "{result}Она заглядывает тебе в глаза так, что ты даже не знаешь, что соврать."
                    play sound ds_sfx_int
                    rhe "Лучше зайди с той стороны, что нет плавок. Это и правдиво - и надёжно."
                "Сказать, что нет плавок":
                    window show
                "Отказаться отвечать":
                    window show
                    me "Просто не хочу! Отстань."
                    show dv normal pioneer at center
                    with dspr
                    dv "Ну, как скажешь - мне вообще без разницы, придёшь ты, не придёшь."
                    dv "Бывай!"
                    $ ds_lp['dv'] -= 1
                    hide dv with dissolve
                    stop ambience fadeout 2
                    jump ds_day4_after_breakfast_reject
            me "Ну, у меня и плавок даже нет…"
            show dv normal pioneer at center   with dspr
            dv "Надень мои."
            if ds_skill_list['instinct'].check(lvl_easy, passive=True).result():
                play sound ds_sfx_fys
                ins "{result}Это намёк! Очень прозрачный намёк!"
                play sound ds_sfx_psy
                aut "Ага, скорее уж попытка высмеять тебя - мужик в женских плавках!"
                play sound ds_sfx_fys
                pat "Ещё и сжимать твои причиндалы будет..."
                th "А откуда такие сведения?!"
                aut "Раз не знаешь - то оно и к лучшему. Меньше знаешь - крепче спишь!"
            play sound ds_sfx_psy
            vol "Идея плохая, в общем. Не поймут."
            me "Думаешь, они на меня налезут?"
            show dv grin pioneer at center   with dspr
            dv "А ты попробуй!"
            window hide
            menu:
                "Cогласиться":
                    window show
                    me "А давай!"
                    show dv surprise pioneer at center
                    with dspr
                    "Cначала Алиса не поняла тебя..."
                    show dv angry pioneer at center
                    with dspr
                    "...а потом как поняла!"
                    dv "Ты там вообще что ли?! Всерьёз поверил, что будешь мои плавки носить?!"
                    $ ds_lp['dv'] -= 1
                    $ ds_morale.damage()
                    play sound ds_sfx_psy
                    sug "Неудобно вышло..."
                    show dv laugh pioneer at center
                    with dspr
                    dv "Но ты не расстраивайся - найдём мы тебе плавки!"
                "Отвергнуть":
                    me "Наверное, не стоит…"
                    show dv smile pioneer at center   with dspr
                    dv "Да ты не бойся!{w} Найдём мы тебе плавки!"
        "Всё-таки пойти" if ds_d4_us_accept:
            window show
            me "Я всё-таки подумал и решил, что пойду с вами."
            dv "Вот как?"
            show dv grin pioneer at center
            with dspr
            dv "А можно нескромный вопрос - а в чём ты пойдёшь?"
            play sound ds_sfx_int
            rhe "Она к тому, что не в пионерской форме же на пляже сидеть."
            play sound ds_sfx_psy
            vol "Что правда - тебе явно нужна одежда более пригодная для плавания. То бишь плавки."
            window hide
            menu:
                "Ответить, что пойдёшь так":
                    window show
                    me "Да прямо так и пойду, что такого?"
                    show dv laugh pioneer at center
                    with dspr
                    dv "Что такого? А плавать в этом ты как собираешься?"
                "Сказать про отсутствие плавок":
                    window show
                    me "Ну... да, у меня нет плавок..."
                    show dv normal pioneer at center   with dspr
                    dv "Надень мои."
                    if ds_skill_list['instinct'].check(lvl_easy, passive=True).result():
                        play sound ds_sfx_fys
                        ins "{result}Это намёк! Очень прозрачный намёк!"
                        play sound ds_sfx_psy
                        aut "Ага, скорее уж попытка высмеять тебя - мужик в женских плавках!"
                        play sound ds_sfx_fys
                        pat "Ещё и сжимать твои причиндалы будет..."
                        th "А откуда такие сведения?!"
                        aut "Раз не знаешь - то оно и к лучшему. Меньше знаешь - крепче спишь!"
                    play sound ds_sfx_psy
                    vol "Идея плохая, в общем. Не поймут."
                    me "Думаешь, они на меня налезут?"
                    show dv grin pioneer at center   with dspr
                    dv "А ты попробуй!"
                    window hide
                    menu:
                        "Cогласиться":
                            window show
                            me "А давай!"
                            show dv surprise pioneer at center
                            with dspr
                            "Cначала Алиса не поняла тебя..."
                            show dv angry pioneer at center
                            with dspr
                            "...а потом как поняла!"
                            dv "Ты там вообще что ли?! Всерьёз поверил, что будешь мои плавки носить?!"
                            $ ds_lp['dv'] -= 1
                            $ ds_morale.damage()
                            play sound ds_sfx_psy
                            sug "Неудобно вышло..."
                            show dv laugh pioneer at center
                            with dspr
                        "Отвергнуть":
                            me "Наверное, не стоит…"
                            show dv smile pioneer at center   with dspr
            show dv smile pioneer at center
            with dspr
            dv "Короче, горемычный ты наш сиротинушка. Сейчас найдём тебе плавки."
        "Подтвердить планы" if ds_d4_us_accept:
            window show
            me "Да, я всё-таки пойду с вами."
            show dv grin pioneer at center
            with dspr
            dv "А можно нескромный вопрос - а в чём ты пойдёшь?"
            play sound ds_sfx_int
            rhe "Она к тому, что не в пионерской форме же на пляже сидеть."
            play sound ds_sfx_psy
            vol "Что правда - тебе явно нужна одежда более пригодная для плавания. То бишь плавки."
            window hide
            menu:
                "Ответить, что пойдёшь так":
                    window show
                    me "Да прямо так и пойду, что такого?"
                    show dv laugh pioneer at center
                    with dspr
                    dv "Что такого? А плавать в этом ты как собираешься?"
                "Сказать про отсутствие плавок":
                    window show
                    me "Ну... да, у меня нет плавок..."
                    show dv normal pioneer at center   with dspr
                    dv "Надень мои."
                    if ds_skill_list['instinct'].check(lvl_easy, passive=True).result():
                        play sound ds_sfx_fys
                        ins "{result}Это намёк! Очень прозрачный намёк!"
                        play sound ds_sfx_psy
                        aut "Ага, скорее уж попытка высмеять тебя - мужик в женских плавках!"
                        play sound ds_sfx_fys
                        pat "Ещё и сжимать твои причиндалы будет..."
                        th "А откуда такие сведения?!"
                        aut "Раз не знаешь - то оно и к лучшему. Меньше знаешь - крепче спишь!"
                    play sound ds_sfx_psy
                    vol "Идея плохая, в общем. Не поймут."
                    me "Думаешь, они на меня налезут?"
                    show dv grin pioneer at center   with dspr
                    dv "А ты попробуй!"
                    window hide
                    menu:
                        "Cогласиться":
                            window show
                            me "А давай!"
                            show dv surprise pioneer at center
                            with dspr
                            "Cначала Алиса не поняла тебя..."
                            show dv angry pioneer at center
                            with dspr
                            "...а потом как поняла!"
                            dv "Ты там вообще что ли?! Всерьёз поверил, что будешь мои плавки носить?!"
                            $ ds_lp['dv'] -= 1
                            $ ds_morale.damage()
                            play sound ds_sfx_psy
                            sug "Неудобно вышло..."
                            show dv laugh pioneer at center
                            with dspr
                        "Отвергнуть":
                            me "Наверное, не стоит…"
                            show dv smile pioneer at center   with dspr
            show dv smile pioneer at center
            with dspr
            dv "Короче, горемычный ты наш сиротинушка. Сейчас найдём тебе плавки."
        "Подтвердить планы" if not ds_d4_us_accept:
            window show
            me "Знаешь, я всё же, наверное, с вами не пойду."
            show dv normal pioneer at center   with dspr
            dv "А что так?"
            window hide
            menu:
                "Cказать, что есть дела":
                    window show
                    me "Ну, дела кое-какие…"
                    show dv surprise pioneer at center   with dspr
                    dv "И что же у тебя за дела?"
                    if not ds_skill_list['composure'].check(lvl_challenging, passive=True).result():
                        play sound ds_sfx_mot
                        com "{result}Она заглядывает тебе в глаза так, что ты даже не знаешь, что соврать."
                    play sound ds_sfx_int
                    rhe "Лучше зайди с той стороны, что нет плавок. Это и правдиво - и надёжно."
                    play sound ds_sfx_int
                    dra "Нет, куда лучше звучат секретные поручения вожатой!"
                    window hide
                    menu:
                        "Cказать, что нет плавок":
                            window show
                        "Соврать про поручения":
                            window show
                            me "Поручения от вожатой. Очень секретные."
                            dv "Да брось ты!"
                            me "Нет, я никуда не пойду."
                            show dv surprise pioneer at center  with dspr
                            play sound ds_sfx_psy
                            aut "Кажется, Алиса такого резкого ответа не ожидала."
                            show dv smile pioneer at center  with dspr
                            dv "Ты что, сдрейфил, пионер? Пляжей боишься?"
                            show dv laugh pioneer at center  with dspr
                            "Алисе так понравилась её собственная колкость, что она звонко смеётся."
                            play sound ds_sfx_fys
                            hfl "Наверняка, дальше будет только хуже."
                            play sound ds_sfx_psy
                            vol "Но не можешь же ты открыто послать её на три буквы?"
                            aut "Или можешь?"
                            window hide
                            menu:
                                "Остаться":
                                    window show
                                "Уйти":
                                    window show
                                    "Ты молча встаёшь из-за стола, уносишь поднос и, не оборачиваясь, покидаешь столовую."
                                    hide dv with dissolve
                                    window hide               

                                    jump ds_day4_after_breakfast_reject
                "Сказать, что нет плавок":
                    window show
                "Отказаться отвечать":
                    window show
                    me "Просто не хочу! Отстань."
                    show dv normal pioneer at center
                    with dspr
                    dv "Ну, как скажешь - мне вообще без разницы, придёшь ты, не придёшь."
                    dv "Бывай!"
                    $ ds_lp['dv'] -= 1
                    hide dv with dissolve
                    stop ambience fadeout 2
                    jump ds_day4_after_breakfast_reject
            me "Ну, у меня и плавок даже нет…"
            show dv normal pioneer at center   with dspr
            dv "Надень мои."
            if ds_skill_list['instinct'].check(lvl_easy, passive=True).result():
                play sound ds_sfx_fys
                ins "{result}Это намёк! Очень прозрачный намёк!"
                play sound ds_sfx_psy
                aut "Ага, скорее уж попытка высмеять тебя - мужик в женских плавках!"
                play sound ds_sfx_fys
                pat "Ещё и сжимать твои причиндалы будет..."
                th "А откуда такие сведения?!"
                aut "Раз не знаешь - то оно и к лучшему. Меньше знаешь - крепче спишь!"
            play sound ds_sfx_psy
            vol "Идея плохая, в общем. Не поймут."
            me "Думаешь, они на меня налезут?"
            show dv grin pioneer at center   with dspr
            dv "А ты попробуй!"
            window hide
            menu:
                "Cогласиться":
                    window show
                    me "А давай!"
                    show dv surprise pioneer at center
                    with dspr
                    "Cначала Алиса не поняла тебя..."
                    show dv angry pioneer at center
                    with dspr
                    "...а потом как поняла!"
                    dv "Ты там вообще что ли?! Всерьёз поверил, что будешь мои плавки носить?!"
                    $ ds_lp['dv'] -= 1
                    $ ds_morale.damage()
                    play sound ds_sfx_psy
                    sug "Неудобно вышло..."
                    show dv laugh pioneer at center
                    with dspr
                    dv "Но ты не расстраивайся - найдём мы тебе плавки!"
                "Отвергнуть":
                    me "Наверное, не стоит…"
                    show dv smile pioneer at center   with dspr
                    dv "Да ты не бойся!{w} Найдём мы тебе плавки!"
        "Промолчать" if ds_d4_us_accept:
            window show
            "Ты хотел молча доесть завтрак, но Алиса, похоже, решила не дать тебе ни шанса на покой."
            dv "Я же правильно поняла, что ты идёшь с нами?"
            me "Ну..."
            show dv grin pioneer at center
            with dspr
            dv "А можно нескромный вопрос - а в чём ты пойдёшь?"
            play sound ds_sfx_int
            rhe "Она к тому, что не в пионерской форме же на пляже сидеть."
            play sound ds_sfx_psy
            vol "Что правда - тебе явно нужна одежда более пригодная для плавания. То бишь плавки."
            window hide
            menu:
                "Ответить, что пойдёшь так":
                    window show
                    me "Да прямо так и пойду, что такого?"
                    show dv laugh pioneer at center
                    with dspr
                    dv "Что такого? А плавать в этом ты как собираешься?"
                "Сказать про отсутствие плавок":
                    window show
                    me "Ну... да, у меня нет плавок..."
                    show dv normal pioneer at center   with dspr
                    dv "Надень мои."
                    if ds_skill_list['instinct'].check(lvl_easy, passive=True).result():
                        play sound ds_sfx_fys
                        ins "{result}Это намёк! Очень прозрачный намёк!"
                        play sound ds_sfx_psy
                        aut "Ага, скорее уж попытка высмеять тебя - мужик в женских плавках!"
                        play sound ds_sfx_fys
                        pat "Ещё и сжимать твои причиндалы будет..."
                        th "А откуда такие сведения?!"
                        aut "Раз не знаешь - то оно и к лучшему. Меньше знаешь - крепче спишь!"
                    play sound ds_sfx_psy
                    vol "Идея плохая, в общем. Не поймут."
                    me "Думаешь, они на меня налезут?"
                    show dv grin pioneer at center   with dspr
                    dv "А ты попробуй!"
                    window hide
                    menu:
                        "Cогласиться":
                            window show
                            me "А давай!"
                            show dv surprise pioneer at center
                            with dspr
                            "Cначала Алиса не поняла тебя..."
                            show dv angry pioneer at center
                            with dspr
                            "...а потом как поняла!"
                            dv "Ты там вообще что ли?! Всерьёз поверил, что будешь мои плавки носить?!"
                            $ ds_lp['dv'] -= 1
                            $ ds_morale.damage()
                            play sound ds_sfx_psy
                            sug "Неудобно вышло..."
                            show dv laugh pioneer at center
                            with dspr
                        "Отвергнуть":
                            me "Наверное, не стоит…"
                            show dv smile pioneer at center   with dspr
            show dv smile pioneer at center
            with dspr
            dv "Короче, горемычный ты наш сиротинушка. Сейчас найдём тебе плавки."
        "Промолчать" if not ds_d4_us_accept:
            window show
            "Алиса вскоре тоже доедает завтрак и встаёт из-за стола."
            show dv normal pioneer at center, ds_get_up
            dv "Бывай!"
            hide dv with dissolve
            "Ты остаёшься один. Доев завтрак, ты тоже выходишь, прикидывая, куда пойдёшь."
            jump ds_day4_after_breakfast_reject
    play sound ds_sfx_fys
    hfl "От этой фразы страх твой только усилился."
    dv "Подожди меня возле столовой, я вернусь через пару минут."
    vol "Вряд ли что-то такое случится от того, что ты её просто подождёшь."
    window hide
    menu:
        "Смириться":
            window show
            me "Ладно…"

        "Потребовать пойти вместе":
            window show
            me "А давай вместе сходим!"
            show dv grin pioneer at center
            with dspr
            dv "Нет уж, не пущу я тебя в свой домик - не дорос ещё!"
            play sound ds_sfx_psy
            aut "Прозвучало обидно."
            "И что хуже всего - Алиса уходит, даже не собираясь тебя ждать."
        "Последовать за Алисой":
            window show
            "Ты невозмутимо идёшь за Алисой."
            scene bg ds_int_dininghall_door_day
            show dv angry pioneer at center
            with dspr
            dv "Куда собрался?!"
            me "Так с тобой..."
            dv "Тебе не ясно было сказано: подождать!"
            dv "Вот и жди тут! Не пущу я тебя в свой домик, и не надейся!"
    stop ambience fadeout 2
    window hide
    scene bg int_dining_hall_people_day 
    with dissolve
    menu:
        "Подожать":
            window show
            $ persistent.sprite_time = "day"
            scene bg ext_dining_hall_near_day 
            with dissolve

            play ambience ambience_camp_center_day fadein 3

            window show
            "Закончив завтрак, ты выходишь на улицу и садишься на ступеньки."
            "Мимо тебя один за другим проходили пионеры, спешащие по своим делам."
            "Никто не останавливается.{w} Никто даже не смотрит в мою сторону."
            play sound ds_sfx_int
            lgc "Кажется, они совсем не считают тебя чужаком, а напротив – обычным подростком их возраста, можно сказать, своим товарищем."
            play sound ds_sfx_psy
            ine "Ты тоже воспринимаешь этот лагерь и всех его обитателей уже не с такой обострённой насторожённостью, как в первый день."
            window hide

            with fade

            window show
            "Алиса возвращается через пару минут."
            show dv normal pioneer at center   with dissolve
        "Cвалить":
            window show
            th "Нафиг, нафиг! Наверняка эта парочка приготовила мне очередной {i}сюрприз{/i}!"
            play sound ds_sfx_fys
            hfl "Поддерживаю!"
            $ ds_lp['dv'] -= 1
            jump ds_day4_after_breakfast_reject
        "Преследовать Алису" (skill='visual_calculus', level=lvl_medium):
            if ds_last_skillcheck.result():
                play sound ds_sfx_int
                vic "{result}Во-первых, пока ты думал, Алиса уже ушла далеко. Ты можешь идти без опаски."
                vic "Дальше - ты мог заметить, что она побежала из столовой прямо - то есть к озеру. Иди туда."
                window hide
                scene bg ext_dining_hall_near_day 
                with dissolve
                play ambience ambience_camp_center_day fadein 3
                $ renpy.pause(1.0)
                scene bg ext_houses_day
                with dissolve
                window show
                vic "Так, пока всё верно. Иди дальше."
                scene bg ext_house_of_dv_day
                with dissolve
                vic "Ну, кажется, и так понятно, что этот домик, и никакой иной, является домиком Алисы!"
                
                "Твои предположения подтверждаются - из домика выходит Алиса."
                play sound sfx_open_door_1
                show dv surprise pioneer at center
                with dissolve
                "Тебя она не ожидала увидеть тут."
                show dv angry pioneer at center
                with dspr
                dv "Я тебе где сказала меня ждать?! Чего ты такой непонятливый?!"
                me "Ну, я подумал..."
                dv "Подумал он..."
                show dv normal pioneer at center
                with dspr
                dv "Ладно, уже неважно!"
            else:
                play sound ds_sfx_int
                vic "{result}Проследить путь Алисы дальше, чем из столовой, тебе не удаётся."
                $ persistent.sprite_time = "day"
                scene bg ext_dining_hall_near_day 
                with dissolve

                play ambience ambience_camp_center_day fadein 3

                "Ты просто выходишь из столовой и садишься на ступеньку."
                play sound ds_sfx_int
                lgc "Если гора не идёт к Магомету, то Магомет идёт к горе. А здесь, похоже, сработает обратное."
                window show
                "Закончив завтрак, ты выходишь на улицу и садишься на ступеньки."
                "Мимо тебя один за другим проходили пионеры, спешащие по своим делам."
                "Никто не останавливается.{w} Никто даже не смотрит в мою сторону."
                play sound ds_sfx_int
                lgc "Кажется, они совсем не считают тебя чужаком, а напротив – обычным подростком их возраста, можно сказать, своим товарищем."
                play sound ds_sfx_psy
                ine "Ты тоже воспринимаешь этот лагерь и всех его обитателей уже не с такой обострённой насторожённостью, как в первый день."
                window hide

                with fade

                window show
                "Алиса возвращается через пару минут."
                show dv normal pioneer at center   with dissolve
    dv "Готов?"
    me "К чему?"

    play music music_list["i_want_to_play"] fadein 1

    "Она протягивает тебе плавки…"
    play sound ds_sfx_mot
    per_eye "Хотя плавками это назвать сложно…"
    per_eye "Больше они походят на розовые семейные трусы, украшенные бабочками и цветочками.{w} Точнее, ими и являются."
    $ ds_d4_dv_diag_asked = False
    $ ds_d4_dv_diag_offer = False
    $ ds_d4_dv_diag_try_reject = False
    jump ds_day4_after_breakfast_dv_dialogue

label ds_day4_after_breakfast_dv_dialogue:
    window hide
    menu:
        set ds_menuset
        "Cпросить, откуда взяла":
            window show
            me "Страшно спросить, откуда ты {i}это{/i} взяла?"
            show dv grin pioneer at center   with dspr
            dv "А что, боишься их надеть?"
            me "Да как-то, знаешь…{w} не имею никакого желания."
            play sound ds_sfx_psy
            aut "Её прикол ты оценил, но выставить себя на посмешище? Увольте!"
            show dv angry pioneer at center   with dspr
            dv "Надевай!"
            jump ds_day4_after_breakfast_dv_dialogue
        "Предложить примерить ей":
            window show
            me "Почему бы тебе их не примерить вместо меня?{w} Мне кажется, цвет этого бикини прекрасно оттеняет твои глаза!"
            show dv smile pioneer at center   with dspr
            dv "Давай на спор!"
            window hide
            menu:
                "Согласиться":
                    window show
                    me "Ну давай!"
                    play sound ds_sfx_int
                    rhe "Только вот как она сформулирует условие спора?"
                    show dv grin pioneer at center
                    with dspr
                "Отказаться":
                    window show
                    me "Нет, спасибо."
                    show dv angry pioneer at center   with dspr
            dv "Короче, либо ты идёшь на пляж в этом, либо плаваешь голым!"
            play sound ds_sfx_fys
            ins "Если всё тщательно взвесить, то второй вариант окажется даже лучше первого."
            window hide
            menu:
                "Продолжить":
                    window show
                "Согласиться плавать голым":
                    window show
                    me "А меня второй вариант устраивает!"
                    show dv laugh pioneer at center
                    with dspr
                    dv "Интересно, а Ольге Дмитриевне этот вариант тоже понравится?"
                    dv "Я пошутила, придурок! Либо идёшь в этом - либо ищи плавки сам!"
            jump ds_day4_after_breakfast_dv_dialogue
        "Передумать идти":
            window show
            me "Я вообще уже не планирую никуда идти!"
            show dv grin pioneer at center   with dspr
            dv "Тогда я всем расскажу, что ты подбросил мне эти трусы!"
            play sound ds_sfx_int
            lgc "А зачем тебе это?"
            me "И зачем мне это?"
            show dv laugh pioneer at center   with dspr
            dv "А мне откуда знать?"
            "Она расхохоталась."
            window hide
            menu:
                "Настоять на отказе":
                    window show
                    me "Не пытайся меня запугать! Никуда я не пойду - и точка!"
                    show dv angry pioneer at center
                    with dspr
                    dv "Да как хочешь! Сдался ты мне!"
                    hide dv with dissolve
                    $ ds_lp['dv'] -= 1
                    jump ds_day4_after_breakfast_reject
                "Отступить":
                    window show
            jump ds_day4_after_breakfast_dv_dialogue
        "Взять трусы":
            window show
            me "Ну ладно, возьму я у тебя эти трусы."
            show dv laugh pioneer at center
            with dspr
            dv "Ну ладно... как скажешь... удачи..."
            "Она заливается смехом, убегая"
            play sound ds_sfx_fys
            hfl "Что-то нехорошее в этом есть..."
            $ ds_on_beach_pants = True
            "Ты переодеваешься за столовой и выдвигаешься в сторону пляжа."
        "Сходить за своими":
            window show
            th "Конечно, я пойду не в этих гламурных «плавках»."
            me "Ладно, приду минут через десять."
            show dv smile pioneer at center   with dspr
            dv "И не опаздывай!"

            stop music fadeout 3

            "Сказав это, она убегает."
            window hide
            $ persistent.sprite_time = "day"
            scene bg ext_house_of_mt_day 
            with dissolve

            stop ambience fadeout 2

            window show
            "Ты плетёшься к домику вожатой, чтобы взять полотенце и заодно попытаться из чего-нибудь соорудить плавки."
            window hide

            $ persistent.sprite_time = "day"
            scene bg int_house_of_mt_day 
            with dissolve

            play ambience ambience_int_cabin_day fadein 3

            show mt normal pioneer at center   with dissolve
            window show
            "В комнате тебя ждёт Ольга Дмитриевна."
            mt "Семён, о Шурике ничего не слышно?"
            me "Ровно столько же, сколько и полчаса назад…"
            window hide
            menu:
                "Взять полотенце":
                    window show
                    "Ты подходишь к своей кровати и берёшь полотенце."
                    mt "Куда-то собираешься?"
                    me "Да, на пляж."
                    mt "Подожди, а у тебя есть плавки?{w} А то ты же вроде без вещей приехал…"
                    play sound ds_sfx_mot
                    res "Странно, что этот факт не удивил её при первой встрече."
                    me "Нет…"
                    show mt surprise pioneer at center   with dspr
                    mt "А в чём пойдёшь?"
                    play sound ds_sfx_int
                    lgc "Действительно, а в чём?"
                    me "Не знаю…"
                "Cпросить про плавки":
                    window show
                    me "Ольга Дмитриевна, а где можно плавки найти?"
            show mt normal pioneer at center   with dspr
            mt "Сейчас, подожди."

            play sound sfx_key_drawer

            "Она подходит к шкафу и открывает ключом запертый ящик."
            "Через мгновение у вожатой в руках оказываются обычные мужские плавки чёрного цвета."
            play sound ds_sfx_mot
            res "И откуда они у неё взялись?{w} А главное, зачем?"
            play sound ds_sfx_int
            lgc "Хотя, может, кто-то из прошлой смены забыл, мало ли…"
            play sound ds_sfx_psy
            ine "Учитывая все странности этого лагеря, найти мужские плавки в комнате Ольги Дмитриевны – это ещё не самое удивительное."
            window hide
            menu:
                "Поблагодарить":
                    window show
                    me "Спасибо."
                "Cпросить, откуда":
                    window show
                    me "Cпасибо... а откуда они?"
                    mt "Меня твои родители предупредили, что ты рассеянный и можешь приехать без вещей. Вот я и приготовила плавки."
                    play sound ds_sfx_int
                    lgc "Всё логично вроде бы."

            stop ambience fadeout 2

            "Плавки оказываются как раз твоего размера."
            window hide

            scene bg black 
            with dissolve

            window show
            "Ты переодеваешься за домиком и идёшь на пляж."
            window hide
    $ persistent.sprite_time = "day"
    scene bg ext_beach_day 
    with dissolve

    play ambience ambience_lake_shore_day fadein 3

    window show
    "Тут уже собралось много пионеров, но из знакомых – только Алиса и Ульяна."
    show us laugh swim at cright   with dissolve
    us "Иди к нам!"
    "Ты подходишь и садишься рядом с ними на песок."
    if not ds_on_beach_pants:
        show dv smile swim at cleft   with dissolve
        dv "Смотрю, ты нашёл получше…"
        "Она смотрит на твои плавки и ехидно улыбается."
        if ds_skill_list['instinct'].check(lvl_easy, passive=True).result():
            ins "{result}А может она и не на плавки смотрит?"
        window hide
        menu:
            "Подтвердить":
                window show
                me "Как видишь."
            "Проигнорировать":
                window show
            "Спошлить" if ds_last_skillcheck.result():
                window show
                me "Что, хочешь увидеть то, что под ними?"
                show dv shy swim at cleft
                with dspr
                dv "Придурок!"
                "И она отворачивается."
    us "Пойдём плавать!"
    window hide
    menu:
        "Согласиться":
            window show
            "Девочки убегают к воде, и ты следуешь за ними."

            scene cg ds_day4_us_dv_play
            with dissolve
            "Ты только сейчас замечаешь, что Алиса и Ульяна взяли с собой мяч."
            window hide
            menu:
                "Присоединиться":
                    window show
                    me "Я с вами!"
                    us "Давай!"
                    $ ds_lp['us'] += 1
                    "И она перекидывает тебе мячик."
                    th "И кому бы его кинуть теперь?"
                    window hide
                    menu:
                        "Кинуть Ульяне":
                            window show
                            me "Лови!"
                            "И ты бросаешь мяч в сторону Ульяны."
                            us "Ловлю-ловлю-ловлю!"
                            "И у неё получается поймать мяч."
                            us "Поймала!"
                            "Теперь она бросает Алисе, а та ловит."
                        "Кинуть Алисе":
                            window show
                            me "Лови!"
                            "И ты бросаешь мяч в сторону Алисы."
                            "Впрочем, Алиса с лёгкостью его отбивает и перенаправляет в сторону Ульяны."
                    scene black with fade
                    $ renpy.pause(2.0)
                    scene cg ds_day4_us_dv_play
                    with dissolve
                    play sound ds_sfx_fys
                    edr "Ты чувствуешь себя уставшим."
                    dv "Всё, достаточно!"
                    "Алиса с тобой солидарна."
                    us "Ну вот, мы только начали..."
                    "На самом деле вы играли не больше пятнадцати минут. Лучше всех показала себя, собственно, Ульянка - отбила все мячи."
                    "Но вы с Алисой также почти ни одного мяча не пропустили, впрочем."
                "Остаться в стороне":
                    window show
                    "Ты решаешь, что подобные игры не для тебя, и просто плаваешь в сторонке."
                    play sound ds_sfx_fys
                    ins "Однако, далеко отплыть ты ну никак не можешь - твой глаз упорно притягивается к Алисе."
                    ins "И немудрено - уж что-что, а фигура у неё прекрасная, и грудь, и попа!"
                    play sound ds_sfx_psy
                    emp "А что касается характера - ты не можешь отбросить мыслей, что с ним всё не так просто, как кажется на первый взгляд."
                    if ds_whom_helped == 'dv':
                        play sound ds_sfx_int
                        con "А ещё ты не можешь выкинуть из головы её прекрасную игру на гитаре."
                    play sound ds_sfx_psy
                    ine "А ещё Алиса тебе явно напоминает кого-то знакомого... и близкого тебе..."
                    play sound ds_sfx_psy
                    vol "Интересно, каковы шансы, что у тебя что-то с ней получится?"
                    th "Да я умоляю - примерно никаких! Мы с ней абсолютно разные!"
                    emp "Ну, как знать, как знать..."
                    dv "Всё, достаточно!"
                    "Алиса с тобой солидарна."
                    us "Ну вот, мы только начали..."
            "Девочки выходят из воды."
            us "Погоди, Алис!"
            "И Ульяна ныряет. Ненадолго."
            dv "Что такое?"
            us "На берегу покажу!"
            "Они оказываются более проворными и выходят на берег, когда ты ещё по пояс в воде."
            if ds_on_beach_pants:
                play sound ds_sfx_mot
                per_toc "И тут ты чувствуешь, как с тебя слетают твои «плавки», заботливо врученные Алисой!"
                th "Ой..."
                "Попытки их найти оказываются безрезультатными."
                play sound ds_sfx_psy
                vol "Cидеть в воде? Идея плохая. Попытайся незаметно выйти на берег и взять полотенце."
                scene bg ext_beach_day 
                show us fear swim at left
                show dv shocked swim at right
                with dissolve
                "Ты пытаешься прикрыть своё причинное место руками - но всё равно вынужден его открыть, чтобы взять полотенце."
                "И надо же было такому случиться - как раз в этот момент и Ульяна, и Алиса оказались рядом."
                us "Э-это что?.."
                play sound ds_sfx_psy
                emp "Ульяна шокирована, даже напугана."
                play sound ds_sfx_int
                enc "Немудрено - советское воспитание. Тема половых взимоотношений табуирована."
                "Ты пытаешься спрятаться, но, похоже, уже поздно."
                show us cry swim at left
                show dv sad swim at cleft
                with dspr
                us "Это отвратительно... Что, я теперь испорчена?"
                dv "Нет, Уль, всё будет нормально... никто даже не узнает об этом."
                us "Всё, теперь Даня от меня отвернётся, и я буду никому не нужна..."
                $ ds_lp['us'] -= 10
                play sound ds_sfx_int
                lgc "Похоже, и у Ульяны есть симпатия - этот самый Даня."
                play sound ds_sfx_psy
                sug "Ты нанёс ей травму. Серьёзную."
                show dv rage swim close at center
                with dspr
                play sound ds_sfx_fys
                hfl "И Алиса не собирается это оставлять безнаказанным."
                $ ds_lp['dv'] -= 10
                dv "Иди сюда, конченный урод! Ты чего это Ульянке ломаешь психику?"
                me "Я... я ничего..."
                dv "Как тебе вообще хватило ума залезть в воду в непригодной для этого одежде?!"
                dv "Я тебе шею сверну сейчас!"
                play sound sfx_lena_hits_alisa
                with hpunch
                $ ds_health.damage()
                "Прежде чем ты успеваешь что-либо сделать, Алиса нокаутирует тебя."
                "И дальше начинает тебя избивать."
                dv "НИКТО НЕ СМЕЕТ ОБИЖАТЬ УЛЬЯНУ!"
                with flash_red
                $ ds_health.damage()
                me "Остано... остановись..."
                play sound ds_sfx_fys
                edr "Ты чувствуешь, как теряешь сознание."
                $ ds_health.damage()
                show blink
                scene black with fade
                dv "Увижу тебя рядом с собой или Ульянкой - убью нахер! Лежи и думай, ублюдок!"
                "Последнее, что ты слышишь - шаги. Думать у тебя уже ни о чём не выйдет - ты отключаешься."
                jump ds_end_beaten_by_dv
            scene bg ext_beach_day
            show us laugh swim at cright 
            show dv normal swim at cleft 
            with dissolve
            "Ты выходишь на берег, и Ульяна уже встречает тебя."
        "Отказаться":
            window show
            me "Не хочется что-то.{w} Может, попозже…"
            dv "Ну, как знаешь."
            hide us 
            hide dv 
            with dissolve
            "Девочки убегают к воде."
            play sound ds_sfx_psy
            vol "Зачем ты вообще сюда пришёл?{w} Почему не ищешь ответы, разгадки?.."
            th "А волнует ли это меня сейчас?"
            play sound ds_sfx_psy
            ine "«Совёнок» кажется нормальным."
            ine "Конечно, за эти три с половиной дня с тобой произошло много всяких странных событий, но ни одно из них само по себе, взятое отдельно, не кажется чем-то чересчур фантастичным."
            play sound ds_sfx_int
            lgc "Тем более ты совершенно не приблизился к разгадке."
            lgc "Напротив, всё, что случалось, только больше запутывает ситуацию."
            th "Да и какие у меня альтернативы?"
            play sound ds_sfx_int
            rhe "Можно всё же попробовать порасспрашивать подробнее про это место."
            vol "Или решиться и сбежать."
            play sound ds_sfx_fys
            edr "Вот только сможешь ли ты дойти до какого-нибудь населённого пункта?"
            vol "И ты даже не знаешь, где что тут находится."
            show us laugh swim at cright 
            show dv normal swim at cleft 
            with dissolve
            "Через некоторое время девочки возвращаются.{w} Ульяна что-то держит в руках."
    us "Смотри!"
    "Ты поднимаешь глаза и видишь рака."
    play sound ds_sfx_int
    enc "Обычного речного рака."
    window hide

    scene cg d4_us_cancer 
    with dissolve

    window show
    "Ульянка ложится рядом и принимается его мучить."
    window hide
    menu:
        "Потребовать прекратить" (skill='authority', level=lvl_up_medium):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_psy
                aut "{result}Покажи, что с тобой шутки плохи."
                me "А ну оставь рака в покое!"
                "Ты показываешь такое злое лицо, что Ульяна не решается тебя ослушаться."
                scene bg ext_beach_day
                show us dontlike swim at center
                with dissolve
                us "Ладно, раз он тебе так дорог..."
                
                show us laugh swim at center
                with dspr
                us "...тогда держи его!"
                "C этими словами она кидает его тебе прямо в руки."
                play sound ds_sfx_mot
                cor "Тебе даже усилий прикладывать не приходится, чтобы его поймать."
            else:
                window show
                aut "{result}Ну, удачи отнять игрушку у ребёнка..."
                me "Оставь бедное животное в покое!"
                us "Ты что!{w} Это же рак!"
                
                me "Ну и что, что рак?{w} Он тоже имеет право на жизнь!"
                us "Вот сейчас я ему клешни поотрываю, а потом попрошу повариху его сварить на ужин!"
                me "Как будто больше есть нечего…"
                "Ты смотришь на Алису."
                play sound ds_sfx_psy
                emp "Похоже, Ульянкины забавы с бедным членистоногим её совсем не интересуют."
                window hide
                menu:
                    "Воззвать к Алисе":
                        window show
                        me "Хоть ты ей скажи!"
                        dv "А что такого?{w} Он же рак – так ему и надо!"
                        play sound ds_sfx_int
                        lgc "Кажется, эти девочки прогуливали уроки природоведения в начальных классах, и бережное отношение к окружающей среде им чуждо…"
                        window hide
                        menu:
                            "Выхватить рака":
                                window show

                                me "Отдай!"
                                "Ты выхватываешь рака у Ульянки."
                                window hide

                                $ persistent.sprite_time = "day"
                                scene bg ext_beach_day 
                                with dissolve

                                show us shy2 swim at center   with dissolve
                                window show
                                us "Да ради бога…"
                                play sound ds_sfx_psy
                                sug "Она не стала сопротивляться?"
                            "Забить":
                                window show
                                th "А впрочем, ладно, какое дело мне до рака?"
                                "Ульяна измывается над бедным членистоногим недолго, после чего кидает его... {w}в тебя!"
                                scene bg ext_beach_day 
                                with dissolve

                                show us laugh swim at center   with dissolve
                                window show
                                us "Лови!"
                                play sound ds_sfx_mot
                                cor "Но тебе и ловить его не приходится - он сам прилетает прямо тебе в руки."
                    "Выхватить рака":
                        window show

                        me "Отдай!"
                        "Ты выхватываешь рака у Ульянки."
                        window hide

                        $ persistent.sprite_time = "day"
                        scene bg ext_beach_day 
                        with dissolve

                        show us shy2 swim at center   with dissolve
                        window show
                        us "Да ради бога…"
                        play sound ds_sfx_psy
                        sug "Она не стала сопротивляться?"
                    "Забить":
                        window show
                        th "А впрочем, ладно, какое дело мне до рака?"
                        "Ульяна измывается над бедным членистоногим недолго, после чего кидает его... {w}в тебя!"
                        scene bg ext_beach_day 
                        with dissolve

                        show us laugh swim at center   with dissolve
                        window show
                        us "Лови!"
                        play sound ds_sfx_mot
                        cor "Но тебе и ловить его не приходится - он сам прилетает прямо тебе в руки."
        "Спасти рака" (skill='savoir_faire', level=lvl_medium):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_mot
                svf "{result}Внимание! Не упади в процессе на Алису!"
                "Тебе удаётся пробежать прямо над Алисой и снять с неё рака."
                $ persistent.sprite_time = "day"
                scene bg ext_beach_day 
                with dissolve

                show us dontlike swim at center   with dissolve
                window show
                us "Ой, не очень-то и хотелось…"
                play sound ds_sfx_psy
                sug "Она не стала сопротивляться?"
            else:
                window show
                play sound ds_sfx_mot
                svf "{result}Ты бросаешься за раком, совершенно не видя ничего вокруг. И это играет с тобой злую шутку."
                window hide
                play sound sfx_alisa_falls
                with vpunch
                window show
                "Ты оказываешься, конечно, с раком в руках - но на Алисе."
                scene ext_beach_day
                show dv angry swim close at center
                with dissolve
                dv "Что это за дела?! А ну слезь с меня!"
                play sound ds_sfx_fys
                ins "Твоё тело моментально откликается на подобную близость к девушке."
                show dv surprise swim close at center
                with dspr
                "Кажется, твою {i}реакцию{/i} заметила и Алиса."
                show dv rage swim close at center
                with dspr
                dv "Извращенец! Слезай уже с меня!"
                show us surp2 swim behind dv at right
                with dissolve
                us "А кто такой «извращенец»?"
                dv "Тебе рано знать о подобных вещах! А вот кое-кому я сейчас задам!"
                "Тут Алиса встаёт, не без труда скинув тебя с себя."
                with vpunch
                show dv angry swim at left
                with dspr
                "А ты всё держишь рака в руках."
        "Забить":
            window show
            th "А впрочем, ладно, какое дело мне до рака?"
            "Ульяна измывается над бедным членистоногим недолго, после чего кидает его... {w}в тебя!"
            scene bg ext_beach_day 
            with dissolve

            show us laugh swim at center   with dissolve
            window show
            us "Лови!"
            play sound ds_sfx_mot
            cor "Но тебе и ловить его не приходится - он сам прилетает прямо тебе в руки."
    window show
    "Ты смотришь в глаза бедному животному."
    play sound ds_sfx_psy
    ine "Они совершенно ничего не выражают, но если бы он умел разговаривать, то обязательно возмутился бы, возможно, даже сослался бы на конвенцию ООН о правах человека."
    ine "Правда, вряд ли это бы помогло..."
    window hide
    "Ты относишь рака к реке и отпускаешь на волю."
    show us surp1 swim at center   with dspr
    us "Ничего, ещё наловлю – тут их много."
    th "Кто бы сомневался…"
    hide us  with dissolve
    window hide

    with fade2

    stop ambience fadeout 2

    window show
    play sound ds_sfx_fys
    "Время шло, и незаметно тебя разморило…"
    window hide

    scene bg black 
    with fade

    window show
    "Ты задремал."
    "Ты не помнишь, что тебе снилось, если снилось вообще, но просыпаешься ты оттого, что кто-то тряс тебя за плечо."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_beach_day 
    with fade

    play ambience ambience_lake_shore_day fadein 3

    show mt normal swim at center   with dissolve
    window show
    "Надо мной стояла Ольга Дмитриевна."
    me "Тоже поплавать пришли?"
    "Спросил я спросонья."
    mt "Нет.{w} Уже обед скоро, а мы Шурика всё ещё не можем найти."
    "Сказала вожатая, стоящая передо мной в мокром купальнике..."
    me "И?"
    mt "Хочу, чтобы ты поискал его."
    me "А что, кроме меня, в лагере больше пионеров нет?"
    "Я искренне возмутился."
    "С каждым разом становилось всё понятнее, что Ольга Дмитриевна держит меня за посыльного с функциями раба.{w} Или наоборот..."
    show mt angry swim at center   with dspr
    mt "Раз я пришла к тебе, значит, хочу, чтобы ты мне помог."
    "И почему же именно ко мне?"
    "Однако, подумав, я решил согласиться."
    "В конце концов, плечи и вся спина сильно обгорели на солнце во время сна, а поиски Шурика, возможно, позволят получше познакомиться с теми местами лагеря, где бывать мне ещё не доводилось."
    me "Ладно…"
    "В плавках идти не комильфо, поэтому сначала надо было переодеться."
    window hide

    stop ambience fadeout 2

    scene black 
    with dissolve

    window show
    "..."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 2

    window show
    "И вот спустя десять минут я стоял на пороге домика Ольги Дмитриевны и думал, куда пойти."
    window hide
    $ disable_all_zones_ds_small()
    $ set_zone_ds_small("entrance","ds_day4_busstop")
    $ set_zone_ds_small("boathouse","ds_day4_boathouse")
    $ set_zone_ds_small("house_me_mt","ds_day4_house_of_mt")
    $ set_zone_ds_small("forest","ds_day4_forest")
    $ set_zone_ds_small("library","ds_day4_library")
    if ds_have_guess_sh:
        $ set_zone_ds_small("old_camp", "ds_day4_old_camp")
    $ set_zone_ds_small("scene","ds_day4_scene")

    jump ds_day4_map

label ds_day4_after_breakfast_reject:
    $ persistent.sprite_time = 'day'
    scene bg ext_dining_hall_away_day
    with dissolve
    play ambience ambience_camp_center_day fadein 3

    window show
    play sound ds_sfx_psy
    vol "В общем-то, с двумя главными хулиганками лагеря тебе делать точно нечего. Да ещё и на пляж с ними идти? Нет уж."
    play sound ds_sfx_mot
    com "У тебя и так полно поводов, чтобы волноваться."
    play sound ds_sfx_int
    lgc "И, кстати, один из них - это исчезновение Шурика. Точнее, количество волнения вокруг его персоны."
    lgc "Какой-то пионер, который проводит всё своё свободное время в кружке и столовой. Его нет, кажется, всего два часа после подъёма, а уже столько шума."
    th "Хотя, действительно, почему тогда его оказалось так сложно найти, если он бывает всего в двух местах?"
    "Я решил мельком заглянуть в кружки."
    window hide

    if ds_sl_beach_invite:
        scene bg ext_square_day
        show sl smile pioneer at center
        with dissolve
        "Однако, на площади тебя перехватывает Славя."
        sl "Привет, Семён!"
        me "Привет."
        sl "Хорошая погода сегодня, не правда ли?"
        th "Погода и правда хорошая..."
        sl "А помнишь, мы с тобой договаривались на пляж сходить?"
        play sound ds_sfx_psy
        vol "Было дело, было..."
        me "Ну да..."
        sl "А пошли сейчас!"
        me "А как же Шурик?"
        show sl normal pioneer at center
        with dspr
        sl "Ну вот искупаемся, освежимся и поищем Шурика!"
        window hide
        menu:
            "Пойти со Славей":
                window show
                me "А давай!"
                show sl smile pioneer at center
                with dspr
                sl "Идём!"
                $ ds_lp['sl'] += 1
                jump ds_day4_sl_beach
            "Отказаться":
                window show
                me "Извини, не сейчас. Я переживаю за Шурика!"
                show sl sad pioneer at center
                with dspr
                sl "Ну ладно..."
                $ ds_lp['sl'] -= 1
                hide sl with dissolve
                "И она уходит расстроенная."
                play sound ds_sfx_int
                dra "А ведь Шурик вас волнует примерно на том же уровне, что и проблемы миграции сов, мессир."
                th "Сов..."
                dra "Ну так ведь лагерь «Совёнок»!"
                th "Ладно, идём к клубу!"

    scene bg ext_clubs_day
    show mt normal pioneer at center
    with dissolve
    "Однако, по всей видимости, Ольге Дмитриевне идея проверить клуб пришла раньше - она уже выходит из него."
    mt "О, Семён, тоже Шурика ищешь?"
    me "Ну... типа того..."
    show mt grin pioneer at center  with dspr
    mt "Вот, что значит - образцовый пионер! Беспокоится за товарищей и сам занимается поисками!"
    play sound ds_sfx_psy
    aut "Всегда готов..."
    dra "Вы недалеки от правды, мессир."
    mt "Ну, тогда не буду мешать."
    hide mt with dissolve
    "Она тотчас убегает."
    play sound ds_sfx_int
    lgc "Прохлаждаться, не иначе."
    th "Придётся заниматься поисками дальше..."
    window hide
    $ disable_all_zones_ds_small()
    $ set_zone_ds_small("entrance","ds_day4_busstop")
    $ set_zone_ds_small("boat_station","ds_day4_boathouse")
    $ set_zone_ds_small("house_me_mt","ds_day4_house_of_mt")
    $ set_zone_ds_small("forest","ds_day4_forest")
    $ set_zone_ds_small("library","ds_day4_library")
    $ set_zone_ds_small("scene","ds_day4_scene")
    if ds_have_guess_sh:
        $ set_zone_ds_small("old_camp", "ds_day4_old_camp")

    jump ds_day4_map

label ds_day4_map:
    stop ambience fadeout 3
    stop music fadeout 3
    window hide
    if ds_d4_places_remain == 0:
        jump ds_day4_lunch
    $ show_small_map_ds()

label ds_day4_sl_beach:
    me "Подожди, Славь, а как же плавки?"
    show sl shy pioneer at center
    with dspr
    sl "И плавки я предусмотрела..."
    play sound ds_sfx_fys
    ins "Ой, кажется, ты заинтересовал девушку..."
    play sound ds_sfx_psy
    vol "Да что ты всё об одном и том же? Просто Славя хочет всем помочь."
    ins "Да говорю вам: ей понравился Семён!"

    scene bg ext_beach_day
    show sl smile pioneer at center
    with dissolve
    sl "Сейчас, Семён, я скину с себя форму!"
    show sl normal swim at center
    with dspr
    "И нет, она не отходит никуда - она прямо при тебе скидывает юбку и рубашку."
    "Впрочем, под ними уже был купальный костюм."
    sl "А вот тебе было бы неплохо отойти в кусты и переодеться."
    "Ты так и делаешь. Вскоре ты предстаёшь перед Славей в одних плавках."
    if ds_triggered_dv:
        show dv rage swim at right
        with dissolve
        dv "ДА ТЫ ИЗДЕВАЕШЬСЯ НАДО МНОЙ СЕГОДНЯ?!"
        me "Алиса?"
        dv "То Лена, то теперь Славя! Давай ещё к Мику пойди, лишь бы не со мной!"
        $ ds_lp['dv'] -= 3
        hide dv with dissolve
        show sl surprise swim at center
        with dspr
        sl "А... это она о чём вообще?"
        window hide
        menu:
            "Притвориться непонимающим":
                window show
                me "Да видимо на солнышке перегрелась... я вообще не понимаю, причём тут Лена и ты."
                show sl serious swim at center
                with dspr
                sl "Мне что-то это не нравится..."
            "Рассказать как есть":
                window show
                me "Да я за завтраком возьми и скажи, что с Леной вечер провёл..."
                show sl normal swim at center
                with dspr
                sl "Ну... это ты зря, Семён, конечно. Запомни: не говори девушке, неравнодушной к тебе, про других девушек."
                play sound ds_sfx_mot
                res "Типа Алиса по её мнению неравнодушна к тебе?"
                play sound ds_sfx_psy
                emp "Да это очевидно же было!"
                play sound ds_sfx_psy
                sug "Как бы то ни было, Славя права. Говорить про Лену было лишним."
                sl "Ладно, успокоится, наверное..."
    show mt smile swim at left
    with dissolve
    mt "О, Славя, Семён! У меня есть для вас поручение!"
    sl "Какое, Ольга Дмитриевна?"
    mt "Шурика поищите!"
    me "А как же..."
    show sl serious swim at center
    with dspr
    sl "Идём, Семён. Нельзя бросать товарища в беде!"
    mt "Вот, молодец, Славя!"
    play sound ds_sfx_psy
    vol "Кажется, тебе деваться некуда. Не оставаться же тебе рядом с отвергнутыми прежде Алисой и Ульяной!"
    window show
    me "Ладно, пойдём..."
    show sl normal pioneer at center
    with dspr
    "Славя накидывает форму, а ты возвращаешь вместо плавок на место трусы и выходишь к ней - также в форме."
    sl "Вперёд!"
    jump ds_day4_find_with_sl

label ds_day4_boathouse:

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day 
    with dissolve

    window show
    play sound ds_sfx_int
    lgc "Может, Шурику захотелось пособирать камни у воды?"
    lgc "В крайнем случае ты найдёшь там его труп…"

    stop ambience fadeout 2

    play sound ds_sfx_psy
    emp "Впрочем, до такого дойти не должно! По крайней мере, тебе искренне хочется в это верить."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_square_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    if ds_lp['dv'] >= 20:
        window show
        "Ты проходишь по площади, как вдруг тебя кто-то окликает."
        show dv smile pioneer2 far at center    with dissolve
        dv "Подожди!"
        show dv smile pioneer2 at center   with dissolve
        "Алиса подходит и улыбается."
        play sound ds_sfx_fys
        hfl "Тут явно какой-то подвох. Как неизбежное следствие Дваче."
        hfl "Беги. Или атакуй первым."
        play sound ds_sfx_psy
        emp "Всё не так плохо. Ты ей интересен."
        play sound ds_sfx_psy
        sug "А может, это просто дежурная вежливость?"
        play sound ds_sfx_int
        lgc "Да скорее Генда сойдёт с пьедестала, нежели Алиса будет вежливой!"
        dv "Куда путь держишь?"
        window hide
        menu:
            "Сказать, что её и искал":
                window show
                me "Да знаешь, как раз тебя и искал!"
                show dv surprise pioneer2 at center
                with dspr
                "Она ожидала чего угодно - но не такого ответа."
                show dv grin pioneer2 at center
                with dspr
                dv "Что ж, ты по адресу!"
                $ ds_lp['dv'] += 1
                me "Пойдём со мной... ты мне нужен!"
                if ds_skill_list['drama'].check(lvl_easy, passive=True).result():
                    play sound ds_sfx_int
                    dra "{result}Что-то тут не так, мессир. Явно пытается сымпровизировать."
                    window hide
                    menu:
                        "Высказать подозрения":
                            window show
                            me "Ты точно ничего не готовишь против меня?"
                            dv "Да точно! Совершенно точно ничегошеньки!"
                            dra "Врёт."
                            $ ds_lp['dv'] -= 1
                            
                            window hide
                            menu:
                                "Согласиться":
                                    window show
                                    me "Идём..."
                                    jump ds_day4_dv_joke
                                "Отказаться":
                                    window show
                                    me "Нет, мне это что-то не нравится..."
                                    show dv angry pioneer2 at center
                                    with dspr
                                    dv "Ну не хочешь - как хочешь!"
                                    hide dv with dissolve
                                    $ ds_lp['dv'] -= 1
                                    th "И что это было?"
                                    "Ты идёшь дальше к реке."
                else:
                    me "Идём..."
                    jump ds_day4_dv_joke
            "Ответить про Шурика":
                window show
                me "Шурика ищу…{w} Ольга Дмитриевна попросила."
                show dv normal pioneer2 at center   with dspr
                dv "И как, интересно?"
                "Она пристально смотрит в глаза."
                if not ds_skill_list['composure'].check(lvl_challenging, passive=True).result():
                    play sound ds_sfx_mot
                    com "{result}Ты смущаешься и отводишь взгляд."
                window hide
                menu:
                    "Cказать, что интересно":
                        window show
                        me "Очень!"
                        show dv laugh pioneer2 at center
                        with dspr
                        dv "Да брешешь!"
                        play sound ds_sfx_psy
                        vol "Она попала в точку."
                    "Сказать, что человек пропал":
                        window show
                        me "Да не то чтобы очень…{w} Но человек всё-таки пропал!"
                    "Сказать, что заставили":
                        window show
                        me "Ну, мне велели - я и пошёл..."
                        show dv dontlike pioneer2 at center
                        with dspr
                        dv "Ну естественно, ты же слабак!"
                        $ ds_morale.damage()
                        me "Так ведь... пропал же..."
                        show dv normal pioneer2 at center
                        with dspr
                dv "Ну, ты же не будешь впадать в панику из-за такой мелочи?"
                me "Ты о чём?"
                dv "Прошло всего несколько часов.{w} Может, загулял…"
                "Конечно, я был согласен с ней, но вида не подал."
                me "Да, верно.{w} Но всякое может быть…"
                show dv smile pioneer2 at center   with dspr
                dv "Давай я тебе помогу!"
                me "Эээ… Чем это?"
                "Я насторожился."
                dv "Шурика искать!"
                me "Да я и сам бы…"
                show dv grin pioneer2 at center   with dspr
                dv "Да брось ты!"
                "Она опять как-то недобро улыбнулась."
                "Нет, улыбка её была вполне милой, но мне почему-то упорно казалось, что ничего хорошего за ней не скрывается."
                me "Ну, если ты настаиваешь…"
                "Пока что я не мог понять, что она замышляет, а веской причины для отказа не находилось."
                show dv smile pioneer2 at center   with dspr
                dv "Только сначала мне надо домой забежать взять кое-что."
                me "Хорошо, я подожду."
                dv "Да что ты стоять будешь!{w} Пойдём со мной!"

                stop ambience fadeout 2

                me "Ладно…"
            "Отказаться отвечать":
                window show
                me "А вот не скажу тебе!"
                show dv angry pioneer2 at center
                with dspr
                dv "Пф, не очень-то и интересно!"
                play sound ds_sfx_int
                dra "Врёт, мессир. Ей {i}очень{/i} интересно."
                hide dv with dissolve
                "Алиса уходит обиженная."
                $ ds_lp['dv'] -= 1
            "Бежать":
                window show
                me "НЕ ТРОГАЙ МЕНЯ!"
                "С истеричным криком ты убегаешь куда-то в сторону склада."
                scene bg ds_ext_storage_day
                with dissolve
                $ ds_lp['dv'] -= 2
                play sound ds_sfx_fys
                hfl "Алиса тебя не догоняет. Уже неплохо."
            "Нанести превентивный удар" (skill='physical_instrument', level=lvl_medium):
                if ds_last_skillcheck.result():
                    window show
                    play sound ds_sfx_fys
                    phi "{result}Покажи этой пацанке, кто тут мужик!"
                    "Почему-то ты решаешь это сделать силой."
                    play sound sfx_lena_hits_alisa
                    show dv cry pioneer2 at center
                    with dspr
                    play sound ds_sfx_mot
                    com "Для Алисы твой поступок оказывается настолько неожиданным, что в первые мгновения ей не удаётся удержать выступившие слёзы."
                    $ ds_lp['dv'] -= 5
                    play sound ds_sfx_psy
                    emp "Она воспринимает твой удар как нож в спину, не иначе."
                    show dv angry pioneer2 at center
                    with dspr
                    "Впрочем, уже через секунд пять она собирается и вновь скрывает свою «нежную» сторону."
                    dv "ЧТО ТЫ ТВОРИШЬ?!"
                    me "Ты явно хотела мне что-то нехорошее сделать!"
                    dv "Может, и хотела пошутить! Но не избивать! Тем более, ты парень, а я девушка!"
                    show dv rage pioneer2 close at center
                    with dspr
                    hfl "Беги. А то получишь в табло."
                    window hide
                    menu:
                        "Бежать":
                            window show
                            scene bg ext_houses_day at ds_running
                            with dissolve
                            "Ты бежишь от разъярённой Алисы."
                            "Впрочем, похоже, она не собирается тебя догонять."
                            play sound ds_sfx_psy
                            aut "Не иначе, считает слишком низким для себя бежать за тобой."
                            scene bg ext_houses_day
                            "Ты останавливаешься. После чего продолжаешь свой путь к реке."
                        "Принять удар на себя" (skill='pain_threshold', level=lvl_medium):
                            window show
                            "Ты готовишься принять ответку от Алисы."
                            play sound sfx_face_slap
                            with hpunch
                            "Алиса ограничивается пощёчиной."
                            window hide
                            if ds_last_skillcheck.result():
                                window show
                                play sound ds_sfx_fys
                                pat "{result}Но всё равно больно! Впрочем, не сильно."
                            else:
                                window show
                                play sound ds_sfx_fys
                                pat "{result}Но даже от этого у тебя уже горит щека!"
                                $ ds_morale.damage()
                            
                            dv "Иди! И чтобы я тебя больше не видела!"
                            hide dv with dissolve
                            "Ты и идёшь туда, куда изначально держал путь."
                else:
                    window show
                    play sound ds_sfx_fys
                    phi "{result}Ты замахиваешься... но и итоге всё ограничивается слабым шлепком по лицу."
                    show dv angry pioneer2 at center
                    with dspr
                    dv "Не смешно! Чего ты сразу с кулаками бросаешься! Я с миром!"
                    dv "Ну раз не хочешь по-хорошему - будет по-плохому!"
                    $ ds_lp['dv'] -= 2
                    dv "Удачи!"
                    hide dv with dissolve
                    play sound ds_sfx_psy
                    emp "По сути она обиделась на тебя. Но, вероятно, не собирается тебе отвечать."
                    play sound ds_sfx_fys
                    hfl "Но тем не менее будь осторожен."
                    "Ты направляешься к реке."
        window hide
    play ambience ambience_lake_shore_day fadein 3
    scene bg ext_boathouse_day
    with dissolve
    "Ты добираешься до лодочной станции."
    play sound ds_sfx_mot
    per_eye "Вполне ожидаемо ты тут Шурика не обнаруживаешь."
    th "Ладно..."
    $ ds_d4_places_remain -= 1
    $ disable_current_zone_ds_small()
    jump ds_day4_map

label ds_day4_dv_joke:
    $ persistent.sprite_time = "day"
    scene bg ext_house_of_dv_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    show dv normal pioneer2 at center   with dissolve
    window show
    "Вы подходите к домику Алисы."
    play sound ds_sfx_mot
    per_eye "Он бы походил на все остальные домики пионеров, если бы не Весёлый Роджер на двери."
    dv "Кстати, моя соседка – Ульянка."
    play sound ds_sfx_int
    lgc "Никогда бы не догадался!"
    me "Окей."
    window hide

    stop ambience fadeout 2

    play sound sfx_open_dooor_campus_2

    pause(1)

    $ persistent.sprite_time = "day"
    scene bg int_house_of_dv_day 
    with dissolve

    play ambience ambience_int_cabin_day fadein 2

    show dv normal pioneer2 at center   with dissolve
    window show
    "Вы заходите. Внутри царит полнейший беспорядок."
    window hide
    scene bg semen_room
    show prologue_dream
    with dissolve
    play sound ds_sfx_psy
    window show
    ine "У тебя в голове всплывает образ, почему-то ассоциирующийся с домом... видимо, твоя прежняя квартира."
    scene bg int_house_of_dv_day 
    show dv normal pioneer2 at center
    with dissolve
    ine "Вообще, ты совсем по-другому себе представлял девчачьи комнаты: белоснежные простыни на кроватях; стены, пол и потолок сверкают; нигде ни пылинки."
    lgc "Но если учесть, что здесь живут две самые «образцовые» пионерки…"
    "Некоторое время вы просто стоите молча."
    window hide
    menu:
        "Спросить":
            window show
            me "И что ты хотела взять?"
            show dv surprise pioneer2 at center   with dspr
            dv "А?"
            "Кажется, я вывел Алису из раздумий."
            show dv smile pioneer2 at center   with dspr
            dv "Да…{w} На самом деле это не здесь…{w} Подожди, я быстро!"
        "Ждать дальше":
            window show
            "Вы продолжаете стоять."
            show dv smile pioneer2 at center
            with dspr
            dv "А! Вспомнила! Это не здесь! Подожди, я быстро!"
        "Начать уходить":
            window show
            me "Ну, раз тебе тут ничего не нужно..."
            show dv angry pioneer2 at center
            with dspr
            dv "Нужно! Оно не тут! Я сейчас вернусь!"
    hide dv  with dissolve

    play sound sfx_close_door_campus_1

    "Она улыбается и убегает."
    play sound ds_sfx_int
    vic "Что-то она какая-то рассеянная сегодня."
    if ds_skill_list['drama'].check(lvl_medium, passive=True).result():
        play sound ds_sfx_int
        dra "{result}Или же {i}изображает{/i} таковую."
    "Ты рассматриваешь комнату."
    vic "Нельзя сказать, что здесь недавно случился погром, но беспорядок порядочный."
    th "Получается, я ещё не самый ленивый и неаккуратный человек в мире – раз уж всего за одну смену в лагере можно развести такой бардак."
    "Ты не думаешь ни о чём конкретно, а просто осматривал домик Алисы."
    play sound ds_sfx_mot
    per_eye "Плакаты советских артистов, какие-то книжки на полках, всякая бытовая мелочёвка…"

    if ds_skill_list['half_light'].check(lvl_easy, passive=True).result():
        stop ambience fadeout 2

        play music music_list["always_ready"] fadein 1

        play sound ds_sfx_fys
        hfl "{result}Всё не так!"
        hfl "{result}В ближайшее время должно что-то случиться!{w} Что-то плохое!"
        play sound ds_sfx_int
        lgc "А почему Алиса тебя оставила здесь одного?"
        lgc "Ответ на этот вопрос таит в себе разгадку."
        hfl "Как бы то ни было, здесь оставаться опасно!"
        window hide
        menu:
            "Ждать":
                window show
            "Уйти":
                window show
                "Ты подходишь к двери и дёргаешь за ручку."
                play sound sfx_campus_door_rattle
                "Заперто!"
                hfl "Вот так номер!{w} Как она успела закрыть тебя так, что ты даже не услышал?"
                hfl "Неизвестно, что она затевает, но пора отсюда выбираться!"
                window hide
                menu:
                    "Вылезти через окно":
                        window show
                        play sound sfx_open_window

                        "Ты подходишь к окну, с трудом открываешь его и вылезаешь."
                        window hide

                        $ persistent.sprite_time = "day"
                        scene bg ext_house_of_dv_day 
                        with dissolve
                        jump ds_day4_dv_escaped
                    "Выбить дверь" (skill='physical_instrument', level=lvl_formidable):
                        if ds_last_skillcheck.result():
                            window show
                            play sound ds_sfx_fys
                            phi "{result}Впрочем, двери тут хлипкие, так что ты без труда дверь выбиваешь."
                            scene bg ext_house_of_dv_day
                            with vpunch
                            "И вываливаешься из домика, лёжа на двери."
                            
                            "Ты поднимаешься и смотришь на домик Алисы."
                            $ ds_dv_door_broken = True
                            
                            jump ds_day4_dv_escaped
                        else:
                            window show
                            play sound ds_sfx_fys
                            phi "{result}Но дверь оказывается не такой слабой, какой она оказалась на первый взгляд."
                            play sound ds_sfx_fys
                            pat "Всё, чего ты добился - отбил себе плечо."
                            
                            $ ds_health.damage()
                    "Ждать своей участи":
                        window show
                        th "Да ладно, ничего же не случится? Надо ведь доверять людям?"
                        play sound ds_sfx_psy
                        vol "Доверяй, но проверяй! А впрочем как хочешь."
    show mt normal panama pioneer at cright
    show dv smile pioneer at cleft
    with dissolve
    "Вскоре Алиса возвращается. И оказывается, что она хотела «взять» Ольгу Дмитриевну!"
    if ds_skill_list['logic'].check(lvl_trivial, passive=True).result():
        play sound ds_sfx_int
        lgc "{result}Она решила тебя в чём-то обвинить. Скорее всего - неправомерно."
    dv "Вот, видите?"
    show mt surprise panama pioneer at cright
    with dspr
    mt "Да, вижу..."
    if ds_karma >= 50:
        mt "...но это очень странно! Семён же примерный пионер!"
        dv "Но вы же видите? Он тут! В домике у меня!"
    show mt angry panama pioneer at cright
    with dspr
    mt "Вы мне ничего не хотите объяснить, молодой человек?!"
    window hide
    menu:
        "Подыграть Алисе":
            window show
            me "Ну... да... не удержался..."
            show dv shocked pioneer at cleft
            show mt shocked panama pioneer at cright
            with dspr
            "Алиса удивлена таким поворотом событий. Как и Ольга Дмитриевна."
            mt "Ты... Ты... Ты понимаешь, насколько это серьёзное нарушение?!"
            $ ds_lp['mt'] -= 2
            $ ds_lp['dv'] += 2
            $ ds_karma -= 10
            show mt rage panama pioneer at cright
            with dspr
            mt "Да ты будешь выкинут из лагеря за такое! Я устрою тебе отвратительную характеристику! Ни в комсомол, никуда тебя не возьмут!"
            show dv guilty pioneer at cleft
            with dspr
            dv "Позвольте, Ольга Дмитриевна..."
            mt "Не сейчас, Двачевская!"
            show dv angry pioneer at cleft
            with dspr
            dv "Семён НЕ ВИНОВАТ!"
            show mt surprise panama pioneer at cright
            with dspr
            mt "В смысле?!"
            dv "Мы с Семёном решили... вас разыграть."
            mt "Вы... вы вообще нормальные?!"
            mt "Это серьёзное дело, а вы так шутите?!"
            me "Извините."
            show mt normal panama pioneer at cright
            with dspr
            mt "Ладно, главное - что домогательств не было. А сейчас мне надо Шурика искать, и вам было бы неплохо."
            hide mt
            show dv guilty pioneer at center
            with dspr
            dv "Спасибо... что всё же не подставил меня..."
            me "Ну так ведь..."
            "Ты хотел сказать что-нибудь ободряющее, но она решает обрезать диалог."
            show dv grin pioneer at center
            with dspr
            dv "А теперь тебе пора!"
            me "Но..."
            show dv angry pioneer at center
            with dspr
            dv "Никаких «но»! Я могу и отозвать свои слова перед вожатой!"
        "Оправдываться":
            window show
            me "Она всё врёт! Я ничего с ней не делал!"
            show dv guilty pioneer at cleft
            with dspr
            if ds_karma < 0:
                show mt rage panama pioneer at cright
                with dspr
                mt "А знаешь, мне что-то не верится! Ты тут уже натворил делов!"
                dv "Ну да, я вас обманула..."
                show mt surprise panama pioneer at cright
                with dspr
                "Ольга Дмитриевна удивлена ходом Алисы. Как и ты."
                mt "В смысле?"
                dv "Ну, я хотела над ним подшутить..."
                show mt angry panama pioneer at cright
                with dspr
                mt "Подшутить?! Ты понимаешь, что то, что ты выдвинула - серьёзное обвинение?!"
                mt "За такое как минимум выкидывают из лагеря! С волчьим билетом!"
            else:
                show mt surprise panama pioneer at cright
                with dspr
                mt "Ну вот и я так думаю, что Двачевская пытается меня надуть!"
            mt "В общем, извиняйся перед Семёном!"
            dv "Ну ладно, извини..."
            mt "Вот так-то! Теперь пора бы и Шурика поискать!"
            hide mt with dissolve
            show dv angry pioneer at center
            with dspr
            dv "Так меня ещё не позорили..."
            play sound ds_sfx_psy
            emp "Она обиделась на тебя."
            play sound ds_sfx_psy
            aut "Только вот за что? Это же она тебя подставить пыталась!"
            dv "Прощай!"
        "Отказаться объясняться" (skill='composure', level=lvl_legendary):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_mot
                com "{result}Ты прав. И лучше всего ты это покажешь, если не будешь судорожно оправдываться, а будешь стоять спокойно."
                
                me "Мне нечего сказать."
                mt "То есть, ты залезаешь в домик Алисы..."
                me "Я не залезал - она сама меня позвала, а потом ушла."
                show mt surprise panama pioneer at center
                with dspr
                mt "А ты ведь говорила, что он залез к тебе в домик!"
                show dv guilty pioneer at cleft
                with dspr
                dv "Да-да-да, я вас с Семёном разыграла..."
                show mt angry panama pioneer at cright
                with dspr
                mt "Подшутить?! Ты понимаешь, что то, что ты выдвинула - серьёзное обвинение?!"
                mt "За такое как минимум выкидывают из лагеря! С волчьим билетом!"
                mt "В общем, извиняйся перед Семёном!"
                dv "Ну ладно, извини..."
                mt "Вот так-то! Теперь пора бы и Шурика поискать!"
                hide mt with dissolve
                show dv angry pioneer at center
                with dspr
                dv "Так меня ещё не позорили..."
                play sound ds_sfx_psy
                emp "Она обиделась на тебя."
                play sound ds_sfx_psy
                aut "Только вот за что? Это же она тебя подставить пыталась!"
                dv "Прощай!"
            else:
                play sound ds_sfx_mot
                com "{result}Ты слишком нервничаешь - ты ведь даже не знаешь, что тебе инкриминируют!"
                
                me "Позвольте... вы о чём?"
                mt "О домогательствах! Ты домогался Алисы?!"
                me "Нет... Я просто пришёл сюда по приглашению Алисы..."
                show dv laugh pioneer at cleft
                with dspr
                dv "Думаешь, я бы тебя пригласила?"
                me "Но ведь пригласила!"
                mt "Так, довольно!"
                if ds_karma < 0:
                    show mt rage panama pioneer at cright
                    with dspr
                    mt "Что-то я тебе не особо верю... Ты тут уже натворил делов!"
                    dv "Ну да, я вас обманула..."
                    show mt surprise panama pioneer at cright
                    with dspr
                    "Ольга Дмитриевна удивлена ходом Алисы. Как и ты."
                    mt "В смысле?"
                    dv "Ну, я хотела над ним подшутить..."
                    show mt angry panama pioneer at cright
                    with dspr
                    mt "Подшутить?! Ты понимаешь, что то, что ты выдвинула - серьёзное обвинение?!"
                    mt "За такое как минимум выкидывают из лагеря! С волчьим билетом!"
                else:
                    show mt surprise panama pioneer at cright
                    with dspr
                    mt "Я думаю, Двачевская и правда что-то затеяла!"
                mt "В общем, извиняйся перед Семёном!"
                dv "Ну ладно, извини..."
                mt "Вот так-то! Теперь пора бы и Шурика поискать!"
                hide mt with dissolve
                show dv angry pioneer at center
                with dspr
                dv "Так меня ещё не позорили..."
                play sound ds_sfx_psy
                emp "Она обиделась на тебя."
                play sound ds_sfx_psy
                aut "Только вот за что? Это же она тебя подставить пыталась!"
                dv "Прощай!"
    scene bg ext_house_of_dv_day
    with dissolve
    "Ты выходишь и направляешься искать Шурика дальше."
    $ disable_current_zone_ds_small()
    jump ds_day4_map

label ds_day4_dv_escaped:
    window show
    th "Теперь можно спокойно идти по своим делам или…"
    window hide
    menu:
        "Уйти прочь":
            window show
            th "Ну нафиг, пусть Двачевская облажается!"
            $ ds_lp['dv'] -= 1
            $ disable_current_zone_ds_small()
            jump ds_day4_map
        "Затаиться и ждать":
            window show
            th "Ладно, подожду."
    play sound ds_sfx_int
    lgc "Не просто же так она тебя здесь заперла?"
    "Тебе интересно выяснить это, и к тому же тебе просто интересно посмотреть на выражение лица Алисы, когда она увидит, что тебя нет."
    "Ты прячешься за кустами рядом с домиком и принимаешься ждать."
    with fade

    window show
    "Через некоторое время слышатся шаги."
    "К домику подходят Алиса и Ольга Дмитриевна."
    show dv normal pioneer far at cleft 
    show mt normal panama pioneer far at cright 
    with dissolve  
    dv "Сейчас всё сами увидите!"
    hide dv  with dissolve
    "Она открывает дверь и входит…"
    "Но буквально спустя пару секунд выскакивает обратно."
    window hide

    scene cg d4_dv_mt 
    with dissolve

    window show
    dv "Знаете, я это…"
    play sound ds_sfx_psy
    ine "На лице Алисы такое выражение, как будто она выиграла на соревнованиях по ловле ежей, пришла всем хвастаться медалью, но в последний момент узнала, что это совсем не олимпийский вид спорта."
    mt "Он испарился, получается?"
    hfl "Как хорошо, что я закрыл окно после того, как вылез!"
    dv "Да нет…{w} Тут, понимаете…"
    mt "Я всё понимаю, Двачевская!"
    mt "Что ты, что соседка твоя – постоянно одно и то же, одно и тоже! Сколько можно уже?!"
    dv "Но ведь правда!.."
    mt "Что правда, что? У тебя один рассказ лучше другого. Про Семёна в твоём домике, про приставания. Что ты придумываешь постоянно? Вообще ужас."
    play sound ds_sfx_psy
    emp "Алиса действительно расстроенна"
    play sound ds_sfx_psy
    aut "И, что ещё удивительнее, не пытается огрызаться."
    aut "С одной стороны, меня такая ситуация забавляла"
    emp "Но с другой – Двачевскую тебе всё же немного жаль."
    aut "Хотя сама заслужила..."
    emp "Или же нет?"
    window hide
    menu:
        "Показать себя":
            window show
            "Жалость к Алисе всё же пересиливает, и ты вылезаешь из кустов."
            scene bg ext_house_of_dv_day
            show mt angry panama pioneer at cright
            show dv guilty pioneer at cleft
            with dspr
            me "Позвольте, Ольга Дмитриевна... Алиса вас не обманывала..."
            show mt surprise panama pioneer at cright
            show dv angry pioneer at cleft
            with dspr
            mt "Семён?!"
            dv "Ага, всё-таки явился!"
            show mt angry panama pioneer at cright
            with dspr
            mt "Двачевская!"
            show dv sad pioneer at cleft
            with dspr
            "Алиса умолкает."
            show mt rage panama pioneer at cright
            with dspr
            mt "Между прочим, Алиса сказала, что ты залез в её домик, чтобы приставать к ней! Это тоже правда?!"
            window hide
            menu:
                "Подыграть Алисе":
                    window show
                    me "Ну... да... не удержался..."
                    show dv shocked pioneer at cleft
                    show mt shocked panama pioneer at cright
                    with dspr
                    "Алиса удивлена таким поворотом событий. Как и Ольга Дмитриевна."
                    mt "Ты... Ты... Ты понимаешь, насколько это серьёзное нарушение?!"
                    $ ds_lp['mt'] -= 2
                    $ ds_lp['dv'] += 1
                    $ ds_karma -= 10
                    show mt rage panama pioneer at cright
                    with dspr
                    mt "Да ты будешь выкинут из лагеря за такое! Я устрою тебе отвратительную характеристику! Ни в комсомол, никуда тебя не возьмут!"
                    show dv guilty pioneer at cleft
                    with dspr
                    dv "Позвольте, Ольга Дмитриевна..."
                    mt "Не сейчас, Двачевская!"
                    show dv angry pioneer at cleft
                    with dspr
                    dv "Семён НЕ ВИНОВАТ!"
                    show mt surprise panama pioneer at cright
                    with dspr
                    mt "В смысле?!"
                    dv "Мы с Семёном решили... вас разыграть."
                    mt "Вы... вы вообще нормальные?!"
                    mt "Это серьёзное дело, а вы так шутите?!"
                    me "Извините."
                    show mt normal panama pioneer at cright
                    with dspr
                    mt "Ладно, главное - что домогательств не было. А сейчас мне надо Шурика искать, и вам было бы неплохо."
                    if ds_dv_door_broken:
                        show mt angry panama pioneer at cright
                        with dspr
                        mt "Хотя нет, подождите... а дверь кто сломал?!"
                        window hide
                        menu:
                            "Признать свою вину":
                                window show
                                me "Это я... извините..."
                                mt "Ясно... пришлю Бориса Александровича починить дверь!"
                                mt "А ты Шурика ищи!"
                                $ ds_lp['mt'] -= 1
                            "Свалить вину на Алису":
                                window show
                                me "Это всё она!"
                                mt "Сказки мне тут не рассказывай! Она всё же девушка и не могла сломать дверь!"
                                mt "А вот ты - мог!"
                                $ ds_lp['mt'] -= 2
                                $ ds_lp['dv'] -= 2
                                $ ds_karma -= 5
                                mt "Ладно, Борис Александрович починит дверь."
                                mt "А ты Шурика ищи!"
                    hide mt
                    show dv guilty pioneer at center
                    with dspr
                    dv "Спасибо... что всё же не подставил меня..."
                    me "Ну так ведь..."
                    "Ты хотел сказать что-нибудь ободряющее, но она решает обрезать диалог."
                    show dv grin pioneer at center
                    with dspr
                    dv "Бывай!"
                    hide dv with dissolve
                    "А ты идёшь искать Шурика дальше."
                    $ disable_current_zone_ds_small()
                    jump ds_day4_map
                "Оправдываться":
                    window show
                    me "Она всё врёт! Я ничего с ней не делал!"
                    show dv guilty pioneer at cleft
                    with dspr
                    if ds_karma <= -50:
                        show mt rage panama pioneer at cright
                        with dspr
                        mt "А знаешь, мне что-то не верится! Ты тут уже натворил делов!"
                        dv "Ну да, я вас обманула..."
                        show mt surprise panama pioneer at cright
                        with dspr
                        "Ольга Дмитриевна удивлена ходом Алисы. Как и ты."
                        mt "В смысле?"
                        dv "Ну, я хотела над ним подшутить..."
                        show mt angry panama pioneer at cright
                        with dspr
                        mt "Подшутить?! Ты понимаешь, что то, что ты выдвинула - серьёзное обвинение?!"
                        mt "За такое как минимум выкидывают из лагеря! С волчьим билетом!"
                    else:
                        show mt surprise panama pioneer at cright
                        with dspr
                        mt "Ну вот и я так думаю, что Двачевская пытается меня надуть!"
                    mt "В общем, извиняйся перед Семёном!"
                    dv "Ну ладно, извини..."
                    mt "Вот так-то! Теперь пора бы и Шурика поискать!"
                    hide mt with dissolve
                    show dv angry pioneer at center
                    with dspr
                    dv "Так меня ещё не позорили..."
                    play sound ds_sfx_psy
                    emp "Она обиделась на тебя."
                    play sound ds_sfx_psy
                    aut "Только вот за что? Это же она тебя подставить пыталась!"
                    dv "Прощай!"
        "Изобразить мимокрокодила" (skill='savoir_faire', level=lvl_medium):
            if ds_last_skillcheck.result():
                window show
                scene ext_house_of_dv_day 
                with dissolve
                play sound sfx_bush_leaves 
                play sound2 ds_sfx_mot
                svf "{result}Ты начинаешь продвигаться по кустам как можно аккуратней чтобы не издавать слишком громких звуков."
                svf "Вскоре тебе удаётся уйти на достаточное расстояние от пионерки с вожатой, чтобы вылезти из кустов незамеченным."
                "Ты прячешься за одним из домиков."
                th "Вроде получилось.{w} Они меня не заметили."
                svf "Да твоим навыкам стэлса может позавидовать даже самый тихий убийца."
                
                svf "А теперь начинается самое интересное..."
                "Ты направляешься в сторону девушек, делая вид, что ты тут мимо проходил."
                show dv sad pioneer at cleft
                show mt angry panama pioneer at cright
                with dissolve
                me "Что за шум, а драки нет?"
                show dv rage pioneer at cleft
                show mt surprise panama pioneer at cright
                with dspr
                dv "Вот он! Я же вам говорила. Ну сейчас ты у меня попляшешь."
                me "О чём это ты? Я не понимаю?"
                mt "Семён, что ты здесь делаешь?"
                me "Как это что? Шурика ищу. Вы же сами меня попросили об этом."
                dv "Да? А в моём домике ты тоже Шурика искал? "
                me "Какой домик? Я только снаружи искал.{w} К сожалению, пока ничего так и не нашёл."
                play sound ds_sfx_int
                dra "Ты вздохнул так, что Никулин, Вицин и прочие Моргуновы отдыхают в сторонке."
                "Алиса вне себя от злости, а ты стараешься изо всех сил быть серьёзным и не взорваться смехом."
                dv "Да врёт он! Хватит прикидываться дурачком. Говори правду иначе..."
                show mt angry panama pioneer at cright with dspr
                mt "Хватит!"
                "Ольга Дмитриевна повышает голос."
                show dv sad pioneer at cleft with dspr
                mt "Прекращай этот цирк! Лучше бы взяла с Семёна пример и помогла бы нам в поисках Шурика, вместо того чтобы всякой чепухой заниматься и людей клеветать."
                th "Ого, я польщён, но примеров с меня лучше не брать – хуже будет."
                me "Не знаю, что у вас тут произошло, но мне надо идти. У меня ещё незаконченные дела есть."
                me "И Алису сильно не ругайте. Ну решила пошутить, с кем не бывает?"
                show dv guilty pioneer at cleft
                show mt normal panama pioneer at cright
                with dspr
                "Ольга Дмитриевна кивает, а Алиса одаривает тебя брезгливым взглядом, после чего отворачивается в сторону."
                $ ds_lp['mt'] += 1
                $ ds_lp['dv'] -= 1
                stop music fadeout 3
                window hide
                play ambience ambience_camp_center_day fadein 2
                scene bg ext_houses_day 
                with fade
                window show
                "Ты направляешься в сторону площади, чтобы выплеснуть все свои эмоции смеха, которые ты сдерживал."
                th "Не ожидал, что всё так удачно выйдет."
                th "Надеюсь Алиса не будет сильно обижаться на меня."
                play sound ds_sfx_psy
                emp "Будет, это как пить дать."
                play sound ds_sfx_psy
                aut "Хотя это ты должен обижаться на неё, ведь она тебя чуть не подставила перед Ольгой Дмитриевной."
                play sound ds_sfx_psy
                sug "А вожатая ведь реально тебе поверила. Ещё ненароком подумает, что ты стал образцовым пионером."
                play sound ds_sfx_psy
                vol "С другой стороны, заручиться поддержкой Ольги Дмитриевны тоже не плохо."
                window hide
                $ disable_current_zone_ds_small()
                $ ds_d4_places_remain -= 1
                jump ds_day4_map
            else:
                window show
                scene ext_house_of_dv_day 
                with dissolve
                play sound sfx_bush_leaves 
                play sound2 ds_sfx_mot
                svf "{result}Ты начинаешь продвигаться по кустам, но шелест листьев тебя выдаёт."
                show mt angry panama pioneer at center
                with dissolve
                mt "А кто это у нас тут в кустах прячется?! Может, Алиса меня и не обманывала?!"
                show dv angry pioneer far at left
                with dissolve
                dv "Вот, я же говорила!"
                mt "Да я уже поняла! Ну, что ты скажешь?"
                $ ds_karma -= 5
                window hide
                menu:
                    "Подыграть Алисе":
                        window show
                        me "Ну... да... не удержался..."
                        show dv shocked pioneer at cleft
                        show mt shocked panama pioneer at cright
                        with dspr
                        "Алиса удивлена таким поворотом событий."
                        mt "Ты... Ты... Ты понимаешь, насколько это серьёзное нарушение?!"
                        $ ds_lp['mt'] -= 2
                        $ ds_lp['dv'] += 1
                        $ ds_karma -= 10
                        show mt rage panama pioneer at cright
                        with dspr
                        mt "Да ты будешь выкинут из лагеря за такое! Я устрою тебе отвратительную характеристику! Ни в комсомол, никуда тебя не возьмут!"
                        show dv guilty pioneer at cleft
                        with dspr
                        dv "Позвольте, Ольга Дмитриевна..."
                        mt "Не сейчас, Двачевская!"
                        show dv angry pioneer at cleft
                        with dspr
                        dv "Семён НЕ ВИНОВАТ!"
                        show mt surprise panama pioneer at cright
                        with dspr
                        mt "В смысле?!"
                        dv "Мы с Семёном решили... вас разыграть."
                        mt "Вы... вы вообще нормальные?!"
                        mt "Это серьёзное дело, а вы так шутите?!"
                        me "Извините."
                        show mt normal panama pioneer at cright
                        with dspr
                        mt "Ладно, главное - что домогательств не было. А сейчас мне надо Шурика искать, и вам было бы неплохо."
                        if ds_dv_door_broken:
                            show mt angry panama pioneer at cright
                            with dspr
                            mt "Хотя нет, подождите... а дверь кто сломал?!"
                            window hide
                            menu:
                                "Признать свою вину":
                                    window show
                                    me "Это я... извините..."
                                    mt "Ясно... пришлю Бориса Александровича починить дверь!"
                                    mt "А ты Шурика ищи!"
                                    $ ds_lp['mt'] -= 1
                                "Свалить вину на Алису":
                                    window show
                                    me "Это всё она!"
                                    mt "Сказки мне тут не рассказывай! Она всё же девушка и не могла сломать дверь!"
                                    mt "А вот ты - мог!"
                                    $ ds_lp['mt'] -= 2
                                    $ ds_lp['dv'] -= 1
                                    $ ds_karma -= 5
                                    mt "Ладно, Борис Александрович починит дверь."
                                    mt "А ты Шурика ищи!"
                        hide mt
                        show dv guilty pioneer at center
                        with dspr
                        dv "Спасибо... что всё же не подставил меня..."
                        me "Ну так ведь..."
                        "Ты хотел сказать что-нибудь ободряющее, но она решает обрезать диалог."
                        show dv grin pioneer at center
                        with dspr
                        dv "Бывай!"
                        hide dv with dissolve
                        "А ты идёшь искать Шурика дальше."
                        $ disable_current_zone_ds_small()
                        jump ds_day4_map
                    "Оправдываться":
                        window show
                        me "Она всё врёт! Я ничего с ней не делал!"
                        show dv guilty pioneer at cleft
                        with dspr
                        if ds_karma <= -50:
                            show mt rage panama pioneer at cright
                            with dspr
                            mt "А знаешь, мне что-то не верится! Ты тут уже натворил делов!"
                            dv "Ну да, я вас обманула..."
                            show mt surprise panama pioneer at cright
                            with dspr
                            "Ольга Дмитриевна удивлена ходом Алисы. Как и ты."
                            mt "В смысле?"
                            dv "Ну, я хотела над ним подшутить..."
                            mt "Подшутить?! Ты понимаешь, что то, что ты выдвинула - серьёзное обвинение?!"
                            mt "За такое как минимум выкидывают из лагеря! С волчьим билетом!"
                        else:
                            show mt surprise panama pioneer at cright
                            with dspr
                            mt "Ну вот и я так думаю, что Двачевская пытается меня надуть!"
                        mt "В общем, извиняйся перед Семёном!"
                        dv "Ну ладно, извини..."
                        mt "Вот так-то! Теперь пора бы и Шурика поискать!"
                        hide mt with dissolve
                        show dv angry pioneer at center
                        with dspr
                        dv "Так меня ещё не позорили..."
                        play sound ds_sfx_psy
                        emp "Она обиделась на тебя."
                        play sound ds_sfx_psy
                        aut "Только вот за что? Это же она тебя подставить пыталась!"
                        dv "Прощай!"
        "Сидеть дальше":
            window show
            $ ds_lp['dv'] -= 1
            $ persistent.sprite_time = "day"
            scene bg ext_house_of_dv_day 
            with dissolve
            show dv rage pioneer far at center    with dissolve
            window show
            "Наконец вожатая заканчивает отчитывать её и ушла."
            "Алиса вне себя от злости.{w} Она сжимает кулаки и вся тряслась, а её лицо так краснеет, что, кажется, она сейчас лопнет."
            "Ты сидишь в кустах и тихо посмеиваешься."
            play sound ds_sfx_int
            lgc "Но что же она замышляла?"
            window hide
            menu:
                "Выйти из укрытия" (skill='volition', level=lvl_legendary):
                    if ds_last_skillcheck.result():
                        window show
                        play sound ds_sfx_psy
                        vol "{result}Ты плюёшь на страх быть поколоченным и выходишь из своего укрытия."
                        
                        me "И что же ты хотела показать вожатой?{w} Меня?"
                        show dv surprise pioneer at center   with dissolve
                        "Алиса оборачивается и недоуменно смотрит в мою сторону."
                        "Впрочем, через секунду недоумение сменяется негодованием."
                        show dv rage pioneer at center   with dspr
                        dv "Ты! Ты!"

                        stop music fadeout 3

                        me "А что я?"

                        play ambience ambience_camp_center_day fadein 3

                        "Она немного смягчается."

                        if ds_bet_dv:
                            if ds_tour_result < 3:
                                show dv smile pioneer at center   with dspr
                                dv "Хотела тебе вернуть должок."
                                me "Какой это?"
                                dv "Ты же мне проспорил.{w} Вот я и хотела показать вожатой, как ты меня домогаешься."
                                play sound ds_sfx_int
                                lgc "Интересно, что такого криминального могла бы найти Ольга Дмитриевна в данной ситуации?"
                                play sound ds_sfx_int
                                rhe "Но речь не о том…"

                            if ds_tour_result == 3:
                                show dv angry pioneer at center   with dspr
                                dv "Хотела тебе отомстить!"
                                me "За что это?"
                                play sound ds_sfx_int
                                lgc "Действительно, что ты такого сделал этой девочке, чтобы мне ещё и мстить?"
                                dv "За то, что обыграл меня в карты!"
                                th "Важный повод!{w} Без сомнения…"
                                play sound ds_sfx_psy
                                aut "То есть ты проиграл бы - она бы тебя обвинила, так как спор, а ты выиграл - и она всё равно обвиняет!"
                                play sound ds_sfx_int
                                lgc "Парадокс брадобрея напоминает. Только наоборот."
                                play sound ds_sfx_int
                                enc "Или гамбит Ксанатоса - независимо от ситуации, человек остаётся в выигрыше."

                            me "Ясно…"

                        else:
                            dv "Потому что ты слабак!"
                            me "Это почему же?"
                            dv "Потому что побоялся со мной тогда поспорить!"
                            me "Когда это?"
                            dv "Когда в карты играли!"
                            play sound ds_sfx_int
                            lgc "Серьёзная причина…"
                            play sound ds_sfx_psy
                            aut "По всей видимости, она засчитала это как проигрыш в споре."
                            me "Да уж…"

                        me "Может быть, мне стоит перед тобой извиниться?"
                        show dv sad pioneer at center   with dspr
                        dv "Да иди ты!"
                    else:
                        window show
                        play sound ds_sfx_psy
                        vol "{result}Тебе слишком страшно - Алиса ведь может и поколотить тебя за такие приколы."
                        
                "Сидеть дальше":
                    window show
    

    play sound sfx_slam_door_campus

    hide dv  with dissolve
    "Она, хлопнув дверью, заходит в домик."
    play sound ds_sfx_psy
    aut "Ты совсем не обижаешься на Алису."
    play sound ds_sfx_int
    lgc "В конце концов, от неё вполне можно было ожидать чего-нибудь подобного."
    play sound ds_sfx_psy
    vol "Тем более всё обходится в общем-то без последствий."
    vol "И даже более того – удача была на твоей стороне, – её растерянный и смущённый вид доставил тебе массу удовольствия."
    "Посмеиваясь, ты удаляешься от домика Алисы, который чуть не стал для тебя смертельной ловушкой."
    window hide

    $ disable_current_zone_ds_small()
    $ ds_d4_places_remain -= 1
    jump ds_day4_map

label ds_day4_busstop:
    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day 
    with dissolve

    window show
    play sound ds_sfx_int
    lgc "Возможно, Шурик, как и ты, решил сбежать из этого лагеря и стоит ждёт автобус номер 410."
    lgc "Это вполне может оказаться правдой, если он тоже попал сюда {i}случайно{/i}."
    lgc "Хотя вероятность этого крайне мала."
    th "Но чем чёрт не шутит!"
    th "Тем более вдруг автобус и правда приедет…"

    stop ambience fadeout 2
    play sound ds_sfx_psy
    vol "Впрочем, в это верится с трудом."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_camp_entrance_day 
    with dissolve

    play ambience ambience_camp_entrance_day fadein 3

    window show
    "Предсказуемо, никого ты не видишь."
    "В итоге, подождав на остановке пару минут, ты убедился, что ни Шурика, ни кого другого здесь не встречу, и идёшь назад в лагерь."

    play sound sfx_body_bump

    with vpunch
    "Однако из ворот кто-то выскакивает и мгновенно врезается в тебя."
    if ds_skill_list['savoir_faire'].check(lvl_easy, passive=True).result():
        play sound ds_sfx_mot
        svf "{result}Удар был не сильный, так что ты лишь немного ошатнулся."
    else:
        play sound ds_sfx_mot
        svf "{result}Хоть удар был несильный, но ты всё равно свалился на землю."
    show mi shocked pioneer close at center    with dissolve   
    "Перед тобой стоит Мику и потирает ушибленный лоб."
    window hide
    menu:
        "Извиниться":
            window show
            me "Ой, извини…"
            show mi normal pioneer at center
            with dspr
            mi "Да ничего! Это я во всём виновата! Понимаешь, я в музыкальный кружок шла, но задумалась над новой песней… Знаешь, текст придумывала, музыку… И сама не заметила, как здесь оказалась."
            mi "Так что ты не извиняйся!"
        "Наехать на Мику":
            window show
            me "Что ты тут ходишь и не смотришь вперёд себя?!"
            show mi sad pioneer at center
            with dspr
            mi "Ой, извини! Это я во всём виновата! Понимаешь, я в музыкальный кружок шла, но задумалась над новой песней… Знаешь, текст придумывала, музыку… И сама не заметила, как здесь оказалась."
    play sound ds_sfx_int
    rhe "Количество слов в минуту превышает лимит восприятия твоего мозга."
    window hide
    menu:
        "Ретироваться":
            window show
            "Ты пытаешься в спешном порядке ретироваться."
            me "Да, да… Мне идти пора… Такие дела…"
            show mi shy pioneer at center   with dspr
            mi "Подожди!"
            "Хотелось, как обычно, уйти, не дослушав её, но Мику хватает тебя за руку."
            if not ds_skill_list['composure'].check(lvl_challenging, passive=True).result():
                com "{result}От её прикосновения у тебя мурашки бегут по коже, а перед глазами проносятся картины мучительной казни через риторику."
        "Слушать дальше":
            window show
    show mi serious pioneer at center   with dspr
    mi "Можешь мне помочь немного, пожалуйста? Совсем чуть-чуть?"
    play sound ds_sfx_psy
    vol "Подобное в твои планы никак не входит."
    me "Да я бы с радостью, но мне…"
    mi "Ну пожалуйста!"
    play sound ds_sfx_psy
    emp "Мику смотрит на меня такими щенячьими глазами, что твоё сердце начало таять."
    "Руку при этом она и не думает отпускать."
    me "А в чём, собственно, помощь заключается?"
    show mi normal pioneer at center   with dspr
    mi "Подыграешь мне! А то у меня так совсем не получается сочинять! Я могу петь. Или играть. Или петь. А вместе почему-то не получается."
    play sound ds_sfx_psy
    aut "Даже у человека-оркестра есть свои слабости."
    mi "А если не умеешь - я тебе покажу! Пойдём!"
    window hide

    menu:
        "Согласиться":
            window show
            play sound ds_sfx_psy
            vol "С другой стороны, ты же ничего не теряешь!"
            me "Давай!"
            $ ds_lp['mi'] += 1
        "Отказаться":
            window show
            me "Знаешь, мне Шурика надо искать, и всё такое..."
            show mi upset pioneer at center   with dspr
            "Мику разочарованно смотрит на меня."
            mi "Ну совсем чуть-чуть!"
            window hide
            menu:
                "Смириться":
                    window show
                    "Ты не находишься, что ответить..."
                "Вырваться" (skill='physical_instrument', level=lvl_medium):
                    if ds_last_skillcheck.result():
                        window show
                        play sound ds_sfx_fys
                        phi "{result}Дёрни резко рукой - что может быть проще?"
                        "Ты так и делаешь. Тебе удаётся вырвать руку у Мику."
                        play sound sfx_bodyfall_1
                        "Но ценой того, что Мику падает на землю."
                        
                        show mi dontlike pioneer at center
                        with dspr
                        mi "Ты чего? Зачем так делать? Не хочешь - как хочешь, бака!"
                        $ ds_lp['mi'] -= 2
                        hide mi with dissolve
                        "И Мику уходит, задрав нос."
                        "А ты направляешься искать Шурика дальше."
                        $ ds_d4_places_remain -= 1
                        $ disable_current_zone_ds_small()
                        jump ds_day4_map
                    else:
                        window show
                        play sound ds_sfx_fys
                        phi "{result}На удивление, захват такой хрупкой девушки как Мику оказывается очень даже сильным! Ты ничего поделать не можешь."
                        
                        $ ds_morale.damage()
                "Настоять на отказе" (skill='suggestion', level=lvl_up_medium):
                    if ds_last_skillcheck.result():
                        play sound ds_sfx_psy
                        sug "{result}Просто откажись - куда уж проще? Тебе надо искать Шурика."
                        me "Вожатая велела мне Шурика искать, и если я не послушаюсь - мне будет плохо!"
                        show mi sad pioneer at center
                        with dspr
                        mi "Жаль... ну ладно, заходи как-нибудь, Семён-кун."
                        hide mi with dissolve
                        $ ds_lp['mi'] -= 1
                        "Мику уходит, а ты направляешься искать Шурика дальше."
                        $ ds_d4_places_remain -= 1
                        $ disable_current_zone_ds_small()
                        jump ds_day4_map
                    else:
                        play sound ds_sfx_psy
                        sug "{result}Похоже, Мику не отступит до последнего..."
                        me "Но..."
                        mi "Ну пожа-а-алуйста!"
                        play sound ds_sfx_psy
                        vol "Нет, ты не можешь ей отказать."

    show mi happy pioneer at center   with dspr
    "Она тащит тебя за собой."

    stop ambience fadeout 2

    th "Ну, в конце концов, ничего страшного не происходит!"
    play sound ds_sfx_fys
    hfl "Наверное…"
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_musclub_day 
    with dissolve

    play ambience ambience_music_club_day fadein 3

    show mi normal pioneer at center   with dissolve
    window show
    "Через минуту вы уже стоите в здании музыкального кружка."
    "Мику берёт гитару."
    mi "Вот, смотри!"
    window hide

    scene cg d4_mi_guitar 
    with dissolve

    play sound sfx_miku_song_learn1

    window show
    "Она садится и начинает играть."
    "Ты следишь за её руками.{w} Мелодия кажется довольно простой."
    play sound ds_sfx_mot
    inf "Да и повторить её было как будто несложно."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_musclub_day 
    with dissolve

    show mi normal pioneer at center   with dissolve
    window show
    mi "Запомнил?"
    me "Вроде да."
    mi "Давай тогда попробуем!"

    window hide
    menu:
        "Попробовать" (skill='interfacing', level=lvl_challenging, modifiers=[('ds_played_guitar', 2, 'Уже играл на гитаре')]):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_mot
                inf "{result}Ты берёшь гитару и точно отыгрываешь нужную партию."
                show mi smile pioneer at center
                with dspr
                mi "Ой, какой ты молодец, Семён-кун, классненько получилось!"
                $ ds_morale.up()
                
            else:
                window show
                play sound sfx_miku_song_learn2
                play sound2 ds_sfx_mot
                inf "{result}Ты берёшь гитару и начинаешь играть."
                inf "Получается не очень…"
                mi "Давай ещё раз покажу."
                window hide

                scene cg d4_mi_guitar 
                with dissolve

                play sound sfx_miku_song_learn1

                window show
                "Она играет куда лучше тебя."
                "Глядя на Мику, ты задумываешься."
                play sound ds_sfx_int
                con "Конечно, она не в меру разговорчивая, рассеянная и слишком наивная…{w} Но при этом талантом к музыке её бог не обделил."
                window hide

                $ persistent.sprite_time = "day"
                scene bg int_musclub_day 
                with dissolve

                show mi normal pioneer at center   with dissolve
                window show
                mi "Попробуй ещё."
                inf "Во второй раз у тебя получается куда лучше."
                show mi smile pioneer at center   with dspr
                mi "Вот! Уже похоже!"
                "Она улыбается."
                inf "На самом деле, ничего сложного – надо просто повторять одни и те же ноты."
                inf "Главное – не сбиться!"
    show mi normal pioneer at center   with dspr
    mi "Давай! На счёт три!"
    me "Давай…"
    mi "Раз! Два! Три!"
    window hide

    scene cg d4_mi_sing 
    with dissolve

    play music music_list["miku_song_voice"] fadein 1

    window show
    play sound ds_sfx_int
    enc "Это песня на японском."
    play sound ds_sfx_psy
    ine "Честно говоря, ты ничего не понял, но поёт Мику хорошо.{w} Даже отлично!"
    ine "Она всю душу вкладывает в каждую ноту, в каждое слово."
    ine "Да, пожалуй, музыка – это именно то, чем ей стоит заниматься в жизни."
    ine "Кажется, не она выбрала музыку, а музыка – её…"
    vol "За последние полчаса ты взглянул на Мику совсем по-другому."

    stop music fadeout 2

    window hide

    $ persistent.sprite_time = "day"
    scene bg int_musclub_day 
    with dissolve

    show mi smile pioneer at center   with dissolve
    window show
    mi "Ой, спасибо тебе! Понравилось? У меня наконец-то получилось, а то одной как-то не очень. Я либо с текста сбивалась, либо мимо струн попадала. А с тобой всё отлично вышло! Спасибо тебе!"
    mi "Знаешь, у тебя определённо талант!{w} Так вот сразу взять и сыграть…"
    play sound ds_sfx_psy
    vol "Нет, похоже, мнение о ней ты изменил рановато."
    window hide
    menu:
        "Поблагодарить за песню":
            window show
            me "Спасибо тебе за песню!{w} Мне пора, увидимся!"
            mi "И тебе…"
            window hide
        "Подбодрить Мику" (skill='empathy', level=lvl_up_medium):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_psy
                emp "{result}Нужно что-нибудь сказать. Ты чувствуешь, что она в глубине души расстроена своей неудачей."
                me "Ничего страшного. Ты умеешь и сочинять текст, и музыку писать, и играть на куче инструментов! Я никого кроме тебя не знаю, кто так умеет! Ты умница!"
                show mi happy pioneer at center
                with dspr
                mi "Ты правда так считаешь?"
                me "Да!"
                mi "Я очень рада это слышать! Так искренне меня ещё никто не хвалил, Семён-кун! Точнее, хвалили, но это было давно, а теперь только аплодисменты фанатов."
                $ ds_lp['mi'] += 2
            else:
                window show
                play sound ds_sfx_psy
                emp "{result}Да какой в этом смысл? Её и так восхваляют все, как певицу!"
                th "Тоже верно..."
                me "Ну, я пойду. У тебя хорошо получается."
                mi "Ну ладно..."
        "Отвергнуть талант":
            window show
            me "Да нет у меня никакого таланта! Просто случайно получилось."
            show mi sad pioneer at center
            with dspr
            mi "Мне кажется, ты себя недооцениваешь, Семён-кун. Очень сильно недооцениваешь! Нужно быть увереннее в себе!"
    "Ты собираешься уходить, но Мику собирается тебе сказать что-то ещё."
    window hide
    menu:
        "Дослушать":
            window show
            "Ты останавливаешься в двери."
            show mi normal pioneer at center
            with dspr
            mi "Слушай, ты же знаешь про концерт, который будет в конце смены?"
            if ds_after_lunch_who == 'mi':
                play sound ds_sfx_mot
                res "Она же тебе и рассказывала вчера про него!"
            elif ds_member['music']:
                play sound ds_sfx_mot
                res "Тебе же говорили об этом, когда ты записался в музклуб."
            me "Ну... да..."
            show mi smile pioneer at center
            with dspr
            mi "Нам нужен бас-гитарист! А у тебя так хорошо получается! Поучаствуй, пожалуйста!"
            window hide
            menu:
                "Согласиться":
                    window show
                    me "Конечно!"
                    show mi happy pioneer at center
                    with dspr
                    mi "Отлично! Тогда нам надо будет с завтрашнего дня начать репетировать!"
                    $ ds_lp['mi'] += 1
                    me "Ладно..."
                "Отказаться":
                    window show
                    me "Нет, я как-то не готов..."
                    show mi sad pioneer at center
                    with dspr
                    mi "А чего так?"
                    me "Не готов. Только испорчу вам концерт. Да и у меня планы... другие!"
                    mi "Очень жаль... Ну ладно, пока..."
                    $ ds_lp['mi'] -= 1
                "Ответить неопределённо":
                    window show
                    me "Я ещё подумаю..."
                    mi "Хорошо, только завтра обязательно скажи, нужно же уже репетировать!"
                    me "Хорошо..."
            "На этом ты выходишь."
            window hide

            stop ambience fadeout 3

            $ persistent.sprite_time = "day"
            scene bg ext_musclub_day 
            with dissolve

            window show
        "Выйти":
            stop ambience fadeout 3

            $ persistent.sprite_time = "day"
            scene bg ext_musclub_day 
            with dissolve

            window show
            "Остаток фразы остаётся за дверью."
    "Ты опираешься о стену музыкального кружка и облегчённо вздыхаешь."
    play sound ds_sfx_psy
    ine "Но песенка Мику всё ещё вертится у тебя в голове."
    window hide

    $ disable_current_zone_ds_small()
    $ ds_d4_places_remain -= 1
    jump ds_day4_map

label ds_day4_forest:
    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day 
    with dissolve

    window show
    play sound ds_sfx_int
    lgc "Ольга Дмитриевна с пионерами уже явно осмотрела весь лагерь."
    lgc "Можно сказать, прочесала вдоль и поперёк…"
    lgc "Поэтому искать Шурика, например, в столовой или на пляже глупо."
    lgc "Тем более в кружке кибернетики! Там был его второй дом.{w} А может, даже и первый."
    lgc "Поэтому самое разумное - осмотреть окрестный лес."
    play sound ds_sfx_psy
    vol "Только далеко заходить не стоит, иначе придётся искать и тебя."
    play sound ds_sfx_psy
    ine "Вообще, ты в своей жизни не так уж часто бывал на природе."
    ine "Разве что в детстве и юношестве ездил на дачу каждое лето.{w} Которая к тому же была рядом с городом."

    stop ambience fadeout 2

    ine "А в этом лагере, в этом мире, можно найти всё, чего ты так давно не видел: кромешная зелень, пение птиц и свежий воздух."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_path_day 
    with dissolve

    play ambience ambience_forest_day fadein 3

    window show
    "Ты выходишь на лесную полянку и садишься на пенёк."
    th "Как же здесь спокойно…"
    play sound ds_sfx_int
    lgc "И куда только этот Шурик запропастился?.."
    play sound ds_sfx_fys
    hfl "Хотя, с другой стороны, он мог исчезнуть и не по своей воле."
    lgc "Интересно только – всему виной та сила, которая забросила тебя сюда, или вмешалась какая-то местечковая чертовщина?"
    if ds_skill_list['perception'].check(lvl_trivial, passive=True).result():
        play sound ds_sfx_mot
        per_eye "{result}Трава передо мной зашевелилась."
        per_eye "Присмотревшись повнимательнее, ты видишь белку."
        per_eye "Она осторожно подобирается к тебе и смотрит на твои руки."
        play sound ds_sfx_int
        lgc "Наверное, привыкла, что её здесь кормят."
        me "Прости, животное, у меня ничего с собой нет…"
        "Конечно, белка не может тебя понять и продолжает просто сидеть, ожидая угощения."
        play sound ds_sfx_psy
        emp "Тебе становится даже несколько обидно, что в кармане не завалялось даже крошки хлеба."
        vol "Тебе стыдно смотреть ей в глаза, поэтому ты уходишь."

    stop ambience fadeout 3

    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_washstand_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "После нескольких минут плутаний ты выходишь к умывальникам."
    play sound ds_sfx_int
    lgc "Получается, что и в лесу его нет.{w} По крайней мере в ближайших окрестностях."
    play sound ds_sfx_fys
    hfl "А идти дальше – попросту страшно."
    play sound ds_sfx_fys
    edr "Ты довольно сильно вспотел за время поисков. Возможно, тебе следует ополоснуться."
    window hide
    menu:
        "Умыться":
            window show
        "Отбросить мысль":
            window show
            th "Не время! Надо искать же!"
            "И ты идёшь дальше."
            $ ds_d4_places_remain -= 1
            $ disable_current_zone_ds_small()
            jump ds_day4_map
    "Ты подходишь к умывальникам, снимаешь рубашку, чтобы немного ополоснуться."
    "Однако это оказывается не так просто."
    play sound ds_sfx_mot
    svf "В раковину залезть явно не получится, а тут нет даже ковшика…"
    play sound ds_sfx_mot
    per_hea "Шаги! Сзади!"
    "Ты оборачиваешься."
    show el normal pioneer far at center    with dissolve   
    "По дорожке в твою сторону идёт Электроник."
    show el normal pioneer at center   with dissolve
    el "Шурика искал?"
    me "Да…{w} А ты?"
    el "И я…"
    window hide
    menu ds_day4_el_dialogue:
        set ds_menuset
        "Cпросить про его предположения":
            window show
            me "Слушай, ты же его лучше знаешь, куда он мог пойти?"
            show el upset pioneer at center   with dspr
            el "Не имею ни малейшего понятия."
            play sound ds_sfx_int
            lgc "Все свои предположения он явно уже проверил. Вопрос бессмысленный."
            window hide
            jump ds_day4_el_dialogue
        "Усомниться в необходимости паники":
            window show
            me "Да уж…{w} Просто я не очень понимаю, зачем разводить такую панику? Ночью же он был с тобой в домике? То есть его нет совсем недолго…{w} Может, погулять пошёл?"
            show el angry pioneer at center   with dspr
            el "Ты просто не знаешь Шурика!"
            el "Он фанатик своего дела!{w} Робототехника и кибернетика – это его жизнь. Таких людей – один на миллион! Нет, на миллиард! Его талант не знает границ! Я восхищаюсь им! Это стальной человек!"
            el "Нет, даже победитовый!"
            if ds_skill_list['inland_empire'].check(lvl_easy, passive=True).result():
                play sound ds_sfx_psy
                ine "{result}В эту минуту он напоминает тебе Гитлера, читающего речь перед многотысячной толпой."
                ine "Да и жестикуляция соответствовала."
            me "Ладно…{w} И что с того?"
            show el shocked pioneer at center   with dspr
            el "Как это что? Ты не понимаешь?"
            me "Нет…"
            el "Он всё! Понимаешь, – ВСЁ! – свободное время проводит в нашем клубе!"
            me "То есть вот так пропасть для него странно?"
            el "Конечно!"
            show el normal pioneer at center   with dspr
            play sound ds_sfx_psy
            emp "Электроник, кажется, немного успокоился."
            me "Ладно…"
            window hide
            jump ds_day4_el_dialogue
        "Напомнить про старый лагерь" if ds_have_guess_sh:
            window show
            me "А в старый лагерь вы не ходили?"
            show el scared pioneer at center
            with dspr
            el "Я очень надеюсь, что он туда не пошёл! Это сумасшествие!"
            me "А что там такого?"
            el "Ну... он уже не менее десяти лет заброшен! Убиться там легче лёгкого."
            el "Да и слухи про него ходят страаашные!"
            el "Одна из легенд «Совёнка» гласит, что там живёт привидение молодой вожатой, которая влюбилась в пионера, но, не найдя взаимности, покончила с собой…"
            el "Но наука не допускает существования привидений, поэтому опасаться там нечего..."
            play sound ds_sfx_psy
            emp "Он говорит это очень неуверенно. Сам сомневается в том, что говорит."
            show el normal pioneer at center
            with dspr
            el "Короче, будем надеяться, что ему хватило благоразумия не идти туда!"
            play sound ds_sfx_int
            rhe "Он протараторил эти слова, пытаясь скрыть своё беспокойство."
            window hide
            jump ds_day4_el_dialogue
        "Приступить к мытью":
            window show
    "Ты вновь начинаешь осматривать раковины, пытаясь выяснить, как же тебе помыться."
    "Он пристально смотрит на тебя."
    el "Мыться собираешься?"
    me "Да не то чтобы…{w} Просто ополоснуться, а то жарко."
    el "Я вот тоже."
    "Он оглядывается."
    el "Эх, жаль ни ведра, ни ковшика нет. Не из чего облиться."
    play sound ds_sfx_int
    lgc "Cпасибо, капитан Очевидность!"
    play sound ds_sfx_int
    rhe "Такое ощущение, что он к чему-то тебя подводит. Вот только к чему?"
    show el smile pioneer at center   with dspr
    el "Тогда сделаем так…"
    "Он обходит умывальники и тянет один из кранов."
    "К твоему удивлению, его носик поднимается, и вода льётся уже не в раковину, а почти под прямым углом."
    play sound ds_sfx_mot
    svf "Так можно вполне помыться."
    window hide

    scene cg d4_el_wash 
    with dissolve

    stop ambience fadeout 2

    play music music_list["eternal_longing"] fadein 3

    window show
    "Электроник же тем временем снимает рубашку, а затем присаживается и, кажется, спускает шорты."
    "Точно ты сказать не можешь, так как он по пояс скрыт за умывальниками."
    window hide
    menu:
        "Заглянуть":
            window show
            "Ты решаешь проверить свою догадку и заглядываешь за умывальники."
            scene bg ext_washstand_day 
            show el normal naked at center
            with dissolve
            "Твоё преположение подтверждается - он стоит абсолютно голый."
            "Тебя он не замечает и продолжает настраивать кран."
            window hide
            menu:
                "Вернуться назад":
                    window show
                "Начать приставать":
                    window show
                    me "Эй, а может вместе помоемся?"
                    show el surprise naked at center
                    with dspr
                    el "В смысле?"
                    me "Ну, типа, чего нам стесняться? Мы же с тобой оба мужчины!"
                    show el smile naked at center
                    with dspr
                    el "А, ну давай!"
                    $ ds_lp['el'] += 1
                    $ ds_homo_traits += 1
        "Наблюдать дальше":
            window show
    "Он направляет струю на себя и начинает напевать себе под нос."
    el "Чисто-чисто моем трубочиста…"
    if ds_skill_list['rhetoric'].check(lvl_medium, passive=True).result():
        play sound ds_sfx_int
        rhe "{result}Для справки - одним из эвфемизмов, обозначающих тех мужчин, что по другим мужчинам - как раз «трубочисты»."
        play sound ds_sfx_psy
        vol "Эта информация тебя в определённом смысле шокирует. Ты стоишь на месте, не зная что делать."
        play sound ds_sfx_mot
        com "Похоже, он это заметил."
    else:
        "Тут он обращает на тебя внимание."
    el "Сейчас помоюсь и тебе место уступлю."
    if (ds_homo_traits == 2) and ds_skill_list['instinct'].check(lvl_medium, passive=True).result():
        play sound ds_sfx_fys
        ins "{result}Ну что - останешься на скучной светлой стороне, или примешь радужную?"
        window hide
        menu:
            "Принять мысль":
                window show
                th "Да! Нафиг девушек, с парнями лучше!"
                me "Да нет, давай вместе, {i}бок о бок{/i}, помоемся!"
                "С этими словами ты подходишь ближе к нему."
                $ ds_homo_traits += 1
                scene bg ext_washstand_day
                show el shocked naked at center
                with dspr
                play sound ds_sfx_mot
                com "Тут пришла очередь Электроника напрячься."
                play sound ds_sfx_psy
                emp "Но, кажется, ему понравилось. Он просто не решается это признать."
                play sound ds_sfx_fys
                ins "Конечно, понравилось!"
                el "Д-давай..."
                "Ты становишься рядом с ним, скинув с себя всё, и ополаскиваешься из одного крана."
                play sound ds_sfx_mot
                per_eye "Краем глаза ты видишь, как он к тебе присматривается. Да и ты тоже посматриваешь на него."
                $ ds_lp['el'] += 1
                $ ds_homo_traits += 1
                hide el with dissolve
                "Закончив мыться, ты одеваешься и уходишь искать Шурика дальше."
                $ disable_current_zone_ds_small()
                $ ds_d4_places_remain -= 1
                jump ds_day4_map
            "Отвергнуть мысль":
                window show
                th "Да, я останусь. Меня интересуют женщины, и никто больше!"
    play sound ds_sfx_mot
    com "Тебя аж передёрнуло!"
    me "Да нет, знаешь…{w} Я вспомнил, что у меня дела! Мне пора!"
    play sound ds_sfx_psy
    vol "При всех странностях Электроника таких наклонностей ты за ним не замечал."
    el "Ты чего?{w} В такой жаркий день помыться под холодной водой – самое лучшее удовольствие!"
    me "Не-не-не!{w} Так не пойдёт!{w} И вообще, мне пора уже."
    window hide

    stop music fadeout 3

    $ persistent.sprite_time = "day"
    scene bg ext_path_day 
    with dissolve

    window show
    "Ты быстро надеваешь рубашку и убегаешь обратно в лес."
    th "Интересно, что это на него нашло?.."
    window hide

    $ disable_current_zone_ds_small()
    $ ds_d4_places_remain -= 1
    jump ds_day4_map

label ds_day4_house_of_mt:
    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day 
    with dissolve

    window show
    play sound ds_sfx_int
    lgc "Но всё же это глупая затея."
    lgc "Если бы Шурик прятался где-то в лагере, его бы давно нашли (если, конечно, он сам бы того захотел)."

    stop ambience fadeout 2

    play sound ds_sfx_psy
    vol "Так что вряд ли тебе удастся чем-то им помочь."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_house_of_mt_day 
    with dissolve

    play ambience ambience_int_cabin_day fadein 3

    window show
    "С этими мыслями ты заходишь в домик и раскладываешься на кровати."
    vol "Если тебя здесь найдёт Ольга Дмитриевна, ничего хорошего не будет..."
    play sound ds_sfx_psy
    aut "Впрочем, это уже чересчур – тварь ты дрожащая или право имею?"
    vol "Да и делать тебе ничего не хочется."
    vol "День сегодня, как и все прошлые, жаркий, так что остаётся только лежать и ждать обеда."
    "Ты уже было задремал, как в дверь постучали."

    play sound sfx_knocking_door_outside

    window hide
    menu:
        "Притвориться отсутствующим":
            window show
            "Ты притаился в кровати, надеясь, что пронесёт."
            sl "Ольга Дмитриевна, вы тут?"
            play sound ds_sfx_mot
            per_hea "Это Славя."
            window hide
            menu:
                "Открыть дверь":
                    window show
                "Продолжить притворяться":
                    window show
                    per_hea "Ты слышишь, как Славя уходит."
                    jump ds_day4_day_sleep
        "Пригласить":
            window show
            me "Войдите."

    play sound sfx_open_door_2

    "На пороге стоит Славя."
    show sl normal pioneer at center   with dissolve
    sl "А Ольги Дмитриевны нет?"
    me "Нет."
    sl "А ты что делаешь?"
    play sound ds_sfx_psy
    emp "Она спрашивает с некоторым недоверием."
    "Ты осматриваешь кровать и себя и думаешь, что ответить."
    window hide
    menu:
        "Сказать честно":
            window show
            me "Лежу…"
            sl "Это я вижу.{w} Но я слышала, что тебе Ольга Дмитриевна поручила искать Шурика."
        "Придумать полезное дело" (skill='drama', level=lvl_up_medium):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_int
                dra "{result}А давайте вы будете переписывать бумаги для вожатой! Тут как раз и реквезит в виде листочков удобно разложился."
                me "Да так, Ольга Дмитриевна велела переписать бумаги."
                show sl serious pioneer at center
                with dspr
                sl "Да? А я слышала, что она поручила тебе Шурика искать."
                dra "Она раскусила нас! Эта проницательная женщина раскусила нас!"
                
            else:
                window show
                play sound ds_sfx_int
                dra "{result}Шурика ищете, мессир, чего ж ещё хотите?"
                me "А... да Шурика ищу!"
                show sl surprise pioneer at center
                with dspr
                sl "В домике Ольги Дмитриевны?"
                me "Ну да, и вообще, хочешь спрятать вещь - положи её на самое видное место."
                show sl laugh pioneer at center
                with dspr
                sl "И как поиски?"
                play sound ds_sfx_psy
                aut "Она откровенно над тобой потешается."
                dra "Шоу должно продолжаться!"
                
                window hide
                menu:
                    "Начать изображать поиски":
                        window show
                        "Ты залезаешь в шкаф, изображая там поиски Шурика."
                        me "Тут его нет... {w}и тут нет... {w}и тут тоже нет!"
                        show sl serious pioneer at center
                        with dspr
                        sl "Так, ладно, посмеялись и хватит."
                        sl "Я же правильно понимаю, что Ольга Дмитриевна поручила тебе его поиски?"
                    "Сдаться":
                        window show
                        me "Ну ладно, не ищу я его..."
                        show sl serious pioneer at center
                        with dspr
                        sl "А ведь Ольга Дмитриевна поручила его искать, так?"
                    "Ответить, что отлично":
                        window show
                        me "Отлично идут, я уже напал на след!"
                        show sl laugh pioneer at center
                        with dspr
                        sl "И куда же они ведут?"
                        me "Эм... {w}ну... {w}туда..."
                        show sl serious pioneer at center
                        with dspr
                        sl "Так, ладно, посмеялись и хватит."
                        sl "Я же правильно понимаю, что Ольга Дмитриевна поручила тебе его поиски?"
                    "Ответить, что плохо":
                        window show
                        me "Неважно..."
                        show sl smile pioneer at center
                        with dspr
                        sl "А хочешь, расскажу, почему?"
                        play sound ds_sfx_int
                        rhe "Готовься к гневной тираде..."
                        me "Ну..."
                        show sl serious pioneer at center
                        with dspr
                        sl "Потому что ты ничего не делаешь и обманываешь!"
                        sl "Тебе же поручили искать Шурика?"
        "Отказаться отвечать":
            window show
            me "Да ничем. И вообще не твоё дело!"
            sl "Ну да. Только ведь, я слышала, Ольга Дмитриевна тебе поручила Шурика искать?"
    window hide
    menu:
        "Подтвердить":
            window show
            me "Ну, да…"
            sl "И?"
        "Отрицать":
            window show
            me "Нет, нет, никто мне ничего не поручал!"
            sl "Значит, я тебе поручаю от имени Ольги Дмитриевны!"
    window hide
    menu:
        "Усомниться в необходимости поисков":
            window show
            me "Какой смысл?{w} Она уже наверняка весь лагерь вверх дном перевернула."
            me "Да и прошло не так много времени.{w} Зачем панику разводить?"
            show sl serious pioneer at center   with dspr
            sl "Всякое бывает…"
        "Промолчать":
            window show
    "Славя задумчиво смотрит на тебя."
    sl "Вставай."
    play sound ds_sfx_fys
    edr "Тебя настолько разморило, что даже мысль о том, что сейчас придётся куда-то идти, пугает."
    me "А это обязательно?"
    show sl smile pioneer at center   with dspr
    sl "Да!"

    stop ambience fadeout 2

    window hide
    menu:
        "Смириться":
            window show
            me "Ладно..."
        "Подняться с энтузиазмом":
            window show
            me "Всегда готов!"
            $ ds_lp['sl'] += 1
        "Отказаться" (skill='authority', level=lvl_medium):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_psy
                aut "{result}Тебе нужен этот Шурик? Если он Славе так сдался - пусть ищет сама."
                me "Нет, не обязательно! Тебе так важен Шурик - ты и ищи, а я поспать хочу!"
                show sl angry pioneer at center
                with dspr
                sl "Ну не хочешь - как хочешь!"
                hide sl with dissolve
                "И Славя уходит."
                $ ds_lp['sl'] -= 1
                
                jump ds_day4_day_sleep
            else:
                window show
                play sound ds_sfx_psy
                aut "{result}Ты считаешь неправильным отказывать Славе."
                
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    show sl normal pioneer at center   with dissolve
    window show
    "Ты встаёшь и вместе с ней выходишь на улицу."
    jump ds_day4_find_with_sl

label ds_day4_day_sleep:
    show blink
    scene black with dissolve
    "Ты вновь укладываешься на кровать, закрываешь глаза и засыпаешь."
    call ds_day4_day_dream
    mt "Семён! Уже обедать пора!"
    hide blink
    show unblink
    scene bg int_house_of_mt_day
    show mt angry pioneer at center
    with dissolve
    me "Уже иду..."
    "Ты встаёшь, одеваешься и следуешь за Ольгой Дмитриевной к столовой."
    jump ds_day4_lunch

label ds_day4_find_with_sl:
    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    show sl normal pioneer at center   with dissolve
    "Некоторое время вы просто стоите на пороге, и греетесь в лучах летнего солнца."
    play sound ds_sfx_fys
    edr "Хотя ты скорее просто жаришься..."
    window hide
    menu:
        "Спросить, куда пойдём":
            window show
            me "Куда пойдём?"
            sl "Надо поискать везде."
        "Ждать молча":
            window show
            sl "В общем, нам надо поискать везде!"

    th "Отличная идея… Просто отличная!"
    window hide

    stop ambience fadeout 3

    show sl smile pioneer at center
    with dspr
    sl "Значит, смотри, мы с тобой обойдём библиотеку, столовую, медпункт, спортплощадку, и, наконец, посмотрим в кружке!"

    $ persistent.sprite_time = "day"
    scene bg int_library_day 
    with dissolve

    play ambience ambience_library_day fadein 3

    play music music_list["take_me_beautifully"] fadein 3

    "Первым пунктом вашего маршрута идёт библиотека."
    "Славя подходит к Жене, сидящей за столом, и о чём-то с ней заговаривает."
    if ds_hit_mz:
        show sl surprise pioneer at cleft
        show mz rage glasses pioneer at cright
        with dissolve
        mz "А чего тут этот делает?!"
        sl "Семён-то? Он со мной."
        mz "А ты знаешь, как он сегодня меня, пока я спала, головой - и об стол?!"
        show sl scared2 pioneer at cleft
        with dspr
        sl "Как?! Зачем ты так, Семён?!"
        $ ds_lp['sl'] -= 2
        $ ds_karma -= 20
        me "Да разбудить хотел, нужна мне была Женя..."
        mz "И что же там такого неотложного было, что надо было меня избивать?!"
        mz "Я сегодня ясно сказала - иди вон!"
        window hide
        menu:
            "Выйти":
                window show
                "Ты решаешь не испытывать судьбу и выходишь."
            "Продолжить стоять":
                window show
                me "И никуда я не пойду!"
                show mz rage glasses pioneer at cright
                with dspr
                mz "Пойдёшь, я сказала!"
                $ ds_lp['mz'] -= 1
                if ds_skill_list['reaction_speed'].check(lvl_medium, passive=True).result():
                    play sound ds_sfx_mot
                    res "{result}Берегись! Она начинает присматривать книгу, чтобы метнуть в тебя."
                    "Ты рефлекторно отпрыгиваешь."
                else:
                    play sound sfx_punch_washstand
                    with flash_red
                    "Тебе по голове прилетает книгой."
                    if ds_skill_list['pain_threshold'].check(lvl_up_medium, passive=True).result():
                        play sound ds_sfx_fys
                        pat "{result}Для тебя это пустяки, конечно..."
                        "Но ты отходишь, чтобы не получить сильнее."
                    else:
                        play sound ds_sfx_fys
                        pat "{result}Больно! У тебя на голове вылезает шишка."
                        $ ds_health.damage()
                    show sl scared pioneer close at center
                    with dspr
                    sl "Ты как, Семён?"
                    window hide
                    menu:
                        "Начать возмущаться":
                            window show
                            me "Да Женя вообще уже потеряла границы!"
                            show mz rage glasses pioneer at right
                            with dspr
                            mz "Я границы потеряла?! А кто меня бил об стол головой?!"
                            play sound ds_sfx_int
                            rhe "Личные? И что же у Жени со Славей {i}личного{/i}?"
                            show sl serious pioneer close at center
                            with dspr
                            sl "Так, угомонились оба! Семён, выйди, дай нам договорить."
                        "Сказать, что всё нормально":
                            window show
                            me "Не переживай за меня, я чувствую себя нормально..."
                            show sl smile pioneer close at center
                            with dspr
                            sl "Вот и хорошо! Выйди, пожалуйста."
                        "Начать «умирать»" (skill='drama', level=lvl_medium):
                            if ds_last_skillcheck.result():
                                play sound ds_sfx_int
                                dra "{result}Ну что, готовы во всех красках передать, насколько сильно вас ударила Женя?"
                                me "Ой, у меня, наверное, сотрясение мозга, я умираю."
                                "И ты показательно падаешь на пол, произнося это нарочито наигранным голосом."
                                show mz rage glasses pioneer at right
                                with dspr
                                mz "Что это ты тут за цирк устроил?!"
                                show sl serious pioneer close at center
                                with dspr
                                sl "Похоже, сильно тебя по голове приложили..."
                                sl "Так, сейчас, выйди, я приду."
                                dra "Артистов всегда недооценивают при жизни!"
                                
                            else:
                                play sound ds_sfx_int
                                dra "{result}Нет, смысла нет. Вы уже простояли спокойно немало времени, мессир."
                                me "Ну... голова болит..."
                                show sl serious pioneer close at center
                                with dspr
                                sl "Подожди тогда, я сейчас приду!"
                                
                        "Извиниться перед Женей":
                            window show
                            me "Извини, Жень..."
                            show mz sceptic glasses pioneer at right
                            with dspr
                            mz "Вот то-то же, вы, мужики, только силу и понимаете!"
                            sl "Не сейчас, Женя!"
                            sl "В общем, Семён, выйди, пожалуйста."
                    play sound ds_sfx_psy
                    vol "Тебе ничего иного не остаётся - снова получить книгой ты явно не хочешь."
        window hide
        scene bg ext_library_day
        with dissolve
        $ renpy.pause(2.0)
        window show
        show sl angry pioneer at center
        with dissolve
        sl "Я сейчас не буду разбираться насчёт твоих взаимоотношений с Женей - нам надо Шурика искать!"
    else:
        window hide
        menu:
            "Постоять в дверях":
                window show
                "Ты же просто стоишь в дверях и ждёшь."
                play sound ds_sfx_psy
                vol "У тебя нет никакого желания общаться с местной библиотекаршей."
            "Подслушать разговор":
                window show
                "Ты приближаешься к девушкам."
                show sl normal pioneer at cleft
                show mz bukal glasses pioneer at cright
                with dissolve
                sl "...да, я понимаю тебя, но..."
                show mz angry glasses pioneer at cright
                with dspr
                mz "А ты чего уши греешь?!"
                $ ds_lp['mz'] -= 1
                window hide
                menu:
                    "Отступить":
                        window show
                        me "Извините..."
                        "И ты отходишь."
                    "Отрицать":
                        window show
                        me "Я тут просто стою..."
                        mz "Вот и стой {i}там{/i} - в двери, а лучше за ней!"
                        me "Ладно..."
                    "Нагрубить":
                        window show
                        me "Хочу и подслушиваю!"
                        show mz rage glasses pioneer at cright
                        with dspr
                        mz "А я не хочу! Я со Славей говорю, а не с тобой!"
                        $ ds_lp['mz'] -= 1
                        if ds_skill_list['reaction_speed'].check(lvl_medium, passive=True).result():
                            play sound ds_sfx_mot
                            res "{result}Берегись! Она начинает присматривать книгу, чтобы метнуть в тебя."
                            "Ты рефлекторно отпрыгиваешь."
                        else:
                            play sound sfx_punch_washstand
                            with flash_red
                            "Тебе по голове прилетает книгой."
                            if ds_skill_list['pain_threshold'].check(lvl_up_medium, passive=True).result():
                                play sound ds_sfx_fys
                                pat "{result}Для тебя это пустяки, конечно..."
                                "Но ты отходишь, чтобы не получить сильнее."
                            else:
                                play sound ds_sfx_fys
                                pat "{result}Больно! У тебя на голове вылезает шишка."
                                $ ds_health.damage()
                            show sl scared pioneer close at center
                            with dspr
                            sl "Ты как, Семён?"
                            window hide
                            menu:
                                "Начать возмущаться":
                                    window show
                                    me "Да Женя вообще уже потеряла границы!"
                                    show mz rage glasses pioneer at right
                                    with dspr
                                    mz "Я границы потеряла?! А кто тут чужие личные разговоры подслушивает?!"
                                    play sound ds_sfx_int
                                    rhe "Личные? И что же у Жени со Славей {i}личного{/i}?"
                                    show sl serious pioneer close at center
                                    with dspr
                                    sl "Так, угомонились оба! Семён, постой тут, дай нам договорить."
                                "Сказать, что всё нормально":
                                    window show
                                    me "Не переживай за меня, я чувствую себя нормально..."
                                    show sl smile pioneer close at center
                                    with dspr
                                    sl "Вот и хорошо! Постой тут, пожалуйста."
                                "Начать «умирать»" (skill='drama', level=lvl_medium):
                                    if ds_last_skillcheck.result():
                                        play sound ds_sfx_int
                                        dra "{result}Ну что, готовы во всех красках передать, насколько сильно вас ударила Женя?"
                                        me "Ой, у меня, наверное, сотрясение мозга, я умираю."
                                        "И ты показательно падаешь на пол, произнося это нарочито наигранным голосом."
                                        show mz rage glasses pioneer at right
                                        with dspr
                                        mz "Что это ты тут за цирк устроил?!"
                                        show sl serious pioneer close at center
                                        with dspr
                                        sl "Похоже, сильно тебя по голове приложили..."
                                        sl "Так, сейчас, подожди тут, я вернусь."
                                        dra "Артистов всегда недооценивают при жизни!"
                                        
                                    else:
                                        play sound ds_sfx_int
                                        dra "{result}Нет, смысла нет. Вы уже простояли спокойно немало времени, мессир."
                                        me "Ну... голова болит..."
                                        show sl serious pioneer close at center
                                        with dspr
                                        sl "Подожди тогда, я сейчас вернусь!"
                                        
                                "Извиниться перед Женей":
                                    window show
                                    me "Извини, Жень..."
                                    show mz sceptic glasses pioneer at right
                                    with dspr
                                    mz "Вот то-то же, вы, мужики, только силу и понимаете!"
                                    sl "Не сейчас, Женя!"
                                    sl "В общем, Семён, постой тут, пожалуйста."
                            play sound ds_sfx_psy
                            vol "Тебе ничего иного не остаётся - снова получить книгой ты явно не хочешь."
                hide sl
                hide mz
                with dissolve
        "Через пару минут Славя возвращается к тебе."
        show sl normal pioneer at center   with dissolve
        me "И как?"
        sl "Нет…"
        "Она качает головой."
        play sound ds_sfx_int
        lgc "А чего, собственно, можно было ожидать?"

    stop ambience fadeout 3

    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_near_day 
    with dissolve

    window show
    "Столовая."
    play sound ds_sfx_int
    lgc "До обеда остаётся ещё порядком времени, так что не стоит ждать здесь привычной толпы пионеров."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_day 
    with dissolve

    play ambience ambience_dining_hall_empty fadein 3

    window show
    "Внутри так же пусто, как и снаружи."
    "Пока Славя разговаривает с поварихой, ты сидишь и крутишь в руках солонку."
    "Немного соли высыпается на стол."
    play sound ds_sfx_int
    enc "Плохая примета, между прочим - просыпать соль."
    window hide
    menu:
        "Проигнорировать":
            window show
            th "Если бы я верил в приметы, то наверняка бы расстроился…"
            play sound ds_sfx_mot
            com "Но так как ты не веришь - ты воспринимаешь это спокойно."
        "Подумать о последствиях" (skill='inland_empire', level=lvl_challenging):
            window show
            th "И что теперь будет? Мы не найдём Шурика?"
            window hide
            if ds_last_skillcheck.result():
                window show
                scene bg int_mine_room_red
                show prologue_dream
                with flash
                play music music_list["no_tresspassing"] fadein 3
                play sound ds_sfx_psy
                ine "{result}Хуже. Ты представляешь какое-то помещение. Давно заброшенное."
                ine "Почему-то тебе кажется, что тут прольётся кровь. Если ты ничего не предпримешь - прольётся."
                th "А не может ли тут быть Шурика?"
                ine "Может, он и тут. Может, он как раз тут лежит мёртвый. Или - он и есть тот {i}убийца{/i}."
                play sound ds_sfx_mot
                com "Тебя бросает в дрожь."
                th "Шурик?!"
                ine "Это всё лишь твои безумные догадки. Может, его вообще тут нет!"
                th "А что это за место?"
                ine "Этого ты не знаешь. И знать не можешь - пока что."
                $ ds_had_vision_mines = True
                play sound ds_sfx_fys
                hfl "Как бы то ни было - сохраняй бдительность!"
                play sound ds_sfx_int
                lgc "Только откуда подобные места могут взяться в пионерлагере?"
                scene bg int_dining_hall_day 
                with fade
                stop music fadeout 3
            else:
                window show
                play sound ds_sfx_psy
                ine "{result}Может, и не найдёте."
            
        "Побежать к Славе":
            window show
            show sl surprise pioneer at center
            show ck normal at right
            with dissolve
            me "Всё, Славя, мы не найдём Шурика! Он пропал, всё пропало!"
            sl "Эм... что случилось, Семён?"
            me "Соль просыпал, а это к беде!"
            "Гробовое молчание."
            play sound ds_sfx_psy
            aut "Похоже, ты сильно пал в глазах Слави."
            show sl smile pioneer at center
            with dspr
            sl "Не переживай, это просто суеверие! Найдём мы Шурика, с ним всё будет хорошо!"
            sl "А теперь дай мне, пожалуйста, договорить."
            hide sl
            hide ck
            with dissolve
            play sound ds_sfx_psy
            vol "Ты отходишь в сторонку, сгорая от стыда."

    show sl normal pioneer at center   with dissolve
    "Как ни странно, его не оказалось и здесь."
    play sound ds_sfx_int
    lgc "Было бы удивительно, если бы она нашла его, скажем, в холодильнике…"

    stop ambience fadeout 3

    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_aidpost_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "Далее по плану идёт медпункт."
    window hide
    menu:
        "Подождать Славю":
            window show
            "Внутрь я решил не заходить и подождал Славю снаружи."
            "Результатов никаких."
        "Зайти со Славей":
            window show
            scene bg int_aidpost_day
            show cs shy medic3 at center
            show sl normal pioneer at right
            with dissolve
            cs "Здравствуй, пионер. Да ещё и с девушкой пришёл, я погляжу."
            play sound ds_sfx_int
            rhe "Началось в деревне утро..."
            play sound ds_sfx_fys
            ins "Да ладно тебе! Ты же и сам наверняка хочешь Славю!"
            show sl shy pioneer at right
            with dspr
            play sound ds_sfx_psy
            emp "А вот Славе от слов медсестры становится некомфортно."
            sl "Кхм... Извините, а вы Шурика не видели?"
            show cs sorrow medic3 at center
            with dspr
            cs "Никак нет, не видела. Надеюсь, с ним всё в порядке."
            rhe "Никак нельзя понять, говорит ли она это {i}pro forma{/i} или искренне."
            show sl normal pioneer at right
            with dspr
            sl "Ну ладно, мы тогда пошли, Виолетта Церновна."
            show cs badgirl medic4 at center
            with dspr
            cs "Если вдруг надумаете {i}повеселиться{/i} вдвоём - то приходите сюда, всё для вашей безопасности и комфорта."
            show sl shy4 pioneer at right
            with dspr
            sl "Обязательно..."
            me "До свидания..."
            "На этой ноте вы выходите."
            scene bg ext_aidpost_day
            with dissolve
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_playground_day 
    with dissolve

    window show
    "На спортивной площадке пионеры играют в футбол."
    play sound ds_sfx_int
    lgc "Шурику затеряться среди них было бы проблематично."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_clubs_day 
    with dissolve

    show sl normal pioneer at center   with dissolve
    window show
    "Наконец, вы подошли к зданию кружков."
    play sound ds_sfx_int
    lgc "Зачем? {w}Даже нет, не так - нахрена? {w}Тут Шурика бы точно нашли уже!"
    window hide
    menu:
        "Последовать за Славей":
            pass
        "Усомниться":
            window show
            me "Ты считаешь, что он может быть тут? Мне кажется, это первое место, где его стоит искать…"
            sl "Зайдём."
            play sound ds_sfx_psy
            vol "Лучше не перечить. Попытка - не пытка."
            window hide
            menu:
                "Согласиться":
                    pass
                "Подождать на месте":
                    window show
                    me "Ну, как хочешь, а я подожду тут."
                    sl "Ладно..."
                    hide sl with dissolve
                    window hide
                    $ renpy.pause(2.0)
                    window show
                    show sl sad pioneer at center
                    with dspr
                    play sound ds_sfx_psy
                    emp "Славя выходит расстроенная. Очевидно, Шурика она не нашла."
                    jump ds_day4_find_with_sl_end

    stop ambience fadeout 3

    play sound sfx_open_door_clubs_2

    $ persistent.sprite_time = "day"
    scene bg int_clubs_male_day 
    with dissolve

    show sl normal pioneer at center   with dissolve
    window show
    "Внутри никого нет."
    hide sl  with dissolve
    "Славя открывает дверь в соседнюю комнату и заходит."
    window hide
    menu:
        "Последовать за Славей":
            window show
            "Ты следуешь за ней."
            window hide

            $ persistent.sprite_time = "sunset"
            scene bg int_clubs_male2_night 
            with dissolve

            window show
        "Подождать на месте":
            window show
            me "Я тебя тут подожду!"
            "Тишина тебе ответ."
            show sl sad pioneer at center
            with dspr
            play sound ds_sfx_psy
            emp "Славя выходит расстроенная. Очевидно, Шурика она не нашла."
    jump ds_day4_find_with_sl_end

label ds_day4_find_with_sl_end:
    play sound ds_sfx_int
    lgc "Это всё же крайне глупая затея."
    lgc "Тем более странно то, что инициатива исходит от Слави."
    lgc "Ответственность там, все дела…{w} Но очевидно же, что его нет в лагере!"
    th "В конце концов, не играет же он с нами в прятки?"
    show sl normal pioneer at center   with dissolve
    sl "И здесь нет…"
    window hide
    menu:
        "Спросить в лоб":
            window show
            me "А чего ты ожидала?{w} Что он в шкафу сидит?"
            show sl angry pioneer at center   with dspr
            sl "Ну!"
            play sound ds_sfx_psy
            emp "Кажется, ты её обидел."
            window hide
            menu:
                "Извиниться":
                    window show
                    me "Извини, извини…"
                "Продолжить":
                    window show
            me "Просто, серьёзно!"
            show sl serious pioneer at center   with dspr
            sl "Я понимаю…{w} Но надо ведь проверить все варианты."
            window hide
            menu ds_day4_sl_dialogue:
                set ds_menuset
                "Спросить мнение Слави":
                    window show
                    me "Слушай, а ты-то что думаешь?"
                    show sl normal pioneer at center   with dspr
                    sl "Насчёт исчезновения Шурика?"
                    me "Да."
                    show sl smile pioneer at center   with dspr
                    sl "Может быть, он гулял в лесу и его там поймал Леший."
                    "Она смеётся."
                    window hide
                    menu:
                        "Посмеяться с ней":
                            window show
                            "Ты смеёшься вместе с ней."
                            show sl normal pioneer at center
                            with dspr
                            sl "Но вообще не время для шуток."
                        "Отреагировать серьёзно":
                            window show
                            me "Неправдоподобно как-то…"
                            show sl normal pioneer at center   with dspr
                            sl "Да, наверное…{w} Сейчас не время для шуток!"
                "Поддержать Славю":
                    window show
                    me "Не грусти!{w} Найдётся он!"
                    show sl smile pioneer at center   with dspr
                    sl "Надеюсь…"
                    "Славя улыбается."
                    $ ds_lp['sl'] += 1
                "Попрощаться":
                    window show
                    me "Увидимся."
    hide sl  with dissolve
    "Она уходит, а ты ещё некоторое время стоишь и думаешь о поисках."

    stop music fadeout 3

    $ disable_current_zone_ds_small()
    $ ds_d4_places_remain -= 1
    jump ds_day4_map

label ds_day4_library:
    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day 
    with dissolve

    play sound ds_sfx_int
    lgc "А если Шурик потерялся в библиотеке?"
    play sound ds_sfx_psy
    vol "Нет, идея дурацкая. Как и все эти поиски Шурика."
    play sound ds_sfx_mot
    svf "Хорошо спрятаться можно в библиотеке."
    "Быстрым шагом ты туда и направляешься."

    stop ambience fadeout 3
    $ persistent.sprite_time = "day"
    scene bg ext_library_day
    with dissolve2
    $ renpy.pause(1)
    play sound sfx_open_door_clubs_2
    scene bg int_library_day 
    with dissolve2
    
    play music music_list["trapped_in_dreams"] fadein 1
    window show
    "В библиотеке пусто."
    play sound ds_sfx_mot
    svf "Идеально. Чёрта с два тебя тут кто-нибудь отыщет."
    play sound ds_sfx_mot
    per_eye "В углу комнаты ты видишь Женю в положении полусидя-полулёжа."
    window hide

    scene cg d2_micu_lib 
    with dissolve

    window show
    "Женя мирно посапывает."
    window hide
    menu:
        "Разбудить" (skill='physical_instrument', level=lvl_medium):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_fys
                phi "{result}Действуй наверняка. Нужно очень сильное воздействие."
                "Ты берёшь её за голову, приподнимаешь и шлёпаешь о стол."
                play sound sfx_table_hit
                scene bg int_library_day
                show mz rage pioneer at center
                with dissolve
                mz "ЧТО ЭТО ЗА ДЕЛА?!"
                phi "Очевидно, ты добился желаемого."
                
                play sound ds_sfx_psy
                vol "Но какой ценой?"
                mz "Я, значит, сплю спокойно, никого не трогаю, а ты меня об стол! А если бы убил меня?!"
                mz "Иди вон!"
                $ ds_lp['mz'] -= 5
                "Она тянется к книге потяжелее, чтобы бросить её в тебя."
                play sound ds_sfx_psy
                vol "Ты благоразумно решаешь выйти."
                scene bg ext_library_day
                with dissolve
                mz "И чтобы я тебя тут больше не видела!"
                play sound sfx_close_door_1
                "После этого она захлопывает дверь прямо перед твоим носом."
                "А ты прикидываешь, куда пойти дальше."
                $ ds_hit_mz = True
                $ disable_current_zone_ds_small()
                $ ds_d4_places_remain -= 1
                jump ds_day4_map
            else:
                window show
                play sound ds_sfx_fys
                phi "{result}Ты трясёшь её за плечо - но безрезультатно. А на большее у тебя не хватает сил."
                
                "Тебе остаётся только ждать."
        "Подождать":
            window show
    
    play ambience ambience_library_day fadein 3
    
    $ persistent.sprite_time = "day"
    scene bg int_library_day 
    with dissolve

    window show
    play sound ds_sfx_int
    lgc "Что можно делать в библиотеке? Читать книги, конечно же!"
    window hide
    menu:
        "Почитать":
            window show
            $ ds_reading_books = True
        "Посидеть тихо":
            window show
            "Ты усаживаешься рядом с Женей и принимаешься ждать."
        "Уйти":
            window show
            th "Нет, я тут подохну со скуки!"
            scene bg ext_library_day
            with dissolve
            "И ты максимально тихо выходишь."
            $ ds_d4_places_remain -= 1
            $ disable_current_zone_ds_small()
            jump ds_day4_map
    if ds_reading_books:
        "Ты берёшь с полки первую попавшуюся книгу."
        play sound ds_sfx_mot
        per_eye "Корней Чуковский - Собрание стихов."
        window hide
        menu:
            "Прочесть":
                window show
                "Ты открываешь примерно на середине и начинаешь читать."

                book "У меня зазвонил телефон."
                book " - Кто говорит?"
                book " - Слон."
                book " - Откуда?"
                book " - От верблюда."
                book " - Что вам надо?"
                book " - Шоколада."
                book " - Для кого?"
                book " - Для сына моего."
                book " - А много ли прислать?"
                book " - Да пудов этак пять"
                book "Или шесть:"
                book "Больше ему не съесть,"
                book "Он у меня еще маленький!"

                play sound ds_sfx_psy
                vol "Чем ты занимаешься вообще?{w} Нет, спасибо."
                if ds_skill_list['conceptualization'].check(lvl_easy, passive=True).result():
                    play sound ds_sfx_int
                    con "{result}Забавно: этот диалог из стиха тебе чем-то напомнил Женю."
            "Поискать ещё":
                window show
                play sound ds_sfx_psy
        vol "Поищи какую-нибудь более серьёзную литературу."
        "Ты тянешься за другой книгой."
        per_eye "Айзек Азимов - Конец Вечности."
        vol "Уже лучше."

        book "Инструкция объясняла ему, где он мог находиться в мире 482-го Столетия, а где - не мог, что ему разрешалось, а чего он должен был избегать любой ценой. Его присутствие было допустимо только там и тогда, где оно не представляло угрозы для Реальности."
        book "482-е Столетие пришлось не по душе Харлану. Оно нисколько не походило на его суровый и аскетический век. Этика и мораль в том виде, как их понимал Харлан, не существовали. Это была эпоха грубых материальных наслаждений с многочисленными признаками матриархата. Семья не признавалась юридически и пары вступали в сожительство и расходились по взаимному согласию, кроме которого их ничто не связывало."
        book "Существовали сотни причин, по которым это общество внушало Харлану отвращение, и он мечтал в душе об Изменении. Ему не раз приходило в голову, что одним только своим присутствием в этом Столетии он, человек из другого Времени, может вызвать \"вилку\" и направить историю по новому пути. Если бы ему удалось своим присутствием в какой-то определенной критической точке оказать достаточно сильное влияние на естественный ход событий, то возникла бы новая линия развития, бывшая до тех пор неосуществленной вероятностью, и миллионы ищущих наслаждений женщин превратились бы в любящих и преданных жен и матерей."
        book "Они жили бы в новой Реальности с новыми воспоминаниями и ни во сне, ни наяву не могли бы ни вспомнить, ни вообразить, что их жизнь когда-то была совершенно иной!"
        book "К несчастью, поступить так - значило нарушить Инструкцию. Даже если бы Харлан решился на это неслыханное преступление, случайное воздействие могло изменить Реальность самым неожиданным образом. Она могла бы стать еще хуже. Только кропотливый анализ и тщательные Вычисления могли предсказать истинный характер Изменения Реальности."

        play sound ds_sfx_int
        con "Прочитанное тебя настолько вдохновляет, что ты с головой погружаешься в книгу."
        window hide
        $ renpy.pause(2)
        window show
        play sound sfx_wood_floor_squeak
        play sound2 ds_sfx_mot
        per_hea "Ты слышишь скрип половиц за своей спиной."
        show mz smile glasses pioneer at center with dissolve
        "За тобой стоит Женя и разглядывает меня."
        mz "Что делаем?"
        play sound ds_sfx_mot
        com "Не теряйся: это просто вопрос."
        window hide
        menu:
            "Ищешь Шурика":
                window show
                me "Шурика ищем."
                show mz bukal glasses pioneer at center with dspr
                "Ей потребовалось некоторое время, чтобы вникнуть."
                show mz fun glasses pioneer at center with dspr
                mz "Ну раз так, удачи. Я, кстати, на 113-ой странице видела кого-то похожего на него."
                if ds_skill_list['logic'].check(lvl_trivial, passive=True).result():
                    play sound ds_sfx_int
                    lgc "{result}Капитан Очевидность подсказывает, что она шутит над тобой."
                    window hide
                    menu:
                        "Принять всерьёз":
                            window show
                            me "Правда?! Надо проверить!"
                            show mz laugh glasses pioneer at center
                            with dspr
                            "Ты начинаешь перелистывать книгу под смех Жени."
                            mz "Какой ты забавный!"
                        "Отшутиться":
                            window show
                            me "До туда дойти ещё надо. Может и сбежит к тому времени оттуда."
                        "Обидеться":
                            window show
                            me "Да ну тебя! Я серьёзно!"
                            show mz confused glasses pioneer at center
                            with dspr
                            mz "Совсем шуток не понимаешь..."
                            $ ds_lp['mz'] -= 1
                else:
                    me "Правда? Надо проверить!"
                    show mz laugh glasses pioneer at center
                    with dspr
                    "Ты начинаешь перелистывать книгу под смех Жени."
                    mz "Какой ты забавный!"
            "Читаешь книгу":
                window show
                me "Да вот, читаю."
                show mz sceptic glasses pioneer at center
                with dspr
                mz "Правда? Ну ладно, читай."
            "Отказаться отвечать":
                window show
                me "Не скажу!"
                show mz angry glasses pioneer at center
                with dspr
                mz "Ну и не говори! Главное - меня не трогай и бардак не наводи!"
                $ ds_lp['mz'] -= 2
        hide mz with dissolve
        "Женя направляется обратно к своему столу. Ты смотришь обратно в книгу."
    else:
        show mz bukal glasses pioneer at center
        with dspr
        "Вскоре Женя просыпается."
        show mz angry glasses pioneer at center
        with dspr
        mz "Что ты тут, рядом со мной, делаешь, пока я сплю?! НЕ ТРОГАЙ МЕНЯ!"
        if ds_skill_list['empathy'].check(lvl_easy, passive=True).result():
            play sound ds_sfx_psy
            emp "Она явно приняла тебя за насильника."
        "Она хватает книгу и пытается... прикрыться ей."
        window hide
        menu:
            "Убедить, что ты не опасен" (skill='suggestion', level=lvl_legendary) if (ds_day3_evening_who == 'mz') and ds_last_skillcheck.result():
                if ds_last_skillcheck.result():
                    window show
                    play sound ds_sfx_psy
                    sug "{result}Напирай на то, что имей ты на неё... гхм, планы, ты бы уже осуществил их вчера. В лесу."
                    me "Слушай, я понимаю, что ты считаешь меня, как и всех мужчин, насильниками..."
                    me "Но я же тебя вчера и пальцем не тронул, хотя мы с тобой и в лес ходили - вот бы где я тебя мог бы изнасиловать."
                    show mz confused glasses pioneer at center
                    with dspr
                    "Женя задумалась над твоими словами."
                    sug "Уже успех."
                    mz "Ладно. Убедил. Пока оставайся тут."
                    $ ds_calmed_mz = True
                    
                else:
                    window show
                    play sound ds_sfx_psy
                    sug "{result}Да чего она выделывается? Ходила вчера с тобой - а сейчас ни-ни!"
                    me "Слушай, мы вчера гуляли, и я мог бы с тобой что-нибудь сделать, но не стал!"
                    show mz rage glasses pioneer at center
                    with dspr
                    mz "ТЫ МНЕ УГРОЖАЕШЬ ЕЩЁ?! Уйди! Уйди, уйди, уйди!"
                    play sound ds_sfx_psy
                    emp "Ты сделал только хуже своими формулировками."
                    
                    $ ds_lp['mz'] -= 1
            "Сказать, что ищешь Шурика":
                window show
                me "Успокойся, я просто Шурика ищу..."
                mz "Нет тут твоих Шуриков. Можешь идти!"
            "Сказать, что ищешь книгу":
                window show
                me "Да мне книга нужна какая-нибудь..."
                show mz bukal glasses pioneer at center
                with dspr
                mz "Какая?"
                me "Любая, мне просто заняться нечем!"
                hide mz with dissolve
                "Женя отходит к ближайшему шкафу, вытаскивает оттуда книгу и отдаёт тебе."
                show mz bukal glasses pioneer at center
                with dspr
                mz "Ладно, сиди тихо и читай."
                "С этими словами она уходит за стол."
                $ ds_reading_books = True
                $ ds_calmed_mz = True
            "Начать возмущаться":
                window show
                me "Ты чего на меня наезжаешь?! Я вообще тебя не трогаю!"
                mz "Вот и уйди, чтобы точно меня не тронуть!"
                $ ds_lp['mz'] -= 1
            "Отказаться отвечать":
                window show
        if not ds_calmed_mz:
            window hide
            menu:
                "Выйти":
                    window show
                    "Ты решаешь не испытывать судьбу и выходишь."
                "Продолжить стоять":
                    window show
                    me "И никуда я не пойду!"
                    show mz rage glasses pioneer at cright
                    with dspr
                    mz "Пойдёшь, я сказала!"
                    $ ds_lp['mz'] -= 1
                    if ds_skill_list['reaction_speed'].check(lvl_medium, passive=True).result():
                        play sound ds_sfx_mot
                        res "{result}Берегись! Она начинает присматривать книгу, чтобы метнуть в тебя."
                        "Ты рефлекторно отпрыгиваешь."
                    else:
                        play sound sfx_punch_washstand
                        with flash_red
                        "Тебе по голове прилетает книгой."
                        if ds_skill_list['pain_threshold'].check(lvl_up_medium, passive=True).result():
                            play sound ds_sfx_fys
                            pat "{result}Для тебя это пустяки, конечно..."
                            "Но ты отходишь, чтобы не получить сильнее."
                        else:
                            play sound ds_sfx_fys
                            pat "{result}Больно! У тебя на голове вылезает шишка."
                            $ ds_health.damage()
                        vol "Ты не хочешь повторять этот опыт и выходишь."
            scene bg ext_library_day
            with dissolve
            th "Куда теперь, раз тут мне не рады?"
            $ ds_d4_places_remain -= 1
            $ disable_current_zone_ds_small()
            jump ds_day4_map
    if ds_lp['mz'] >= 15:
        show mz hope glasses pioneer at center
        with dspr
        mz "Чай будешь?"
        window hide
        menu:
            "Согласиться":
                window show
                me "Кто же от чая откажется."
                $ ds_lp['mz'] += 1
                hide mz with dissolve
                "Женя наклоняется к своему столу, достаёт оттуда два стакана и выходит из библиотеки."
                if ds_reading_books:
                    "Ты же вновь обращаешься к книге."
                    
                    book " - Отлично. Для начала выкинь все это из головы. История, которую учат Времяне, лишена всякого смысла; она меняется с каждым Изменением Реальности. Сами они, разумеется, даже не подозревают об этом. Для каждой Реальности ее история кажется единственной. С Первобытной историей дело обстоит совершенно иначе. Собственно, в этом-то и заключается вся ее прелесть. Что бы мы ни делали. Первобытная история всегда остается неизменной. Колумб и Вашингтон, Шекспир и Герефорд - все они существуют."
                    book "Купер нерешительно улыбнулся. Он провел мизинцем по верхней губе, и Харлан заметил на ней темную полоску, словно Ученик отращивал усы."
                    book " - Скоро год, как я здесь, а все никак не могу... вполне привыкнуть."
                    book " - К чему именно?"
                    book " - К тому, что меня отделяют от дома пятьсот веков."
                    book " - Я и сам немногим ближе. Я ведь из 95-го."
                    book " - Вот и это тоже. Вы старше меня, но в другом смысле я старше вас на семнадцать веков. Я вполне могу оказаться вашим прапрапрапра- и так далее -дедушкой."
                    book " - Какое это имеет значение? Допустим, так оно и есть."
                    book " - Ну, уж знаете... с этим еще надо свыкнуться. - В  голосе Купера зазвучали мятежные нотки."
                    book " - Мы все в одинаковом положении, - сухо заметил Харлан и приступил к уроку."
                "Вскоре Женя возвращается."
                show mz normal glasses pioneer at center
                with dissolve

                if ds_day3_num_sugar==0:
                    mz "Тебе без сахара?"
                elif ds_day3_num_sugar==1:
                    mz "Тебе одну ложку сахара?"
                elif ds_day3_num_sugar==2:
                    mz "Тебе две ложки сахара?"
                elif ds_day3_num_sugar==3:
                    mz "Тебе три ложки сахара?"
                elif ds_day3_num_sugar==4:
                    mz "Тебе всю сахарницу высыпать в стакан?"
                    window hide
                    menu:
                        "Подтвердить":
                            window show
                            me "Да, давай!"
                            "Женя невозмутимо вбухивает весь сахар в стакан."
                            "Места для чая в итоге не остаётся."
                            show mz fun glasses pioneer at center
                            with dspr
                            mz "Ой, похоже, кто-то будет один сахар пить!"
                            show mz bukal glasses pioneer at center
                            with dspr
                            "Но, увидев непонимание на твоём лице, она начинает сгребать его обратно."
                        "Отказаться":
                            window show
                            me "Очень смешно."
                    mz "Четыре, правильно?"
                window hide
                menu:
                    "Подтвердить":
                        window show
                        me "Да."
                    "Попросить больше" if ds_day3_num_sugar != 0:
                        window show
                        me "А можно побольше?"
                        if ds_day3_num_sugar == 4:
                            show mz fun glasses pioneer at center
                            with dspr
                            mz "А кое-что не слипнется? Пять ложек - это многовато!"
                            play sound ds_sfx_int
                            rhe "Перевод: больше четырёх она не наложит - считает расточительством."
                            me "Ладно, давай четыре..."
                            mz "Как скажешь."
                        else:
                            mz "Ну ладно, мне не жалко."
                    "Попросить меньше" if ds_day3_num_sugar > 1:
                        window show
                        me "А можно поменьше?"
                        mz "Как скажешь."
                    "Попросить без сахара" if ds_day3_num_sugar != 0:
                        window show
                        me "Сегодня я как-то не хочу сахара..."
                        mz "Как скажешь."
                    "Попросить добавить сахар" if ds_day3_num_sugar == 0:
                        window show
                        me "Нет, давай с сахаром."
                        mz "Хорошо, мне сахара не жалко."
                show mz normal glasses pioneer at center with dissolve
                "Через некоторое время она приносит тебе стакан с чаем."
                hide mz with dissolve
                if ds_reading_books:
                    "Похлёбывая, ты начинаешь читать дальше."
                $ ds_having_tea_mz = True
            "Отказаться":
                window show
                me "Нет, спасибо."
                show mz bukal glasses pioneer at center
                with dspr
                mz "Ну, как хочешь, а я выпью."
                hide mz with dissolve
                "Она выходит."
                if ds_reading_books:
                    "Ты в это время вновь погружаешься в чтение."
    if ds_reading_books:
        book " - У тебя талант, мой мальчик. Рука мастера. Я жду от тебя великих дел. А пока мы займемся вот этим небольшим дельцем из 223-го. Ты был совершенно прав, утверждая, что достаточно заклинить муфту сцепления в двигателе. При этом действительно получается необходимая \"вилка\" без нежелательных побочных эффектов. Возьмешься заклинить сцепление?"
        book " - Слушаюсь, сэр."
        book "Так совершилось подлинное посвящение Харлана в Техники. После этого он уже не был просто человеком с розовой нашивкой на плече. Он изменил Реальность. За несколько минут, выкраденных из 223-го, он испортил двигатель, и в результате некий молодой человек не попал на лекцию по механике. Из-за этого так и не стал заниматься солнечными установками, и очень простое устройство не было изобретено в течение десяти критических лет."
        book "А в результате всего этого, как ни странно, война в 224-м была вычеркнута из Реальности."
        book "Разве это не было благом? И так ли уж важно, что какие-то личности изменились? Новые личности были такими же людьми, как и прежние, с таким же правом на жизнь. Чьи-то жизни стали короче, зато у большего числа людей они стали дольше и счастливее."
        book "Правда, великое литературное произведение, грандиозное создание человеческого разума и чувств, не было написано в новой Реальности, но разве несколько экземпляров этой книги не сохранились в библиотеках Вечности? И разве в новой Реальности не будут созданы иные великие творения искусства?"

        show mz bukal glasses pioneer at center with dissolve
        mz "Ну и как тебе?"
        "Женя опять неожиданно появляется за моей спиной."
        play sound ds_sfx_mot
        svf "Это профеcсиональный навык такой - тихо передвигаться?"
        play sound ds_sfx_int
        con "Ей бы в разведчики. Мало того, что никто не услышит и не заметит, так она ещё и до ручки доведёт кого угодно, если захочет."
        "Она тем временем глотает чай из своего стакана."
        if ds_having_tea_mz:
            "Ты делаешь то же самое."
        window hide
        menu:
            "Одобрить":
                window show
                me "Отлично. Всегда любил научную фантастику."
                show mz normal glasses pioneer at center
                with dspr
                mz "А я вот - не особо. Но главное, чтобы книга была хорошая."
            "Раскритиковать":
                window show
                me "Не, научная фантастика мне как-то не очень."
                show mz normal glasses pioneer at center
                with dspr
                mz "Соглашусь, однако. Но главное, чтобы книга была хорошая."
        play sound ds_sfx_int
        rhe "Это утверждение совершенно ни к чему не обязывает, его отвергать бессмысленно."
        me "Сложно не согласиться."
        window hide
        menu:
            "Спросить про её предпочтения":
                window show
                me "А про что ты больше любишь читать?"
                show mz bukal glasses pioneer at center with dspr
                mz "История."
                me "Какая-то определённая или..."
                mz "Вплоть до падения Римской империи."
                rhe "С Женей было разговаривать не легче, чем с Леной: те же самые короткие реплики из одного слова."
                con "Только если Лена это делает из-за стеснения и это выглядит мило..."
                play sound ds_sfx_psy
                sug "...то с Женей ситуация полностью противоположная."
                "Женя вдруг решила продолжить беседу."
                sug "Не иначе как твои мысли прочла!"
                show mz normal glasses pioneer at center with dspr
                mz "Всё таки, это - колыбель нашей цивилизации. Иногда читаешь истории оттуда и понимаешь, что совершенно ничего не изменилось."
                if ds_skill_list['encyclopedia'].check(lvl_medium, passive=True).result():
                    play sound ds_sfx_int
                    enc "{result}То-то же, они тут в своём пионерлагере собственное государство по Платону построили. Не удивительно, что ничего не изменилось."
                mz "Начинаешь лучше понимать, почему всё вокруг устроено так, а не иначе. С чего всё началось, чем люди вдохновлялись."
                if ds_skill_list['encyclopedia'].check(lvl_easy, passive=True).result():
                    play sound ds_sfx_int
                    enc "{result}Ты мало что понимаешь в этом. В твоей голове всплывает только история о Калигуле - императоре, который известен необычайной широтой и максимальным абсурдом своих непотребств."
                    sug "Женe этого лучше не рассказывать. Вряд ли она пребывает в эйфории истории древнего мира, но настолько сильно портить впечатление - не стоит."
                    window hide
                    menu:
                        "Сказать про Калигулу":
                            window show
                            me "Ага, например, некто Калигула очень вдохновляет."
                            mz "И это тоже. На ошибках прошлого, по идее, надо учиться. Жаль только, что история учит только тому, что ничему не учит."
                            enc "К сожалению - чистейшая правда."
                            $ ds_lp['mz'] += 1
                        "Промолчать":
                            window show
            "Промолчать":
                window show
    hide mz with dissolve
    stop music fadeout 2
    if ds_having_tea_mz :
        "Вы допиваете чай, после чего ты отдаёшь Жене стакан и она уносит его к своему столу."
    "Вдруг дверь в библиотеку распахнулась."
    show us normal pioneer far at center with dspr
    play music music_list["timid_girl"] fadein 2
    us "Вы чего тут сидите?"
    me "Что-то случилось?"
    show us surp2 pioneer at center with dspr
    us "Да!"
    me "Что?"
    show us surp1 pioneer at center with dspr
    us "Шурик пропал!"
    "Женя тихонько скрипит зубами."
    show us smile pioneer at center with dspr
    us "А ты почему его не ищешь?"
    show us smile pioneer far at center with dspr
    us "А я всё Ольге Дмитриевне расскажу."
    "Ульянка показывает язык и выбегает на улицу."
    hide us with dspr
    show mz normal glasses pioneer at cright with dspr
    play sound ds_sfx_int
    con "Возможно, Женя сможет тебя в библиотеке спрятать понадёжнее."
    window hide
    menu:
        "Пойти на выход":
            window show
            if ds_reading_books:
                "Ты быстрым шагом подходишь к Жене, отдал ей книгу и направляешься к выходу."
            else:
                "Ты направляешься к выходу."
            "Женя лишь сочувствующе вздохнула."
            hide mz with dissolve
            stop music fadeout 4
            play sound ds_sfx_psy
            vol "Смысла догонять Ульяну уже нет. Лучше смени место дислокации."
            
            $ disable_current_zone_ds_small()
            $ ds_d4_places_remain -= 1
            jump ds_day4_map
        "Побежать за Ульяной":
            window show
            "Ты выбегаешь за Ульяной."
            scene bg ext_library_day
            with dissolve
            "Но когда ты оказываешься на улице - Ульяны и след простыл."
            stop music fadeout 4
            play sound ds_sfx_psy
            vol "Смысла догонять Ульяну уже нет. Лучше смени место дислокации."
            
            $ disable_current_zone_ds_small()
            $ ds_d4_places_remain -= 1
            jump ds_day4_map
        "Попросить Женю спрятать":
            window show
            me "Жень, а у тебя в библиотеке нет, скажем так, потайных комнат?"
            show mz amazed glasses pioneer at center
            with dspr
            mz "Прекрасно понимаю твоё нежелание искать этого Шурика, так что помогу тебе."
            mz "Есть подвал библиотеки, можешь пересидеть там до обеда. Заодно осмотри книги там."
            window hide
            menu:
                "Принять":
                    window show
                    me "Отлично, подойдёт, спасибо!"
                    mz "Не за что, иди уже."
                "Отказаться":
                    window show
                    me "Ну нет, не такое тёмное же."
                    show mz bukal glasses pioneer at center
                    with dspr
                    mz "Тебе шашечки или ехать?"
                    me "Я хочу нормальное место укрытия!"
                    mz "Тогда не ко мне."
                    me "Ладно, пойду куда-нибудь..."
                    hide mz with dissolve
                    stop music fadeout 4
                    
                    $ disable_current_zone_ds_small()
                    $ ds_d4_places_remain -= 1
                    jump ds_day4_map
    stop music fadeout 4
    scene bg ds_int_library_basement
    with dissolve
    "Ты спускаешься в подвальное помещение. Тут сплошные шкафы книг - идеальное место для пряток."
    play sound ds_sfx_fys
    edr "Единственный его недостаток - слишком уж тёмное. Тебя начинает клонить в сон."
    play sound ds_sfx_psy
    vol "А впрочем, чего ты теряешь? Тебе же надо провести время!"
    th "Вот и я так думаю..."
    show blink
    scene black with dissolve
    "Ты закрываешь глаза и засыпаешь."
    call ds_day4_day_dream
    mz "Подъём, обед уже!"
    hide blink
    show unblink
    scene bg ds_int_library_basement
    with dissolve
    me "Уже иду."
    scene bg int_library_day
    with dissolve
    "Ты вылезаешь и выдвигаешься в сторону столовой."
    jump ds_day4_lunch

label ds_day4_day_dream:
    scene bg ds_church_entrance
    with dissolve2
    play music ds_church_theme
    "Ты оказываешь в какой-то пещере. Перед тобой дверь."
    play sound ds_sfx_mot
    per_eye "Символы! Ты видишь какие-то символы."
    play sound ds_sfx_int
    vic "Увы, нет, ты не Роберт Лэнгдон и не в состоянии разгадать их значение."
    play sound ds_sfx_psy
    ine "{i}Пока{/i} не в состоянии."
    me "И что мне с этим делать?"
    window hide
    menu:
        "Вглядеться в символы" (skill='logic', level=lvl_challenging):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_int
                lgc "{result}Ну, давай посмотрим."
                lgc "Вверху - солнце. Солнце. Жёлтый. Пшеница. {w}Славя."
                lgc "Слева - нота. Музыка. {w}Мику."
                lgc "Cправа - молния... Что она может значить?"
                play sound ds_sfx_int
                enc "Молния - знак имиджборды Двач."
                lgc "Двач. Двачевская. Алиса Двачевская."
                lgc "А что до остальных... ты их даже толком рассмотреть не можешь."
                me "Так а причём тут Алиса, Мику и Славя?"
                arb "Зайди внутрь - и, быть может, поймёшь."
            else:
                window show
                play sound ds_sfx_int
                lgc "{result}Нет, ты никакой связи не видишь."
                arb "Потому что тебе пора зайти внутрь. Тогда, быть может, поймёшь."
        "Идти вперёд":
            window show
    "Ты идёшь к двери, берёшь её за ручку. Она не заперта, так что ты имеешь возможность туда зайти."
    scene bg ds_church
    with dissolve
    play sound ds_sfx_fys
    pat "Тебя ослепляет яркий свет."
    play sound ds_sfx_mot
    per_eye "Однако, ты можешь разглядеть очертания... церкви?"
    play sound ds_sfx_int
    vic "Да, это совершенно точно церковь."
    me "Церковь? А... разве я не в атеистическом СССР?"
    arb "Ты прежде всего во сне, балда!"
    me "И что это за церковь?"
    show dv rage pioneer at center
    with dissolve
    me "Алиса... это ты?"
    arb "Она тебе не ответит. Это порождение твоего подсознания."
    lim "Застывшее в эмоции, наиболее прочно с ней ассоциированной."
    hide dv with dissolve
    me "К-куда? Не отнимайте у меня её!"
    arb "Хочешь сказать «снова»?"
    lim "А правда - почему ты это сказал? Вовсе же не обязательно, что тебе нравится именно Алиса, разве не так?"
    play sound ds_sfx_psy
    vol "Нет! Не падай духом!"
    play sound ds_sfx_psy
    ine "Ты вспомнил что-то. Вспомнил то, чего очень не хотел вспоминать."
    me "Я... я уже знаю Алису?"
    arb "Как мы ни старались отгородить тебя от истины... ты пришёл к ней."
    me "Я. Знал. Алису?!"
    ine "Не совсем прям Алису Двачевскую. Но в твоей жизни была {i}она{/i}, поразительно напоминавшая Алису."
    show dvw normal at center
    with dissolve
    dv "Ты меня помнишь?"
    me "Я... я тебя видел... пару дней назад..."
    lim "Да. И ты прям на глазах падаешь духом. От каждой секунды осознания истины."
    "Ты не заметил, как уже лежишь на полу в ногах у явившейся тебе девушки."
    arb "Это всё сон. Запомнится тебе только самое яркое."
    me "Ты... Т-ты решила ко мне вернуться?"
    hide dvw
    show dv angry pioneer at center
    with dspr
    dv "Какое «вернуться», придурок?! Ты меня даже завоевать не сможешь, какое уж вернуть?"
    window hide
    menu:
        "Я справлюсь":
            window show
            me "Я... я справлюсь."
            vol "Ты справишься. Ты должен справиться. Двигайся вперёд, оставь прошлое в прошлом."
            arb "А вот справишься ли ты - посмотрим."
        "Я начну с другим человеком":
            window show
            me "А почему я вообще должен к ней возвращаться? Есть же столько других девушек!"
            vol "Тебе никто не сказал, что ты должен возвращаться. Напротив - ты должен двигаться вперёд."
            arb "Но как бы тебе не пожалеть о своём выборе... "
        "Я буду одиночкой":
            window show
            me "Мне никто не нужен! Никто! Мне и одному хорошо!"
            vol "Ты ведь сам прекрасно понимаешь, что это ложь. Зачем ты пытаешься обмануть свой же разум?"
            arb "Я знаю ответ. Но он тебе не понравится."
    me "Ты о чём?"
    arb "Ты вогнал себя в забытьё - и всё у тебя было хорошо. Но потом вновь начал мыслить и чувствовать - и всё пошло по новой."
    lim "Уж не лучше было бы провалиться в {i}вечное{/i} забытьё?"
    vol "Нет, не лучше. Ты должен жить! Жить - и бороться! «Совёнок» - это твой шанс!"
    show sl smile pioneer at fleft
    with dspr
    sl "Ты справишься, Семён. Всё будет хорошо."
    show mi smile pioneer at cleft
    with dspr
    mi "Да, Семён-кун, у тебя всё обязательно получится и будет хорошо-хорошо!"
    show us laugh sport at cright
    with dspr
    us "А ну выше нос, и вперёд! Не будь таким скучным!"
    show un sad pioneer at fright
    with dspr
    un "Да... тебе нужно постараться..."
    show dv angry pioneer close at center
    with dspr
    dv "Ты всё понял? Что ты ответишь?"
    window hide
    menu:
        "Согласиться впасть в забытьё":
            window show
            me "Да. Я думаю, так было бы лучше - забыть об этом всём."
            lim "Но увы. Ты себе этот путь отрезал. Теперь тебе придётся страдать. Вечно страдать."
            dv "Идиот! Ничего так и не понял!"
        "Принять борьбу":
            window show
            me "Да, я буду бороться за своё счастье и использую свой шанс по полной!"
            lim "Как бы ты не пожалел о своём решении. Жизнь - вечная борьба. Борьба за выживание, за благополучие."
            show dv smile pioneer close at center
            with dspr
            dv "А вот посмотрим, как ты исполнишь своё {i}мужское{/i} слово!"
    lim "Пора просыпаться, Семён. В новый бой!"
    return

label ds_day4_old_camp:
    $ persistent.sprite_time = 'day'
    scene bg ext_square_day
    with dissolve
    th "Итак, значит, попробуем сходить к старому лагерю..."
    th "Только вот где он?"
    scene bg ds_ext_square2_day
    with dissolve
    play sound ds_sfx_mot
    per_eye "Возле площади ты примечаешь карту лагеря. Может, на ней что-то есть."
    window hide
    menu ds_day4_find_camp:
        set ds_menuset
        "Изучить карту" (skill='logic', level=lvl_formidable):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_int
                lgc "{result}Смотри! В нижнем левом углу некий пунктир. Это не может быть ничем иным, кроме как дорогой к нему!"
                play sound ds_sfx_psy
                vol "Значит, идём туда."
                
            else:
                window show
                play sound ds_sfx_int
                lgc "{result}На карте нет даже намёков на старый лагерь. Она бесполезна."
                
                jump ds_day4_find_camp
        "Спросить у лагеря" (skill='shivers', level=lvl_legendary):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_fys
                shi "{result}Прислушайся. Ты слышишь скрип очень старых полов. Ветер, гуляющий по заброшенным комнатам."
                shi "Он доносит до тебя голоса детей. Очень давние голоса детей. И пытающихся их утихомирить вожатых."
                th "А откуда это всё идёт-то."
                shi "Юго-запад. Тебе нужно туда."
                
            else:
                window show
                play sound ds_sfx_fys
                shi "{result}Бесполезно. Лагерь не откликается на твой призыв о помощи."
                
                jump ds_day4_find_camp
        "Пойти наугад":
            window show
            "Ты направляешься в сторону ближайшего леса в надежде случайно наткнуться на лагерь."
            play sound ds_sfx_int
            lgc "Впрочем, шансы на это малы."
            jump ds_day4_forest_un
        "Оставить мысль":
            window show
            th "В общем, ладно, посмотрим пока известные мне локации."
            $ disable_current_zone_ds_small()
            jump ds_day4_map
    scene bg ext_path2_day
    with dissolve
    "Ты выдвигаешься в путь."
    play sound ds_sfx_psy
    vol "Тебе очень желательно было бы успеть до обеда."
    th "Я знаю..."
    window hide
    $ renpy.pause(3.0)
    scene bg ds_ext_old_building_day
    with dissolve
    window show
    "Долго ли, коротко ли, но вскоре ты видишь перед собой заброшенное здание."
    if ds_skill_list['volition'].check(lvl_challenging, passive=True).result():
        play sound ds_sfx_psy
        vol "{result}Заходим!"
        "И ты решительным шагом направляешься внутрь."
    else:
        play sound ds_sfx_psy
        vol "{result}Но что-то тебя останавливает. Ты... боишься?"
        th "Н-нет, наверное..."
        "Ты собираешь волю в кулак и заходишь."
    scene bg ds_int_old_building_day
    with dissolve
    play music ds_old_camp fadein 3
    play sound ds_sfx_int
    vic "Это здание определённо не использовалось очень давно. Разруха царит полнейшая."
    $ ds_visited_old_camp = True
    if ds_skill_list['conceptualization'].check(lvl_easy, passive=True).result():
        play sound ds_sfx_int
        con "{result}Только представь: ранее тут играли и резвились пионеры, а вожатые следили за порядком. Одни лица сменялись другими. А теперь всё ушло."
        con "Этот лагерь ассоциируется у тебя с твоей жизнью. Ранее она была наполнена счастьем, у тебя было много знакомых. А теперь? Всё вот так же пришло в негодность."
    if ds_skill_list['inland_empire'].check(lvl_easy, passive=True).result():
        window hide
        play sound sfx_ghost_children_laugh
        $ renpy.pause(1.5)
        window show
        play sound2 ds_sfx_psy
        ine "{result}Ты слышишь детский смех. Послышалось?"
        play sound2 ds_sfx_psy
        vol "Тем не менее, тебе становится не по себе."
        if not ds_skill_list['composure'].check(lvl_challenging, passive=True).result():
            play sound ds_sfx_mot
            com "{result}Тебя передёргивает от испуга."
        th "Откуда тут... смех?"
        ine "Некогда в этом лагере были же дети? Были. Вот твоё сознание и родило это по ассоциации."
        ine "Или же... ты снова что-то вспомнил?"
        ine "Да! Ты вспомнил своё детство. Твой детский садик напоминал это строение."
        play sound ds_sfx_psy
        vol "А с детским садом у тебя связаны не самые приятные воспоминания..."
        ine "Да! Ты всегда был {i}не такой как все{/i}. И за это подвергался травле."
        $ ds_morale.damage()
        vol "Тебе слишком тяжело от этих воспоминаний. Выкинь их из головы."
        window hide
        menu:
            "Потрясти головой":
                window show
                "Ты трясёшь головой. Наваждение, кажется, проходит."
            "Дать себе пощёчину":
                window show
                play sound sfx_face_slap
                with hpunch
                "Ты шлёпаешь себя по щекам."
                play sound ds_sfx_fys
                pat "Больно!"
                vol "Однако, это выбивает из тебя нежелательные мысли."
            "Выбежать и отдышаться":
                scene bg ds_ext_old_building_day
                with dissolve
                window show
                play sound sfx_intro_bus_stop_sigh
                "Ты выбегаешь из здания и начинаешь жадно вдыхать свежий воздух."
                $ ds_morale.up()
                "Тебе становится немного легче."
                window hide
                menu:
                    "Вновь зайти" (skill='volition', level=lvl_medium):
                        if ds_last_skillcheck.result():
                            window show
                            vol "{result}Ты переьарываешь свои опасения и заходишь в старый лагерь снова."
                        else:
                            window show
                            vol "{result}И ноги твоей тут не будет снова!"
                            stop music fadeout 3
                            scene bg ext_path2_day
                            with dissolve
                            "Ты бежишь обратно в лагерь."
                            scene bg ext_square_day
                            with dissolve
                            "В лагере всё по-прежнему. И тут тебе комфортнее."
                            $ disable_current_zone_ds_small()
                            jump ds_day4_map
                    "Вернуться в лагерь":
                        window show
                        me "Ну нафиг!"
                        stop music fadeout 3
                        scene bg ext_path2_day
                        with dissolve
                        "Ты бежишь обратно в лагерь."
                        scene bg ext_square_day
                        with dissolve
                        "В лагере всё по-прежнему. И тут тебе комфортнее."
                        $ disable_current_zone_ds_small()
                        jump ds_day4_map
                scene bg ds_int_old_building_day
                with dissolve
    th "Так, ладно, куда мне пойти?"
    play sound ds_sfx_int
    vic "Вариантов у тебя немного. Либо пойти в комнату левее - либо на второй этаж. Всё остальное завалено - туда пройти невозможно."
    window hide
    menu ds_day4_choose_room:
        set ds_menuset
        "Зайти в комнату":
            window show
            scene bg ds_int_old_building_room2_day
            with dissolve
            "Ты проходишь в комнату. Она пуста. Лишь матрас, чистый шкаф, да забитые досками окна."
            if ds_skill_list['instinct'].check(lvl_medium, passive=True).result():
                play sound ds_sfx_fys
                if ds_homo_traits < 3:
                    ins "{result}Идеальное место, чтобы трахнуть тяночку!"
                else:
                    ins "{result}Идеальное место, чтобы жёстко потрахаться!"
            play sound ds_sfx_int
            lgc "Тут ловить нечего. Возвращаемся."
            scene bg ds_int_old_building_day
            with dissolve
            jump ds_day4_choose_room
        "Подняться на второй этаж":
            window show
            scene bg ds_int_old_building_secondfloor
            with dissolve
            "В коридоре второго этажа кромешная тьма. Даже несмотря на то, что на улице уже почти полдень."
            "Ты заходишь в первую комнату."
            scene bg ds_int_old_building_cabinet_day
            with flash
            play sound ds_sfx_fys
            pat "После тьмы коридора тебя ослепляет солнечный свет."
            "Немного привыкнув, ты начинаешь осматривать помещение."
            play sound ds_sfx_mot
            per_eye "Из примечательного тут только книги. Их названия тебе совершенно непонятны."
            play sound ds_sfx_int
            lgc "Похоже на что-то, относящееся к переднему краю науки. Теория относительности, мультивселенная, многомировая интерпретация..."
            play sound ds_sfx_int
            enc "Ни один из этих терминов ты не знаешь."
            if ds_skill_list['reaction_speed'].check(lvl_easy, passive=True).result():
                play sound ds_sfx_mot
                res "{result}Погоди. «Многомировая интерпретация»? Не может ли это иметь отношение к твоей ситуации."
                lgc "Точно... Похоже, то, что хранится тут, имеет самое прямое отношение к твоему попаданию в «Совёнок»."
                enc "Но сам ты ничего не поймёшь. Возможно, стоит поспрашивать кибернетиков? Или Женю?"
                $ ds_found_old_books = True
                window hide
                menu:
                    "Взять книгу":
                        window show
                        "Ты хватаешь первую попавшуюся книгу и кладёшь её себе за пояс."
                        $ ds_took_old_book = True
                    "Не брать книг":
                        window show
            scene bg ds_int_old_building_secondfloor
            with dissolve
            "Ты вновь ныряешь в тьму и направляешься в следующую комнату."
            scene bg ds_int_old_building_room_day
            with dissolve
            "Эта комната чиста и опрятна."
            play sound ds_sfx_fys
            hfl "Даже, можно сказать, {i}необычно{/i} чиста и опрятна, {i}пугающе{/i}."
            play sound ds_sfx_int
            vic "В отличие от других мест здания, в этой комнате как будто бы кто-то был совсем недавно."
            th "А кто это мог быть?"
            play sound ds_sfx_int
            lgc "Кто угодно. Возможно, тот самый пропавший Шурик. Возможно, кто-то из лагерных не тот, за кого себя выдаёт."
            lgc "А может, это вообще никакого отношения к лагерю не имеет."
            if ds_skill_list['perception'].check(lvl_medium, passive=True).result():
                play sound ds_sfx_mot
                per_eye "{result}Ты примечаешь за углом что-то, напоминающее... лифт?"
                me "Лифт?!"
                per_eye "Да. Тут есть и кнопка вызова."
                $ ds_found_elevator = True
                window hide
                menu:
                    "Нажать кнопку":
                        window show
                        "Ты нажимаешь кнопку. Ноль результата. Лифт не работает."
                        play sound ds_sfx_fys
                        shi "Или же он был выключен."
                    "Не нажимать":
                        window show
            scene bg ds_int_old_building_secondfloor
            with dissolve
            "Ты исчерпал все доступные локации. На этом ты идёшь вниз."
            scene bg ds_int_old_building_day
            jump ds_day4_choose_room
        "Покинуть старый лагерь":
            window show
            stop music fadeout 3
    scene bg ds_ext_old_building_day
    with dissolve
    "С чувством облегчения ты выходишь из гнетущего здания."
    play sound ds_sfx_int
    lgc "Ты и тут Шурика не нашёл. Хотя сюда он и шёл! Где же он?"
    lgc "Либо он уже ушёл отсюда - либо он пробрался в заблокированные комнаты."
    play sound ds_sfx_mot
    svf "Но как?"
    play sound ds_sfx_psy
    ine "Тут вполне могут быть тайные ходы."
    play sound sfx_stomach_growl
    play sound2 ds_sfx_fys
    edr "Как бы то ни было - твой желудок ясно даёт понять, что пришло время обедать."
    play sound ds_sfx_psy
    vol "И тебе следовало бы прислушаться - иначе проблем не оберёшься."
    scene bg ext_path2_day
    with dissolve
    "Ты бежишь обратно в лагерь."
    scene bg ext_square_day
    with dissolve
    "В лагере всё по-прежнему. И тут тебе комфортнее."
    jump ds_day4_lunch

label ds_day4_forest_un:
    $ persistent.sprite_time = 'day'
    scene bg ext_path_day
    with dissolve
    play ambience ambience_forest_day fadein 3
    "Ты заходишь в глубь леса в надежде найти там старый лагерь."
    "Идёшь. {w}Идёшь. {w}Идёшь. {w}Идёшь. {w}Идёшь."
    "Но даже намёков на старый лагерь не видишь."
    play sound ds_sfx_int
    con "Вокруг тебя царит благоденствие - трава, кусты и деревья зеленеют, поют птички, резвится всякая мелочь вроде белочек и кроликов."
    play sound ds_sfx_psy
    ine "Как жаль, что ничего они тебе сказать про Шурика не могут, хотя наверняка знают, где он."
    th "То есть, Шурик всё же в лесу заблудился?"
    play sound ds_sfx_int
    lgc "Ну а где ему ещё быть? Был бы он в лагере - давно бы уже нашли."
    scene bg ext_polyana_day
    with dissolve
    play sound ds_sfx_fys
    edr "Ты выбился из сил. Сядь и отдохни."
    "Ты присаживаешься на ближайшее бревно."
    play music music_list["lets_be_friends"] fadein 3
    show un surprise pioneer at center
    with dspr
    "И как только ты присаживаешься - на поляну выходит Лена."
    un "Ой..."
    me "Привет, Лена."
    show un shy pioneer at center
    with dspr
    un "Привет..."
    me "Как у тебя дела?"
    un "Ну, так..."
    play sound ds_sfx_int
    dra "У Лены, кажется, есть что скрывать, мессир."
    play sound ds_sfx_psy
    emp "Очевидно, Лена чем-то расстроена. Начнёшь выяснять?"
    $ ds_embraced_un = False
    $ ds_asked_un_on_sh = False
    window hide
    menu ds_day4_un_dialogue_forest:
        set ds_menuset
        "Обнять Лену":
            window show
            show un shy pioneer close at center
            with dspr
            "Ты подходишь к Лене, прижимаешь её к себе."
            play sound ds_sfx_mot
            per_toc "Ты чувствуешь её тепло. Её {i}нежность{/i}."
            play sound ds_sfx_psy
            emp "И ты чувствуешь, что ей стало легче от твоих объятий."
            "Она еле слышно шепчет тебе на ухо."
            un "Спасибо..."
            show un shy pioneer at center
            with dspr
            "После этого она отстраняется от тебя."
            $ ds_lp['un'] += 1
            $ ds_embraced_un = True
            window hide
            jump ds_day4_un_dialogue_forest
        "Спросить про Шурика":
            window show
            me "Как поиски Шурика?"
            show un normal pioneer at center
            with dspr
            un "Никак... я его не видела..."
            play sound ds_sfx_int
            dra "Сие истина есть."
            $ ds_asked_un_on_sh = True
            window hide
            jump ds_day4_un_dialogue_forest
        "Выяснить причины грусти" (skill='empathy', level=lvl_up_medium, modifiers=[('ds_embraced_un', 1, 'Обнял Лену'), ('ds_asked_un_on_sh', -3, 'Поставил Шурика вперёд')]):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_psy
                emp "{result}Похоже на то, что у Лены что-то не получилось, и она пала духом из-за этого."
                emp "Самым неразумным будет спрашивать в лоб. Лучше скажи в общем, что она умница."
            else:
                window show
                play sound ds_sfx_psy
                emp "{result}Всё хорошо. Лена явно тебе доверится."
            
            window hide
            menu:
                "Приободрить Лену" if ds_last_skillcheck.result():
                    window show
                    me "Что бы там ни было - ты умничка! У тебя всё получится!"
                    show un shy2 pioneer at center
                    with dspr
                    un "Правда?"
                    me "Да, правда."
                    show un smile pioneer at center
                    with dspr
                    un "Спасибо, Семён..."
                    $ ds_lp['un'] += 2
                    un "Ладно, попробую ещё раз - может, и придёт вдохновение..."
                    play sound ds_sfx_int
                    lgc "Так вся проблема заключалась в творческом кризисе?"
                    emp "Для неё это очень важно. Как для любой творческой личности."
                    hide un with dissolve
                    play sound sfx_bush_leaves
                    "Лена тем временем удаляется в кусты."
                "Спросить про причины":
                    window show
                    me "Что у тебя случилось?"
                    show un cry pioneer at center
                    with dspr
                    un "Н-ничего... Всё хорошо..."
                    me "Ну я же вижу... ты плачешь!"
                    un "Просто я ни на что не способная неудачница!"
                    hide un with dspr
                    play sound sfx_bush_leaves
                    "И, выпалив это, Лена сбегает в кусты."
                "Уйти":
                    window show
                    me "Ладно, я пошёл!"
                    hide un with dissolve
                    stop music fadeout 3
                    $ ds_lp['un'] -= 2
                    $ disable_current_zone_ds_small()
                    jump ds_day4_map
        "Уйти":
            window show
            me "Ну ладно, не скучай!"
            hide un with dissolve
            stop music fadeout 3
            "И ты уходишь."
            $ disable_current_zone_ds_small()
            jump ds_day4_map
    window hide
    menu:
        "Догнать Лену":
            window show
            $ ds_lp['un'] += 1
        "Оставить в покое":
            window show
            stop music fadeout 3
            "Ты тоже уходишь - искать Шурика дальше."
            $ disable_current_zone_ds_small()
            jump ds_day4_map
    play sound sfx_bush_leaves 
    show un cry pioneer at center
    with dspr
    "Буквально на соседней поляне располагается Лена - заплаканная."
    me "Ты чего?"
    un "Да я просто... извини... у меня не получается..."
    me "Что не получается?"
    show un sad pioneer at center
    with dspr
    if ds_lp['un'] < 10:
        un "Ничего, неважно... не хочу тебя беспокоить."
        me "Но..."
        show un serious pioneer at center
        with dspr
        un "Я сказала: ничего. Не лезь, пожалуйста, ко мне!"
        hide un with dissolve
        play sound sfx_bush_leaves
        "И она уходит в чаще леса. Ты её не найдёшь."
        "Ты же выбираешься из леса, прикидывая, куда пойдёшь дальше."
        $ disable_current_zone_ds_small()
        jump ds_day4_map
    "Лена немного успокаивается и начинает рассказывать."
    un "Просто... понимаешь... я же рисую..."
    un "Ну, точнее как... просто размазываю краски..."
    un "А сейчас я даже придумать ничего не могу!"
    play sound ds_sfx_int
    con "Да, творческий кризис - случай тяжёлый... Для настоящего художника это смерти подобно."
    window hide
    menu ds_day4_un_find_solution:
        set ds_menuset
        "Придумать выход" (skill='conceptualization', level=lvl_challenging):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_int
                con "{result}Так пусть она {i}тебя{/i} изобразит!"
                me "Слушай, у меня есть идея..."
                show un shy pioneer at center
                with dspr
                un "Какая?"
                me "А давай ты изобразишь меня!"
                show un smile pioneer at center
                with dspr
                un "Да, Семён, давай... спасибо..."
                $ ds_lp['un'] += 2
                
            else:
                window show
                play sound ds_sfx_int
                con "{result}Но если Лена, художница, ничего придумать не может - то ты и подавно ничего не придумаешь!"
                
                window hide
                jump ds_day4_un_find_solution
        "Поддержать Лену":
            window show
            me "Сочувствую тебе..."
            show un sorrow pioneer at center
            with dspr
            un "Ага... Ладно, иди, тебе же Шурика искать надо..."
            play sound ds_sfx_int
            rhe "Это значит - она не хочет с тобой разговаривать."
            me "Но..."
            hide un with dissolve
            play sound sfx_bush_leaves 
            "И Лена снова уходит. На этот раз - без шансов её догнать, так как начинается чаща."
            "Ты же выбираешься из леса, прикидывая, куда пойдёшь дальше."
            $ disable_current_zone_ds_small()
            jump ds_day4_map
        "Посмеяться над Леной":
            window show
            me "Ну и что тут такого? Придумать! Видимо, ты и правда неспособная просто!"
            show un cry pioneer at center
            with dspr
            un "Ты... Т-ты..."
            "Ты продолжаешь веселиться, не замечая нарастающего гнева Лены."
            show un angry pioneer at center
            with dspr
            un "Слушай, я посмотрю на тебя, когда у тебя будет что-то не получаться!"
            $ ds_lp['un'] -= 2
            play sound ds_sfx_mot
            com "Ты аж приседаешь на землю от удивления."
            play sound ds_sfx_psy
            aut "Это что нашло на Лену?"
            hide un with dspr
            play sound sfx_bush_leaves
            "Тем временем Лена убегает - без шансов её найти."
            "Ты же выбираешься из леса, прикидывая, куда пойдёшь дальше."
            $ disable_current_zone_ds_small()
            jump ds_day4_map
        "Отреагировать равнодушно":
            window show
            me "Понятно... ну ладно, удачи!"
            show un sorrow pioneer far at center
            with dspr
            un "Удачи..."
            hide un with dissolve
            $ ds_lp['un'] -= 1
            "Ты же выбираешься из леса, прикидывая, куда пойдёшь дальше."
            $ disable_current_zone_ds_small()
            jump ds_day4_map
    scene bg ext_path_day
    show un normal pioneer at center
    with dissolve
    play sound ds_sfx_psy
    emp "Кажется, Лене становится лучше по мере того, как вы идёте из лесу."
    scene bg ds_ext_another_club_day
    show un smile pioneer at center
    with dspr
    un "Вот, заходи, Семён!"
    play sound ds_sfx_mot
    res "Погоди, а мы разве не к ней в домик пойдём?"
    window hide
    menu:
        "Молча зайти":
            window show
        "Спросить":
            window show
            me "А мы... не к тебе пойдём?"
            show un surprise pioneer at center
            with dspr
            un "В... в смысле?"
            me "Ну... ты не у себя в домике рисуешь разве?"
            show un smile pioneer at center
            with dspr
            un "Неа."
            show un shy pioneer at center
            with dspr
            if ds_whom_helped == 'un':
                un "Ты же сам вчера помогал мне заполучить вот это здание для рисования..."
            else:
                un "Я вчера собралась с силами и выпросила у Ольги Дмитриевны этот домик..."
            un "Тут просто удобнее, места побольше, да и Мику неудобств не создам..."
            play sound ds_sfx_int
            con "Ну, и художники зачастую предпочитают одиночество."
            window hide
            menu:
                "Cогласиться":
                    window show
                    me "Хорошо."
                "Отказаться":
                    window show
                    me "Ну нет, я думал, мы у тебя в домике будем рисовать, а так я не согласный!"
                    show un sad pioneer at center
                    with dspr
                    un "Ну... ну ладно..."
                    hide un with dspr
                    "И Лена убегает."
                    $ ds_lp['un'] -= 2
                    $ disable_current_zone_ds_small()
                    jump ds_day4_map
    play sound sfx_open_door_clubs_2
    scene bg ds_int_another_club_day
    show un smile pioneer at center
    with dspr
    "Вы заходите в домик."
    un "Проходи, Семён, располагайся!"
    if ds_skill_list['visual_calculus'].check(lvl_easy, passive=True).result():
        play sound ds_sfx_int
        vic "{result}Как видно, ранее в этом здании было что-то вроде... редакции газеты?"
        vic "Да! Письменные столы, книги, плакаты. И, похоже, газета закрылась недавно."
        play sound ds_sfx_int
        rhe "Но попробуй узнать наверняка у Лены."
        window hide
        menu:
            "Спросить у Лены":
                window show
                me "Слушай, Лен, а что тут было до... до тебя?"
                show un surprise pioneer at center
                with dspr
                un "Честно говоря... не знаю... кажется, какую-то газету делали..."
                un "А почему тебя это интересует, Семён?"
                if ds_skill_list['drama'].check(lvl_medium, passive=True).result():
                    play sound ds_sfx_int
                    dra "{result}Как занервничала, как занервничала! Похоже, есть у неё в шкафу скелетики..."
                me "Да так, просто интересно стало."
            "Не спрашивать":
                window show
    show un normal pioneer far at left
    with dspr
    "Тем временем, пока ты садишься на ближайший стул, Лена подходт к мольберту и поднимает его."
    play sound ds_sfx_psy
    sug "Помочь девушке не хочешь?"
    window hide
    menu:
        "Предложить помощь":
            window show
            me "Может, помочь тебе?"
            show un shy2 pioneer far at left
            with dspr
            un "Да нет... я сама справлюсь..."
            "И она ставит мольберт на место."
        "Помочь принудительно":
            window show
            "Ты подходишь к Лене и выхватываешь у неё мольберт."
            play sound ds_sfx_fys
            phi "Лена не то не стала сопротивляться, не то слишком слаба - но в любом случае усилий от тебя это не требует."
            show un scared pioneer at left
            with dspr
            un "Ч-что... ты делаешь?"
            me "Мольберт помогаю тебе перетащить."
            show un shy2 pioneer at left
            with dspr
            un "Ну... давай... поставь его вот сюда..."
            $ ds_lp['un'] += 1
        "Сидеть на месте":
            window show
            th "Думаю, она и сама прекрасно справится."
    "Наконец, мольберт оказывается на нужном месте, а Лена садится перед ним."
    show un normal pioneer at center
    with dspr
    un "Значит, смотри... сядь вот сюда, пожалуйста... я сделаю набросок, чтобы мы успели до обеда..."
    un "А потом я дорисую."
    window hide
    menu:
        "Поддержать Лену":
            window show
            me "Да, я уверен - у тебя получится очень классно!"
            show un shy pioneer at center
            with dspr
            un "Ты... правда так думаешь?"
            me "Конечно, я уверен!"
            show un smile3 at center
            with dspr
            un "Тогда я начну!"
            $ ds_lp['un'] += 1
        "Промолчать":
            window show
            "Ты усаживаешься в нужное место."
    "Лена берёт в руку карандаш и касается им листа."
    hide un
    window hide
    with fade
    $ renpy.pause(3.0)
    window show
    show un smile2 pioneer at center
    with dspr
    "Спустя пару часов Лена откладывает карандаш и зовёт тебя к себе."
    un "Вот, смотри, что получилось."
    play sound ds_sfx_mot
    per_eye "На удивление, Лене получилось запечатлеть твои контуры с высокой степенью достоверности. Придай сюда цвета - и не отличишь от настоящего."
    window hide
    menu:
        "Похвалить искренне":
            window show
            me "Ого, это ты нарисовала так реалистично?"
            show un shy pioneer at center
            with dspr
            un "Ну... да..."
            me "Отлично получилось, просто восхитительно! Когда дорисуешь - я заберу себе эту картину. В память о тебе!"
            un "Правда?"
            me "Да!"
            $ ds_lp['un'] += 2
        "Похвалить формально":
            window show
            me "Неплохо получилось."
            show un shy pioneer at center
            with dspr
            un "Cпасибо..."
            $ ds_lp['un'] += 1
        "Раскритиковать":
            window show
            me "Ну что это такое. Вот тут не так! И тут! И тут!"
            show un sorrow pioneer at center
            with dspr
            un "К-как? Я же так старалась..."
            show un cry pioneer at center
            with dspr
            un "Всё же я ни на что не способна!"
            hide un with dspr
            play sound sfx_slam_door_campus
            "И Лена вылетает из здания в слезах."
            $ ds_lp['un'] -= 5
            play sound ds_sfx_int
            con "Ну и зачем это было? Что за ненависть к искусству?"
    play sound sfx_dinner_jingle_speaker_tape
    play sound2 ds_sfx_mot
    per_hea "Тут звучит призыв к обеду."
    play sound ds_sfx_int
    lgc "Итак, Шурика мы так и не нашли. Что дальше?"
    play sound ds_sfx_psy
    aut "Ну, вообще это всё же забота Ольги Дмитриевны больше, нежели твоя. Просто скажешь: искал, но не нашёл."
    jump ds_day4_lunch

label ds_day4_scene:
    $ persistent.sprite_time = 'day'
    scene bg ext_aidpost_day
    with dissolve
    play ambience ambience_camp_center_day
    "Ты направляешься в сторону сцены."
    play sound ds_sfx_int
    lgc "Должна же быть у сцены какая-то подсобка? Декорации там, костюмы хранить. Вот там и мог Шурик потеряться."
    if ds_met['yn'] == 2:
        show yn normal pioneer at center
        with dspr
        "Когда ты проходишь около медпункта, то натыкаешься на появившуюся словно из воздуха Яну."
        show yn surprise pioneer at center
        with dspr
        yn "Ой, привет..."
        window hide
        menu:
            "Извиниться":
                window show
                me "Извини, я не хотел."
                show yn normal pioneer at center
                with dspr
                yn "Да всё нормально..."
            "Просто поздоровться":
                window show
                me "Привет."
            "Сбежать":
                window show
                "А ты убегаешь, надеясь, что Яна не поймёт, что это была ты."
                $ ds_ran_from_yn = True
                $ ds_lp['yn'] -= 1
        if not ds_ran_from_yn:
            window hide
            menu ds_day4_yn_dialogue:
                set ds_menuset
                "Cказать про пропавшего Шурика":
                    window show
                    me "Cлушай... а ты не видела Шурика?"
                    show yn surprise pioneer at center
                    with dspr
                    yn "А это... кто?"
                    play sound ds_sfx_int
                    rhe "Cледовало бы описать его - опрометчиво было считать, что она знает кого-то там из другого отряда."
                    me "Ну... такой, блондин в очках, ещё часы носит."
                    show yn normal pioneer at center
                    with dspr
                    yn "Нет... я не видела такого..."
                    yn "Хотя... кто-то похожий, кажется, ходил в лес..."
                    play sound ds_sfx_mot
                    res "В лес? Тогда бессмысленно его искать по лагерю, вероятно."
                    me "Cпасибо..."
                    $ ds_got_info_from_yn = True
                    window hide
                    jump ds_day4_yn_dialogue
                "Cпросить, что она тут делает":
                    window show
                    me "А... а что у тебя случилось?"
                    show yn shy pioneer at center
                    with dspr
                    yn "Да так... один из моих подопечных поранился..."
                    me "А... сочувствую ему..."
                    show yn normal pioneer at center
                    with dspr
                    yn "Я передам ему."
                    window hide
                    jump ds_day4_yn_dialogue
                "Cделать Яне комплимент":
                    window show
                    me "Прекрасно выглядишь, кстати!"
                    me "Такие яркие зелёные глаза, да и волосы..."
                    show yn shy2 pioneer at center
                    with dspr
                    yn "Спасибо..."
                    $ ds_lp['yn'] += 1
                    window hide
                    jump ds_day4_yn_dialogue
                "Предложить помощь":
                    window show
                    me "Может, помочь тебе?"
                    show yn shy pioneer at center
                    with dspr
                    yn "Ой... нет, не надо... я сама..."
                    play sound ds_sfx_psy
                    emp "Ей действительно не требуется помощь. Она в принципе не желает кого-либо напрягать."
                    me "Точно?"
                    yn "Точно..."
                    window hide
                    jump ds_day4_yn_dialogue
                "Попрощаться и уйти":
                    window show
                    me "Ну ладно, я пошёл! Пока!"
                    yn "Пока..."
                    hide yn with dissolve
        if ds_got_info_from_yn:
            play sound ds_sfx_psy
            vol "Как думаешь, разумно идти на сцену, зная, что Шурик уходил в лес?"
            window hide
            menu:
                "Отказаться от похода":
                    window show
                    th "Да, неразумно..."
                    $ disable_current_zone_ds_small()
                    $ ds_day4_places_remain -= 1
                    jump ds_day4_map
                "Продолжить":
                    window show
                    th "Думаю, лучше всё же проверить."
                    vol "Как хочешь."
    scene bg ds_ext_stage_big_day
    with dissolve
    "Ты подходишь к сцене. На ней совершенно никого нет."
    play sound ds_sfx_int
    lgc "Так что если Шурик действительно застрял тут - ему никто бы не помог."
    lgc "Но, с другой стороны, зачем он мог сюда полезть?"
    play sound ds_sfx_mot
    inf "Ну так ведь радиодетали ему нужны. Он вполне мог надеяться найти что-то тут. Или утащить усилитель какой."
    scene bg ext_stage_normal_day
    with dissolve
    "Ты приближаешься к ней."
    if not ds_skill_list['perception'].check(lvl_medium, passive=True).result():
        play sound ds_sfx_mot
        per_eye "{result}Но тут нет никаких даже намёков на подсобное помещение! По крайней мере, ты их не видишь."
        play sound ds_sfx_int
        lgc "А если сзади посмотреть?"
    else:
        play sound ds_sfx_mot
        per_eye "{result}Ты видишь неприметную дверцу снизу справа. Но на ней висит большой замок."
        play sound ds_sfx_int
        lgc "Cомнительно, что Шурик там. Как он мог туда попасть?"
        lgc "Хотя он мог и сзади пройти... вдруг там дверь?"
    window hide
    menu:
        "Выломать дверь" (skill='physical_instrument', level=lvl_heroic) if ds_last_skillcheck.result():
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_fys
                phi "{result}Готов? {w}И раз! {w}И два! {w}И три!"
                "Ты наносишь своим плечом пару ударов по двери, пока она не слетает с петель."
                scene bg ds_int_stage_basement_day
                play sound sfx_break_cupboard
                with vpunch
                "Ты оказываешься в помещении, давно заброшенном."
                play sound ds_sfx_int
                vic "И как только сцена держится ещё, а не рухнула? Тут же всё прогнило и осыпается!"
                play sound ds_sfx_mot
                per_eye "К тому же, повсюду разбросаны какие-то тряпки, провода и прочий мусор."
                if ds_skill_list['inland_empire'].check(lvl_medium, passive=True).result():
                    play sound ds_sfx_psy
                    ine "{result}Почему-то тебе приходит в голову мысль, что тут идеально кого-то держать в заточении."
                    th "Шурика?"
                    ine "Да какого Шурика?! Скорее, девушку. Связанную, неспособную позвать на помощь, будут пытать..."
                    play sound ds_sfx_mot
                    com "От подобных мыслей кого угодно бросит в дрожь. Ты - не исключение."
                    th "Кого... будут пытать?"
                    ine "Предвидеть невозможно будущее. Быть может, это просто фантазия твоя больная разыгралась."
                    th "Брррр! Выходим отсюда!"
                else:
                    per_eye "Впрочем, одно можно сказать точно - Шурика тут нет."
                    play sound ds_sfx_fys
                    edr "А ещё тебе становится дурно от запаха гнили."
                scene bg ext_stage_normal_day
                with dissolve
                "Ты выходишь на поверхность и вдыхаешь воздуха."
                me "Фууух!"
            else:
                window show
                play sound2 sfx_knock_door_closed_hard2
                play sound ds_sfx_fys
                phi "{result}Дверь слишком прочная - ты не можешь её выбить."
                play sound ds_sfx_fys
                pat "Всё, что у тебя остаётся - ушибленное плечо. Ты рефлекторно потираешь его."
                $ ds_health.damage()
        "Обойти сцену":
            window show
            scene bg ds_ext_backstage_day
            with dissolve
            "Ты заглядываешь за сцену в надежде найти что-то похожее на открытую дверь."
            play sound ds_sfx_int
            vic "Но тут есть лишь одна дверь, да и та ведёт {i}на{/i} сцену, а не {i}под{/i} неё."
            th "Значит, Шурика тут нет."
        "Оставить сцену":
            window show
    "Не найдя Шурика на сцене, ты возвращаешься обратно."
    $ disable_current_zone_ds_small()
    jump ds_day4_map

label ds_day4_lunch:
    scene bg black 
    with dissolve

    window show

    stop ambience fadeout 2
    play sound ds_sfx_psy
    vol "На обед ты идёшь со смешанными чувствами – выполненного долга и бесцельности последних нескольких часов."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_people_day 
    with dissolve

    play ambience ambience_dining_hall_full fadein 3

    window show
    play sound ds_sfx_int
    vic "Столовая битком."
    play sound ds_sfx_mot
    svf "Остаться незамеченным не удаётся – тебя окликает Ольга Дмитриевна."
    show mt normal pioneer at center, ds_seated 
    show sl normal pioneer at right, ds_seated 
    show el normal pioneer at left, ds_seated 
    with dissolve
    mt "Семён, иди к нам."
    "За четырёхместным столом сидят вожатая, Славя и Электроник."
    hide mt 
    hide sl 
    hide el 
    with dissolve
    if ds_skill_list['perception'].check(lvl_medium, passive=True).result():
        show dv angry pioneer far at cleft, ds_seated
        show yn normal pioneer far at cright, ds_seated
        with dissolve
        play sound ds_sfx_mot
        if ds_met['yn'] == 2:
            per_eye "{result}Вдали ты примечаешь свободное место рядом с Алисой и Яной."
        else:
            per_eye "{result}Вдали ты примечаешь свободное место рядом с Алисой и незнакомой тебе девушкой."
        window hide
        menu:
            "Сесть с девушками" (skill='authority', level=lvl_medium):
                if ds_last_skillcheck.result():
                    window show
                    play sound ds_sfx_psy
                    aut "{result}Просто откажись. Возражений не последует."
                    me "Я уже договорился!"
                    
                    "И ты идёшь к девочкам."
                    show dv angry pioneer at cleft
                    show yn normal pioneer at cright
                    with dspr
                    play sound ds_sfx_int
                    rhe "По всей видимости, они о чём-то спорят. Точнее, спорит Алиса."
                    dv "Почему ты такая... такая безразличная ко всему?!"
                    dv "Почему ты ведёшь себя как тупо кукла в руках чиновников?!"
                    yn "Прекрати злиться..."
                    if ds_lp['dv'] >= 25:
                        yn "Ты не сможешь понравиться ему, если будешь срываться на всех."
                    else:
                        yn "Ты не сможешь быть лучшей, если будешь срываться на всех."
                    yn "Тебе нужно быть спокойнее..."
                    dv "Да откуда тебе знать про это?!"
                    dv "Или ты считаешь себя самой лучшей?! Только потому, что обласкана ими?!"
                    play sound ds_sfx_int
                    lgc "Единственный способ, по которой они могли оказаться за одним столом - случайность."
                    lgc "Слишком уж они разные. Противоположности."
                    play sound ds_sfx_int
                    con "Как свет и тень. Как солнце и луна. Как огонь и вода."
                    show us laugh pioneer at center
                    with dissolve
                    us "А ну прекратили спорить! Давайте обедать!"
                    play sound ds_sfx_psy
                    sug "А вот и лесник пришёл. Им оказывается Ульянка."
                    lgc "Проблема в том, что тебе придётся вернуться к вожатой."
                    hide dv
                    hide yn
                    hide us
                    with dissolve
                else:
                    window show
                    play sound ds_sfx_psy
                    aut "{result}Ты не решаешься отказать вожатой."
            "Cесть с вожатой":
                window show
    else:
        play sound ds_sfx_mot
        per_eye "{result}Cвободных мест нет - отказываться неразумно."
    "Ты киваешь головой и отправляешься за обедом."
    "В этот раз тебе приходится несколько минут постоять в очереди."
    "Сегодняшнее меню мало чем отличается от меню предыдущих дней. По крайней мере по внешнему виду блюд."
    show mt normal pioneer at center, ds_seated 
    show sl normal pioneer at right, ds_seated 
    show el normal pioneer at left, ds_seated 
    with dissolve
    "Ты садишься за стол."
    window hide
    menu:
        "Пожелать приятного аппетита":
            window show
            me "Всем приятного аппетита!"
            $ ds_karma += 5
        "Промолчать":
            window show
    mt "Ну, и что вы думаете?"
    me "О чём?"
    mt "О Шурике!{w} Уже обед, а его всё нет."
    play sound ds_sfx_int
    con "Пушкинская рифма, однако."
    show sl sad pioneer at right   with dspr
    sl "Мы обыскали весь лагерь."
    show el upset pioneer at left   with dspr
    el "Я обошёл весь окрестный лес."
    play sound ds_sfx_psy
    sug "Ты тоже помогал."
    me "И я…{w} помогал."
    show mt surprise pioneer at center   with dspr
    mt "Надо звонить в милицию!"
    window hide
    menu:
        "Cогласиться":
            window show
            me "Да! Надо!"
            sl "Да, соглашусь с Семёном - мы всё возможное сделали."
            mt "C другой стороны - страшно представить, что с нами за это сделают! Потерять пионера!"
            mt "Мы должны до последнего искать сами! Даже администрации нельзя знать об этом!"
        "Предложить подождать до вечера":
            window show
            me "Может, хотя бы до вечера подождём?"
            me "Домой он поехал, например…"
            mt "Не может быть!{w} Шурик живёт отсюда в тысячах километров."
            me "Ну так на поезде."
            mt "До ближайшей станции…"
            "Она задумывается"
            show mt normal pioneer at center   with dspr
            mt "Далеко… не менее полутора часов на автомобиле. А пешком - вечность!"
        "Cообщить сведения от Яны" if ds_got_info_from_yn:
            window show
            me "Я говорил сегодня с вожатой младшего отряда..."
            me "Она сказала, как видела, что Шурик в лес ходил."
            show mt scared pioneer at center
            with dspr
            mt "Так он в лес ушёл всё-таки?! Но зачем?!"
            el "Нам понадобились детали в кружок... И вот он решил в старый лагерь уйти..."
            mt "В старый лагерь?! Он вообще с ума сошёл?!"
        "Промолчать":
            window show
            mt "C другой стороны - страшно представить, что с нами за это сделают! Потерять пионера!"
            mt "Мы должны до последнего искать сами! Даже администрации нельзя знать об этом!"
    sl "Значит, надо идти глубже в лес! Может, он заблудился!"
    el "У Шурика всегда с собой компас."
    play sound ds_sfx_mot
    inf "Интересно, что ещё можно найти в его чудо-жилетке (если она у него вообще есть)?"
    show mt surprise pioneer at center   with dspr
    mt "И в милицию!{w} В милицию вечером!"
    show mt sad pioneer at center   with dspr
    mt "Если он правда пропал, то нельзя медлить!"
    show sl serious pioneer at right   with dspr
    sl "Мы не можем пока этого знать."
    mt "Ну а где он тогда, где он?"
    play sound ds_sfx_int
    lgc "В словах вожатой есть доля истины – довольно странно вот так «прятаться» целый день."
    lgc "Да и зачем ему это?{w} Всё-таки Шурик кажется вполне серьёзным пионером, а такое поведение больше подошло бы Ульянке."
    lgc "Значит, действительно есть основания полагать, что он пропал."
    me "В любом случае мы сделали всё от нас зависящее, теперь остаётся только ждать."
    "Славя, Электроник и Ольга Дмитриевна грустно смотрят на тебя, но ничего не говорят."
    hide el 
    hide sl 
    hide mt 
    with dissolve

    stop ambience fadeout 2

    "Закончив обедать, ты относишь поднос на стол с грязной посудой и выходишь из столовой."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_near_day 
    with dissolve

    window show
    th "Ещё даже не вторая половина дня…"
    th "Чем бы заняться?"
    window hide
    $ persistent.sprite_time = "day"
    scene bg ext_square_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    play sound ds_sfx_psy
    ine "Лагерь словно отходит к послеобеденному сну."
    ine "Только Генда пристально смотрит на тебя из-под очков."
    ine "Конечно, взгляд его направлен на что-то другое, но тебе кажется, что он следит именно за тобой."
    ine "Наверняка он знает, куда пропал Шурик.{w} Только вот рассказать не сможет…"
    play sound ds_sfx_int
    lgc "Может быть, исчезновение кибернетика как-то связано с твоей ситуацией?"
    show cs normal medic2 at center   with dissolve
    cs "О, пионер!"
    "Перед тобой стояла медсестра."
    "Ты вопросительно смотришь на неё."
    cs "Посиди в медпункте за меня.{w} Мне нужно срочно отойти. Травма у кого-то."
    me "Я?"
    cs "Да, ты!{w} Вот ключи!"

    play sound sfx_keys_rattle

    pause(1)

    hide cs  with dissolve
    "Медсестра кидает тебе ключи и убегает."
    play sound ds_sfx_psy
    aut "Почему именно ты?{w} Как будто больше некому!"
    play sound ds_sfx_psy
    vol "И что конкретно ты должен сделать? А если что-то случится?.."
    vol "Но раз уж отказаться не успел, то ничего не поделаешь…"
    window hide
    menu:
        "Пойти в медпункт":
            window show
        "Не идти":
            window show
            th "Просто не пойду туда! Это не мои заботы!"
            jump ds_day4_no_medic
    jump ds_day4_medic

label ds_day4_medic:
    $ persistent.sprite_time = "day"
    scene bg ext_aidpost_day 
    with dissolve

    window show
    "Ты стоишь перед дверью в нерешительности."
    play sound ds_sfx_psy
    vol "С одной стороны, ничего страшного – посидишь здесь полчасика, она вернётся…"
    play sound ds_sfx_fys
    hfl "Ну, а если кто-то действительно придёт за помощью?{w} Со сломанной ногой?{w} Или пробитой головой?"
    play sound ds_sfx_mot
    com "Тебя охватывает нешуточное волнение."
    play sound ds_sfx_int
    lgc "Наверное, в этом лагере, кроме ссадин и синяков, никаких серьёзных травм не бывает."

    stop ambience fadeout 2

    hfl "Но в то же время случись что, и ты окажешься беспомощным."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_aidpost_day 
    with dissolve

    play ambience ambience_medstation_inside_day fadein 3

    window show
    if ds_skill_list['perception'].check(lvl_easy, passive=True).result():
        play sound ds_sfx_mot
        per_eye "{result}У медсестры на столе лежит журнал. Неплохой способ отвлечься."
        per_eye "Он называется «Советская модница». Издан в июне 1989 года."
        window hide
        menu:
            "Почитать журнал":
                window show
                $ ds_reading_journal = True
            "Отбросить мысль":
                window show
    if ds_reading_journal:
        play sound sfx_open_journal

        "С глянцевых страниц на тебя смотрят модели, разряженные в старомодные платья."
        play sound ds_sfx_int
        con "Сейчас бы так точно не стали ходить."
        con "Интересно, например, Славя, считает это модным?"
        con "Что было бы, если бы она надела нечто подобное и появилась в твоём времени?"
        con "Вот идёшь ты с ней под ручку в своём пальто и с капюшоном на голове, а она в пышном платье с рюшечками…"
        play sound ds_sfx_psy
        vol "Получается, ты уже представляешь Славю в своём мире…{w} Вместе с собой…{w} И не только Славю."
        con "Вот это платье больше подойдет Ульяне, вот этот сарафанчик – Алисе, а вот эта юбочка и кофточка – Лене."
        th "Действительно, если бы эти девочки были реальными…"
        ine "Нет, ты видишь их, слышишь их голос, можешь даже прикоснуться."
        th "Но они всё равно здесь, а я…{w} я просто не принадлежу этому месту."
        th "Оно для меня чужое.{w} Я просто жду возможности выбраться отсюда."
        th "Жду, потому что от меня уже ничего не зависит…"
        vol "Точно ли просто ждёшь возможности выбраться?"
    "Ты вздыхаешь, кладёшь голову на стол и засыпаешь."
    window hide

    scene bg black 
    with fade

    $ persistent.sprite_time = "day"
    scene bg int_aidpost_day 
    with fade

    play sound sfx_open_door_clubs

    window show
    "Тебя будит шум открывающейся двери."

    play music music_list["everyday_theme"] fadein 3

    show un normal pioneer at center   with dissolve
    "На пороге стоит Лена."
    if ds_to_help_un and (ds_day3_evening_who != 'un'):
        play sound ds_sfx_psy
        vol "Ведь ты вчера обещал помочь ей в медпункте..."
        if ds_skill_list['composure'].check(lvl_medium, passive=True).result():
            play sound ds_sfx_mot
            com "{result}Ты отворачиваешься, делая вид, что чем-то занят."
        else:
            play sound ds_sfx_mot
            com "{result}Лицо наливается кровью. Ты пытаешься отвести от Лены глаза."
    un "А медсестры нет?{w} Тогда попозже зайду…"
    play sound ds_sfx_mot
    res "Быстро! Скажи, что ты за неё!"
    play sound ds_sfx_psy
    vol "Раз уж на тебя возложили обязанность по лечению пионеров - подойди к ней со всей ответственностью."
    window hide
    menu:
        "Cказать, что ты за неё":
            window show
            me "Я за неё!"
            me "На что жалуетесь?"
            "Ты стараешься улыбнуться как можно аккуратнее - чтобы не смутить Лену."
            un "Да ничего такого…{w} Голова немного болит просто."
            me "Сейчас исправим!"
            play sound ds_sfx_int
            enc "Здесь нужно обезболивающее."
            if ds_skill_list['instinct'].check(lvl_medium, passive=True).result():
                play sound ds_sfx_fys
                ins "{result}Намекни ей. Протяни кое-что, связанное с любовью... Физической любовью..."
            window hide
            menu ds_day4_choose_drug:
                set ds_menuset
                "Предложить анальгин":
                    window show
                    "Процесс поиска занимает у тебя порядочно времени - ты же не знаешь, где что лежит."
                    "Однако, наконец ты находишь анальгин."
                    me "Нашёл!"
                    "Ты протягиваешь Лене таблетку анальгина."
                    show un smile pioneer at center   with dspr
                    un "Спасибо…"
                    "Она улыбается."
                    play sound ds_sfx_mot
                    com "Это неожиданно. Ты выпадаешь из реальности, уставившись на него."
                    show un surprise pioneer at center   with dspr
                    un "Что?"
                    "Лена моментально смущается."
                "Предложить пластырь":
                    window show
                    me "Вот, возьми."
                    show un surprise pioneer at center
                    with dspr
                    un "Думаешь... пластыря тут достаточно?"
                    play sound ds_sfx_int
                    rhe "Она очень аккуратно намекает на то, что ты не угадал."
                    window hide
                    jump ds_day4_choose_drug
                "Предложить бинт":
                    window show
                    me "Вот, возьми."
                    show un surprise pioneer at center
                    with dspr
                    un "И... что мне с этим делать?"
                    play sound ds_sfx_int
                    rhe "Нет. Мимо."
                    window hide
                    jump ds_day4_choose_drug
                "Предложить презерватив" if ds_last_skillcheck.result():
                    window show
                    me "У меня тут есть вот что..."
                    "Ты осматриваешь ящики, пока не находишь пачку с «изделиями №2»."
                    show un scared pioneer at center
                    with dspr
                    "Лицо Лены буквально перекашивает."
                    un "Э... Это ты к чему?"
                    me "Ну, типа..."
                    play sound ds_sfx_psy
                    emp "Её твой поступок лишь отпугнул."
                    ins "Вот же недогадливая..."
                    $ ds_lp['un'] -= 1
                    me "Ай, ладно."
                    "Ты убираешь пачку."
                    window hide
                    jump ds_day4_choose_drug
                "Сказать, что не знаешь, что дать":
                    window show
                    me "Я не знаю, чем тебе помочь. Я вообще не знаю, что тут есть!"
                    show un sad pioneer at center
                    with dspr
                    un "Понятно..."
    if ds_reading_journal:
        if ds_skill_list['conceptualization'].check(lvl_easy, passive=True).result():
            play sound ds_sfx_int
            con "{result}Юбочка и кофточка смотрелись бы на ней отлично. Под стать её художественной натуре."
            play sound ds_sfx_psy
            sug "Скажи ей об этом."
            window hide
            menu:
                "Предложить Лене":
                    window show
                    me "Слушай, а вот интересно, тебе понравилось бы такое?"
                    "Ты хватаешь со стола журнал и показываешь ту картинку, где нарисованы юбка и кофта."
                    play sound ds_sfx_psy
                    ine "Похоже, ты совсем сходишь с ума. То ли от разрушенных надежд на возвращение к себе. То ли от скуки."
                    "Лена смотрит на рисунок."
                    show un normal pioneer at center   with dspr
                    un "Да, наверное…"
                    me "А сейчас это… модно?"
                    show un shy pioneer at center   with dspr
                    un "Наверное…"
                    "Она смущается и краснеет."
                    play sound ds_sfx_int
                    rhe "Она не знает. Не интересуется модой."
                    un "А почему ты спрашиваешь?"
                    me "Мне кажется, на тебе это бы смотрелось прекрасно."
                    $ ds_lp['un'] += 1
                    un "Спасибо…"
                    me "Да не за что, я же правду говорю!"
                "Промолчать":
                    window show
    "Некоторое время вы молчите."
    window hide
    menu:
        "Спросить про самочувствие":
            window show
            me "Как голова?"
            show un smile pioneer at center   with dspr
            un "Лучше, спасибо."
            "Она улыбается."
        "Промолчать":
            window show
            "Наконец, Лена решается прервать молчание."
    un "Я пойду."
    window hide
    menu:
        "Пожелать удачи":
            window show
            me "Удачи!"
        "Промолчать":
            window show
        "Послать":
            window show
            me "Cкатертью дорожка!"
            $ ds_lp['un'] -= 1
    hide un  with dissolve

    stop music fadeout 3

    if ds_reading_journal:
        "Лена выходит, а ты садишься и принялся дальше листать журнал."
    else:
        "Лена выходит, а ты садишься и втыкаешь в окно."
    window hide

    with fade

    play sound sfx_knock_door7_polite

    window show
    "Через некоторое время в дверь стучат."
    th "Медпункт что, тут самое посещаемое место?"
    play sound ds_sfx_int
    dra "Вы - настоящая медсестра! Вернее, медбрат. Так вживитесь в роль!"
    window hide
    menu:
        "Впустить":
            window show
            me "Войдите!"
        "Притвориться, что никого нет":
            window show
            "Ты притаился."
            "Но посетитель не собирается ждать и открывает дверь."
            $ ds_lp['us'] -= 1

    play sound sfx_open_door_clubs

    play music music_list["eat_some_trouble"] fadein 3

    show us normal pioneer at center   with dissolve
    "Дверь открывается, на пороге стоит Ульянка."
    play sound ds_sfx_psy
    aut "А с каких пор Ульяна-то стучится?"
    window hide
    menu ds_day4_medic_ask_us:
        set ds_menuset
        "Прицепиться к стуку":
            window show
            me "С каких это пор ты стучишься?"
            show us sad pioneer at center   with dspr
            us "А что, нельзя?"
            "Она насупилась."
            window hide
            jump ds_day4_medic_ask_us
        "Спросить про самочувствие":
            window show
            me "Болит что-то?"
            show us dontlike pioneer at center   with dspr
            us "А тебе я с какой стати рассказывать должна?"
        "Промолчать":
            window show
    us "Где медсестра?"
    me "Перед тобой."
    play sound ds_sfx_int
    dra "Вы вальяжно закидываете ногу на ногу и вопросительно смотрите на неё."
    show us surp1 pioneer at center   with dspr
    us "Тогда я, пожалуй, пойду.{w} Лучше уж умереть, чем лечиться у тебя."
    "Она ехидно улыбается."
    window hide
    menu:
        "Попытаться удержать":
            window show
            me "Ты ведь даже не пробовала!"
        "Послать":
            window show
            me "Ну, как хочешь!"
            $ ds_lp['us'] += 1
    show us normal pioneer at center   with dspr
    "Ульяна на мгновение задумывается."
    us "Хотя таблетки можешь и ты мне дать."
    me "А что вас беспокоит?"
    "Она отвечает не сразу."
    show us dontlike pioneer at center   with dspr
    us "Тяжесть в животе…"
    aut "А не пустота в голове?"
    show us surp3 pioneer at center   with dspr
    us "Чего?"
    window hide
    menu:
        "Сказать вслух":
            window show
            me "А не пустота в голове?"
            show us dontlike pioneer at center
            with dspr
            us "Да ты! Дай уже что-нибудь!"
            me "Ладно, поищу сейчас..."
        "Просто поискать":
            window show
            me "Ничего, сейчас поищу."
        "Сказать, что ничего нет":
            window show
            me "Извини, нет ничего у нас."
            show us laugh pioneer at center
            with dspr
            us "А если найду?"
            me "Ладно..."
    show us normal pioneer at center   with dspr
    "В первом же ящике находится упаковка но-шпы."
    show us laugh2 pioneer at center   with dspr
    us "Спасибо вам, доктор!"
    "Она весело улыбается."
    play sound ds_sfx_int
    lgc "Смотря на Ульянку, ты никак не можешь понять, как такой жизнерадостный и активный ребёнок может испытывать проблемы со здоровьем."
    aut "Да просто наворовала конфет, объелась и всё!"
    play sound ds_sfx_psy
    emp "А может, у неё по-настоящему что-то болит? В столовой отравилась, скажем."
    play sound ds_sfx_fys
    edr "Да уж, местная еда зачастую слишком {i}abscheulich{/i}."
    window hide
    menu:
        "Обвинить в воровстве":
            me "Небось, конфет ворованных объелась?"
            show us dontlike pioneer at center   with dspr
            window show
            "Она недобро cмотрит на тебя."
            us "Нет, всё тебе оставила!"
            window hide

            pause(1)

            play sound sfx_slam_door_campus

            hide us  with dissolve
            window show
            "Ульянка убегает, хлопнув дверью."
            play sound ds_sfx_psy
            emp "Наверное, не стоило этого говорить. Даже если это правда."
            $ ds_lp['us'] -= 1
        "Предположить отравление":
            $ ds_lp['us'] += 1
            window show
            me "Учитывая местную стряпню, это неудивительно."
            show us surp1 pioneer at center   with dspr
            us "Может быть…"
            show us grin pioneer at center   with dspr
            us "А ты, я погляжу, здоровенький!"
            me "Не жалуюсь…"
            us "Ну, бывай!"
            window hide

            pause(1)

            play sound sfx_slam_door_campus

            hide us  with dissolve
            window show
            "Ульянка убегает, хлопнув дверью."
        "Промолчать":
            window show
            play sound sfx_slam_door_campus

            hide us  with dissolve
            window show
            "Ульянка убегает, хлопнув дверью."

    stop music fadeout 3

    window hide
    with fade

    window show
    if ds_reading_journal:
        "Ты вновь углубляешься в изучение советских модных тенденций."
    "Время идёт, а медсестра так и не возвращается."
    play sound ds_sfx_psy
    vol "В поисках Шурика ты не участвуешь, разгадок своего положения не ищешь…"
    if ds_reading_journal:
        vol "Просто сидишь и листаешь журнал."
    vol "Неплохая, в общем-то, ситуация..."
    play sound ds_sfx_psy
    ine "В конце концов, пока что всё происходящее можно считать чем-то вроде отдыха в летнем лагере, а если ничего не изменится в ближайшее время, тогда уж стоит и волноваться начинать."

    play sound sfx_knock_door2

    "В дверь опять стучат."
    vol "Сегодня эпидемия, что ли, какая-то?"

    play sound sfx_open_door_clubs

    play music music_list["my_daily_life"] fadein 3

    show sl normal pioneer at center   with dissolve
    "На пороге стоит Славя."
    show sl smile pioneer at center   with dspr
    sl "Ой, привет! А медсестры нет?"
    me "Привет. Нет. Я за неё."
    show sl shy pioneer at center   with dspr
    sl "Хорошо.{w} А мне бы…"
    "Она заминается."
    if ds_skill_list['empathy'].check(lvl_easy, passive=True).result():
        play sound ds_sfx_psy
        emp "{result}Это нечто личное, интимное. О чём неприлично говорить."
    me "Что?"
    if ds_sl_keys:
        show sl normal pioneer at center   with dspr
        sl "Кстати, Семён..."
        "Cлавя внимательно смотрит на тебя."
        me "Что?"
        sl "Я тут недавно свои ключи, кажется, потеряла. Ты не видел?"
        th "И ведь ещё как видел!"
        window hide
        menu:
            "Отдать ключи":
                window show
                me "Да, вот, я вчера их нашёл возле столовой, хотел тебе отдать, но забыл..."
                show sl serious pioneer at center   with dspr
                "Славя взяла ключи, а ты уже морально готов к любому уместному в данной ситуации наказанию."
                show sl smile pioneer at center   with dspr
                sl "Спасибо."
            "Не отдавать":
                window show
                me "Не видел я твоих ключей!"
                show sl sad pioneer at center
                with dspr
                sl "Печально... Я уже везде их искала... Ты был моей последней надеждой..."
        play sound ds_sfx_int
        rhe "Быстро смени тему разговора."
        me "Так зачем приходила?"
        me "Что-то болит?"
        show sl shy pioneer at center   with dspr
    sl "Да нет, ничего…"
    play sound ds_sfx_int
    rhe "Странно. Всегда такая открытая Славя о чем-то умалчивает?"
    me "Если что, ты говори! Меня сюда и посадили, чтобы всех лечить."
    "Ты широко улыбаешься."
    sl "Да нет…{w} То есть да, но нет."
    rhe "После этой фразы деление на ноль выглядит реальным."
    me "Ну, так чем могу помочь?"
    show sl smile2 pioneer at center   with dspr
    sl "Ты?{w} Думаю, ничем."
    "Она улыбается и собирается уходить, но вдруг останавливается."
    show sl normal pioneer at center   with dspr
    sl "Хотя…{w} Можешь выйти на минутку?"
    window hide
    menu:
        "Cогласиться":
            window show
            th "Почему бы и нет?"

            stop ambience fadeout 2

            me "Хорошо…"
            window hide

            $ persistent.sprite_time = "day"
            scene bg ext_aidpost_day 
            with dissolve

            play ambience ambience_camp_center_day fadein 3

            window show
            "Ты выходишь из медпункта и прислоняешься к стене."
            th "Интересно, что она такое там делает, что мне нельзя на это даже смотреть?"
            if ds_skill_list['logic'].check(lvl_medium, passive=True).result():
                play sound ds_sfx_int
                lgc "{result}Дай-ка подумать... Девушка, медпункт, нечто постыдное. {w}Уж не месячные ли у неё?"
                play sound ds_sfx_psy
                sug "Но Славя выглядит такой аккуратной девушкой, неужели она не предумотрела начало этого?"
                lgc "И на старуху бывает проруха, как говорится."
            show sl normal pioneer at center   with dissolve
            "Через минуту открывается дверь, и выходит Славя."
            "У неё в руках какой-то небольшой пакетик."
            play sound ds_sfx_psy
            emp "Думаю, ты уже понял, что спрашивать об этом неуместно."
            window hide
            menu:
                "Спросить про содержимое":
                    window show
                    me "А что это такое?"
                    show sl shy pioneer at center   with dspr
                    sl "Ничего!"
                    "Она краснеет."
                    sl "Спасибо тебе!"
                    me "Да не за что… И всё-таки..."
                    hide sl  with dissolve
                    "Славя убегает, так что спросить ты не успеваешь."

                    stop music fadeout 3

                    $ ds_lp['sl'] -= 1
                "Вырвать пакетик" (skill='physical_instrument', level=lvl_easy):
                    if ds_last_skillcheck.result():
                        window show
                        play sound ds_sfx_fys
                        phi "{result}Неужели ты не сможешь отнять этот несчастный пакетик у девушки."
                        "Ты и вырываешь пакетик. Да так, что он рвётся."
                        "Оттуда, как нетрудно было предположить, вываливаются средства гигиены. А именно прокладки."
                        show sl angry pioneer at center
                        with dspr
                        sl "Увидел? Доволен?"
                        sl "Зайду, в общем, когда Виолетта Церновна будет на месте..."
                        hide sl with dissolve
                        "И она убегает."
                        $ ds_lp['sl'] -= 2
                        $ ds_karma -= 20
                    else:
                        window show
                        play sound ds_sfx_fys
                        phi "{result}Похоже, для Слави этот пакетик очень важен. Она просто так его не отдаст."
                        "Действительно - тебе не удаётся его отобрать, несмотря на все попытки."
                        show sl angry pioneer at center
                        with dspr
                        sl "Отпусти пакетик, пожалуйста."
                        me "Ладно..."
                        "Ты выпускаешь из рук пакет."
                        sl "Cпасибо."
                        hide sl with dissolve
                        "И она уходит."
                        $ ds_lp['sl'] -= 1
                    

                "Проявить тактичность":
                    $ ds_lp['sl'] += 1
                    show sl normal pioneer far at center    with dissolve
                    window show
                    me "Удачи!"
                    "Кричишь ты ей вслед."
                    show sl smile2 pioneer far at center   with dspr
                    sl "Спасибо!"

                    stop music fadeout 3

                    "Одаривает она тебя напоследок милой улыбкой."
                    hide sl  with dissolve
        "Отказать":
            window show
            me "Нет. Если хочешь - бери, я не мешаю."
            show sl normal pioneer at center
            with dspr
            sl "Понятно... Зайду попозже..."
            $ ds_lp['sl'] -= 1
            hide sl with dissolve
            "И она уходит."

    window hide

    scene bg black 
    with dissolve

    stop ambience fadeout 3

    $ persistent.sprite_time = "day"
    scene bg int_aidpost_day 
    with dissolve

    play ambience ambience_medstation_inside_day fadein 3

    window show
    "Ты смотришь на часы."
    "Время уже приближается к вечеру, журнал был прочитан вдоль и поперёк, а медсестра так и не возвращается."
    play sound ds_sfx_psy
    ine "У тебя усиливается подозрение, что не в травме тут дело."

    play sound sfx_open_door_kick

    play music music_list["that_s_our_madhouse"] fadein 3

    show dv normal pioneer at center   with dissolve
    "Вдруг дверь распахивается, и в медпункт вбегает Алиса."
    "Она пристально смотрит на тебя."
    dv "А ты что здесь делаешь?"
    me "Сижу…"
    show dv smile pioneer at center   with dspr
    dv "Ну и ладно!{w} Так даже лучше, что медсестры нет."
    me "Заболела?"
    "Алиса не отвечает и подходит к тебе."
    show dv normal pioneer at center   with dspr
    dv "Подвинься."
    window hide
    menu:
        "Подвинуться":
            window show
            me "Ну ладно..."
            "Ты отодвигаешься. Алиса подходит к ящику, копается в нём и, не находя нужного, обращается к тебе."
        "Cпросить, зачем":
            window show
            me "Зачем?"
            dv "Чтобы я ящик смогла открыть, очевидно же!"
            me "Зачем это?"
            show dv angry pioneer at center   with dspr
            dv "Тебе какое дело?"
            me "Ну, я тут вроде как исполняющий обязанности…"
            show dv normal pioneer at center   with dspr
            "Она задумывается."
        "Отказаться":
            window show
            me "Нет."
            show dv angry pioneer at center
            with dspr
    dv "Дай мне тогда активированный уголь!"
    me "Живот болит?"
    show dv grin pioneer at center   with dspr
    dv "Да."
    "Ехидно усмехается она."
    play sound ds_sfx_fys
    hfl "Что-то здесь не так… Ты чувствуешь это спинным мозгом."
    play sound ds_sfx_psy
    emp "Но мало ли… Вдруг правда что-то болит."
    window hide

    menu:
        "Дать Алисе уголь":
            $ ds_lp['dv'] += 1
            window show
            me "Ладно."
            window hide

            play sound sfx_open_table

            $ renpy.pause(1)

            window show
            "Ты лезешь в ящик и вытаскиваешь оттуда упаковку активированного угля."
            show dv normal pioneer at center   with dspr
            dv "Спасибо!"
            hide dv  with dissolve

            stop music fadeout 3

            "Она вырывает её у тебя из рук и убегает."
            $ ds_dv_has_coal = True

        "Не давать ей уголь":
            window show
            me "Точно живот болит?"
            dv "Точно-точно!"
            me "Что-то не похоже…"
            show dv angry pioneer at center   with dspr
            dv "А что, меня здесь разорвать должно, чтобы ты поверил?"
            me "Я не знаю, что можно плохого сделать с активированным углем, но, уверен, ты придумаешь!"
            "Она заминается."
            show dv normal pioneer at center   with dspr
            dv "А даже если так?"
            me "Вот!{w} Так и думал!{w} Тогда я тебе точно ничего не дам!"
            "Алиса пытается силой пролезть к ящикам, но ты закрываешь грудью его."
            if ds_skill_list['conceptualization'].check(lvl_medium, passive=True).result():
                play sound ds_sfx_int
                con "{result}Как Александр Матросов амбразуру."
            play sound ds_sfx_fys
            phi "При всей своей наглости она всё же девочка, и оттеснить тебя у неё никак не получится."
            show dv angry pioneer at center   with dspr
            dv "Ну и ладно! В другом месте найду."
            hide dv  with dissolve
            "Она разворачивается и направляется к выходу."
            "В дверях Алиса останаливается и оборачивается."
            show dv normal pioneer at center   with dspr
            dv "Кстати, там вожатая с медсестрой пионера несут, который ногу сломал.{w} Мне-то всё равно, но им, наверное, тяжело."
            if ds_skill_list['drama'].check(lvl_trivial, passive=True).result():
                play sound ds_sfx_int
                dra "{result}Звездит. Звездит как дышит."
                me "Так я тебе и поверил!"
                dv "Иди сам посмотри…"
            play sound ds_sfx_mot
            svf "В любом случае, ты же быстренько."
            window hide
            menu:
                "Проверить" (skill='reaction_speed', level=lvl_challenging):
                    window show
                    hide dv  with dissolve
                    "Ты подходишь к двери и выглядываешь на улицу.{w} Там никого не оказывается."
                    if ds_last_skillcheck.result():
                        window show
                        show dv evil_smile pioneer at center
                        with dissolve
                        res "{result}Алиса полезла в ящик! Ты успеваешь это заметить!"
                        me "Так-так!"
                        
                        show dv scared pioneer at center
                        with dspr
                        "Алиса в ступоре от случившегося."
                        play sound ds_sfx_mot
                        com "Впрочем, она быстро собирается."
                        show dv angry pioneer at center
                        with dspr
                        dv "С дороги! Не мешай мне!"
                        window hide
                        menu:
                            "Забить":
                                window show
                                me "Да и ладно, иди уже!"
                                dv "Спасибо!"
                                hide dv with dissolve
                                $ ds_dv_has_coal = True
                            "Потребовать вернуть уголь" (skill='authority', level=lvl_medium):
                                if ds_last_skillcheck.result():
                                    window show
                                    play sound ds_sfx_psy
                                    aut "{result}Надави на неё. Скажи, что у неё всё равно ничего не получится - вожатая не даст."
                                    me "У тебя всё равно ничего не выйдет! Я сейчас же иду и говорю обо всём Ольге Дмитриевне!"
                                    show dv angry pioneer at center
                                    with dspr
                                    dv "Ябеда! Подавись своим углём!"
                                    "С этими словами она швыряет в тебя уголь и уходит, задрав нос."
                                    hide dv with dissolve
                                    $ ds_lp['dv'] -= 1
                                else:
                                    window show
                                    play sound ds_sfx_psy
                                    aut "{result}Вид Алисы настолько угрожающий. Почему-то ты не решаешься потребовать у неё забрать уголь. Всё, на что тебя хватает - пролепетать."
                                    me "Отдай, пожалуйста, уголь..."
                                    show dv grin pioneer at center
                                    with dspr
                                    dv "А ты отними!"
                                    hide dv with dissolve
                                    "C этими словами она убегает, да так, что догнать её не представляется возможным."
                                    $ ds_morale.damage()
                                    $ ds_dv_has_coal = True
                                
                            "Отнять уголь" (skill='physical_instrument', level=lvl_medium):
                                if ds_last_skillcheck.result():
                                    window show
                                    play sound ds_sfx_fys
                                    phi "{result}Как конфетку отнять у ребёнка!"
                                    show dv scared pioneer close at center
                                    with dspr
                                    "Ты прижимаешь Алису к стене и вырываешь у неё из рук уголь."
                                    me "Вот так-то!"
                                    show dv angry pioneer at center
                                    with dspr
                                    dv "Да ты! Я тебе отомщу в следующий раз..."
                                    $ ds_lp['dv'] -= 2
                                    $ ds_karma -= 10
                                    hide dv with dissolve
                                else:
                                    window show
                                    play sound ds_sfx_fys
                                    phi "{result}Однако, Алиса физически довольно сильна..."
                                    show dv angry pioneer close at center
                                    with dspr
                                    "Ты хватаешься за уголь, но Алиса цепко его держит."
                                    "Вы сваливаетесь на стол и начинаете кататься по нему."
                                    window hide
                                    play sound ds_things_fall
                                    $ renpy.pause(5.0)
                                    window show
                                    "Алисе всё же удаётся вырваться, и даже оставить уголь за собой."
                                    $ ds_health.damage()
                                    show dv laugh pioneer at center
                                    with dspr
                                    dv "Вот же ты слабак, даже уголь забрать не можешь!"
                                    $ ds_morale.damage()
                                    $ ds_dv_has_coal = True
                                    "Со смехом Алиса уходит."
                                    hide dv with dissolve
                                    $ ds_lp['dv'] -= 2
                                    "А тебе остаётся разгромленный медпункт."
                                
                    else:
                        window show
                        play sound ds_sfx_mot
                        res "{result}Никого нет. Твоего внимания ничего не требует."
                        show dv normal pioneer at center   with dissolve
                        me "Ну и где?"
                        show dv surprise pioneer at center   with dspr
                        dv "Не дошли, значит, ещё."
                        "Она разводит руками."
                        show dv smile pioneer at center   with dspr
                        dv "Счастливо!"
                        hide dv  with dissolve
                        "Ты возвращаешься к столу и только тогда обнаруживаешь, что один из ящиков открыт."
                        res "Как же она так успела?!"
                        res "Всего на секунду отвернулся..."

                        stop music fadeout 3

                        th "Впрочем, что плохого может выйти из активированного угля?.."
                        if ds_skill_list['encyclopedia'].check(lvl_up_medium, passive=True).result():
                            play sound ds_sfx_int
                            enc "Если она сможет раздобыть серу и селитру - сможет подорвать лагерь."
                "Не поверить":
                    window show
                    me "Я уверен, что ты пытаешься меня надуть!"
                    show dv angry pioneer at center
                    with dspr
                    dv "Вот же непрошибаемый! Не веришь! Мне!!"
                    play sound ds_sfx_int
                    rhe "А с чего бы тебе ей верить?"
                    dv "Ну и сиди со своим углём в обнимку!"
                    hide dv with dissolve
                    "И она уходит, задрав нос."
                    $ ds_lp['dv'] -= 2
    window hide

    scene black 
    with dissolve

    $ persistent.sprite_time = "day"
    scene bg int_aidpost_day 
    with dissolve

    stop music fadeout 3

    play sound ds_sfx_psy
    vol "Пора выдвигаться на ужин."
    window hide
    jump ds_day4_dinner

label ds_day4_no_medic:
    th "Куда бы мне пойти?"
    window hide
    $ disable_all_zones_ds_small()
    $ set_zone_ds_small('house_me_mt', 'ds_day4_after_lunch_mt')
    $ set_zone_ds_small('music_club', 'ds_day4_after_lunch_mi')
    $ set_zone_ds_small('clubs', 'ds_day4_after_lunch_el')
    $ set_zone_ds_small('library', 'ds_day4_after_lunch_mz')
    $ set_zone_ds_small('entrance', 'ds_day4_after_lunch_cs')
    $ set_zone_ds_small('medic_house', 'ds_day4_medic') # V
    $ set_zone_ds_small('storage', 'ds_day4_storage') # V
    jump ds_day4_after_lunch_map

label ds_day4_after_lunch_map:
    stop ambience fadeout 3
    stop music fadeout 3
    window hide
    if ds_dv_intercepted_stage > 2:
        $ reset_zone_ds_small('storage')
    $ show_small_map_ds()

label ds_day4_after_lunch_cs:
    $ persistent.sprite_time = 'day'
    scene bg ds_ext_clubs_gate_day
    with dissolve
    th "Попробую из лагеря выйти... должно же получиться добраться до какой-нибудь хотя бы деревни!"
    play sound ds_sfx_psy
    vol "Должно..."

    scene bg ds_ext_camp_entrance_car
    show cs normal medic2 at center
    with dissolve
    "На выходе из лагеря ты видишь машину и Виолу перед нет."
    if ds_skill_list['encyclopedia'].check(lvl_up_medium, passive=True).result():
        play sound ds_sfx_int
        enc "{result}Это Иж-2125 «Комби». Основана на «Москвиче-412», имела новый для советского автопрома кузов типа хэтчбек. Была довольно популярной за счёт улучшенных ходоых качеств и увеличенного багажника."
    cs "А ты что тут делаешь, пионер? Я же сказала тебе посидеть в медпункте."
    if ds_skill_list['reaction_speed'].check(lvl_easy, passive=True).result():
        play sound ds_sfx_mot
        res "А разве она не говорила, что ей надо травмировавшегося пионера лечить?"
    window hide
    menu ds_day4_cs_dialogue_enter:
        set ds_menuset
        "Спросить про пионера и травму" if ds_skill_list['reaction_speed'].check_results[-1].result():
            window show
            me "А вы же говорили, что травма у кого-то, поэтому вам идти надо."
            show cs grin medic2 at center
            with dspr
            cs "Понимаешь, пионер... мне было проще сказать это, нежели объяснять, куда и зачем я еду."
            cs "Вы какие-то слишком любопытные зачастую, суёте свой нос... куда не надо."
            play sound ds_sfx_int
            dra "Какой позор! Какой стыд! Не понять, что она врёт! Провела вас она, мессир!"
            window hide
            jump ds_day4_cs_dialogue_enter
        "Убедить Виолу, что ты нужен ей" (skill='suggestion', level=lvl_challenging):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_psy
                sug "{result}Женщина одинокая едет куда-то? Предложи ей свою помощь, своё мужское плечо."
                me "Я посчитал, что лучше помогу вам в вашей поездке! Вдруг вам тяжести надо будет таскать?"
                show cs doubt medic2 at center
                with dspr
                cs "Ну... ладно, садись в машину."
                $ ds_lp['cs'] += 1
                "Ты подчиняешься ей."
                scene cg ds_day4_cs_car
                with dissolve
                play sound ds_auto_ignite
                "Виола заводит машину."
                stop sound fadeout 3
                play sound_loop sfx_bus_interior_moving fadein 3
                "И вы трогаетесь."
            else:
                window show
                play sound ds_sfx_psy
                sug "{result}Она должна тебя взять! Начни её упрашивать! Молить!"
                me "Возьмите меня, пожалуйста! Я очень хочу покататься на машине! Ну пожалуйста!"
                show cs irritated medic2 at center
                with dspr
                cs "Ну-ну, пионер, прекращай этот детский сад. Мне надо ехать по важным делам, а ты будешь мешать."
                $ ds_lp['cs'] -= 1
                play sound ds_sfx_psy
                aut "Она назвала твои слова детским садом?"
                $ ds_morale.damage()
                show cs normal medic2 at center
                with dspr
                cs "Всё, я поехала. Иди в медпункт, пионер."
                hide cs with dissolve
                th "Не получилось..."
                if ds_skill_list['drama'].check(lvl_medium, passive=True).result():
                    play sound ds_sfx_int
                    dra "{result}Всё больше кажется, что она нечто скрывает..."
                $ disable_current_zone_ds_small()
                jump ds_day4_after_lunch_map
        "Отказаться сидеть в медпункте" (skill='authority', level=lvl_challenging):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_psy
                aut "{result}Сделай шаг вперёд. Выставь свою грудь. И спокойно откажи."
                me "Я не обязан сидеть в медпункте. У меня есть свои планы и дела."
                cs "И какие же, пионер?"
                play sound ds_sfx_mot
                res "Шурика искать!"
                me "Шурика искать, например."
                show cs doubt medic2 at center
                with dspr
                cs "Ладно, пионер. Но найди кого-нибудь, кто посидит в медпункте."
                cs "А мне ехать пора."
                hide cs with dissolve
                "И Виола садится в машину и уезжает."
                $ disable_current_zone_ds_small()
                jump ds_day4_after_lunch_map
            else:
                window show
                play sound ds_sfx_psy
                aut "{result}Набери воздуха в грудь... {w}вот так... {w}а теперь кричи!"
                me "Никуда я не пойду! Не хочу я в вашем медпункте сидеть!"
                show cs irritated medic2 at center
                with dspr
                cs "Есть такое слово, пионер: «надо». Как говорится: «пионер всегда готов!»"
                cs "Так что иди в медпункт. Вечером проверю."
                hide cs with dissolve
                "И Виола садится в машину и уезжает."
                $ ds_lp['cs'] -= 1
                $ disable_current_zone_ds_small()
                jump ds_day4_after_lunch_map
        "Похвалить машину" if ds_skill_list['encyclopedia'].check_results[-1].result():
            window show
            me "Какая классная машина."
            show cs shy medic2 at center
            with dspr
            cs "Нравится? А как она едет классно... так мягко, плавно..."
            show cs normal medic2 at center
            with dspr
            cs "Ладно, давай к делу. Иди в медпункт."
            window hide
            jump ds_day4_cs_dialogue_enter
        "Уйти":
            window show
            me "Извините, я пойду в медпункт..."
            cs "Давай, пионер... вечером увидимся."
            hide cs with dissolve
            "C этими словами Виола садится в машину и уезжает."
            $ disable_current_zone_ds_small()
            jump ds_day4_after_lunch_map
    "Вы отъезжаете от лагеря. С переднего сидения открывается прекрасный вид на дорогу."
    "Впрочем, сама дорога ничего интересного не представляет - вокруг неё поля, поля, поля и ничего больше."
    if ds_skill_points['conceptualization'].check(lvl_medium, passive=True).result():
        play sound ds_sfx_int
        con "{result}Ну как же ничего интересного? Сколько художников воспевали русскую природу наподобие той, что ты видишь!"
        con "Вот бы ты умел рисовать! {w}Или хотя бы фотоаппарат, чтобы запечатлеть эту красоту..."
    window hide
    menu ds_day4_cs_dialogue_car:
        "Спросить про место назначения":
            window show
            me "А куда мы едем?"
            cs "Не спеши. Всему своё время."
            play sound ds_sfx_int
            rhe "Не расколется. Лучше подожди - сам всё узнаешь."
            window hide
            jump ds_day4_cs_dialogue_car
        "Попросить включить радио":
            window show
            me "Может, радио включим?"
            cs "Ну давай, пионер."
            "Виола тянется к магнитоле и нажимает кнопку включения. Но радио не может выдавить из себя ничего кроме шипения."
            cs "Ой. Не ловит тут радио."
            "И она выключает радио."
            window hide
            jump ds_day4_cs_dialogue_car
        "Спросить про работу медсестрой":
            window show
            me "А как вам ваша работа?"
            cs "Ты о чём?"
            me "Ну, как вам работается медсестрой?"
            cs "А... ну, сам подумай. Целый день сидишь в медпункте, отходить никуда нельзя - вдруг кто травмируется..."
            cs "Вот то ли дело раньше..."
            play sound ds_sfx_int
            rhe "Раньше?"
            me "Что раньше?"
            cs "Неважно."
            rhe "Похоже, она проговорилась, и теперь пытается скрыть..."
            rhe "Бесполезно - она не расколется."
            window hide
            jump ds_day4_cs_dialogue_car
        "Попросить фотоаппарат" if ds_skill_list['encyclopedia'].check_list[-1].result():
            window show
            me "А можно у вас... фотоаппарат?"
            cs "Тебе зачем?"
            me "Природу запечатлеть хочу..."
            cs "А, ну посмотри в сумке."
            play sound ds_sfx_mot
            inf "Ты залезаешь в сумку и нащупываешь там фотоаппарат. Зачем он медсестре?"
            inf "Впрочем, неважно. Ты достаёшь его и готовишься сделать снимок."
            play sound ds_sfx_int
            con "Да, вот так... отлично... снимай!"
            play sound ds_photo
            with flash
            con "Получилось, кажется!"
            inf "К сожалению, увидеть снимок сейчас ты не можешь - тебе нужно будет его проявить."
            $ ds_made_nature_photo = True
        "Молча сидеть":
            window show
    "Проходит час... {w}полтора часа..."
    play sound ds_car_brakes
    stop sound_loop
    "Наконец, вы прибываете и выходите из машины."
    scene bg ds_ext_old_camp_storage_day
    show cs normal medic2 at center
    with dissolve
    "Перед тобой склад, явно давно заброшенный."
    cs "Так, пионер. Заходи на склад и внимательно его осмотри. Найдёшь коробку с номером 42 - возьмёшь её и принесёшь сюда."
    window hide
    menu ds_day4_cs_dialogue_storage:
        set ds_menuset
        "Cпросить про коробку":
            window show
            me "А можно узнать, что в этой коробке?"
            cs "Нет."
            play sound ds_sfx_int
            rhe "Кратко и ясно. Ничего ты не узнаешь - не сейчас."
            window hide
            jump ds_day4_cs_dialogue_storage
        "Пойти на склад":
            window show
            me "Как скажете."
        "Отказаться":
            window show
            me "Не пойду я туда!"
            show cs irritated medic2 at center
            with dspr
            cs "А кто просился со мной и обещал помочь? Нет уж - я тебя обратно не повезу. Или помогаешь мне - или идёшь пешком."
            play sound ds_sfx_psy
            vol "У тебя нет выбора - тебе придётся помочь ей."
            window hide
            jump ds_day4_cs_dialogue_storage
    scene bg ds_int_old_camp_storage
    with dissolve
    "Ты заходишь на склад. Тебя встречают ряды коробок. Целая армия."
    play sound ds_sfx_int
    lgc "И каковы шансы найти нужную?"
    play sound ds_sfx_psy
    vol "Берись за дело!"
    "Ты начинаешь обходить стеллажи в поиске заветного числа 42."
    window hide
    $ renpy.pause(5.0)
    window show
    "Спустя полчаса поисков ты находишь искомую коробку. Она находится на верхней полке, так что перед тобой стоит задача её спустить."
    play sound ds_sfx_mot
    per_eye "Перед входом стоит лестница. Попробуй использовать её."
    play sound ds_sfx_mot
    svf "Лестница выглядит хлипкой. Тебе надо будет взбираться на неё аккуратно."
    window hide
    menu:
        "Воспользоваться лестницей" (skill='savoir_faire', level=lvl_up_medium):
            window show
            "Ты берёшь лестницу и приставляешь её к стеллажу."
            window hide
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_mot
                svf "{result}Ты ловко взбираешься по лестнице и тянешь на себя коробку."
                svf "Теперь самое сложное - спуститься. Ты аккуратно делаешь шаг за шагом, перемещая коробку по ступеньке вниз."
                svf "Cпустя пять минут ты оказываешься внизу с коробкой."
            else:
                window show
                play sound ds_sfx_mot
                svf "{result}Ты взбираешься по лестнице и тянешь на себя коробку."
                svf "Но тебе не удаётся удержать равновесие, и, выпустив коробку, ты падаешь."
                window hide
                play sound sfx_bodyfall_1
                with vpunch
                $ ds_health.damage()
                window show
                play sound ds_sfx_fys
                pat "Ты ударяешься о пол, и сверху тебе на живот падает коробка. Тебя скрючивает от боли."
                "Ты непроизвольно происносишь пару непечатных выражений, после чего с трудом поднимаешься."
                play sound ds_sfx_int
                vic "Коробка, кажется, не пострадала. Впрочем, понять, пострадало ли содержимое, нельзя."
                play sound ds_sfx_fys
                edr "Ты тоже вроде живой, умирать не собираешься."
            play sound ds_sfx_psy
            vol "Итак, теперь тебе нужно отнести её Виоле."
            play sound ds_sfx_int
            lgc "Разве тебе не интересно, что внутри?"
            window hide
            menu:
                "Посмотреть содержимое" (skill='interfacing', level=lvl_challenging):
                    if ds_last_skillcheck.result():
                        window show
                        play sound ds_sfx_mot
                        inf "{result}Не вскрывай коробку - тут лучше остаться незамеченным. Просто аккуратно расширь щель между крышкой и стенкой."
                        "Ты так и делаешь."
                        play sound ds_sfx_mot
                        per_eye "В глуби коробки перед тобой предстают... детали? Да, это детали."
                        play sound ds_sfx_int
                        enc "Ты не имеешь ни малейшего представления о том, для чего они нужны."
                        play sound ds_sfx_psy
                        ine "Но у тебя есть ощущение, что это детали имеют какое-то отношение к твоему попаданию в лагерь."
                        th "Ладно, так я ничего нового не узнаю..."
                        "Ты отпускаешь края щели, берёшь коробку в руки и направляешься к выходу."
                    else:
                        window show
                        play sound ds_sfx_mot
                        inf "{result}Давай, открой коробку, и мы узнаем все тайны Виолы!"
                        "Скотч, скрепляющий края коробки, оказывается не очень прочным. Немного поднапрягвшись, ты разрываешь его."
                        "Перед тобой предстают какие-то детали."
                        play sound ds_sfx_int
                        enc "Ты не имеешь ни малейшего представления о том, для чего они нужны."
                        play sound ds_sfx_psy
                        ine "Но у тебя есть ощущение, что это детали имеют какое-то отношение к твоему попаданию в лагерь."
                        th "Ладно, так я ничего нового не узнаю..."
                        play sound ds_sfx_fys
                        hfl "Интересно, и что сделает с тобой Виола, когда узнает, что ты залез к ней в коробку."
                        $ ds_tampered_box = True
                        "Ты закрываешь коробку и направляешься с ней к выходу."
                    $ ds_seen_box_content = True
                "Отбросить мысль":
                    window show
                    "Ты берёшь коробку в руки и направляешься к выходу."
            scene bg ds_ext_old_camp_storage_day
            show cs normal medic2 at center
            with dissolve
            "Выйдя со склада, ты опускаешь коробку прямо перед Виолой."
            cs "Ну как, пионер. Вижу, ты принёс нужную коробку."
            if ds_tampered_box:
                show cs rage medic2 at center
                with dspr
                "А вот тут я не поняла... Почему коробка вскрыта?!"
                window hide
                menu:
                    "Убедить, что это не ты":
                        window show
                        me "Видимо, кто-то проник на склад. Вы когда его в последний раз смотрели?"
                        show cs doubt medic2 at center
                        with dspr
                        cs "Вчера я тут была, и тут никого не было."
                        cs "Правда, сами коробки я не проверяла... так что может быть, пионер."
                        "Виола открывает коробку и осматривает содержимое."
                        cs "Ладно, вроде всё целое."
                    "Признаться":
                        window show
                        me "Ну, мне было интересно, что там, вот я и открыл..."
                        cs "А если бы ты сломал что-нибудь? Испортил?! Тебе разрешали открывать?!"
                        $ ds_lp['cs'] -= 1
                        show cs tired medic2 at center
                        with dspr
                        "Виола открывает коробку и осматривает содержимое."
                        cs "Ладно, вроде всё целое. Но больше я на тебя полагаться не буду."
                        play sound ds_sfx_int
                        rhe "Это значит, что она тебя с собой больше не повезёт."
            else:
                $ ds_lp['cs'] += 1
                cs "Молодец."
        "Обратиться к Виоле":
            window show
            th "Нет уж, лучше попрошу Виолу помочь - а то мало ли..."
            scene bg ds_ext_old_camp_storage_day
            show cs normal medic2 at center
            with dissolve
            cs "А где коробка, пионер?"
            me "Понимаете, она высоко, и я не знаю, как её спустить..."
            show cs tired at center
            with dspr
            cs "Эх ты... И зачем только я брала тебя с собой?"
            cs "Ладно, покажи, где эта коробка, я сама уж спущу."
            me "Идёмте."
            scene bg ds_int_old_camp_storage
            show cs tired medic2 at center
            with dissolve
            "Ты отводишь Виолу к нужному стеллажу и указываешь на цель."
            me "Вот она. На самой верхней полке."
            cs "Стой тут."
            hide cs with dissolve
            "Виола уходит за лестницей."
            show cs normal medic3 at center
            with dissolve
            "Вернувшись, она ставит её к стеллажу, быстро взбирается, берёт коробку и возвращается к тебе."
            cs "Вот так-то, пионер!"
            play sound ds_sfx_mot
            svf "Ничего себе какая ловкость..."
            cs "Бери коробку и относи её на улицу."
            "Ты перехватываешь коробку у Виолы и выходишь с ней."
            scene bg ds_ext_old_camp_storage_day
            show cs normal medic3 at center
            with dissolve
            cs "Оставь её тут."
            "Ты опускаешь коробку наземь."
    cs "А теперь поехали."
    play sound ds_sfx_mot
    res "А коробка?"
    window hide
    menu:
        "Спросить про коробку":
            window show
            me "А как же коробка?"
            cs "Ей тут самое место - до поры до времени."
            me "Понятно..."
            play sound ds_sfx_int
            lgc "...что ничего не понятно."
        "Забить":
            window show
    hide cs with dissolve
    "Виола садится в машину. Ты следуешь за ней."
    window hide
    scene black
    with fade
    $ renpy.pause(5.0)
    scene bg ext_camp_entrance_day
    show cs normal medic2 at center
    with dissolve
    "Спуcтя полтора часа вы приезжаете в лагерь. Уже подошло время ужина."
    cs "До встречи, пионер."
    hide cs with dissolve
    "А ты направляешься в сторону столовой."
    $ ds_dv_has_coal = True
    jump ds_day4_dinner

label ds_day4_after_lunch_mt:
    $ persistent.sprite_time = 'day'
    scene bg ext_house_of_mt_day
    with dissolve
    "Ты подходишь к своему домику в надежде отсидеться там до вечера."
    th "Лишь бы там не оказалось вожатой, лишь бы не оказалось."
    play sound sfx_open_door_1
    scene bg int_house_of_mt_day
    show mt normal pioneer at center
    with dissolve
    mt "О, Семён, как поиски продвигаются?"
    th "Не повезло..."
    me "Нормально, только Шурика не нашёл."
    mt "Так, похоже, тебе придётся немного отвлечься от поисков."
    play sound ds_sfx_int
    rhe "Тебя готовятся грузить..."
    mt "Значит, смотри. Администрация к концу смены опомнилась и потребовала список пионеров по отрядам. С паспортными данными."
    mt "Вот на столе паспорта и форма отчёта. Заполни её."
    window hide
    menu ds_day4_mt_dialogue:
        set ds_menuset
        "Cогласиться":
            window show
            me "Хорошо, как скажете..."
            show mt smile at center
            with dspr
            mt "Молодец, Семён!"
            $ ds_lp['mt'] += 1
        "Спросить, почему не она":
            window show
            me "А почему вы сами это не сделаете?"
            show mt angry at center
            with dspr
            mt "Потому что я поручила это тебе, Семён!"
            window hide
            jump ds_day4_mt_dialogue
        "Спросить, почему на бумаге":
            window show
            me "А зачем мы на бумаге это выписываем? Разве нет ком... {w=0.2}ЭВМ?"
            show mt normal at center
            with dspr
            mt "Потому что администрация так захотела... Я тоже не понимаю, почему нельзя использовать ЭВМ."
            window hide
            jump ds_day4_mt_dialogue
        "Отказаться" (skill='authority', level=lvl_legendary):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_psy
                aut "{result}Ну нет, так не пойдёт. У тебя есть важные дела - а ещё это её работа. А ещё можно пожаловаться на её «ответственное отношение к работе»."
                me "А с чего я буду делать вашу работу? У меня есть и свои дела!"
                show mt angry at center
                with dspr
                mt "И какие же у тебя дела?!"
                me "Важные пионерские дела. А у вас ваши дела. Или хотите, чтобы я рассказал кому надо, что вы перекладываете свои обязанности на пионеров?"
                show mt surprise at center
                with dspr
                mt "Ладно, иди уже..."
                $ ds_lp['mt'] -= 1
                scene bg ext_house_of_mt_day
                with dspr
                jump ds_day4_after_lunch_map
            else:
                window show
                play sound ds_sfx_psy
                aut "{result}Она не имеет права! Начни кричать об этом!"
                me "Не буду я заниматься этим!"
                show mt angry at center
                with dspr
                mt "Будешь! А то накажу тебя! Без ужина оставлю!"
                aut "Серьёзная угроза... Похоже, тут ты проиграл..."
                window hide
                jump ds_day4_mt_dialogue
    scene cg ds_day4_work_mt
    with dspr
    play music ds_work fadein 3
    "Ты садишься за стол, где уже подготовлен лист с таблицей и пачка паспортов."
    "Ольга Дмитриевна же как ни в чём не бывало укладывается на кровать, открывает книгу и начинает читать."
    play sound ds_sfx_psy
    aut "Какая несправедливость! Она лежит, читает, а ты работаешь!"
    window hide
    menu:
        "Возмутиться":
            window show
            me "А вы не будете работать?"
            mt "А я уже отработала своё! И вообще, ты сам согласился..."
            aut "Ага, только выбора-то у тебя и не было..."
            $ ds_lp['mt'] -= 1
        "Смириться":
            window show
    "Ты берёшь в руку первую книжечку с золотыми буквами «СССР - ПАСПОРТ»."
    th "И кто же там?"
    play sound ds_sfx_mot
    per_eye "А встречает нас Двачевская Алиса Викентьевна. Первой графой в таблице как раз идёт «Ф.И.О.»"
    "Ты вписываешь туда фамилию, имя, отчество."
    per_eye "Серия и номер паспорта - IX-ЦД № ******"
    "Ты вписываешь это в нужное место и переворачиваешь страницу."
    per_eye "Дата рождения - 3 апреля 1972 года. Место рождения... {w}прочерк?"
    play sound ds_sfx_int
    lgc "Место рождения неизвестно. Только как это возможно?"
    window hide
    menu:
        "Спросить у Ольги Дмитриевны":
            window show
            me "У Алисы в паспорте в графе «место рождения» стоит прочерк. Что с этим делать?"
            "Ольга Дмитриевна отрывается от чтения."
            mt "А, да, видимо бюрократы паспортного стола напортачили. Оставляй прочерк."
            "Ты со спокойной душой ставишь прочерк и продолжаешь. Вожатая же вновь погружается в чтение."
        "Поставить прочерк":
            window show
            "Ты ставишь прочерк."
        "Придумать место рождения" (skill='conceptualization', level=lvl_easy):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_int
                con "{result}Какие есть интересные города... А пусть будет, скажем, Пермь! «Счастье не за горами», все дела."
                "Ты вписываешь «г. Пермь, РСФСР»."
            else:
                window show
                play sound ds_sfx_int
                con "{result}Впиши Москву и не парься!"
                "Ты вписываешь «г. Москва, РСФСР»."
    per_eye "Национальность - русская. Выдано отделом внутренних дел Работинского исполкома Калининской области 6 апреля 1986 г."
    "На этом первая строка таблицы оканчивается. Ты переходишь к следующей."
    per_eye "Унылова Елена Сергеевна. Серия и номер - X-ЯН № ******"
    "Ты переписываешь это."
    per_eye "Дата рождения - 25 сентября 1972 г. Место рождения - г. Работино, Калининская области, РСФСР."
    per_eye "Национальность - русская. Выдано тем же учреждением, 3 октября 1986 г."
    "Ты берёшь следующий паспорт."
    per_eye "Феоктистова Славяна Георгиевна - IX-ЕМ № ****** - 12 мая 1972 г. - дер. Мятусово, Ленинградская область, РСФСР - русская - выдано ОВД Подпорожского исполкома Ленинградской области 25 мая 1986 г."
    "Беря в руки следующий паспорт, ты обнаруживаешь вместо уже привычного серпа с молотом какую-то новую эмблему."
    per_eye "Сверху неё написано иероглифами, а снизу - более понятное тебе «JAPAN - PASSPORT»."
    if ds_skill_list['encyclopedia'].check(level=lvl_trivial, passive=True).result():
        play sound ds_sfx_int
        enc "{result}«Япония - паспорт». А эмблема - тоже государственный символ Японии. Очевидно, это японский паспорт."
    "Открыв его, ты видишь знакомое тебе лицо. Из паспорта на тебя смотрит Мику."
    window hide
    menu:
        "Спросить у Ольги Дмитриевны":
            window show
            me "А что делать с иностранными паспортами."
            "Вожатая с плохо скрываемым раздражением отрывается от чтения."
            mt "А, ты до Мику дошёл? Ну, знаешь английский? А если даже не знаешь - думаю, догадаешься, что откуда выписывать."
            play sound ds_sfx_int
            enc "На каком-то уровне английский ты знаешь, разберёшься."
            "Ольга Дмитриевна вновь уходит в книгу."
        "Начать заполнять":
            window show
    "В графу «Ф.И.О.» ты собираешься было вписывать фамилию-имя Мику."
    th "А как правильно написать - «Хацуне» или «Хатсуне»?"
    if ds_skill_list['encyclopedia'].check(level=lvl_medium, passive=True).result():
        play sound ds_sfx_int
        enc "{result}Согласно нормативной для русского языка системе Поливанова - «Хацуне»."
        play sound ds_sfx_psy
        ine "Однако, в тоннах прочитанных тобой постов на тему Мику использовался вариант «Хатсуне»."
        enc "Потому что анимешники зачастую переписывают имена с английской транскрипции по системе Хепбёрна - где (как ты и видишь в паспорте) получается «Hatsune»."
    window hide
    menu ds_day4_write_hatsune:
        set ds_menuset
        "Написать «Хацуне»":
            window show
            "Ты вписываешь в таблицу «Хацуне Мику» и следуешь дальше."
        "Написать «Хатсуне»":
            window show
            "Ты следуешь прочитанным тобой в интернете текстам и пишешь «Хатсуне Мику»."
        "Спросить у Ольги Дмитриевны":
            window show
            me "Ольга Дмитриевна, а вы не знаете, как правильно писать фамилию Мику?"
            play sound ds_sfx_psy
            emp "Ей определённо не нравится, что ты её постоянно дёргаешь."
            play sound ds_sfx_psy
            aut "А фиг ли она разлеглась с книжкой?"
            mt "В смысле? «Хацуне» - она и есть «Хацуне»."
            me "Я имею ввиду - через Ц или Т-С писать?"
            mt "А... вот тут не знаю... ну у тебя и вопросы..."
            "Сказав это, она самоустраняется, спрятавшись за книгой."
            window hide
            jump ds_day4_write_hatsune
    play sound ds_sfx_int
    lgc "За номер паспорта логично принять мешанину букв и цифр в верхнем правом углу."
    play sound ds_sfx_mot
    per_eye "VC1016002"
    per_eye "После фамилии с именем следует «JAPAN» и дата - «31 AUG 1972»."
    lgc "31 августа 1972 года."
    per_eye "Далее «Sex - F»."
    if ds_skill_list['instinct'].check(level=lvl_easy, passive=True):
        play sound ds_sfx_fys
        ins "{result}Кто-то сказал «секс»?"
        play sound ds_sfx_int
        enc "Успокойся - в английском это слово означает и «пол». В данном случае - женский."
    per_eye "«Registered Domicile - TOKYO»"
    lgc "А это что за фигня? Понятно только «Токио»."
    window hide
    menu:
        "Cпросить":
            window show
            me "Ольга Дмитриевна, а что такое «Registered domicile»?"
            mt "Не знаю я, не знаю!"
            play sound ds_sfx_psy
            emp "Она уже устала от твоих вопросов."
            mt "Напиши это в место рождения!"
            "Ты послушно вписываешь и переходишь дальше."
        "Вписать как место рождения":
            window show
            "Ты пишешь в графу «Место рождения» «г. Токио, Япония»"
        "Опустить":
            window show
            "Ты пропускаешь эту графу и идёшь дальше."
    per_eye "Date of issue - 20 MAY 1983. Date of expiry - 20 MAY 1993. Issuing authority - MINISTRY OF FOREIGN AFFAIRS."
    enc "Выдан 20 мая 1983 года министерством иностранных дел Японии."
    "Ты вписываешь эту информацию в соответствующие поля."
    th "Теперь должно быть попроще..."
    per_eye "Советова Ульяна Ильична - XII-ПБ № ****** - ... 1975 г. - г. Ульяновск, РСФСР - русская - выдано ОВД г. Ульяновск ... 1989 г."
    play sound ds_sfx_int
    vic "То-то этот паспорт выглядит новее остальных, совсем свежим."
    per_eye "Мицгол Евгения ... - IX-МГ № ****** - ... 1972 г. - г. Одесса, УССР - еврейка - выдано ОВД г. Одесса ... 1986 г."
    play sound ds_sfx_int
    dra "Женя таки из «богоизбранной» нации. Да ещё и прямиком с Одессы!"
    per_eye "Сыроежкин Сергей ... - IX-ЭЛ № ****** - ... 1972 г. - г. Москва, РСФСР - русский - выдано ... 1986 г."
    per_eye "Демьяненко Александр ... - IX-ШУ № ****** - ... 1972 г. - г. Москва, РСФСР - белорус - выдано ... 1986 г."
    play sound ds_sfx_psy
    vol "На этом всё! Переписав последний паспорт, ты откидываешь ручку и вздыхаешь."
    stop music fadeout 3
    mt "Всё, Семён?"
    me "Да!"
    scene bg ext_house_of_mt_day
    show mt smile pioneer at center
    with dissolve
    mt "Молодец! Можешь идти ужинать!"
    $ ds_lp['mt'] += 1
    "И ты удовлетворённо выдвигаешься в сторону столовой."
    jump ds_day4_dinner

label ds_day4_after_lunch_el:
    $ persistent.sprite_time = "day"
    scene bg ext_clubs_day
    with dissolve
    "Ты подходишь к клубу кибернетиков."
    show el normal pioneer at center
    with dissolve
    "Когда ты подходишь к двери, она распахивается, и навстречу тебе выходит Электроник."
    show el surprise pioneer at center
    with dissolve
    el "Семён, а что ты тут делаешь?"
    window hide
    menu:
        "Нужен Электроник":
            window show
            me "Мне нужен ты."
            show el normal pioneer at center
            with dspr
            el "А, ну пройдём в клуб тогда."
            $ ds_lp['el'] += 1
        "Решил зайти в клуб":
            window show
            me "Да так, просто в клуб решил зайти."
            el "Ну... заходи, только там никого нет, сам понимаешь."
            el "Пока!"
            hide el with dissolve
            "А ты заходишь в клуб."
            scene bg int_clubs_male_day
            with dissolve
            "Как и говорил Электроник - никого тут нет."
            play sound ds_sfx_psy
            vol "А это значит - в клубе тебе делать нечего. Ты тут сам не сориентируешься."
            th "Значит, пойдём в другое место..."
            $ disable_current_zone_ds_small()
            jump ds_day4_after_lunch_map
        "Просто прогулка":
            window show
            me "Да так, просто тут гуляю..."
            show el normal pioneer at center
            with dspr
            el "А, ну ладно, тогда пока!"
            hide el with dissolve
            th "Лучше будет пойти в другое место..."
            $ disable_current_zone_ds_small()
            jump ds_day4_after_lunch_map
    scene bg int_clubs_male_day
    show el normal pioneer at center
    with dissolve
    el "И что же тебя привело ко мне?"
    $ ds_talked_with_el = False
    window hide
    menu ds_day4_clubs_el_dialogue:
        set ds_menuset
        "Показать книгу" if ds_took_old_book:
            window show
            me "Смотри. Я сегодня раздобыл вот такую книгу. Сам я в ней ничего не понял, хотел у тебя спросить."
            "Электроник берёт книгу и начинает перелистывать её, пробегая содержимое страниц по диагонали."
            play sound ds_sfx_psy
            emp "В его глазах читается недоверие..."
            show el surprise pioneer at center
            with dspr
            emp "...сменяющееся удивлением..."
            show el shocked pioneer at center
            with dspr
            emp "..а затем шоком."
            el "Откуда у тебя это?"
            window hide
            menu:
                "Сказать про старый лагерь":
                    window show
                    me "Я сегодня до старого лагеря дошёл, и вот это там нашёл."
                    el "Видимо, старый лагерь не так прост..."
                "Отказаться отвечать":
                    window show
                    me "Неважно."
            me "Так что это такое?"
            el "Это монография... Которая способна перевернуть всю науку!"
            me "А конкретнее?"
            el "Насколько я понял из беглого просмотра, тут речь идёт о квантовой гравитации."
            if ds_skill_list['encyclopedia'].check(level=lvl_challenging, passive=True).result():
                play sound ds_sfx_int
                enc "{result}В рамках квантовой гравитации физики пытаются описать гравитацию с помощью средств квантовой физики. Если это получится - то это будет революцией в науке, т.к. позволит построить «теорию всего». На данный момент безуспешно."
            me "То есть?"
            el "Это то, над чем учёные бьются уже много десятилетий! А тут вот, ответ! Уравнение гравитации в квантовой форме!"
            play sound ds_sfx_int
            lgc "В порядке бреда - а не могут ли быть эти кванты связаны с твоим попаданием сюда?"
            window hide
            menu:
                "Спросить":
                    window show
                    me "А может ли быть это всё связано с путешествием между мирами?"
                    el "Да! Тут прямо описаны и решения, соответствующие червоточинам."
                    el "Вот, смотри!"
                    "Ты смотришь, но формулы выглядят для тебя мешаниной латинских и греческих букв и непонятных значков."
                    el "Тут описано решение для чёрных дыр, из которых следует, что то, что в ОТО давало сингулярность, на самом деле является «кротовой норой»."
                    el "И каждой чёрной дыре где-то в другой точке пространства-времени соответствует белая дыра."
                    if ds_skill_list['encyclopedia'].check(level=lvl_medium, passive=True):
                        play sound ds_sfx_int
                        enc "{result}Ну, это ты знаешь. Чёрные дыры - объекты, чьё гравитационное притяжение в пределах так называемого горизонта событий не может преодолеть даже свет."
                        enc "А в белую дыру, напротив, невозможно попасть."
                    el "И это значит, что если получится создать чёрную дыру - то можно будет куда-то попасть. Если, конечно, удастся пережить приливные силы."
                    el "Да, микроскопическая чёрная дыра позволит быстро переместиться куда-то!"
                    el "Вот только куда?.. Соответствующие системы уравнений выглядят слишком сложными, чтобы решить их вручную."
                    lgc "Получается, кто-то, используя эти знания, сгенерировал возле тебя чёрную дыру, которая тебя засосала и выплюнула в «Совёнке»?"
                "Отбросить мысль":
                    window show
            show el normal pioneer at center
            with dspr
            el "Тут на обложке стоит гриф «СЕКРЕТНО». Тебе бы избавиться от неё..."
            me "Ну..."
            el "Хотя ладно, оставь мне! Я изучу подробее!"
            el "Не полезет же КГБ в пионерлагерь за секретными документами!"
            play sound ds_sfx_fys
            hfl "Как знать, как знать... Тебя накрывает нехорошее предчувствие..."
            window hide
            menu:
                "Отдать книгу":
                    window show
                    me "Ладно, бери."
                    show el smile pioneer at center
                    with dspr
                    el "Спасибо, Семён! Ты оказал неоценимую услугу науке!"
                    $ ds_lp['el'] += 1
                "Оставить книгу себе":
                    window show
                    me "Нет, не хочу тебя опасности подвергать... Лучше у себя подержу."
                    show el upset pioneer at center
                    with dspr
                    el "Ну ладно, как скажешь..."
            window hide
            $ ds_talked_with_el = True
            jump ds_day4_clubs_el_dialogue
        "Предложить провести время вместе":
            window show
            me "Да так, знаешь... может, проведём время {i}вместе{/i}? Посидим, поговорим, то, сё..."
            show el shocked pioneer at center
            with dspr
            play sound ds_sfx_psy
            emp "Для Электроника твоё предложение оказывается полной неожиданностью."

        "Предложить помощь":
            window show
            me "Может, тебе помочь чем-нибудь?"
            show el upset pioneer at center
            with dspr
            el "Спасибо, конечно... но нет, не требуется."
            el "Я тут без Шурика ничего делать не собираюсь, и тебе не стоит. Он тут главный всё-таки."
            me "Ну ладно, как скажешь..."
        "Это всё" if ds_talked_to_el:
            window show
            me "Это всё!"
            show el normal pioneer at center
            with dspr
            el "Ладно."
    el "Вообще, я собираюсь сейчас пойти поискать Шурика. И ты поищи!"
    me "Эм... ну ладно..."
    if ds_talked_to_el:
        play sound sfx_open_door_clubs
        show dv surprise pioneer2 at left
        show us surp1 sport at right
        with dissolve
        "Однако, тут в клуб заходят Алиса и Ульяна. Они удивлены вашим присутствием не меньше, чем вы - их."
        play sound ds_sfx_fys
        hfl "И что эти двое забыли в клубе кибернетиков?"
        if ds_skill_list['logic'].check(level=lvl_easy, passive=True).result():
            play sound ds_sfx_int
            lgc "{result}Очевидно, им для очередной шалости понадобилось что-то из технических приблуд из клуба."
        show el surprise pioneer at center
        with dspr
        el "А... что вам тут надо?"
        show dv angry pioneer2 at left
        with dspr
        dv "Уже неважно! Пойдём, Ульяна!"
        $ ds_lp['dv'] -= 1
        $ ds_lp['us'] -= 1
        show us upset sport at right
        with dspr
        us "Ну вот..."
        hide dv
        hide us
        with dissolve
        play sound sfx_close_door_1
        "Хлопок закрывающейся двери прерывает жалобную речь Ульяны."
        show el normal pioneer at center
        with dspr
        el "Небось, опять что-то украсть хотели, чтобы напроказничать!"
        el "Но в этот раз у них ничего не вышло!"
    play sound sfx_open_door_clubs
    scene bg ext_clubs_day
    show el normal pioneer at center
    with dspr
    "Вы выходите."
    el "Ладно, пока!"
    hide el with dissolve
    "Электроник убегает, а ты прикидываешь, куда тебе пойти дальше."
    $ disable_current_zone_ds_small()
    jump ds_day4_after_lunch_map

label ds_day4_after_lunch_mz:
    $ persistent.sprite_time = "day"
    scene bg ext_library_day
    with dissolve
    "Ты подходишь к библиотеке."
    if (ds_dv_intercepted_stage <= 1) and (ds_lp['dv'] >= 25):
        show dv normal pioneer2 at center
        with dissolve
        "Возле входа ты наталкиваешься на Алису, выходящую из библиотеки."
        play sound ds_sfx_int
        lgc "Вот уж кого ты меньше всего ожидал увидеть в библиотеке - так это Алису."
        show dv angry pioneer2 at center
        with dspr
        dv "Что уставился?"
        if ds_skill_list['perception'].check(level=lvl_easy, passive=True).result():
            play sound ds_sfx_mot
            per_eye "В руках у неё какая-то книга. Однако, разглядеть название невозможно."
            window hide
            menu:
                "Спросить про книгу":
                    window show
                    me "А что за книга у тебя в руках?"
                    show dv shy pioneer2 at center
                    with dspr
                    $ renpy.pause(0.2)
                    show dv angry pioneer2 at center
                    with dspr
                    play sound ds_sfx_mot
                    res "На секунду Алиса смутилась от твоего вопроса."
                    play sound ds_sfx_int
                    rhe "От вопроса про книгу?"
                    play sound ds_sfx_psy
                    emp "Видимо, с этой книгой связано что-то личное. Лучше не напирать."
                    "Впрочем, Алиса быстро возвращается в своё привычное агрессивное состояние."
                    dv "Не твоё дело! Иди куда шёл!"
                    rhe "И всё-таки, это она из вредности, или что-то есть в этой книге."
                    play sound ds_sfx_fys
                    hfl "Да сто процентов это план для новой шалости!"
                    window hide
                    menu:
                        "Вырвать книгу" (check='savoir_faire', level=lvl_up_medium):
                            if ds_last_skillcheck.result():
                                window show
                                play sound ds_sfx_mot
                                svf "{result}Тебе ловкими движениями удаётся выхватить у Алисы книгу, прежде чем она успевает сообразить, что произошло."
                                per_eye "«Унесённые ветром»"
                                hfl "Да ну? Не «Поваренная книга анархиста»?"
                                $ ds_lp['dv'] -= 1
                                if ds_know_un_book:
                                    th "Такая же книга была у Лены..."
                                show dv rage pioneer2 at center
                                with dspr
                                dv "Всё? Насмотрелся? Доволен?"
                                window hide
                                menu:
                                    "Извиниться":
                                        window show
                                        me "Извини, пожалуйста, мне просто интересно было..."
                                        dv "Отстань!"
                                        play sound ds_sfx_psy
                                        emp "Она не собирается обсуждать с тобой эту тему."
                                        dv "Иди, куда шёл!"
                                        hide dv with dissolve
                                        "И она уходит - вернее, убегает."
                                    "Посмеяться":
                                        window show
                                        me "Ты читаешь это? Как можно такое читать? От тебя уж точно не ожидал..."
                                        dv "Замолчи! А то урою!"
                                        if ds_skill_list['empathy'].check(level=lvl_easy, passive=True).result():
                                            play sound ds_sfx_psy
                                            emp "{result}Для неё это дело деликатное..."
                                        $ ds_lp['dv'] -= 1
                                        hide dv with dissolve
                                        "И она уходит, даже не попрощавшись."
                                    "Cказать про Лену" if ds_know_un_book:
                                        window show
                                        me "У Лены была..."
                                        play sound sfx_angry_ulyana
                                        "Алиса не даёт тебе договорить."
                                        dv "Я тебе сейчас!.."
                                        "Она замахивается на тебя."
                                        if ds_skill_list['half_light'].check(level=lvl_medium, passive=True).result():
                                            play sound ds_sfx_fys
                                            hfl "{result}Ты машинально ставишь блок, готовясь принять удар."
                                        "Но через секунду опускает руку. Бить тебя она не собирается - пока."
                                        $ ds_lp['dv'] -= 3
                                        dv "Вали отсюда, пока живой..."
                                        "Она процедила это сквозь зубы."
                                        show dv rage pioneer2 far at center
                                        with dspr
                                        "Ты и пододвигаешься в сторону библиотеки - и подальше от Алисы."
                                        hide dv with dissolve
                                        "Алиса же убегает."
                                    "Промолчать":
                                        window show
                                        "Ты молча переводишь взгляд то на книгу, то на Алису."
                                        show dv angry pioneer2 at center
                                        with dspr
                                        dv "Ну и?"
                                        me "Что?"
                                        dv "Ничего, идиот!"
                                        hide dv with dissolve
                                        "И она уходит."
                                play sound ds_sfx_mot
                                res "Книга, кстати, так и осталась у тебя в руках."
                                $ ds_have_dv_book = True
                            else:
                                window show
                                play sound ds_sfx_mot
                                svf "{result}Ты хватаешься за книгу. Но Алиса не собирается её просто так уступать тебе."
                                show dv rage pioneer2 close at center
                                with dspr
                                $ ds_lp['dv'] -= 1
                                dv "Отстань! Что ты прицепился ко мне?!"
                                me "Ну дай книгу посмотреть!"
                                dv "Не дам, она моя, придурок!"
                                dv "Извращенец, клеишься ко мне, да ещё в буквальном смысле!"
                                me "Да я книгу хочу глянуть! Может, она и мне интересна будет!"
                                dv "Да вам всем одно только нужно!"
                                if ds_skill_list['reaction_speed'].check(level=lvl_easy, passive=True).result():
                                    play sound ds_sfx_mot
                                    res "{result}Что «одно»?"
                                    window hide
                                    menu:
                                        "Cпросить":
                                            window show
                                            me "Ты о чём?"
                                            dv "Ты и сам прекрасно понимаешь! Отвянь!"
                                            if ds_skill_list['suggestion'].check(level=lvl_challenging, passive=True).result():
                                                play sound ds_sfx_psy
                                                sug "{result}Подозреваю, речь идёт о сексе."
                                                play sound ds_sfx_fys
                                                ins "Это да, это мы хотим!"
                                                play sound ds_sfx_psy
                                                vol "Но не только же это! Не животные же."
                                        "Отвергнуть":
                                            window show
                                            me "Это неправда!"
                                            dv "Да вы все так говорите! Отлипни от меня, идиот!"
                                        "Подтвердить":
                                            window show
                                            me "Это да, тут ты права!"
                                            "И ты строишь гримасу не то заговорщика, не то канонического интернет-тролля."
                                            dv "Ты издеваешься надо мной?! Придурок! Изврат!"
                                            $ ds_lp['dv'] -= 1
                                        "Проигнорировать":
                                            window show
                                "Наконец, книге надоедают ваши издевательства, и она выскальзывает из рук, падая на пол."
                                play sound sfx_bodyfall_1 
                                show dv scared pioneer2:
                                    zoom 1.28
                                    ease 0.2 zoom 1.0
                                with vpunch
                                "Вы с Алисой разлетаетесь и падаете на землю."
                                if ds_skill_list['pain_threshold'].check(level=lvl_medium, passive=True).result():
                                    play sound ds_sfx_fys
                                    pat "{result}Не страшно! Земля мягкая, тебе не больно."
                                else:
                                    play sound ds_sfx_fys
                                    pat "{result}Твоей пятой точке это, мягко говоря, неприятно."
                                    $ ds_health.damage()
                                play sound ds_sfx_mot
                                per_eye "Алиса также плюхнулась на землю."
                                play sound ds_sfx_int
                                vic "Cтоит заметить, ей куда менее комфортно, чем тебе - у неё задралась юбка, и приземлилась она прямо голым, извините за выражение, задом."
                                play sound ds_sfx_fys
                                ins "Какой вид должен открыться там!"
                                "Но Алиса вскакивает, не давая тебе ни шанса - впрочем, и без того призрачного - взглянуть под юбку."
                                show dv angry pioneer at center
                                with dspr
                                dv "Чего расселся? Иди куда шёл!"
                                hide dv with dissolve
                                "Алиса убегает. Даже не подняв книгу."
                                "Ты встаешь на ноги, думая, что с ней делать."
                                window hide
                                menu:
                                    "Оставить книгу":
                                        window show
                                        th "Вернётся и подберёт, что мне с того?"
                                    "Взять книгу":
                                        window show
                                        "Ты поднимаешь книгу с земли."
                                        play sound ds_sfx_mot
                                        per_eye "«Унесённые ветром»"
                                        if ds_know_un_book:
                                            th "Такая же у Лены была..."
                                "Ты направляешься прямиком в библиотеку."
                        "Потребовать сказать" (skill='authority', level=lvl_heroic):
                            if ds_last_skillcheck.result():
                                window show
                                play sound ds_sfx_psy
                                aut "{result}А ну-ка собрал всю свою волю в кулак! Ты командуешь балом! Скажи громко и чётко!"
                                me "Я требую, чтобы ты показала мне книгу!"
                                show dv shocked pioneer2 at center
                                with dspr
                                "Алиса впадает в ступор. Впрочем, ненадолго."
                                show dv angry pioneer2 at center
                                with dspr
                                dv "Не кричи на меня! И не командуй мной! Ничего я тебе не покажу!"
                                hide dv with dspr
                                "И Алиса убегает быстрее ветра."
                                $ ds_lp['dv'] -= 1
                                if ds_skill_list['empathy'].check(level=lvl_easy, passive=True).result():
                                    play sound ds_sfx_psy
                                    emp "{result}Ты затронул нечто очень личное, можно сказать, деликатное..."
                            else:
                                window show
                                play sound ds_sfx_psy
                                aut "{result}Начни умолять. Молить, просить, плакать, чтобы она показала! Это точно сработает!"
                                me "Пожалуйста, дай мне книгу... посмотреть... я только одним глазком."
                                show dv grin pioneer2 at center
                                with dspr
                                "Агрессия на лице Алисы сменяется насмешкой."
                                dv "Ты ещё, ещё поплачь! Тогда точно дам!"
                                play sound ds_sfx_psy
                                vol "Над тобой смеются!"
                                $ ds_morale.damage()
                                me "Правда?"
                                show dv angry pioneer2 at center
                                with dspr
                                dv "Нет, конечно, придурок! Катись, куда шёл, и не позорься!"
                                hide dv with dissolve
                                "И, гордо задрав голову, Алиса удаляется."
                        "Отступить":
                            window show
                            me "Ладно, как скажешь..."
                            dv "Да, как скажу. И я скажу - иди, куда шёл! Бывай!"
                            hide dv with dissolve
                            "И Алиса уходит, не удостаивая тебя даже взглядом."
                "Проигнорировать":
                    window show
                    me "Ничего, я в библиотеку шёл..."
                    dv "Вот и иди туда! А я пошла отсюда!"
                    hide dv with dissolve
                    "Ты же идёшь в противоположную сторону - к библиотеке."
        else:
            me "Ничего, я в библиотеку шёл..."
            dv "Вот и иди туда! А я пошла отсюда!"
            hide dv with dissolve
            "И Алиса убегает прежде чем ты успеваешь спросить, что она делала в библиотеке."
        $ ds_dv_intercepted_stage = 1
    else:
        th "Интересно, Женя там? Наверняка должна быть там, где ей ещё быть!"
    play sound sfx_open_dooor_campus_1
    scene bg int_library_day
    with dissolve
    "Библиотека как обычно пустынна."
    "За столом ты примечаешь Женю..."
    scene cg d2_micu_lib
    with dissolve
    "...снова спящую."
    window hide
    menu:
        "Разбудить":
            window show
            "Ты начинаешь тормошить Женю."
            "Но безуспешно - она не просыпается."
        "Оставить в покое":
            window show
            th "Лучше не буду её трогать - пусть высыпается."
        "Положить книгу тихо" if ds_have_dv_book:
            window show
            "Ты тихонько, стараясь не разбудить Женю, кладёшь «Унесённых ветром» на стол."
        "Хлопнуть книгой" if ds_have_dv_book:
            window show
            "Ты как можно громче хлопаешь «Унесёнными ветром» о стол."
            "Однако, Женя не просыпается."
            play sound ds_sfx_psy
            vol "Оставь её в покое - сейчас она всё равно не проснётся."
    th "Итак, и чем же мне тут заняться?"
    play sound ds_sfx_int
    lgc "Очевидно, либо почитать что-нибудь - либо уйти."
    window hide
    menu:
        "Почитать художетвенную литературу":
            window show
        "Почитать научную литературу":
            window show

        "Почитать педагогическую литературу":
            window show
            "Обойдя пару шкафов, ты находишь «Педагогическую поэму» Макаренко."
            th "Должно подойти."
            "Ты распахиваешь книгу и погружаешься в чтение."
            book "Воспитатель всегда должен начинать процесс воспитания с себя самого. И именно к себе предъявлять наиболее высокие требования."
            play sound ds_sfx_psy
            vol "Позволь заметить: это не только для педагогики важно."
            book "Когда человек получает жалованье, так у него появляется столько идей, что их некуда девать. А когда у него нет денег, так у него одна идея: у кого бы занять? Это же факт."
            book "Человек не может жить на свете, если у него нет впереди ничего радостного. Истинным стимулом человеческой жизни является завтрашняя радость."
            book "И так же бывают разные случаи, так же иногда топорщатся характеры, и так же временами, как в улье, тревожно гудит коллектив и бросается в опасное место. И все такой же трудной и хитрой остается наука педагогика."
            book "Кража в коллективе вызывает к жизни раскрытие тайных дум, уничтожает необходимую деликатность и терпеливость коллектива, что особенно гибельно в обществе, состоящем из «правонарушителей»."
            book "Воспитать человека – значит воспитать у него перспективные пути, по которым располагается его завтрашняя радость."
            book "Почему в технических вузах мы изучаем сопротивление металлов, а в педагогических не изучаем сопротивление личности, когда ее начинают воспитывать? А ведь для всех не секрет, что такое сопротивление имеет место."
            book "Вопрос педагогической техники. Технику можно вывести только из опыта. Законы резания металлов не могли бы быть найдены, если бы в опыте человечества никто никогда металлов не резал. Только тогда, когда есть технический опыт, возможно изобретение, усовершенствование, отбор и браковка."
            book "Когда-нибудь настоящая педагогика разработает этот вопрос, разберет механику человеческого усилия, укажет, какое место принадлежит в нем воле, самолюбию, стыду, внушаемости, подражанию, страху, соревнованию и как все это комбинируется с явлениями чистого сознания, убежденности, разума."
            book "Для нас мало просто «исправить» человека, мы должны его воспитать по-новому, то есть должны воспитать так, чтобы он сделался не просто безопасным или безвредным членом общества, но чтобы он стал активным деятелем новой эпохи."
            play sound ds_sfx_int
            rhe "Коммунистической."
            book "Всегда ли можно «спасти воспитанием» или бывают случаи, когда самый талантливый педагог уже не сможет ничего сделать?"
            play sound ds_sfx_psy
            sug "Вот и вопрос к тебе. Как ты считаешь?"
            window hide
            menu:
                "Можно спасти всегда":
                    window show
                    th "Я думаю, да, правильный подход к детям творит чудеса!"
                    sug "А ты не думал, что тебе стоит сеять разумное, доброе, вечное?"
                    th "Да, думаю, можно было бы попробовать..."
                    sug "Так действуй! Начни с малого - устройся помощником к кому-нибудь из вожатых."
                    $ ds_special_traits['teach'] += 1
                "Не всегда":
                    window show
                    th "Думаю, некоторые дети безнадёжны. Как и взрослые."
                    sug "Ты уверен?"
                    th "Ну... да..."
                "Отвергнуть детей":
                    window show
                    th "Да ну её, эту педагогику, и детей тоже! Надоедливые такие и мелкие!"
                    $ ds_special_traits['teach'] -= 1
            "Ты закрываешь книгу и кладёшь её на полку."
        "Почитать коммунистическую литературу":
            window show
            "На первых же полках тебя встречают многочисленные полные собрания сочинений Маркса, Ленина и прочих корифеев коммунизма."
            th "А есть что-нибудь более... фундаментальное?"
            play sound ds_sfx_mot
            per_eye "Есть. На полке выше ты замечаешь «Капитал»."
            play sound ds_sfx_int
            enc "Opus magnum Карла Маркса."
            th "Давайте её тогда..."
            "Ты берёшь толстый том и приступаешь к чтению."
            book "Богатство обществ, в которых господствует капиталистический способ производства, выступает как «огромное скопление товаров», а отдельный товар – как элементарная форма этого богатства. Наше исследование начинается поэтому анализом товара."
            book "Товар есть прежде всего внешний предмет, вещь, которая, благодаря ее свойствам, удовлетворяет какие-либо человеческие потребности. Природа этих потребностей, – порождаются ли они, например, желудком или фантазией, – ничего не изменяет в деле Дело также не в том, как именно удовлетворяет данная вещь человеческую потребность: непосредственно ли, как жизненное средство, т. е. как предмет потребления, или окольным путем, как средство производства."
            "Ты погружаешься в книгу, отмечая для себя в голове отдельные тезисы."
            book "Не сознание людей определяет их бытие, а, наоборот, их общественное бытие определяет их сознание."
            book "Своеобразный характер материала, с которым имеет дело политическая экономия, вызывает на арену борьбы против свободного научного исследования самые яростные, самые низменные и самые отвратительные страсти человеческой души — фурий частного интереса."
            book "Чем более способен господствующий класс принимать в свою среду самых выдающихся людей из угнетенных классов, тем прочнее и опаснее его господство."
            book "В мануфактуре и ремесле рабочий заставляет орудие служить себе, на фабрике он служит машине."
            book "Капитализм стремится уничтожить оба источника своих богатств: природу и человека."
            book "Стоимость рабочей силы определяется стоимостью привычно необходимых жизненных средств среднего рабочего."
            book "Машина, которая не служит в процессе труда, бесполезна."
            book "При всякой спекуляции с акциями каждый знает, что гроза когда-нибудь да грянет, но каждый надеется, что она разразится над головой его ближнего уже после того, как ему самому удастся собрать золотой дождь и укрыть его в безопасном месте."
            book "На жалобы относительно физического и духовного калечения, преждевременной смерти, истязаний чрезмерным трудом он отвечает: как могут терзать нас эти муки, если они увеличивают наше наслаждение (прибыль)?"
            book "Экономические эпохи различаются не тем, что производится, а тем, как производится, какими средствами труда."
            book "Раньше рабочий продавал свою собственную рабочую силу, которой он располагал как формально свободная личность. Теперь он продаёт жену и детей. Он становится работорговцем."
            book "Борьба между капиталистом и наёмным рабочим начинается с самого возникновения капиталистического отношения."
            book "Способность к труду ещё не означает труд."
            book "Если способность к труду не может быть продана, рабочему от неё нет никакой пользы."
            book "Товар, который функционирует в качестве меры стоимости, а поэтому также, непосредственно или через своих заместителей, и в качестве средства обращения, есть деньги."
            book "Стоимость рабочей силы определяется рабочим временем, необходимым для существования не только отдельного взрослого рабочего, но и рабочей семьи."
            book "Если машина является наиболее могущественным средством увеличения производительности труда, т. е. сокращения рабочего времени, необходимого для производства товаров, то как носительница капитала она становится, прежде всего, в непосредственно захваченных его отраслях промышленности, наиболее могущественным средством удлинения рабочего дня дальше всех естественных пределов."
            book "Капиталист знает, что всякие товары, какими бы оборвышами они ни выглядели, как бы скверно они ни пахли, суть деньги в духе и истине, евреи внутреннего обрезания, и к тому же чудотворное средство из денег делать большее количество денег."
            book "Деньги как деньги и деньги как капитал сначала отличаются друг от друга лишь неодинаковой формой обращения."
            book "Итак, стоимость рабочей силы сводится к стоимости определённой суммы жизненных средств."
            book "Кто говорит о способности к труду, тот не отвлекается от жизненных средств, необходимых для её поддержания."
            book "Невежество есть мать промышленности, как и суеверий. Сила размышления и воображения подвержена ошибкам; но привычка двигать рукой или ногой не зависит ни от того, ни от другого. Поэтому мануфактуры лучше всего процветают там, где наиболее подавлена духовная жизнь, так что мастерская может рассматриваться как машина, части которой составляют люди."
            book "Если рассматривать машины исключительно как средство удешевления продукта, то граница их применения определяется тем, что труд, которого стоит их производство, должен быть меньше того труда, который замещается их применением."
            play sound ds_sfx_int
            rhe "Дело, однако, пишет Маркс. Всё ведь именно так и есть!"
            play sound ds_sfx_fys
            edr "{i}Das ist Quatsch, mein Brüder{/i}! Одни люди природой предрасположены к доминированию над другими. Мужчины - над женщинами, белые - над цветными, более успешные - над менее."
            rhe "Ну вот, я же говорю - Маркс как раз про это и пишет."
            window hide
            menu:
                "Принять марксизм":
                    window show
                    th "Да, пожалуй, великим человеком был Маркс. С каждой мыслью согласен!"
                    $ ds_special_traits['marx'] += 1
                    play sound ds_sfx_int
                    rhe "Готовь расстрельную команду!"
                    th "Зачем?"
                    rhe "Ну как же - врагов народа истреблять!"
                    edr "Вот именно - при царе-батюшке такого не было!"
                    th "Каких врагов народа. У нас же тут и так социализм!"
                    rhe "Cоциализм - это лишь первая стадия коммунизма. А этих стадий ещё много - путь тернист."
                    th "А без расстрелов никак?"
                    rhe "Никак, товарищ. Но ради светлого будущего разве ты не готов?"
                    window hide
                    menu:
                        "Принять с энтузиазмом":
                            window show
                            th "Всегда готов!"
                        "Смириться":
                            window show
                            th "Ну, если для коммунизма надо..."
                        "Отказаться расстреливать":
                            window show
                            th "Я построю коммунизм без расстрелов!"
                            rhe "Другие тоже так думали... А в итоге врагов оказалось куда больше. Думаешь, капиталисты просто так отдадут власть пролетариату?"
                        "Передумать":
                            window show
                            th "Нет, я не хочу так играть!"
                            rhe "Так и запишем: враг народа..."
                            th "Эй!"
                            $ ds_special_traits['marx'] -= 1
                "Принять {s}фашизм{/s}традиционализм":
                    window show
                    th "Да, я буду самым главным. Cамым главным после царя! И в обществе воцарится гармония!"
                    play sound ds_sfx_int
                    rhe "Угу, капитализм, счастье, з*****ь!"
                    $ ds_special_traits['marx'] -= 1
                    play sound ds_sfx_fys
                    edr "{i}Das ist fantastisch{/i}! Расчехляй {i}Gasenwagen{/i}!"
                    th "З-зачем?"
                    edr "Истреблять расово неполноценных, конечно! И врагов государства, заодно! В частности - мерзких коммуняк!"
                    edr "Развалили великую Империю и пируют на её остатках, прикрываясь «властью народа»!"
                    th "А без газовых камер никак?"
                    edr "Никак нет, мой друг! Ну так что, вперёд, к светлому будущему?"
                    window hide
                    menu:
                        "Принять с энтузиазмом":
                            window show
                            th "Да! За веру, царя и отечество!"
                        "Принять формально":
                            window show
                            th "Ладно..."
                            edr "Не вижу победного настроя! Будущий {i}Führer{/i} должен быть решителен!"
                        "Отвергнуть":
                            window show
                            th "Это не по мне! Я не согласен убивать!"
                            edr "Предатель Империи! Такие, как ты, и позволили большевикам ввергнуть Россию в мрак!"
                "Остаться нейтральным":
                    window show
                    th "Нет, идеологические баталии - это не по мне."
            "Ты захлопываешь книгу и кладёшь её на место."
        "Уйти":
            play sound sfx_open_door_campus_1
            scene bg ext_library_day
            with dissolve
            "Ты выходишь из библиотеки и думаешь, куда бы тебе пойти дальше."
            $ disable_current_zone_ds_small()
            jump ds_day4_after_lunch_map

label ds_day4_after_lunch_mi:
    $ persistent.sprite_time = 'day'
    scene bg ext_musclub_day
    with dissolve
    "Ты направляешься в сторону музыкального клуба. Зачем - ты пока не решил."
    play sound sfx_open_door_clubs_2
    scene bg int_musclub_day
    show mi normal pioneer at center
    with dissolve
    play music music_list["so_good_to_be_careless"] fadein 3
    "В музклубе тебя - совершенно предсказуемо - встречает Мику. Твой приход вызывает очередной словесный артобстрел."
    show mi smile pioneer at center
    with dspr
    mi "Привет-привет, Семён-кун, как ты поживаешь? Как у тебя дела? Я слышала, что ваш товарищ потерялся, вы его ещё не нашли?"
    mi "Ой, кстати, мне ты как раз и был нужен! Помнишь, я говорила про прощальный концерт. Нам нужен третий, и я думаю, ты подойдёшь идеально!"
    play sound ds_sfx_psy
    sug "Кажется, это мероприятие - идеальная возможность сблизиться с Мику."
    play sound ds_sfx_psy
    vol "Ага, только помнится мне, тут есть ещё одна переменная, известная под прозвищем «Дваче». Как она к этому отнесётся?"
    play sound ds_sfx_psy
    aut "О боже мой, да всем... плевать! Сказали, что будем участвовать - значит, будем, никакая Двачевская нам не помешает. Тем более, нас Мику позвала."
    play sound ds_sfx_int
    rhe "Мы ещё не сказали. Нам и предлагается решить."
    window hide
    menu ds_day4_concert:
        set ds_menuset
        "Согласиться с энтузиазмом":
            window show
            me "Да, конечно я буду рад поучаствовать!"
            show mi happy pioneer at center
            with dspr
            "От радости Мику начинает подпрыгивать и хлопать в ладоши."
            mi "Отличненько, раз ты согласен, значит, сейчас мы всё решим, всё распределим, всё подготовим, всё-всё-всё!"
            $ ds_lp['mi'] += 2
        "Cделать одолжение":
            window show
            me "Ну ладно... раз ты так просишь..."
            show mi happy pioneer at center
            with dspr
            "От радости Мику начинает подпрыгивать и хлопать в ладоши."
            mi "Отличненько, раз ты согласен, значит, сейчас мы всё решим, всё распределим, всё подготовим, всё-всё-всё!"
            $ ds_lp['mi'] += 1
        "Cпросить про мнение Алисы":
            window show
            me "Ну не знаю... а как Алиса к этому отнесётся?"
            show mi confused pioneer at center
            with dspr
            "До Мику не сразу доходит, о чём ты говоришь."
            show mi laugh pioneer at center
            with dspr
            mi "Да ладно тебе, я уверена, Алиса-тян будет только рада третьему в нашей команде, да к тому же мальчику!"
            play sound ds_sfx_psy
            sug "И откуда у неё такая уверенность в этом? Как раз непохоже на то, что Двачевской кто-то нужен."
            if ds_skill_list['encyclopedia'].check(level=lvl_challenging, passive=True).result():
                play sound ds_sfx_int
                enc "Уж кому, как не японке Мику знать, знать о берущем своё происхождении из японского понятии «цундере»?"
            window hide
            jump ds_day4_concert
        "Отложить решение на потом":
            window show
            me "Ну... мне надо подумать..."
            show mi normal pioneer at center
            with dspr
            mi "Хорошо, подумай, конечно, только тебе надо завтра уже точно сказать, так как тогда уже точно надо будет репетиции начинать, иначе мы не успеем подготовиться, и всё будет плохо!"
            me "Я понял..."
            mi "Ладно, тогда не буду тебя задерживать, Семён-кун, пока-пока! Мне надо бежать!"
            hide mi with dissolve
            "И Мику убегает. Ты тоже выходишь из клуба."
            play sound sfx_open_door_clubs_2
            scene bg ext_musclub_day
            with dissolve
            $ disable_current_zone_ds_small()
            jump ds_day4_after_lunch_map
        "Отказаться":
            window show
            me "Я как-то не готов выступать на публике, участвовать в подобном мероприятии, да и играю я так себе..."
            show mi upset pioneer at center
            with dspr
            mi "Очень жаль, что так... Я бы очень хотела, чтобы ты поучаствовал, но раз ты не хочешь - заставлять тебя не буду."
            show mi normal pioneer at center
            with dspr
            mi "Ладно, тогда я побежала! Пока-пока, Семён-кун."
            hide mi with dissolve
            "И Мику убегает. Ты тоже выходишь из клуба."
            play sound sfx_open_door_clubs_2
            scene bg ext_musclub_day
            with dissolve
            $ ds_concert_status = -1
            $ disable_current_zone_ds_small()
            jump ds_day4_after_lunch_map
    stop music fadeout 3
    $ ds_concert_status = 1
    "Мику подбегает к столу, подхватывает лежащую на нём стопку листов и возвращается к тебе."
    "Она протягивает листы к тебе - на них напечатаны ноты."
    show mi smile pioneer at center
    with dspr
    mi "Вот, смотри. Вот это я написала к нашему концерту."
    if not ds_skill_list['encyclopedia'].check(level=lvl_up_medium, passive=True).result():
        play sound ds_sfx_int
        enc "{result}Ноты для тебя являются чем-то вроде китайской грамоты."
    mi "Тебе надо будет выбрать один инструмент - на выбор есть бас-гитара или синтезатор."
    mi "А ещё кому-то нужно сидеть за пультиком, который звук в колонках делает громче-тише."
    mi "А раз ты пришёл сейчас - можешь выбрать!"
    window hide
    menu ds_day4_choose_instrument:
        set ds_menuset
        "Выбрать бас-гитару":
            window show
            $ ds_instrument_chosen = 'guitar'
            me "Давай гитару..."
            if ds_played_guitar:
                mi "Да, я тоже думаю, что тебе она подойдёт лучше всего, ты же так на ней играешь!"
            else:
                mi "Да, давай, конечно!"
            show mi normal pioneer at center
            with dspr
            mi "Значит, смотри, вот тут написана партия для тебя. Сейчас мы попробуем с тобой в первый раз сыграть дуэтом."
            mi "В смысле, я буду петь, а ты - играть. Ты же понимаешь, что тебе надо делать?"
            play sound ds_sfx_int
            enc "В памяти у тебя всплывает что-то связанное с музыкой - и нотной грамотой в частности. Так что худо-бедно, но справишься."
            me "Ну... да"
            mi "Хотя стоп. Сначала будет лучше, чтобы ты сам сыграл! Правда ведь?"
            play sound ds_sfx_int
            rhe "Мику не делает даже малейшей паузы - она уже всё решила за тебя."
            mi "Ну что, приступим, Семён-кун?"
            $ ds_prepare_play_status = 0
            window hide
            menu ds_day4_play_preparation:
                set ds_menuset
                "Начать" (skill='interfacing', level=lvl_formidable, modifiers=[('ds_prepare_play_status == 1', 1, "Собрался с мыслями"), ('ds_prepare_play_status == -1', -2, "Накрутил себе")]):
                    pass
                "Попросить немного времени":
                    window show
                    me "Сейчас, я пару минут посижу, ознакомлюсь с инструментом..."
                    mi "Да, конечно, Семён-кун!"
                    "Ты начинаешь оглядывать гитару... и думать о взятой на себя ответственности."
                    if ds_skill_list['volition'].check(level=lvl_up_medium, passive=True).result():
                        play sound ds_sfx_psy
                        vol "{result}Cоберись, тряпка! Всё у тебя получится!"
                        "Ты выпрямляешь спину, набравшись уверенности в себе."
                        $ ds_prepare_play_status = 1
                    else:
                        play sound ds_sfx_psy
                        vol "{result}А вдруг ты прямо сейчас опозоришься? Или того хуже - на концерте, при народе?"
                        "Тебя бросает в дрожь от этих мыслей."
                        $ ds_prepare_play_status = -1
                    me "Ну, вроде всё..."
                    window hide
                    jump ds_day4_play_preparation
                "Отказаться":
                    window show
                    me "Я как-то не был готов вот так с места в карьер - и начать репетировать..."
                    show mi unsure pioneer at center
                    with dspr
                    mi "А зачем же нам время терять? Раньше начнём - лучше получится на концерте!"
                    me "И всё-таки я бы хотел сначала посидеть, изучить то, что ты мне дала..."
                    mi "С другой стороны, ты, пожалуй, прав. Ладно, давай завтра тогда, Семён-кун!"
                    me "Давай."
                    show mi normal pioneer at center
                    with dspr
                    mi "Тогда я побежала! Пока!"
                    hide mi with dissolve
                    "И Мику выбегает из клуба. Ты следуешь за ней."
                    scene bg ext_musclub_day
                    with dissolve
                    $ disable_current_zone_ds_small()
                    jump ds_day4_after_lunch_map
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_mot
                inf "{result}Ты окидываешь глазами ноты, затем закидываешь гитару себе на колени, разминаешь пальцы, и, наконец, извлекаешь первый аккорд."
                inf "Тебе удаётся получить точно требуемые партитурой звуки. Удовлетворившись успехом, ты переходишь к последующим созвучиям."
                if ds_skill_list['conceptualization'].check(level=lvl_medium, passive=True, modifiers=[("ds_helped_who == 'dv'", 3, "Что-то уже слышанное")]):
                    play sound ds_sfx_int
                    con "{result}Извлекая аккомпанемент аккорд за аккордом, ты осознаёшь, что {i}конкретная{/i} мелодия идеально ложится на неё."
                    th "Какая?"
                    con "«{i}Взвейтесь кострами, синие ночи...{/i}» Понимаешь?"
                    play sound ds_sfx_int
                    lgc "Как же можно было не догадаться! Прощальный концерт - конечно, там будет гимн пионеров!"
                play sound ds_sfx_psy
                vol "То, что у тебя с первого раза получилось сыграть без ошибок, приподнимает твою самооценку. Тебе становится теплее на душе."
                $ ds_morale.up()
                "Мелодия - точнее, аккомпанемент - оказывается не такой уж и длинной. Дойдя до конца, ты выдыхаешь и откладываешь гитару."
                show mi charmed pioneer at center
                with dspr
                mi "Какой ты молодец, сразу всё сыграл - и всё идеально! Я поражена! Да ты прирождённый музыкант!"
                me "Cпасибо..."
            else:
                window show
                play sound ds_sfx_mot
                inf "{result}Ты пытаешься взять хотя бы первый аккорд - но твои пальцы тебя не слушаются, заплетаются. Делают всё, но не то, что нужно."
                inf "Ты пытаешься переиграть, продвигаться раньше, но, мягко говоря, не очень успешно."
                play sound ds_sfx_int
                con "Получается форменная какофония."
                $ ds_morale.damage()
                play sound ds_sfx_fys
                pat "Ты падаешь духом. Тебе больно осознавать, что ты не можешь справиться даже с простым аккомпанементом."
                if not ds_skill_list['composure'].check(level=lvl_legendary, passive=True).result():
                    play sound ds_sfx_mot
                    com "{result}Ты психуешь, бросаешь гитару, а сам бросаешься в слёзы."
                    me "Не буду я играть! Не получается у меня ничего!"
                    show mi despair pioneer at center
                    with dspr
                    mi "Ну не надо так убиваться, Семён-кун. У тебя получилось в целом неплохо..."
                    play sound ds_sfx_int
                    rhe "Это просто попытка тебя успокоить. Она (как и ты) прекрасно понимает, что сыграл ты чудовищно."
                    window hide
                    menu:
                        "Успокоиться":
                            window show
                            play sound ds_sfx_mot
                            com "C большим трудом тебе удаётся взять себя в руки и прекратить плакать."
                            mi "Ну всё-всё-всё, сейчас посидим, и всё у тебя получится."
                            me "Думаешь?"
                            show mi smile pioneer at center
                            with dspr
                            mi "Конечно, всё будет отлично, я верю в тебя!"
                            me "Ладно..."
                        "Продолжать плакать":
                            window show
                            "Ты не обращаешь внимания на Мику и продолжаешь плакать."
                            play sound ds_sfx_mot
                            per_toc "Внезапно ты чувствуешь тепло на своих плечах."
                            play sound ds_sfx_psy
                            esp "Это Мику. Она, чтобы успокоить тебя, подошла сзади и приобняла."
                            "Она прижимается к тебе и целует в щёку."
                            play sound ds_sfx_psy
                            vol "Тебе становится немного легче. Во всяком случае плакать ты прекращаешь."
                            mi "Не плачь, Семён-кун. Ты всё равно молодец, немного попрактикуешься - и, вот увидишь, всё у тебя получится."
                            play sound ds_sfx_mot
                            per_hea "Она говорит голосом даже более высоким и мягким, чем обычно."
                            play sound ds_sfx_psy
                            emp "Мику искренне за тебя переживает. Она не может оставаться равнодушным к твоим слезам."
                            me "Cпасибо..."
                        "Послать всё":
                            window show
                            me "Да пошло оно всё! Не буду я в ваших концертах участвовать!"
                            scene bg ds_ext_musclub_veranda_day
                            with dissolve
                            $ ds_lp['mi'] -= 1
                            "C этими словами ты выбегаешь из клуба и продолжаешь истерить уже на веранде."
                            th "Я не понимаю. Я пытаюсь, но у меня НИЧЕГО не получается! Даже самое простое!"
                            show mi shocked pioneer at center
                            with dissolve
                            "Внезапно к тебе прибегает Мику."
                            mi "Ты чего, Семён-кун? Зачем же сразу сдаваться? Всё у тебя получится, нужно лишь ещё попробовать."
                            mi "Возвращайся в клуб. Всё будет хорошо."
                            window hide
                            menu:
                                "Cогласиться":
                                    window show
                                    me "Ладно..."
                                    play sound sfx_open_door_clubs_2
                                    scene bg int_musclub_day
                                    show mi normal pioneer at center
                                    with dissolve
                                    "Вы заходите обратно. Тебе уже стало полегче."
                                "Отвергнуть":
                                    window show
                                    me "Нет, не будет! Я полный бездарь! Только испоганю вам всё!"
                                    $ ds_lp['mi'] -= 1
                                    scene bg ext_musclub_day
                                    with dissolve
                                    "Ты убегаешь дальше."
                                    scene bg ext_square_day
                                    with dissolve
                                    "Добежав до площади и присев на скамейку, ты более-менее успокаиваешься."
                                    "Через пару минут ты встаёшь, думая, куда бы тебе пойти дальше."
                                    $ ds_concert_status = -1
                                    window hide
                                    $ disable_current_zone_ds_small()
                                    jump ds_day4_after_lunch_map
                else:
                    "Ты откладываешь гитару, решив прекратить мучать инструмент."
                    show mi unsure pioneer at center
                    with dspr
                    play sound ds_sfx_psy
                    esp "Мику изо всех сил старается подобрать слова помягче, чтобы охарактеризовать твою игру."
                    mi "Это было... неплохо... {w}Да, неплохо, но надо бы ещё позаниматься..."
            show mi normal pioneer at center
            with dspr
            mi "Так, давай теперь попробуем вместе. Я буду петь - ты мне подыгрывать. Хорошо?"
            me "Хорошо."
            mi "Итак, три-четыре!"
            "Ты снова склоняешься над инструментом и пытаешься извлечь аккорды."
            if ds_last_skillcheck.result(invoke_callbacks=False):
                "Тебе удаётся повторить свой прошлый успех."
            else:
                "В этот раз у тебя получается сыграть немного лучше."
            "Тем временем Мику начинает петь."
            mi "{i}Взвейтесь кострами, синие ночи...{/i}"
            mi "{i}Мы пионеры, дети рабочих...{/i}"
            mi "{i}Близится эра светлых годов...{/i}"
            mi "{i}Клич пионеров: «Всегда будь готов!»{/i}"
            play sound ds_sfx_mot
            per_hea "В речи Мику слышно, что её родной язык имеет фонетический строй, непохожий на русский. Но в пении это проявляется наиболее явно - акцент немалый."
            window hide
            menu:
                "Высказать":
                    window show
                    me "Прекрати, это невозможно слушать!"
                    show mi shocked pioneer at center
                    with dspr
                    mi "Ты о чём?"
                    me "Как можно так коверкать русские слова, песню? Вообще же ничего не разберёшь!"
                    show mi sad pioneer at center
                    with dspr
                    mi "Я... я... ты..."
                    play sound ds_sfx_psy
                    emp "Она не знает, что сказать... Ты её, мягко говоря, очень сильно обидел."
                    $ ds_lp['mi'] -= 5
                    $ ds_concert_status = -1
                    $ ds_upset_mi = True
                    show mi rage pioneer at center
                    with dspr
                    mi "Да как ты смеешь вообще так говорить?! Я знаю, что я не русская, и стараюсь, как могу, совладать с вашими странными стечениями согласных! Не тебе судить об этом! Иди отсюда!"
                    me "Но..."
                    mi "ПРОЧЬ!"
                    play sound ds_sfx_fys
                    hfl "Такой разгневанной Мику ты не не мог даже помыслить себе. У тебя душа в пятки уходит, и ты сам не замечаешь, как оказываешься на улице."
                    scene bg ext_musclub_day
                    with dissolve
                    "Отдышавшись, ты решаешь, куда направиться дальше."
                    $ disable_current_zone_ds_small()
                    jump ds_day4_after_lunch_map
                "Промолчать":
                    window show
                    th "Думаю, лучше не стоит об этом говорить - иначе обижу её."
            "Наконец, Мику заканчивает."
            show mi smile pioneer at center
            with dspr
            mi "Мне кажется, у нас неплохо получается! А ты как думаешь, Семён-кун?"
            window hide
            menu:
                "Отлично":
                    window show
                    me "У нас отлично получается!"
                    mi "Я рада это слышать! Осталось ещё пару раз отрепетировать, затем позвать Алису-тян и отрепетировать с ней, и у нас будет самый лучший концерт!"
                "Неплохо":
                    window show
                    me "Неплохо, я думаю..."
                    mi "Тогда мы сейчас ещё несколько раз отрепетируем, чтобы всё было отлично-отлично! Мы будем лучшими на концерте, с Алисой-тян, конечно!"
                "Не очень":
                    window show
                    me "Не очень, честно говоря..."
                    mi "Ну ничего, порепетируем ещё, и всё будет хорошо! Вот увидишь!"
                    play sound ds_sfx_psy
                    vol "Её жизнерадостности и позитивному настрою остаётся только завидовать."
            mi "И раз-два-три!"
            "Ты вновь бьёшь по струнам, а она запевает."
            window hide
            scene black
            with fade
            $ renpy.pause(5.0)
        "Выбрать синтезатор":
            window show
            $ ds_instrument_chosen = 'piano'
            me "А чем чёрт не шутит - давай синтезатор."
            show mi smile pioneer at center
            with dspr
            mi "Давай, конечно! Он убран в кладовку - сходи туда и принеси, пожалуйста."
            window hide
            menu:
                "Сходить":
                    window show
                    me "Сейчас всё будет!"
                "Предложить сходить Мику":
                    window show
                    me "А может ты сходишь?"
                    show mi grin pioneer at center
                    with dspr
                    mi "Не ленись, Сёмочка, сходи сам."
                    play sound ds_sfx_int
                    rhe "...потому что ты мужчина, не я."
                    $ ds_lp['mi'] -= 1
            play sound sfx_open_door_squeak_2
            scene bg ds_int_wardrobe
            with dissolve
            $ persistent.sprite_time = 'night'
            "Ты заходишь в гардеробную. Здесь царит полутьма."
            window hide
            menu ds_day4_find_synth:
                set ds_menuset
                "Найти синтезатор взглядом" (skill='perception', level=lvl_challenging):
                    if ds_last_skillcheck.result():
                        window show
                        play sound ds_sfx_mot
                        per_eye "{result}В дальнем углу ты видишь смутные очертания искомого предмета."
                        "Подойдя к нему, ты убеждаешься, что это синтезатор."
                    else:
                        window show
                        play sound ds_sfx_mot
                        per_eye "{result}Как бы ты ни вглядывался в потёмки - ты не видишь ничего похожего на синтезатор. Да и в принципе не можешь отличить предметы."
                        play sound ds_sfx_psy
                        vol "Тебе не остаётся ничего иного, кроме как позвать Мику. Или же ты проведёшь тут много времени бесцельно."
                        window hide
                        jump ds_day4_find_synth
                "Начать искать на ощупь":
                    window show
                    "Ты начинаешь ощупывапть каждую полку шкафа."
                    "А полок очень много, и всякого хлама на них - тоже. Так что поиски затягиваются."
                    window hide
                    $ renpy.pause(2.0)
                    show mi serious pioneer at center
                    with dspr
                    window show
                    mi "Ты чего-то тут надолго застрял, Семён-кун, не можешь найти?"
                    window hide
                    menu:
                        "Признаться":
                            window show
                            me "Ну... да..."
                            show mi smile pioneer at center
                            with dspr
                            mi "Иди за мной!"
                        "Отрицать":
                            window show
                            me "Да всё отлично идёт, я уже напал на след синтезатора!"
                            show mi laugh pioneer at center
                            with dspr
                            mi "Ты, конечно, умничка, но давай я тебя сразу прямо к нему проведу!"
                    "Она берёт тебя за руку и отводит прямо к искомой вещи."
                    mi "Тебе остаётся только отнести её!"
                    hide mi with dissolve
                    "И она убегает обратно."
                "Позвать Мику":
                    window show
                    "Ты высовываешься в дверь, ведущую в клуб, и кричишь Мику."
                    me "Мику, помоги, пожалуйста, найти синтезатор, я ни зги не вижу."
                    show mi normal pioneer at center
                    with dspr
                    "Мику вбегает в подсобку."
                    mi "Cейчас-сейчас, всё покажу тебе, Семён-кун."
                    "Она берёт тебя за руку и отводит прямо к искомой вещи."
                    mi "Тебе остаётся только отнести её!"
                    hide mi with dissolve
                    "И она убегает обратно."
            window hide
            menu:
                "Отнести синтезатор" (skill='physical_instrument', level=lvl_medium):
                    if ds_last_skillcheck.result():
                        window show
                        play sound ds_sfx_fys
                        phi "{result}Готов? На плечо!"
                        "Cинтезатор не оказывается для тебя какой-то тяжестью - ты с лёгкостью загружаешь его себе на плечо и относишь в помещение, где тебя уже ждёт Мику."
                        $ persistent.sprite_time = 'day'
                        scene bg int_musclub_day
                        show mi happy pioneer at center
                        with dissolve
                        mi "Ой, ты принёс, Семён-кун. Какой ты молодец! Давай же быстрее приступать!"
                    else:
                        window show
                        play sound ds_sfx_fys
                        phi "{result}Ты хлопаешь рукой о руку и пытаешься поднять синтезатор. Тебе удаётся это с трудом."
                        phi "Более того, после пары шагов ты теряешь равновесие и вместе с синтезатором падаешь."
                        window hide
                        play sound sfx_body_bump
                        with vpunch
                        $ renpy.pause(1.0)
                        window show
                        play sound ds_sfx_fys
                        edr "Вроде цел."
                        play sound ds_sfx_int
                        vic "Cинтезатор, кажется, тоже не пострадал."
                        show mi scared pioneer at center
                        with dissolve
                        "Мику прибегает на грохот."
                        mi "Всё хорошо, Семён-кун? Ты цел? Здоров?"
                        me "Вроде да..."
                        "И ты встаёшь."
                        show mi serious pioneer at center
                        with dspr
                        mi "Давай тогда вместе отнесём!"
                        "И она, не дождавшись твоего ответа, берётся за другой конец ситнезатора."
                        play sound ds_sfx_psy
                        aut "Какой позор - девчонка будет тебе помогать!"
                        $ ds_morale.damage()
                        "Тем не менее, ты берёшься за другой конец, и вы заносите синтезатор в зал."
                "Попросить помощи Мику":
                    window show
                    me "Мику, мне, кажется, нужна твоя помощь!"
                    show mi surprise pioneer at center
                    with dspr
                    mi "Что такое, Семён-кун?"
                    me "Боюсь, в одиночку такой огромный синтезатор я не дотащу..."
                    show mi smile pioneer at center
                    with dspr
                    mi "А, значит, вместе дотащим. Берись за тот конец!"
                    "И Мику хватается за ближний. Ты заходишь с другой стороны, и вместе вы поднимаете инструмент."
            scene bg int_musclub_day
            show mi normal pioneer at center
            with dissolve
            play sound sfx_drop_alisa_bag
            with vpunch
            "Вы выносите синтезатор и ставите его возле рояля на уже подготовленную подставку."
            if ds_skill_list['reaction_speed'].check(level=lvl_easy, passive=True).result():
                play sound ds_sfx_mot
                res "{result}Погодь. А почему нельзя было на рояле отрепетировать?"
                window hide
                menu:
                    "Cпросить":
                        window show
                        me "А почему мы не могли вместо того, чтобы переносить синтезатор, сейчас на рояле отрепетировать?"
                        show mi serious pioneer at center
                        with dspr
                        mi "Потому что звучание синтезатора - это вовсе не то же самое, что и звучание рояля, а ещё на синтезаторе есть кнопочки, с которыми было бы неплохо тебе разобраться, и желательно сразу же, а ещё тебе было полезно потаскать синтезатор!"
                        play sound ds_sfx_psy
                        sug "Поправочка - ей было удобно так."
                        me "Понятно..."
                    "Отбросить мысль":
                        window show
            show mi smile pioneer at center
            with dspr
            mi "Ты сначала разомнись, сыграй гаммы, аккорды, арпеджио!"
            if not ds_skill_list['encyclopedia'].check(level=lvl_medium, passive=True).result():
                play sound ds_sfx_int
                enc "{result}Кого-кого сыграть? Ты точно не знаешь композицию «Гаммы, аккорды, арпеджио»!"
                me "Кого сыграть, Мику?"
                show mi laugh pioneer at center
                with dspr
                mi "Ты такой забавный, Семён-кун! Сейчас сыграю, и ты вспомнишь!"
                "Она садится за синтезатор и перебирает клавиши одну за другой. Затем зажимает по 3-4 клавиши одновременно. Затем эти же клавиши последовательно."
                mi "Вот, теперь понял?"
                play sound ds_sfx_int
                lgc "Да понял ты всё, разберёмся!"
                me "Ну да."
            "Ты усаживаешься за синтезатор и проигрываешь «до-ре-ми-фа-соль-ля-си-до». Потом назад."
            "Затем играешь «до-ми-соль» одновременно, а затем и пошагово."
            if ds_skill_list['conceptualization'].check(level=lvl_up_medium, passive=True).result():
                play sound ds_sfx_int
                con "{result}Ну, это скучно. Давай коротенькую, но интересную композицию."
                window hide
                menu:
                    "Послушать мысль":
                        window show
                        th "И что мне сыграть?"
                        con "Играй: до-ре-ми-до-ре-до. Две последние ноты - длиннее."
                        "Ты исполняешь: до-ре-ми-до-рее-доо."
                        show mi confused pioneer at center
                        with dspr
                        "Мику меняется в лице. Кажется, она не оценила."
                        mi "Эээ... а ты к чему это сыграл?"
                        me "Да так, просто!"
                        mi "Лучше не стоит, особенно на публике?"
                        th "Эй, а что такого я сыграл?"
                        con "Как что? Ты показал своё отношение к миру! А Мику не поняла концепции, вот и всё!"
                        th "Какое отношение?"
                        play sound ds_sfx_int
                        rhe "По сути - послал в пешее эротическое."
                        th "В смысле?"
                        play sound ds_sfx_int
                        enc "Ну, «до-ре-ми-до-ре-до» - это жаргонное ругательство музыкантов. Мику его тоже знает."
                        th "Вот дела..."
                    "Отбросить мысль":
                        window show
                        th "Не хочу!"
                        con "Какой ты скучный!"
            show mi normal pioneer at center
            with dspr
            mi "Итак, попробуем исполнить?"
            window hide
            menu:
                "Сыграть с листа" (skill='interfacing', level=lvl_heroic):
                    window show
                    me "Да, давай!"
                    mi "Начинаем! Три-четыре!"
                    window hide
                    if ds_last_skillcheck.result():
                        window show
                        play sound ds_sfx_mot
                        inf "{result}Ты просматриваешь глазами ноты и синхронно со взглядом начинаешь играть."
                        inf "Тебе удаётся поспевать одновременно читать и извлекать из клавиш инструмента нужные звуки."
                        $ ds_lp['mi'] += 2
                        play sound ds_sfx_mot
                        per_hea "Синтезатор звучит как пианино... но немного по-другому."
                        "Одновременно с тобой Мику начинает петь."
                        mi "{i}Взвейтесь кострами, синие ночи...{/i}"
                        mi "{i}Мы пионеры, дети рабочих...{/i}"
                        mi "{i}Близится эра светлых годов...{/i}"
                        mi "{i}Клич пионеров: «Всегда будь готов!»{/i}"
                        play sound ds_sfx_mot
                        per_hea "В речи Мику слышно, что её родной язык имеет фонетический строй, непохожий на русский. Но в пении это проявляется наиболее явно - акцент немалый."
                        window hide
                        menu:
                            "Высказать":
                                window show
                                me "Прекрати, это невозможно слушать!"
                                show mi shocked pioneer at center
                                with dspr
                                mi "Ты о чём?"
                                me "Как можно так коверкать русские слова, песню? Вообще же ничего не разберёшь!"
                                show mi sad pioneer at center
                                with dspr
                                mi "Я... я... ты..."
                                play sound ds_sfx_psy
                                emp "Она не знает, что сказать... Ты её, мягко говоря, очень сильно обидел."
                                $ ds_lp['mi'] -= 5
                                $ ds_concert_status = -1
                                $ ds_upset_mi = True
                                show mi rage pioneer at center
                                with dspr
                                mi "Да как ты смеешь вообще так говорить?! Я знаю, что я не русская, и стараюсь, как могу, совладать с вашими странными стечениями согласных! Не тебе судить об этом! Иди отсюда!"
                                me "Но..."
                                mi "ПРОЧЬ!"
                                play sound ds_sfx_fys
                                hfl "Такой разгневанной Мику ты не не мог даже помыслить себе. У тебя душа в пятки уходит, и ты сам не замечаешь, как оказываешься на улице."
                                scene bg ext_musclub_day
                                with dissolve
                                "Отдышавшись, ты решаешь, куда направиться дальше."
                                $ disable_current_zone_ds_small()
                                jump ds_day4_after_lunch_map
                            "Промолчать":
                                window show
                                th "Думаю, лучше не стоит об этом говорить - иначе обижу её."
                        "Наконец, Мику заканчивает."
                        show mi smile pioneer at center
                        with dspr
                        mi "Мне кажется, у нас неплохо получается! А ты как думаешь, Семён-кун?"
                        window hide
                        menu:
                            "Отлично":
                                window show
                                me "У нас отлично получается!"
                                mi "Я рада это слышать! Осталось ещё пару раз отрепетировать, затем позвать Алису-тян и отрепетировать с ней, и у нас будет самый лучший концерт!"
                            "Неплохо":
                                window show
                                me "Неплохо, я думаю..."
                                mi "Тогда мы сейчас ещё несколько раз отрепетируем, чтобы всё было отлично-отлично! Мы будем лучшими на концерте, с Алисой-тян, конечно!"
                            "Не очень":
                                window show
                                me "Не очень, честно говоря..."
                                mi "Ну ничего, порепетируем ещё, и всё будет хорошо! Вот увидишь!"
                                play sound ds_sfx_psy
                                vol "Её жизнерадостности и позитивному настрою остаётся только завидовать."
                        mi "И раз-два-три!"
                        window hide
                        scene black with dissolve2
                        $ renpy.pause(5.0)
                    else:
                        window show
                        play sound ds_sfx_mot
                        inf "{result}Нет, бесполезно. Когда ты фокусируешь внимание на нотах - теряешь ритм и нажимаешь невпопад. Когда пытаешься сконцентрироваться на клавишах - перестаёшь понимать, что играть."
                        play sound ds_sfx_fys
                        edr "Ты вспотел, у тебя дрожат руки - тебе никак не удаётся собраться и сыграть хорошо."
                        edr "Кажется, ещё чуть-чуть - и ты упадёшь в обморок от перенапряжения."
                        $ ds_health.damage()
                        show mi scared pioneer at center
                        with dspr
                        mi "Cемён-кун? С тобой всё в порядке? Ты побледнел."
                        me "Cо мной... всё... нормально..."
                        if not ds_skill_list['endurance'].check(level=lvl_challenging, passive=True).result():
                            edr "{result}Если бы. Твоя голова готова взорваться."
                            show blink
                            scene black with dissolve2
                            play sound sfx_fall_wood_floor
                            edr "Ты падаешь на пол, теряя сознание."
                            window hide
                            $ renpy.pause(3.0)
                            window show
                            mi "Cемён?.."
                            play sound ds_sfx_psy
                            vol "Голос Мику тебя вытягивает из забытья, куда ты уже готов был погрузиться. Или погрузился? Понять невозможно."
                            hide blink
                            scene int_musclub_day
                            show mi scared pioneer at center
                            with dissolve
                            show unblink
                            "Ты открываешь глаза. Мику склонилась над тобой. Её взгляд полон страха."
                            play sound ds_sfx_psy
                            esp "Страха за {i}тебя{/i}."
                            mi "Ты целый час пролежал тут без сознания! Я бегала за медсестрой - но её не оказалось на месте! Хотела найти Ольгу Дмитриевну-сама, но тоже не смогла! Я уже не знала, что мне делать!"
                            play sound ds_sfx_mot
                            res "Целый час?! Нет, ЧАС?!"
                            me "Cколько-сколько я пролежал?"
                            show mi upset pioneer at center
                            with dissolve
                            mi "Час. Нам уже ужинать идти пора. Придётся завтра дорепетировать."
                            me "Идём..."
                            jump ds_day4_dinner
                        else:
                            "Наконец, ты решаешь оставить это гиблое дело."
                            me "Нет, у меня как-то не получается..."
                            show mi sad_smile pioneer at center
                            with dspr
                            mi "В целом у тебя получается неплохо!"
                            play sound ds_sfx_int
                            rhe "Формула вежливости - не больше."
                            mi "Но давай мы с тобой вместе попрактикуемся!"
                            me "Ну ладно..."
                            "И Мику начинает тщательно разучивать с тобой составленную ею же композицию."
                            window hide
                            scene black with dissolve2
                            $ renpy.pause(5.0)
                "Разобрать партию отдельно":
                    window show
                    me "Слушай, мне бы сначала самому разобрать эту партию... для каждой руки отдельно, а потом вместе."
                    show mi smile pioneer at center
                    with dspr
                    mi "А, конечно-конечно, сейчас вместе разберёмся!"
                    "И она, не дожидаясь твоей реакции, располагается за тобой, готовясь разъяснять каждую мелочь."
                    show mi serious pioneer close at center
                    with dspr
                    mi "Давай начнём с правой руки. Смотри: вот тут над играть так."
                    "Она взмахивает рукой и извлекает звук - мелодичный, но резкий."
                    play sound ds_sfx_int
                    con "Что оправданно: это же марш."
                    mi "Теперь повтори."
                    "Ты повторяешь за ней, более-менее близко к правде."
                    mi "Смотри дальше. Теперь играй вот так."
                    "Такт за тактом вы разбираете мелодию."
                    if ds_skill_list['perception'].check(level=lvl_medium, passive=True).result():
                        play sound ds_sfx_mot
                        per_hea "{result}Ты можешь осознать игмн пионеров. «Взвейтесь кострами, синие ночи...»"
                    mi "Теперь давай приступим к левой руке. Тут тебе надо сыграть ряд аккордов. Соль-мажор, соль-мажор, ре-мажор, соль-мажор, ре-септаккорд, ..."
                    play sound ds_sfx_int
                    rhe "Куда она так спешит? Ты ничего не понимаешь."
                    me "Можно пошагово, пожалуйста?"
                    mi "Ой, конечно, смотри, первый аккорд берётся так."
                    "Она зажимает три белые клавиши."
                    mi "Так же и второй. А третий - вот так."
                    "Ты повторяешь за ней. На практике - ничего сложного."
                    mi "А теперь септаккорд, который ты берёшь вот так."
                    "Она зажимает уже четыре клавиши. Ты вслед за ней зажимаешь те же клавиши."
                    "Cпустя некоторое время вы разбираете партию. Кажется, ты чувствуешь себя куда как увереннее."
                    show mi smile pioneer at center
                    with dspr
                    mi "А теперь давай вместе!"
                    "И она запевает, в то время как ты мало-помалу начинаешь играть."
        "Выбрать микшер":
            window show
            $ ds_instrument_chosen = 'mixer'
        "Спросить про «обычную» гитару":
            window show
            me "А просто гитары нет?"
            show mi normal pioneer at center
            with dspr
            mi "Есть, конечно, но её уже Алиса-тян заняла, и никому-никому отдавать не собирается!"
            if ds_whom_helped == 'dv':
                play sound ds_sfx_int
                lgc "Закономерно, что Алиса играет на гитаре..."
            mi "Так что остаётся только бас-гитара. Не переживай - она ничем не хуже обычной!"
            if ds_skill_list['conceptualization'].check(level=lvl_easy, passive=True).result():
                play sound ds_sfx_int
                con "Не считая того, что это лишь аккомпанемент. Как ты выразишь свой внутренний мир, когда мелодии тебе не дано?!"
            me "Ладно..."
            window hide
            jump ds_day4_choose_instrument
        "Cпросить про барабаны":
            window show
            me "А на барабанах поиграть нельзя?"
            show mi pity pioneer at center
            with dspr
            mi "Пришёл бы ты на пару часиков раньше... А тут уже попросили у меня, чтобы Ульяна-кохай на барабанах постучала, я не могла, да и не хотела отказывать!"
            if ds_skill_list['logic'].check(level=lvl_easy, passive=True).result():
                play sound ds_sfx_int
                lgc "{result}И по чьей же протекции Ульяна получила это место? Что-то тебе подсказывает, что это благодетельница с огненной причёской..."
            me "Понятно..."
            window hide
            jump ds_day4_choose_instrument
        "Пожелать инструмент оригинальнее":
            window show
            me "Какой скучный выбор... А ничего пооригинальнее нет?"
            show mi confused pioneer at center
            with dspr
            mi "Ты про что говоришь, Семён-кун?"
            me "Ну, не знаю, может, есть какие-то необычные инструменты..."
            show mi pity_smile pioneer at center 
            with dspr
            mi "Инструменты-то есть, но для концерта они не подойдут - во-первых, нам нужны электронные, во-вторых, их звучание под мелодию не очень..."
            mi "Так что извини, но тебе лучше выбрать из того, что есть, Семён-кун."
            window hide
            jump ds_day4_choose_instrument
    scene bg int_musclub_day
    show mi happy pioneer at center
    with dissolve
    "После десятого, кажется, прохода, и у Мику проявляются признаки усталости."
    play sound ds_sfx_fys
    edr "О тебе и говорить не приходится - ты устал и проголодался."
    mi "Как же классненько получается у нас! А теперь пора идти покушать!"
    me "Да, пора..."
    scene bg ext_musclub_day
    show mi smile pioneer at center
    with dissolve
    "Вы выходите на улицу - вместе."
    show mi surprise pioneer at center
    with dspr
    mi "Ой, ты иди, Семён-кун, а мне надо в домик забежать!"
    hide mi with dissolve
    "И Мику убегает прежде, чем ты успеваешь что-либо возразить."
    "Поэтому ты, повинуясь зову желудка, направляешься дальше в столовую."
    jump ds_day4_dinner

label ds_day4_storage:
    $ persistent.sprite_time = "day"
    scene bg ds_ext_storage_day
    with dissolve
    "Ты подходишь к складу."
    if ds_skill_list['half_light'].check(lvl_up_medium, passive=True).result():
        play sound ds_sfx_fys
        hfl "{result}Кажется, внутри склада уже кто-то есть..."
    "Дверь оказывается открытой. Ты заходишь."
    scene bg ds_int_storage_day
    show dv surprise pioneer2 at center
    with dissolve
    "В здании ты обнаруживаешь Алису, вдумчиво изучающую мешки. Твоего (да и чьего-либо ещё) прихода она не ожидала."
    show dv angry pioneer2 at center
    with dspr
    dv "Чего припёрся?!"
    $ ds_d4_know_bags_content = False
    window hide
    menu:
        "Рассмотреть мешки" (skill='perception', level=lvl_medium):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_mot
                per_eye "{result}На мешках написано «УДОБРЕНИЯ. СЕЛИТРА.»"
                
                $ ds_d4_know_bags_content = True
            else:
                window show
                play sound ds_sfx_mot
                per_eye "{result}В полутьме буквы, отпечатанные на мешках, не различить. А содержимого не видно."
        "Спросить Алису":
            window show
            me "А что ты тут делаешь с мешками?"
            dv "Нужно мне! Не лезь не в своё дело!"
        "Извиниться и уйти":
            window show
            me "Ой, извини, ухожу-ухожу..."
            dv "Давай, иди!"
            $ disable_current_zone_ds_small()
            jump ds_day4_after_lunch_map
    window hide
    $ ds_d4_dv_told_plan = False
    menu ds_d4_dv_storage:
        set ds_menuset
        "Понять, зачем нужна селитра" (skill='encyclopedia', level=lvl_challenging) if ds_d4_know_bags_content:
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_int
                enc "{result}Cелитра, сера и уголь - это же компоненты, которые позволят создать взрывчатку!"
                enc "Селитра - вот она, серу позаимствует у кибернетиков, а активированный уголь - в медпункте."
                
                $ ds_d4_know_dv_plan = True
            else:
                window show
                play sound ds_sfx_int
                enc "{result}Селитра... селитра-селитра-селитра... сейчас я найду назначение..."
                enc "Может, Алиса решила садоводством заняться?"
                play sound ds_sfx_psy
                aut "Алиса? Садоводством?! Да скорее Ульяна попадёт на доску почёта как самая примерная пионерка!"
                
            window hide
            jump ds_d4_dv_storage
        "Втереться в доверие Алисы" (skill='suggestion', level=lvl_heroic, modifiers=[('ds_dinner_dv', 3, 'Был соучастником'), ("ds_lp[['dv'] >= 20", 2, "Алиса тебе доверяет")]) if not ds_betray_dv:
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_psy
                sug "{result}Вспомни то, что делал вместе с ней. И покажи, что тебе можно довериться и сейчас."
                me "Кажется, раньше я тебя не предавал. А сейчас готов тебе помочь. Ты только скажи, чем."
                show dv surprise pioneer2 at center
                with dspr
                dv "Э... ну ладно. Я хочу, скажем так, фейерверк устроить. Мне для этого нужны селитра, сера и уголь!"
                $ ds_d4_know_dv_plan = True
                $ ds_d4_dv_told_plan = True
            else:
                window show
                play sound ds_sfx_psy
                sug "{result}Надави на неё! Она обязательно расколется!"
                me "И всё-таки, что ты замышляешь? Я не уйду, пока не скажешь."
                dv "Уйдёшь! А то врежу тебе! Не мешай мне!"
                $ ds_lp['dv'] -= 1
            
            window hide
            jump ds_d4_dv_storage
        "Пригрозить вожатой" if not ds_d4_know_dv_plan:
            window show
            me "А если я Ольге Дмитриевне расскажу о том, что ты по складам шаришься?"
            show dv rage pioneer2 at center
            with dspr
            dv "А я ничего не делаю! И вообще, я побежала!"
            hide dv with dissolve
            "Тут Алиса загребает немного содержимого мешка и убегает."
            th "И что это было?"
            $ ds_lp['dv'] -= 2
            $ ds_threaten_dv_mt = True
        "Пригрозить вожатой" if ds_d4_know_dv_plan:
            window show
            me "Интересно, а как Ольга Дмитриевна отнесётся к подобной твоей задумке?"
            if ds_d4_dv_told_plan:
                show dv rage pioneer2 at center
                with dspr
                dv "То есть, ты воспользовался моим доверием, чтобы шпионить за мной по указке вожатой?!"
                $ ds_lp['dv'] -= 5
                dv "Да иди ты куда подальше!"
            else:
                show dv rage pioneer2 at center
                with dspr
                dv "А я ничего не делаю! И вообще, я побежала!"
                $ ds_lp['dv'] -= 2
            "Тут Алиса загребает немного содержимого мешка и убегает."
            th "И что это было?"
            $ ds_threaten_dv_mt = True
        "Сказать про пустой медпункт" if ds_d4_know_dv_plan:
            window show
            me "Кстати, до меня тут сведения дошли, что в медпункте совсем-совсем никого нет..."
            show dv smile pioneer2 at center
            with dspr
            if ds_d4_dv_told_plan:
                dv "О, за это спасибо, буду знать! Это облегчает задачу!"
            else:
                dv "И к чему ты это? Я не понимаю тебя."
                play sound ds_sfx_int
                dra "Всё она прекрасно понимает. Намёк она уловила."
            $ ds_lp['dv'] += 1
            hide dv with dissolve
            dv "Бывай!"
            "C этими словами она загребает селитру и уходит."
        "Пожелать удачи" if ds_d4_know_dv_plan:
            window show
            me "Удачи, Алиса, у тебя всё получится!"
            if ds_d4_dv_told_plan:
                show dv smile pioneer2 at center
                with dspr
                dv "Cпасибо."
            else:
                show dv surprise pioneer2 at center
                with dspr
                dv "Это ты к чему?"
                dra "Всё она прекрасно понимает."
            hide dv with dissolve
            dv "Бывай!"
            "C этими словами она загребает селитру и уходит."
        "Оставить Алису в покое":
            window show
            me "Ладно, я пойду."
            dv "Иди уже!"
    scene bg ds_ext_storage_day
    with dissolve
    th "Итак, и что дальше?"
    $ disable_current_zone_ds_small()
    jump ds_day4_after_lunch_map

label ds_day4_dinner:
    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_away_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    show el normal pioneer at center   with dissolve
    window show
    "По дороге тебя догоняет Электроник."
    window hide
    menu:
        "Cпросить про поиски":
            window show
            me "Как поиски Шурика?"
            show el upset pioneer at center   with dspr
            el "Да всё так же…"
            window hide
            menu:
                "Подбодрить":
                    window show
                    me "Ты не расстраивайся…{w} Найдётся он!"
                "Промолчать":
                    window show
            el "Уже столько времени прошло!{w} Пойду искать дальше."
            window hide
            menu:
                "Cпросить про ужин":
                    window show
                    me "А как же ужин?"
                    el "Это важнее."
                    "Глубокомысленно изрекает он."
                "Промолчать":
                    window show
    hide el  with dissolve
    "На перекрёстке ваши дороги расходятся."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_near_day 
    with dissolve

    window show
    "В дверях столовой толпятся пионеры."
    play sound ds_sfx_mot
    svf "Иди быстрее - не то снова окажешься последний."
    window hide
    menu:
        "Ускорить шаг":
            window show
            "Ты ускоряешь шаг."
        "Идти спокойно":
            window show
            "Ты продолжаешь идти вальяжно."
    window hide

    stop ambience fadeout 3

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_people_day 
    with dissolve

    play ambience ambience_dining_hall_full fadein 3

    window show
    "В дальнем углу остаётся полностью свободный столик."
    "Ты быстро берёшь еду и садишься."
    "Сегодня на ужин фруктовый суп и несколько булочек."
    "Такой набор блюд тебя весьма удивил."
    play sound ds_sfx_mot
    per_tas "А после дегустации даже радует."
    "Ты принимаешься сосредоточенно есть."
    mi "Лена, давай сюда! Смотри – целых три стула!"
    show un normal pioneer at left 
    show mi normal pioneer at center 
    with dissolve
    "Перед тобой стояли Лена и Мику."
    un "Тут свободно?"
    window hide
    menu:
        "Пустить девушек":
            window show
            me "Да, садитесь."
            play sound ds_sfx_psy
            sug "Лучше бы, конечно, она была одна."
            un "Спасибо…"
            show un normal pioneer at left, ds_sit_down
            show mi normal pioneer at center, ds_sit_down
            show mz normal glasses pioneer at right
            with dissolve
            "Только и успевает сказать Лена, как у неё из-за спины появляется Женя."
            mz "Я сяду тут.{w} Больше некуда."
            "Не дождавшись твоего ответа, она ставит поднос на стол."
        "Отказать":
            window show
            me "Нет, тут занято!"
            $ ds_lp['un'] -= 1
            $ ds_lp['mi'] -= 1
            mz "Я сяду тут.{w} Больше некуда."
            "Не дождавшись твоего ответа, она ставит поднос на стол. Лена и Мику следуют за ней."
            show un normal pioneer at left, ds_sit_down
            show mi normal pioneer at center, ds_sit_down
            show mz normal glasses pioneer at right
    window hide
    menu:
        "Cмириться":
            window show
            me "Конечно, располагайтесь..."
            "Грустно пробурчал я себе под нос."
        "Потребовать уйти":
            window show
            me "Тебя ещё тут не хватало..."
            show mz angry glasses pioneer at right, ds_sit_down
            with dspr
            mz "Я же сказала - сесть некуда. И вообще - я сказала, что сяду тут, значит сяду тут."
            $ ds_lp['mz'] -= 1
            play sound ds_sfx_psy
            aut "Нет, так не пойдёт. Ты диктуешь условия, не она."
            window hide
            menu:
                "Опрокинуть поднос":
                    window show
                    "Ты берёшь поднос Жени и бросаешь его на пол."
                    play sound sfx_broken_dish
                    show mz rage glasses pioneer at right
                    show un surprise pioneer at left
                    show mi scared pioneer at center
                    with dspr
                    mz "Ты... Ты..."
                    "Она буквально шипит от злости."
                    $ ds_lp['mz'] -= 3
                    $ ds_lp['un'] -= 2
                    $ ds_lp['mi'] -= 2
                    show mt angry pioneer at cleft
                    with dissolve
                    mt "Что тут происходит?"
                    mz "Этот вот взял и швырнул на пол мой поднос. Просто потому, что я сесть сюда хотела!"
                    show mt rage pioneer at center
                    with dspr
                    mt "Пёрсунов! Сегодня без ужина! Бери швабру и убирай то, что ты натворил! А твой поднос уйдёт Жене."
                    $ ds_karma -= 20
                    $ ds_lp['mt'] -= 1
                    play sound ds_sfx_psy
                    aut "Поведение уровня младшей группы детского садика..."
                    th "Ольги Дмитриевны или Жени?"
                    aut "Твоё! На тебя смотрит вся столовая. Какой позор!"
                    $ ds_morale.damage()
                    "Делать нечего - ты берёшь швабру и убираешь то, что сам и натворил."
                    play sound ds_sfx_fys
                    edr "Ты хотел бы поесть, но тебе никто не даст - сам виноват."
                    aut "А Женя тем временем заняла твоё место и ест твой ужин."
                    window hide
                    
                    scene bg int_dining_hall_day
                    with dissolve2

                    window show
                    "Когда ты заканчиваешь с уборкой, столовая уже опустела."
                    jump ds_day4_after_dinner
                "Повторить требование":
                    window show
                    me "Я тебе сказал - тут тебе не рады!"
                    show mi tender pioneer at center
                    with dspr
                    mi "Да ладно тебе, Семён-кун. Я вот рада тому, что Женечка-тян присоединилась к нам."
                    show un shy pioneer at left
                    with dspr
                    un "Я тоже..."
                    aut "Полное поражение."
                    show mz bukal glasses pioneer at center
                    with dspr
                    "Женя садится за стол с торжествующим видом."
                    $ ds_lp['mz'] -= 1
                "Отступить":
                    window show
                    me "Ладно уж..."
    show mz angry glasses pioneer at right   with dspr
    mz "Что?!"
    me "Ничего..."
    show mz normal glasses pioneer at right   with dspr
    play sound ds_sfx_fys
    hfl "По крайней мере они все абсолютно безвредны по сравнению с некоторыми."
    show un surprise pioneer at left   with dspr
    un "Ой, я ключ, кажется, забыла…"
    show mi smile pioneer at center   with dspr
    mi "Ничего страшного, возьми мой!"
    show un normal pioneer at left   with dspr
    play sound ds_sfx_mot
    res "Мику ограничилась такой короткой фразой?"
    if 13 in ds_visited_houses:
        play sound ds_sfx_int
        rhe "Она имеет ввиду ключик от домика. Ведь они живут вместе."
    else:
        res "И они что, живут вместе?"
        window hide
        menu:
            "Спросить":
                window show
                me "А вы…{w} вместе живёте?"
                mi "Да, конечно! А ты не знал? Вместе. Наш домик самый крайний. То есть самый дальний от столовой. Ну, то есть самый последний."
                play sound ds_sfx_int
                lgc "Ты бы не удивился, если бы узнал, что Лена живёт со Славей.{w} С Женей на худой конец.{w} Да хоть с Электроником."
                lgc "Но молчаливая и застенчивая Лена и не в меру словоохотливая Мику…{w} Да, это сюрприз!"
            "Промолчать":
                window show
    show mi normal pioneer at center   with dspr
    mz "Нашли своего Шурика?"
    play sound ds_sfx_psy
    aut "Странно, что Женю вообще волнуют чужие проблемы."
    me "Нет."
    show mz angry glasses pioneer at right   with dspr
    mz "Небось в деревню убежал за сигаретами.{w} Или за водкой."
    "Она фыркает."
    if ds_skill_list['reaction_speed'].check(lvl_easy, passive=True).result():
        play sound ds_sfx_mot
        res "{result}Погоди. С этого момента разговор становится интереснее."
        window hide
        menu:
            "Расспросить":
                window show
                me "В деревню?"
                show mz bukal glasses pioneer at right   with dspr
                mz "А что такого?"
                me "Значит, здесь есть поблизости деревня?"
                show mz normal glasses pioneer at right   with dspr
                mz "Ну да, вроде есть…"
                play sound ds_sfx_int
                rhe "Она говорит неуверенно."
                "Ты смотришь на Лену и Мику, но они заняты едой и не обращают внимания на ваш разговор."
                window hide
                menu:
                    "Обратиться к ним":
                        window show
                        me "Лена, Мику, а вы что скажете?"
                        "Для них твой вопрос оказывается неожиданностью."
                        show mi surprise pioneer at center
                        show un surprise pioneer at left
                        with dspr
                        mi "Ты о чём хочешь спросить нас с Леной-тян, Семён-кун?"
                        me "Тут есть деревня? Вот, Женя говорит."
                        show mi sad pioneer at center
                        with dspr
                        mi "Ой, я не знаю, я же не местная..."
                        show un normal pioneer at center
                        with dspr
                        un "Да, есть. И дотуда можно дойти за где-то час."
                        res "Запомни это!"
                        me "Спасибо..."
                        show mi normal pioneer at center
                        with dspr
                        mi "А тебе зачем это, Семён-кун?"
                        me "Да так, просто интересно про окружение узнать..."
                    "Надавить на Женю":
                        window show
                        me "То есть ты точно не знаешь?"
                        show mz angry glasses pioneer at right   with dspr
                        mz "Да какое мне дело!"
                        me "Но здесь же должны быть какие-то населённые пункты поблизости?"
                        show mz angry glasses pioneer at right   with dspr
                        mz "Слушай..."
                        me "Слушаю."
                        mz "Не знаю я! Я, слава всем богам, не местная! Дай спокойно поесть."
                        show mz normal glasses pioneer at right   with dspr
                        play sound ds_sfx_int
                        rhe "Похоже, больше от неё ничего не добиться."
                        rhe "Хотя, может быть, она правда не знает..."
                    "Отступить":
                        window show
            "Сидеть молча":
                window show

    stop ambience fadeout 2

    "Всё оставшееся время приходится слушать, как Мику говорит о каких-то малозначительных вещах, и тихо сходить с ума…"
    window hide
    jump ds_day4_after_dinner

label ds_day4_after_dinner:
    $ persistent.sprite_time = "sunset"
    scene bg ext_dining_hall_away_sunset 
    with dissolve

    play ambience ambience_camp_center_evening fadein 3

    $ sunset_time()

    window show
    "Выйдя на улицу, ты вздыхаешь с облегчением."
    "Солнце уже садится."
    play sound ds_sfx_psy
    vol "Можно немного прогуляться."
    vol "Вряд ли сам найдёшь какое-то занятие на вечер, а так, может, что интересное подвернётся."

    if ds_dv_has_coal:
        play sound sfx_muffled_explosion

        play music music_list["doomed_to_be_defeated"] fadein 3

        play sound ds_sfx_mot
        per_hea "Сильный хлопок.{w} Похоже, что-то взорвалось."
        if not ds_skill_list['composure'].check(lvl_challenging, passive=True).result():
            play sound ds_sfx_mot
            com "{result}Тебя словно парализовало."
            play sound ds_sfx_fys
            hfl "Ты находишься во враждебной среде – неизвестно, что там и как!"
            hfl "Лучше убежать!"
            play sound ds_sfx_int
            lgc "Но в то же время интересно…"
        show mt normal pioneer at center   with dissolve
        "Тебя хватает за руку Ольга Дмитриевна."
        mt "Чего стоишь?{w} Пойдём разберёмся, что там произошло!"
        window hide
        menu:
            "Попросить остаться":
                window show
                me "А без меня никак?"

                stop music fadeout 3

                show mt surprise pioneer at center   with dspr
                mt "Да ничего там страшного не должно быть!{w} По идее…"
                window hide
            "Пойти молча":
                pass

        $ persistent.sprite_time = "sunset"
        scene bg ext_square_sunset 
        with dissolve

        play music music_list["you_won_t_let_me_down"] fadein 3

        window show
        "Когда вы выходите на площадь, там уже столпились пионеры."
        "Ольга Дмитриевна, решительно расталкивая всех, подходит к месту преступления."
        if ds_skill_list['visual_calculus'].check(lvl_medium, passive=True).result():
            play sound ds_sfx_int
            vic "{result}Судя по всему, взорвали Генду."
            vic "Но у злоумышленников ничего не вышло – памятник устоял."
            vic "Лишь на пьедестале видны еле заметные следы копоти."
        show mt angry pioneer at center   with dissolve
        mt "Ну, и кто это сделал?"
        "Она оглядывает толпу пионеров."
        play sound ds_sfx_psy
        esp "Понятно, что это не террористический акт, совершённый группой лиц по предварительному сговору."
        esp "Они все просто пришли сюда посмотреть, что произошло."
        "В толпе ты примечаешь Ульяну и Алису.{w} Похоже, замечает их и вожатая."
        mt "Вы двое, ко мне!"
        "Они протестуют, но всё же подходят."
        show us surp2 pioneer at right 
        show dv normal pioneer at left 
        with dissolve
        us "А что сразу я?"
        dv "Если вы считаете…"
        mt "Двачевская! Покажи-ка руки!"
        show dv surprise pioneer at left   with dspr
        dv "А что с ними не так?"
        if ds_skill_list['perception'].check(lvl_medium, passive=True).result():
            play sound ds_sfx_mot
            per_eye "{result}Руки Алисы измазаны чем-то чёрным."
        mt "Теперь понятно…{w} Из чего бомбу делала?!"
        show dv normal pioneer at left   with dspr
        "Юная террористка, кажется, раздумывает, сознаваться или нет, но потом гордо отвечает."
        show dv smile pioneer at left   with dspr
        dv "Активированный уголь, селитра и сера!"
        play sound ds_sfx_mot
        res "Стоп!{w} Уголь!{w} Уголь из медпункта!"
        mt "И почему именно памятник?{w} Чем тебе помешал уважаемый, заслуженный человек? Борец за права…"

        if ds_lp['dv'] < 20:
            show dv normal pioneer at left   with dspr
            dv "Уголь, кстати, он мне дал."
            "Она показывает пальцем в твою сторону, и тут же вся толпа уставилась на тебя."
            window hide
            menu:
                "Сказать, что по незнанию":
                    window show
                    me "Ну да, я дал уголь..."
                    me "Но я же не знал, что она для вот этого возьмёт!"
                    if ds_karma < 25:
                        show mt rage pioneer at center
                        with dspr
                        mt "Ага, не знал он! Будешь вместе с Двачевской и Советовой отмывать памятник!"
                    else:
                        mt "Даже если и дал, я уверена, что Семён не стал бы участвовать в столь омерзительном антиобщественном акте!"
                "Заявить о соучастии":
                    window show
                    me "Да, я тоже поучаствовал..."
                    show mt rage pioneer at center
                    with dspr
                    mt "Значит, будешь вместе с Двачевской и Советовой драить памятник! До блеска!"
                    $ ds_lp['dv'] += 1
                    $ ds_karma -= 10
                "Отрицать":
                    window show
                    me "Она украла!{w} Я тут ни при чём!"
                    if ds_karma < 0:
                        show mt rage pioneer at center
                        with dspr
                        mt "Да конечно! Будешь вместе с Двачевской и Советовой отмывать памятник!"
                    else:
                        mt "Даже если и дал, я уверена, что Семён не стал бы участвовать в столь омерзительном антиобщественном акте!"
                        me "Да-да, именно!"
                        $ ds_lp['mt'] += 1

        stop music fadeout 3

        "Ольга Дмитриевна ещё долго могла бы отчитывать двух рыжих бестий, но тут вбегает Электроник."
        hide dv 
        hide us 
        hide mt 
        with dissolve
    show el smile pioneer at center   with dissolve
    el "Нашёл! Нашёл!"
    "Все поворачиваются в его сторону."
    play sound ds_sfx_mot
    per_eye "В руке он держит ботинок."
    el "Вот!"
    "Электроник победоносно трясёт им над головой."

    play music music_list["into_the_unknown"] fadein 3

    el "Это ботинок Шурика!"
    show mt normal pioneer at right   with dissolve
    mt "Так, успокойся!{w} Расскажи подробно, где ты его нашёл!"
    show el normal pioneer at center   with dspr
    el "В лесу.{w} На тропинке в старый лагерь!"
    "По рядам проходит какой-то шёпот."
    all "Старый лагерь… Старый лагерь…"
    show mt surprise pioneer at right   with dspr
    mt "Ты уверен?"
    el "Абсолютно!"
    window hide
    menu:
        "Cпросить про старый лагерь" if not ds_visited_old_camp:
            window show
            me "А что такого в этом старом лагере?"
            mt "Да ничего такого на самом деле…"
            "Она запинается."
            el "Одна из легенд «Совёнка» гласит, что там живёт привидение молодой вожатой, которая влюбилась в пионера, но, не найдя взаимности, покончила с собой…"
            show us laugh pioneer at left   with dissolve
            us "Сделала харакири кухонным ножом.{w} А мальчика этого на следующий день сбил автобус!"
            "Ульяна выбегает из толпы."
            me "Автобус?"
            "Ты еле удержался, чтобы не спросить о номере маршрута."
            el "Но наука не допускает существования привидений, поэтому опасаться там нечего!"
        "Сказать, что ты там был" if ds_visited_old_camp:
            window show
            me "Я туда дошёл сегодня... и никого не видел!"
            show mt shocked pioneer at right
            with dspr
            mt "Ты с ума сошёл?!"
            me "А что такое?"
            el "Одна из легенд «Совёнка» гласит, что там живёт привидение молодой вожатой, которая влюбилась в пионера, но, не найдя взаимности, покончила с собой…"
            show us laugh pioneer at left   with dissolve
            us "Сделала харакири кухонным ножом.{w} А мальчика этого на следующий день сбил автобус!"
            "Ульяна выбегает из толпы."
            me "Автобус?"
            "Ты еле удержался, чтобы не спросить о номере маршрута."
            el "Но наука не допускает существования привидений, поэтому опасаться там нечего!"
        "Промолчать":
            window show
            show us smile pioneer at left
            with dissolve
            us "Значит, мы пойдём в старый лагерь? К привидееениям?"
            show mt scared pioneer at right
            with dspr
            mt "Это же опасно. Нет, не из-за привидений. Лагерь уже давно заброшен ведь!"
            mt "Но..."
    show mt normal pioneer at right   with dspr
    mt "Всё равно кто-то должен туда пойти!"
    "Ряды пионеров внезапно начинают редеть."
    sl "Ольга Дмитриевна, ночь уже почти! Может, завтра?"
    hide us 
    hide el 
    hide mt 
    with dissolve
    show sl normal pioneer at right 
    show un normal pioneer at center 
    with dissolve
    "Ты оборачиваешься и увидел Славю с Леной."
    mt "А если ночью…{w} ночью с ним что-нибудь случится…{w} Нет! Сегодня! Сейчас!"
    if not ds_visited_old_camp:
        me "Кстати, а где это?"
        "Электроник примерно объясняет дорогу и рассказывает про историю старого лагеря."
    show mt normal pioneer at left   with dissolve
    "Вожатая пристально смотрит на тебя."
    me "Если вы думаете, что я…"
    mt "Ты один здесь остался из мужчин."
    "Ты осматриваешь площадь."
    play sound ds_sfx_mot
    per_eye "И правда ведь…{w} Электроник куда-то слинял!"
    mt "Ты можешь выбрать себе, с кем ты желаешь пойти."
    window hide
    menu:
        "Пойти с Алисой":
            jump ds_day4_dv_route
        "Пойти с Леной":
            jump ds_day4_un_route
        "Пойти со Славей":
            jump ds_day4_sl_route
        "Пойти с Мику":
            jump ds_day4_mi_route
        "Пойти с Ульяной":
            jump ds_day4_us_route
        "Пойти с Женей":
            jump ds_day4_mz_route
        "Нагнать Электроника":
            jump ds_day4_el_route
        "Пойти одному":
            jump ds_day4_me_route
        "Отказаться" (skill='authority', level=lvl_heroic):
            jump ds_day4_no_shaft

label ds_day4_dv_route:
    $ save_name = u"Disco Sovenok. Рут Алисы. День 4."
    me "А давайте я пойду с Алисой."
    if ds_dv_has_coal:
        show mt angry pioneer at center
        with dspr
        mt "Согласна! Её надо наказать за подорванный памятник!"
    else:
        mt "Да будет так!"
    mt "Двачевская!"
    "Ольга Дмитриевна словно угадала мои мысли."
    hide sl 
    hide un 
    with dissolve
    show dv angry pioneer at right   with dissolve
    dv "Что вам надо?"
    mt "Пойдешь с Семёном за Шуриком!"
    dv "Это ещё почему?!"
    if ds_dv_has_coal:
        show mt angry pioneer at left   with dspr
        mt "А кто памятник взрывал?"
    else:
        show mt angry pioneer at left   with dspr
        mt "Потому что я так сказала!"
    play sound ds_sfx_psy
    aut "Она сказала это таким тоном, что Алиса не решается возражать."
    hide mt  with dissolve
    show dv angry pioneer at right :
        linear 1.0 xalign 0.5
    dv "Доволен?"
    window hide
    menu:
        "Не при делах":
            window show
            me "А я-то тут при чём?"
            if ds_dv_has_coal:
                me "Не я же взрывал памятник!"
        "Посмеяться" if ds_dv_has_coal:
            window show
            me "Так тебе и надо за подорванный памятник!"
            $ ds_lp['dv'] -= 1
        "Посочувствовать":
            window show
            me "Извини, я не хотел так..."
            dv "Да слышала я всё, ты и сказал, что хочешь со мной!"
    show dv guilty pioneer at center   with dspr
    "Алиса фыркает и отворачивается."
    dv "Никуда я с тобой не пойду!"
    play sound ds_sfx_psy
    aut "Только не вздумай умолять её пойти с тобой."
    window hide
    menu:
        "Показать безразличие":
            window show
            me "Да и ради бога!"
            dv "Вот и отлично!"
            me "Прекрасно!"
        "Попросить остаться":
            window show
            me "Останься."
            dv "А вот и не останусь!"
    "Некоторое время вы стоите молча, не смотря друг на друга."
    window hide
    menu:
        "Прервать молчание":
            window show
            me "Это всё?"
            dv "Что всё?"
            me "Всё, что ты хотела мне сказать?"
            dv "Всё!"
            play sound ds_sfx_int
            rhe "Cпроси про памятник."
            me "Тогда можно поинтересоваться, зачем ты пыталась памятник взорвать?"
            show dv normal pioneer  with dspr
            dv "Скучно было…"
            play sound ds_sfx_psy
            vol "А это, конечно, помогло бы развеселиться!"
        "Идти вперёд":
            window show
            "Ты направляешься в сторону лагеря."
    play sound ds_sfx_psy
    sug "Алиса, похоже, действительно не хочет идти с тобой."
    sug "Однако ты-то всё же решил найти Шурика."
    play sound ds_sfx_psy
    ine "Хотя тебя интересует не столько он сам, сколько заброшенный лагерь."
    ine "Почему-то тебе кажется что там ты сможешь что-нибудь выяснить."
    if ds_visited_old_camp:
        ine "Хоть ты уже и был там сегодня и почти ничего не обнаружил."
    play sound ds_sfx_fys
    hfl "А идти одному ночью как-то совсем не хочется…"
    if ds_skill_list['authority'].check(level=lvl_easy, passive=True).result():
        play sound ds_sfx_psy
        aut "{result}Кажется, кое-кто боится старого лагеря... И никогда этого не признает. Возьми на слабо!"
        window hide
        menu:
            "Взять на слабо":
                window show
                me "Значит, боишься?"
                show dv smile pioneer  with dspr
                dv "На слабо меня хочешь взять?"
                "Она ехидно улыбается."
                play sound ds_sfx_mot
                com "Настолько ехидно, что ты моментально теряешься."
                me "Нет, что ты…{w} Тогда счастливо оставаться!"
            "Отбросить мысль":
                window show
                me "Счастливо оставаться!"
    else:
        me "Cчастливо оставаться!"

    stop music fadeout 3

    stop ambience fadeout 2

    hide dv  with dissolve
    "Ты разворачиваешься и шагаешь в ту сторону, где должен находиться старый лагерь."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_path_sunset 
    with dissolve

    play ambience ambience_forest_evening fadein 3

    window show
    "На опушке леса тебя догоняет Алиса."
    show dv normal pioneer at center   with dissolve
    dv "Стой!{w} Я пойду с тобой!"
    window hide
    menu:
        "Cъязвить":
            window show
            me "С чего это вдруг вы соизволили изменить своё решение?"
            show dv angry pioneer at center   with dspr
            dv "Меньше знаешь – лучше спишь!"
            "Огрызается она и протягивает тебе фонарик."
        "Cпросить аккуратно":
            window show
            me "А зачем?"
            show dv angry pioneer at center   with dspr
            dv "Меньше знаешь – лучше спишь!"
            "Огрызается она и протягивает тебе фонарик."
        "Принять":
            window show
            me "Ну ладно..."
            dv "Ещё вот это возьми!"
            "И она отдаёт тебе фонарик."
        "Отвергнуть":
            window show
            me "Ты сказала, что не пойдёшь - значит, не иди!"
            show dv angry pioneer at center
            with dissolve
            dv "А я сказала, что пойду! А ещё тебе явно пригодится вот это!"
            "C этими словами она протягивает тебе фонарик."
    play sound ds_sfx_psy
    esp "Неожиданная, но очень нужная помощь. Если бы не Алиса, непонятно, что бы ты делал там один в темноте…"
    hide dv  with dissolve
    "По рассказам Электроника, старое здание построили сразу после войны."
    "Оно похоже на детский сад и рассчитано на куда меньшее число пионеров, чем вмещал нынешний лагерь."

    stop ambience fadeout 2

    "Забросили же его лет двадцать назад…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_path2_night 
    with dissolve

    $ night_time()

    play ambience ambience_forest_night fadein 3

    play music music_list["door_to_nightmare"] fadein 3

    window show
    if ds_skill_list['conceptualization'].check(level=lvl_easy, passive=True).result():
        play sound ds_sfx_int
        con "{result}Ночной лес совершенно не похож на дневной."
        con "Ещё пару часов назад казалось, что это всего лишь небольшая рощица, где невозможно заблудиться даже слепому."
        con "Однако с наступлением темноты деревья словно вырастают, кустарники внезапно занимают собой всё свободное пространство, а такие широкие в светлое время суток тропинки превращаются в еле заметные волны в тёмно-зелёном лесном океане."
        con "Общую картину довершают птицы, насекомые, звери, которые устраивают концерт, каждый со своим инструментом, создавая вместе удивительную, но в то же время пугающую симфонию ноктюрна."
    show dv normal pioneer at center   with dissolve
    "Идёте вы медленно, Алиса – немного впереди, а ты – позади, стараясь сильно не отставать."
    "Она ведёт себя даже чересчур самоуверенно."
    play sound ds_sfx_fys
    hfl "Совсем не в пример тебе – каждый шорох кустов рядом и крик совы над головой заставлял меня ёжиться и боязливо оглядываться по сторонам."
    hfl "Конечно, понятно, что опасаться здесь особо нечего – вряд ли окрестные леса кишат дикими животными."
    hfl "Однако на уровне инстинкта ты всё равно ощущаешь страх и стараешься идти как можно аккуратнее и быть как можно более внимательным. В конце концов, бережёного бог бережёт."
    "Алиса внезапно останавливается.{w} Так, что ты чуть не врезался в неё."
    show dv surprise pioneer  with dspr
    dv "И куда дальше?"
    me "Что? Ну… Прямо, наверное?"
    show dv normal pioneer  with dspr
    dv "Ты уверен?"
    "Ты прикидываешь направление."
    play sound ds_sfx_int
    vic "Казалось, вы идёте куда надо.{w} По крайней мере туда, куда указал Электроник."
    vic "Однако без карты, GPS- или ГЛОНАСС-навигации ты бы не поручился даже за то, что всё ещё находишься на этой планете (где бы она ни была)."
    me "Мы не сворачивали, шли всё время прямо, Электроник же…"
    show dv angry pioneer  with dspr
    dv "И почему мы тогда ещё не вышли к этому старому лагерю?"
    me "Откуда я знаю?!"
    play sound ds_sfx_mot
    com "Грубый тон Алисы уже начинает выводить тебя из себя."
    dv "Может, мы заблудились вообще?"
    me "С какой стати? Мы отошли максимум на километр от лагеря."
    show dv sad pioneer  with dspr
    dv "Ну и что?"
    "Она заметно грустнеет."
    window hide
    menu:
        "Предложить идти дальше":
            window show
            me "Идём дальше. Думаю, выйдем куда-нибудь."
            show dv angry pioneer at center
            with dspr
            dv "Вот и иди сам! А я возвращаюсь!"
        "Послать в лагерь":
            window show
            me "А ничего! Не нравится – можешь возвращаться."
            "Алиса некоторое время расстроенно смотрит на тебя, потом резко меняется в лице."
            show dv angry pioneer  with dspr
            dv "А вот и вернусь!"
    hide dv  with dissolve
    "Она внезапно разворачивается и бодро шагает в сторону лагеря."
    window hide
    menu:
        "Попрощаться":
            window show
            me "Вот и счастливо!"
            "Бросаешь ты ей вслед."
        "Проводить молча":
            window show
            "Ты провожаешь её взглядом."
    play sound ds_sfx_int
    lgc "Однако, возможно, Алиса всё же была права, и вы таки заблудились.{w} Тогда оставаться одному здесь – не лучшая идея…"

    play sound sfx_wind_gust

    "Сильнее задул прохладный ночной ветер, и ты поёжился."
    play sound ds_sfx_psy
    aut "Но возвращаться за ней – это значит потерять лицо, более того – согласиться с ней."
    window hide
    menu:
        "Оставаться на месте":
            window show
            "Наверное, ты бы мог так рассуждать до утра, если бы не крик Алисы…"
            play sound ds_sfx_psy
            vol "Ноги сами понесли тебя в ту сторону, куда она ушла."

            if ds_skill_list['reaction_speed'].check(level=lvl_medium, passive=True).result():

                scene black 
                show bg ext_path2_night :
                    linear 0.2 pos (0,50)
                    linear 0.2 pos (0,0)

                play sound sfx_jump_over_hole

                play sound2 ds_sfx_mot
                res "{result}Через пару десятков метров ты чуть не проваливаешься в яму, успев в последний момент перепрыгнуть её."
                window hide

                play sound sfx_alisa_falls

                pause(1)

                window show
                play sound ds_sfx_int
                lgc "А вот Алиса, похоже, не успела…"
                "Ты только собирался посветить фонарём в темноту, как понял, что она его забрала с собой."
                aut "Что же, этого стоило ожидать."
                me "Живая?"
                dv "Да…"
                me "Ничего не сломала?"
                dv "Не знаю, блин! Идиот!"
                "В яме мелькает свет, ты подходишь поближе и наклоняешься, чтобы рассмотреть, насколько там глубоко."
                play sound ds_sfx_int
                vic "Вниз метра на 3 уходит узкая дыра, но дальше ничего не видно."
                dv "Помоги мне выбраться!"
                vol "Легко сказать..."
                me "И как ты себе это представляешь?"
                dv "Не знаю как! Придумай!"
                me "Ты где хоть находишься? Опиши."
                dv "Тут туннель какой-то и… Туннель."
                res "Туннель? Странно."
                dv "Спускайся давай!"
                window hide
                menu:
                    "Cпуститься":
                        window show
                        "Ты прыгаешь в яму вслед за Алисой."
                        $ ds_lp['dv'] += 1
                    "Уйти в лагерь":
                        window show
                        me "Ага, ещё чего? Я лучше сбегаю в лагерь за верёвкой."
                        dv "И что, я тут одна останусь?"
                        aut "Нахальства в голосе Алисы заметно поубавилось."
                        me "А ты и так одна, вообще-то, там…"
                        dv "Эй!"
                        "Громко кричит она и направляет луч фонаря прямо тебе в глаза."
                        me "Ладно, не паникуй, авось тебя тролли там не съедят, я быстро!"
                        "Алиса что-то отчаянно орёт снизу, но слов не разобрать."
                        window hide

                        scene black 
                        show bg ext_path2_night :
                            linear 0.1 pos (0,25)
                            linear 0.2 pos (0,-25)
                            linear 0.1 pos (0,0)
                            repeat

                        play sound sfx_simon_fall_1

                        pause(1)

                        window show
                        "Однако не успеваешь ты сделать и пары шагов, как почва у тебя под ногами поехала, и ты начал стремительно проваливаться вниз."

                        stop music fadeout 3

                        stop ambience fadeout 2

                        "Рука ухватывается за тонкий корень, который несколько затормозил падение..."
                        window hide

                        play sound sfx_simon_fall_2

                        pause(1)

                        window show
                        "... однако под твоим весом надламывается и летит вниз вместе с тобой."
                        window hide
            else:
                play sound ds_sfx_mot
                res "{result}Однако, ты слишком поздно осознаёшь, что под тобой оказывается яма - уже когда внезапно падаешь в неё."
        "Пойти за Алисой":
            window show
            "Ты следуешь за Алисой."
            show dv angry pioneer far at center
            with dissolve
            "Вот ты её видишь вдали..."
            show dv shocked pioneer far:
                ease 0.2 ypos 1.0
            with dspr
            "... а вот в следующую секунду она уплывает под землю."
            if ds_skill_list['reaction_speed'].check(level=lvl_medium, passive=True).result():
                play sound ds_sfx_mot
                res "{result}Ты успеваешь подскочить к Алисе и в последний момент схватить её за руку."
                scene cg ds_day4_dv_fall
                with dissolve
                $ ds_lp['dv'] += 1
                me "Держись!"
                dv "Держусь..."
                dv "Держи крепче, а то сейчас упаду!"
                play sound ds_sfx_fys
                pat "Алису нельзя назвать лёгкой как пушинка. Твоя рука, на которой повисла вся её масса, даёт об этом знать."
                play sound ds_sfx_psy
                vol "Поднять её в таком положении - без шансов. Но и отпустить нельзя - это может оказаться смертельным для неё."
                window hide
                menu:
                    "Поднять Алису" (skill='physical_instrument', level=lvl_impossible):
                        if ds_last_skillcheck.result():
                            window show
                            play sound ds_sfx_fys
                            phi "{result}Тем не менее тебе удаётся сделать немыслимое. Алиса начинает мало-помалу подниматься..."
                            play sound ds_sfx_mot
                            svf "Но что это? Когда, казалось, победа была близка, земля под тобой осыпается, и вы с Алисой падаете в яму..."
                        else:
                            window show
                            play sound ds_sfx_fys
                            phi "{result}Как и ожидалось - ты не можешь поднять Алису ни на миллиметр. Напротив, она перетягивает тебя, и вы проваливаетесь в яму."
                    "Отпустить Алису":
                        window show
                        "Cкрепя сердце ты выпускаешь руку Алисы."
                        play sound sfx_alisa_falls
                        "С диким криком и, кажется, матом девочка падает вниз."
                        play sound ds_sfx_mot
                        per_hea "Ты слышишь глухой удар. Можно сделать вывод, что глубина ямы не более пяти метров."
                        me "Ты как там, живая?"
                        dv "ИДИОТ! ТЫ ЧУТЬ НЕ УГРОБИЛ МЕНЯ! Ай!"
                        th "Ну, хоть живая..."
                        "Тут Алиса резко меняется в тоне."
                        dv "Помоги мне выбраться!"
                        vol "Легко сказать..."
                        me "И как ты себе это представляешь?"
                        dv "Не знаю как! Придумай!"
                        me "Ты где хоть находишься? Опиши."
                        dv "Тут туннель какой-то и… Туннель."
                        res "Туннель? Странно."
                        dv "Спускайся давай!"
                        window hide
                        menu:
                            "Cпуститься":
                                window show
                                "Ты прыгаешь в яму вслед за Алисой."
                                $ ds_lp['dv'] += 1
                            "Уйти в лагерь":
                                window show
                                me "Ага, ещё чего? Я лучше сбегаю в лагерь за верёвкой."
                                dv "И что, я тут одна останусь?"
                                aut "Нахальства в голосе Алисы заметно поубавилось."
                                me "А ты и так одна, вообще-то, там…"
                                dv "Эй!"
                                "Громко кричит она и направляет луч фонаря прямо тебе в глаза."
                                me "Ладно, не паникуй, авось тебя тролли там не съедят, я быстро!"
                                "Алиса что-то отчаянно орёт снизу, но слов не разобрать."
                                window hide

                                play sound sfx_simon_fall_1

                                pause(1)

                                window show
                                "Однако не успеваешь ты сделать и пары шагов, как почва у тебя под ногами поехала, и ты начал стремительно проваливаться вниз."

                                stop music fadeout 3

                                stop ambience fadeout 2

                                "Рука ухватывается за тонкий корень, который несколько затормозил падение..."
                                window hide

                                play sound sfx_simon_fall_2

                                pause(1)

                                window show
                                "... однако под твоим весом надламывается и летит вниз вместе с тобой."
                                window hide
                    "Не двигаться":
                        window show
                        "Ты стараешься не двигаться и даже, кажется, не дышать."
                        "Однако, дёргающаяся от страха Алиса всё портит."
                        dv "Ты собираешься вообще доставать меня, придурок?!"
                        me "Подожди, я придумаю, что делать..."
                        dv "Да что тут думать?! Меня доставай!"
                        "Ты хотел было ответить, но земля под тобой обваливается, и вы падаете."

                        play sound sfx_alisa_falls

    scene black 
    with dissolve

    $ ds_health.damage()

    play music ds_dream

    window show
    arb "Смерть. Ещё одна дверь."
    me "Что... что со мной будет?"
    lim "Ты проиграл. Много тысячелетий назад ты проиграл. Проходи, не стесняйся. Продолжай падать в небытие..."
    play sound ds_sfx_psy
    vol "Нет, ты не можешь. Не сейчас - тебе нужно выбраться. Вывести Алису. Найти Шурика. Тебе столько всего ещь сделать надо!"
    play sound ds_sfx_fys
    edr "Ты чувствуешь боль. Тебе было бы неплохо отдохнуть. Но раны не смертельны - выживешь."
    lim "Значит, скоро ты встанешь - и начнёшь всё сначала? Снова метаться, дёргаться, пытаясь узнать непознаваемое, достичь недостижимое?"
    window hide

    $ renpy.pause(1)

    window show
    dv "Ты живой?"
    play sound ds_sfx_psy
    vol "Голос Алисы - не нахальный, а заботливый - тем не менее буквально за шиворот вытягивает тебя из забытья."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_entrance 
    show unblink 
    with dissolve

    play ambience ambience_catacombs fadein 3

    play music music_list["sunny_day"] fadein 5

    $ renpy.pause(1)

    window show
    "Ты с трудом открываешь один глаз, в который тут же ударил яркий свет фонаря."
    play sound ds_sfx_fys
    pat "Фотоны пронзают твою голову - та раскалывается от боли."
    show dv scared pioneer at center   with dissolve
    me "Убери…"
    "Алиса сидит рядом и взволнованно смотрит на тебя."
    dv "Ничего не сломал?"
    me "Не знаю…"
    "Ты шевелишь руками и ногами – как будто всё в порядке."
    play sound ds_sfx_fys
    edr "Учитывая высоту, тебе ещё повезло, что вообще не разбился!"
    "Ты с трудом встаёшь и осматриваешь место падения."
    play sound ds_sfx_mot
    per_eye "Вы действительно находитесь в длинном коридоре, вдоль стен которого протянуты какие-то провода, а под потолком висят лампы, закованные в металлические держатели."
    per_eye "В другой ситуации ты бы сказал, что это подсобный туннель метро."
    play sound ds_sfx_int
    lgc "Но вряд ли пионерлагерь «Совёнок» уже достиг такого уровня развития…"
    show dv sad pioneer at center   with dspr
    dv "Где мы?"
    me "Не знаю, но надо попытаться выбраться!"
    play sound ds_sfx_int
    vic "Залезть по стене на первый взгляд не представляется возможным, да и вообще было не очень понятно, как вы, упав с такой высоты, остались живы."
    me "Ну что же, придётся искать выход в другом месте."
    show dv scared pioneer at center   with dspr
    dv "Это как?"
    "Сейчас на её лице не остаётся и следа былой надменности."
    me "Ну, как-как… Должен же здесь быть выход?"
    show dv sad pioneer at center   with dspr
    dv "Наверное, но куда идти?"
    th "Хороший вопрос."
    play sound ds_sfx_int
    lgc "Направиться в сторону лагеря (хотя бы туда, где он был по моим прикидкам) кажется разумным, но ты не замечал там ничего похожего на выходы из подземелья.{w} Значит, возможно, стоит пойти в противоположную сторону."
    play sound ds_sfx_mot
    inf "Но сначала тебе явно понадобится фонарь."
    window hide
    menu:
        "Отобрать у Алисы":
            window show
            show dv shocked pioneer at center   with dspr
            me "Дай сюда!"
            "Ты грубо вырываешь у Алисы из рук фонарь и направляешь его свет в темноту."
            play sound ds_sfx_psy
            emp "Алиса настолько напугана, что не собирается отвечать даже на столь агрессивный выпад."
        "Попросить у Алисы":
            window show
            me "Дай, пожалуйста."
            dv "Да бери."
            "И она без боя сдаёт тебе фонарь."
        "Доверить фонарь Алисе":
            window show
            me "Будешь ответственной за фонарь!"
            dv "Ладно..."
    window hide
    menu:
        "Пойти в сторону лагеря":
            window show
            me "Туда!"
            window hide

            scene black 
            with dissolve

            window show
            "…"
            window hide

            scene cg d4_catac_dv 
            with dissolve

            window show
            "Вы медленно пробираетесь вперёд, Алиса крепко сжимает твою руку."
            play sound ds_sfx_psy
            vol "В другой ситуации ты бы, может, удивился, смутился, обрадовался (чем чёрт не шутит), но сейчас тебе лишь хочется поскорее выбраться отсюда."
            play sound ds_sfx_fys
            edr "Ссадины от падения болели, в голове ритмично бил тяжёлый маятник, да и дрожащий свет фонаря, выхватывающий из темноты одни и те же бетонные стены, не прибавлял уверенности."
            vol "А ещё Шурик..."
            window hide
            menu:
                "Сказать про Шурика":
                    window show
                    me "Чёрт, ещё же Шурик…"
                    dv "Что?"
                    me "Ну, а зачем мы вообще ночью в лес попёрлись? Чтобы Шурика искать!"
                    dv "Ой, да забудь ты."
                    me "Может, он тоже провалился, как и мы…"
                    vol "Конечно, Алиса в чём-то права – сейчас не самое подходящее время, чтобы заниматься его поисками – если не выберемся, придётся искать вас самих."
                    vol "Однако я не мог просто так выкинуть эту мысль из головы."
                    vol "Как будто перед глазами стоял Шурик и укоризненно смотрел на меня."
                "Отбросить мысль":
                    window show
                    th "Не до Шурика сейчас!"
            dv "Осторожно!"
            window hide

            $ persistent.sprite_time = "night"
            scene bg int_catacombs_door 
            with dissolve

            window show
            "Ты останавливаешься в полушаге от массивной железной двери…"
            play sound ds_sfx_mot
            per_eye "Сразу бросается в глаза значок радиационной опасности."
            me "Значит, мы в бомбоубежище…"
            show dv scared pioneer at center   with dissolve
            dv "Да, что-то такое слышала…"
            me "Слышала? А почему раньше не сказала?"
            show dv sad pioneer at center   with dspr
            dv "Откуда я знала, что это важно?"
            play sound ds_sfx_int
            rhe "Здесь и не возразишь."
            me "Ну, пожалуй, да… Ладно."
            hide dv  with dissolve
            window hide
            menu:
                "Открыть дверь самому" (skill='physical_instrument', level=lvl_formidable):
                    if ds_last_skillcheck.result():
                        window show
                        play sound ds_sfx_fys
                        phi "{result}Ты берёшься за колесо двери и что есть мочи начинаешь давить на него, пытаясь провернуть."

                        play sound sfx_metal_door_handle_rattle

                        "Заржавевший металл скрипит и наконец поддаётся."
                    else:
                        window show
                        play sound ds_sfx_fys
                        phi "{result}Ты начинаешь крутить колесо, но руки просто проскальзывают по нему, не сдвигая ничуть."
                        play sound sfx_metal_door_handle_rattle
                        "Алиса некоторое время наблюдает, но потом крепко хватается за ручку и начинает дёргать на себя."
                        play sound sfx_open_metal_hatch
                "Попросить помощи Алисы":
                    window show
                    me "Помоги, что ли, что стоишь!"
                    "Алиса некоторое время колеблется, но потом крепко хватается за ручку и начинает дёргать на себя."

                    play sound sfx_open_metal_hatch
                "Развернуться":
                    window show
                    me "Да ну её, эту дверь! Идём в другую сторону!"
                    dv "Идём..."
                    window hide

                    scene cg d4_catac_dv 
                    with dissolve

                    play ambience ambience_catacombs fadein 3

                    window show
                    "Алиса крепко держит тебя за руку, идя ровно шаг в шаг."
                    "Вы так же медленно идёте назад, внимательно высматривая дыру в потолке."
                    "Однако туннель кажется бесконечным – вам не удаётся найти место падения ни через пять, ни через десять минут."
                    window hide
                    jump ds_dv_day4_forward_tunnel
            stop ambience fadeout 2

            "Наконец колесо прокручивается до конца, и дверь открывается."
            window hide

            $ persistent.sprite_time = "sunset"
            scene bg int_catacombs_living 
            with dissolve

            window show
            play sound ds_sfx_int
            vic "Вы оказываетесь в комнате, назначение которой можно установить безошибочно – бомбоубежище."
            vic "Шкафы с противогазами и сухпайками, различная аппаратура, койки и трубы вентиляции – всё здесь было сделано для того, чтобы пережить ядерную войну.{w} Ну, или по крайней мере выжить после первого удара."
            show dv scared pioneer at center   with dissolve
            "Алиса ещё крепче сжимает твою руку."
            me "Что?"
            dv "Что-что…"
            "Шёпотом лепечет она."
            show dv sad pioneer at center   with dspr
            dv "Страшно…"
            me "А чего тут бояться?"
            play sound ds_sfx_psy
            emp "Действительно, чего?"
            emp "Вы провалились в заброшенное бомбоубежище, бродим тут впотьмах, пытаемся найти выход…{w} Чего бояться, особенно девочке?"
            show dv sad pioneer close at center    with dissolve
            play sound ds_sfx_fys
            hfl "От этих мыслей тебя передёрнуло, и ты инстинктивно подошёл ближе к Алисе."
            "Она ничего не говорит, лишь слегка краснеет и отворачивается."
            me "Ладно, в любом случае…"
            dv "Что?"
            me "Надо искать выход."
            dv "Ну, вот ещё одна дверь."
            "У дальней стены точно такая же дверь, как та, через которую вы попали сюда."
            window hide
            menu:
                "Открыть дверь":
                    window show
                    hide dv  with dissolve
                    phi "Однако, она не поддаётся. Сколько бы ты ни старался"
                    show dv sad pioneer at center   with dissolve
                    dv "Помочь?"
                    me "Нет, тут намертво заклинило…"
                    "Ты окидываешь комнату взглядом в поисках чего-нибудь, что может сойти за рычаг."
                    if ds_skill_list['perception'].check(level=lvl_easy, passive=True).result():
                        play sound ds_sfx_mot
                        per_eye "{result}В дальнем углу ты примечаешь фомку."
                        me "Отлично!"
                        show dv surprise pioneer at center   with dspr
                        "Алиса непонимающе смотрит на тебя."
                        me "Сейчас!"

                        play sound sfx_insert_crowbar_door

                        "Но и с помощью фомки ручка не сдвигается ни на сантиметр…"
                "Отбросить мысль":
                    window show
                    me "Нет. Не откроется. Да и сил у меня больше нет!"
            "Ты без сил опускаешься на аккуратно застеленную кровать и вздыхаешь."
            me "Придётся идти назад."
            show dv normal pioneer at center   with dspr
            dv "Но мы же оттуда пришли!"
            play sound ds_sfx_mot
            com "Похоже, к Алисе немного возвращается самообладание, а с ним и привычное нахальство."
            window hide
            menu:
                "Предложить остаться":
                    window show
                    me "Ты можешь остаться здесь – вода, сухпайки, может, радио ещё работает…"
                    show dv angry pioneer at center   with dspr
                    "Она злобно посмотрела на тебя, но ничего не отвечает."
                    play sound ds_sfx_psy
                    esp "Она не готова оставить тебя одного."
                    play sound ds_sfx_psy
                    emp "Да и самой страшно оставаться одной."
                "Сказать, что надо":
                    window show
                    me "Ну а что нам ещё делать? Тут, как видишь, тупик."
                    "Алиса ничего не отвечает тебе на это."
            show dv normal pioneer at center   with dspr
            play sound ds_sfx_fys
            edr "Всё тело ужасно болит."
            edr "Ты это понял только в состоянии покоя, расслабившись."
            edr "На ноге сильно кровоточит глубокий порез, все руки в ссадинах, а в волосах запеклась кровь."
            play sound ds_sfx_psy
            emp "А как Алиса?"
            window hide
            menu:
                "Спросить про самочувствие":
                    window show
                    me "Ты-то… нормально?"
                    "Она отвечает не сразу."
                    show dv sad pioneer at center   with dspr
                    dv "Ну, как тут в такой ситуации может быть нормально."
                    $ ds_lp['dv'] += 1
                "Промолчать":
                    window show
            "Тут Алиса примечает порез у тебя на ноге."
            show dv shocked pioneer at center   with dspr
            dv "Ой!"
            dv "Надо срочно продезинфицировать."
            window hide
            menu:
                "Cогласиться":
                    window show
                    me "Давай..."
                "Отказаться":
                    window show
                    me "Не надо. Жить буду."
                    dv "Нет-нет! Нельзя так, вдруг заражение пойдёт, потом ногу отрежут!"
                    play sound ds_sfx_psy
                    emp "Алиса выглядит и правда обеспокоенной. Лучше не спорь."
                    me "Ладно, но мы сейчас далековато от медпункта."
                    show dv smile pioneer at center   with dspr
                    dv "Ничего."
                    hide dv  with dissolve
                    "Улыбается она и принимается рыться в шкафах."
            show dv smile pioneer at center   with dissolve
            lgc "Действительно, стоило ожидать, что в бомбоубежище найдутся какие-то средства первой помощи"
            "И вскоре Алиса торжествующе демонстрирует тебе аптечку."
            dv "Не дёргайся."
            me "Постараюсь."
            play sound ds_sfx_fys
            pat "Ватный тампон, смоченный йодом, проходится по ране, словно раскалённый нож, заставив тебя крепко стиснуть зубы и зашипеть от боли."
            show dv guilty pioneer at center   with dspr
            dv "Ой, да ладно, как будто так больно."
            me "Больно! Сама попробуй!"
            "С остальными ранами было попроще, и вскоре ты стал напоминать леопарда – весь усеянный коричневыми пятнами."
            $ ds_health.up()
            me "Спасибо…"
            show dv shy pioneer at center   with dspr
            dv "Не подумай ничего, просто надо было обработать раны!"
            "Алиса фыркает и отворачивается."
            me "Да-да…"
            play sound ds_sfx_psy
            aut "Ну конечно же она не имеет никаких чувств к тебе! Да кому она рассказывает?"
            "Ты рывком встаёшь с кровати."
            "Непродолжительный отдых явно пошёл тебе на пользу."
            $ ds_health.restore()
            show dv normal pioneer at center   with dspr
            me "Ну что, пойдём?"
            window hide

            scene cg d4_catac_dv 
            with dissolve

            play ambience ambience_catacombs fadein 3

            window show
            "Алиса крепко держит тебя за руку, идя ровно шаг в шаг."
            "Вы так же медленно идёте назад, внимательно высматривая дыру в потолке."
            "Однако туннель кажется бесконечным – вам не удаётся найти место падения ни через пять, ни через десять минут."
            window hide
        "Пойти в противпоположную сторону":
            window show
            me "Туда!"
            "Алисы послушно следует за тобой."
    jump ds_dv_day4_forward_tunnel

label ds_dv_day4_forward_tunnel:
    $ persistent.sprite_time = "night"
    scene bg int_catacombs_entrance 
    with dissolve

    show dv sad pioneer at center   with dissolve
    window show
    dv "Мы заблудились?"
    me "Заблудиться можно в лесу, допустим…"
    play sound ds_sfx_psy
    sug "Вы буквально это провернули полчаса назад! Не пугай её ещё больше!"
    me "А тут прямой туннель – не заблудишься!"
    dv "Ну и куда мы выйдем?"
    play sound ds_sfx_psy
    emp "Похоже, твои слова не сильно успокоили Алису."
    me "Выйдем куда-нибудь, всегда есть выход."
    dv "Всегда ли?"
    me "Ну конечно! Ведь когда его строили, рабочие как-то выбрались наверх, ведь так?"
    dv "Ну да, наверное."
    play sound ds_sfx_mot
    com "Кажется, она изо всех сил старается выглядеть как обычно, но выходит с трудом – в тусклом свете фонаря видно, как тело Алисы изредка подрагивает, а на лице застыло выражение крайнего напряжения."
    me "Ладно, пойдём дальше!"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_hole 
    with dissolve

    window show
    play sound ds_sfx_mot
    per_eye "Через пару минут ты замечаешь дыру в полу."
    play sound ds_sfx_int
    vic "Достаточно большую, похоже образовавшуюся от взрыва, в которую вполне можно пролезть."
    show dv scared pioneer at center   with dissolve
    dv "А что там?"
    me "Не знаю…"
    "Ты наклоняешься и светишь фонарём вниз"
    per_eye "Cырая земля, какие-то рельсы."
    me "Наверное, шахта."
    show dv surprise pioneer at center   with dspr
    "Алиса вопросительно смотрит на меня."
    play sound ds_sfx_int
    lgc "Конечно, дыру можно легко обойти, но что-то тебе подсказывает, что дальше ничего хорошего вас не ждёт – тупик или очередная закрытая дверь."
    lgc "Хотя, с другой стороны, рассчитывать на то, что выход может скрываться в шахте, тоже глупо."
    if ds_skill_list['interfacing'].check(level=lvl_medium, passive=True).result():
        play sound ds_sfx_mot
        inf "{result}Сделай отметку. На случай, если потребуется вернуться."
    window hide
    menu ds_dv_day4_near_hole:
        set ds_menuset
        "Cделать отметку" if ds_last_skillcheck.result(invoke_callbacks=False):
            window show
            "Ты берёшь ближайший уголёк и делаешь на стене стрелку, направленную в сторону убежища."
            me "Так мы сможем вернуться в бомбоубежище!"
            dv "Ага..."
            $ ds_set_path_mark = True
            jump ds_dv_day4_near_hole
        "Обойти дыру":
            window show
            me "Пойдём в обход. Если не повезёт - вернёмся сюда."
            show dv sad pioneer at center   with dspr
            "На её лице появляется страдальческое выражение, затем Алиса отворачивается от света и тихо говорит."

            stop ambience fadeout 3

            dv "Как скажешь…"
            play sound ds_sfx_psy
            aut "Ей очень неудобно признавать твой авторитет."
            window hide
            jump ds_dv_day4_lab
        "Cпуститься в шахту":
            window show
            me "Можно проверить. В крайнем случае вернёмся – глубина позволяет выбраться потом."
            show dv sad pioneer at center   with dspr
            "На её лице появляется страдальческое выражение, затем Алиса отворачивается от света и тихо говорит."

            stop ambience fadeout 3

            dv "Как скажешь…"
            play sound ds_sfx_psy
            aut "Ей очень неудобно признавать твой авторитет."
            window hide
            jump ds_dv_day4_shaft

label ds_dv_day4_lab:
    $ persistent.sprite_time = 'night'
    scene bg ds_tunnel1
    show dv sad pioneer at center
    with dissolve
    "Вы с Алисой продолжаете идти вдоль тоннеля."
    scene bg ds_tunnel2
    show dv sad pioneer at center
    with dissolve
    "Тьма постепенно сгущается вокруг вас. И конца и края ей не видно."
    dv "Мы точно... идём куда надо?"
    me "Наверное..."
    scene bg ds_tunnel3
    show dv sad2 pioneer at center
    with dissolve
    "Вот вы оказываетесь почти в полной темноте."
    play sound ds_sfx_mot
    per_toc "Ты можешь ощутить, как рука Алисы ещё сильнее сжимает твою."
    scene bg ds_int_cs_lab_entry
    show dv shocked pioneer at center
    with dissolve
    "И внезапно вы выходите к помещению с очень большой дверью, украшенной знаками опасности."
    dv "Что... это?"
    me "Не знаю..."
    play sound ds_sfx_psy
    ine "Кажется, за этой дверью таится что-то интересное. Для тебя. Может, и для Алисы."
    window hide
    menu:
        "Зайти":
            window show
        "Развернуться":
            window show
            me "Идём обратно."
            "Алиса молча тебе подчиняется."

    "Ты подходишь к двери и видишь рядом с ней щиток."
    play sound ds_sfx_mot
    inf "Похоже на электронный замок. Попробуй нажать что-нибудь."
    "Ты жмёшь большую зелёную кнопку. Она отзывается тебе, медленно раскрывая дверь."
    me "Заходим!"
    "Алиса забегает в открывшийся проход. Ты следуешь за ней."
    $ persistent.sprite_time = 'sunset'
    scene bg ds_int_cs_lab
    show dv shocked pioneer at center
    with dissolve
    "Перед вами предстаёт лаборатория. Какие-то приборы, пробирки, а для чего всё это - тебе решительно непонятно."
    dv "Что... это? Как... оно оказалось тут?"
    me "Cамому бы знать..."
    hide dv with dissolve
    "Алиса подбегает к ящикам и начинает их осматривать. Ты тоже начинаешь оглядывать шкаф."
    "Внезапно Алиса издаёт удивлённый вопль."
    dv "Иди сюда!"
    show dv scared pioneer at center
    with dissolve
    "Ты подходишь к ней, и она протягивает тебе книгу."
    dv "Посмотри... сюда..."
    "Ты открываешь книгу и видишь в ней..."
    play sound ds_sfx_mot
    per_eye "Cвой мир. Словно камера облетает его."
    th "Как? Как это возможно?"
    if ds_skill_list['encyclopedia'].check(level=lvl_medium, passive=True).result():
        play sound ds_sfx_int
        enc "{result}Не иначе, Д'ни постарались... И символы похожи..."
        th "Д'ни? Кто это?"
        enc "Народ, владевший искусством писать книги перемещения между мирами. По крайней мере, в компьютерных играх серии Myst так было!"
        enc "Но тут, кажется, ты держишь в руках пример... настоящей книги перемещения."
    play sound ds_sfx_psy
    vol "Почему-то тебе очень хочется прикоснуться к этой картинке."
    window hide
    menu:
        "Прикоснуться":
            window show
            "Ты прикладываешь свою руку к картинке."
            play sound ds_linking
            scene black
            with ds_disintegration
            "Мир вокруг тебя словно разрушается, сменяясь тьмой."
            jump ds_end_preterm_return
        "Предложить Алисе прикоснуться":
            window show
            me "Попробуй... приложить сюда руку..."
            dv "Ладно..."
            "Алиса прикладывает руку..."
            hide dv with dissolve
            $ volume(0.2,"sound")
            play sound ds_linking
            "...и исчезает."
            $ volume(1.0,"sound")
            th "Неужели это... книга телепортации?"
            play sound ds_sfx_int
            lgc "Это значит, что Алиса... угодила в твой мир?!"
            window hide
            menu:
                "Телепортироваться за Алисой":
                    window show
                    "Ты прикладываешь свою руку к картинке."
                    play sound ds_linking
                    scene black
                    with ds_disintegration
                    "Мир вокруг тебя словно разрушается, сменяясь тьмой."
                    jump ds_end_preterm_return_dv
                "Забить":
                    window show
                    "Ты закрываешь книгу и кладёшь её на стол."
                    scene bg ds_int_cs_lab_entry
                    with dissolve
                    "Покидаешь лабораторию, не забыв закрыть дверь."
                    "И уходишь."
                    scene black with dissolve2
                    stop ambience
                    jump ds_end_dv_sent_to_rf
        "Закрыть книгу":
            window show
            me "Я думаю... лучше её не трогать."
            dv "Как скажешь..."
            "Ты захлопываешь книгу и кладёшь её на стол."
            $ ds_seen_linking_book = True
        "Взять книгу с собой":
            window show
            me "У тебя есть, куда положить эту книгу?"
            show dv angry pioneer at center
            with dspr
            dv "Ты идиот или да? В отличие от тебя, у меня даже карманов нет!"
            play sound ds_sfx_mot
            inf "И то верно."
            "Ты с трудом убираешь книгу к себе в карман - благо она всё же не больше блокнота."
            $ ds_seen_linking_book = True
            $ ds_took_linking_book = True
    me "Что-то ещё тут есть?"
    dv "Ничего... Совсем ничего... Точнее, тут много всего... но я вообще не понимаю, для чего это всё!"
    show dv angry pioneer at center
    with dspr
    dv "Куда ты вообще притащил меня?!"
    me "Сейчас... сейчас найдём выход..."
    play sound ds_sfx_mot
    per_eye "Тут твой взгляд привлекает маленькая дверь."
    window hide
    menu:
        "Пройти в дверь":
            window show
            me "Идём туда."
            show dv sad pioneer at center
            with dspr
            dv "Ладно... веди уже..."
            $ persistent.sprite_time = 'night'
            scene bg ds_int_cs_lab_exit
            show dv sad pioneer at center
            with dspr
            "На выходе оказывается новый туннель. Впрочем, короткий."
            scene bg ds_elevator_up
            show dv surprise pioneer at left
            with dissolve
            "Вскоре он заканчивается дверью лифта."
            dv "Cкажи... что он ведёт наверх..."
            me "Не знаю..."
            window hide
            menu:
                "Вызвать лифт":
                    window show
                    play sound ds_call_elevator
                    "Ты нажимаешь кнопку «вверх»."
                    play sound ds_sfx_mot
                    per_hea "Зазвучали механизмы и, кажется, сверху что-то поехало к вам."
                    scene bg ds_elevator_down
                    show dv shocked pioneer at left
                    with dissolve
                    "Вскоре к вам приезжает лифт."
                    me "Заходи."
                    dv "Ага..."
                    hide dv with dissolve
                    "И Алиса осторожно проходит в лифт. Ты следуешь за ней."
                    scene bg ds_int_elevator
                    show dv shocked pioneer at center
                    with dissolve
                    "Ты закрываешь дверь и нажимаешь кнопку «вверх»."
                    play music ds_up_and_out fadein 3
                    play sound_loop ds_elevator_up
                    "Лифт дёргается и отправляется вверх."
                    show dv scared pioneer at center
                    with dspr
                    "Алиса прижимается к тебе. Лицо её выглядит испуганным."
                    me "Не переживай... мы едем наверх... наружу..."
                    "Ты поглаживаешь её по голове. Она ничего не отвечает."
                    play sound ds_sfx_mot
                    inf "Механизм лифта производит впечатление старого. Периодически что-то искрит, а сам лифт подёргивается."
                    play sound ds_sfx_fys
                    hfl "Довезёт ли он вас?"
                    play sound ds_sfx_psy
                    vol "Деваться всё равно некуда."
                    window hide
                    $ renpy.pause(1.0)
                    window show
                    stop sound_loop
                    stop music fadeout 3
                    play sound ds_stop_elevator
                    "Cпустя пару минут лифт останавливается."
                    "Ты распахиваешь дверь и выходишь. Алиса за тобой."
                    scene bg ds_int_old_building_room_night
                    show dv scared pioneer at center
                    with dissolve
                    if ds_found_elevator:
                        th "Та самая комната... где я сегодня был... с лифтом..."
                        play sound ds_sfx_int
                        lgc "Так вот куда этот лифт ведёт. Одной загадкой меньше! Только вот кому и зачем понадобился этот лифт?"
                    me "Ура! Свобода!"
                    show dv angry pioneer at center
                    with dspr
                    dv "Ну и куда ты меня привёз?!"
                    me "Ну... мы по крайней мере вышли из подземелий! Теперь нам осталось совсем немного!"
                    dv "Вот и пошли сейчас!"
                    jump ds_dv_day4_old_camp
                "Вернуться в лабораторию":
                    window show
                    me "Лучше пойдём назад."
                    dv "Как скажешь..."
                    scene bg ds_int_cs_lab
                    show dv sad pioneer at center
                    with dspr
                    "Через пару минут вы вновь оказываетесь в лаборатории."
        "Выйти в тоннель":
            window show
            scene bg ds_int_cs_lab_entry
            with dissolve
            "Вы выходите обратно в тоннель."
            $ ds_visited_lab = True
            if ds_visited_mine:
                jump ds_dv_day4_return
            scene bg int_catacombs_hole 
            with dissolve
            "Вскоре вы возвращаетесь к дыре."
            window hide
            menu:
                "Cпуститься в шахту":
                    window show
                    me "Cпускаемся."
                    show dv sad pioneer at center   with dspr
                    "На её лице появляется страдальческое выражение, затем Алиса отворачивается от света и тихо говорит."

                    stop ambience fadeout 3

                    dv "Как скажешь…"
                    play sound ds_sfx_psy
                    aut "Ей очень неудобно признавать твой авторитет."
                    window hide
                    jump ds_dv_day4_shaft
                "Вернуться в убежище":
                    window show
                    me "Идём туда."
                    show dv sad pioneer at center
                    with dspr
                    dv "Ну идём..."
                    jump ds_dv_day4_return
        "Лечь спать тут":
            window show
            me "Слушай. Лаборатория не выглядит заброшенной. Давай тут останемся на ночь."
            dv "Давай..."
            "Алиса укладывается на раскладушке, стоящей в углу, в то время как ты располагаешься на кресле, положив голову на стол."
            scene black with dissolve
            show blink
            "Ты быстро засыпаешь."
            jump ds_end_found_in_lab_dv

label ds_dv_day4_shaft:
    $ persistent.sprite_time = "night"
    scene bg int_mine 
    with dissolve

    play ambience ambience_catacombs_stones fadein 3

    window show
    "Вы действительно оказались в шахте: вдаль уносились давно заржавевшие рельсы, по которым когда-то, наверное, со скрипом проносились набитые доверху вагонетки; стены укреплены подгнившими балками, а с потолка изредка капает вода."
    play sound ds_sfx_int
    con "Нельзя сказать, что здесь страшнее, чем в катакомбах бомбоубежища – скорее там, «наверху», царит постапокалиптика, а здесь, «внизу» – оккультные истории Средневековья."
    play sound ds_sfx_fys
    hfl "В любом случае теье ещё сильнее захотелось убраться отсюда, и как можно быстрее."
    show dv sad pioneer at center   with dissolve
    "Алиса не говорит ни слова после того, как вы спустились в шахту – лишь идёт рядом, крепко сжимая твою руку."
    play sound ds_sfx_psy
    emp "Ты начинаешь волноваться."
    me "Всё в порядке?"
    dv "Нет."
    play sound ds_sfx_int
    rhe "«В порядке» тут быть и не может."
    me "Ну, я понимаю, что «в порядке» быть не может, но ты как, держишься?"
    dv "Да."
    "Тем же безучастным тоном отвечает Алиса."
    me "Ну, это хорошо, потому что…"
    sug "Ты хотел было сказать «потому что если и у тебя ещё крыша поедет, то тушите свет» - но благоразумно воздерживаешься."
    me "Потому что выход мы найдём. Обязательно найдём."
    dv "Угу…"
    emp "Похоже, что долго она не выдержит."
    play sound ds_sfx_psy
    vol "А значит, надо идти быстрее!"
    "Ты прибавляешь шагу, и через пару десятков метров вы оказываетесь у развилки."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad 
    with dissolve

    window show
    me "Так…"
    show dv sad pioneer at center   with dissolve
    dv "И куда?"
    emp "Похоже, Алиса окончательно отключилась от внешнего мира, и её уже не волнует то, что будет с вами, то, как выбраться отсюда."
    me "Ну, сейчас подумаем..."
    th "Направо или налево?{w} А если заблудимся…"
    play sound ds_sfx_mot
    inf "Сделай засечку."
    "Ты делаешь отметку на стене - на случай возвращения."
    "Вскоре на одной из балок красуется большой крест, нацарапанный камнем."
    me "Так, вот теперь можно идти…"
    window hide

    $ ds_mine_route = "dv"

    jump ds_day4_mine

label ds_day4_mine:

    $ ds_point = "1"
    $ ds_previous_point = "1"
    $ ds_halt_visited = False
    $ ds_coalface_visited = False
    $ ds_back_to_start = False
    $ ds_first_turn = True

    jump ds_day4_mine_crossroad

label mine_crossroad:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad 
    with fade

    if not ds_first_turn:
        th "Похоже, ещё одна равилка."

    menu:
        "Налево":
            $ ds_first_turn = False
            $ ds_mine_eval("left")
        "Направо":
            $ ds_first_turn = False
            $ ds_mine_eval("right")

label ds_day4_alone_mine_return:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad 
    with fade

    window show
    "Ты возвращаешься к тому месту, с которого и начинал."
    play sound ds_sfx_int
    lgc "Значит, где-то не там повернул."
    window hide

    menu:
        "Налево":
            $ ds_mine_eval("left")
        "Направо":
            $ ds_mine_eval("right")

label ds_day4_girls_mine_return:

    $ persistent.sprite_time = "night"
    scene bg int_mine_crossroad 
    with fade

    window show
    "Вы возвращаетесь к тому месту, с которого и начинали."
    play sound ds_sfx_int
    lgc "Значит, где-то не там повернули."
    window hide

    menu:
        "Налево":
            $ ds_mine_eval("left")
        "Направо":
            $ ds_mine_eval("right")

label ds_dv_day4_mine_coalface:

    $ persistent.sprite_time = "night"
    scene bg int_mine_halt
    with fade

    if coalface_visited:
        window show
        "Здесь мы уже были."
        window hide

        jump ds_dv_day4_mine_crossroad

    show dv sad pioneer at center   with dissolve
    window show
    "Наконец мы вышли из туннеля в довольно большую комнату с высоким потолком."
    "Хотя комнатой это можно было назвать только с натяжкой – похоже, здесь что-то добывали.{w} Возможно, уголь, может, золото."
    "Все стены были изрублены то ли киркой, то ли отбойным молотком."
    "Здесь царил кромешный мрак, поэтому единственным нашим спасением оставался фонарик."
    th "Сломайся он, и мы вряд ли когда-нибудь выберемся отсюда…"
    "В его свете я заметил в углу какую-то красную тряпку."
    "Это был пионерский галстук!"
    "Теперь-то ясно, что Шурик здесь."
    me "Шурик! Шурик!"
    "Ответом мне стало лишь эхо."
    dv "Чего кричать? Как будто он тебя слышит..."
    me "Ну а вдруг?"
    "Алиса ничего не ответила, лишь вздохнула."
    "Из этой комнаты не было другого выхода."
    th "Конечно, возможно, в этих туннелях есть ещё места, где мы не бывали…"
    th "Значит, придётся искать дальше!"
    window hide

    $ coalface_visited = True

    jump ds_dv_day4_mine_crossroad

label ds_dv_day4_mine_uv:
    $ persistent.sprite_time = "night"
    scene bg int_mine_coalface
    show dv sad pioneer at center
    with dissolve

    "Вы выходите из туннеля в зал. Кругом тебя необычно светятся кристаллы."
    play sound ds_sfx_mot
    per_eye "Здесь имеется лампа - но она погашена. А свет тем не менее есть."
    dv "Это... куда мы зашли?.."
    play sound ds_sfx_int
    lgc "Самим бы знать."
    play sound ds_sfx_int
    rhe "Ты даже не знаешь, что ответить."
    "Вы уже собирались было идти дальше, как краем глаза ты примечаешь в глуби... силуэт?"
    window hide
    menu:
        "Проследить за силуэтом" (skill='perception', level=lvl_challenging):
            if ds_last_skillcheck.result():
                window show
            else:
                window show
                play sound ds_sfx_mot
                per_eye "{result}К сожалению, ты теряешь силуэт из виду. Где он?"
                me "Эх, упустил..."
                show dv surprise pioneer at center
                with dspr
                dv "Ты о чём?"
                me "Да увидел какую-то... фигуру..."
                show dv shocked pioneer at center
                with dspr
                "Алису твои сведения напрягли."
                dv "Идём отсюда!"
                "И вы направляетесь дальше."
                $ ds_coalface_visited = True
                jump ds_day4_mine_crossroad
        "Идти дальше":
            window show
            me "Идём!"
            dv "Ага..."
            "И вы направляетесь дальше."
            $ ds_coalface_visited = True
            jump ds_day4_mine_crossroad
    play sound ds_sfx_mot
    per_eye "{result}Ты всматриваешься в силуэт..."
    play music music_list["mystery_girl_v2"] fadein 5
    scene cg ds_day4_uv_appear1
    with dissolve
    play sound ds_sfx_psy
    ine "Он создаёт ощущение одновременно человеческого... и нечеловеческого..."
    dv "Что там?.."
    me "Не вижу... но что-то необычное... кажется, там человек..."
    "Алиса направляет туда фонарик."
    per_eye "Теперь ты отчётливее некуда видишь..."
    scene cg ds_day4_uv_appear2
    with dissolve
    per_eye "...девушку. В одном платьице, с длинными коричневыми косами и... кошачьими ушами! Попрошу заметить - реальными!"
    th "Что за... чертовщина?"
    play sound ds_sfx_int
    enc "Это ещё мягко сказано. Твои знания не допускают существования кошкодевочек в реальном мире - это принадлежность манги, аниме - но и только!"
    per_eye "Но тем не менее ты её видишь."
    play sound ds_sfx_psy
    vol "Спроси у Алисы."
    me "Ты это... видишь?"
    dv "Да... я вижу... я уж подумала, что с ума сошла!"
    vol "Как и ты. Твой вопрос принёс облегчение вам обоим."
    "Заметив вас, странная девочка сначала боязливо осматривает, а затем потихоньку подползает к вам."
    scene bg int_mine_coalface
    show dv scared pioneer at fleft
    show uv surprise dress at center
    with dissolve
    play sound ds_sfx_int
    vic "Девочка как девочка. Ростом с Женю. Если бы не кошачьи уши..."
    window hide
    menu ds_dv_day4_uv_encounter:
        set ds_menuset
        "Прислушаться":
            window show
            play sound ds_sfx_mot
            per_toc "Воздух подёргивается возле девочки. Кажется, она принюхивается к тебе."
            per_hea "Можно услышать мурчание. Что-то ей в тебе понравилось."
            "Она помахивает хвостиком, словно приветствует им тебя."
            window hide
            jump ds_dv_day4_uv_encounter
        "Поприветствовать":
            window show
            "Ты поднимаешь руку в приветствии. Девочка с интересом смотрит на неё."
            "Тишина. Она застывает."
            play sound ds_sfx_fys
            hfl "Что-то сейчас будет."
            show uv dress smile at center
            with dspr
            "Но девочка складывает руки и, кажется, улыбается."
            play sound ds_sfx_mot
            per_hea "Ты можешь услышать тихий детский смех."
            window hide
            jump ds_dv_day4_uv_encounter
        "Дать кошкодевочке имя" (skill='conceptualization', level=lvl_up_medium):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_int
                con "{result}Юля. Имя Юля ей подойдёт идеально."
                $ meet('uv', u'Юля')
                window hide
                jump ds_dv_day4_uv_encounter
            else:
                window show
                play sound ds_sfx_int
                con "{result}Ты пытаешься ухватить имя за хвост - но оно выскальзывает и убегает."
                $ meet('uv', u'Кошкодевочка')
                window hide
                jump ds_dv_day4_uv_encounter
        "Заговорить с девочкой" (skill='inland_empire', level=lvl_foimidable):
            if ds_last_skillcheck.result():
                window show
                play sound ds_sfx_psy
                ine "{result}Ты подходишь ближе к кошкодевочке. Она продолжает на тебя смотреть с неменьшим интересом."
            else:
                window show
                play sound ds_sfx_psy
                ine "{result}Она не ответит тебе. По всем признакам она не наделена разумом."
                me "Идём..."
                dv "Ладно..."
                show uv sad dress at center
                with dspr
                "Девочка с грустным лицом провожает тебя."
                stop music fadeout 5
                show blinking
                hide uv
                "А когда ты моргаешь - она исчезает, будто её и не было."
                show dv shocked pioneer at center
                with dspr
                dv "Что... это было?.."
                me "Не знаю... но нам надо двигаться дальше..."
                $ ds_coalface_visited = True
                jump ds_day4_mine_crossroad
        "Уйти":
            window show
            me "Идём..."
            dv "Ладно..."
            show uv sad dress at center
            with dspr
            "Девочка с грустным лицом провожает тебя."
            stop music fadeout 5
            show blinking
            hide uv
            "А когда ты моргаешь - она исчезает, будто её и не было."
            show dv shocked pioneer at center
            with dspr
            dv "Что... это было?.."
            me "Не знаю... но нам надо двигаться дальше..."
            $ ds_coalface_visited = True
            jump ds_day4_mine_crossroad
    me "Что... ты делаешь тут?"
    show uv smile dress at center
    with dspr
    uv "Я существую."
    window hide
    menu ds_dv_day4_uv_dialogue:
        set ds_menuset
        "Я тоже существую":
            window show
            me "Я тоже существую."
            uv "И как оно?"
            me "Тяжело... я, кажется, болен..."
            show uv guilty dress at center
            with dspr
            uv "Чем ты болен?"
            me "Грустью. Внутри меня огонь - и он испепеляет меня. Это всё из-за моей головы."
            uv "Я не вполне тебя понимаю. Я ведь просто кошка: увидела мышку - схватила - съела. У меня не так много эмоций, как у вас."
            window hide
            jump ds_dv_day4_uv_dialogue
        "Это сон?":
            window show
            me "Это всё сон?"
            uv "Нет. Я реальна. Как и всё происходящее."
            me "Алис, я в обморок падаю?"
            dv "Нет, Семён. Ты просто уставился на эту девочку-кошку и смотришь уже минут пять."
            uv "Вот видишь. {i}Она{/i} тоже это видит."
            window hide
            jump ds_dv_day4_uv_dialogue
        "Кто ты такая?":
            window show
            me "Кем ты являешься?"
            show uv surprise2 dress at center
            with dspr
            uv "Я - гибрид кошки и девочки, сотворена, не рождена."
            uv "Десять лет назад меня создали, после чего выпустили в лес. С тех пор я лазила и вылавливала мышей."
            uv "Пока 7 июня 1989 года ты меня не нашёл."
            play sound ds_sfx_fys
            hfl "Что-то нехорошее тут... Она не может быть опасна?"
            play sound ds_sfx_int
            lgc "Здесь больше интересно, кто же её сотворил?"
            play sound ds_sfx_int
            enc "Виктор Франкенштейн XX века?"
            me "А... кем ты сотворена?"
            show uv upset dress at center
            with dissolve
            uv "Этого я не помню, прости."
            window hide
            jump ds_dv_day4_uv_dialogue
        "Ты чудо":
            window show
            me "Ты - настоящее чудо..."
            show uv smile dress at center
            with dspr
            uv "Нет. Это ты - чудо."
            me "Как?"
            uv "Ты спустился сюда, прошёл через эти шахты и, наконец, нашёл меня."
            uv "И - что более важно - несмотря ни на что ты продолжаешь бороться и жить."
            play sound ds_sfx_psy
            vol "Она права. Ты продолжаешь существовать несмотря на всё пережитое тобой."
            window hide
            jump ds_dv_day4_uv_dialogue
        "Я всего лишь пионер":
            window show
            me "А я всего лишь простой пионер Пёрсунов Семён."
            show uv smile dress at center
            with dspr
            uv "Нет. Ты особенный. Как и девушка, стоящая рядом с тобой."
            play sound ds_sfx_psy
            esp "Алиса... Она до сих пор в оцепенении от происходящего."
            uv "Как и все люди."
            window hide
            jump ds_dv_day4_uv_dialogue
        "Я хотел бы быть тобой":
            window show
            me "Я хотел бы быть как ты..."
            show uv surprise dress at center
            with dspr
            uv "Думаешь?"
            me "Да..."
            uv "Моя жизнь на самом деле невообразимо скучна. Каждый раз одно и то же - смотреть за людьми и ловить мышей."
            show uv smile dress at center
            with dspr
            uv "У вас жизнь намного интереснее - дружба, любовь..."
            me "У меня нет ничего этого!"
            uv "Придёт. Оно не может не прийти. У всех людей есть друзья и любимые - и у тебя тоже будут."
            window hide
            jump ds_dv_day4_uv_dialogue
        "Попрощаться":
            window show
            me "Это всё. Всё, что я хотел сказать."
    show uv normal dress at center
    with dspr
    uv "Нет. Есть ещё кое-что."
    window hide
    menu:
        "Ты самая прекрасная":
            window show
            me "Ты самая прекрасная из тех, кого я видел."
            uv "Нет. Самая прекрасная и добрая - та, кто стоит рядом с тобой. Твоя избранница."
            play sound ds_sfx_psy
            vol "Алиса..."
        "Ты самая добрая":
            window show
            me "Ты самая добрая из тех, кого я видел."
            uv "Нет. Самая прекрасная и добрая - та, кто стоит рядом с тобой. Твоя избранница."
            play sound ds_sfx_psy
            vol "Алиса..."
        "Ты пугающая":
            window show
            me "Ты пугающая..."
            uv "Возможно. Самая прекрасная и добрая - та, кто стоит рядом с тобой. Твоя избранница."
            play sound ds_sfx_psy
            vol "Алиса..."
    uv "И ещё кое-что. Та девушка - оставь её в прошлом. Оставь, а сам иди вперёд."
    me "Ты о ком?"
    uv "Ты прекрасно понимаешь, о ком я. О той женщине, которую ты любил. И из-за которой ты выгорел. Покончи с этим."
    window hide
    menu:
        "Я сделаю это":
            window show
            me "Я сделаю это."
        "Я постараюсь":
            window show
            me "Я постараюсь."
        "Я не смогу":
            window show
            me "Я не смогу."
    uv "Рядом с тобой стоит девушка, которая искренне тебя любит и готова тебе помочь. Всё у тебя с ней получится - если ты приложишь усилия."
    uv "А теперь я побежала! Меня ждут мыши!"
    stop music fadeout 5
    hide uv with dissolve2
    show dv shocked pioneer at center
    with dspr
    dv "Ч-что... это... было?"
    window hide
    menu:
        "Чудо":
            window show
            me "Это было... чудом. Не знаю, как... но после разговора с ней я чувствую облегчение на душе..."
            dv "Р-разговора?"
            me "Да... она сказала, что нам с тобой нужно держаться вместе..."
            dv "Вместе?.. Наверное..."
            play sound ds_sfx_psy
            emp "Она не знает, что на это ответить. В глубине её души твой посыл откликнулся - но она не готова показать это."
        "Что-то странное":
            window show
            me "Это было что-то очень странное..."
            dv "Ага..."
    me "Пойдём?"
    dv "Пойдём..."
    $ ds_coalface_visited = True
    $ ds_spoken_to_uv = True
    jump ds_day4_mine_crossroad

label ds_dv_day4_mine_halt:
    $ persistent.sprite_time = "night"
    scene bg int_mine_coalface 
    with fade

    if ds_halt_visited:
        window show
        "Здесь вы уже были."
        window hide

        jump ds_day4_mine_crossroad

    show dv sad pioneer at center   with dissolve
    window show
    "Вы доходите до поворота. От него в глубь породы ответвляется проход."
    play sound ds_sfx_int
    vic "Похоже, здесь что-то добывали.{w} Возможно, уголь, может, золото."
    vic "Все стены были изрублены то ли киркой, то ли отбойным молотком."
    "Здесь царит кромешный мрак, поэтому единственным вашим спасением остаётся фонарик."
    play sound ds_sfx_fys
    hfl "Сломайся он, и вы вряд ли когда-нибудь выберетесь отсюда…"
    if ds_skill_list['perception'].check(level=lvl_challenging, passive=True).result():
        play sound ds_sfx_mot
        per_eye "{result}В его свете ты замечаешь в углу какую-то красную тряпку."
        per_eye "Это пионерский галстук!"
        play sound ds_sfx_fys
        lgc "Теперь-то ясно, что Шурик здесь."
        me "Шурик! Шурик!"
        "Ответом мне стало лишь эхо."
        dv "Чего кричать? Как будто он тебя слышит..."
        me "Ну а вдруг?"
        "Алиса ничего не отвечает, лишь вздыхает."
        vic "Отсюда выходы есть лишь в туннели."
        lgc "Конечно, возможно, в этих туннелях есть ещё места, где мы не бывали…"
        window hide

    $ ds_halt_visited = True

    jump ds_day4_mine_crossroad

label ds_dv_day4_mine_exit:

    $ persistent.sprite_time = "night"
    scene bg int_mine_door 
    with fade

    window show
    play sound ds_sfx_mot
    per_eye "За очередным поворотом в свете фонаря ты можешь разглядеть деревянную дверь."
    me "Ну вот, уже что-то!"
    show dv sad pioneer at center   with dissolve
    dv "Думаешь?"
    "Алиса немного оживилась."
    me "Конечно!"
    play sound ds_sfx_int
    lgc "Хотя крайне маловероятно, что за этой дверью скрывается выход."
    lgc "Но в любом случае выбора нет."
    if ds_had_vision_mines:
        play sound ds_sfx_fys
        hfl "Что-то тут нечисто. Тебе бы подготовиться."
        window hide
        menu:
            "Принять боевую стойку":
                window show
                "Ты выставляешь руки перед собой, как боксёр, и подходишь ближе к Алисе."
                me "Будь начеку. Я чувствую, что дальше будет непросто."
                $ ds_prepared_for_fight = True
            "Забить":
                pass
        window hide
    else:
        window hide

    play sound sfx_open_door_mines

    pause(1)

    window show
    play sound ds_sfx_fys
    phi "Ты сильно дёргаешь за ручку…"
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "night"
    scene bg int_mine_room 
    with dissolve

    window show
    "Вы оказались в какой-то комнате, которая напоминала то ли котельную, то ли подсобные помещения бомбоубежища."
    "На полу повсюду валяются пустые бутылки, окурки и другой разнообразный мусор."
    play sound ds_sfx_int
    lgc "Это значит, что из этих пещер существует выход!"
    "Ты водишь фонарём по комнате и в дальнем углу видишь…"
    window hide

    scene cg d4_sh_sit 
    with dissolve

    window show
    "Шурика, скрючившегося в три погибели и трясущегося всем телом."
    $ ds_found_sh = True
    me "Шурик!"
    sh "Кто… кто это?"
    me "Шурик! Мы тебя всю ночь ищем, а ты тут сидишь! Ну-ка вставай немедленно!"
    sh "Никуда я не пойду…"
    "Начинает он тихо, но с каждым словом его тон всё больше переходит на крик."
    sh "Никуда я с вами не пойду! Вы не существуете! Вас вообще здесь нет! Это галлюцинации! Антинаучно! Да, антинаучно!"
    me "Что значит «вас нет»?! Вот мы, тебя искать пришли!"
    "Алиса всё это время стоит молча, но сейчас отпускает твою руку и делает несколько шагов по направлению к Шурику."
    me "Ты куда?"
    "Тихо спрашиваешь ты."
    "Она останавливается на мгновение, но, словно не слыша тебя, направляется дальше."
    window hide

    play sound sfx_face_slap

    pause(1)

    window show
    "Наконец, приблизившись к потерянному пионеру вплотную, Алиса залепляет ему хлёсткую пощёчину."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine_room 
    show sh scared pioneer far at cright 
    show dv rage pioneer far at cleft 
    with dissolve

    window show
    dv "Да ты! Мы чуть не убились, пока тебя искали! Лес этот чёртов ночной, бомбоубежища, шахты какие-то! Я вся в синяках из-за тебя! А ты тут что, самогона обпился и белку поймал, скотина?"
    "Шурик ошарашенно смотрит на неё."
    dv "Ну-ка вставай и пошли! Быстро!"
    sh "Нет…"
    "Затем он повышает громкость."
    sh "Нет…"
    $ ds_hfl_warning = False
    if ds_skill_list['half_light'].check(level=lvl_easy, passive=True).result():
        play sound ds_sfx_fys
        hfl "{result}Сейчас будет плохо! Берегись! И спасай Двачевскую!"
        $ ds_hfl_warning = True

    stop music fadeout 2
    window hide

    scene cg d4_sh_stay 
    with dissolve

    play music music_list["pile"] fadein 1

    menu:
        "Защитить Алису" (skill='reaction_speed', level=lvl_heroic, modifiers=[('ds_had_vision_mines', 3, "Предупреждён видением"), ('ds_prepared_for_fight', 3, 'Боевая поза'), ('ds_hfl_warning', 6, "Предупреждён Сумраком")]):
            if ds_last_skillcheck.result():
                window show
                res "{result}Ты инстинктивно бросаешься к Алисе, пятно света бешено прыгает по комнате, на секунду выхватив из темноты обезображенное гримасой безумия лицо Шурика."
                res "В руке он сжимает кусок арматуры, и, опоздай ты хоть на мгновение, обязательно размозжил бы им голову Алисы. Но ты успел."
                res "Что дальше?"
                $ ds_lp['dv'] += 2
                window hide
                menu:
                    "Оттолкнуть Шурика":
                        window show
                        "Ты отталкиваешь Шурика от Алисы. Однако, он просто так сдаваться не намерен, и напоследок делает взмах рукой..."
                        with flash_red
                    "Оттолкнуть Алису":
                        window show
                        "Ты отталкиваешь Алису от Шурика и встаёшь на её место. Но Шурик, кажется, не обращает на это внимания..."
                        with flash_red
                    "Встать перед Алисой":
                        window show
                        "Ты встаёшь прямо перед Алисой. Неприступной стеной. Но Шурик, кажется, не обращает на это внимания..."
                        with flash_red
            else:
                window show
                # ...
        "Остаться в стороне":
            window show
            # ...

    window hide

    play sound sfx_break_flashlight_alisa

    with vpunch

    pause(1)

    window show

    scene black 
    with dissolve

    stop music fadeout 5

    play sound ds_sfx_fys
    edr "Последнее, что ты чувствуешь перед тем, как упасть без сознания - боль, разрывающую твою голову, вместе с криком Алисы."
    window hide

    $ renpy.pause(1.0)

    play music ds_dream fadein 5
    window show
    arb "И снова добро пожаловать! Как хорошо, что ты всё-таки вернулся!"
    me "Где Алиса? Что с ней стало?"
    lim "Нет больше никакой Алисы. Нет больше никого. Ты потерпел окончательное поражение."
    play sound ds_sfx_psy
    vol "Ты не мог проиграть. Момент, когда ты отбиваешь руку Шурика с арматурой прямо около лба Алисы намертво отпечатался у тебя в памяти."
    me "Я... я спас Алису... ведь так?"
    arb "И пожертвовал для этого собой. А стоила ли эта жертва того?"
    play sound ds_sfx_psy
    esp "За время вашего похода по шахтам Алиса показала, что она небезразлична к чужой боли. Вспомни, как она искренне переживала за тебя в убежище."
    lim "А сейчас. Где же она сейчас?"
    esp "Придёт. И поможет тебе. Почему-то ты в этом уверен."
    lim "Ой, неужели ты можешь быть кому-то нужен?"
    if ds_spoken_to_uv:
        vol "Вспомни, что тебе сказала та кошкодевочка."
        me "Да... я нужен ей, как и она - мне..."
    else:
        me "Вероятно... по крайней мере я надеюсь..."
    play sound ds_sfx_mot
    per_hea "Cквозь пучину тьмы прорывается... плач?"
    per_toc "И тепло... будто тебя кто-то обнимает..."
    dv "ТЫ УЖЕ ВСТАНЕШЬ НАКОНЕЦ?!"
    "Голос Алисы звучит, хоть и криком, но без агрессии. Напротив - каким-то заплаканным."
    lim "Кажется, тебя что-то - а вернее, кто-то - не отпускает. Ты продолжаешь цепляться за жизнь благодаря ей."
    window hide
    scene bg int_mine_room
    show dv cry_smile pioneer close at center
    show unblink
    stop music fadeout 5

    window show
    "Открыв глаза, ты видишь Алису в слезах, прижавшуюся к тебе."
    "Тебе понадобилось какое-то время, чтобы прийти в себя."
    me "Что это было, придурок?!"
    play sound ds_sfx_psy
    aut "А вот это старая добрая Дваче - агрессивная и ершистая."
    play sound ds_sfx_psy
    emp "Но чувствуются и ноты заботы."
    "Ты ощупал голову. Она замотана бинтом. На руках остаются следы крови."
    window hide
    menu ds_dv_day4_fight_aftermath:
        set ds_menuset
        "Спросить, что случилось":
            window show
            me "Что... случилось?"
            dv "Этот ублюдок... набросился на меня с арматурой... я уже думала, что мне конец..."
            play sound ds_sfx_psy
            emp "Ей очень тяжело говорить - она всё ещё напугана из-за пережитого."
            dv "Но тут ты... подставился под него, прикрыв меня... и получил по голове."
            dv "Потом... он убежал... а ты лежал тут без сознания... а ещё фонарь разбился..."
            play sound ds_sfx_fys
            hfl "Плохо дело..."
            dv "Но у меня была с собой зажигалка..."
            play sound ds_sfx_mot
            per_eye "Ты только сейчас обращаешь внимание на то, что комната освещена светом огня, не электрическим."
            play sound ds_sfx_mot
            res "Откуда?"
            me "Откуда... у тебя зажигалка?"
            dv "Памятник..."
            "Она произносит это с беззлобной улыбкой."
            dv "В общем... мне пришлось сбегать в убежище за аптечкой... хотя было очень страшно..."
            play sound ds_sfx_psy
            esp "Cпасибо. Если бы не она - ты бы сдох тут."
            window hide
            jump ds_dv_day4_fight_aftermath
        "Cпросить про неё":
            window show
            me "Ты в порядке?"
            "Лишь тихий всхлип, и в ту же секунду ты чувствуешь, как она крепко прижимается к тебе, обхватив руками."
            play sound ds_sfx_psy
            vol "Нужно, чтобы она успокоилась - иначе вам не выбраться отсюда."
            play sound ds_sfx_psy
            aut "Интересно, а плачущая Алиса – это смешно?{w} Наверное, при других обстоятельствах…"
            play sound ds_sfx_psy
            emp "...но уж точно не сейчас."
            window hide
            menu:
                "Успокоить Алису" (skill='empathy', level=lvl_medium):
                    if ds_last_skillcheck.result():
                        window show
                        me "Ладно-ладно, всё хорошо…"
                        "Ты аккуратно гладишь её по голове."
                        $ ds_lp['dv'] += 1
                        dv "Страшно…"
                        me "Это нормально, мне тоже…"
                    else:
                        window show
                        me "Так, успокаивайся и поднимайся!"
                        dv "Ага, сейчас..."
                        $ ds_lp['dv'] -= 1
                        "Ты слышишь новый всхлип."
                "Посмеяться":
                    window show
                    me "Что, порастеряла весь свой гонор?"
                    "Она лишь больше поникла. Ты слышишь новые тихие всхлипы."
                    $ ds_lp['dv'] -= 2
                "Молча ждать":
                    window show
                    "Ты умолкаешь. Тишину прерывают лишь периодические всхлипы Алисы."
            play sound ds_sfx_psy
            sug "Такое резкое, неожиданное преображение Алисы..."
            sug "Хотя в такой ситуации испугается любой.{w} Тем более она девочка…"
            th "Но почему тогда не боюсь я?{w} Нет, не так – почему я ещё сохраняю возможность рассуждать здраво?"
            th "Может быть, потому что мне приходится беспокоиться не только о себе?.."
            vol "Ага, а то, что перед ней промелькнула смерть, потом на её глазах ради неё чуть не пожертвовали жизнью и, наконец, ей потом пришлось беспокоиться о тебе, чтобы ты тут кони не двинул - это мелочи жизни?"
            window hide
            jump ds_dv_day4_fight_aftermath
        "Подняться":
            window show
    me "Ладно, в любом случае надо как-то выбираться."
    
    hide dv  with dissolve
    $ ds_visited_mines = True
    "Ты быстро окидываешь помещение взглядом в поисках чего-то, что можно было использовать как факел."
    play sound ds_sfx_mot
    inf "На полу нашлись какие-то старые тряпки, палка, а в одной из бутылок – немного жидкости, по запаху напоминающей технический спирт."
    window hide

    play sound sfx_ignite_torch

    pause(1)

    play sound_loop sfx_torch fadein 1

    window show
    "Через минуту ты уже держишь в руках худо-бедно горящее нечто."
    show dv normal pioneer at center   with dissolve
    me "Не знаю, сколько он продержится, поэтому придётся идти быстро."
    dv "А куда?"
    play sound ds_sfx_mot
    com "Алиса, похоже, немного пришла в себя."
    me "Пойдём назад. Хотя бы до бомбоубежища. Там по крайней мере есть свет."
    "Она молча кивает и берёт тебя за руку."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_mine 
    with dissolve

    play ambience ambience_catacombs fadein 3
    play music ds_deliverance fadein 3

    window show
    "Факел горит плохо, приходится его поджигать заново каждую минуту, а уж про долговечность тряпки, составляющей его основу, и говорить не приходится."
    play sound ds_sfx_fys
    hfl "На зажигалку рассчитывать не приходится - а как только выгорит тряпка, вы останетесь в полной темноте."
    "Однако до дыры, ведущей наверх, в катакомбы, вы добираетесь довольно быстро."
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_hole 
    with dissolve

    window show
    "Выбрались с трудом, вам приходилось карабкаться практически на ощупь."
    show dv normal pioneer at center   with dissolve
    dv "И куда дальше?"
    "Отдышавшись, спрашивает Алиса."
    me "В смысле? Ну, в ту комнату с кроватями, шкафами."
    show dv surprise pioneer at center   with dspr
    dv "А в какую она сторону?"
    if ds_set_path_mark:
        me "Так вот же я оставил указание."
        "Чёрная стрелка по-прежнему красуется на стене."
        if not ds_visited_lab and ds_skill_list['inland_empire'].check(level=lvl_easy, passive=True).result():
            play sound ds_sfx_psy
            ine "{result}Разве тебе неинтересно, что там, в другой стороне?"
            window hide
            menu:
                "Пойти по стрелке":
                    window show
                "Пойти в другом направлении":
                    window show
                    me "Давай сходим в другую сторону, вдруг там выход есть."
                    dv "Идём уже куда-нибудь..."
                    jump ds_dv_day4_lab
        me "Идём!"
        jump ds_dv_day4_return
    play sound ds_sfx_int
    lgc "Позвольте, а как она сбегала до убежища, чтобы взять лекарств?"
    play sound ds_sfx_psy
    vol "На автомате. Судя по её поведению, она не вполне осознанно делала что-либо в тот момент."
    vol "Кстати, ты ведь тоже не имеешь ни малейшего представления, куда идти."
    play sound ds_sfx_int
    vic "Дыра со всех сторон кажется одинаковой, как и стены, пол и потолок, а значит, нет никакой возможности точно установить направление."
    me "Ну…"
    show dv sad pioneer at center   with dspr
    dv "Не знаешь?"
    "Грустно спрашивает Алиса и садится на землю."
    play sound ds_sfx_mot
    inf "Ты можешь выбрать ОДНО направление - факела на кругосветное путешествие по туннелю не хватит."
    window hide
    menu ds_dv_day4_way_out:
        "Пойти назад":
            window show
            me "Пойдём вот туда."
            "Ты указываешь за собой."
            dv "Ну, пойдём... Мне уже вообще без разницы..."
            jump ds_dv_day4_return
        "Пойти вперёд":
            window show
            me "Идём. Вот туда!"
            "Ты указываешь впереди себя."
            dv "Ну, пойдём... Мне уже вообще без разницы..."
            jump ds_dv_day4_lab
        "Прислушаться" (skill='shivers', level=lvl_challenging):
            if ds_last_skillcheck.result():
                 $ volume(0.2, "sound")

                play sound sfx_open_metal_door
                play sound2 ds_sfx_fys
                shi "{result}Вдалеке послышался какой-то шум."

                $ volume(1.0, "sound")

                play music music_list["sunny_day"] fadein 2
                shi "Лязг дверных засовов."
                if ds_skill_list['half_light'].check(level=lvl_up_medium, passive=True).result():
                    window show
                    hfl "{result}Ты рывком поднимаешь Алису с земли и трясущимися руками зажигаешь факел."
                    me "Вставай!"
                    window hide

                    $ persistent.sprite_time = "night"
                    scene bg int_catacombs_hole 
                    show dv scared pioneer at center 
                    with dissolve

                    play sound sfx_ignite_torch

                    pause(1)

                    play sound_loop sfx_torch fadein 1
                    dv "Что?.."
                    "Она напугана."
                    me "Не знаю, но там кто-то есть. Придётся бежать!"
                    hfl "По правде говоря, вряд ли это хорошая идея."
                    hfl "Вдруг там безумный Шурик?{w} И ведь это ещё самое меньшее из всех возможных зол!"
                    play sound ds_sfx_psy
                    vol "Однако выбора не остаётся."
                    play sound ds_sfx_fys
                    edr "Но и сил бежать у тебя - а у Алисы и подавно - не остаётся."
                    window hide
                else:
                    window show
                    me "Идём туда!"
                    dv "Идём..."
                jump ds_dv_day4_return
            else:
                play sound ds_sfx_fys
                shi "{result}Бесполезно. Ты не понимаешь, в какую сторону тебе идти. Ни звука, чтобы подсказать тебе."
                window hide
                jump ds_dv_day4_way_out
        "Сказать, что не знаешь":
            window show
            me "Нет."

    stop sound_loop fadeout 1

    scene black 
    with dissolve

    window show
    "Ты гасишь факел, чтобы не сжигать его попусту, и пристраиваешься рядом с ней."
    dv "Значит, мы тут умрём?"
    "Она кладёт голову мне на плечо."
    "Голос Алисы звучал ровно, можно даже сказать, спокойно."
    play sound ds_sfx_psy
    emp "Но чувствуется, как её тело дрожит – то ли от холода, то ли от страха, то ли от всего вместе."
    window hide
    menu:
        "Начать паниковать":
            window show
            me "Да, мы умрём! Что делать, что делать?! Я, как и ты, в ужасе!"
            play sound ds_sfx_psy
            aut "В другой ситуации Двачевская бы залепила тебе пощёчину за это, не меньше. Но сейчас она, кажется, и сама верит в это."
            $ ds_lp['dv'] -= 1
            "Она съёживается ещё больше."
        "Успокоить":
            window show
            me "Да ну, глупости! Неприятная ситуация, конечно, но чтобы прямо «умрём»… Утром за нами придут. Ольга Дмитриевна с милицией. Ну и…"
            hfl "Хотелось бы в это верить."
            dv "Хорошо…"
            me "Угу…"
    window hide

    with fade

    window show
    "Неизвестно, сколько вы просидели так…"
    play sound ds_sfx_psy
    vol "Ты не решаешься идти «вперёд» или «назад», боишься выбрать, ведь  оказаться в полной темноте ещё хуже, чем ждать спасения здесь."
    play sound ds_sfx_mot
    inf "Так у вас хотя бы будет немного света на крайний случай…"

    window hide
    $ renpy.pause(1.0)
    window show

    "Алиса уже давно заснула. Ты тоже засыпаешь."
    scene black with dissolve
    show blink
    window hide

    jump ds_end_lost_in_shaft

label ds_dv_day4_return:
    $ persistent.sprite_time = "night"
    scene bg int_catacombs_entrance 
    with dissolve

    window show

    stop ambience fadeout 2

    "Наконец впереди показывается открытая дверь, и ты прыжком заскакиваешь в бомбоубежище"
    if ds_found_sh:
        play sound ds_sfx_fys
        hfl "Ты готов отбиваться от возможных противников - безумного Шурика, скажем."
        window hide

        stop sound_loop fadeout 1

        $ persistent.sprite_time = "sunset"
        scene bg int_catacombs_living 
        with dissolve

        window show
        play sound ds_sfx_mot
        per_eye "Однако комната пуста…"
        hfl "Ты бешено шаришь по ней глазами, стараясь в углах разглядеть прячущихся врагов, Шурика, нечистую силу, но всё такое же, как и в первый раз, когда вы здесь были."
        per_eye "Разве что дверь, вторая дверь…{w} Она открыта!"
        show dv scared pioneer at center   with dissolve
        me "Значит, здесь кто-то проходил!"
        dv "Кто?"
        me "Не знаю, Шурик, может быть…"
        dv "Но как он смог её открыть?"
        me "Да какая сейчас разница! Пойдём!"
        window hide
    else:
        play sound ds_sfx_mot
        per_eye "Вторая дверь... она открыта!"
        show dv scared pioneer at center   with dissolve
        me "Значит, здесь кто-то проходил!"
        dv "Кто?"
        me "Не знаю, Шурик, может быть…"
        dv "Но как он смог её открыть?"
        me "Да какая сейчас разница! Пойдём!"
        window hide

    $ persistent.sprite_time = "night"
    scene bg int_catacombs_entrance 
    with dissolve

    window show
    "За дверью оказывается ещё один коридор, медленно поднимающийся вверх."
    play sound ds_sfx_int
    lgc "Значит, вы приближаетесь к поверхности."
    scene bg int_mine_exit_night_torch
    with dissolve

    "И действительно, через пару сотен метров ты натыкаешься на лестницу, упирающуюся под потолком в небольшой люк."

    play sound sfx_open_metal_hatch

    "Открыть его не составило особого труда."
    show dv scared pioneer at center   with dissolve
    dv "А что там?"
    me "Наверняка лучше, чем здесь!"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_square_night
    with dissolve

    window show
    "Ты вылезаешь и оказываешься... прямиком на площади!"

    stop music fadeout 3

    "Ты помог Алисе выбраться, и вы буквально выскочили наружу."
    window hide
    jump ds_dv_day4_square

label ds_dv_day4_old_camp:
    play ambience ambience_old_camp_outside fadein 3

    window show
    if ds_visited_old_camp:
        "Выход из лифта действительно оказывается в уже знакомом тебе старом лагере."
    else:
        "Выход из лифта находится в каком-то старом здании, по виду напоминавшем то ли детский сад, то ли сельскую школу."
    show dv normal pioneer at center   with dissolve
    dv "Это, наверное, старый лагерь…"
    "Алиса садится на диван и вытирает тыльной стороной ладони пот с лица."
    me "Наверное… Значит, мы его всё-таки нашли."
    "Ты невольно улыбаешься."
    show dv angry pioneer at center   with dspr
    dv "Не вижу ничего смешного!"
    "Она нахмурилась и недовольно надулась."
    play sound ds_sfx_psy
    aut "Короче говоря, стала такой же, как обычно."
    show dv scared pioneer at center   with dspr
    dv "Ты куда?"
    "Уже менее уверенно спросила она, когда ты развернулся и направился в сторону выхода."
    me "Назад."
    show dv shocked pioneer at center   with dspr
    dv "Эй!"
    "Алиса тут же подскочила и зашагала рядом."
    scene bg int_old_building_night
    with dissolve
    "Вы выходите к видавшей виды лестнице..."
    scene bg ext_old_building_night
    "...и выходите из здания."
    "Вы удивительно быстро находите тропу, по которой шли, даже те две ямы, в которые провалились."
    play sound ds_sfx_int
    vic "И ведь вам оставалось до старого лагеря пройти всего каких-то пару сотен метров!"

    stop ambience fadeout 2

    window hide
    jump ds_dv_day4_square

label ds_dv_day4_square:
    $ persistent.sprite_time = "night"
    scene bg ext_square_night
    with dissolve
    play ambience ambience_camp_center_night fadein 3

    show dv shy pioneer at center   with dissolve
    window show
    "На площади ты останавливаешься и поворачиваешься к Алисе."
    me "Ладно…"
    dv "Ладно…"
    "Она выглядит неуверенно, даже немного смущённо."
    me "Тогда…"
    dv "Угу…"
    play sound ds_sfx_psy
    aut "Где-то в глубине души тебе хочется наорать на неё, обругать, может, обматерить даже.{w} С другой стороны – провести душеспасительную беседу."
    window hide
    menu:
        "Наорать на Алису":
            window show
            me "Что, тут уже не страшно?"
            dv "Да мне и тогда страшно не было!"
            me "Ну-ну!"
            dv "Да!"
            me "Ради бога…"
            aut "Да если бы не ты, она бы до сих пор там и сидела, в шахте этой проклятой!"
            $ ds_lp['dv'] -= 1
        "Промолчать"
            "Но в итоге ты просто промолчал, развернулся и медленно направился в сторону домика вожатой."

    hide dv  with dissolve

    if not ds_found_sh:
        jump ds_day4_no_sh

    play sound_loop sfx_shurik_snore fadein 1
    play sound ds_sfx_mot
    per_hea "Однако что-то упорно нарушает ночную тишину."
    per_hea "Прислушавшись, ты понимаешь, что это храп..."
    per_hea "Шурика, который мирно спит на скамейке!"
    window hide
    menu:
        "Позвать Алису":
            window show
            me "Эй!"
            "Кричишь ты Алисе, которая ещё не успела далеко уйти."
            me "Ну-ка вставай!"

            stop sound_loop fadeout 1

            show sh upset pioneer at cright 
            show dv angry pioneer at cleft 
            with dissolve
            "Шурик медленно пришёл в себя и непонимающе посмотрел на вас."
            sh "А что, уже утро?"
            me "Утро? Да, утро…"
            $ ds_hit_sh = False
            if ds_skill_list['half_light'].check(level=lvl_trivial, passive=True).result():
                hfl "{result}Твоя рука на автомате поднимается и быстро влетает Шурику под дых. Только потом ты осознаёшь, что сделал."
                show sh scared pioneer at cright   with dspr
                "Он закашлялся, пытаясь поймать дыхание, и скрючился на скамейке."
                $ ds_hit_sh = True
            me "Что ты там учудил?!"
            sh "Ты… ты о чём?"
            "Шурик со страхом в глазах смотрит на тебя."
            me "В шахте!"
            sh "В какой шахте?"
            "Он недоуменно вертит головой."
            sh "И почему я тут?"
            sh "И почему вы тут?"
            show dv rage pioneer at cleft   with dspr
            dv "Ты что, прикалываешься?"
            "В разговор вмешивается Алиса."
            dv "Ты меня там чуть не убил! А теперь будешь притворяться, что ничего не было?"
            sh "Чего не было?"
            me "Ты правда не помнишь?"
            sh "Нет…"
            me "А что последнее помнишь?"
            show sh upset pioneer at cright   with dspr
            "Шурик напрягся."
            sh "Ну, я утром пошёл в старый лагерь. Там можно найти детали для робота и…"
            me "И?"
            sh "И всё… Дальше не помню. Проснулся здесь."
            "Ты тяжело вздыхаешь и отворачиваешься."
            play sound ds_sfx_int
            rhe "Большего ты тут не добьёшься."
            window hide
            menu:
                "Уйти":
                    window show
                    me "Ладно, спокойной ночи…"
                    show dv shocked pioneer at cleft   with dspr
                    dv "Эй, ты куда?"
                    hide dv 
                    hide sh 
                    with dissolve
                    "Ты не обращаешь внимания на Алису и быстро идёшь к домику Ольги Дмитриевны.{w} Она же о чём-то ругается с Шуриком."
                "Продолжать":
                    window show
                    me "Нет, ты вообще в здравом уме? Ты, значит, чуть не убил Алису, чуть не убил меня, а теперь сидишь, придуриваешься?!"
                    if ds_hit_sh:
                        me "Ты ещё хочешь получить?!"
                    dv "Да! Не надо тут нас за идиотов держать! Завтра утром всё про тебя расскажу!"
                    dv "Хотя нет! Лучше сейчас тебя побью! Выбью из тебя желание размахивать арматурой! Держи его, Семён!"
                    show sh scared pioneer at cright
                    with dspr
                    "Глаза Шурика наполнились страхом."
                    window hide
                    menu:
                        "Схватить Шурика" (skill='savoir_faire', level=lvl_challenging):
                            if ds_last_skillcheck.result():
                                play sound ds_sfx_mot
                                svf "{result}Заходи сзади и хватай его!"
                                "Ты так и делаешь. С другой стороны приближается Алиса и бьёт его по голове."
                                $ ds_lp['dv'] += 1
                                dv "Это тебе за меня! За то, что чуть меня не угробил, хотя я попёрлась тебя искать!"
                                "Затем Алиса наносит ещё удар."
                                dv "А это тебе за Семёна. Который подставился под тебя, чтобы меня ты не убил, выродок!"
                                "И ешё удар - на этот раз в живот."
                                dv "А это - для закрепления! Отпускай его."
                                "Ты выпускаешь Шурика, и он падает на пол."
                                me "Ладно, я пойду... Спокойной ночи!"
                                "Алиса ничего тебе не отвечает."
                                "Ты идёшь к домику Ольги Дмитриевны."
                            else:
                                play sound ds_sfx_mot
                                svf "{result}Прежде чем ты успеваешь схватить Шурика - он выскальзывает из твоих рук и убегает."
                                hide sh with dissolve
                                dv "КУДА СОБРАЛСЯ?!"
                                hide dv with dissolve
                                "Алиса бросается за ним вдогонку. Ты же уходишь в сторону домика Ольги Дмитриевны."
                        "Стоять на месте":
                            window show
                            "Ты стоишь и смотришь за дальнейшим развитием событий."
                            hide sh with dissolve
                            "Шурик срывается с места и убегает."
                            dv "КУДА СОБРАЛСЯ?!"
                            hide dv with dissolve
                            "Алиса бросается за ним вдогонку. Ты же уходишь в сторону домика Ольги Дмитриевны."
        "Проигнорировать":
            window show
            th "Пусть спит"
            "И ты направляешься к домику Ольги Дмитриевны."

    stop ambience fadeout 2

    $ persistent.sprite_time = "night"
    scene bg ext_house_of_mt_night_without_light 
    with dissolve

    play sound ds_sfx_psy
    ine "Тебе нужно кое-кого подождать."
    th "Кого?"
    ine "Увидишь. Расположись на шезлонге."
    window hide
    menu:
        "Лечь на шезлонг":
            window show
        "Зайти в домик":
            window show
            th "Да ну нафиг! Спать хочу!"
            jump ds_dv_day4_mt_house

    window hide

    scene stars 
    with dissolve

    play music music_list["waltz_of_doubts"] fadein 3

    window show
    "Ты сидишь в шезлонге и смотришь на звёзды."
    play sound ds_sfx_mot
    per_eye "Сегодня ночью они кажутся ярче, чем обычно."
    per_eye "Может быть, потому что ещё недавно твоим единственным источников света был фонарь, а потом – факел."
    play sound ds_sfx_int
    con "Звёзды – ярче фонаря, тем более – факела.{w} Многие звёзды, наверное, даже ярче Солнца, только они далеко…"
    per_hea "В ночи шаги Алисы слышны за много метров."
    me "И зачем пришла?"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_house_of_mt_night_without_light 
    with dissolve

    window show
    "Ты спрашиваешь, не оборачиваясь."
    show dv shy pioneer at center   with dissolve
    dv "Да я…"
    me "Что Шурик сказал?"
    dv "Сказал, что ничего не помнит, что «антинаучно», ещё какой-то бред нёс."
    me "Я думаю, он правда не помнит – шок, стрессовая ситуация."
    play sound ds_sfx_psy
    vol "Кто бы говорил?{w} Ведь ты сам ещё недавно был в такой же «ситуации»."
    vol "Впрочем, ты и сейчас в ней.{w} И что же, у тебя тоже амнезия?"
    me "Так зачем пришла?"
    play sound ds_sfx_psy
    ine "Ты и сам знаешь ответ."
    show dv shy pioneer close at center    with dissolve
    dv "Ну я…"
    "Алиса садится рядом."
    dv "Поблагодарить хотела… Ведь там это... Ты это... Ну…"
    window hide
    menu:
        "Не за что":
            window show
            me "Не за что."
            "Спокойно сказал я и откинулся назад."
            dv "Ну ладно тогда…"
        "Покичиться":
            window show
            me "Вот если бы не я..."
            dv "Заткнись, а?"
    show dv shy pioneer at center   with dissolve
    "Она встаёт и собирается уходить."
    window hide
    menu:
        "Успокоить Алису":
            window show
            me "Если ты думаешь, что я злюсь, то не стоит. Всё в порядке."
            show dv angry pioneer at center   with dspr
            dv "Я и не думала!"
            "Заводится Алиса."
            me "Ну тогда хорошо."
        "Промолчать":
            window show
    show dv normal pioneer at center   with dspr
    dv "Ладно…"
    me "Угу…"
    dv "Тогда…"
    window hide
    menu:
        "Отправить Алису беззлобно":
            window show
            me "Да иди уже!"
            "Беззлобно говоришь ты и машешь рукой."
        "Отправить Алису резко":
            window show
            me "Иди спать уже!"
            $ ds_lp['dv'] -= 1
        "Спросить":
            window show
            me "Ты идёшь?"
    show dv angry pioneer at center   with dspr
            
    dv "Пойду, когда посчитаю нужным!"
    me "То есть сейчас ты нужным это не считаешь?"
    dv "Считаю!"
    me "Ну? И что тебя останавливает?"
    if ds_lp['dv'] >= 35:
        show dv angry pioneer at center
        with dspr
        "Вместо ответа Алиса приближается к тебе... {w}берёт тебя за плечи, прижимая к себе..."
        scene cg ds_day4_dv_kiss
        with dissolve
        "...и целует тебя!"
        play sound ds_sfx_psy
        emp "В её поцелуе чувствуется... тепло. Тепло любви."
        play sound ds_sfx_psy
        ine "Такое же чувство, какое у тебя было давно... ты вновь его испытываешь, спустя столько лет..."
        th "Что... это значит?"
        play sound ds_sfx_psy
        sug "Это значит, что тебе дали шанс. Не упусти его."
        window hide
        menu:
            "Отдаться Алисе":
                window show
                "Ты прижимаешь Алису к себе, заключая в объятия. Она поддаётся тебе."
                play sound ds_sfx_psy
                emp "Она готова тебе довериться. Пока что не полностью - но {i}попробовать{/i} с тобой она готова."
                "Ты стараешься отдать ей всю теплоту и нежность, что у тебя есть - от всего твоего истерзанного сердца."
                window hide
                $ renpy.pause(1.0)
                scene bg ext_house_of_mt_night_without_light
                show dv angry pioneer at center
                with dissolve
                window show
                "Через пару минут Алиса отстраняется от тебя."
                dv "Теперь до тебя дошло, придурок?"
                hide dv with dspr
                "И она убегает прежде, чем ты хотя бы осознаешь сказанное ею."
                play sound ds_sfx_int
                rhe "Дошло. И ежу понятно, что она в тебя {i}влюбилась{/i}."
                "С осознанием этой мысли ты направляешься к домику."
                $ ds_route = 'dv'
            "Оттолкнуть Алису":
                window show
                "Ты мягко отстраняешь от себя Алису."
                me "Не сейчас... я не готов."
                scene bg ext_house_of_mt_night_without_light
                show dv rage pioneer at center
                with dissolve

                dv "Дебил!"
                hide dv  with dissolve
                "Алиса топает ногой и быстро направляется прочь от домика вожатой."
                "Ты тяжело вздыхаешь и встаёшь."
                play sound ds_sfx_fys
                edr "Голова от усталости кружится ужасно."
    else:
        show dv rage pioneer at center
        with dissolve

        dv "Дебил!"
        hide dv  with dissolve
        "Алиса топает ногой и быстро направляется прочь от домика вожатой."
        "Ты тяжело вздыхаешь и встаёшь."
        play sound ds_sfx_fys
        edr "Голова от усталости кружится ужасно."
    jump ds_dv_day4_mt_house

label ds_dv_day4_mt_house:
    stop ambience fadeout 2

    th "Хорошо хоть Ольга Дмитриевна уже спит, значит, не придётся перед ней объясняться…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_house_of_mt_night2 
    with dissolve

    window show
    "Однако всё оказывается не так просто."
    show mt angry pioneer at center   with dissolve
    "Вожатая стоит посреди комнаты и явно готовится к долгой беседе."
    "Или скорее – к разбору полётов."
    mt "Изволишь объясниться?"
    play sound ds_sfx_psy
    aut "Вот тут вообще непонятно было сейчас. Сама же отправила Шурика искать."
    window hide
    menu:
        "Сказать про поиски":
            window show
            me "А что такого?{w} Вы же не были против, когда мы собрались идти на поиски Шурика?"
            mt "И как, нашли?"
            play sound ds_sfx_int
            rhe "Кажется, что сейчас её куда больше интересует то, почему ты припозднился, а не судьба потерявшегося пионера."
            me "Да.{w} Кстати, а почему вы тут в темноте стоите?"
            show mt surprise pioneer at center   with dspr
            mt "Что?"
            me "В темноте, говорю, почему?"
            show mt normal pioneer at center   with dspr
            mt "Потому что пора спать."
            edr "Ты с ней согласен как никогда, хоть и немного удивился такой резкой смене настроения."
        "Демонстративно пойти спать":
            window show
            me "Мне не в чем объясняться, я иду спать. Вашего Шурика я нашёл."
            "Ты начинаешь раскладывать постель."
            mt "Ладно. Ложись спать уже."
            edr "Ты с ней согласен как никогда, хоть и немного удивился такой резкой смене настроения."
        "Извиниться":
            window show
            me "Извините."
            mt "Ладно. Ложись спать уже."
            edr "Ты с ней согласен как никогда, хоть и немного удивился такой резкой смене настроения."
    hide mt  with dissolve
    window hide

    with fade

    window show
    "Кое-как доковыляв до своей постели, ты падаешь не раздеваясь."
    if ds_route == 'dv':
        th "Всё же Алиса…{w} Алиса…"
        "Ты не знаешь, что о ней думать."
        play sound ds_sfx_int
        lgc "И не потому что она вела себя как-то странно.{w} Нет, как раз наоборот – всё в её поведении было весьма логично и объяснимо."
        lgc "Даже то, что она пришла поблагодарить."
        play sound ds_sfx_psy
        sug "В твоих мыслях Алиса занимает куда больше места, чем всё то, что случилось за ночь."
        sug "Тот её неожиданный поцелуй... неужели она и правда что-то кроме агрессии к тебе испытывает?"
        "С этими мыслями ты засыпаешь."
    window hide

    stop music fadeout 5

    scene black 
    with fade3

    pause(3)

    if ds_route == 'dv':
        jump ds_dv_day4_dream
    else:
        jump ds_day4_dream

label ds_day4_no_sh:
    stop ambience fadeout 2

    th "Хорошо хоть Ольга Дмитриевна уже спит, значит, не придётся перед ней объясняться…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg int_house_of_mt_night2 
    with dissolve

    window show
    "Однако всё оказывается не так просто."
    show mt angry pioneer at center   with dissolve
    "Вожатая стоит посреди комнаты и явно готовится к долгой беседе."
    "Или скорее – к разбору полётов."
    mt "Изволишь объясниться?"
    play sound ds_sfx_psy
    vol "Незадача... Шурика-то вы так и не нашли..."
    me "Ну... Шурик, кажется, потерялся безвозвратно... мы оказались в шахтах, долго там блуждали - безуспешно."
    show mt shocked pioneer at center
    with dspr
    "Ольга Дмитриевна хватается за голову руками."
    mt "Ну всё... это конец... Лагерь закроют, всех отстранят от работы!"
    mt "Ладно, спасибо... завтра будем в милицию звонить..."
    mt "Ложись спать..."
    hide mt with dissolve
    "Сама же Ольга Дмитриевна выходит куда-то. Ты, следуя её указанию, ложишься в кровать."
    scene black
    with dissolve2
    jump ds_end_sh_lost
