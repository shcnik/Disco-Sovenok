# DISCO SOVENOK
# ОБЩИЙ РУТ. ДЕНЬ 4
# +КОРНИ РУТОВ АЛИСЫ, ЛЕНЫ, СЛАВИ, МИКУ

init:
    $ ds_caught_in_lib = False
    $ ds_have_guess_sh = False
    $ ds_dv_breakfast_absent = False
    $ ds_triggered_dv = False
    $ ds_d4_us_accept = True
    $ ds_on_beach_pants = False
    $ ds_d4_places_remain = 5
    $ ds_dv_door_broken = False
    $ ds_had_vision_mines = False
    $ ds_hit_mz = False
    $ ds_reading_books = False
    $ ds_calmed_mz = False
    $ ds_having_tea_mz = False
    $ ds_visited_old_camp = False
    $ ds_found_old_books = False
    $ ds_took_old_book = False
    $ ds_found_elevator = False
    $ ds_ran_from_ya = False
    $ ds_got_info_from_ya = False
    $ ds_reading_journal = False
    $ ds_dv_has_coal = False
    $ ds_d4_know_dv_plan = False
    $ ds_dv_threaten_dv_mt = False

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
            $ ds_have_guess_sh = True
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
                el "Или старый лагерь! Да, он говорил об этом!"
                $ ds_have_guess_sh = True
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
                $ ds_have_guess_sh = True
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
            $ ds_d4_us_accept = False
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
                    if not skillcheck('composure', lvl_challenging, passive=True):
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
            if skillcheck('instinct', lvl_easy, passive=True):
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
                    $ ds_damage_morale()
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
                    if skillcheck('instinct', lvl_easy, passive=True):
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
                            $ ds_damage_morale()
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
                    if skillcheck('instinct', lvl_easy, passive=True):
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
                            $ ds_damage_morale()
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
                    if not skillcheck('composure', lvl_challenging, passive=True):
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
            if skillcheck('instinct', lvl_easy, passive=True):
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
                    $ ds_damage_morale()
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
                    if skillcheck('instinct', lvl_easy, passive=True):
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
                            $ ds_damage_morale()
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
    scene bg 
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
        "{check=visual_calculus:10}Преследовать Алису":
            if skillcheck('visual_calculus', lvl_medium):
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
                $ ds_skill_points['visual_calculus'] += 1
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
        if skillcheck('instinct', lvl_easy, passive=True):
            ins "{result}А может она и не на плавки смотрит?"
        window hide
        menu:
            "Подтвердить":
                window show
                me "Как видишь."
            "Проигнорировать":
                window show
            "Спошлить" if ds_last_skillcheck.result:
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
                $ ds_damage_health()
                "Прежде чем ты успеваешь что-либо сделать, Алиса нокаутирует тебя."
                "И дальше начинает тебя избивать."
                dv "НИКТО НЕ СМЕЕТ ОБИЖАТЬ УЛЬЯНУ!"
                with flash_red
                $ ds_damage_health()
                me "Остано... остановись..."
                play sound ds_sfx_fys
                edr "Ты чувствуешь, как теряешь сознание."
                $ ds_damage_health()
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
        "{check=authority:11}Потребовать прекратить":
            if skillcheck('authority', lvl_up_medium):
                window show
                play sound ds_sfx_psy
                aut "{result}Покажи, что с тобой шутки плохи."
                me "А ну оставь рака в покое!"
                "Ты показываешь такое злое лицо, что Ульяна не решается тебя ослушаться."
                scene bg ext_beach_day
                show us dontlike swim at center
                with dissolve
                us "Ладно, раз он тебе так дорог..."
                $ ds_skill_points['authority'] += 1
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
                $ ds_skill_points['authority'] += 1
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
        "{check=savoir_faire:10}Спасти рака":
            if skillcheck('savoir_faire', lvl_medium):
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
                show us surp2 swim at right
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
                jump ds_day4_beach_sl
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
                if skillcheck('drama', lvl_easy, passive=True):
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
                            $ ds_skill_points['drama'] += 1
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
                if not skillcheck('composure', lvl_challenging, passive=True):
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
                        $ ds_damage_morale()
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
            "{check=physical_instrument:10}Нанести превентивный удар":
                if skillcheck('physical_instrument', lvl_medium):
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
                        "{check=pain_threshold:10}Принять удар на себя":
                            window show
                            "Ты готовишься принять ответку от Алисы."
                            play sound sfx_face_slap
                            with hpunch
                            "Алиса ограничивается пощёчиной."
                            window hide
                            if skillcheck('pain_threshold', lvl_medium):
                                window show
                                play sound ds_sfx_fys
                                pat "{result}Но всё равно больно! Впрочем, не сильно."
                            else:
                                window show
                                play sound ds_sfx_fys
                                pat "{result}Но даже от этого у тебя уже горит щека!"
                                $ ds_damage_morale()
                            $ ds_skill_points['pain_threshold'] += 1
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
    if skillcheck('drama', lvl_medium, passive=True):
        play sound ds_sfx_int
        dra "{result}Или же {i}изображает{/i} таковую."
    "Ты рассматриваешь комнату."
    vic "Нельзя сказать, что здесь недавно случился погром, но беспорядок порядочный."
    th "Получается, я ещё не самый ленивый и неаккуратный человек в мире – раз уж всего за одну смену в лагере можно развести такой бардак."
    "Ты не думаешь ни о чём конкретно, а просто осматривал домик Алисы."
    play sound ds_sfx_mot
    per_eye "Плакаты советских артистов, какие-то книжки на полках, всякая бытовая мелочёвка…"

    if skillcheck('half_light', lvl_easy, passive=True):
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
                    "{check=physical_instrument:13}Выбить дверь":
                        if skillcheck('physical_instrument', lvl_formidable):
                            window show
                            play sound ds_sfx_fys
                            phi "{result}Впрочем, двери тут хлипкие, так что ты без труда дверь выбиваешь."
                            scene bg ext_house_of_dv_day
                            with vpunch
                            "И вываливаешься из домика, лёжа на двери."
                            $ ds_skill_points['physical_instrument'] += 1
                            "Ты поднимаешься и смотришь на домик Алисы."
                            $ ds_dv_door_broken = True
                            $ ds_skill_points['physical_instrument'] += 1
                            jump ds_day4_dv_escaped
                        else:
                            window show
                            play sound ds_sfx_fys
                            phi "{result}Но дверь оказывается не такой слабой, какой она оказалась на первый взгляд."
                            play sound ds_sfx_fys
                            pat "Всё, чего ты добился - отбил себе плечо."
                            $ ds_skill_points['physical_instrument'] += 1
                            $ ds_damage_health()
                    "Ждать своей участи":
                        window show
                        th "Да ладно, ничего же не случится? Надо ведь доверять людям?"
                        play sound ds_sfx_psy
                        vol "Доверяй, но проверяй! А впрочем как хочешь."
    show mt normal panama pioneer at cright
    show dv smile pioneer at cleft
    with dissolve
    "Вскоре Алиса возвращается. И оказывается, что она хотела «взять» Ольгу Дмитриевну!"
    if skillcheck('logic', lvl_trivial, passive=True):
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
        "{check=composure:14}Отказаться объясняться":
            if skillcheck('composure', lvl_legendary):
                window show
                play sound ds_sfx_mot
                com "{result}Ты прав. И лучше всего ты это покажешь, если не будешь судорожно оправдываться, а будешь стоять спокойно."
                $ ds_skill_points['composure'] += 1
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
                $ ds_skill_points['composure'] += 1
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
        "{check=savoir_faire:10}Изобразить мимокрокодила":
            if skillcheck('savoir_faire', lvl_medium):
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
                $ ds_skill_points['savoir_faire'] += 1
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
                "{check=volition:14}Выйти из укрытия":
                    if skillcheck('volition', lvl_legendary):
                        window show
                        play sound ds_sfx_psy
                        vol "{result}Ты плюёшь на страх быть поколоченным и выходишь из своего укрытия."
                        $ ds_skill_points['volition'] += 1
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
                        $ ds_skill_points['volition'] += 1
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
    if skillcheck('savoir_faire', lvl_easy, passive=True):
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
            if not skillcheck('composure', lvl_challenging, passive=True):
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
                "{check=physical_instrument:10}Вырваться":
                    if skillcheck('physical_insturment', lvl_medium):
                        window show
                        play sound ds_sfx_fys
                        phi "{result}Дёрни резко рукой - что может быть проще?"
                        "Ты так и делаешь. Тебе удаётся вырвать руку у Мику."
                        play sound sfx_body_fall
                        "Но ценой того, что Мику падает на землю."
                        $ ds_skill_points['physical_instrument'] += 1
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
                        $ ds_skill_points['physical_instrument'] += 1
                        $ ds_damage_morale()
                "{check=suggestion:11}Настоять на отказе":
                    if skillcheck('suggestion', lvl_up_medium):
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
        "{check=interfacing:12}Попробовать":
            if skillcheck('interfacing', lvl_challenging, modifiers=[('ds_played_guitar', 2, 'Уже играл на гитаре')]):
                window show
                play sound ds_sfx_mot
                inf "{result}Ты берёшь гитару и точно отыгрываешь нужную партию."
                show mi smile pioneer at center
                with dspr
                mi "Ой, какой ты молодец, Семён-кун, классненько получилось!"
                $ ds_up_morale()
                $ ds_skill_points['interfacing'] += 1
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
        "{check=empathy:11}Подбодрить Мику":
            if skillcheck('empathy', lvl_up_medium):
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
    if skillcheck('perception', lvl_trivial, passive=True):
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
            if skillcheck('inland_empire', lvl_easy, passive=True):
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
    if skillcheck('rhetoric', lvl_medium, passive=True):
        play sound ds_sfx_int
        rhe "{result}Для справки - одним из эвфемизмов, обозначающих тех мужчин, что по другим мужчинам - как раз «трубочисты»."
        play sound ds_sfx_psy
        vol "Эта информация тебя в определённом смысле шокирует. Ты стоишь на месте, не зная что делать."
        play sound ds_sfx_mot
        com "Похоже, он это заметил."
    else:
        "Тут он обращает на тебя внимание."
    el "Сейчас помоюсь и тебе место уступлю."
    if (ds_homo_traits == 2) and skillcheck('instinct', lvl_medium, passive=True):
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
        "{check=drama:11}Придумать полезное дело":
            if skillcheck('drama', lvl_up_medium):
                window show
                play sound ds_sfx_int
                dra "{result}А давайте вы будете переписывать бумаги для вожатой! Тут как раз и реквезит в виде листочков удобно разложился."
                me "Да так, Ольга Дмитриевна велела переписать бумаги."
                show sl serious pioneer at center
                with dspr
                sl "Да? А я слышала, что она поручила тебе Шурика искать."
                dra "Она раскусила нас! Эта проницательная женщина раскусила нас!"
                $ ds_skill_points['drama'] += 1
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
                $ ds_skill_points['drama'] += 1
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
        "{check=authority:10}Отказаться":
            if skillcheck('authority', lvl_medium):
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
                $ ds_skill_points['authority'] += 1
                jump ds_day4_day_sleep
            else:
                window show
                play sound ds_sfx_psy
                aut "{result}Ты считаешь неправильным отказывать Славе."
                $ ds_skill_points['authority'] += 1
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
                if skillcheck('reaction_speed', lvl_medium, passive=True):
                    play sound ds_sfx_mot
                    res "{result}Берегись! Она начинает присматривать книгу, чтобы метнуть в тебя."
                    "Ты рефлекторно отпрыгиваешь."
                else:
                    play sound sfx_punch_washstand
                    with flash_red
                    "Тебе по голове прилетает книгой."
                    if skillcheck('pain_threshold', lvl_up_medium, passive=True):
                        play sound ds_sfx_fys
                        pat "{result}Для тебя это пустяки, конечно..."
                        "Но ты отходишь, чтобы не получить сильнее."
                    else:
                        play sound ds_sfx_fys
                        pat "{result}Больно! У тебя на голове вылезает шишка."
                        $ ds_damage_health()
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
                        "{check=drama:10}Начать «умирать»":
                            if skillcheck('drama', lvl_medium):
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
                                $ ds_skill_points['drama'] += 1
                            else:
                                play sound ds_sfx_int
                                dra "{result}Нет, смысла нет. Вы уже простояли спокойно немало времени, мессир."
                                me "Ну... голова болит..."
                                show sl serious pioneer close at center
                                with dspr
                                sl "Подожди тогда, я сейчас приду!"
                                $ ds_skill_points['drama'] += 1
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
                        if skillcheck('reaction_speed', lvl_medium, passive=True):
                            play sound ds_sfx_mot
                            res "{result}Берегись! Она начинает присматривать книгу, чтобы метнуть в тебя."
                            "Ты рефлекторно отпрыгиваешь."
                        else:
                            play sound sfx_punch_washstand
                            with flash_red
                            "Тебе по голове прилетает книгой."
                            if skillcheck('pain_threshold', lvl_up_medium, passive=True):
                                play sound ds_sfx_fys
                                pat "{result}Для тебя это пустяки, конечно..."
                                "Но ты отходишь, чтобы не получить сильнее."
                            else:
                                play sound ds_sfx_fys
                                pat "{result}Больно! У тебя на голове вылезает шишка."
                                $ ds_damage_health()
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
                                "{check=drama:10}Начать «умирать»":
                                    if skillcheck('drama', lvl_medium):
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
                                        $ ds_skill_points['drama'] += 1
                                    else:
                                        play sound ds_sfx_int
                                        dra "{result}Нет, смысла нет. Вы уже простояли спокойно немало времени, мессир."
                                        me "Ну... голова болит..."
                                        show sl serious pioneer close at center
                                        with dspr
                                        sl "Подожди тогда, я сейчас вернусь!"
                                        $ ds_skill_points['drama'] += 1
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
        "{check=inland_empire:12}Подумать о последствиях":
            window show
            th "И что теперь будет? Мы не найдём Шурика?"
            window hide
            if skillcheck('inland_empire', lvl_challenging):
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
            $ ds_skill_points['inland_empire'] += 1
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
        "{check=physical_instrument:10}Разбудить":
            if skillcheck('physical_instrument', lvl_medium):
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
                $ ds_skill_points['physical_instrument'] += 1
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
                $ ds_skill_points['physical_instrument'] += 1
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
                if skillcheck('conceptualization', lvl_easy, passive=True):
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
                if skillcheck('logic', lvl_trivial, passive=True):
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
        if skillcheck('empathy', lvl_easy, passive=True):
            play sound ds_sfx_psy
            emp "Она явно приняла тебя за насильника."
        "Она хватает книгу и пытается... прикрыться ей."
        window hide
        menu:
            "{check=suggestion:14}Убедить, что ты не опасен" if (ds_day3_evening_who == 'mz') and ds_last_skillcheck.result:
                if skillcheck('suggestion', lvl_legendary):
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
                    $ ds_skill_points['suggestion'] += 1
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
                    $ ds_skill_points['suggestion'] += 1
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
                    if skillcheck('reaction_speed', lvl_medium, passive=True):
                        play sound ds_sfx_mot
                        res "{result}Берегись! Она начинает присматривать книгу, чтобы метнуть в тебя."
                        "Ты рефлекторно отпрыгиваешь."
                    else:
                        play sound sfx_punch_washstand
                        with flash_red
                        "Тебе по голове прилетает книгой."
                        if skillcheck('pain_threshold', lvl_up_medium, passive=True):
                            play sound ds_sfx_fys
                            pat "{result}Для тебя это пустяки, конечно..."
                            "Но ты отходишь, чтобы не получить сильнее."
                        else:
                            play sound ds_sfx_fys
                            pat "{result}Больно! У тебя на голове вылезает шишка."
                            $ ds_damage_health()
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
                if skillcheck('encyclopedia', lvl_medium, passive=True):
                    play sound ds_sfx_int
                    enc "{result}То-то же, они тут в своём пионерлагере собственное государство по Платону построили. Не удивительно, что ничего не изменилось."
                mz "Начинаешь лучше понимать, почему всё вокруг устроено так, а не иначе. С чего всё началось, чем люди вдохновлялись."
                if skillcheck('encyclopedia', lvl_easy, passive=True):
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
        "{check=logic:12}Вглядеться в символы":
            if skillcheck('logic', lvl_challenging):
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
        "{check=logic:13}Изучить карту":
            if skillcheck('logic', lvl_formidable):
                window show
                play sound ds_sfx_int
                lgc "{result}Смотри! В нижнем левом углу некий пунктир. Это не может быть ничем иным, кроме как дорогой к нему!"
                play sound ds_sfx_psy
                vol "Значит, идём туда."
                $ ds_skill_points['logic'] += 1
            else:
                window show
                play sound ds_sfx_int
                lgc "{result}На карте нет даже намёков на старый лагерь. Она бесполезна."
                $ ds_skill_points['logic'] += 1
                jump ds_day4_find_camp
        "{check=shivers:14}Спросить у лагеря":
            if skillcheck('shivers', lvl_legendary):
                window show
                play sound ds_sfx_fys
                shi "{result}Прислушайся. Ты слышишь скрип очень старых полов. Ветер, гуляющий по заброшенным комнатам."
                shi "Он доносит до тебя голоса детей. Очень давние голоса детей. И пытающихся их утихомирить вожатых."
                th "А откуда это всё идёт-то."
                shi "Юго-запад. Тебе нужно туда."
                $ ds_skill_points['shivers'] += 1
            else:
                window show
                play sound ds_sfx_fys
                shi "{result}Бесполезно. Лагерь не откликается на твой призыв о помощи."
                $ ds_skill_points['shivers'] += 1
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
    if skillcheck('volition', lvl_challenging, passive=True):
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
    if skillcheck('conceptualization', lvl_easy, passive=True):
        play sound ds_sfx_int
        con "{result}Только представь: ранее тут играли и резвились пионеры, а вожатые следили за порядком. Одни лица сменялись другими. А теперь всё ушло."
        con "Этот лагерь ассоциируется у тебя с твоей жизнью. Ранее она была наполнена счастьем, у тебя было много знакомых. А теперь? Всё вот так же пришло в негодность."
    if skillcheck('inland_empire', lvl_easy, passive=True):
        window hide
        play sound sfx_ghost_children_laugh
        $ renpy.pause(1.5)
        window show
        play sound2 ds_sfx_psy
        ine "{result}Ты слышишь детский смех. Послышалось?"
        play sound2 ds_sfx_psy
        vol "Тем не менее, тебе становится не по себе."
        if not skillcheck('composure', lvl_challenging, passive=True):
            play sound ds_sfx_mot
            com "{result}Тебя передёргивает от испуга."
        th "Откуда тут... смех?"
        ine "Некогда в этом лагере были же дети? Были. Вот твоё сознание и родило это по ассоциации."
        ine "Или же... ты снова что-то вспомнил?"
        ine "Да! Ты вспомнил своё детство. Твой детский садик напоминал это строение."
        play sound ds_sfx_psy
        vol "А с детским садом у тебя связаны не самые приятные воспоминания..."
        ine "Да! Ты всегда был {i}не такой как все{/i}. И за это подвергался травле."
        $ ds_damage_morale()
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
                $ ds_up_morale()
                "Тебе становится немного легче."
                window hide
                menu:
                    "{check=volition:10}Вновь зайти":
                        if skillcheck('volition', lvl_medium):
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
            if skillcheck('instinct', lvl_medium, passive=True):
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
            scene bg ds_int_old_building_cabinet
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
            if skillcheck('reaction_speed', lvl_easy, passive=True):
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
            scene bg ds_int_old_building_room
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
            if skillcheck('perception', lvl_medium, passive=True):
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
        "{check=empathy:11}Выяснить причины грусти":
            if skillcheck('empathy', lvl_up_medium, modifiers=[('ds_embraced_un', 1, 'Обнял Лену'), ('ds_asked_un_on_sh', -3, 'Поставил Шурика вперёд')]):
                window show
                play sound ds_sfx_psy
                emp "{result}Похоже на то, что у Лены что-то не получилось, и она пала духом из-за этого."
                emp "Самым неразумным будет спрашивать в лоб. Лучше скажи в общем, что она умница."
            else:
                window show
                play sound ds_sfx_psy
                emp "{result}Всё хорошо. Лена явно тебе доверится."
            $ ds_skill_points['empathy'] += 1
            window hide
            menu:
                "Приободрить Лену" if ds_last_skillcheck.result:
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
        "{check=conceptualization:12}Придумать выход":
            if skillcheck('conceptualization', lvl_challenging):
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
                $ ds_skill_points['conceptualization'] += 1
            else:
                window show
                play sound ds_sfx_int
                con "{result}Но если Лена, художница, ничего придумать не может - то ты и подавно ничего не придумаешь!"
                $ ds_skill_points['conceptualization'] += 1
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
    if skillcheck('visual_calculus', lvl_easy, passive=True):
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
                if skillcheck('drama', lvl_medium, passive=True):
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
    if ds_met['ya'] == 2:
        show ya normal pioneer at center
        with dspr
        "Когда ты проходишь около медпункта, то натыкаешься на появившуюся словно из воздуха Яну."
        show ya surprise pioneer at center
        with dspr
        ya "Ой, привет..."
        window hide
        menu:
            "Извиниться":
                window show
                me "Извини, я не хотел."
                show ya normal pioneer at center
                with dspr
                ya "Да всё нормально..."
            "Просто поздоровться":
                window show
                me "Привет."
            "Сбежать":
                window show
                "А ты убегаешь, надеясь, что Яна не поймёт, что это была ты."
                $ ds_ran_from_ya = True
                $ ds_lp['ya'] -= 1
        if not ds_ran_from_ya:
            window hide
            menu ds_day4_ya_dialogue:
                set ds_menuset
                "Cказать про пропавшего Шурика":
                    window show
                    me "Cлушай... а ты не видела Шурика?"
                    show ya surprise pioneer at center
                    with dspr
                    ya "А это... кто?"
                    play sound ds_sfx_int
                    rhe "Cледовало бы описать его - опрометчиво было считать, что она знает кого-то там из другого отряда."
                    me "Ну... такой, блондин в очках, ещё часы носит."
                    show ya normal pioneer at center
                    with dspr
                    ya "Нет... я не видела такого..."
                    ya "Хотя... кто-то похожий, кажется, ходил в лес..."
                    play sound ds_sfx_mot
                    res "В лес? Тогда бессмысленно его искать по лагерю, вероятно."
                    me "Cпасибо..."
                    $ ds_got_info_from_ya = True
                    window hide
                    jump ds_day4_ya_dialogue
                "Cпросить, что она тут делает":
                    window show
                    me "А... а что у тебя случилось?"
                    show ya shy pioneer at center
                    with dspr
                    ya "Да так... один из моих подопечных поранился..."
                    me "А... сочувствую ему..."
                    show ya normal pioneer at center
                    with dspr
                    ya "Я передам ему."
                    window hide
                    jump ds_day4_ya_dialogue
                "Cделать Яне комплимент":
                    window show
                    me "Прекрасно выглядишь, кстати!"
                    me "Такие яркие зелёные глаза, да и волосы..."
                    show ya shy2 pioneer at center
                    with dspr
                    ya "Спасибо..."
                    $ ds_lp['ya'] += 1
                    window hide
                    jump ds_day4_ya_dialogue
                "Предложить помощь":
                    window show
                    me "Может, помочь тебе?"
                    show ya shy pioneer at center
                    with dspr
                    ya "Ой... нет, не надо... я сама..."
                    play sound ds_sfx_psy
                    emp "Ей действительно не требуется помощь. Она в принципе не желает кого-либо напрягать."
                    me "Точно?"
                    ya "Точно..."
                    window hide
                    jump ds_day4_ya_dialogue
                "Попрощаться и уйти":
                    window show
                    me "Ну ладно, я пошёл! Пока!"
                    ya "Пока..."
                    hide ya with dissolve
        if ds_got_info_from_ya:
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
    if not skillcheck('perception', lvl_medium, passive=True):
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
        "{check=physical_instrument:15}Выломать дверь" if ds_last_skillcheck.result:
            if skillcheck('physical_instrument', lvl_heroic):
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
                if skillcheck('inland_empire', lvl_medium, passive=True):
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
                scene bg ext_stage_near_day
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
                $ ds_damage_health()
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
    if skillcheck('perception', lvl_medium, passive=True):
        show dv angry pioneer far at cleft, ds_seated
        show ya normal pioneer far at cright, ds_seated
        with dissolve
        play sound ds_sfx_mot
        if ds_met['ya'] == 2:
            per_eye "{result}Вдали ты примечаешь свободное место рядом с Алисой и Яной."
        else:
            per_eye "{result}Вдали ты примечаешь свободное место рядом с Алисой и незнакомой тебе девушкой."
        window hide
        menu:
            "{check=authority:10}Сесть с девушками":
                if skillcheck('authority', lvl_medium):
                    window show
                    play sound ds_sfx_psy
                    aut "{result}Просто откажись. Возражений не последует."
                    me "Я уже договорился!"
                    $ ds_skill_points['authority'] += 1
                    "И ты идёшь к девочкам."
                    show dv angry pioneer at cleft
                    show ya normal pioneer at cright
                    with dspr
                    play sound ds_sfx_int
                    rhe "По всей видимости, они о чём-то спорят. Точнее, спорит Алиса."
                    dv "Почему ты такая... такая безразличная ко всему?!"
                    dv "Почему ты ведёшь себя как тупо кукла в руках чиновников?!"
                    ya "Прекрати злиться..."
                    if ds_lp['dv'] >= 25:
                        ya "Ты не сможешь понравиться ему, если будешь срываться на всех."
                    else:
                        ya "Ты не сможешь быть лучшей, если будешь срываться на всех."
                    ya "Тебе нужно быть спокойнее..."
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
                    hide ya
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
        "Cообщить сведения от Яны" if ds_got_info_from_ya:
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
    show cs normal at center   with dissolve
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
    if skillcheck('perception', lvl_easy, passive=True):
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
        if skillcheck('composure', lvl_medium, passive=True):
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
            if skillcheck('instinct', lvl_medium, passive=True):
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
                "Предложить презерватив" if ds_last_skillcheck.result:
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
        if skillcheck('conceptualization', lvl_easy, passive=True):
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
    if skillcheck('empathy', lvl_easy, passive=True):
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
            if skillcheck('logic', lvl_medium, passive=True):
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
                "{check=physical_instrument:8}Вырвать пакетик":
                    if skillcheck('physical_instrument', lvl_easy):
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
                    $ ds_skill_points['physical_instrument'] += 1

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
            if skillcheck('conceptualization', lvl_medium, passive=True):
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
            if skillcheck('drama', lvl_trivial, passive=True):
                play sound ds_sfx_int
                dra "{result}Звездит. Звездит как дышит."
                me "Так я тебе и поверил!"
                dv "Иди сам посмотри…"
            play sound ds_sfx_mot
            svf "В любом случае, ты же быстренько."
            window hide
            menu:
                "{check=reaction_speed:12}Проверить":
                    window show
                    hide dv  with dissolve
                    "Ты подходишь к двери и выглядываешь на улицу.{w} Там никого не оказывается."
                    if skillcheck('reaction_speed', lvl_challenging):
                        window show
                        show dv evil_smile pioneer at center
                        with dissolve
                        res "{result}Алиса полезла в ящик! Ты успеваешь это заметить!"
                        me "Так-так!"
                        $ ds_skill_points['reaction_speed'] += 1
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
                            "{check=authority:10}Потребовать вернуть уголь":
                                if skillcheck('authority', lvl_medium):
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
                                    $ ds_damage_morale()
                                    $ ds_dv_has_coal = True
                                $ ds_skill_points['authority'] += 1
                            "{check=physical_instrument:10}Отнять уголь":
                                if skillcheck('physical_instrument', lvl_medium):
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
                                    $ ds_damage_health()
                                    show dv laugh pioneer at center
                                    with dspr
                                    dv "Вот же ты слабак, даже уголь забрать не можешь!"
                                    $ ds_damage_morale()
                                    $ ds_dv_has_coal = True
                                    "Со смехом Алиса уходит."
                                    hide dv with dissolve
                                    $ ds_lp['dv'] -= 2
                                    "А тебе остаётся разгромленный медпункт."
                                $ ds_skill_points['physical_instrument'] += 1
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
                        if skillcheck('encyclopedia', lvl_up_medium, passive=True):
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
    $ show_small_map_ds()

label ds_day4_storage:
    $ persistent.sprite_time = "day"
    scene bg ds_ext_storage_day
    with dissolve
    "Ты подходишь к складу."
    if skillcheck('half_light', lvl_up_medium, passive=True):
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
        "{check=perception:10}Рассмотреть мешки":
            if skillcheck('perception', lvl_medium):
                window show
                play sound ds_sfx_mot
                per_eye "{result}На мешках написано «УДОБРЕНИЯ. СЕЛИТРА.»"
                $ ds_skill_points['perception'] += 1
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
        "{check=encyclopedia:12}Понять, зачем нужна селитра" if ds_d4_know_bags_content:
            if skillcheck('encyclopedia', lvl_challenging):
                window show
                play sound ds_sfx_int
                enc "{result}Cелитра, сера и уголь - это же компоненты, которые позволят создать взрывчатку!"
                enc "Селитра - вот она, серу позаимствует у кибернетиков, а активированный уголь - в медпункте."
                $ ds_skill_points['encyclopedia'] += 1
                $ ds_d4_know_dv_plan = True
            else:
                window show
                play sound ds_sfx_int
                enc "{result}Селитра... селитра-селитра-селитра... сейчас я найду назначение..."
                enc "Может, Алиса решила садоводством заняться?"
                play sound ds_sfx_psy
                aut "Алиса? Садоводством?! Да скорее Ульяна попадёт на доску почёта как самая примерная пионерка!"
                $ ds_skill_points['encyclopedia'] += 1
            window hide
            jump ds_d4_dv_storage
        "{check=suggestion:15}Втереться в доверие Алисы" if not ds_betray_dv:
            if skillcheck('suggestion', lvl_heroic, modifiers=[('ds_dinner_dv', 3, 'Был соучастником'), ("ds_lp[['dv'] >= 20", 2, "Алиса тебе доверяет")]):
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
            $ ds_skill_points['suggestion'] += 1
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
    scene bg ext_storage_day
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
    "По дороге меня догнал Электроник."
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
                    $ ds_damage_morale()
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
    if skillcheck('reaction_speed', lvl_easy, passive=True):
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
        if not skillcheck('composure', lvl_challenging, passive=True):
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
        if skillcheck('visual_calculus', lvl_medium, passive=True):
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
        if skillcheck('perception', lvl_medium, passive=True):
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
        "{check=authority:15}Отказаться":
            jump ds_day4_no_shaft