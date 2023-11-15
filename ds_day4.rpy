# DISCO SOVENOK
# ОБЩИЙ РУТ. ДЕНЬ 4
# +КОРНИ РУТОВ АЛИСЫ, ЛЕНЫ, СЛАВИ, МИКУ

init:
    $ ds_caught_in_lib = False
    $ ds_dv_breakfast_absent = False

label ds_day4_morning:

    $ backdrop = "days"

    $ new_chapter(4, u"Disco Sovenok. День 4.")
    $ save_name('Disco Sovenok. Общий рут. День 4.')

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

    if skillcheck('perception', lvl_easy, passive=True):

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
                    "{check=interfacing:18}Начать собирать порошок":
                        if skillcheck('interfacing', lvl_unimaginable):
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
                        $ ds_skill_points['interfacing'] += 1
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

    jump ds_day4_breakfast

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
        "{check=physical_instrument:16}Подняться":
            if skillcheck('physical_instrument', lvl_godly):
                window show
                phi "{result}И раз! Ты поднимаешься..."
                phi "И два! Давай!"
                "У тебя получается подняться, и ты уже собираешься уходить..."
                $ ds_skill_points['physical_instrument'] += 1
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
        "{check=savoir_faire:14}Ползти":
            if skillcheck('savoir_faire', lvl_legendary):
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
            if skillcheck('encyclopedia', lvl_challenging, passive=True):
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
            if skillcheck('logic', lvl_trivial, passive=True):
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
            if skillcheck('physical_instrument', lvl_legendary, passive=True):
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
                    if skillcheck('authority', lvl_medium, passive=True):
                        play sound ds_sfx_psy
                        aut "{result}Держись ровно, спокойно. Просто ответь."
                    window hide
                    menu:
                        "Спокойно ответить" if ds_last_skillcheck.result:
                            window show
                            me "Ну, мы сидели в библиотеке, как вы и велели, ну и уснули..."
                            mt "Вообще замечательно: вы уснули, а я потом бегай отвечай за вас!"
                            show mt normal pioneer at left
                            with dspr
                            mt "Хотя, с другой стороны, и я должна была проверить библиотеку в первую очередь, сама ведь вас послала..."
                            show mt angry pioneer at left
                            with dspr
                            mt "В общем, дуйте умываться! У меня и без вас забот полон рот!"
                        "{check=drama:11}Театрально покаяться":
                            if skillcheck('drama', lvl_up_medium):
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
                            $ ds_skill_points['drama'] += 1
                        "Извиниться":
                            window show
                            me "Извините..."
                            mt "В общем, всё, идите умываться, а потом собираемся около столовой!"
                        "{check=savoir_faire:16}Улизнуть":
                            if skillcheck('savoir_faire', lvl_godly):
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
                                $ ds_skill_points['savoir_faire'] += 1
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
                                $ ds_skill_points['savoir_faire'] += 1
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
    if skillcheck('rhetoric', lvl_easy, passive=True):
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
    if skillcheck('authority', lvl_medium, passive=True):
        play sound ds_sfx_psy
        aut "{result}Держись ровно, спокойно. Просто ответь."
    window hide
    menu:
        "Спокойно ответить" if ds_last_skillcheck.result:
            window show
            me "Ну, мы сидели в библиотеке, как вы и велели, ну и уснули..."
            mt "Вообще замечательно: вы уснули, а я потом бегай отвечай за вас!"
            show mt normal pioneer at left
            with dspr
            mt "Хотя, с другой стороны, и я должна была проверить библиотеку в первую очередь, сама ведь вас послала..."
            show mt angry pioneer at left
            with dspr
            mt "В общем, дуйте умываться! У меня и без вас забот полон рот!"
        "{check=drama:11}Театрально покаяться":
            if skillcheck('drama', lvl_up_medium):
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
            $ ds_skill_points['drama'] += 1
        "Извиниться":
            window show
            me "Извините..."
            mt "В общем, всё, идите умываться, а потом собираемся около столовой!"
        "{check=savoir_faire:16}Улизнуть":
            if skillcheck('savoir_faire', lvl_godly):
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
                $ ds_skill_points['savoir_faire'] += 1
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
                $ ds_skill_points['savoir_faire'] += 1
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
        "{check=authority:18}Отказаться":
            if skillcheck('authority', lvl_unimaginable):
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
                $ ds_skill_points['authority'] += 1
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
                $ ds_skill_points['authority'] += 1
                me "Ясно, ну ладно..."
        "{check=drama:12}Притвориться больным":
            if skillcheck('drama', lvl_challenging):
                window show
                play sound ds_sfx_int
                dra "{result}Вы хватаетесь за голову, старательно изображая боль в ней."
                me "Извините... никак не смогу... голова болит почему-то..."
                show mt surprise pioneer at center
                with dspr
                mt "Наверное, это из-за вчерашней дискотеки... ладно, полежи ещё, отдохни..."
                hide mt with dissolve
                $ ds_skill_points['drama'] += 1
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
                $ ds_skill_points['drama'] += 1
                me "Ладно-ладно..."
        "Сбежать":
            window show
            "Ты пытаешься сбежать, но запутываешься в одеяле."
            play sound sfx_bodyfall_1
            with vpunch
            $ ds_damage_health()
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
                "{check=drama:11}Соврать":
                    if skillcheck('drama', lvl_challenging):
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
        "{check=endurance:11}Cделать честно":
            if skillcheck('endurance', lvl_up_medium):
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
                $ ds_damage_morale()
            $ ds_skill_points['endurance'] += 1
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
        "{check=logic:10}Выдвинуть «обоснованные» предположения":
            if skillcheck('logic', lvl_medium):
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
            else:
                window show
                play sound ds_sfx_int
                lgc "{result}Да сто процентов гулять пошёл просто и скоро вернётся!"
                me "Я думаю, он просто загулялся и скоро сам придёт."
        "{check=shivers:14}Вслушаться в окружающую среду":
            if skillcheck('shivers', lvl_legendary):
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
            else:
                window show
                play sound ds_sfx_fys
                shi "{result}Как ты ни пытаешься - не даёт тебе природа ответа."
            $ ds_skill_points['shivers'] += 1
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
            "{check=savoir_faire:13}Прошмыгнуть в столовую":
                if skillcheck('savoir_faire', lvl_formidable):
                    window show
                    play sound ds_sfx_mot
                    svf "{result}Ты быстрыми резкими движениями пробегаешь мимо Ольги Дмитриевны, и прежде чем она успеет отреагировать, ты оказываешься в столовой."
                    $ ds_skill_points['savoir_faire'] += 1
                else:
                    window show
                    play sound ds_sfx_mot
                    svf "{result}Однако, ты врезаешься прямо в Ольгу Дмитриевну и опрокидываешь её."
                    show mt rage pioneer at center
                    with dspr
                    "Ольга Дмитриевна поднимается очень злая на тебя."
                    $ ds_lp['mt'] -= 1
                    $ ds_karma -= 10
                    $ ds_skill_points['savoir_faire'] += 1
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
            "{check=composure:15}Стоять молча":
                if skillcheck('composure', lvl_heroic):
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
                    $ ds_skill_points['composure'] += 1
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
    show us laugh pioneer at cright 
    show dv normal pioneer at cleft 
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
                        show dv rage pioneer at cleft
                        with dspr
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
                        if skillcheck('empathy', lvl_easy, passive=True):
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
        "Ответить неопределённо":
            window show
            me "Можно мне подумать?"
            show us laugh2 pioneer at cright
            with dspr
            us "Нет, нельзя! Твоё решение нужно сейчас!"
    if skillcheck('half_light', lvl_trivial, passive=True):
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
    "Мы остались наедине с Алисой."
    me "Знаешь, я всё же, наверное, с вами не пойду."
    show dv normal pioneer at center   with dspr
    dv "А что так?"
    me "Ну, дела кое-какие…"
    show dv surprise pioneer at center   with dspr
    dv "И что же у тебя за дела?"
    "Она заглянула мне в глаза так, что я не нашёлся, что соврать."
    me "Ну, у меня и плавок даже нет…"
    show dv normal pioneer at center   with dspr
    dv "Надень мои."
    me "Думаешь, они на меня налезут?"
    show dv grin pioneer at center   with dspr
    dv "А ты попробуй!"
    me "Наверное, не стоит…"
    show dv smile pioneer at center   with dspr
    dv "Да ты не бойся!{w} Найдём мы тебе плавки!"
    "От этой фразы страх мой только усилился."
    dv "Подожди меня возле столовой, я вернусь через пару минут."
    me "Ладно…"

    stop ambience fadeout 2

    th "В конце концов, ничего такого в том, чтобы просто её дождаться, нет?.."
    window hide