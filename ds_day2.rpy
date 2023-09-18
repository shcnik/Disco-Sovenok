# DISCO SOVENOK
# ОБЩИЙ РУТ. ДЕНЬ 2
init:
    $ mods["disco_sovenok"] = u"Disco Sovenok"

    $ ds_know_face = False
    $ ds_passed_places = 0
    $ ds_visited_music = False
    $ ds_visited_clubs = False
    $ ds_visited_sport = False
    $ ds_visited_medic = False
    $ ds_visited_library = False
    $ ds_cyber_member = False
    $ ds_music_member = False
    $ ds_sport_member = False
    $ ds_library_member = False
    $ ds_find_hairpin = False
    $ ds_read_book = False
    $ ds_had_lunch = False
    $ ds_sl_interrogate = False
    $ ds_witnessed_el_hit = False
    $ ds_sl_gone = False
    $ ds_un_upset = False
    $ ds_un_invite = False
    $ ds_yield_un = False
    $ ds_cs_invite = False
    $ ds_eldv_side_taken = 0
    $ ds_cards_sl = False
    $ ds_cards_labeled = False
    $ ds_cards_damaged = False
    $ ds_some_key = False
    $ ds_bet_dv = False
    $ ds_mz_brought_el = False
    $ ds_bring_mz_fail = False
    $ ds_attack_mz = False
    $ ds_tour_result = 0 # 0 - не прошёл 1/4-финал, 1 - дошёл до полуфинала, 2 - дошёл до финала, 3 - выиграл в турнире, -1 - отказался от участия, -2 - дисквалифицирован.
    $ ds_mi_hairpin = False
    $ ds_gave_hairpin_dv = False
    $ ds_gave_hairpin_sl = False
    $ ds_gave_hairpin_un = False
    $ ds_dv_rescued = False
    $ ds_dv_steal_got = False
 
label ds_day2_morning:
    $ ds_health = ds_skill_points['endurance']
    $ ds_morale = ds_skill_points['volition']

    $ backdrop = "days"

    $ new_chapter(2, u"Disco Sovenok. День 2")
    $ day_time()

    $ persistent.sprite_time = "day"
    scene bg int_house_of_mt_day 
    with fade2

    window show
    "Ты просыпаешься."
    window hide

    play music music_list["my_daily_life"] fadein 5

    with flash

    window show
    "Яркие лучи солнца бьют в глаза."
    "На будильнике, стоявшем на окне, время приближается к полудню."
    play sound ds_sfx_psy
    ine "Лениво потянувшись и зевнув, ты начинаешь вспоминать вчерашний день."
    ine "За несколько секунд все его события пронеслись перед глазами: автобус, лагерь, местные обитатели."
    ine "И тут ты явственно понимаешь, что все это не так, неправильно!"
    ine "Нет, не эта ситуация, не твоё положение – они неправильны априори, – а твоё отношение к ним."
    th "Ведь я вот так запросто заснул здесь, до этого мило беседовал с местными пионерами, даже умудрялся шутить!"
    th "Но как можно себя так вести в подобной ситуации?!"
    th "Я же должен бояться, опасаться каждого шороха, избегать любого контакта с потенциально враждебными существами."
    ine "Все события вчерашнего дня словно заволакивает похмельная дымка."
    th "Да, это очень похоже на утро после хорошей пьянки – то, что тебе накануне представлялось вполне естественным, непредосудительным и вообще в высшей степени нормальным, сегодня кажется каким-то кошмаром, гротескной гравюрой из иллюстраций к «Божественной комедии»."
    th "Да, все именно так, однако прошлого уже не вернуть."
    play sound ds_sfx_fys
    hfl "Хотя, возможно, ничего такого в твоих поступках и нет – оценив обстановку, ты действовал по ситуации."
    hfl "В крайнем случае вреда тебе это не принесло, так что лучше сильно не менять свою линию поведения, но впредь быть осмотрительнее."
    play sound ds_sfx_mot
    per_eye "Оглядевшись по сторонам, словно пытаясь понять, не забросило ли тебя опять куда-нибудь в другое место, ты отмечаешь, что домик Ольги Дмитриевны выглядит так же, как и вчера."
    per_eye "Но что-то все же изменилось."
    per_eye "Пионерская форма, висящая на спинке кровати!"
    "Ты с недоверием покрутил ее в руках, примерил и оделся."
    th "Все равно это лучше, чем ходить в зимней одежде."
    window hide
    menu:
        "Посмотреть в зеркало":
            window show
            "Ты начал искать зеркало."
            th "Хотя бы самое маленькое – надо посмотреть на себя, оценить как ты выгляжу."

            "Это не составило большого труда – оно обнаружилось на внутренней стороне дверцы шкафа."

            play sound sfx_open_cabinet_2

            window hide

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
        "Забить":
            window show
            th "Проблема с моим внешним видом, может, и важна, но решение ее сейчас не главное, и вряд ли оно приблизит меня к разгадке всего, что здесь происходит."
    window hide

    pause(1)

    $ persistent.sprite_time = "day"
    scene bg int_house_of_mt_day 
    with dissolve

    window show
    "Если верить часам, то завтрак уже давно позади."
    th "Ну ладно, попробую все же в столовой чего-нибудь найти."
    if ds_dinner_dv:
        th "Вчера же с Алисой получилось."
    else:
        th "Вчера же со Славей получилось."
    "При воспоминании об этом ты невольно улыбаешься."
    window hide

    stop music fadeout 3

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    "На улице ярко светит солнце, дует легкий ветерок."
    th "Прекрасный летний день."
    "Ты ловишь себя на мысли, что уже несколько лет не чувствовал себя по утрам так хорошо."
    "Все твои проблемы на секунду улетают куда-то далеко..."
    "Как вдруг перед тобой словно из ниоткуда возникает Ольга Дмитриевна..."
    show mt normal panama pioneer at center   with dissolve
    mt "Доброе утро, Семен!"
    me "Доброе!"
    "Ты улыбаешься, пытаясь всем своим видом показать, что несмотря ни на что утро твоё было действительно добрым."
    mt "У тебя первый день только вчера был, поэтому я тебя будить не стала, но завтрак-то…"
    show mt smile panama pioneer at center   with dspr
    mt "Впрочем, ладно! Вот, держи!"
    "Она протягивает тебе какой-то бумажный сверток."
    "При ближайшем рассмотрении по масляным пятнам ты понимаешь, что это бутерброды."
    me "Ой, спасибо!"
    show mt normal panama pioneer at center   with dspr
    mt "А теперь марш умываться!"
    "Ты уже собрался уходить, как она останавливает меня."
    mt "Сейчас, подожди."
    hide mt  with dissolve
    window hide

    pause(1)

    window show
    show mt normal panama pioneer at center   with dissolve
    "Ольга Дмитриевна забегает в домик и, вернувшись, суёт тебе какой-то пакетик."
    "Внутри - зубная щетка, мыло, небольшое полотенце и что-то еще."
    show mt smile panama pioneer at center   with dspr
    mt "Пионер должен быть всегда чист и опрятен!"
    mt "Дай я тебе галстук правильно завяжу на первый раз, а то он у тебя болтается.{w} Потом научишься, сам будешь!"
    me "А может, не надо? Я сейчас умываться же иду – неудобно будет."
    th "Ну да, вдруг зацеплюсь за кран и удавлюсь..."
    show mt normal panama pioneer at center   with dspr
    mt "Да, пожалуй…{w} Ладно, тогда потом.{w} И не забудь про линейку."
    th "Карандаши, ручки, линейки…{w} Такие вещи не забываются!"
    me "Какую линейку?"
    show mt angry panama pioneer at center   with dspr
    mt "Ну как же?!"
    "Она хмурится."
    mt "Сегодня же понедельник!"
    th "Странно, а по моим подсчетам – воскресенье…"
    th "Впрочем, смена дня недели – это не самое страшное."
    show mt normal panama pioneer at center   with dspr
    mt "Обычно у нас линейки рано утром, еще до завтрака, но сегодня, так как понедельник, она будет в 12 часов."
    mt "Не опаздывай!"
    me "Хорошо. А где?"
    mt "На площади, где же еще!"
    play sound ds_sfx_int
    rhe "Спорить бессмысленно."

    stop ambience fadeout 2

    "Ты направляешься в сторону «помывочной»."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_washstand_day 
    with dissolve

    play music music_list["everyday_theme"] fadein 5

    window show
    "Да, отдельного душа и туалета в пионерлагере, конечно, ожидать не стоило, но почему-то при виде этого атавизма загнивающего социализма – причудливой черепашки с панцирем из жести, множеством ног-кранов и кафельным брюшком – тебе становится несколько не по себе."
    play sound ds_sfx_psy
    vol "Нет, ты не брезгливый человек."
    vol "В конце концов, тебе даже как-то удалось пережить вчерашний день."
    vol "Но тем не менее, стоя тут, ты осознаёшь, что все же есть какой-то минимальный уровень комфорта, к которому ты привык и без которого жить мне довольно проблематично."
    vol "Вот ведь как бывает – когда теряешь вещи, кажущиеся тебе абсолютно обыденными и естественными, понимаешь, что на самом деле они были незаменимы."
    vol "С другой стороны, выбора у тебя особого и нет."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_washstand2_day 
    with dissolve

    play sound sfx_open_water_sink

    $ renpy.pause(1)

    play sound_loop sfx_water_sink_stream

    window show
    "Ты открываешь кран."
    play sound ds_sfx_fys
    pat "Вода просто ледяная."
    pat "Если помыть руки такой водой не составило особого труда, то вот умыться или прополоскать рот с ее помощью - большая проблема."
    play sound ds_sfx_mot
    per_eye "В пакетике, который тебе дала Ольга Дмитриевна, нет зубной пасты."
    per_eye "Ты уже было решил, что ничего страшного не будет, если почистить зубы и так, как натыкаешься на какую-то кругленькую коробочку."
    per_eye "При ближайшем рассмотрении это оказывается «Зубной порошок»."
    th "Прелестно! +1 за то, что я где-то в прошлом."
    window hide
    menu:
        "Умыться":
            if skillcheck('pain_threshold', lvl_heroic):
                window show
                play sound ds_sfx_fys
                pat "Однако, тебе удаётся вытерпеть холод и как следует почистить зубы."
            else:
                window show
                play sound ds_sfx_fys
                pat "Всё-таки холод воды невыносим. Тебе больно от неё, физически больно."
                "Ты кое-как умываешься, корчась и ёжась от ледяной воды."
                $ ds_health -= 1
            $ ds_skill_points['pain_threshold'] += 1
        "Забить":
            window show
            th "Не смогу я умыться в такой воде..."
            play sound ds_sfx_int
            lgc "Но это значит, что ты всё время не будешь чистить зубы..."
            lgc "Обязательно попробуй найти воду потеплее!"
    window hide

    stop sound_loop
    play sound sfx_close_water_sink

    $ persistent.sprite_time = "day"
    scene bg ext_washstand_day 
    with dissolve

    window show
    play sound_loop sfx_far_steps
    "Ты уже собираешься идти назад, как слышишь рядом с собой шум шагов."
    show sl normal sport at center   with dissolve
    stop sound_loop
    "Перед тобой стоит Славя в спортивном костюме."
    play sound ds_sfx_int
    con "Похоже, что эта девочка будет хорошо выглядеть абсолютно во всем – и в пионерской форме, и в купальнике, и, наверное, даже в космическом скафандре."
    play sound ds_sfx_fys
    ins "Её фигура тебя определённо манит..."
    show sl smile sport at center   with dspr
    sl "Физкульт-привет!"
    window hide
    menu:
        "Поздороваться":
            if skillcheck('rhetoric', lvl_easy):
                window show
                play sound ds_sfx_int
                rhe "Тут ничего сложного, «привет» достаточно."
                me "Привет!"
            else:
                window show
                play sound ds_sfx_int
                rhe "Приветствие тебе удаётся выбрать не сразу."
                me "Охай… То есть, бобр… Доброе утро! Вот…"
            $ ds_skill_points['rhetoric'] += 1
        "Начать приставать":
            if skillcheck('instinct', lvl_medium):
                window show
                ins "Её фигура настолько привлекательная, а форма так облегает... руки сами тянутся."
                show sl serious sport at center with dspr
                sl "Куда руки тянешь?"
                $ ds_lp_sl -= 1
            else:
                window show
                ins "Но у тебя нет никакой реакции на фигуру. Стимула недостаточно!"
            $ ds_skill_points['instinct'] += 1
    show sl normal sport at center   with dspr
    sl "Почему на завтраке не был?"
    me "Проспал."
    play sound ds_sfx_psy
    aut "Ты говоришь это так, словно гордишься этим своим достижением."
    me "Но мне Ольга Дмитриевна бутерброды принесла."
    show sl smile sport at center   with dspr
    sl "А, ну отлично тогда! Не забудь на линейку прийти!"
    me "Да, конечно."
    th "Забудешь тут."
    sl "Ладно, я побежала, не скучай!"
    hide sl  with dissolve
    "Она машет тебе на прощание и скрывается за поворотом тропинки."
    play sound ds_sfx_int
    lgc "Судя по всему, линейка должна начаться через пару минут."

    stop music fadeout 3

    play sound ds_sfx_mot
    svf "Стоит быстренько забежать «домой», закинуть пакетик с умывальными принадлежностями, съесть бутерброды и только уже потом идти на площадь."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day 
    with dissolve
    menu:
        "Забежать":
            window show
            "Ты распахиваешь дверь домика вожатой и вбежал внутрь так, как будто запрыгивал в последний вагон уходящего поезда."
            $ ds_semtype += 1
            window hide

            scene cg ds_day2_mt_undress1
            with dissolve

            play music music_list["awakening_power"] fadein 0

            window show
            play sound ds_sfx_mot
            res "Но, кажется, это было не лучшим решением – посреди комнаты стоит Ольга Дмитриевна…"
            res "И переодевается!"
            window hide
            menu:
                "Молча стоять":
                    window show
                    play sound ds_sfx_mot
                    com "Ты застываешь как вкопанный, стараясь даже не дышать."
                "Приставать к ней":
                    if skillcheck('instinct', lvl_easy):
                        window show
                        play sound ds_sfx_fys
                        ins "У тебя в штанах от наблюдаемой сцены настоящий праздник."
                        ins "Ты подходишь к ней и хватаешь её за спину."
                    else:
                        window show
                        play sound ds_sfx_fys
                        ins "Ты настолько перенервничал от неудобства ситуации, что ничего сделать не можешь."
                    $ ds_skill_points['instinct'] += 1
            scene cg ds_day2_mt_undress2
            "Наконец вожатая замечает твоё присутсвие..."
            mt "Семен!"
            "Ты тут же отворачиваешься."
            mt "Стучаться надо! А теперь выйди!"
            $ ds_karma -= 5
            window hide
            menu:
                "Подкатить":
                    me "Ну как же, тут такая красота ведь!"
                    mt "Вон!"
                    $ ds_karma -= 5
                    play sound ds_sfx_mot
                    svf "Она начинает искать что-нибудь, чтобы метнуть в тебя, так что беги!"
                    "И ты выбегаешь."
                "Выйти":
                    pass

            stop music fadeout 2

            $ persistent.sprite_time = "day"
            scene bg ext_house_of_mt_day 
            with dissolve

            play ambience ambience_camp_center_day fadein 3

            window show
            "Ты выходишь."
            th "Да, неудобно получилось."
            play sound ds_sfx_fys
            ins "Хотя то, что я увидел, тебе весьма понравилось."
            $ ds_skill_points['instinct'] += 1
        "Постучаться":
            play sound sfx_knock_door2
            window show
            "Ты стучишься в дверь."
            mt "Минуту!"
            $ renpy.pause(1)
            "Ты стоишь и ждёшь."
            $ ds_karma += 1
    "Через минуту показывается Ольга Дмитриевна."
    show mt normal panama pioneer at center   with dissolve
    mt "Вот, держи.{w} Теперь это и твой дом тоже."
    window hide

    play sound sfx_keys_rattle

    $ renpy.pause(1)

    window show
    "Она протянула тебе ключ.{w} Ты кладёшь его в карман."
    th "Дом…"
    th "Конечно, если опустить всю фантасмагоричность происходящего, этот лагерь был далеко не самым плохим местом на Земле, но назвать его домом…"
    th "Всего за день, проведенный здесь."
    play sound ds_sfx_psy
    sug "Ты не уверен, что сможешь сделать это даже спустя год."
    mt "Ладно, пойдем, опаздываем."
    me "А как же бутерброды?.."
    mt "По дороге съешь!"
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_houses_day 
    with dissolve

    window show
    "Вы идёте вдоль палаток пионеров, ты уплетаешь бутерброды с колбасой, а Ольга Дмитриевна без умолку о чем-то говорит."
    "Но твоё внимание полностью сосредоточено на еде."
    show mt normal panama pioneer at center   with dissolve
    mt "Ты меня понял?"
    menu:
        "Притвориться, что слушал":
            if skillcheck('drama', lvl_medium):
                dra "Вы ясно даёте понять своим видом, что всё поняли."
                me "Да, понял."
                show mt smile panama pioneer at center with dspr
                mt "Вот и отлично!"
                $ ds_skill_points['drama'] += 1
            else:
                dra "Но твоё выражение лица всё выдаёт!"
                show mt angry panama pioneer at center   with dspr
                mt "Ты не слушаешь!"
                me "Простите…"
                show mt normal panama pioneer at center   with dspr
                $ ds_karma -= 5
                $ ds_skill_points['drama'] += 1
        "Переспросить":
            me "А?"
            show mt angry panama pioneer at center   with dspr
            mt "Ты не слушаешь!"
            me "Простите…"
            show mt normal panama pioneer at center   with dspr
            $ ds_karma += 5
    mt "Сегодня начинается твоя новая пионерская жизнь!"
    mt "И ты должен приложить все усилия, чтобы она стала счастливой!"
    me "А, да, конечно…"
    show mt surprise panama pioneer at center   with dspr
    mt "Я серьезно! У пионера много обязанностей, на него возложена большая ответственность – участвовать в общественной работе, помогать младшим, учиться, учиться и еще раз учиться!"
    mt "Мы все тут как одна большая семья.{w} И тебе предстоит стать ее частью."
    th "Да, частью…{w} Я готов даже расписаться в партбилете, лишь бы не слушать этот бред."
    show mt smile panama pioneer at center   with dspr
    mt "Надеюсь, что по окончании смены у тебя останутся самые лучшие воспоминания о нашем лагере."
    mt "Воспоминания на всю жизнь!"
    me "А когда смена заканчивается?"
    show mt normal panama pioneer at center   with dspr
    mt "Что ты постоянно глупые вопросы задаешь?"
    th "Похоже, от нее мне никаким образом не добиться ответов."
    play sound ds_sfx_fys
    hfl "А жаль, ведь при всей кажущейся дружелюбности этого мира, {i}он{/i} так и не соизволил представиться."
    th "Возможно, сейчас я к этому отношусь несколько спокойнее, чем еще вчера?"
    hfl "Как будто у вас с {i}ним{/i} негласное перемирие – он не трогает меня, но при этом и мне запрещено задавать какие-либо вопросы."
    hfl "Конечно, такой ситуацией нельзя быть довольным, но что тебе остается?{w} Плохой мир лучше доброй ссоры."
    mt "Самое главное для тебя – использовать время, которое ты проведешь здесь, с пользой."
    me "Я постараюсь."
    play sound ds_sfx_fys
    edr "Этот разговор тебя сильно утомил."

    stop ambience fadeout 2

    th "Я бы лучше попытался узнать хотя бы, где это «здесь» находится.{w} Но…"
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_square_day 
    with dissolve

    play music music_list["get_to_know_me_better"] fadein 5

    window show
    "Вы приходите на площадь."
    "Там уже стоят пионеры, выстроившись в шеренгу."
    "Кажется, что их не так уж и много."
    "Если судить даже по количеству палаток, то детей здесь должно было быть в два, а то и в три раза больше."
    show mt normal panama pioneer at center   with dissolve
    me "А что, еще не все пришли?"
    mt "Да вроде все."
    "Она окидывает взглядом пионеров."
    mt "Ладно, иди становись."
    play sound ds_sfx_mot
    res "Странно.{w} Почему тогда она тебе сказала, что больше спальных мест нет."
    hide mt  with dissolve
    window hide

    scene cg ds_day2_lineup
    with dissolve

    window show
    "Пока вожатая рассказывала о плане мероприятий на неделю, ты осматриваешь присутствующих."
    play sound ds_sfx_int
    enc "Рядом с тобой оказался Электроник, {w}затем Славя, Алиса и Лена (в порядке удаления от тебя), {w}потом две пока незнакомые тебе девушки. {w}В конце Ульяна."
    th "Все знакомые здесь."
    "Пока Ольга Дмитриевна рассказывает про какие-то спортивные соревнования, ты с интересом начинаешь рассматривать памятник."
    th "«Генда»..."
    enc "Ты никак не можешь вспомнить ни одного революционера с похожей фамилией."
    enc "Да и поза у него какая-то странная – кажется, он смотрит на все происходящее с каким-то недоверием, может быть, пренебрежением или даже надменностью."
    th "Наверное, это какой-то местный деятель был…"
    sl "О чем мечтаешь?"
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_square_day 
    show sl normal pioneer at cright 
    show mt normal panama pioneer at cleft 
    with dissolve

    window show
    "Славя выводит меня из раздумий."
    "Рядом стоит Ольга Дмитриевна."
    mt "Ты запомнил план на неделю?"
    me "План?{w} План я никогда не забуду!"
    show mt smile panama pioneer at cleft   with dspr
    mt "Вот и отлично!"
    "Она смотрит на Славю."
    show mt normal panama pioneer at cleft   with dspr
    mt "Принесла?"
    sl "Да."
    "Славя протягивает тебе какой-то листок."
    mt "Это обходной лист. Тут пять позиций. За сегодня тебе нужно везде побывать."
    mt "Во-первых, записаться в клуб, они у нас в здании кружков и отдельно – музыкальный и спортивный."
    mt "Во-вторых, в медпункт зайти."
    mt "Ну, и в-третьих – в библиотеку."
    mt "Все понял?"
    me "Да."
    play sound ds_sfx_int
    enc "Кажется, это отличная возможность что-нибудь выяснить, так как в этих локациях ты еще не бывал."
    mt "Тогда давай, начинай прямо сейчас."
    mt "Или, если хочешь, можешь попросить кого-нибудь пойти с тобой."
    sl "Удачи тебе."
    hide sl 
    hide mt 
    with dissolve
    "Они ушли так быстро, что ты и слова сказать не успел."
    stop music fadeout 3
    window hide
    menu:
        "Пойти с Алисой":
            window show
            th "Мне бы хотелось пойти с Алисой... но вдруг она агрессивно среагирует?"
            if ds_beat_dv or ds_betray_dv:
                "Ты подходишь к Алисе, но сразу замечаешь её недоброжелательный настрой."
                show dv angry pioneer at center with dspr
                dv "Чего тебе надо ещё? Создал уже мне проблем! Проваливай, пока жив!"
                play sound ds_sfx_psy
                emp "Она совершенно не расположена к общению с тобой."
                th "Похоже, придётся идти одному..."
                jump ds_day2_pass_alone_main
            if skillcheck('volition', lvl_challenging):
                play sound ds_sfx_psy
                vol "Всё получится! Иди к ней!"
                $ ds_skill_points['volition'] += 1
                "Ты подходишь к Алисе."
                show dv normal pioneer at center with dspr
                if ds_lp_dv >= 5:
                    show dv smile pioneer at center with dspr
                    dv "Что, тебя отправили обходной лист подписывать?"
                    me "Да."
                    dv "Провести тебя надо?"
                    me "Да, если можно..."
                    dv "Ну так чего тормозишь тогда, пошли!"
                    $ ds_lp_dv += 1
                    jump ds_day2_pass_dv_main
                if skillcheck('authority', lvl_up_medium):
                    play sound ds_sfx_psy
                    aut "А сейчас ты её убедишь пойти с тобой."
                    me "Алиса, тебе {i}нужно{/i} пойти со мной подписывать обходной лист."
                    show dv angry pioneer at center with dspr
                    dv "Чего это вдруг нужно?"
                    show dv normal pioneer at center with dspr
                    "Она видит твоё выражение лица и успокаивается."
                    dv "Ладно, пойдём, всё равно делать нечего!"
                    $ ds_skill_points['authority'] += 1
                    $ ds_lp_dv += 1
                    jump ds_day2_pass_dv_main
                else:
                    play sound ds_sfx_psy
                    aut "У тебя не хватает решимости потребовать у Алисы пойти с тобой."
                    aut "Согласится ли она на просьбу?"
                    me "Алиса, пойдёшь со мной?"
                    show dv angry pioneer at center with dspr
                    dv "Да с чего мне идти с тобой, своих дел полно!"
                    hide dv with dissolve
                    th "Не сработало. Придётся идти одному."
                    $ ds_skill_points['authority'] += 1
                    jump ds_day2_pass_alone_main
            else:
                $ ds_skill_points['volition'] += 1
                vol "Но нет, тебе не хватает решимости подойти к ней и заговорить."
                th "Ладно, наверное, лучше будет пойти одному..."
                jump ds_day2_pass_alone_main
        "Пойти с Леной":
            th "А стоит ли подходить к Лене? Напугаю её еще..."
            if skillcheck('volition', lvl_medium):
                play sound ds_sfx_psy
                vol "Давай, подойди к ней!"
                show un normal pioneer at center with dspr
                me "Лен, может, сходишь со мной на обход?"
                show un shocked pioneer at center with dspr
                un "Что? Ты это мне?"
                show un shy pioneer at center with dspr
                un "Ну пойдём..."
                me "Отлично!"
                jump ds_day2_pass_un_main
            else:
                play sound ds_sfx_psy
                vol "Нет, ты слишком боишься подходить к девушкам."
                th "Лучше пойду один, не буду её беспокоить..."
                jump ds_day2_pass_alone_main
        "Пойти со Славей":
            window show
            "Ты решаешь догнать Славю и попросить её пойти с тобой."
            show sl normal pioneer at center with dspr
            me "Славь, можешь, пожалуйста, сходить со мной?"
            show sl smile pioneer at center with dspr
            sl "Да, конечно."
            sl "Пойдём."
            jump ds_day2_pass_sl_main
        "Пойти одному":
            window show
            th "Лучше пойду один, так будет удобнее."
            $ ds_semtype -= 1
            jump ds_day2_pass_alone_main

label ds_day2_pass_alone_main:
    window show
    if ds_passed_places == 5:
        th "Вот и всё, готово!"
        jump ds_day2_after_pass
    if (ds_passed_places == 3) and not ds_had_lunch:
        th "А вот и обед уже наступил..."
    if ds_passed_places == 0:
        th "Итак, куда лучше сходить сначала?"
    else:
        th "Куда теперь?"
    window hide
    $ disable_all_zones_ds_small()
    if not ds_visited_music:
        $ set_zone_ds_small("music_club", "ds_day2_pass_alone_music")
    if not ds_visited_sport:
        $ set_zone_ds_small("sport_area", "ds_day2_pass_alone_sport")
    if not ds_visited_clubs:
        $ set_zone_ds_small("clubs", "ds_day2_pass_alone_clubs")
    if not ds_visited_library:
        $ set_zone_ds_small("library", "ds_day2_pass_alone_library")
    if not ds_visited_medic:
        $ set_zone_ds_small("medic_house", "ds_day2_pass_alone_medic")
    if (ds_passed_places == 3) and not ds_had_lunch:
        $ set_zone_ds_small("dining_hall", "ds_day2_pass_alone_lunch")
    $ show_small_map_ds()

label ds_day2_pass_dv_main:
    window show
    if ds_passed_places == 0:
        show dv normal pioneer at center with dspr
    else:
        show dv normal pioneer2 at center with dspr
    if ds_passed_places == 5:
        me "Всё, готово, отлично!"
        dv "Ну наконец-то всё обошли..."
        jump ds_day2_after_pass
    if (ds_passed_places == 3) and not ds_had_lunch:
        dv "Так, а мы пойдём обедать? Пора бы уже!"
    elif ds_passed_places == 0:
        dv "И куда мы пойдём сначала? Выбирай!"
        dv "Слушай, а может ну его? Давай я подделаю тебе подписи, и мы займёмся чем-нибудь поинтереснее."
        menu:
            "Подделать подписи":
                me "Давай."
                "Алиса забирает у тебя обходной лист и ставит подписи."
                window hide
                queue sound ds_pen
                queue sound ds_pen
                queue sound ds_pen
                queue sound ds_pen
                queue sound ds_pen
                $ renpy.pause(5.0)
                window show
                "Затем она возвращает его тебе."
                dv "Всё, готово, иди."
                me "А ты?"
                show dv smile pioneer at center with dspr
                dv "А я пойду на пляж! Бывай!"
                $ ds_lp_dv += 1
                $ ds_karma -= 15
                hide dv with dissolve
                jump ds_day2_forged
            "Обойти честно":
                me "Нет, давай честно совершим обход. А то вдруг запалят?"
                show dv sad pioneer at center with dspr
                dv "Ладно-ладно..."
                show dv normal pioneer at center with dspr
                dv "Так, стой!"
                show dv normal pioneer2 at center with dspr
                dv "Жарко, знаешь ли! И не надо так смотреть!"
                show dv laugh pioneer2 at center with dspr
                dv "Глаза выпадут!"
                play sound ds_sfx_fys
                ins "Тебе стоило большого труда оторваться от открывшегося вида."
                show dv normal pioneer2 at center with dspr
                dv "Теперь идём!"
    else:
        th "Куда теперь?"
    window hide
    $ disable_all_zones_ds_small()
    if not ds_visited_music:
        $ set_zone_ds_small("music_club", "ds_day2_pass_dv_music")
    if not ds_visited_sport:
        $ set_zone_ds_small("sport_area", "ds_day2_pass_dv_sport")
    if not ds_visited_clubs:
        $ set_zone_ds_small("clubs", "ds_day2_pass_dv_clubs")
    if not ds_visited_library:
        $ set_zone_ds_small("library", "ds_day2_pass_dv_library")
    if not ds_visited_medic:
        $ set_zone_ds_small("medic_house", "ds_day2_pass_dv_medic")
    if (ds_passed_places == 3) and not ds_had_lunch:
        $ set_zone_ds_small("dining_hall", "ds_day2_pass_dv_lunch")
    $ show_small_map_ds()

label ds_day2_pass_un_main:
    window show
    if ds_passed_places == 5:
        th "Всё, готово, отлично!"
        jump ds_day2_after_pass
    if (ds_passed_places == 3) and not ds_had_lunch:
        show un shy pioneer at center with dspr
        un "Нам бы пообедать..."
    if ds_passed_places == 0:
        th "Итак, куда лучше сходить сначала?"
    else:
        th "Куда теперь?"
    window hide
    $ disable_all_zones_ds_small()
    if not ds_visited_music:
        $ set_zone_ds_small("music_club", "ds_day2_pass_un_music")
    if not ds_visited_sport:
        $ set_zone_ds_small("sport_area", "ds_day2_pass_un_sport")
    if not ds_visited_clubs:
        $ set_zone_ds_small("clubs", "ds_day2_pass_un_clubs")
    if not ds_visited_library:
        $ set_zone_ds_small("library", "ds_day2_pass_un_library")
    if not ds_visited_medic:
        $ set_zone_ds_small("medic_house", "ds_day2_pass_un_medic")
    if (ds_passed_places == 3) and not ds_had_lunch:
        $ set_zone_ds_small("dining_hall", "ds_day2_pass_un_lunch")
    $ show_small_map_ds()

label ds_day2_pass_sl_main:
    window show
    if ds_passed_places == 5:
        th "Всё, готово, отлично!"
        jump ds_day2_after_pass
    show sl smile pioneer at center with dspr
    if (ds_passed_places == 3) and not ds_had_lunch:
        sl "Пойдём пообедаем может?"
    elif ds_passed_places == 0:
        sl "Итак, куда ты хочешь сходить сначала?"
    else:
        sl "Куда пойдём теперь?"
    window hide
    $ disable_all_zones_ds_small()
    if not ds_visited_music:
        $ set_zone_ds_small("music_club", "ds_day2_pass_sl_music")
    if not ds_visited_sport:
        $ set_zone_ds_small("sport_area", "ds_day2_pass_sl_sport")
    if not ds_visited_clubs:
        $ set_zone_ds_small("clubs", "ds_day2_pass_sl_clubs")
    if not ds_visited_library:
        $ set_zone_ds_small("library", "ds_day2_pass_sl_library")
    if not ds_visited_medic:
        $ set_zone_ds_small("medic_house", "ds_day2_pass_sl_medic")
    if (ds_passed_places == 3) and not ds_had_lunch:
        $ set_zone_ds_small("dining_hall", "ds_day2_pass_sl_lunch")
    $ show_small_map_ds()

label ds_day2_forged:
    scene bg ext_house_of_mt_day
    "Ты подходишь к домику Ольги Дмитриевны, как будто уже всё подписал."
    "Она как раз выходит."
    show mt surprise panama pioneer far at center with dspr
    mt "Cемён? Уже всё подписал? Так быстро?"
    me "Да."
    mt "Ну-ка давай-ка сюда."
    $ renpy.pause(1.0)
    show mt rage panama pioneer at center with dspr
    mt "Ты чего это надумал, обмануть меня?!"
    mt "Все подписи написаны одним почерком... {w}подозрительно напоминающим почерк Двачевской, кстати..."
    mt "Напротив библиотеки и медпункта должны стоять печати..."
    mt "И, наконец, главная в музклубе японка, а у них подписей нет, только опять же печати!"
    mt "Это совершенно не по-пионерски! Пионер не должен обманывать!"
    mt "Так, бери новый лист и дуй подписывать по-честному!"
    play sound ds_sfx_int
    dra "Увы, не вышло изобразить исполнительность и уйти от сией обязанности..."
    hide mt with dissolve
    "Она заходит в дом, и выходит с новым листом."
    $ renpy.pause(1.0)
    show mt angry panama pioneer at center with dissolve
    mt "Всё, иди!"
    hide mt with dissolve
    th "Печально, придётся идти подписывать... ещё и одному..."
    jump ds_day2_pass_alone_main

label ds_day2_pass_alone_music:
    play ambience ambience_camp_center_day fadein 3

    $ persistent.sprite_time = "day"
    scene bg ext_musclub_day 
    with dissolve

    window show
    "Музыкальный клуб располагается на некотором расстоянии от остальных построек лагеря."
    "Снаружи он представляет из себя небольшое одноэтажное здание."
    play sound ds_sfx_psy
    vol "Не раздумывая, ты заходишь."
    window hide

    stop ambience fadeout 2
    play sound sfx_open_door_2

    $ renpy.pause(1)

    $ persistent.sprite_time = "day"
    scene bg int_musclub_day 
    with dissolve

    play ambience ambience_music_club_day fadein 3

    window show
    play sound ds_sfx_int
    enc "Внутри оказывается полный набор музыкальных инструментов, на любой вкус и слух – барабаны, гитары и даже настоящий рояль."
    enc "Некоторое время твоё внимание плотно приковано к ним – хочется понять, из какого они примерно временного периода..."
    play sound ds_sfx_mot
    per_hea "Но неожиданно под роялем послышалось какое-то копошение."
    window hide

    scene cg ds_day2_mi_piano1
    with dissolve

    play music music_list["so_good_to_be_careless"] fadein 5
    $ ds_met['mi'] = 1

    window show
    "Ты наклоняешься и видишь девочку, которая, кажется, что-то искала."
    play sound ds_sfx_fys
    ins "Она стоит на четвереньках в такой пикантной позе..."
    window hide
    menu:
        "Сдержать порывы":
            window show
            me "Простите…"
        "Начать приставать":
            if skillcheck('instinct', lvl_trivial):
                window show
                ins "Внизу у тебя встаёт твой ствол..."
                ins "Ты подходишь к ней и прижимаешься ей к юбке..."
                play sound ds_sfx_mot
                res "Но она тебя замечает!"
            else:
                window show
                ins "Ты хочешь к ней пристать, но что-то идёт не так."
                ins "Извини."
                "Твои неуклюжие движения привлекают внимание девочки."
            $ ds_skill_points['instinct'] += 1
    window hide

    scene cg ds_day2_mi_piano2
    with dissolve

    window show
    mip "Ааа! Кто здесь?"
    window hide

    play sound sfx_piano_head_bump
    with vpunch

    $ renpy.pause(1)

    window show
    "Она пытается вскочить, но днище рояля стало для нее непреодолимой преградой."
    mip "Ой!"
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_musclub_day 
    with dissolve

    show mi shocked pioneer at center   with dissolve
    window show
    "С трудом, но она все же выбирается."
    me "Извини, что напугал…"
    show mi normal pioneer at center   with dspr
    mip "Да ничего! Вижу, у тебя обходной, новенький, значит?"
    me "А? Да."
    show mi smile pioneer at center   with dspr
    mip "Меня Мику зовут."
    $ ds_met['mi'] = 2
    play sound ds_sfx_int
    enc "Тебе её имя почему-то кажется знакомым."
    if skillcheck('encyclopedia', lvl_medium, passive=True):
        enc "Точно, Мику существует и в твоём мире..."
        enc "В качестве так называемого «вокалоида» - компьютерной программы, симулирующей голос певицы."
        enc "А тут вот, вполне реальная девочка."
        play sound ds_sfx_int
        rhe "Только ей об этом вообще не стоит говорить."
    else:
        enc "Нет, показалось. Ты никогда не слышал имени Мику."

    mi "Нет, честно-честно! Никто не верит, а меня правда так зовут. Просто у меня мама из Японии. Папа с ней познакомился, когда строил там… Ну, то есть не строил – он у меня инженер…"
    mi "Короче, атомную станцию! Или плотину… Или мост… Ну, неважно!"
    play sound ds_sfx_mot
    res "Она говорит с такой скоростью, что половину слов ты не успеваешь разбирать."
    menu:
        "Сделать комплимент":
            me "Да... а ты прекрасно выглядишь, кстати."
            $ ds_lp_mi += 1
            show mi shy pioneer at center with dspr
            mi "Что ты говоришь? Ты правда считаешь, что я прекрасно выгляжу? А впрочем, мне все так говорят. Я почему-то очень-очень привлекаю всех парней."
            show mi smile pioneer at center with dspr
            mi "Ой, а как тебя зовут, кстати? Наверное, у тебя и имя должно быть каким-нибудь красивым!"
        "Высказать насчёт болтливости":
            me "Слушай, а ты всегда такая болтливая?"
            show mi sad pioneer at center with dspr
            mi "Да, есть у меня такое, совсем-совсем не знаю, что с этим делать. Все-все из-за этого раздражаются, даже ты... а как тебя зовут, кстати?"
            $ ds_lp_mi -= 1
            $ ds_karma -= 5
            play sound ds_sfx_psy
            emp "Она старается изобразить, будто её вообще не задели твои слова, хотя это далеко не так."
        "Промолчать":
            pass
    me "А я Семен."
    show mi happy pioneer at center   with dspr
    mi "Отлично! Не хочешь к нам в клуб вступить? Правда, нас тут пока только двое: я и Алиса-тян, но вместе мы будем втроём! Ты на чем-нибудь играть умеешь?"
    th "Уже в период моего «отшельничества» я купил себе гитару и по самоучителям выучил пару аккордов, но потом забросил это дело, как и любое другое, которое требовало больше нескольких часов."
    play sound ds_sfx_int
    con "А тут ты наверняка сможешь подтянуть свои навыки и сыграть что-нибудь прекрасное!"
    menu:
        "Записаться":
            me "Да, давай!"
            mi "Отлично, сейчас я тебя запишу к нам, Семён-кун. Я так рада, что ты присоединился к нам. Алиса-тян наверняка тоже обрадуется!"
            play sound ds_pen
            "Она достаёт листок и вписывает туда твои имя..."
            mi "А фамилия у тебя какая? А, точно, давай обходной, его заодно подпишу и спишу фамилию!"
            queue sound ds_mi_sign
            queue sound ds_pen
            "Ты отдаёшь ей свой обходной, она ставит подпись (вернее, печать, как истинная японка) там и дописывает в список членов клуба твою фамилию."
            mi "Распишись тут, пожалуйста."
            play sound ds_sfx_mot
            per_eye "Ты просматриваешь список, теперь состоящий из трёх человек."
            per_eye "1. ХАЦУНЕ МИКУ, {w}2. ДВАЧЕВСКАЯ АЛИСА..."
            per_eye "И вот наконец ты видишь себя: 3. ПЁРСУНОВ СЕМЁН."
            play sound ds_pen
            "Ты ставишь свою подпись."
            mi "Как же отлично. Как-нибудь обязательно надо будет вместе что-нибудь сыграть! Как раз на прощальном концерте через восемь дней и сыграем!"
            me "Да..."
            $ ds_lp_mi += 1
            $ ds_skill_points['conceptualization'] += 1
            $ ds_music_member = True
        "Отказаться":
            me "Знаешь, я как-то не планировал особо…"
            show mi normal pioneer at center   with dspr
            mi "Да ладно тебе, я тебя научу играть! Хочешь на трубе, например? Или на скрипке? Я на всем умею, честно-честно."
            play sound ds_sfx_mot
            сom "Ты решаешь не спорить с девочкой-мультиинструменталистом, так как в ответ наверняка бы получил очередную пулеметную очередь из слов."
            me "Я подумаю, а пока не могла бы ты подписать?"
            show mi happy pioneer at center   with dspr
            mi "Да-да-да, конечно, давай! Ты заходи, не стесняйся! Я еще и пою хорошо! Послушаешь, как я пою японские народные песни. Ну, или, если не нравится, может, что-нибудь из современных шлягеров?"
            me "Обязательно…"
    me "А сейчас мне пора, извини."
    show mi shy pioneer at center   with dspr
    mi "Конечно, приходи непременно… а, подожди..."
    window hide

    stop ambience fadeout 2

    stop music fadeout 3

    menu:
        "Дослушать":
            window show
            "Ты останавливаешься в двери, чтобы дослушать Мику"
            show mi sad pioneer at center with dspr
            mi "У меня тут потерялась заколка, ты случайно не видел её? Мне она очень-очень дорога и важна!"
            me "Нет..."
            mi "Поищи её, пожалуйста, если найдёшь - отнеси сюда или в домик 13, мне правда она очень-очень нужна..."
            me "Ладно..."
            $ ds_lp_mi += 1
            $ ds_find_hairpin = True
            "И с этими словами ты выходишь."
            show mi happy pioneer at center with dspr
            mi "Cпасибо-спасибо большое, Семён-кун!"
            scene bg ext_musclub_day 
            with dissolve

            play ambience ambience_camp_center_day fadein 3
        "Идти дальше":
            $ renpy.pause(1)

            $ persistent.sprite_time = "day"
            scene bg ext_musclub_day 
            with dissolve

            play ambience ambience_camp_center_day fadein 3

            window show
            "Окончание ее фразы скрывается за закрытой дверью."
    if not ds_music_member:
        play sound ds_sfx_int
        con "С одной стороны, ты был бы не против вечерком посидеть побренчать на гитаре"
        play sound ds_sfx_mot
        com "Но в такой компании…"
    show dv normal pioneer close at center    with dissolve
    "Ты поворачиваешься, собираясь уходить, и сталкиваешься нос к носу с Алисой."
    "Она недобро смотрит на тебя."
    dv "Зачем пришел?"
    if ds_music_member:
        window hide
        menu:
            "Чтобы записаться":
                window show
                me "В музклуб записаться..."
                show dv smile pioneer close at center with dspr
                dv "А... неплохо."
                $ ds_lp_dv += 1
                dv "Записался?"
            "Чтобы подписать обходной":
                window show
                me "Обходной…"
                dv "Подписал?"
    else:
        me "Обходной…"
        dv "Подписал?"
    me "Да…"
    dv "Свободен!"
    hide dv  with dissolve
    "Она входит внутрь, а ты спешишь покинуть это место."
    window hide

    stop ambience fadeout 2

    $ ds_passed_places += 1
    $ ds_visited_music = True

    if ds_sl_gone:
        show sl normal pioneer at center with dissolve
        sl "А вот и я! Ну как, справился?"
        me "Да..."
        show sl smile pioneer at center with dspr
        sl "Пойдём дальше?"
        jump ds_day2_pass_sl_main

    jump ds_day2_pass_alone_main

label ds_day2_pass_alone_clubs:
    play ambience ambience_camp_center_day fadein 2

    $ persistent.sprite_time = "day"
    scene bg ext_clubs_day 
    with dissolve

    window show
    "Ты идёшь к зданию кружков."
    play sound ds_sfx_psy
    esp "По правде говоря, тебе никогда особо не доставляла удовольствия общественная работа."
    esp "В школе ты всегда под любым предлогом пытался пропустить субботники, в институте тебя никак не привлекал студенческий совет."
    esp "Тебя не интересовали секции бокса, авиамоделирования или кройки и шитья."
    esp "Так что сюда ты приходишь лишь с целью отметиться.{w} Хотя, может, и попробуешь записаться хоть тут, вдруг будет интересно."

    stop ambience fadeout 2

    "Ты открываешь дверь и входишь."
    window hide

    play sound sfx_open_door_clubs

    $ renpy.pause(1)

    $ persistent.sprite_time = "day"
    scene bg int_clubs_male_day 
    with dissolve

    play ambience ambience_clubs_inside_day fadein 3

    window show
    "Внутри никого нет."
    play sound ds_sfx_int
    con "Комната представляет из себя что-то наподобие берлоги юного робототехника – повсюду валялись какие-то провода, нехитрые платы, микросхемы, на столе стоит осциллограф."
    "Из соседнего помещения слышатся голоса, и через секунду в комнату вошли двое пионеров."
    show el normal pioneer at cleft 
    show sh normal pioneer at cright 
    with dissolve
    play sound ds_sfx_int
    enc "В одном ты узнаёшь Электроника, второй же тебе был незнаком."
    el "Привет, Семен! А мы тебя ждали."
    th "Кажется, он знает все и обо всех…"
    me "А чего вы меня ждали?"
    el "Ну как же, ты же пришел в наш клуб кибернетиков записываться, так?"
    "Он не дал тебе ответить."
    show el smile pioneer at cleft   with dspr
    el "Знакомься, это Шурик, он у нас главный!"

    me "А вас в клубе этом только двое, я так полагаю?"
    show el normal pioneer at cleft   with dspr
    el "Ну, можешь считать, что уже трое."
    "Шурик подходит к тебе и уверенно протянул руку."
    play sound ds_sfx_int
    enc "Его лицо тебе кажется почему-то знакомым."
    if skillcheck('encyclopedia', lvl_easy, passive=True):
        enc "Точно, он же вылитый Шурик из комедий Гайдая!"
    else:
        enc "Хотя нет, показалось..."
    show sh normal_smile pioneer at cright   with dspr
    sh "Добро пожаловать!"
    me "Угу…"
    show sh normal pioneer at cright   with dspr
    el "Давай я тебе тут все покажу!{w} Ты не стесняйся, располагайся."
    me "Да нет, ребята, я вообще-то…"
    show sh normal_smile pioneer at cright   with dspr
    sh "Всегда рады новым членам."
    play music ds_ussr_anthem fadein 2
    enc "Он сказал это так, что в голове у тебя невольно заиграл гимн Советского Союза."
    enc "Удивительно, но ты еще помнишь слова – в первом классе у тебя была тетрадка, на обратной стороне которой они были напечатаны."
    stop music fadeout 2
    menu:
        "Записаться":
            th "Впрочем, новые знакомства мне точно не помешают."
            me "Да, давайте, записывайте меня!"
            sh "Отлично. Давай, кстати, сюда обходной лист."
            play sound ds_pen
            "Ты отдаёшь обходной лист, они записывают тебя в какой-то список и подписывают тебе его."
            sh "Вот, распишись тут."
            play sound ds_sfx_mot
            per_eye "Итак, члены клуба..."
            per_eye "1. ДЕМЬЯНЕНКО АЛЕКСАНДР"
            per_eye "2. CЫРОЕЖКИН СЕРГЕЙ"
            play sound ds_sfx_mot
            res "Значит, настоящее имя Электроника - Сергей..."
            per_eye "А вот и ты: 3. ПЁРСУНОВ СЕМЁН"
            play sound ds_pen
            "Ты ставишь свою подпись."
            show el laugh pioneer at cleft with dspr
            el "Приветствуем нового члена клуба кибернетиков!"
            $ ds_cyber_member = True
            $ ds_skill_points['interfacing'] += 1
            "И тут в комнату кто-то входит."
        "Отказаться":
            me "Да нет, мне бы просто обходной лист подписать."
            show sh normal_smile pioneer at cright   with dspr
            show el grin pioneer at cleft   with dspr
            el "Так ты к нам запишись, и мы тебе его подпишем."
            "Он хитро улыбается."
            play sound ds_sfx_psy
            sug "Какой хитрец!"
            "Ты уже подготовился к длинной и нудной дискуссии, как вдруг в комнату кто-то входит."
    show el normal pioneer at left 
    show sh normal pioneer at right 
    show sl normal pioneer at center 
    with dissolve
    "Ты оборачиваешься и видишь Славю."
    sl "А, Семен! Надеюсь, они тут тебя не достают?"
    show sl angry pioneer at center   with dspr
    "Она строго смотрит на будущих светил отечественного роботостроения."
    sl "А то я их знаю – они могут!"
    if ds_cyber_member:
        me "Нет, я просто решил к ним записаться."
        show sl smile pioneer at center with dspr
        if ds_sl_gone:
            if not (ds_music_member or ds_sport_member):
                $ ds_lp_sl += 1
            sl "А, отлично. Тогда пойдём?"
        else:
            sl "А, отлично. Тогда я пойду!"
            hide sl with dissolve
    else:
        me "Да, понимаешь, на самом деле мне бы просто обходной подписать…"
        "Я решил воспользоваться ситуацией."
        show sl normal pioneer at center   with dspr
        sl "Так это не проблема, давай сюда."
        "Она взяла листок и подошла к Шурику."
        sl "Подписывай!"
        show sh upset pioneer at right   with dspr
        sh "Ну подожди, мы еще не закончили…"
        show sl angry pioneer at center   with dspr
        sl "Закончили! Подписывай!"
        play sound ds_sfx_psy
        emp "Она посмотрела на него так, что возражать Шурик не решается."

        stop ambience fadeout 2
        play sound ds_pen
        if ds_sl_gone:
            "Он поставил свою закорючку, ты благодаришь Славю, и вы со ней уходите."
        else:
            "Он поставил свою закорючку, и ты, поблагодарив Славю, с чистой совестью направляешься дальше."
    window hide

    $ ds_passed_places += 1
    $ ds_visited_clubs = True

    if ds_sl_gone:
        jump ds_day2_pass_sl_main

    jump ds_day2_pass_alone_main

label ds_day2_pass_alone_medic:
    $ persistent.sprite_time = "day"
    scene bg ext_aidpost_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    window show
    play sound ds_sfx_fys
    edr "Ты решительно не понимаешь, что тебе делать в медпункте."
    edr "Здоровье вроде не шалит, тем более местный свежий воздух явно пошел тебе на пользу, и самочувствие было куда бодрее, чем обычно."
    th "Но раз надо так надо."
    "Ты входишь."
    window hide

    stop ambience fadeout 2

    play sound sfx_open_door_1

    $ renpy.pause(1)

    $ persistent.sprite_time = "day"
    scene bg int_aidpost_day 
    with dissolve

    play ambience ambience_medstation_inside_day fadein 3

    window show
    th "Обычный такой медпункт, у нас в школе был примерно такой же."
    show cs normal stethoscope at center   with dissolve

    play music ds_cs_theme fadein 5

    "За столом сидит женщина средних лет."
    "Она бросает на меня пристальный, оценивающий взгляд, и продолжила что-то писать."
    csp "Ну, здравствуй… пионер."
    "Говорит она, не отрываясь от своего занятия."
    me "Добрый день… Мне бы вот…"
    csp "Ты присаживайся."
    "Ты оглядываешь комнату."
    csp "На кушеточку."
    "Ты садишься."
    csp "Раздевайся."
    "Все это она говорит совершенно ровным тоном."
    me "А зачем?.."
    csp "Смотреть тебя будем, слушать, здоровье проверять."
    show cs smile stethoscope at center   with dspr
    csp "Меня, кстати, зовут Виолетта Церновна, но ты меня можешь звать просто Виолой."

    "Она поворачивается в твою сторону."
    cs "Ну, чего сидишь? Раздевайся."
    me "Да я не жалуюсь ни на что. Мне бы вот…"
    "Ты аккуратно протягиваешь ей листок."
    cs "Потом."
    show cs smile at center   with dissolve
    "Она снимает с шеи стетоскоп и, кажется, намеревается тебя им препарировать."
    window hide

    stop music fadeout 3
    play sound sfx_knock_door7_polite

    $ renpy.pause(1)

    window show
    "Но тут в дверь постучали."
    show cs normal at center   with dspr
    cs "Входите!"
    play sound ds_sfx_psy
    emp "Она ответила нехотя."

    play sound sfx_open_door_strong
    play music music_list['eternal_longing'] fadein 5

    "Моментально дверь распахнулась, и в комнату вбегает Электроник."
    show el fingal pioneer far at left    with dissolve   
    show cs normal at center   with dspr
    el "Здрасьте! Я тут это… На футболе упал. Глупости, конечно, я бы и так, но меня Ольга Дмитриевна…"
    "У Электроника под глазом красуется здоровенный фингал."
    play sound ds_sfx_int
    vic "Что-то сомнительно, что такой можно заработать на футболе."
    cs "Садись, сейчас посмотрим."
    show cs normal glasses at center   with dissolve
    cs "А ты давай сюда свой обходной."
    queue sound ds_pen
    queue sound ds_stamp
    "Медсестра быстро подписывает его, ставит печать и продолжает:"
    show cs smile glasses at center   with dspr
    cs "Если что заболит – сразу ко мне… пионер."

    stop ambience fadeout 2
    stop music fadeout 3

    "Ты ничего не отвечаешь и выходишь, закрыв за собой дверь."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_aidpost_day 
    with dissolve

    window show
    if ds_sl_gone:
        show sl normal pioneer at center with dissolve
        sl "А вот и я!"
        sl "Ну как, всё хорошо?"
        me "Медсестра здесь, конечно, еще та…"
        sl "Да, есть такое..."
    else:
        th "Медсестра здесь, конечно, еще та…"
    $ ds_skill_points['instinct'] += 1
    window hide

    $ ds_passed_places += 1
    $ ds_visited_medic = True
    if ds_sl_gone:
        jump ds_day2_pass_sl_main
    jump ds_day2_pass_alone_main

label ds_day2_pass_alone_library:
    play ambience ambience_camp_center_day fadein 3
    $ persistent.sprite_time = "day"
    scene bg ext_library_day 
    with dissolve

    window show
    play sound ds_sfx_psy
    vol "Вообще, ты, конечно, любишь читать, но просиживать днями в библиотеке при нынешних обстоятельствах в твои планы не входит, так что ты решил побыстрее пройти этот чекпойнт."
    window hide

    stop ambience fadeout 3

    $ persistent.sprite_time = "day"
    scene bg int_library_day 
    with dissolve

    play ambience ambience_library_day fadein 3

    window show
    play sound ds_sfx_psy
    ine "Когда ты заходишь внутрь, у тебя в голове всплывает воспоминание из детства."
    ine "Оно очень яркое."
    ine "Тебе лет 7 или 8, ты с мамой в библиотеке."
    ine "Пока она выбирает какие-то книжки, которые тебе понадобятся для учебы, ты сидишь и разглядываешь местную подборку комиксов."
    ine "Тогда тебе было сложно понять, почему их здесь так много и почему нельзя забрать часть домой."
    ine "Понятия коллективной собственности тогда для тебя не существовало."
    ine "Впрочем, как и понятия собственности вообще."
    ine "Тем более странным было это воспоминание сейчас, когда ты находишься в том самом отдельно взятом пионерлагере, где коммунизм таки удалось построить за 3 года."
    "Повсюду висит огромное количество советской символики, а на полках книги в основном соответствующей тематики."
    vol "Читать их ты никак не планировал – знакомство с полным собранием сочинений Маркса было одной из последних вещей на Земле, которая пришла бы тебе в голову."
    vol "Надо найти библиотекаря."
    "Оказалось это не так сложно – она спит на столе рядом с тобой."
    window hide

    scene cg d2_micu_lib 
    with dissolve

    window show
    "Ты пригляделся.{w} Короткая стрижка, толстые очки, довольно приятное лицо."
    $ ds_met['mz'] = 1
    play sound ds_sfx_psy
    th "Она так мило спит..."
    window hide
    menu:
        "Разбудить":
            me "Проснитесь, мне надо подписать обходной лист."
            scene bg int_library_day 
            with dissolve
            show mz bukal pioneer at center with dspr
            mzp "А... что такое... дайте поспать..."
            "И она снова погружается в сон."
            hide mz with dissolve
        "Не будить":
            th "Пожалуй, подожду, если через полчаса не проснется, тогда уж что поделать…"
            window hide

            $ persistent.sprite_time = "day"
            scene bg int_library_day 
            with dissolve
            menu:
                "Почитать":
                    $ ds_read_book = True
                    window show
                    "Просто так сидеть было скучно, и ты берёшь с полки первую попавшуюся книгу."
                    "Артур Шопенгауэр, «Мир как воля и представление»."
                    "Ты открываешь примерно на середине и начинаешь читать:"
                    window hide

                    $ set_mode_nvl()

                    window show
                    nvl clear
                    "Жизнь человека с ее бесконечными трудами, нуждой и страданием следует рассматривать как объяснение и парафраз акта зачатия, т.е. решительного утверждения воли к жизни; с этим связано и то, что человек обязан природе смертью и с тоской думает об этом обязательстве."
                    "Разве это не свидетельствует о том, что в нашей жизни заключена некая вина?"
                    "И тем не менее, периодически расплачиваясь смертью за рождения и смерти, мы всегда существуем и испытываем все горести и радости жизни попеременно, когда ни одна из них не может нас миновать: таков результат утверждения воли к жизни."
                    "При этом страх смерти, который, несмотря на все страдания жизни, удерживает нас в ней, становится, в сущности, иллюзией; но столь же иллюзорно и влечение, заманившее нас в жизнь."
                    "Объективное выражение этого соблазна можно увидеть в обращенных друг на друга страстных взглядах влюбленных: они есть чистейшее выражение воли к жизни в ее утверждении. Как она здесь кротка и нежна!"
                    "Она хочет благополучия, спокойного наслаждения и тихой радости для себя, для других, для всех."
                    window hide

                    $ set_mode_adv()
                "Просто посидеть":
                    window show
                    "Ты садишься и просто ждёшь."
                    window hide

    play sound sfx_knock_door2

    window show
    "В дверь стучат."
    if ds_read_book:
        "Ты быстро закрываешь книгу и кладёшь ее на место."
    th "Какая отличная привычка – стучать.{w} Надо и мне ее взять на вооружение."

    play sound sfx_open_door_clubs_2

    "В дверь входит Лена."
    show un normal pioneer at cleft   with dissolve
    un "Ой…"
    show un shy pioneer at cleft   with dspr
    me "Привет!"
    "Ты улыбаешься."
    un "Привет, а я вот книжку пришла отдать…"
    "У нее в руках была «Унесенные ветром», которую ты видел вчера."
    un "Ой, а Женя спит, тогда я попозже зайду…"
    $ ds_met['mz'] = 2
    mz "Уже не сплю."
    show mz normal glasses pioneer far at cright    with dissolve
    "Ты удивленно смотришь в сторону библиотекарши."
    "Она сидит за столом и пристально наблюдает за мной."
    show mz angry glasses pioneer far at cright   with dspr
    mz "А тебе чего?"
    me "Мне бы обходной…"
    show mz normal glasses pioneer at cright   with dissolve
    mz "Давай."
    queue sound ds_pen
    queue sound ds_stamp
    "Она быстро расписывается, ставит печать и протягивает тебе его обратно."
    mz "Получать читательский билет будем?"
    menu:
        "Согласиться":
            me "Да, давай...те."
            "Женя залезает в стол, достаёт какой-то листок..."
            mz "Фамилия, имя?"
            me "Пёрсунов Семён..."
            play sound ds_pen
            "Она записывает сведения в билет, а затем отдаёт тебе."
            mz "Бери!"
            "Ты забираешь бумажку и складываешь в карман штанов."
            $ ds_library_member = True
            $ ds_skill_points['encyclopedia'] += 1
            mz "Cледующий!"
        "Отказаться":
            me "Нет, спасибо."
            mz "Тогда следующий!"
    play sound ds_sfx_psy
    emp "Вид у нее такой, что дальнейший разговор кажется совершенно неуместным."
    "Лена подходит к ней и отдаёт книжку, а ты благодаришь Женю и выходишь."
    window hide

    stop ambience fadeout 2

    $ ds_passed_places += 1
    $ ds_visited_library = True

    if ds_sl_gone:
        scene bg ext_library_day with dissolve
        show sl normal pioneer at center with dissolve
        sl "А вот и я! Ну как, справился?"
        me "Да..."
        show sl smile pioneer at center with dspr
        sl "Пойдём дальше?"
        jump ds_day2_pass_sl_main

    jump ds_day2_pass_alone_main

label ds_day2_pass_alone_lunch:
    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_away_day 
    with dissolve

    window show
    "Ты решаешь всё же выкроить время, чтобы сходить пообедать."
    th "Обходной лист никуда не денется, потом быстренько подпишу, а вот мой желудок явно ждать до ужина не намерен."
    "С такими мыслями ты входишь в столовую."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_day 
    with dissolve

    play ambience ambience_dining_hall_empty fadein 3

    window show
    "Там почти никого нет – видимо, большинство пионеров уже пообедало."
    "Ты встаёшь в очередь за едой."
    "Впрочем, очередью это назвать нельзя, ибо ты там один."
    show ck normal at center with dissolve
    "Внушающая уважение своими габаритами повариха выдаёт тебе шикарный обед из трех блюд: суп «Ипрская похлебка», гуляш «от Лаврентия Палыча» с гарниром из картошки, сваренной, видимо, по рецептам конца XV века, и компот «Таблица Менделеева»."
    hide ck with dissolve
    play sound ds_sfx_fys
    edr "Такому меню позавидовали бы и лучшие рестораны мира, но тебе все равно, ибо есть хотелось сильно."
    edr "А по сравнению с твоими обычными пельменями, приправленными макаронами и дошираком, и такой обед кажется весьма неплохим."
    scene bg ds_int_dininghall_table1_day with dissolve
    "Ты садишься за первый попавшийся стол и принимаешься сосредоточенно есть."
    window hide

    play sound sfx_punch_medium
    with vpunch

    play music music_list["eat_some_trouble"] fadein 5

    $ renpy.pause(1)

    window show
    play sound ds_sfx_fys
    pat "Однако сосредоточенность твоя продлилась недолго – кто-то ударил тебя по спине, да так, что ты подавился."
    show us laugh pioneer at center   with dissolve
    "Ты оборачиваешься и видишь Ульянку."
    window hide
    menu:
        "Отреагировать":
            window show
            me "Я тебя когда-нибудь удушу!"
            show us laugh2 pioneer at center   with dspr
            us "Не догонишь!"
            "Она показывает тебе язык!"
            show us grin pioneer at center   with dspr
            if not ds_caught_us:
                us "Один раз уже пытался – не догнал же."
            me "Хорошо, тогда я тебя где-нибудь подкараулю!"
            show us surp2 pioneer at center   with dspr
            us "Так нечестно!"
            me "Ты на себя посмотри, честная!"
            "Ты ухмыляешься."
        "Игнорировать":
            if skillcheck('composure', lvl_challenging):
                window show
                play sound ds_sfx_mot
                com "Ты делаешь вид, будто ничего не происходит и углубляешься в обед."
                $ ds_skill_points['composure'] += 1
                $ ds_lp_us -= 1
                show us dontlike pioneer at center with dspr
                us "Эй, я тут! Ответь!"
            else:
                window show
                play sound ds_sfx_mot
                com "Ты бы и хотел сделать вид, что её нет, но она тебя слишком уж раздражает."
                me "Я тебя когда-нибудь удушу!"
                show us laugh2 pioneer at center   with dspr
                us "Не догонишь!"
                "Она показывает тебе язык!"
                show us grin pioneer at center   with dspr
                if not ds_caught_us:
                    us "Один раз уже пытался – не догнал же."
                me "Хорошо, тогда я тебя где-нибудь подкараулю!"
                show us surp2 pioneer at center   with dspr
                us "Так нечестно!"
                me "Ты на себя посмотри, честная!"
                "Ты ухмыляешься."
    show us laugh pioneer at center   with dspr
    us "Ладно, подожди, сейчас обед возьму и подойду, вместе поедим."
    hide us  with dissolve
    play sound ds_sfx_fys
    hfl "Перспектива не самая радужная, поэтому ты стараешься побыстрее закончить."
    "Однако тебе это не удаётся, так как Ульянка вернулась буквально через полминуты."
    show us smile pioneer at center   with dspr
    "На ее тарелке лежит огромный кусок жареного мяса и несколько отварных картофелин."
    play sound ds_sfx_mot
    res "По сравнению с твоей королевской трапезой…"
    me "Это ты как?.. Откуда?.."
    show us laugh2 pioneer at center   with dspr
    us "Уметь надо!"
    "Она смотрит на тебя и улыбается во все свои 32… или сколько их у нее там было… зуба."
    play sound ds_sfx_psy
    aut "Такого оскорбления ты никак стерпеть не можешь!"
    aut "Ты никогда не умел толком над кем-то подшучивать, да и в школе больше прикалывались над тобой."
    aut "Однако ты чувствуешь, что просто необходимо ей чем-то отомстить."
    window hide
    menu:
        "Подшутить":
            if skillcheck('drama', lvl_easy):
                window show
                me "А что если Ольга Дмитриевна узнает, что ты воруешь еду?"
                show us surp3 pioneer at center   with dspr
                us "Так я не ворую!"
                me "А вот это ты ей будешь рассказывать. Думаешь, поверит?"
                show us surp2 pioneer at center   with dspr
                us "Ты же не собираешься ей меня закладывать?!"
                me "Ну… это зависит от многих обстоятельств."
                show us calml pioneer at center   with dspr
                us "Например?"
                "Она внимательно смотрит на тебя."
                me "Принеси мне булочку. Сладкую."
                show us shy2 pioneer at center   with dspr
                us "Откуда же я тебе ее возьму?"
                me "Наверное, оттуда же, где взяла это."
                "Ты показываешь на ее тарелку."
                show us dontlike pioneer at center   with dspr
                us "Ладно. Но только одну!"
                show us surp2 pioneer at center   with dspr
                us "И обещай, что после этого не расскажешь Ольге Дмитриевне!"
                me "Слово пионера!"
                hide us  with dissolve
                "Она убегает в сторону буфета, а ты, недолго думая, берёшь перечницу, откручиваешь крышку и высыпаешь все содержимое ей в компот."
                "Только ты успеваешь поставить ее на место, как Ульяна возвращается."
                show us laugh pioneer at center   with dissolve
                me "Держи, вымогатель!"
                th "Кажется, она ничего не заметила."
                me "А теперь давай кто быстрее выпьет компот!"
                show us surp2 pioneer at center   with dspr
                us "Что еще за глупости!"
                me "Почему глупости? Я выиграю, вот увидишь!"
                show us dontlike pioneer at center   with dspr
                us "Не буду я с тобой в детские игры играть."
                me "Сама-то не ребенок разве?"
                "Ты ехидно улыбаешься."
                play sound ds_sfx_psy
                emp "Но она подвоха не замечает."
                show us angry pioneer at center   with dspr
                us "Ах так! Ладно! Раз, два, три!"
                "Она не даёт тебе времени даже взять чашку, а сама моментально, одним глотком, выпивает весь свой компот."
                window hide

                show bg int_dining_hall_day :
                    linear 0.1 pos (-5,-5)
                    linear 0.1 pos (0,0)
                    linear 0.1 pos (5,5)
                    linear 0.1 pos (0,5)
                    linear 0.1 pos (5,0)
                    linear 0.1 pos (0,0)
                    repeat 10
                with flash_red

                stop music fadeout 0

                show us fear pioneer at center   with dspr

                play sound sfx_angry_ulyana

                $ renpy.pause(5)

                window show
                "Через секунду у нее на лице появляется выражение первобытного ужаса, щеки краснеют, а глаза, кажется, готовы вылезти из орбит."
                hide us  with dissolve
                "Она вскакивает и бежит в сторону чайников с водой, на ходу выкрикивая:"
                us "Ты! Ты! Ты…"

                stop ambience fadeout 2

                "Ты решаешь не дожидаться, пока она придет в себя и, посмеиваясь, выходишь из столовой, на ходу доедая булочку."
                window hide
                $ ds_lp_us += 1
                $ ds_skill_points['authority'] += 1
                $ ds_skill_points['drama'] += 1
            else:
                dra "Но у вас совсем нет идей, как бы подшутить, мессир."
                $ ds_skill_points['drama'] += 1
                "Ты быстро съедаешь всю еду и уходишь."
                show us dontlike pioneer at center with dspr
                us "Эй, ты куда?"
                me "Обходной подписывать!"
                "И, не выслушивая её дальше, ты уходишь."
        "Не подшучивать":
            "Ты быстро съедаешь всю еду и уходишь."
            show us dontlike pioneer at center with dspr
            us "Эй, ты куда?"
            me "Обходной подписывать!"
            "И, не выслушивая её дальше, ты уходишь."
            $ ds_semtype -= 1
    $ ds_had_lunch = True
    jump ds_day2_pass_alone_main

label ds_day2_pass_alone_sport:
    scene bg ext_playground_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    window show
    "Ты подходишь к спортплощадке."
    "Не увидев никого, ты решаешь было уйти..."
    play sound ds_sfx_mot
    per_eye "Подожди, тут же есть и здание, по всей видимости, спортзал."
    "Ты направляешься туда."
    scene bg ds_int_sporthall_day with dissolve
    show us smile sport far at center with dspr
    "Зайдя в спортзал, ты видишь Ульяну бегающей по залу."
    me "Ульяна, а где я тут могу подписать обходной лист?"
    us "Давай его сюда!"
    show us laugh sport at center with dspr
    play sound ds_sfx_int
    dra "По всей видимости, она опять хочет вас провести."
    us "Я тут спортклубом руковожу!"
    play sound ds_sfx_mot
    res "Так ей же не более 14 лет! И уже руководит чем-то?"
    menu:
        "Принять":
            me "А... хорошо."
        "Усомниться":
            me "Ты? Ты же ещё маленькая!"
            show us dontlike sport at center with dspr
            us "И ничего не маленькая! Мне сама Ольга Дмитриевна доверила!"
            $ ds_lp_us -= 1
    show us normal sport at center with dspr
    us "Кстати, не хочешь записаться к нам?"
    if not ds_caught_us:
        show us laugh2 sport at center with dspr
        us "Может, и сможешь меня тогда догнать!"
    window hide
    menu:
        "Записаться":
            window show
            me "Давай!"
            show us smile sport at center with dspr
            us "Вот, бери листик и записывайся сюда!"
            "Ты вносишь своё имя в данный тебе клочок бумаги."
            me "Вот, а теперь подпиши мне обходной."
            us "Давай сюда!"
            play sound ds_pen
            "Она подписывает обходной и отдаёт лист тебе."
            play sound ds_sfx_mot
            per_eye "СОВЕТОВА У.И. {w}Теперь мы знаем её фамилию!"
            me "Cпасибо!"
            show us laugh sport
            us "Только не забывай регулярно приходить сюда!"
            $ ds_sport_member = True
            $ ds_lp_us += 1
            "Под эти слова ты выходишь из зала."
        "Отказаться":
            window show
            me "Нет, спасибо... мне просто нужен обходной лист."
            show us dontlike sport at center with dspr
            us "Ну и ладно, давай сюда свою бумажку!"
            play sound ds_pen
            "Она подписывает обходной и отдаёт лист тебе."
            play sound ds_sfx_mot
            per_eye "СОВЕТОВА У.И. {w}Теперь мы знаем её фамилию!"
            me "Cпасибо!"
            "И ты уходишь."
    $ ds_passed_places += 1
    $ ds_visited_sport = True
    if ds_sl_gone:
        scene bg ext_playground_day with dissolve
        show sl normal pioneer at center with dissolve
        sl "А вот и я! Ну как, справился?"
        me "Да..."
        show sl smile pioneer at center with dspr
        sl "Пойдём дальше?"
        jump ds_day2_pass_sl_main

    jump ds_day2_pass_alone_main

label ds_day2_pass_dv_music:
    play ambience ambience_camp_center_day fadein 3

    $ persistent.sprite_time = "day"
    scene bg ext_musclub_day 
    with dissolve

    if (ds_passed_places >= 3) and not ds_had_lunch:
        show dv angry pioneer2 at center with dspr
        dv "Так, всё, я обедать!"
        dv "Я тебе ясно сказала, что пора обедать, а ты проигнорировал!"
        dv "Дальше подписывай свой лист сам!"
        hide dv with dissolve
        $ ds_lp_dv -= 1
        play sound ds_sfx_int
        lgc "Дальше тебе придётся подписывать лист одному."
        jump ds_day2_pass_alone_music

    show dv normal pioneer2 at center with dissolve

    window show
    "Музыкальный клуб располагается на некотором расстоянии от остальных построек лагеря."
    "Снаружи он представляет из себя небольшое одноэтажное здание."
    play sound ds_sfx_psy
    vol "Не раздумывая, вы заходите."
    window hide

    stop ambience fadeout 2
    play sound sfx_open_door_2

    $ renpy.pause(1)

    $ persistent.sprite_time = "day"
    scene bg int_musclub_day 
    with dissolve

    show dv normal pioneer2 at center with dspr

    play ambience ambience_music_club_day fadein 3

    window show
    play sound ds_sfx_int
    enc "Внутри оказывается полный набор музыкальных инструментов, на любой вкус и слух – барабаны, гитары и даже настоящий рояль."
    enc "Некоторое время твоё внимание плотно приковано к ним – хочется понять, из какого они примерно временного периода..."
    play sound ds_sfx_mot
    per_hea "Но неожиданно под роялем послышалось какое-то копошение."
    window hide

    scene cg ds_day2_mi_piano1
    with dissolve
    $ ds_met['mi'] = 1
    play music music_list["so_good_to_be_careless"] fadein 5

    window show
    "Ты наклоняешься и видишь девочку, которая, кажется, что-то искала."
    play sound ds_sfx_fys
    ins "Она стоит на четвереньках в такой пикантной позе, что ты останавливаешься и хочешь пристать к ней..."
    dv "Так, Мику, вылезай, у нас тут срочное дело!"
    $ ds_met['mi'] = 2
    window hide

    scene cg ds_day2_mi_piano2
    with dissolve

    window show
    mi "Ааа! Кто здесь?"
    window hide

    play sound sfx_piano_head_bump
    with vpunch

    $ renpy.pause(1)

    window show
    "Она пытается вскочить, но днище рояля стало для нее непреодолимой преградой."
    mi "Ой!"
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_musclub_day 
    with dissolve

    show dv grin pioneer2 at fright with dissolve
    show mi shocked pioneer at center   with dissolve
    window show
    "С трудом, но она все же выбирается."
    me "Извини, что напугали…"
    show mi normal pioneer at center   with dspr
    mip "Да ничего! Вижу, у тебя обходной, новенький, значит?"
    play sound ds_sfx_mot
    res "Ты хотел было ответить, но Алиса опережает."
    show dv normal pioneer2 at fright with dspr
    dv "Да, у него обходной, так что подпиши быстрее!"
    show mi smile pioneer at center   with dspr
    mip "Меня Мику зовут."
    play sound ds_sfx_int
    enc "Тебе её имя почему-то кажется знакомым."
    if skillcheck('encyclopedia', lvl_medium, passive=True):
        enc "Точно, Мику существует и в твоём мире..."
        enc "В качестве так называемого «вокалоида» - компьютерной программы, симулирующей голос певицы."
        enc "А тут вот, вполне реальная девочка."
        play sound ds_sfx_int
        rhe "Только ей об этом вообще не стоит говорить."
    else:
        enc "Нет, показалось. Ты никогда не слышал имени Мику."

    mi "Нет, честно-честно! Никто не верит, а меня правда так зовут. Просто у меня мама из Японии. Папа с ней познакомился, когда строил там… Ну, то есть не строил – он у меня инженер…"
    mi "Короче, атомную станцию! Или плотину… Или мост… Ну, неважно!"
    show dv angry pioneer2 at fright with dspr
    dv "Мы поняли! Обходной!"
    play sound ds_sfx_mot
    res "Она говорит с такой скоростью, что половину слов ты не успеваешь разбирать."
    menu:
        "Сделать комплимент":
            me "Да... а ты прекрасно выглядишь, кстати."
            $ ds_lp_mi += 1
            show mi shy pioneer at center with dspr
            show dv rage pioneer at fright with dspr
            dv "Что ты несёшь?!"
            $ ds_lp_dv -= 1
            mi "Что ты говоришь? Ты правда считаешь, что я прекрасно выгляжу? А впрочем, мне все так говорят. Я почему-то очень-очень привлекаю всех парней."
            show mi smile pioneer at center with dspr
            mi "Ой, а как тебя зовут, кстати? Наверное, у тебя и имя должно быть каким-нибудь красивым!"
        "Высказать насчёт болтливости":
            me "Слушай, а ты всегда такая болтливая?"
            show mi sad pioneer at center with dspr
            mi "Да, есть у меня такое, совсем-совсем не знаю, что с этим делать. Все-все из-за этого раздражаются, даже ты... а как тебя зовут, кстати?"
            $ ds_lp_mi -= 1
            $ ds_karma -= 5
            play sound ds_sfx_psy
            emp "Она старается изобразить, будто её вообще не задели твои слова, хотя это далеко не так."
            dv "Мы уже подпишем обходной когда-нибудь?!"
        "Промолчать":
            pass
    me "А я Семен."
    show mi happy pioneer at center   with dspr
    mi "Отлично! Не хочешь к нам в клуб вступить? Правда, нас тут пока только двое: я и Алиса-тян, но вместе мы будем втроём! Ты на чем-нибудь играть умеешь?"
    show dv grin pioneer2 at fright with dspr
    dv "Кстати, да. Ты хоть на чём-нибудь играть умеешь?"
    th "Уже в период моего «отшельничества» я купил себе гитару и по самоучителям выучил пару аккордов, но потом забросил это дело, как и любое другое, которое требовало больше нескольких часов."
    play sound ds_sfx_int
    con "А тут ты наверняка сможешь подтянуть свои навыки и сыграть что-нибудь прекрасное!"
    menu:
        "Записаться":
            me "Да, давай!"
            show dv smile pioneer2 at fright with dspr
            dv "О, наш человек!"
            $ ds_lp_dv += 1
            mi "Отлично, сейчас я тебя запишу к нам, Семён-кун. Я так рада, что ты присоединился к нам. Алиса-тян наверняка тоже обрадуется!"
            play sound ds_pen
            "Она достаёт листок и вписывает туда твои имя..."
            mi "А фамилия у тебя какая? А, точно, давай обходной, его заодно подпишу и спишу фамилию!"
            queue sound ds_mi_sign
            queue sound ds_pen
            "Ты отдаёшь ей свой обходной, она ставит подпись (вернее, печать, как истинная японка) там и дописывает в список членов клуба твою фамилию."
            mi "Распишись тут, пожалуйста."
            play sound ds_sfx_mot
            per_eye "Ты просматриваешь список, теперь состоящий из трёх человек."
            per_eye "1. ХАЦУНЕ МИКУ, {w}2. ДВАЧЕВСКАЯ АЛИСА..."
            per_eye "И вот наконец ты видишь себя: 3. ПЁРСУНОВ СЕМЁН."
            play sound ds_pen
            "Ты ставишь свою подпись."
            mi "Как же отлично. Как-нибудь обязательно надо будет вместе что-нибудь сыграть! Как раз на прощальном концерте через восемь дней и сыграем!"
            dv "Да, и ты теперь тоже будешь играть с нами. И только попробуй отвертеться!"
            me "Да..."
            $ ds_lp_mi += 1
            $ ds_skill_points['conceptualization'] += 1
            $ ds_music_member = True
        "Отказаться":
            me "Знаешь, я как-то не планировал особо…"
            show mi normal pioneer at center   with dspr
            show dv normal pioneer2 at fright with dspr
            dv "И почему я не удивлена?"
            mi "Да ладно тебе, я тебя научу играть! Хочешь на трубе, например? Или на скрипке? Я на всем умею, честно-честно."
            dv "Подпиши уже ему обходной, и мы пойдём!"
            play sound ds_sfx_mot
            сom "Ты решаешь не спорить с девочкой-мультиинструменталистом, так как в ответ наверняка бы получил очередную пулеметную очередь из слов."
            me "Я подумаю, а пока не могла бы ты подписать?"
            show mi happy pioneer at center   with dspr
            mi "Да-да-да, конечно, давай! Ты заходи, не стесняйся! Я еще и пою хорошо! Послушаешь, как я пою японские народные песни. Ну, или, если не нравится, может, что-нибудь из современных шлягеров?"
            me "Обязательно…"
    dv "Всё, мы пошли, поговорим потом!"
    show mi shy pioneer at center   with dspr
    mi "Конечно, приходите непременно… а, подождите..."
    window hide

    stop ambience fadeout 2

    stop music fadeout 3

    menu:
        "Дослушать":
            window show
            "Ты останавливаешься в двери, чтобы дослушать Мику"
            show dv angry pioneer2 at fright with dspr
            show mi sad pioneer at center with dspr
            dv "Что ещё?"
            mi "У меня тут потерялась заколка, ты случайно не видел её? Мне она очень-очень дорога и важна!"
            me "Нет..."
            mi "Поищи её, пожалуйста, если найдёшь - отнеси сюда или в домик 13, мне правда она очень-очень нужна..."
            me "Ладно..."
            $ ds_lp_mi += 1
            $ ds_find_hairpin = True
            "И с этими словами ты выходишь."
            show mi happy pioneer at center with dspr
            mi "Cпасибо-спасибо большое, Семён-кун!"
            scene bg ext_musclub_day 
            with dissolve
            show dv angry pioneer2 at center with dspr
            dv "Но сейчас я никуда ничего искать не пойду! Потом поищешь!"
            dv "Мы так твою бумажку до вечера подписывать будем!"

            play ambience ambience_camp_center_day fadein 3
        "Идти дальше":
            $ renpy.pause(1)

            $ persistent.sprite_time = "day"
            scene bg ext_musclub_day 
            with dissolve
            show dv normal pioneer2 at center with dspr

            play ambience ambience_camp_center_day fadein 3

            window show
            "Окончание ее фразы скрывается за закрытой дверью."
    if not ds_music_member:
        play sound ds_sfx_int
        con "С одной стороны, ты был бы не против вечерком посидеть побренчать на гитаре"
        play sound ds_sfx_mot
        com "Но в такой компании…"
    else:
        show dv normal pioneer2 at center with dspr
        dv "А ты всё-таки музыкой интересуешься. Не ожидала от тебя."
        dv "Возможно, из тебя и выйдет толк."
        dv "Чтоб поучаствовал в нашем выступлении, а то лично тебя урою, понял?"
        show dv laugh pioneer2 at center with dspr
        $ renpy.pause(0.5)
        me "Да..."
    window hide

    stop ambience fadeout 2

    $ ds_passed_places += 1
    $ ds_visited_music = True
    jump ds_day2_pass_dv_main

label ds_day2_pass_dv_clubs:
    play ambience ambience_camp_center_day fadein 2

    $ persistent.sprite_time = "day"
    scene bg ext_clubs_day 
    with dissolve

    if (ds_passed_places >= 3) and not ds_had_lunch:
        show dv angry pioneer2 at center with dspr
        dv "Так, всё, я обедать!"
        dv "Я тебе ясно сказала, что пора обедать, а ты проигнорировал!"
        dv "Дальше подписывай свой лист сам!"
        hide dv with dissolve
        $ ds_lp_dv -= 1
        play sound ds_sfx_int
        lgc "Дальше тебе придётся подписывать лист одному."
        jump ds_day2_pass_alone_clubs

    window show
    "Вы подходите к зданию кружков."
    play sound ds_sfx_psy
    esp "По правде говоря, тебе никогда особо не доставляла удовольствия общественная работа."
    esp "В школе ты всегда под любым предлогом пытался пропустить субботники, в институте тебя никак не привлекал студенческий совет."
    esp "Тебя не интересовали секции бокса, авиамоделирования или кройки и шитья."
    esp "Так что сюда ты приходишь лишь с целью отметиться.{w} Хотя, может, и попробуешь записаться хоть тут, вдруг будет интересно."
    show dv sad pioneer2 at center with dspr
    dv "Сюда нам тоже надо?"
    me "Ну да..."
    show dv angry pioneer2 at center with dspr
    dv "Ну, значит, набью я морду тут кое-кому..."
    play sound ds_sfx_fys
    hfl "Какая опасная женщина... серьёзно."

    stop ambience fadeout 2

    "Ты открываешь дверь, и вы заходитн."
    window hide

    play sound sfx_open_door_clubs

    $ renpy.pause(1)

    $ persistent.sprite_time = "day"
    scene bg int_clubs_male_day 
    with dissolve
    show dv normal pioneer2 at center with dspr

    play ambience ambience_clubs_inside_day fadein 3

    window show
    "Внутри никого нет."
    play sound ds_sfx_int
    con "Комната представляет из себя что-то наподобие берлоги юного робототехника – повсюду валялись какие-то провода, нехитрые платы, микросхемы, на столе стоит осциллограф."
    "Из соседнего помещения слышатся голоса, и через секунду в комнату вошли двое пионеров."
    show el normal pioneer at cleft 
    show sh normal pioneer at cright 
    show dv angry pioneer2 at fright
    with dissolve
    play sound ds_sfx_int
    enc "В одном ты узнаёшь Электроника, второй же тебе был незнаком."
    el "Привет, Семен! А мы тебя ждали... {w}ой"
    el "Алиса, а ты что тут делаешь?!"
    play music music_list["awakening_power"] fadein 3
    dv "Да так, решила зайти, совершить акт возмездия... и заодно отбить новичка от вас!"
    show el scared pioneer at cleft with dspr
    el "Чего?"
    dv "Нет, это ты чего называешь меня всякими обидными прозвищами!"
    dv "Чего, кстати, ты меня Алисой назвал, а не «ДваЧе\", как любишь?!"
    el "И ничего я..."
    show dv rage pioneer2 at fright with dspr
    dv "Я тебе недостаточно ясно давала раньше понять, что это прозвище под запретом?!"
    dv "Вот я тебе сейчас задам! Вобью в тебя это кулаками, раз словами не понимаешь!"

    play music ds_chase fadein 5
    show dv rage pioneer2:
        ease 0.5 pos (0.2, 0)
        ease 0.5 pos (0.8, 0)
        repeat
    
    show el scared pioneer:
        ease 0.5 pos (0.8, 0)
        ease 0.5 pos (0.2, 0)
        repeat
    
    show sh pioneer close at right with dspr
    
    "Алиса и Электроник начинают бегать вокруг стола."
    dv "А ну иди сюда!"
    dv "А ещё парень, бежишь от девушки!"
    dv "Ответь за свои слова, как мужчина!"
    el "Да я не специально!"
    dv "Как раз специально так, чтобы я слышала!"
    shp "Алиса, успокойся... Электроник больше не будет..."
    dv "Да он уже кучу раз так меня называл!"
    dv "Его нужно хорошенько поколотить, чтобы до него что-нибудь дошло!"

    menu:
        "Остановить Алису":
            window show
            me "Алиса, прекрати, пожалуйста! Обходной!"
            play sound ds_sfx_mot
            svf "Она тебя не слышит. Придётся влезть в пучину!"
            window hide
            if skillcheck('savoir_faire', lvl_legendary):
                window show
                svf "Ты ловким движением останавливаешь руку Алисы."
                show dv rage pioneer2 at cright with dspr
                svf "Она вынуждена остановиться."
                dv "Что ты творишь?! Не мешай мне!"
                show el fingal pioneer at cleft with dspr
                svf "Но ты забыл про Электроника!"
                svf "Пока ты занимался Алисой, он продолжал бегать, споткнулся и упал."
            else:
                window show
                svf "Однако ты влезаешь неудачно, и кулак Алисы, отскочив от глаза Электроника, прилетает тебе в голову."
                $ ds_health -= 1
                show dv scared pioneer2 at cright with dspr
                show el fingal pioneer at cleft with dspr
                play sound ds_sfx_fys
                pat "Тебе больно, но ты держишься."
                play sound ds_sfx_psy
                emp "В выражении лица Алисы читается, что она не такого результата хотела."
                show dv angry pioneer2 at cright with dspr
                dv "Зачем ты мешаешься?! Теперь и ты получил! Подумал бы о себе хотя бы!"
            $ ds_skill_points['savoir_faire'] += 1
            $ ds_lp_dv -= 1
        "Ждать молча":
            "Ты стоишь и ждёшь разрешения конфликта."
            $ ds_semtype -= 1
            "И оно скоро наступает. {w}Алиса дотягивается до Электроника, и ему прилетает по глазу."
    $ ds_wintessed_el_hit = True
    show dv angry pioneer2 at cright with dspr
    show el fingal pioneer at cleft with dspr
    stop music fadeout 3

    dv "Теперь до тебя дошло, как меня нельзя называть?"
    el "Да-да, отстань от меня!"
    shp "Эл, иди лучше к медсестре, с новеньким я сам разберусь."
    hide el with dissolve
    "Электроник выходит, оставляя вас втроём."
    shp "На самом деле я должен сказать, что и я предупреждал Электроника насчёт Алисы."
    shp "Но он меня не слушал, хотел испытать судьбу, видимо."
    dv "Что ж, он испытал! Надеюсь, теперь он доволен!"
    show dv normal pioneer2 at left with dspr
    dv "Так, обходной нам ещё надо подписать!"

    me "А вас в клубе этом только двое, я так полагаю?"
    shp "Ну да. Меня Шурик зовут, кстати."
    "Шурик подходит к тебе и уверенно протянул руку."
    play sound ds_sfx_int
    enc "Его лицо тебе кажется почему-то знакомым."
    if skillcheck('encyclopedia', lvl_easy, passive=True):
        enc "Точно, он же вылитый Шурик из комедий Гайдая!"
    else:
        enc "Хотя нет, показалось..."
    show sh normal_smile pioneer at cright   with dspr
    sh "Добро пожаловать!"
    me "Угу…"
    show sh normal_smile pioneer at cright   with dspr
    sh "Всегда рады новым членам."
    play music ds_ussr_anthem fadein 2
    enc "Он сказал это так, что в голове у тебя невольно заиграл гимн Советского Союза."
    enc "Удивительно, но ты еще помнишь слова – в первом классе у тебя была тетрадка, на обратной стороне которой они были напечатаны."
    stop music fadeout 2
    show dv grin pioneer at left with dspr
    dv "Ну и зачем ему это?"
    window hide
    menu:
        "Записаться":
            window show
            th "Впрочем, новые знакомства мне точно не помешают."
            me "Да, давайте, записывайте меня!"
            show dv angry pioneer2 at left with dspr
            dv "Зачем тебе это?"
            sh "Отлично. Давай, кстати, сюда обходной лист."
            play sound ds_pen
            "Ты отдаёшь обходной лист, они записывают тебя в какой-то список и подписывают тебе его."
            sh "Вот, распишись тут."
            play sound ds_sfx_mot
            per_eye "Итак, члены клуба..."
            per_eye "1. ДЕМЬЯНЕНКО АЛЕКСАНДР"
            per_eye "2. CЫРОЕЖКИН СЕРГЕЙ"
            play sound ds_sfx_mot
            res "Значит, настоящее имя Электроника - Сергей..."
            per_eye "А вот и ты: 3. ПЁРСУНОВ СЕМЁН"
            play sound ds_pen
            "Ты ставишь свою подпись."
            $ ds_cyber_member = True
            $ ds_skill_points['interfacing'] += 1
        "Отказаться":
            window show
            me "Да нет, мне бы просто обходной лист подписать."
            dv "Да, нам ваши железяки неинтересны!"
            $ ds_lp_dv += 1
    dv "Всё, пошли отсюда!"

    scene bg ext_clubs_day 
    with dissolve
    stop ambience
    show dv normal pioneer2 at center with dspr
    "Вы с Алисой выходите молча. У неё какое-то странное выражение лица."

    menu:
        "Обратить внимание на Алису":
            if skillcheck('empathy', lvl_up_medium):
                $ ds_skill_points['empathy'] += 1
                play sound ds_sfx_psy
                emp "Ты замечаешь, что с Алисой что-то не так."
                me "Алис?.."
                show dv sad pioneer2 at center with dspr
                dv "Слушай, он правда уже задолбал меня так называть..."
                dv "Я ему столько раз говорила, а он... ну не нравится мне это прозвище!"
                dv "А ведь теперь он наверняка меня виноватой и сделает..."
                menu:
                    "Поддержать Алису":
                        me "Не переживай... я-то знаю, что права ты."
                        me "Если что, засвидетельствую."
                        show dv smile pioneer2 at center with dspr
                        $ ds_lp_dv += 1
                    "Осудить Алису":
                        me "Я всё понимаю, конечно, но бить не стоило всё же..."
                        show dv angry pioneer2 at center with dspr
                        dv "И ты туда же!"
                        dv "Все вы так говорите!"
                dv "Ладно, пошли!"
            else:
                $ ds_skill_points['empathy'] += 1
                play sound ds_sfx_psy
                emp "Вроде всё нормально."
        "Пойти дальше":
            pass

    $ ds_passed_places += 1
    $ ds_visited_clubs = True
    jump ds_day2_pass_dv_main

label ds_day2_pass_dv_medic:
    $ persistent.sprite_time = "day"
    scene bg ext_aidpost_day 
    with dissolve
    if (ds_passed_places >= 3) and not ds_had_lunch:
        show dv angry pioneer2 at center with dspr
        dv "Так, всё, я обедать!"
        dv "Я тебе ясно сказала, что пора обедать, а ты проигнорировал!"
        dv "Дальше подписывай свой лист сам!"
        hide dv with dissolve
        $ ds_lp_dv -= 1
        play sound ds_sfx_int
        lgc "Дальше тебе придётся подписывать лист одному."
        jump ds_day2_pass_alone_medic

    show dv normal pioneer2 at center with dspr

    play ambience ambience_camp_center_day fadein 3

    window show
    play sound ds_sfx_fys
    edr "Ты решительно не понимаешь, что тебе делать в медпункте."
    edr "Здоровье вроде не шалит, тем более местный свежий воздух явно пошел тебе на пользу, и самочувствие было куда бодрее, чем обычно."
    th "Но раз надо так надо."

    show dv grin pioneer2 at center with dspr
    dv "Ну что, готов встретиться с нашей медсестрой?"
    me "А что такое?"
    dv "Ну, знаешь..."
    show dv laugh pioneer2 at center with dspr
    dv "У неё очень специфические вкусы... она очень {i}любит{/i} пионеров."
    dv "Такая {i}горячая{/i} женщина."
    play sound ds_sfx_psy
    ine "Что она имеет ввиду?"
    play sound ds_sfx_psy
    aut "В любом случае, лучше не подавать виду."
    menu:
        "Пойти самому":
            th "Да чего там бояться, скорее всего меня опять разыграть пытаются!"
            $ ds_semtype += 1
            "Ты входишь."
            window hide

            stop ambience fadeout 2

            play sound sfx_open_door_1

            $ renpy.pause(1)

            $ persistent.sprite_time = "day"
            scene bg int_aidpost_day 
            with dissolve

            play ambience ambience_medstation_inside_day fadein 3

            window show
            th "Обычный такой медпункт, у нас в школе был примерно такой же."
            show cs normal stethoscope at center   with dissolve

            play music ds_cs_theme fadein 5

            "За столом сидит женщина средних лет."
            "Она бросает на меня пристальный, оценивающий взгляд, и продолжила что-то писать."
            csp "Ну, здравствуй… пионер."
            "Говорит она, не отрываясь от своего занятия."
            me "Добрый день… Мне бы вот…"
        "Попросить пойти вместе":
            me "Тогда, может, это... проводишь меня туда?"
            dv "Чего-чего? Мальчик испугался всего лишь женщины?"
            $ ds_morale -= 1
            $ ds_semtype -= 1
            show dv normal pioneer2 at center with dspr
            dv "Ладно, так уж и быть, пойду с тобой!"
            scene bg int_aidpost_day 
            with dissolve

            play ambience ambience_medstation_inside_day fadein 3

            window show
            th "Обычный такой медпункт, у нас в школе был примерно такой же."
            show cs normal stethoscope at center   with dissolve
            show dv normal pioneer2 at fright with dissolve

            play music ds_cs_theme fadein 5

            "За столом сидит женщина средних лет."
            "Она бросает на меня пристальный, оценивающий взгляд, и продолжила что-то писать."
            csp "Ну, здравствуй… пионер."
            "Говорит она, не отрываясь от своего занятия."
            csp "Я смотрю, ты и девушку уже привёл."
            csp "За изделием номер два пришли, небось?"
            show dv angry pioneer2 at fright with dspr
            dv "И ничего я не его девушка!"
            show cs shy stethoscope at center with dspr
            csp "Да ладно вам, мне вы можете рассказывать о своих... похождениях. Я вас вожатой не сдам."
            show dv shy pioneer2 at fright with dspr
            dv "В общем, давай тут сам, а то я помру от стыда!"
            dv "Буду ждать тебя у выхода!"
            me "Ну ладно..."
            hide dv with dissolve

    csp "Ты присаживайся."
    "Ты оглядываешь комнату."
    csp "На кушеточку."
    "Ты садишься."
    csp "Раздевайся."
    "Все это она говорит совершенно ровным тоном."
    me "А зачем?.."
    csp "Смотреть тебя будем, слушать, здоровье проверять."
    show cs smile stethoscope at center   with dspr
    csp "Меня, кстати, зовут Виолетта Церновна, но ты меня можешь звать просто Виолой."

    "Она поворачивается в твою сторону."
    cs "Ну, чего сидишь? Раздевайся."
    me "Да я не жалуюсь ни на что. Мне бы вот…"
    "Ты аккуратно протягиваешь ей листок."
    cs "Потом."
    show cs smile at center   with dissolve
    "Она снимает с шеи стетоскоп и, кажется, намеревается тебя им препарировать."
    window hide

    scene cg ds_day2_cs_near with dissolve

    window show
    "Она наклоняется, и тут..."
    play sound ds_sfx_fys
    ins "Какой прекрасный вид! Кое-что у тебя явно радуется этому."
    "Действительно, у тебя внизу быстро образовался характерный бугорок."
    play sound ds_sfx_mot
    com "Ты пытаешься не подать виду."
    cs "Что, нравится тебе... пионер?"
    "Ты молчишь, с трудом скрывая стыд от ситуации."
    cs "Так и запишем: рефлексы в порядке."

    scene bg int_aidpost_day with dissolve
    show cs normal stethoscope at center with dissolve
    cs "А теперь раздевайся."
    "Ты решаешь послушать её и снимаешь с себя рубашку."
    "Виола пристально всматривается в твой торс."
    cs "Да, тело у тебя, конечно, не в самом лучшем виде... но в целом неплохо."
    cs "Повернись спиной и дыши глубоко."
    play sound ds_sfx_mot
    per_toc "Как только ты это делаешь, ты ощущаешь холод стетоскопа на спине."
    cs "Дыши. {w}Не дыши. {w}Дыши. {w}Не дыши."
    show cs shy stethoscope at center with dspr
    cs "Эх, времени у нас маловато, а то..."
    cs "В общем, одевайся... пионер."
    "В это время она берёт твой обходной."
    queue sound ds_pen
    queue sound ds_stamp
    "Виола ставит подпись и печать и, когда ты оделся, отдаёт тебе."
    show cs smile glasses at center   with dspr
    cs "Если что заболит – сразу ко мне… пионер."
    stop ambience fadeout 2
    window hide
    menu:
        "Требовать продолжения":
            if skillcheck('instinct', lvl_easy):
                window show
                ins "Она {i}хочет{/i} тебя. И это взаимно. Требуй продолжения!"
                me "Нет уж, давайте продолжим!"
                show cs shy glasses at center with dspr
                cs "Увы, времени мало... тебе ещё обходной подписывать и сдавать."
                cs "Но... можешь зайти вечерком. Я до ночи тут."
                ins "Обязательно зайди."
                $ ds_cs_invite = True
                $ ds_skill_points['instinct'] += 1
                "На этой ноте ты выходишь."
            else:
                window show
                ins "Но ты не хочешь продолжения! Тебя она не привлекает."
                ins "Милфы - это не твоё, тебя интересуют девушки помоложе."
                ins "Или не интересуют..."
                $ ds_skill_points['instinct'] += 1
                "Ты ничего не отвечаешь и выходишь, закрыв за собой дверь."
        "Молча выйти":
            window show
            "Ты ничего не отвечаешь и выходишь, закрыв за собой дверь."
        "Поблагодарить и выйти":
            window show
            me "Cпасибо..."
            $ ds_karma += 5
            "И с этими словами ты выходишь."

    stop music fadeout 3

    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_aidpost_day 
    with dissolve
    show dv laugh pioneer2 at center with dspr

    window show
    dv "Ну что, как тебе наша медсестра?"
    me "Гхм... интересная женщина."
    dv "А то! Я же тебе говорила!"
    play sound ds_sfx_fys
    ins "Да не то слово..."
    window hide

    $ ds_passed_places += 1
    $ ds_visited_medic = True
    jump ds_day2_pass_dv_main

label ds_day2_pass_dv_library:
    play ambience ambience_camp_center_day fadein 3
    $ persistent.sprite_time = "day"
    scene bg ext_library_day 
    with dissolve
    show dv normal pioneer2 at center with dissolve

    if (ds_passed_places >= 3) and not ds_had_lunch:
        show dv angry pioneer2 at center with dspr
        dv "Так, всё, я обедать!"
        dv "Я тебе ясно сказала, что пора обедать, а ты проигнорировал!"
        dv "Дальше подписывай свой лист сам!"
        hide dv with dissolve
        $ ds_lp_dv -= 1
        play sound ds_sfx_int
        lgc "Дальше тебе придётся подписывать лист одному."
        jump ds_day2_pass_alone_library

    window show
    play sound ds_sfx_psy
    vol "Вообще, ты, конечно, любишь читать, но просиживать днями в библиотеке при нынешних обстоятельствах в твои планы не входит, так что ты решил побыстрее пройти этот чекпойнт."
    dv "Готовься, нам придётся забраться в логово к зверю!"
    dv "Местная библиотекарша Женя, хоть и пионерка, но ведёт себя как настоящая бабка!"
    window hide

    stop ambience fadeout 3

    $ persistent.sprite_time = "day"
    scene bg int_library_day 
    with dissolve

    play ambience ambience_library_day fadein 3

    window show
    play sound ds_sfx_psy
    ine "Когда ты заходишь внутрь, у тебя в голове всплывает воспоминание из детства."
    ine "Оно очень яркое."
    ine "Тебе лет 7 или 8, ты с мамой в библиотеке."
    ine "Пока она выбирает какие-то книжки, которые тебе понадобятся для учебы, ты сидишь и разглядываешь местную подборку комиксов."
    ine "Тогда тебе было сложно понять, почему их здесь так много и почему нельзя забрать часть домой."
    ine "Понятия коллективной собственности тогда для тебя не существовало."
    ine "Впрочем, как и понятия собственности вообще."
    ine "Тем более странным было это воспоминание сейчас, когда ты находишься в том самом отдельно взятом пионерлагере, где коммунизм таки удалось построить за 3 года."
    "Повсюду висит огромное количество советской символики, а на полках книги в основном соответствующей тематики."
    vol "Читать их ты никак не планировал – знакомство с полным собранием сочинений Маркса было одной из последних вещей на Земле, которая пришла бы тебе в голову."
    vol "Надо найти библиотекаря."
    "Оказалось это не так сложно – она спит на столе рядом с тобой."
    $ ds_met['mz'] = 2
    window hide

    scene cg d2_micu_lib 
    with dissolve

    window show
    "Ты пригляделся.{w} Короткая стрижка, толстые очки, довольно приятное лицо."
    th "Она так мило спит..."
    scene bg int_library_day with dissolve
    show dv angry pioneer2 at cleft with dissolve
    dv "ПОДЪЁМ!"
    show mz angry glasses pioneer far at cright   with dspr
    mz "В библиотеке нужно поддерживать тишину!"
    dv "А ещё в библиотеке нужно работать, а не сны смотреть!"
    mz "А это не твоё дело, что я делаю в библиотеке!"
    mz "Не нравится - поработай сама!"
    mz "А то сама книги не читаешь, и другим мешаешь!"
    show dv rage pioneer2 at cleft with dspr
    dv "Я-то не читаю книги?!"
    dv "Ты считаешь меня тупой?!"
    mz "Я тебя тупой не называла! Иди вон, у меня посетитель тут! Следующий!"
    "Последнее слово она произносит нарочито громко."
    show dv angry pioneer2 at cleft with dspr
    dv "Ну и пойду!"
    hide dv with dissolve
    mz "А тебе чего?"
    me "Мне бы обходной…"
    show mz normal glasses pioneer at cright   with dissolve
    mz "Давай."
    queue sound ds_pen
    queue sound ds_stamp
    "Она быстро расписывается, ставит печать и протягивает тебе его обратно."
    mz "Получать читательский билет будем?"
    window hide
    menu:
        "Согласиться":
            window show
            me "Да, давай...те."
            "Женя залезает в стол, достаёт какой-то листок..."
            mz "Фамилия, имя?"
            me "Пёрсунов Семён..."
            play sound ds_pen
            "Она записывает сведения в билет, а затем отдаёт тебе."
            mz "Бери!"
            "Ты забираешь бумажку и складываешь в карман штанов."
            $ ds_library_member = True
            $ ds_skill_points['encyclopedia'] += 1
            mz "Cледующий!"
        "Отказаться":
            window show
            me "Нет, спасибо."
            mz "Тогда следующий!"
    play sound ds_sfx_psy
    emp "Вид у нее такой, что дальнейший разговор кажется совершенно неуместным."
    "Ты благодаришь Женю и выходишь."
    window hide

    stop ambience fadeout 2

    scene bg ext_library_day
    with dissolve

    show dv smile pioneer2 at center with dissolve

    dv "Ну что, укротил зверя?"
    me "Да справился, не волнуйся за меня..."
    show dv grin pioneer2 at center with dissolve
    dv "Ну и хорошо, идём дальше!"

    show un normal pioneer far at fleft with dissolve
    "Краем глаза ты видишь Лену, заходящую в библиотеку."
    show dv angry pioneer at center with dspr
    show dv normal pioneer at center with dspr
    hide un with dissolve
    if skillcheck('reaction_speed', lvl_medium):
        play sound ds_sfx_mot
        res "На миг ты замечаешь, что появление Лены вызвало неприязненную реакцию Алисы."
        res "Впрочем, лишь на миг."
        play sound ds_sfx_psy
        emp "Это явно неспроста. Попробуй выяснить это позже."

    $ ds_passed_places += 1
    $ ds_visited_library = True
    jump ds_day2_pass_dv_main

label ds_day2_pass_dv_sport:
    scene bg ext_playground_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    show dv normal pioneer2 at center with dissolve
    window show
    if (ds_passed_places >= 3) and not ds_had_lunch:
        show dv angry pioneer2 at center with dspr
        dv "Так, всё, я обедать!"
        dv "Я тебе ясно сказала, что пора обедать, а ты проигнорировал!"
        dv "Дальше подписывай свой лист сам!"
        hide dv with dissolve
        $ ds_lp_dv -= 1
        play sound ds_sfx_int
        lgc "Дальше тебе придётся подписывать лист одному."
        jump ds_day2_pass_alone_sport
    "Ты подходишь к спортплощадке."
    show dv smile pioneer2 at center with dspr
    dv "Идём сюда!"
    "Алиса указывает в сторону небольшого здания."
    "Ты направляешься туда."
    scene bg ds_int_sporthall_day with dissolve
    show us smile sport far at center with dissolve
    show dv smile pioneer2 at right with dissolve
    "Зайдя в спортзал, ты видишь Ульяну бегающей по залу."
    us "Алиса, а где ты была? Почему на пляж не ходила?"
    show dv grin pioneer2 at right with dspr
    dv "Да мне тут надо помочь нашему новому обходной подписать... он же сам не справится!"
    show us laugh2 sport at center with dspr
    us "Да вообщк, что бы ты без нашей Алисы делал бы, а?"
    me "Ульяна, а где я тут могу подписать обходной лист?"
    us "Давай его сюда!"
    show us laugh sport at center with dspr
    play sound ds_sfx_int
    dra "По всей видимости, она опять хочет вас провести."
    us "Я тут спортклубом руковожу!"
    play sound ds_sfx_mot
    res "Так ей же не более 14 лет! И уже руководит чем-то?"
    menu:
        "Принять":
            me "А... хорошо."
        "Усомниться":
            me "Ты? Ты же ещё маленькая!"
            show us dontlike sport at center with dspr
            us "И ничего не маленькая! Мне сама Ольга Дмитриевна доверила!"
            $ ds_lp_us -= 1
    show dv laugh pioneer2 at right with dspr
    dv "Вот, а тебе что-нибудь доверили бы?"
    show us normal sport at center with dspr
    show dv normal pioneer2 at right with dspr
    us "Кстати, не хочешь записаться к нам?"
    if not ds_caught_us:
        show us laugh2 sport at center with dspr
        us "Может, и сможешь меня тогда догнать!"
    menu:
        "Записаться":
            me "Давай!"
            show us smile sport at center with dspr
            us "Вот, бери листик и записывайся сюда!"
            "Ты вносишь своё имя в данный тебе клочок бумаги."
            me "Вот, а теперь подпиши мне обходной."
            us "Давай сюда!"
            play sound ds_pen
            "Она подписывает обходной и отдаёт лист тебе."
            play sound ds_sfx_mot
            per_eye "СОВЕТОВА У.И. {w}Теперь мы знаем её фамилию!"
            me "Cпасибо!"
            show us laugh sport at center with dspr
            us "Только не забывай регулярно приходить сюда!"
            show dv laugh pioneer2 at right with dspr
            dv "Я прослежу за этим!"
            $ ds_sport_member = True
            $ ds_lp_us += 1
            "Под эти слова вы уходите из зала."
        "Отказаться":
            me "Нет, спасибо... мне просто нужен обходной лист."
            show us dontlike sport at center with dspr
            us "Ну и ладно, давай сюда свою бумажку!"
            play sound ds_pen
            "Она подписывает обходной и отдаёт лист тебе."
            play sound ds_sfx_mot
            per_eye "СОВЕТОВА У.И. {w}Теперь мы знаем её фамилию!"
            me "Cпасибо!"
            "И вы уходите."
    $ ds_passed_places += 1
    $ ds_visited_sport = True
    jump ds_day2_pass_dv_main

label ds_day2_pass_dv_lunch:
    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_away_day 
    with dissolve
    show dv normal pioneer2 at center with dissolve

    window show
    "Вы решаете всё же сходить пообедать."
    show dv grin pioneer2 at center with dspr
    dv "Так уж и быть, сегодня сядешь со мной!"
    window hide

    scene bg int_dining_hall_day
    with dissolve

    show dv sad pioneer2 at center with dissolve
    play sound ds_sfx_psy
    emp "Чего-то Алиса погрустнела."
    me "Ты чего?"
    dv "Посмотри на эту очередь... нам в ней стоять и стоять..."
    play sound ds_sfx_int
    vic "И то верно: очередь действительно длинная."
    window hide
    menu:
        "Предложить Алисе занять место":
            window show
            me "Cлушай, может, пока тогда место нам подыщешь?"
            show dv smile pioneer2 at center with dspr
            dv "И то верно, удачи! Как получишь еду - найдёшь меня!"
            hide dv with dissolve
            window hide
            $ renpy.pause(3.0)
            window show
            "Наконец, спустя какое-то время ты доходишь до выдачи еды."
            show ck normal at center with dissolve
            ck "Вот, бери, пионер. Приятного аппетита!"
            window hide
            menu:
                "Попросить обед для Алисы":
                    window show
                "Забить на Алису":
                    window show
                    th "Cама возьмёт!"
                    ck "Cледующий!"
                    hide ck with dissolve
                    "Ты подходишь к Алисе."
                    show dv angry pioneer2 at center with dissolve
                    dv "А где еда для меня?!"
                    dv "Ты издеваешься надо мной?"
                    me "Извини, не взял..."
                    dv "Да пошёл ты! Подписывай дальше лист один!"
                    hide dv with dissolve
                    $ ds_lp_dv -= 2
                    "Ты быстро съедаешь обед и идёшь подписывать лист, теперь один."
                    $ ds_had_lunch = True
                    jump ds_day2_pass_alone_main
            me "А можно обед для... {w}подруги, пожалуйста, она заняла нам место заранее."
            show ck smile at center with dspr
            ck "Да, конечно."
            "Она даёт тебе ещё порцию еды."
            me "Cпасибо."
            scene bg ds_int_dininghall_table2_day with dissolve
            show dv smile pioneer2 at center with dissolve
            "С этими словами ты идёшь прямо к Алисе - благо, её рыжие хвосты очень трудно не заметить."
            dv "О, пришёл! С едой!"
        "Заставить Алису стоять вместе":
            window show
            me "Cтой тут."
            dv "Ладно..."
            window hide
            $ renpy.pause(3.0)
            window show
            show ck normal at center with dissolve
            show dv normal pioneer2 at right with dspr
            "Наконец, спустя какое-то время вы доходите до выдачи еды."
            window hide
            menu:
                "Пропустить вперёд Алису":
                    window show
                    me "Прошу, проходи."
                    show dv smile pioneer2 at right with dspr
                    dv "И пройду!"
                    "Алиса забирает еду, затем берёшь еду и ты."
                    show ck smile at center with dspr
                    ck "Я смотрю, ты с девушкой, пионер."
                    show dv shy pioneer2 at right with dspr
                    me "Ну, всё-таки скорее с подругой."
                    show ck laugh at center with dspr
                    ck "Ну, как скажете!"
                    hide ck with dissolve
                "Пойти вперёд самому":
                    window show
                    "Ты влезаешь вперёд и берёшь еду."
                    $ ds_lp_dv -= 1
                    show ck smile at center with dspr
                    ck "Я смотрю, ты с девушкой, пионер."
                    show dv shy pioneer2 at right with dspr
                    me "Ну, всё-таки скорее с подругой."
                    show ck laugh at center with dspr
                    ck "Ну, как скажете!"
                    hide ck with dissolve
                    "Ты отходишь, дожидаешься Алису."
                    "Вскоре она возвращается с едой."
            show dv angry pioneer2 at center with dspr
            "Вы отходите, пытаясь найти столик."
            dv "Ну и где все столики?!"
            window hide
            $ renpy.pause(0.5)
            window show
            play sound ds_sfx_mot
            per_eye "Вон там есть, вдалеке!"
            me "Я нашёл столик!"
            scene bg ds_int_dininghall_table2_day with dissolve
            show dv normal pioneer2 at center with dspr
            "Вы как можно более быстро добираетесь до него и присаживаетесь."
    me "Приятного аппетита."
    dv "Тебе тоже."
    window hide
    menu:
        "Заговорить с Алисой":
            window show
            me "Алиса?"
            play sound ds_sfx_int
            rhe "Она делает вид, будто тебя нет."
            me "Али-и-иса! Приём!"
            show dv angry pioneer2 at center with dspr
            dv "Чего тебе надо?"
            window hide
            menu:
                "Начать разговор":
                    if skillcheck('rhetoric', lvl_challenging):
                        window show
                        rhe "Набор вопросов стандартный - откуда она, чем увлекается."
                        $ ds_skill_points['rhetoric'] += 1
                        me "А ты откуда?"
                        dv "Какая тебе разница?! Из Работино я, тут недалеко!"
                        me "А увлекаешься чем?"
                        dv "Что ты пристал ко мне... На гитаре играю!"
                        dv "Может быть, даже послушаешь на концерте... или сыграешь. Посмотрим."
                        dv "Всё, оставь меня в покое!"
                        $ ds_lp_dv -= 1
                        "Оказывается, что вы съели весь обед. Вы встаёте и идёте подписывать обходной."
                    else:
                        window show
                        rhe "Тебе не приходят в голову никакие темы."
                        $ ds_skill_points['rhetoric'] += 1
                        "Вы молча доедаете обед и идёте подписывать обходной."
                "Проанализировать её поведение":
                    if skillcheck('empathy', lvl_legendary):
                        window show
                        play sound ds_sfx_psy
                        emp "Она из-за чего-то сильно переживает."
                        emp "Кстати. Вспомни нелюбимое ею прозвище. Кажется, тут есть связь..."
                        emp "Да и в целом её поведение напоминает поведение травмированного человека."
                        emp "Но ты в любом случае не заработал её доверия. Пока лучше не лезь."
                        emp "Разговаривать с тобой она точно не захочет. Просто извинись и отступи."
                        $ ds_skill_points['empathy'] += 1
                        window hide
                        menu:
                            "Начать разговор":
                                if skillcheck('rhetoric', lvl_challenging):
                                    window show
                                    rhe "Набор вопросов стандартный - откуда она, чем увлекается."
                                    $ ds_skill_points['rhetoric'] += 1
                                    me "А ты откуда?"
                                    dv "Какая тебе разница?! Из Работино я, тут недалеко!"
                                    me "А увлекаешься чем?"
                                    dv "Что ты пристал ко мне... На гитаре играю!"
                                    dv "Может быть, даже послушаешь на концерте... или сыграешь. Посмотрим."
                                    dv "Всё, оставь меня в покое!"
                                    $ ds_lp_dv -= 1
                                    "Оказывается, что вы съели весь обед. Вы встаёте и идёте подписывать обходной."
                                else:
                                    window show
                                    rhe "Тебе не приходят в голову никакие темы."
                                    $ ds_skill_points['rhetoric'] += 1
                                    "Вы молча доедаете обед и идёте подписывать обходной."
                            "Поддержать":
                                window show
                                me "Я ещё плохо тебя знаю... но понимаю, что тебе от чего-то плохо."
                                dv "Не лезь в это... это не твоё дело!"
                                emp "Но это значит, что точно что-то есть!"
                                emp "Обязательно вернись к этому, когда (и если) сблизишься с ней больше."
                                "Тут вы доедаете обед, встаёте и идёте подписывать обходной."
                            "Извиниться":
                                window show
                                me "Извини... просто думал поговорить."
                                dv "А я не настроена на разговор!"
                                "Вы молча доедаете обед, встаёте и идёте дальше подписывать обходной."
                    else:
                        window show
                        play sound ds_sfx_psy
                        emp "Тебе решительно непонятно её поведение."
                        $ ds_skill_points['empathy'] += 1
                        window hide
                        menu:
                            "Начать разговор":
                                if skillcheck('rhetoric', lvl_challenging):
                                    window show
                                    rhe "Набор вопросов стандартный - откуда она, чем увлекается."
                                    $ ds_skill_points['rhetoric'] += 1
                                    me "А ты откуда?"
                                    dv "Какая тебе разница?! Из Работино я, тут недалеко!"
                                    me "А увлекаешься чем?"
                                    dv "Что ты пристал ко мне... На гитаре играю!"
                                    dv "Может быть, даже послушаешь на концерте... или сыграешь. Посмотрим."
                                    dv "Всё, оставь меня в покое!"
                                    $ ds_lp_dv -= 1
                                    "Оказывается, что вы съели весь обед. Вы встаёте и идёте подписывать обходной."
                                else:
                                    window show
                                    rhe "Тебе не приходят в голову никакие темы."
                                    "Вы молча доедаете обед и идёте подписывать обходной."
                            "Извиниться":
                                window show
                                me "Извини... просто думал поговорить."
                                dv "А я не настроена на разговор!"
                                "Вы молча доедаете обед, встаёте и идёте дальше подписывать обходной."
                    dv "Теперь ты завис?!"
                "Извиниться":
                    window show
                    me "Извини... просто думал поговорить."
                    dv "А я не настроена на разговор!"
                    "Вы молча доедаете обед, встаёте и идёте дальше подписывать обходной."
        "Поесть молча":
            window show
            th "Что-то не хочется с ней разговаривать..."
            "Поэтому вы, быстро поев, встали и пошли дальше подписывать обходной."
    $ ds_had_lunch = True
    jump ds_day2_pass_dv_main

label ds_day2_pass_sl_music:
    play ambience ambience_camp_center_day fadein 3

    $ persistent.sprite_time = "day"
    scene bg ext_musclub_day 
    with dissolve
    show sl normal pioneer at center with dspr

    if ds_sl_keys:
        if ds_passed_places == 0:
            th "У меня ещё ключи... может, отдать их Славе?"
        else:
            th "Может, всё-таки отдать ключи Славе?"
        window hide
        menu:
            "Отдать ключи":
                window show
                me "Славя, ты вчера в столовой, кстати, ключи забыла."
                me "Вот, я их тебе принёс."
                play sound sfx_keys_rattle
                show sl smile pioneer at center with dspr
                sl "О, спасибо большое! Я их обыскалась уже!"
                sl "Если бы не ты, мне бы влетело от Ольги Дмитриевны!"
                $ ds_lp_sl += 1
                $ ds_sl_keys = False
            "Не отдавать":
                window show
                th "Да зачем? Может, эти ключи мне потребуются ещё."
            "Отцепить ключик себе":
                if skillcheck('interfacing', lvl_godly):
                    window show
                    inf "Ты ловко двигаешь пальцами у себя в кармане... "
                    window hide
                    $ renpy.pause(0.5)
                    window show
                    inf "И в итоге туда проваливается какой-то ключик."
                    $ ds_karma -= 5
                    $ ds_skill_points['interfacing'] += 1
                    inf "Остальное ты вынимаешь и протягиваешь Славе."
                    me "Cлавь, ты вчера в столовой ключи забыла..."
                    show sl surprise pioneer at center with dspr
                    sl "Правда? Спасибо, что вернул!"
                    play sound sfx_keys_rattle
                    $ ds_lp_sl += 1
                    $ ds_sl_keys = False
                    $ ds_some_key = True
                    show sl smile pioneer at center with dspr
                    emp "Она тебе благодарна."
                    play sound ds_sfx_mot
                    svf "А у тебя остался ключик! Только вот какой?"
                else:
                    window show
                    play sound sfx_keys_rattle
                    $ renpy.pause(0.5)
                    play sound ds_sfx_mot
                    inf "Но ключи слишком громко шумят, и Славя обращает внимание."
                    $ ds_skill_points['interfacing'] += 1
                    show sl serious pioneer at center with dspr
                    sl "Что за звук?"
                    window hide
                    menu:
                        "Сказать про ключи":
                            window show
                            me "Да я про ключи вспомнил, доставал их, чтобы тебе отдать."
                            show sl smile pioneer at center with dspr
                            sl "Правда? Спасибо, что вернул!"
                            play sound sfx_keys_rattle
                            $ ds_lp_sl += 1
                            $ ds_sl_keys = False
                            emp "Она тебе благодарна."
                        "Cоврать":
                            if skillcheck('drama', lvl_formidable):
                                window show
                                play sound ds_sfx_int
                                dra "Скажите, мессир, будто это кто-то другой проходил."
                                dra "И главное - покажите, что вы тоже ищете источник."
                                me "Не знаю, тут ходит кто-то, наверное. Или в лесу."
                                $ ds_skill_points['drama'] += 1
                                show sl normal pioneer at center with dspr
                                sl "А, ну ладно!"
                                dra "Про ключи лучше не говори."
                            else:
                                window show
                                play sound ds_sfx_int
                                dra "Это не вы! Это точно не вы!"
                                me "Этот звук не от меня!"
                                sl "Точно? Покажи, что у тебя в кармане!"
                                "Ты достаёшь ключи."
                                $ ds_skill_points['drama'] += 1
                                show sl angry pioneer at center with dspr
                                sl "Значит, ключи украл? А я тебя в столовую проводила..."
                                $ ds_lp_sl -= 1
                                me "Да ты просто их в столовой забыла, а я хотел вернуть."
                                sl "Ага, хотел... Отдавай их!"
                                play sound sfx_keys_rattle
                                "Тебе приходится их отдать."
                                play sound ds_sfx_psy
                                emp "Ей очень обидно, что ты хотел скрыть их от неё. Она же могла быть и наказана за потерю ключей."
    
    if (ds_passed_places == 3) and not ds_had_lunch:
        sl "Cлушай, я схожу пообедаю, а ты пока зайди без меня, хорошо?"
        sl "Я приду сюда же. Я быстро!"
        me "Ладно..."
        hide sl with dissolve
        $ ds_sl_gone = True
        jump ds_day2_pass_alone_music

    window show
    "Музыкальный клуб располагается на некотором расстоянии от остальных построек лагеря."
    "Снаружи он представляет из себя небольшое одноэтажное здание."
    play sound ds_sfx_psy
    vol "Не раздумывая, ты заходишь. Cлавя за тобой"
    window hide

    stop ambience fadeout 2
    play sound sfx_open_door_2

    $ renpy.pause(1)

    $ persistent.sprite_time = "day"
    scene bg int_musclub_day 
    with dissolve

    show sl normal pioneer at center with dissolve

    play ambience ambience_music_club_day fadein 3

    window show
    play sound ds_sfx_int
    enc "Внутри оказывается полный набор музыкальных инструментов, на любой вкус и слух – барабаны, гитары и даже настоящий рояль."
    enc "Некоторое время твоё внимание плотно приковано к ним – хочется понять, из какого они примерно временного периода..."
    play sound ds_sfx_mot
    per_hea "Но неожиданно под роялем послышалось какое-то копошение."
    window hide

    scene cg ds_day2_mi_piano1
    with dissolve

    play music music_list["so_good_to_be_careless"] fadein 5

    window show
    "Ты наклоняешься и видишь девочку, которая, кажется, что-то искала."
    $ ds_met['mi'] = 1
    play sound ds_sfx_fys
    ins "Она стоит на четвереньках в такой пикантной позе..."
    window hide
    menu:
        "Сдержать порывы":
            window show
            me "Простите…"
        "Начать приставать":
            if skillcheck('instinct', lvl_easy):
                window show
                ins "Внизу у тебя встаёт твой ствол..."
                ins "Ты подходишь к ней и прижимаешься ей к юбке..."
                sl "Что ты делаешь, Семён?"
                $ ds_lp_sl -= 1
                play sound ds_sfx_mot
                res "Но она тебя замечает!"
            else:
                window show
                ins "Ты бы и начал к ней приставать, но тут Славя..."
                "Твои неуклюжие движения привлекают внимание девочки."
            $ ds_skill_points['instinct'] += 1
    window hide

    scene cg ds_day2_mi_piano2
    with dissolve

    window show
    mip "Ааа! Кто здесь?"
    window hide

    play sound sfx_piano_head_bump
    with vpunch

    $ renpy.pause(1)

    window show
    "Она пытается вскочить, но днище рояля стало для нее непреодолимой преградой."
    mip "Ой!"
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_musclub_day 
    with dissolve

    show mi shocked pioneer at center   with dissolve
    show sl normal pioneer at right with dissolve
    window show
    "С трудом, но она все же выбирается."
    sl "Извини, что помешали, но у нас к тебе дело."
    show mi normal pioneer at center   with dspr
    mip "Да ничего! Вижу, у тебя обходной, новенький, значит?"
    me "А? Да."
    show mi smile pioneer at center   with dspr
    mip "Меня Мику зовут."
    $ ds_met['mi'] = 2
    play sound ds_sfx_int
    enc "Тебе её имя почему-то кажется знакомым."
    if skillcheck('encyclopedia', lvl_medium, passive=True):
        enc "Точно, Мику существует и в твоём мире..."
        enc "В качестве так называемого «вокалоида» - компьютерной программы, симулирующей голос певицы."
        enc "А тут вот, вполне реальная девочка."
        play sound ds_sfx_int
        rhe "Только ей об этом вообще не стоит говорить."
    else:
        enc "Нет, показалось. Ты никогда не слышал имени Мику."

    mi "Нет, честно-честно! Никто не верит, а меня правда так зовут. Просто у меня мама из Японии. Папа с ней познакомился, когда строил там… Ну, то есть не строил – он у меня инженер…"
    mi "Короче, атомную станцию! Или плотину… Или мост… Ну, неважно!"
    play sound ds_sfx_mot
    res "Она говорит с такой скоростью, что половину слов ты не успеваешь разбирать."
    menu:
        "Сделать комплимент":
            me "Да... а ты прекрасно выглядишь, кстати."
            $ ds_lp_mi += 1
            show mi shy pioneer at center with dspr
            mi "Что ты говоришь? Ты правда считаешь, что я прекрасно выгляжу? А впрочем, мне все так говорят. Я почему-то очень-очень привлекаю всех парней."
            show mi smile pioneer at center with dspr
            mi "Ой, а как тебя зовут, кстати? Наверное, у тебя и имя должно быть каким-нибудь красивым!"
        "Высказать насчёт болтливости":
            me "Слушай, а ты всегда такая болтливая?"
            show mi sad pioneer at center with dspr
            mi "Да, есть у меня такое, совсем-совсем не знаю, что с этим делать. Все-все из-за этого раздражаются, даже ты... а как тебя зовут, кстати?"
            $ ds_lp_mi -= 1
            $ ds_karma -= 5
            play sound ds_sfx_psy
            emp "Она старается изобразить, будто её вообще не задели твои слова, хотя это далеко не так."
        "Промолчать":
            pass
    me "А я Семен."
    show mi happy pioneer at center   with dspr
    mi "Отлично! Не хочешь к нам в клуб вступить? Правда, нас тут пока только двое: я и Алиса-тян, но вместе мы будем втроём! Ты на чем-нибудь играть умеешь?"
    th "Уже в период моего «отшельничества» я купил себе гитару и по самоучителям выучил пару аккордов, но потом забросил это дело, как и любое другое, которое требовало больше нескольких часов."
    play sound ds_sfx_int
    con "А тут ты наверняка сможешь подтянуть свои навыки и сыграть что-нибудь прекрасное!"
    if not (ds_cyber_member or ds_sport_member):
        show sl smile pioneer at center with dspr
        sl "Да, давай, тебе как раз было бы неплохо куда-нибудь записаться!"
    window hide
    menu:
        "Записаться":
            window show
            me "Да, давай!"
            mi "Отлично, сейчас я тебя запишу к нам, Семён-кун. Я так рада, что ты присоединился к нам. Алиса-тян наверняка тоже обрадуется!"
            play sound ds_pen
            "Она достаёт листок и вписывает туда твои имя..."
            mi "А фамилия у тебя какая? А, точно, давай обходной, его заодно подпишу и спишу фамилию!"
            queue sound ds_mi_sign
            queue sound ds_pen
            "Ты отдаёшь ей свой обходной, она ставит подпись (вернее, печать, как истинная японка) там и дописывает в список членов клуба твою фамилию."
            mi "Распишись тут, пожалуйста."
            play sound ds_sfx_mot
            per_eye "Ты просматриваешь список, теперь состоящий из трёх человек."
            per_eye "1. ХАЦУНЕ МИКУ, {w}2. ДВАЧЕВСКАЯ АЛИСА..."
            per_eye "И вот наконец ты видишь себя: 3. ПЁРСУНОВ СЕМЁН."
            play sound ds_pen
            "Ты ставишь свою подпись."
            mi "Как же отлично. Как-нибудь обязательно надо будет вместе что-нибудь сыграть! Как раз на прощальном концерте через восемь дней и сыграем!"
            me "Да..."
            sl "Молодец!"
            $ ds_lp_mi += 1
            if not (ds_cyber_member or ds_sport_member):
                $ ds_lp_sl += 1
            $ ds_skill_points['conceptualization'] += 1
            $ ds_music_member = True
        "Отказаться":
            window show
            me "Знаешь, я как-то не планировал особо…"
            show mi normal pioneer at center   with dspr
            mi "Да ладно тебе, я тебя научу играть! Хочешь на трубе, например? Или на скрипке? Я на всем умею, честно-честно."
            play sound ds_sfx_mot
            сom "Ты решаешь не спорить с девочкой-мультиинструменталистом, так как в ответ наверняка бы получил очередную пулеметную очередь из слов."
            me "Я подумаю, а пока не могла бы ты подписать?"
            show mi happy pioneer at center   with dspr
            mi "Да-да-да, конечно, давай! Ты заходи, не стесняйся! Я еще и пою хорошо! Послушаешь, как я пою японские народные песни. Ну, или, если не нравится, может, что-нибудь из современных шлягеров?"
            me "Обязательно…"
    me "А сейчас мне пора, извини."
    show mi shy pioneer at center   with dspr
    mi "Конечно, приходи непременно… а, подожди..."
    sl "Подожди, давай дослушаем."
    window hide

    stop ambience fadeout 2

    stop music fadeout 3

    menu:
        "Дослушать":
            window show
            "Ты останавливаешься в двери, чтобы дослушать Мику"
            show mi sad pioneer at center with dspr
            mi "У меня тут потерялась заколка, ты случайно не видел её? Мне она очень-очень дорога и важна!"
            me "Нет..."
            mi "Поищи её, пожалуйста, если найдёшь - отнеси сюда или в домик 13, мне правда она очень-очень нужна..."
            me "Ладно..."
            $ ds_lp_mi += 1
            $ ds_find_hairpin = True
            "И с этими словами ты выходишь."
            show mi happy pioneer at center with dspr
            mi "Cпасибо-спасибо большое, Семён-кун!"
            scene bg ext_musclub_day 
            with dissolve

            play ambience ambience_camp_center_day fadein 3
        "Идти дальше":
            $ renpy.pause(1)

            $ persistent.sprite_time = "day"
            scene bg ext_musclub_day 
            with dissolve

            play ambience ambience_camp_center_day fadein 3

            window show
            "Окончание ее фразы скрывается за закрытой дверью."
            show sl serious pioneer at center with dspr
            sl "Надо было дослушать, что она говорит."
            me "Нам ещё нужно успеть обходной подписать!"
    if not ds_music_member:
        play sound ds_sfx_int
        con "С одной стороны, ты был бы не против вечерком посидеть побренчать на гитаре"
        play sound ds_sfx_mot
        com "Но в такой компании…"
    show dv normal pioneer close at center    with dissolve
    show sl normal pioneer at right with dspr
    "Ты поворачиваешься, собираясь уходить, и сталкиваешься нос к носу с Алисой."
    "Она недобро смотрит на тебя."
    dv "Зачем пришел?"
    if ds_music_member:
        window hide
        menu:
            "Чтобы записаться":
                window show
                me "В музклуб записаться..."
                show dv smile pioneer close at center with dspr
                dv "А... неплохо."
                $ ds_lp_dv += 1
                dv "Записался?"
            "Чтобы подписать обходной":
                window show
                me "Обходной…"
                dv "Подписал?"
    else:
        me "Обходной…"
        dv "Подписал?"
    me "Да…"
    dv "Свободен!"
    show sl angry pioneer at right with dspr
    sl "Алиса, не будь такой грубой с новичком!"
    show dv angry pioneer at center with dspr
    dv "Да что ты опять ко мне прицепилась?!"
    hide dv  with dissolve
    "Она входит внутрь."
    window hide
    menu:
        "Вмешательство не требовалось":
            window show
            me "Да всё нормально, Славь, тебе не надо было к ней лезть."
            $ ds_semtype += 1
            show sl smile pioneer at center with dspr
            sl "Ну, как скажешь."
            $ ds_skill_points['authority'] += 1
        "Поблагодарить":
            window show
            me "Спасибо, а то грубит мне она тут..."
            $ ds_semtype -= 1
            show sl normal pioneer at center with dspr
            sl "Да не за что."
        "Промолчать":
            pass
    window hide

    stop ambience fadeout 2

    $ ds_passed_places += 1
    $ ds_visited_music = True
    jump ds_day2_pass_sl_main

label ds_day2_pass_sl_clubs:
    play ambience ambience_camp_center_day fadein 2

    $ persistent.sprite_time = "day"
    scene bg ext_clubs_day 
    with dissolve
    show sl normal pioneer at center with dspr

    if ds_sl_keys:
        if ds_passed_places == 0:
            th "У меня ещё ключи... может, отдать их Славе?"
        else:
            th "Может, всё-таки отдать ключи Славе?"
        window hide
        menu:
            "Отдать ключи":
                window show
                me "Славя, ты вчера в столовой, кстати, ключи забыла."
                me "Вот, я их тебе принёс."
                play sound sfx_keys_rattle
                show sl smile pioneer at center with dspr
                sl "О, спасибо большое! Я их обыскалась уже!"
                sl "Если бы не ты, мне бы влетело от Ольги Дмитриевны!"
                $ ds_lp_sl += 1
                $ ds_sl_keys = False
            "Не отдавать":
                window show
                th "Да зачем? Может, эти ключи мне потребуются ещё."
            "Отцепить ключик себе":
                if skillcheck('interfacing', lvl_godly):
                    window show
                    inf "Ты ловко двигаешь пальцами у себя в кармане... "
                    window hide
                    $ renpy.pause(0.5)
                    window show
                    inf "И в итоге туда проваливается какой-то ключик."
                    $ ds_karma -= 5
                    $ ds_skill_points['interfacing'] += 1
                    inf "Остальное ты вынимаешь и протягиваешь Славе."
                    me "Cлавь, ты вчера в столовой ключи забыла..."
                    show sl surprise pioneer at center with dspr
                    sl "Правда? Спасибо, что вернул!"
                    play sound sfx_keys_rattle
                    $ ds_lp_sl += 1
                    $ ds_sl_keys = False
                    $ ds_some_key = True
                    show sl smile pioneer at center with dspr
                    emp "Она тебе благодарна."
                    play sound ds_sfx_mot
                    svf "А у тебя остался ключик! Только вот какой?"
                else:
                    window show
                    play sound sfx_keys_rattle
                    $ renpy.pause(0.5)
                    play sound ds_sfx_mot
                    inf "Но ключи слишком громко шумят, и Славя обращает внимание."
                    $ ds_skill_points['interfacing'] += 1
                    show sl serious pioneer at center with dspr
                    sl "Что за звук?"
                    window hide
                    menu:
                        "Сказать про ключи":
                            window show
                            me "Да я про ключи вспомнил, доставал их, чтобы тебе отдать."
                            show sl smile pioneer at center with dspr
                            sl "Правда? Спасибо, что вернул!"
                            play sound sfx_keys_rattle
                            $ ds_lp_sl += 1
                            $ ds_sl_keys = False
                            emp "Она тебе благодарна."
                        "Cоврать":
                            if skillcheck('drama', lvl_formidable):
                                window show
                                play sound ds_sfx_int
                                dra "Скажите, мессир, будто это кто-то другой проходил."
                                dra "И главное - покажите, что вы тоже ищете источник."
                                me "Не знаю, тут ходит кто-то, наверное. Или в лесу."
                                $ ds_skill_points['drama'] += 1
                                show sl normal pioneer at center with dspr
                                sl "А, ну ладно!"
                                dra "Про ключи лучше не говори."
                            else:
                                window show
                                play sound ds_sfx_int
                                dra "Это не вы! Это точно не вы!"
                                me "Этот звук не от меня!"
                                sl "Точно? Покажи, что у тебя в кармане!"
                                "Ты достаёшь ключи."
                                $ ds_skill_points['drama'] += 1
                                show sl angry pioneer at center with dspr
                                sl "Значит, ключи украл? А я тебя в столовую проводила..."
                                $ ds_lp_sl -= 1
                                me "Да ты просто их в столовой забыла, а я хотел вернуть."
                                sl "Ага, хотел... Отдавай их!"
                                play sound sfx_keys_rattle
                                "Тебе приходится их отдать."
                                play sound ds_sfx_psy
                                emp "Ей очень обидно, что ты хотел скрыть их от неё. Она же могла быть и наказана за потерю ключей."
    
    if (ds_passed_places == 3) and not ds_had_lunch:
        sl "Cлушай, я схожу пообедаю, а ты пока зайди без меня, хорошо?"
        sl "Я приду сюда же. Я быстро!"
        me "Ладно..."
        hide sl with dissolve
        $ ds_sl_gone = True
        jump ds_day2_pass_alone_clubs

    window show
    "Вы идёте к зданию кружков."
    play sound ds_sfx_psy
    esp "По правде говоря, тебе никогда особо не доставляла удовольствия общественная работа."
    esp "В школе ты всегда под любым предлогом пытался пропустить субботники, в институте тебя никак не привлекал студенческий совет."
    esp "Тебя не интересовали секции бокса, авиамоделирования или кройки и шитья."
    esp "Так что сюда ты приходишь лишь с целью отметиться.{w} Хотя, может, и попробуешь записаться хоть тут, вдруг будет интересно."

    stop ambience fadeout 2

    "Ты открываешь дверь, и вы входите."
    window hide

    play sound sfx_open_door_clubs

    $ renpy.pause(1)

    $ persistent.sprite_time = "day"
    scene bg int_clubs_male_day 
    with dissolve

    play ambience ambience_clubs_inside_day fadein 3

    window show
    "Внутри никого нет."
    play sound ds_sfx_int
    con "Комната представляет из себя что-то наподобие берлоги юного робототехника – повсюду валялись какие-то провода, нехитрые платы, микросхемы, на столе стоит осциллограф."
    "Из соседнего помещения слышатся голоса, и через секунду в комнату вошли двое пионеров."
    show el normal pioneer at cleft 
    show sh normal pioneer at cright 
    show sl normal pioneer at fright
    with dissolve
    play sound ds_sfx_int
    enc "В одном ты узнаёшь Электроника, второй же тебе был незнаком."
    el "Привет, Семен! А мы тебя ждали. Славя, тебе тоже привет!"
    sl "Привет, Электроник. Привет, Шурик."
    th "Кажется, он знает все и обо всех…"
    me "А чего вы меня ждали?"
    el "Ну как же, ты же пришел в наш клуб кибернетиков записываться, так?"
    "Он не даёт тебе ответить."
    show el smile pioneer at cleft   with dspr
    el "Знакомься, это Шурик, он у нас главный!"

    me "А вас в клубе этом только двое, я так полагаю?"
    show el normal pioneer at cleft   with dspr
    el "Ну, можешь считать, что уже трое."
    "Шурик подходит к тебе и уверенно протягивает руку."
    enc "Его лицо тебе кажется почему-то знакомым."
    if skillcheck('encyclopedia', lvl_easy, passive=True):
        enc "Точно, он же вылитый Шурик из комедий Гайдая!"
    else:
        enc "Хотя нет, показалось..."
    show sh normal_smile pioneer at cright   with dspr
    sh "Добро пожаловать!"
    me "Угу…"
    show sh normal pioneer at cright   with dspr
    el "Давай я тебе тут все покажу!{w} Ты не стесняйся, располагайся."
    me "Да нет, ребята, я вообще-то…"
    show sh normal_smile pioneer at cright   with dspr
    sh "Всегда рады новым членам."
    play music ds_ussr_anthem fadein 2
    enc "Он сказал это так, что в голове у тебя невольно заиграл гимн Советского Союза."
    enc "Удивительно, но ты еще помнишь слова – в первом классе у тебя была тетрадка, на обратной стороне которой они были напечатаны."
    stop music fadeout 2
    menu:
        "Записаться":
            th "Впрочем, новые знакомства мне точно не помешают."
            me "Да, давайте, записывайте меня!"
            sh "Отлично. Давай, кстати, сюда обходной лист."
            play sound ds_pen
            "Ты отдаёшь обходной лист, они записывают тебя в какой-то список и подписывают тебе его."
            sh "Вот, распишись тут."
            play sound ds_sfx_mot
            per_eye "Итак, члены клуба..."
            per_eye "1. ДЕМЬЯНЕНКО АЛЕКСАНДР"
            per_eye "2. CЫРОЕЖКИН СЕРГЕЙ"
            play sound ds_sfx_mot
            res "Значит, настоящее имя Электроника - Сергей..."
            per_eye "А вот и ты: 3. ПЁРСУНОВ СЕМЁН"
            play sound ds_pen
            "Ты ставишь свою подпись."
            show el laugh pioneer at cleft with dspr
            el "Приветствуем нового члена клуба кибернетиков!"
            show sl smile pioneer at fright with dspr
            sl "Молодец, что записался!"
            if not (ds_music_member or ds_sport_member):
                $ ds_lp_sl += 1
            $ ds_cyber_member = True
            $ ds_skill_points['interfacing'] += 1
        "Отказаться":
            me "Да нет, мне бы просто обходной лист подписать."
            show sh normal_smile pioneer at cright   with dspr
            show el grin pioneer at cleft   with dspr
            el "Так ты к нам запишись, и мы тебе его подпишем."
            "Он хитро улыбается."
            play sound ds_sfx_psy
            sug "Какой хитрец!"
            show sl angry pioneer at fright with dspr
            sl "Так, подпишите обходной уже! Не докучайте новенькому!"
            show sh upset pioneer at right with dspr
            sh "Ну подожди..."
            sl "Подписывайте!"
            play sound ds_sfx_psy
            emp "Она посмотрела на него так, что возражать Шурик не решается."

            stop ambience fadeout 2
            play sound ds_pen
            "Он поставил свою закорючку, и ты, поблагодарив Славю, с чистой совестью направляешься дальше."

    $ ds_passed_places += 1
    $ ds_visited_clubs = True
    jump ds_day2_pass_sl_main

label ds_day2_pass_sl_medic:
    $ persistent.sprite_time = "day"
    scene bg ext_aidpost_day 
    with dissolve
    show sl normal pioneer at center with dissolve

    play ambience ambience_camp_center_day fadein 3

    if ds_sl_keys:
        if ds_passed_places == 0:
            th "У меня ещё ключи... может, отдать их Славе?"
        else:
            th "Может, всё-таки отдать ключи Славе?"
        window hide
        menu:
            "Отдать ключи":
                window show
                me "Славя, ты вчера в столовой, кстати, ключи забыла."
                me "Вот, я их тебе принёс."
                play sound sfx_keys_rattle
                show sl smile pioneer at center with dspr
                sl "О, спасибо большое! Я их обыскалась уже!"
                sl "Если бы не ты, мне бы влетело от Ольги Дмитриевны!"
                $ ds_lp_sl += 1
                $ ds_sl_keys = False
            "Не отдавать":
                window show
                th "Да зачем? Может, эти ключи мне потребуются ещё."
            "Отцепить ключик себе":
                if skillcheck('interfacing', lvl_godly):
                    window show
                    inf "Ты ловко двигаешь пальцами у себя в кармане... "
                    window hide
                    $ renpy.pause(0.5)
                    window show
                    inf "И в итоге туда проваливается какой-то ключик."
                    $ ds_karma -= 5
                    $ ds_skill_points['interfacing'] += 1
                    inf "Остальное ты вынимаешь и протягиваешь Славе."
                    me "Cлавь, ты вчера в столовой ключи забыла..."
                    show sl surprise pioneer at center with dspr
                    sl "Правда? Спасибо, что вернул!"
                    play sound sfx_keys_rattle
                    $ ds_lp_sl += 1
                    $ ds_sl_keys = False
                    $ ds_some_key = True
                    show sl smile pioneer at center with dspr
                    emp "Она тебе благодарна."
                    play sound ds_sfx_mot
                    svf "А у тебя остался ключик! Только вот какой?"
                else:
                    window show
                    play sound sfx_keys_rattle
                    $ renpy.pause(0.5)
                    play sound ds_sfx_mot
                    inf "Но ключи слишком громко шумят, и Славя обращает внимание."
                    $ ds_skill_points['interfacing'] += 1
                    show sl serious pioneer at center with dspr
                    sl "Что за звук?"
                    window hide
                    menu:
                        "Сказать про ключи":
                            window show
                            me "Да я про ключи вспомнил, доставал их, чтобы тебе отдать."
                            show sl smile pioneer at center with dspr
                            sl "Правда? Спасибо, что вернул!"
                            play sound sfx_keys_rattle
                            $ ds_lp_sl += 1
                            $ ds_sl_keys = False
                            emp "Она тебе благодарна."
                        "Cоврать":
                            if skillcheck('drama', lvl_formidable):
                                window show
                                play sound ds_sfx_int
                                dra "Скажите, мессир, будто это кто-то другой проходил."
                                dra "И главное - покажите, что вы тоже ищете источник."
                                me "Не знаю, тут ходит кто-то, наверное. Или в лесу."
                                $ ds_skill_points['drama'] += 1
                                show sl normal pioneer at center with dspr
                                sl "А, ну ладно!"
                                dra "Про ключи лучше не говори."
                            else:
                                window show
                                play sound ds_sfx_int
                                dra "Это не вы! Это точно не вы!"
                                me "Этот звук не от меня!"
                                sl "Точно? Покажи, что у тебя в кармане!"
                                "Ты достаёшь ключи."
                                $ ds_skill_points['drama'] += 1
                                show sl angry pioneer at center with dspr
                                sl "Значит, ключи украл? А я тебя в столовую проводила..."
                                $ ds_lp_sl -= 1
                                me "Да ты просто их в столовой забыла, а я хотел вернуть."
                                sl "Ага, хотел... Отдавай их!"
                                play sound sfx_keys_rattle
                                "Тебе приходится их отдать."
                                play sound ds_sfx_psy
                                emp "Ей очень обидно, что ты хотел скрыть их от неё. Она же могла быть и наказана за потерю ключей."
    
    if (ds_passed_places == 3) and not ds_had_lunch:
        sl "Cлушай, я схожу пообедаю, а ты пока зайди без меня, хорошо?"
        sl "Я приду сюда же. Я быстро!"
        me "Ладно..."
        hide sl with dissolve
        $ ds_sl_gone = True
        jump ds_day2_pass_alone_clubs

    window show
    play sound ds_sfx_fys
    edr "Ты решительно не понимаешь, что тебе делать в медпункте."
    edr "Здоровье вроде не шалит, тем более местный свежий воздух явно пошел тебе на пользу, и самочувствие было куда бодрее, чем обычно."
    th "Но раз надо так надо."
    sl "Ты справишься тут сам? Я лучше заходить не буду."
    me "Ладно..."
    "Ты входишь."
    window hide

    stop ambience fadeout 2

    play sound sfx_open_door_1

    $ renpy.pause(1)

    $ persistent.sprite_time = "day"
    scene bg int_aidpost_day 
    with dissolve

    play ambience ambience_medstation_inside_day fadein 3

    window show
    th "Обычный такой медпункт, у нас в школе был примерно такой же."
    show cs normal stethoscope at center   with dissolve

    play music ds_cs_theme fadein 5

    "За столом сидит женщина средних лет."
    "Она бросает на меня пристальный, оценивающий взгляд, и продолжила что-то писать."
    csp "Ну, здравствуй… пионер."
    "Говорит она, не отрываясь от своего занятия."
    me "Добрый день… Мне бы вот…"
    csp "Ты присаживайся."
    "Ты оглядываешь комнату."
    csp "На кушеточку."
    "Ты садишься."
    csp "Раздевайся."
    "Все это она говорит совершенно ровным тоном."
    me "А зачем?.."
    csp "Смотреть тебя будем, слушать, здоровье проверять."
    show cs smile stethoscope at center   with dspr
    csp "Меня, кстати, зовут Виолетта Церновна, но ты меня можешь звать просто Виолой."

    "Она поворачивается в твою сторону."
    cs "Ну, чего сидишь? Раздевайся."
    me "Да я не жалуюсь ни на что. Мне бы вот…"
    "Ты аккуратно протягиваешь ей листок."
    cs "Потом."
    show cs smile at center   with dissolve
    "Она снимает с шеи стетоскоп и, кажется, намеревается тебя им препарировать."
    window hide

    stop music fadeout 3
    play sound sfx_knock_door7_polite

    $ renpy.pause(1)

    window show
    "Но тут в дверь постучали."
    show cs normal at center   with dspr
    "Медсестра нехотя отвечает:"
    cs "Входите!"

    play sound sfx_open_door_strong
    play music music_list['eternal_longing'] fadein 5

    "Моментально дверь распахнулась, и в комнату вбегает Электроник."
    show el fingal pioneer far at left    with dissolve   
    show cs normal at center   with dspr
    el "Здрасьте! Я тут это… На футболе упал. Глупости, конечно, я бы и так, но меня Ольга Дмитриевна…"
    "У Электроника под глазом красуется здоровенный фингал."
    play sound ds_sfx_int
    vic "Что-то сомнительно, что такой можно заработать на футболе."
    cs "Садись, сейчас посмотрим."
    show cs normal glasses at center   with dissolve
    cs "А ты давай сюда свой обходной."
    queue sound ds_pen
    queue sound ds_stamp
    "Медсестра быстро подписывает его, ставит печать и продолжает:"
    show cs smile glasses at center   with dspr
    cs "Если что заболит – сразу ко мне… пионер."

    stop ambience fadeout 2
    stop music fadeout 3

    "Ты ничего не отвечаешь и выходишь, закрыв за собой дверь."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_aidpost_day 
    with dissolve
    show sl normal pioneer at center with dissolve

    window show
    sl "Ну как, всё хорошо?"
    me "Медсестра здесь, конечно, еще та…"
    sl "Да, есть такое..."
    $ ds_skill_points['instinct'] += 1
    window hide

    $ ds_passed_places += 1
    $ ds_visited_medic = True
    jump ds_day2_pass_sl_main

label ds_day2_pass_sl_library:
    play ambience ambience_camp_center_day fadein 3
    $ persistent.sprite_time = "day"
    scene bg ext_library_day 
    with dissolve

    show sl normal pioneer at center with dspr
    window show
    if ds_sl_keys:
        if ds_passed_places == 0:
            th "У меня ещё ключи... может, отдать их Славе?"
        else:
            th "Может, всё-таки отдать ключи Славе?"
        window hide
        menu:
            "Отдать ключи":
                window show
                me "Славя, ты вчера в столовой, кстати, ключи забыла."
                me "Вот, я их тебе принёс."
                play sound sfx_keys_rattle
                show sl smile pioneer at center with dspr
                sl "О, спасибо большое! Я их обыскалась уже!"
                sl "Если бы не ты, мне бы влетело от Ольги Дмитриевны!"
                $ ds_lp_sl += 1
                $ ds_sl_keys = False
            "Не отдавать":
                window show
                th "Да зачем? Может, эти ключи мне потребуются ещё."
            "Отцепить ключик себе":
                if skillcheck('interfacing', lvl_godly):
                    window show
                    inf "Ты ловко двигаешь пальцами у себя в кармане... "
                    window hide
                    $ renpy.pause(0.5)
                    window show
                    inf "И в итоге туда проваливается какой-то ключик."
                    $ ds_karma -= 5
                    $ ds_skill_points['interfacing'] += 1
                    inf "Остальное ты вынимаешь и протягиваешь Славе."
                    me "Cлавь, ты вчера в столовой ключи забыла..."
                    show sl surprise pioneer at center with dspr
                    sl "Правда? Спасибо, что вернул!"
                    play sound sfx_keys_rattle
                    $ ds_lp_sl += 1
                    $ ds_sl_keys = False
                    $ ds_some_key = True
                    show sl smile pioneer at center with dspr
                    emp "Она тебе благодарна."
                    play sound ds_sfx_mot
                    svf "А у тебя остался ключик! Только вот какой?"
                else:
                    window show
                    play sound sfx_keys_rattle
                    $ renpy.pause(0.5)
                    play sound ds_sfx_mot
                    inf "Но ключи слишком громко шумят, и Славя обращает внимание."
                    $ ds_skill_points['interfacing'] += 1
                    show sl serious pioneer at center with dspr
                    sl "Что за звук?"
                    window hide
                    menu:
                        "Сказать про ключи":
                            window show
                            me "Да я про ключи вспомнил, доставал их, чтобы тебе отдать."
                            show sl smile pioneer at center with dspr
                            sl "Правда? Спасибо, что вернул!"
                            play sound sfx_keys_rattle
                            $ ds_lp_sl += 1
                            $ ds_sl_keys = False
                            emp "Она тебе благодарна."
                        "Cоврать":
                            if skillcheck('drama', lvl_formidable):
                                window show
                                play sound ds_sfx_int
                                dra "Скажите, мессир, будто это кто-то другой проходил."
                                dra "И главное - покажите, что вы тоже ищете источник."
                                me "Не знаю, тут ходит кто-то, наверное. Или в лесу."
                                $ ds_skill_points['drama'] += 1
                                show sl normal pioneer at center with dspr
                                sl "А, ну ладно!"
                                dra "Про ключи лучше не говори."
                            else:
                                window show
                                play sound ds_sfx_int
                                dra "Это не вы! Это точно не вы!"
                                me "Этот звук не от меня!"
                                sl "Точно? Покажи, что у тебя в кармане!"
                                "Ты достаёшь ключи."
                                $ ds_skill_points['drama'] += 1
                                show sl angry pioneer at center with dspr
                                sl "Значит, ключи украл? А я тебя в столовую проводила..."
                                $ ds_lp_sl -= 1
                                me "Да ты просто их в столовой забыла, а я хотел вернуть."
                                sl "Ага, хотел... Отдавай их!"
                                play sound sfx_keys_rattle
                                "Тебе приходится их отдать."
                                play sound ds_sfx_psy
                                emp "Ей очень обидно, что ты хотел скрыть их от неё. Она же могла быть и наказана за потерю ключей."
    
    if (ds_passed_places == 3) and not ds_had_lunch:
        sl "Cлушай, я схожу пообедаю, а ты пока зайди без меня, хорошо?"
        sl "Я приду сюда же. Я быстро!"
        me "Ладно..."
        hide sl with dissolve
        $ ds_sl_gone = True
        jump ds_day2_pass_alone_library

    play sound ds_sfx_psy
    vol "Вообще, ты, конечно, любишь читать, но просиживать днями в библиотеке при нынешних обстоятельствах в твои планы не входит, так что ты решил побыстрее пройти этот чекпойнт."
    window hide

    stop ambience fadeout 3

    $ persistent.sprite_time = "day"
    scene bg int_library_day 
    with dissolve
    show sl normal pioneer at center with dissolve

    play ambience ambience_library_day fadein 3

    window show
    play sound ds_sfx_psy
    ine "Когда ты заходишь внутрь, у тебя в голове всплывает воспоминание из детства."
    ine "Оно очень яркое."
    ine "Тебе лет 7 или 8, ты с мамой в библиотеке."
    ine "Пока она выбирает какие-то книжки, которые тебе понадобятся для учебы, ты сидишь и разглядываешь местную подборку комиксов."
    ine "Тогда тебе было сложно понять, почему их здесь так много и почему нельзя забрать часть домой."
    ine "Понятия коллективной собственности тогда для тебя не существовало."
    ine "Впрочем, как и понятия собственности вообще."
    ine "Тем более странным было это воспоминание сейчас, когда ты находишься в том самом отдельно взятом пионерлагере, где коммунизм таки удалось построить за 3 года."
    "Повсюду висит огромное количество советской символики, а на полках книги в основном соответствующей тематики."
    vol "Читать их ты никак не планировал – знакомство с полным собранием сочинений Маркса было одной из последних вещей на Земле, которая пришла бы тебе в голову."
    vol "Надо найти библиотекаря."
    "Оказалось это не так сложно – она спит на столе рядом с тобой."
    $ ds_met['mz'] = 1
    window hide

    scene cg d2_micu_lib 
    with dissolve

    window show
    "Ты пригляделся.{w} Короткая стрижка, толстые очки, довольно приятное лицо."
    play sound ds_sfx_psy
    th "Она так мило спит..."

    scene bg int_library_day 
    with dissolve
    show sl normal pioneer at center with dissolve
    sl "Жень, просыпайся, тут новенький с обходным."
    $ ds_met['mz'] = 2
    show mz bukal glasses pioneer far at right with dissolve
    mz "А, да... сейчас..."

    play sound sfx_knock_door2

    "В дверь стучат."
    th "Какая отличная привычка – стучать.{w} Надо и мне ее взять на вооружение."

    play sound sfx_open_door_clubs_2

    "В дверь входит Лена."
    show un normal pioneer at cleft   with dissolve
    un "Ой…"
    show un shy pioneer at cleft   with dspr
    me "Привет!"
    "Ты улыбаешься."
    un "Привет, а я вот книжку пришла отдать…"
    sl "Привет, Лена!"
    play sound ds_sfx_mot
    per_eye "У нее в руках «Унесенные ветром», которую ты видел вчера."

    show mz normal glasses pioneer far at cright    with dissolve
    mz "Так, давай быстро сюда обходной."
    "Ты отдаёшь обходной."
    queue sound ds_pen
    queue sound ds_stamp
    "Она быстро расписывается, ставит печать и протягивает тебе его обратно."
    mz "Получать читательский билет будем?"
    window hide
    menu:
        "Согласиться":
            window show
            me "Да, давай...те."
            "Женя залезает в стол, достаёт какой-то листок..."
            mz "Фамилия, имя?"
            me "Пёрсунов Семён..."
            play sound ds_pen
            "Она записывает сведения в билет, а затем отдаёт тебе."
            mz "Бери!"
            "Ты забираешь бумажку и складываешь в карман штанов."
            show sl smile pioneer at center with dspr
            sl "Молодец, так тянешься к знаниям... или просто любишь читать!"
            $ ds_lp_sl += 1
            $ ds_library_member = True
            $ ds_skill_points['encyclopedia'] += 1
            mz "Cледующий!"
        "Отказаться":
            window show
            me "Нет, спасибо."
            mz "Тогда следующий!"
    play sound ds_sfx_psy
    emp "Вид у нее такой, что дальнейший разговор кажется совершенно неуместным."
    "Лена подходит к ней и отдаёт книжку, а ты благодаришь Женю и выходишь."
    window hide

    stop ambience fadeout 2

    $ ds_passed_places += 1
    $ ds_visited_library = True
    jump ds_day2_pass_sl_main

label ds_day2_pass_sl_lunch:
    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_away_day 
    with dissolve

    show sl normal pioneer at center with dissolve

    window show
    "Вы со Славей всё же решаете сходить пообедать."
    th "Обходной лист никуда не денется, потом быстренько подпишу, а вот мой желудок явно ждать до ужина не намерен."
    "С такими мыслями ты входишь в столовую."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_day 
    with dissolve

    show sl normal pioneer at center with dissolve

    play ambience ambience_dining_hall_empty fadein 3

    window show
    "Там почти никого нет – видимо, большинство пионеров уже пообедало."
    "Вы встаёте в очередь за едой."
    show ck normal at center with dissolve
    show sl normal pioneer at right with dissolve
    
    "Впрочем, очередью это назвать нельзя, ибо вы тут вдвоём."
    window hide
    menu:
        "Пойти первым":
            window show
            me "Спасибо!"
            "Забрав еду, ты пропускаешь Славю."
            "Она тоже берёт."
        "Пропустить Славю":
            window show
            me "Прошу, проходи первая."
            show sl smile pioneer at right with dspr
            sl "Ой, спасибо!"
            $ ds_lp_sl += 1
            "Она забирает еду, затем еду берёшь и ты."
            me "Спасибо!"
    hide ck with dissolve
    "Вы принимаетесь есть."
    jump ds_day2_lunch_dialogue

label ds_day2_lunch_dialogue:
    if ds_sl_keys:
        th "Ещё же ключи..."
    window hide
    menu:
        "Отдать ключи" if ds_sl_keys:
            window show
            me "Слушай, Славь, ты вчера, когда отводила меня сюда, ключи оставила..."
            play sound sfx_keys_rattle
            show sl smile pioneer at center with dissolve
            sl "Правда? Спасибо большое!"
            sl "А то меня бы отругала Ольга Дмитриевна, обнаружь она, что ключи я потеряла."
            $ ds_lp_sl += 1
            $ ds_sl_keys = False
            jump ds_day2_lunch_dialogue
        "Поговорить о Славе":
            window show
            me "А откуда ты приехала?"
            show sl normal pioneer at center   with dissolve
            sl "Я с севера."
            me "А поточнее?"
            show sl smile pioneer at center   with dspr
            sl "Холодного севера."
            "Она смотрит на тебя и улыбается."
            play sound ds_sfx_int
            rhe "Как информативно!"
            rhe "Возможно, стоит попробовать действовать по-другому."
            window hide
            menu:
                "Надавить":
                    window show
                    me "И всё-таки, откуда ты?"
                    show sl angry pioneer at center with dspr
                    sl "Почему тебе так важно это? Из деревни я, ты в любом случае не знаешь всех деревень."
                "Поинтересоваться увлечениями":
                    window show
                    me "А что тебе нравится?"
                    sl "В смысле?"
                    me "Ну, твои увлечения?"
                    show sl smile2 pioneer at center   with dspr
                    sl "Ааа… Я природу люблю."
                    rhe "Странно, но сейчас она почему-то немногословна."
                    me "Природу?.. Ясно.{w} Хочешь стать натуралистом?"
                    sl "Скорее краеведом. Всегда интересовалась историей родной страны."
                    play sound ds_sfx_int
                    dra "Это действительно похоже на нее."
                    dra "Казалось, из всех местных обитателей она единственная, кто не скрывает в себе никаких загадок."
                "Не говорить ничего":
                    window show
            play sound ds_sfx_psy
            emp "Может быть, ее тоже как-то сюда забросило, как и тебя, и она просто, так же, как и ты, пока не доверяет никому до конца."
            play sound ds_sfx_int
            rhe "Попробуй прощупать почву аккуратно."
            rhe "Cпроси, например, почему она именно сюда поехала."
            window hide
            menu:
                "Cпросить":
                    window show
                    me "А почему ты именно в этот лагерь поехала?"
                    show sl normal pioneer at center   with dspr
                    sl "Родителям путевку на работе дали."
                    th "Опять облом."
                    me "Ну, предположим, если бы у тебя был выбор?"
                    sl "Здесь хорошо.{w} Не думаю, что выбрала бы какое-нибудь другое место – здесь кажется, что ты становишься каким-то другим человеком!"
                    "Мне такого совсем не казалось."
                    me "В смысле «другим»?"
                    sl "Ну, столько возможностей, столькому можно научиться, стольких людей узнать!"
                    rhe "Сейчас она рассуждает точно так же, как и Ольга Дмитриевна."
                    play sound ds_sfx_fys
                    hfl "И это тебя настораживает."
                    stop music fadeout 3
                "Не спрашивать":
                    window show
            $ ds_skill_points['rhetoric'] += 1
            $ ds_sl_interrogate = True
            "Тут оказывается, что вы уже доели."
            show sl normal pioneer at center with dspr
            sl "Ну что, пойдём дальше?"
            me "Да..."
            scene bg ext_dining_hall_away_day
            with dissolve
        "Поговорить о лагере":
            window show
            me "Слушай, а мы ещё сколько тут проведём?"
            show sl surprise pioneer at center with dspr
            sl "Ты чего, забыл?"
            show sl normal pioneer at center with dspr
            sl "А, точно, ты же прибыл с опозданием!"
            sl "Так, сегодня десятое августа... смена оканчивается восемнадцатого..."
            sl "Да, мы тут ещё девять дней проведём!"
            me "Вот как... спасибо."
            me "А чем мы будем заниматься?"
            show sl surprise pioneer at center with dspr
            play sound ds_sfx_fys
            hfl "Ты всё больше в её глазах выглядишь слабоумным."
            sl "Ты что, никогда в лагерях не был?"
            show sl normal pioneer at center with dspr
            sl "Ну смотри: во-первых, мы работаем на благо общества, как и положено пионерам."
            play sound ds_sfx_int
            enc "Тебе её речи очень напоминают коммунистическую агитацию."
            sl "Но у нас есть и возможности для досуга: кружки, где можно заниматься любимым делом..."
            play sound ds_sfx_int
            con "...в узких рамках, определённых администрацией."
            sl "Можно и просто погулять или искупаться на пляже."
            sl "Ещё регулярно проводятся всякие мероприятия."
            sl "Кстати, на завтра в лагере запланирована дискотека!"
            sl "А через три дня будет поход!"
            show sl serious pioneer at center with dspr
            sl "Я тебя не спрашиваю, придёшь ли ты, так как явка обязательна!"
            play sound ds_sfx_int
            lgc "Какой же это досуг, если он обязателен?"
            window hide
            menu:
                "Заметить несостыковку":
                    window show
                    me "Но ведь это уже не досуг, а обязаловка!"
                    show sl angry pioneer at center with dspr
                    sl "А кто тебе сказал, что это досуг?"
                    sl "Это мероприятия, направленные на развитие коллективного духа!"
                    play sound ds_sfx_psy
                    esp "История (которая тут только должна произойти лет через пять) явно показывает, что такой способ неэффективен."
                    sl "И вообще, тут правила такие, что посещение обязательно!"
                    sl "Правила надо соблюдать!"
                    play sound ds_sfx_psy
                    aut "Ты уже мог понять, что она тут по сути второй человек после вожатой."
                "Принять":
                    pass
            "Тут оказывается, что вы уже всё съели."
            show sl normal pioneer at center with dspr
            sl "Ну что, пойдём дальше?"
            me "Пойдём..."
            scene bg ext_dining_hall_away_day 
            with dissolve
        "Есть молча":
            window show
            "Вы молча съедаете свои обеды."
            sl "Так, всё, идём подписывать обходной дальше!"
            scene bg ext_dining_hall_away_day 
            with dissolve
            "Ты, соглашаясь с ней, выходишь из столовой, Славя за тобой."
    $ ds_had_lunch = True
    jump ds_day2_pass_sl_main

label ds_day2_pass_sl_sport:
    scene bg ext_playground_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    window show
    show sl normal pioneer at center with dspr
    if ds_sl_keys:
        if ds_passed_places == 0:
            th "У меня ещё ключи... может, отдать их Славе?"
        else:
            th "Может, всё-таки отдать ключи Славе?"
        window hide
        menu:
            "Отдать ключи":
                window show
                me "Славя, ты вчера в столовой, кстати, ключи забыла."
                me "Вот, я их тебе принёс."
                play sound sfx_keys_rattle
                show sl smile pioneer at center with dspr
                sl "О, спасибо большое! Я их обыскалась уже!"
                sl "Если бы не ты, мне бы влетело от Ольги Дмитриевны!"
                $ ds_lp_sl += 1
                $ ds_sl_keys = False
            "Не отдавать":
                window show
                th "Да зачем? Может, эти ключи мне потребуются ещё."
            "Отцепить ключик себе":
                if skillcheck('interfacing', lvl_godly):
                    window show
                    inf "Ты ловко двигаешь пальцами у себя в кармане... "
                    window hide
                    $ renpy.pause(0.5)
                    window show
                    inf "И в итоге туда проваливается какой-то ключик."
                    $ ds_karma -= 5
                    $ ds_skill_points['interfacing'] += 1
                    inf "Остальное ты вынимаешь и протягиваешь Славе."
                    me "Cлавь, ты вчера в столовой ключи забыла..."
                    show sl surprise pioneer at center with dspr
                    sl "Правда? Спасибо, что вернул!"
                    play sound sfx_keys_rattle
                    $ ds_lp_sl += 1
                    $ ds_sl_keys = False
                    $ ds_some_key = True
                    show sl smile pioneer at center with dspr
                    emp "Она тебе благодарна."
                    play sound ds_sfx_mot
                    svf "А у тебя остался ключик! Только вот какой?"
                else:
                    window show
                    play sound sfx_keys_rattle
                    $ renpy.pause(0.5)
                    play sound ds_sfx_mot
                    inf "Но ключи слишком громко шумят, и Славя обращает внимание."
                    $ ds_skill_points['interfacing'] += 1
                    show sl serious pioneer at center with dspr
                    sl "Что за звук?"
                    window hide
                    menu:
                        "Сказать про ключи":
                            window show
                            me "Да я про ключи вспомнил, доставал их, чтобы тебе отдать."
                            show sl smile pioneer at center with dspr
                            sl "Правда? Спасибо, что вернул!"
                            play sound sfx_keys_rattle
                            $ ds_lp_sl += 1
                            $ ds_sl_keys = False
                            emp "Она тебе благодарна."
                        "Cоврать":
                            if skillcheck('drama', lvl_formidable):
                                window show
                                play sound ds_sfx_int
                                dra "Скажите, мессир, будто это кто-то другой проходил."
                                dra "И главное - покажите, что вы тоже ищете источник."
                                me "Не знаю, тут ходит кто-то, наверное. Или в лесу."
                                $ ds_skill_points['drama'] += 1
                                show sl normal pioneer at center with dspr
                                sl "А, ну ладно!"
                                dra "Про ключи лучше не говори."
                            else:
                                window show
                                play sound ds_sfx_int
                                dra "Это не вы! Это точно не вы!"
                                me "Этот звук не от меня!"
                                sl "Точно? Покажи, что у тебя в кармане!"
                                "Ты достаёшь ключи."
                                $ ds_skill_points['drama'] += 1
                                show sl angry pioneer at center with dspr
                                sl "Значит, ключи украл? А я тебя в столовую проводила..."
                                $ ds_lp_sl -= 1
                                me "Да ты просто их в столовой забыла, а я хотел вернуть."
                                sl "Ага, хотел... Отдавай их!"
                                play sound sfx_keys_rattle
                                "Тебе приходится их отдать."
                                play sound ds_sfx_psy
                                emp "Ей очень обидно, что ты хотел скрыть их от неё. Она же могла быть и наказана за потерю ключей."
    
    if (ds_passed_places == 3) and not ds_had_lunch:
        sl "Cлушай, я схожу пообедаю, а ты пока зайди без меня, хорошо?"
        sl "Я приду сюда же. Я быстро!"
        me "Ладно..."
        hide sl with dissolve
        $ ds_sl_gone = True
        jump ds_day2_pass_alone_sport
    "Вы подходите к спортплощадке."
    sl "Нам туда."
    "Ты направляешься за Славей."
    scene bg ds_int_sporthall_day with dissolve
    show us smile sport far at center with dspr
    show sl normal pioneer at right with dissolve
    "Зайдя в спортзал, ты видишь Ульяну бегающей по залу."
    sl "Осторожней, Ульяна!"
    us "Есть, гржнначальник!"
    me "Ульяна, а где я тут могу подписать обходной лист?"
    us "Давай его сюда!"
    show us laugh sport at center with dspr
    play sound ds_sfx_int
    dra "По всей видимости, она опять хочет вас провести."
    us "Я тут спортклубом руковожу!"
    play sound ds_sfx_mot
    res "Так ей же не более 14 лет! И уже руководит чем-то?"
    menu:
        "Принять":
            me "А... хорошо."
            sl "Молодец, Ульяна, хорошо справляешься!"
        "Усомниться":
            me "Ты? Ты же ещё маленькая!"
            show us dontlike sport at center with dspr
            us "И ничего не маленькая! Мне сама Ольга Дмитриевна доверила!"
            sl "Да, это так. Ольга Дмитриевна решила использовать энергию Ульяны на пользу."
            $ ds_lp_us -= 1
    show us normal sport at center with dspr
    us "Кстати, не хочешь записаться к нам?"
    if not ds_caught_us:
        show us laugh2 sport at center with dspr
        us "Может, и сможешь меня тогда догнать!"
    menu:
        "Записаться":
            me "Давай!"
            show us smile sport at center with dspr
            us "Вот, бери листик и записывайся сюда!"
            "Ты вносишь своё имя в данный тебе клочок бумаги."
            me "Вот, а теперь подпиши мне обходной."
            us "Давай сюда!"
            play sound ds_pen
            "Она подписывает обходной и отдаёт лист тебе."
            play sound ds_sfx_mot
            per_eye "СОВЕТОВА У.И. {w}Теперь мы знаем её фамилию!"
            me "Cпасибо!"
            show us laugh sport
            us "Только не забывай регулярно приходить сюда!"
            sl "Не забудет!"
            show sl smile pioneer at right with dspr
            sl "А ты молодец!"
            if not (ds_music_member or ds_cyber_member):
                $ ds_lp_sl += 1
            $ ds_sport_member = True
            $ ds_lp_us += 1
            "Под эти слова вы выходите из зала."
        "Отказаться":
            me "Нет, спасибо... мне просто нужен обходной лист."
            show us dontlike sport at center with dspr
            us "Ну и ладно, давай сюда свою бумажку!"
            play sound ds_pen
            "Она подписывает обходной и отдаёт лист тебе."
            play sound ds_sfx_mot
            per_eye "СОВЕТОВА У.И. {w}Теперь мы знаем её фамилию!"
            me "Cпасибо!"
            "И вы уходите."
    $ ds_passed_places += 1
    $ ds_visited_sport = True
    jump ds_day2_pass_alone_main

label ds_day2_pass_un_music:
    play ambience ambience_camp_center_day fadein 3

    $ persistent.sprite_time = "day"
    scene bg ext_musclub_day 
    with dissolve

    if (ds_passed_places == 3) and not ds_had_lunch:
        show un shy pioneer at center with dissolve
        un "Я схожу, пообедаю пока..."
        window hide
        menu:
            "Отпустить":
                me "Ладно..."
                hide un with dissolve
                jump ds_day2_pass_alone_music
            "Остановить":
                if skillcheck('suggestion', lvl_up_medium):
                    window show
                    sug "Вы быстро обойдёте всё остальное и сможете поесть."
                    me "Нет, подожди... мы быстренько! И сходим пообедаем."
                    un "Ладно..."
                    $ ds_lp_un -= 1
                else:
                    window show
                    sug "Ты не знаешь, что сказать - она же определённо хочет есть."
                    me "Ну, останься..."
                    show un angry pioneer at center with dspr
                    un "Нет, я пойду."
                    hide un with dissolve
                    $ ds_lp_un -= 1
                    jump ds_da2_pass_alone_music
    show un normal pioneer at center with dissolve

    window show
    "Музыкальный клуб располагается на некотором расстоянии от остальных построек лагеря."
    "Снаружи он представляет из себя небольшое одноэтажное здание."
    play sound ds_sfx_psy
    vol "Не раздумывая, вы заходите."
    window hide

    stop ambience fadeout 2
    play sound sfx_open_door_2

    $ renpy.pause(1)

    $ persistent.sprite_time = "day"
    scene bg int_musclub_day 
    with dissolve
    show un normal pioneer at center with dissolve

    play ambience ambience_music_club_day fadein 3

    window show
    play sound ds_sfx_int
    enc "Внутри оказывается полный набор музыкальных инструментов, на любой вкус и слух – барабаны, гитары и даже настоящий рояль."
    enc "Некоторое время твоё внимание плотно приковано к ним – хочется понять, из какого они примерно временного периода..."
    play sound ds_sfx_mot
    per_hea "Но неожиданно под роялем послышалось какое-то копошение."
    window hide

    scene cg ds_day2_mi_piano1
    with dissolve

    play music music_list["so_good_to_be_careless"] fadein 5
    $ ds_met['mi'] = 1

    window show
    "Ты наклоняешься и видишь девочку, которая, кажется, что-то искала."
    play sound ds_sfx_fys
    ins "Она стоит на четвереньках в такой пикантной позе..."
    menu:
        "Сдержать порывы":
            window show
            me "Простите…"
        "Начать приставать":
            if skillcheck('instinct', lvl_easy):
                window show
                ins "Внизу у тебя встаёт твой ствол..."
                ins "Ты подходишь к ней и прижимаешься ей к юбке..."
                un "Семён?.."
                $ ds_lp_un -= 1
                play sound ds_sfx_mot
                res "Но она тебя замечает!"
            else:
                window show
                ins "Ты бы и начал к ней приставать, но тут Лена..."
                "Твои неуклюжие движения привлекают внимание девочки."
            $ ds_skill_points['instinct'] += 1
    window hide

    scene cg ds_day2_mi_piano2
    with dissolve

    window show
    mip "Ааа! Кто здесь?"
    window hide

    play sound sfx_piano_head_bump
    with vpunch

    $ renpy.pause(1)

    window show
    "Она пытается вскочить, но днище рояля стало для нее непреодолимой преградой."
    mip "Ой!"
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_musclub_day 
    with dissolve

    show mi shocked pioneer at center   with dissolve
    show un scared pioneer at right with dissolve
    window show
    "С трудом, но она все же выбирается."
    me "Извини, что напугал…"
    show mi normal pioneer at center   with dspr
    mip "Да ничего! Вижу, у тебя обходной, новенький, значит?"
    me "А? Да."
    show mi smile pioneer at center   with dspr
    mip "Меня Мику зовут."
    mip "Привет, Лена, кстати!"
    show un shy pioneer at center with dspr
    un "Привет..."
    $ ds_met['mi'] = 2
    play sound ds_sfx_int
    enc "Тебе её имя почему-то кажется знакомым."
    if skillcheck('encyclopedia', lvl_medium, passive=True):
        enc "Точно, Мику существует и в твоём мире..."
        enc "В качестве так называемого «вокалоида» - компьютерной программы, симулирующей голос певицы."
        enc "А тут вот, вполне реальная девочка."
        play sound ds_sfx_int
        rhe "Только ей об этом вообще не стоит говорить."
    else:
        enc "Нет, показалось. Ты никогда не слышал имени Мику."

    mi "Нет, честно-честно! Никто не верит, а меня правда так зовут. Просто у меня мама из Японии. Папа с ней познакомился, когда строил там… Ну, то есть не строил – он у меня инженер…"
    mi "Короче, атомную станцию! Или плотину… Или мост… Ну, неважно!"
    play sound ds_sfx_mot
    res "Она говорит с такой скоростью, что половину слов ты не успеваешь разбирать."
    menu:
        "Сделать комплимент":
            me "Да... а ты прекрасно выглядишь, кстати."
            $ ds_lp_mi += 1
            show mi shy pioneer at center with dspr
            show un sad pioneer at right with dspr
            mi "Что ты говоришь? Ты правда считаешь, что я прекрасно выгляжу? А впрочем, мне все так говорят. Я почему-то очень-очень привлекаю всех парней."
            play sound ds_sfx_psy
            emp "Только вот Лене это слышать не сильно приятно, тем более что ей ты такого не говорил."
            $ ds_lp_un -= 1
            show mi smile pioneer at center with dspr
            mi "Ой, а как тебя зовут, кстати? Наверное, у тебя и имя должно быть каким-нибудь красивым!"
        "Высказать насчёт болтливости":
            me "Слушай, а ты всегда такая болтливая?"
            show mi sad pioneer at center with dspr
            mi "Да, есть у меня такое, совсем-совсем не знаю, что с этим делать. Все-все из-за этого раздражаются, даже ты... а как тебя зовут, кстати?"
            $ ds_lp_mi -= 1
            $ ds_karma -= 5
            play sound ds_sfx_psy
            emp "Она старается изобразить, будто её вообще не задели твои слова, хотя это далеко не так."
        "Промолчать":
            pass
    me "А я Семен."
    show mi happy pioneer at center   with dspr
    mi "Отлично! Не хочешь к нам в клуб вступить? Правда, нас тут пока только двое: я и Алиса-тян, но вместе мы будем втроём! Ты на чем-нибудь играть умеешь?"
    show un angry2 pioneer at right with dspr
    show un normal pioneer at right with dspr
    play sound ds_sfx_mot
    res "Ты замечаешь, что на миг настроение Лены изменилось."
    play sound ds_sfx_psy
    emp "Очевидно, это как-то связано с Алисой. Поговори об этом позже."
    th "Уже в период моего «отшельничества» я купил себе гитару и по самоучителям выучил пару аккордов, но потом забросил это дело, как и любое другое, которое требовало больше нескольких часов."
    play sound ds_sfx_int
    con "А тут ты наверняка сможешь подтянуть свои навыки и сыграть что-нибудь прекрасное!"
    show un smile pioneer at center with dspr
    un "Да, я уверена, у тебя получится!"
    window hide
    menu:
        "Записаться":
            me "Да, давай!"
            mi "Отлично, сейчас я тебя запишу к нам, Семён-кун. Я так рада, что ты присоединился к нам. Алиса-тян наверняка тоже обрадуется!"
            play sound ds_pen
            "Она достаёт листок и вписывает туда твои имя..."
            mi "А фамилия у тебя какая? А, точно, давай обходной, его заодно подпишу и спишу фамилию!"
            queue sound ds_mi_sign
            queue sound ds_pen
            "Ты отдаёшь ей свой обходной, она ставит подпись (вернее, печать, как истинная японка) там и дописывает в список членов клуба твою фамилию."
            mi "Распишись тут, пожалуйста."
            play sound ds_sfx_mot
            per_eye "Ты просматриваешь список, теперь состоящий из трёх человек."
            per_eye "1. ХАЦУНЕ МИКУ, {w}2. ДВАЧЕВСКАЯ АЛИСА..."
            per_eye "И вот наконец ты видишь себя: 3. ПЁРСУНОВ СЕМЁН."
            play sound ds_pen
            "Ты ставишь свою подпись."
            mi "Как же отлично. Как-нибудь обязательно надо будет вместе что-нибудь сыграть! Как раз на прощальном концерте через восемь дней и сыграем!"
            me "Да..."
            $ ds_lp_mi += 1
            $ ds_skill_points['conceptualization'] += 1
            $ ds_music_member = True
        "Отказаться":
            me "Знаешь, я как-то не планировал особо…"
            show mi normal pioneer at center   with dspr
            mi "Да ладно тебе, я тебя научу играть! Хочешь на трубе, например? Или на скрипке? Я на всем умею, честно-честно."
            play sound ds_sfx_mot
            сom "Ты решаешь не спорить с девочкой-мультиинструменталистом, так как в ответ наверняка бы получил очередную пулеметную очередь из слов."
            me "Я подумаю, а пока не могла бы ты подписать?"
            show mi happy pioneer at center   with dspr
            mi "Да-да-да, конечно, давай! Ты заходи, не стесняйся! Я еще и пою хорошо! Послушаешь, как я пою японские народные песни. Ну, или, если не нравится, может, что-нибудь из современных шлягеров?"
            show un smile3 pioneer at right with dspr
            un "Да, она очень хорошо поёт. Я-то знаю, так как живу с ней!"
            me "Обязательно…"
    me "А сейчас мне пора, извини."
    show mi shy pioneer at center   with dspr
    mi "Конечно, приходи непременно… а, подожди..."
    show un serious pioneer at right with dspr
    un "Давай дослушаем..."
    window hide

    stop ambience fadeout 2

    stop music fadeout 3

    menu:
        "Дослушать":
            window show
            "Ты останавливаешься в двери, чтобы дослушать Мику"
            show mi sad pioneer at center with dspr
            mi "У меня тут потерялась заколка, ты случайно не видел её? Мне она очень-очень дорога и важна!"
            me "Нет..."
            mi "Поищи её, пожалуйста, если найдёшь - отнеси сюда или в домик 13, мне правда она очень-очень нужна..."
            show un normal pioneer at right with dspr
            un "Это, если что, и мой домик тоже."
            me "Ладно..."
            $ ds_lp_mi += 1
            $ ds_find_hairpin = True
            "И с этими словами ты выходишь."
            show mi happy pioneer at center with dspr
            mi "Cпасибо-спасибо большое, Семён-кун!"
            scene bg ext_musclub_day 
            with dissolve

            play ambience ambience_camp_center_day fadein 3
        "Идти дальше":
            $ renpy.pause(1)

            $ persistent.sprite_time = "day"
            scene bg ext_musclub_day 
            with dissolve

            play ambience ambience_camp_center_day fadein 3

            window show
            "Окончание ее фразы скрывается за закрытой дверью."
    show un normal pioneer at center with dissolve
    if not ds_music_member:
        play sound ds_sfx_int
        con "С одной стороны, ты был бы не против вечерком посидеть побренчать на гитаре"
        play sound ds_sfx_mot
        com "Но в такой компании…"
    show dv normal pioneer close at center    with dissolve
    "Ты поворачиваешься, собираясь уходить, и сталкиваешься нос к носу с Алисой."
    "Она недобро смотрит на тебя."
    show un angry pioneer at right with dspr
    play sound ds_sfx_psy
    emp "А Лена недобро смотрит на Алису."
    dv "Зачем пришел?"
    if ds_music_member:
        window hide
        menu:
            "Чтобы записаться":
                window show
                me "В музклуб записаться..."
                show dv smile pioneer close at center with dspr
                dv "А... неплохо."
                $ ds_lp_dv += 1
                dv "Записался?"
            "Чтобы подписать обходной":
                window show
                me "Обходной…"
                dv "Подписал?"
    else:
        me "Обходной…"
        dv "Подписал?"
    me "Да…"
    dv "Свободен!"
    hide dv  with dissolve
    "Она входит внутрь, а ты спешишь покинуть это место."
    emp "Ну, или не спешишь..."
    window hide
    menu:
        "Спросить про Алису":
            window show
            me "Лен, а почему ты так злишься при каждом упоминании Алисы?"
            show un shy pioneer at center with dspr
            un "Ничего я не злюсь... всё в порядке."
            if skillcheck('drama', lvl_challenging, passive=True):
                play sound ds_sfx_int
                dra "Нет, она от вас что-то скрывает, мессир."
                dra "Похоже, тут есть какая-то неприличная тайна. Нам обязательно надо будет выяснить!"
                dra "Но не сейчас - сейчас вы её вывести на чистую воду не сможете."
                $ ds_skill_points['drama'] += 1
            play sound ds_sfx_psy
            emp "Она просто не хочет рассказывать сейчас. Попробуй ещё раз позже."
            window hide
        "Не спрашивать":
            pass

    stop ambience fadeout 2

    $ ds_passed_places += 1
    $ ds_visited_music = True

    jump ds_day2_pass_un_main

label ds_day2_pass_un_clubs:
    play ambience ambience_camp_center_day fadein 2

    $ persistent.sprite_time = "day"
    scene bg ext_clubs_day 
    with dissolve
    if (ds_passed_places == 3) and not ds_had_lunch:
        show un shy pioneer at center with dissolve
        un "Я схожу, пообедаю пока..."
        window hide
        menu:
            "Отпустить":
                me "Ладно..."
                hide un with dissolve
                jump ds_day2_pass_alone_clubs
            "Остановить":
                if skillcheck('suggestion', lvl_up_medium):
                    window show
                    sug "Вы быстро обойдёте всё остальное и сможете поесть."
                    me "Нет, подожди... мы быстренько! И сходим пообедаем."
                    un "Ладно..."
                    $ ds_lp_un -= 1
                else:
                    window show
                    sug "Ты не знаешь, что сказать - она же определённо хочет есть."
                    me "Ну, останься..."
                    show un angry pioneer at center with dspr
                    un "Нет, я пойду."
                    hide un with dissolve
                    $ ds_lp_un -= 1
                    jump ds_da2_pass_alone_clubs

    show un normal pioneer at center with dissolve
    window show
    "Вы подходите к зданию кружков."
    th "Именно тут мы с Леной впервые встретились..."
    play sound ds_sfx_psy
    esp "По правде говоря, тебе никогда особо не доставляла удовольствия общественная работа."
    esp "В школе ты всегда под любым предлогом пытался пропустить субботники, в институте тебя никак не привлекал студенческий совет."
    esp "Тебя не интересовали секции бокса, авиамоделирования или кройки и шитья."
    esp "Так что сюда ты приходишь лишь с целью отметиться.{w} Хотя, может, и попробуешь записаться хоть тут, вдруг будет интересно."

    stop ambience fadeout 2

    "Ты открываешь дверь, и вы заходите."
    window hide

    play sound sfx_open_door_clubs

    $ renpy.pause(1)

    $ persistent.sprite_time = "day"
    scene bg int_clubs_male_day 
    with dissolve
    show un normal pioneer at center with dissolve

    play ambience ambience_clubs_inside_day fadein 3

    window show
    "Внутри никого нет."
    play sound ds_sfx_int
    con "Комната представляет из себя что-то наподобие берлоги юного робототехника – повсюду валялись какие-то провода, нехитрые платы, микросхемы, на столе стоит осциллограф."
    "Из соседнего помещения слышатся голоса, и через секунду в комнату вошли двое пионеров."
    show el normal pioneer at cleft 
    show sh normal pioneer at cright 
    with dissolve
    play sound ds_sfx_int
    enc "В одном ты узнаёшь Электроника, второй же тебе был незнаком."
    el "Привет, Семен! А мы тебя ждали."
    el "О, привет, Лена!"
    show un shy pioneer at center with dspr
    un "Привет..."
    th "Кажется, он знает все и обо всех…"
    me "А чего вы меня ждали?"
    el "Ну как же, ты же пришел в наш клуб кибернетиков записываться, так?"
    "Он не дал тебе ответить."
    show el smile pioneer at cleft   with dspr
    el "Знакомься, это Шурик, он у нас главный!"

    me "А вас в клубе этом только двое, я так полагаю?"
    show el normal pioneer at cleft   with dspr
    el "Ну, можешь считать, что уже трое."
    "Шурик подходит к тебе и уверенно протянул руку."
    play sound ds_sfx_int
    enc "Его лицо тебе кажется почему-то знакомым."
    if skillcheck('encyclopedia', lvl_easy):
        enc "Точно, он же вылитый Шурик из комедий Гайдая!"
    else:
        enc "Хотя нет, показалось..."
    show sh normal_smile pioneer at cright   with dspr
    sh "Добро пожаловать!"
    me "Угу…"
    show sh normal pioneer at cright   with dspr
    el "Давай я тебе тут все покажу!{w} Ты не стесняйся, располагайся."
    me "Да нет, ребята, я вообще-то…"
    show sh normal_smile pioneer at cright   with dspr
    sh "Всегда рады новым членам."
    play music ds_ussr_anthem fadein 2
    enc "Он сказал это так, что в голове у тебя невольно заиграл гимн Советского Союза."
    enc "Удивительно, но ты еще помнишь слова – в первом классе у тебя была тетрадка, на обратной стороне которой они были напечатаны."
    stop music fadeout 2
    menu:
        "Записаться":
            th "Впрочем, новые знакомства мне точно не помешают."
            me "Да, давайте, записывайте меня!"
            sh "Отлично. Давай, кстати, сюда обходной лист."
            play sound ds_pen
            "Ты отдаёшь обходной лист, они записывают тебя в какой-то список и подписывают тебе его."
            sh "Вот, распишись тут."
            play sound ds_sfx_mot
            per_eye "Итак, члены клуба..."
            per_eye "1. ДЕМЬЯНЕНКО АЛЕКСАНДР"
            per_eye "2. CЫРОЕЖКИН СЕРГЕЙ"
            play sound ds_sfx_mot
            res "Значит, настоящее имя Электроника - Сергей..."
            per_eye "А вот и ты: 3. ПЁРСУНОВ СЕМЁН"
            play sound ds_pen
            "Ты ставишь свою подпись."
            show el laugh pioneer at cleft with dspr
            show un smile pioneer at center with dspr
            el "Приветствуем нового члена клуба кибернетиков!"
            $ ds_cyber_member = True
            $ ds_skill_points['interfacing'] += 1
            "И тут в комнату кто-то входит."
        "Отказаться":
            me "Да нет, мне бы просто обходной лист подписать."
            show sh normal_smile pioneer at cright   with dspr
            show el grin pioneer at cleft   with dspr
            show un normal pioneer at center with dspr
            el "Так ты к нам запишись, и мы тебе его подпишем."
            "Он хитро улыбается."
            play sound ds_sfx_psy
            sug "Какой хитрец!"
            "Ты уже подготовился к длинной и нудной дискуссии, как вдруг в комнату кто-то входит."
    show el normal pioneer at left 
    show sh normal pioneer at right 
    show sl normal pioneer at center 
    show un normal pioneer at fright
    with dissolve
    "Ты оборачиваешься и видишь Славю."
    sl "Привет, Лена!"
    un "Привет, Славя. А мы тут..."
    sl "А, Семен! Надеюсь, они тут тебя не достают?"
    show sl angry pioneer at center   with dspr
    "Она строго смотрит на будущих светил отечественного роботостроения."
    sl "А то я их знаю – они могут!"
    if ds_cyber_member:
        me "Нет, я просто решил к ним записаться."
        show sl smile pioneer at center with dspr
        sl "А, отлично. Тогда я пойду!"
        hide sl with dissolve
    else:
        me "Да, понимаешь, на самом деле мне бы просто обходной подписать…"
        "Я решил воспользоваться ситуацией."
        show sl normal pioneer at center   with dspr
        sl "Так это не проблема, давай сюда."
        "Она взяла листок и подошла к Шурику."
        sl "Подписывай!"
        show sh upset pioneer at right   with dspr
        sh "Ну подожди, мы еще не закончили…"
        show sl angry pioneer at center   with dspr
        sl "Закончили! Подписывай!"
        play sound ds_sfx_psy
        emp "Она посмотрела на него так, что возражать Шурик не решается."

        stop ambience fadeout 2
        play sound ds_pen
        "Он поставил свою закорючку, и ты, поблагодарив Славю, с чистой совестью направляешься дальше."
    window hide

    $ ds_passed_places += 1
    $ ds_visited_clubs = True

    jump ds_day2_pass_un_main

label ds_day2_pass_un_medic:
    $ persistent.sprite_time = "day"
    scene bg ext_aidpost_day 
    with dissolve
    if (ds_passed_places == 3) and not ds_had_lunch:
        show un shy pioneer at center with dissolve
        un "Я схожу, пообедаю пока..."
        window hide
        menu:
            "Отпустить":
                me "Ладно..."
                hide un with dissolve
                jump ds_day2_pass_alone_medic
            "Остановить":
                if skillcheck('suggestion', lvl_up_medium):
                    window show
                    sug "Вы быстро обойдёте всё остальное и сможете поесть."
                    me "Нет, подожди... мы быстренько! И сходим пообедаем."
                    un "Ладно..."
                    $ ds_lp_un -= 1
                else:
                    window show
                    sug "Ты не знаешь, что сказать - она же определённо хочет есть."
                    me "Ну, останься..."
                    show un angry pioneer at center with dspr
                    un "Нет, я пойду."
                    hide un with dissolve
                    $ ds_lp_un -= 1
                    jump ds_da2_pass_alone_medic

    show un normal pioneer at center with dissolve
    play ambience ambience_camp_center_day fadein 3

    window show
    play sound ds_sfx_fys
    edr "Ты решительно не понимаешь, что тебе делать в медпункте."
    edr "Здоровье вроде не шалит, тем более местный свежий воздух явно пошел тебе на пользу, и самочувствие было куда бодрее, чем обычно."
    th "Но раз надо так надо."
    show un shy pioneer at center with dspr
    un "Слушай, я подожду тут... мне бы очень не хотелось сталкиваться с нашей медсестрой."
    play sound ds_sfx_psy
    emp "Что же у неё с медсестрой не так?"
    play sound ds_sfx_psy
    aut "Тебе так-то Лена там и не очень нужна, скорее всего."
    window hide
    menu:
        "Настоять пойти вместе":
            if skillcheck('suggestion', lvl_medium):
                window show
                sug "Тебе не справиться без неё. Акцентируй внимание на этом."
                me "Послушай, я тут никого не знаю, только тебя. Мне нужна {i}твоя{/i} поддержка."
                un "Ладно, пойдём."
                "Вы входите."
                window hide

                stop ambience fadeout 2

                play sound sfx_open_door_1

                $ renpy.pause(1)

                $ persistent.sprite_time = "day"
                scene bg int_aidpost_day 
                with dissolve
                show un shy pioneer at center with dissolve

                play ambience ambience_medstation_inside_day fadein 3

                window show
                th "Обычный такой медпункт, у нас в школе был примерно такой же."
                show cs normal stethoscope at center   with dissolve

                play music ds_cs_theme fadein 5

                "За столом сидит женщина средних лет."
                "Она бросает на вы пристальный, оценивающий взгляд, и продолжила что-то писать."
                csp "Ну, здравствуй… пионер."
                "Говорит она, не отрываясь от своего занятия."
                csp "Девушку привёл уже?"
                csp "Вам нужны {i}определённые{/i} изделия или уже таблетки?"
                play sound ds_sfx_fys
                ins "Она намекает на то, что у вас был или будет секс."
                show un sad pioneer at right with dspr
                play sound ds_sfx_psy
                emp "Отбой! Отбой! Очень плохая идея была тащить Лену с собой!"
                $ ds_lp_un -= 1
                show cs shy stethoscope at center with dspr
                csp "Или же я могу предложить палату для {i}дел{/i}."
                show un cry pioneer at right with dspr
                un "Всё, я не могу, дальше давай сам!"
                hide un with dissolve
                emp "Ну ты и делов натворил, конечно..."
                $ ds_un_upset = True
            else:
                window show
                sug "Она сказала нет - значит, нет."
                me "Ладно, я пойду."
                "Ты входишь."
                window hide

                stop ambience fadeout 2

                play sound sfx_open_door_1

                $ renpy.pause(1)

                $ persistent.sprite_time = "day"
                scene bg int_aidpost_day 
                with dissolve

                play ambience ambience_medstation_inside_day fadein 3

                window show
                th "Обычный такой медпункт, у нас в школе был примерно такой же."
                show cs normal stethoscope at center   with dissolve

                play music ds_cs_theme fadein 5

                "За столом сидит женщина средних лет."
                "Она бросает на меня пристальный, оценивающий взгляд, и продолжила что-то писать."
                csp "Ну, здравствуй… пионер."
                "Говорит она, не отрываясь от своего занятия."
                me "Добрый день… Мне бы вот…"
        "Пойти одному":
            window show
            me "Хорошо, подожди тут..."
            "Ты входишь."
            window hide

            stop ambience fadeout 2

            play sound sfx_open_door_1

            $ renpy.pause(1)

            $ persistent.sprite_time = "day"
            scene bg int_aidpost_day 
            with dissolve

            play ambience ambience_medstation_inside_day fadein 3

            window show
            th "Обычный такой медпункт, у нас в школе был примерно такой же."
            show cs normal stethoscope at center   with dissolve

            play music ds_cs_theme fadein 5

            "За столом сидит женщина средних лет."
            "Она бросает на меня пристальный, оценивающий взгляд, и продолжила что-то писать."
            csp "Ну, здравствуй… пионер."
            "Говорит она, не отрываясь от своего занятия."
            me "Добрый день… Мне бы вот…"
    csp "Ты присаживайся."
    "Ты оглядываешь комнату."
    csp "На кушеточку."
    "Ты садишься."
    csp "Раздевайся."
    "Все это она говорит совершенно ровным тоном."
    me "А зачем?.."
    csp "Смотреть тебя будем, слушать, здоровье проверять."
    show cs smile stethoscope at center   with dspr
    csp "Меня, кстати, зовут Виолетта Церновна, но ты меня можешь звать просто Виолой."

    "Она поворачивается в твою сторону."
    cs "Ну, чего сидишь? Раздевайся."
    me "Да я не жалуюсь ни на что. Мне бы вот…"
    "Ты аккуратно протягиваешь ей листок."
    cs "Потом."
    show cs smile at center   with dissolve
    "Она снимает с шеи стетоскоп и, кажется, намеревается тебя им препарировать."
    window hide

    stop music fadeout 3
    play sound sfx_knock_door7_polite

    $ renpy.pause(1)

    window show
    "Но тут в дверь постучали."
    show cs normal at center   with dspr
    cs "Входите!"
    play sound ds_sfx_psy
    emp "Она ответила нехотя."

    play sound sfx_open_door_strong
    play music music_list['eternal_longing'] fadein 5

    "Моментально дверь распахнулась, и в комнату вбегает Электроник."
    show el fingal pioneer far at left    with dissolve   
    show cs normal at center   with dspr
    el "Здрасьте! Я тут это… На футболе упал. Глупости, конечно, я бы и так, но меня Ольга Дмитриевна…"
    "У Электроника под глазом красуется здоровенный фингал."
    play sound ds_sfx_int
    vic "Что-то сомнительно, что такой можно заработать на футболе."
    cs "Садись, сейчас посмотрим."
    show cs normal glasses at center   with dissolve
    cs "А ты давай сюда свой обходной."
    queue sound ds_pen
    queue sound ds_stamp
    "Медсестра быстро подписывает его, ставит печать и продолжает:"
    show cs smile glasses at center   with dspr
    cs "Если что заболит – сразу ко мне… пионер."

    stop ambience fadeout 2
    stop music fadeout 3

    "Ты ничего не отвечаешь и выходишь, закрыв за собой дверь."
    window hide

    $ ds_passed_places += 1
    $ ds_visited_medic = True
    $ ds_skill_points['instinct'] += 1

    $ persistent.sprite_time = "day"
    scene bg ext_aidpost_day 
    with dissolve
    if ds_un_upset:
        th "Медсестра здесь, конечно, еще та…"
        window hide
        jump ds_day2_pass_alone_main
    else:
        show un scared pioneer at center with dissolve
        un "Ты как?"
        me "Медсестра здесь, конечно, еще та…"
        show un serious pioneer at center with dissolve
        un "Вот потому я её и избегаю..."
        window hide
        jump ds_day2_pass_un_main

label ds_day2_pass_un_library:
    play ambience ambience_camp_center_day fadein 3
    $ persistent.sprite_time = "day"
    scene bg ext_library_day 
    with dissolve
    if (ds_passed_places == 3) and not ds_had_lunch:
        show un shy pioneer at center with dissolve
        un "Я схожу, пообедаю пока..."
        window hide
        menu:
            "Отпустить":
                me "Ладно..."
                hide un with dissolve
                jump ds_day2_pass_alone_library
            "Остановить":
                if skillcheck('suggestion', lvl_up_medium):
                    window show
                    sug "Вы быстро обойдёте всё остальное и сможете поесть."
                    me "Нет, подожди... мы быстренько! И сходим пообедаем."
                    un "Ладно..."
                    $ ds_lp_un -= 1
                else:
                    window show
                    sug "Ты не знаешь, что сказать - она же определённо хочет есть."
                    me "Ну, останься..."
                    show un angry pioneer at center with dspr
                    un "Нет, я пойду."
                    hide un with dissolve
                    $ ds_lp_un -= 1
                    jump ds_da2_pass_alone_library

    show un normal pioneer at center with dissolve

    window show
    play sound ds_sfx_psy
    vol "Вообще, ты, конечно, любишь читать, но просиживать днями в библиотеке при нынешних обстоятельствах в твои планы не входит, так что ты решил побыстрее пройти этот чекпойнт."
    un "Мне как раз книжку надо отнести..."
    window hide

    stop ambience fadeout 3

    $ persistent.sprite_time = "day"
    scene bg int_library_day 
    with dissolve
    show un normal pioneer at center with dissolve

    play ambience ambience_library_day fadein 3

    window show
    play sound ds_sfx_psy
    ine "Когда ты заходишь внутрь, у тебя в голове всплывает воспоминание из детства."
    ine "Оно очень яркое."
    ine "Тебе лет 7 или 8, ты с мамой в библиотеке."
    ine "Пока она выбирает какие-то книжки, которые тебе понадобятся для учебы, ты сидишь и разглядываешь местную подборку комиксов."
    ine "Тогда тебе было сложно понять, почему их здесь так много и почему нельзя забрать часть домой."
    ine "Понятия коллективной собственности тогда для тебя не существовало."
    ine "Впрочем, как и понятия собственности вообще."
    ine "Тем более странным было это воспоминание сейчас, когда ты находишься в том самом отдельно взятом пионерлагере, где коммунизм таки удалось построить за 3 года."
    "Повсюду висит огромное количество советской символики, а на полках книги в основном соответствующей тематики."
    vol "Читать их ты никак не планировал – знакомство с полным собранием сочинений Маркса было одной из последних вещей на Земле, которая пришла бы тебе в голову."
    vol "Надо найти библиотекаря."
    "Оказалось это не так сложно – она спит на столе рядом с тобой."
    window hide

    scene cg d2_micu_lib 
    with dissolve

    window show
    "Ты пригляделся.{w} Короткая стрижка, толстые очки, довольно приятное лицо."
    $ ds_met['mz'] = 1
    play sound ds_sfx_psy
    th "Она так мило спит..."
    scene bg int_library_day 
    with dissolve
    show un normal pioneer at center with dissolve
    un "Ой, а Женя спит…"
    $ ds_met['mz'] = 2
    mz "Уже не сплю."
    show mz normal glasses pioneer far at cright    with dissolve
    "Ты удивленно смотришь в сторону библиотекарши."
    "Она сидит за столом и пристально наблюдает за мной."
    show mz angry glasses pioneer far at cright   with dspr
    mz "А тебе чего?"
    window hide
    menu:
        "Пропустить вперёд Лену":
            window show
            me "Давайте сначала Лена."
            show mz normal glasses pioneer far at cright    with dissolve
            mz "Давайте!"
            show un shy pioneer at center with dissolve
            un "Спасибо..."
            $ ds_yield_un = True
            $ ds_lp_un += 1
            "Лена отдаёт книжку, после чего очередь снова подходит к тебе."
            mz "Так а тебе чего? Или просто девушку сопроводил."
        "Пойти первому":
            window show
    me "Мне бы обходной…"
    show mz normal glasses pioneer at cright   with dissolve
    mz "Давай."
    queue sound ds_pen
    queue sound ds_stamp
    "Она быстро расписывается, ставит печать и протягивает тебе его обратно."
    mz "Получать читательский билет будем?"
    menu:
        "Согласиться":
            me "Да, давай...те."
            "Женя залезает в стол, достаёт какой-то листок..."
            mz "Фамилия, имя?"
            me "Пёрсунов Семён..."
            play sound ds_pen
            "Она записывает сведения в билет, а затем отдаёт тебе."
            mz "Бери!"
            "Ты забираешь бумажку и складываешь в карман штанов."
            $ ds_library_member = True
            $ ds_skill_points['encyclopedia'] += 1
            $ ds_lp_un += 1
            show un smile pioneer at center with dspr
            un "Как-нибудь сможем вместе почитать тогда..."
            show un shy pioneer at center with dspr
            un "...если захочешь."
            mz "Cледующий!"
        "Отказаться":
            me "Нет, спасибо."
            mz "Тогда следующий!"
    play sound ds_sfx_psy
    emp "Вид у нее такой, что дальнейший разговор кажется совершенно неуместным."
    if ds_yield_un:
        "Ты благодаришь Женю."
    else:
        "Лена подходит к ней и отдаёт книжку, а ты благодаришь Женю."
    "После вы выходите."
    window hide

    stop ambience fadeout 2

    $ ds_passed_places += 1
    $ ds_visited_library = True

    jump ds_day2_pass_un_main

label ds_day2_pass_un_lunch:
    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_away_day 
    with dissolve

    show sl normal pioneer at center with dissolve

    window show
    "Ты отводишь Лену пообедать."
    th "Обходной лист никуда не денется, потом быстренько подпишу, а вот мой желудок явно ждать до ужина не намерен."
    "С такими мыслями ты входишь в столовую."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_day 
    with dissolve

    show un normal pioneer at center with dissolve

    play ambience ambience_dining_hall_empty fadein 3

    window show
    "Там почти никого нет – видимо, большинство пионеров уже пообедало."
    "Вы встаёте в очередь за едой."
    show ck normal at center with dissolve
    show un normal pioneer at right with dissolve
    
    "Впрочем, очередью это назвать нельзя, ибо вы тут вдвоём."
    window hide
    menu:
        "Пойти первым":
            window show
            me "Спасибо!"
            "Забрав еду, ты пропускаешь Лену."
            "Она тоже берёт."
        "Пропустить Лену":
            window show
            me "Прошу, проходи первая."
            show un shy pioneer at right with dspr
            sl "Спасибо..."
            $ ds_lp_un += 1
            "Она забирает еду, затем еду берёшь и ты."
            me "Спасибо!"
    hide ck with dissolve
    show un normal pioneer at center with dspr
    "Вы принимаетесь есть."
    window hide
    menu:
        "Заговорить с Леной":
            if skillcheck('rhetoric', lvl_up_medium):
                window show
                play sound ds_sfx_int
                rhe "Начни расспрашивать про её интересы. Про то, как она попала в лагерь. Вообще про неё!"
                $ ds_skill_points['rhetoric'] += 1
                th "Про что её спросить?"
                window hide
                menu:
                    "Откуда она":
                        me "А ты откуда?"
                        show un scared pioneer at center with dspr
                        play sound ds_sfx_psy
                        emp "Твой вопрос оказался неожиданным для неё."
                        un "Я... да я местная... из райцентра."
                        rhe "Так, райцентр. Туда, наверное, можно попасть. Выясняй дальше."
                        me "А он далеко?"
                        show un shy pioneer at center with dspr
                        un "Не знаю... вроде не очень, но я не уверена."
                        me "А называется как?"
                        un "Да Работино..."
                        show un normal pioneer at center with dspr
                        un "Ты не местный, ведь так?"
                        me "Ну да..."
                        un "А откуда ты?.."
                        play sound ds_sfx_int
                        con "Придумай что-нибудь интересное. Необычное! Оригинальное!"
                        window hide
                        menu:
                            "Рассказать как есть":
                                window show
                                me "Да я из Сан..."
                                if skillcheck('reaction_speed', lvl_easy, passive=True):
                                    play sound ds_sfx_mot
                                    res "Нет тут Санкт-Петербурга, только Ленинград!"
                                    $ ds_skill_points['reaction_speed'] += 1
                                    me "Я из Ленинграда."
                                    un "Понятно, красивый город..."
                                else:
                                    me "...Санкт-Петербурга."
                                    show un surprise pioneer at center with dspr
                                    un "Так ведь он уже давно стал Ленинградом..."
                                    me "А, точно... просто привычка есть называть по-старому у местных!"
                                    un "Ну ладно..."
                            "Придумать":
                                if skillcheck('conceptualization', lvl_formidable):
                                    window show
                                    con "Заграница. Ты из-за границы. Из ГДР, например."
                                    $ ds_skill_points['conceptualization'] += 1
                                    me "Я из дальних краёв. Из-за границы! ГДР!"
                                    show un surprise pioneer at center with dspr
                                    un "Ого, и как там?.."
                                    me "Неплохо..."
                                    window hide
                                    menu:
                                        "Но тут лучше":
                                            window show
                                            me "Но тут лучше!"
                                            show un smile pioneer at center with dspr
                                            un "Да, на родине всегда лучше..."
                                        "Лучше там":
                                            window show
                                            me "Там всяко лучше чем тут!"
                                            show un scared pioneer at center with dspr
                                            un "Ты осторожнее с подобным!"
                                        "Закончить":
                                            window show
                                else:
                                    window show
                                    con "Ничего интереснее Москвы тебе не приходит в голову."
                                    $ ds_skill_points['conceptualization'] += 1
                                    me "Я из Москвы!"
                                    show un surprise pioneer at center with dspr
                                    un "Ого, и как там?.."
                                    me "Неплохо..."
                            "Промолчать":
                                window show
                                me "Да так... неважно..."
                    "Её увлечения":
                        window show
                        me "А чем ты увлекаешься?"
                        show un scared pioneer at center with dspr
                        play sound ds_sfx_psy
                        emp "Твой вопрос оказался неожиданным для неё."
                        show un shy pioneer at center with dspr
                        un "Да так... рисую."
                        play sound ds_sfx_int
                        con "Так, интересно... попробуй сказать, что ты тоже рисуешь."
                        window hide
                        menu:
                            "Я тоже рисую":
                                window show
                                me "Я тоже немного рисую..."
                                show un smile pioneer at center with dspr
                                un "О, хорошо..."
                                play sound ds_sfx_psy
                                sug "Может, вам вместе заняться рисованием?"
                                window hide
                                menu:
                                    "Предложить":
                                        window show
                                        me "А может, нам вместе как-нибудь порисовать?"
                                        show un surprise pioneer at center with dspr
                                        un "Давай..."
                                        $ ds_lp_un += 1
                                        $ ds_un_invite = True
                                        $ ds_skill_points['conceptualization'] += 1
                                    "Не предлагать":
                                        window show
                                        th "Да не, не буду. Опозорюсь только."
                            "Хочу научиться рисовать":
                                window show
                                me "А я нет... но хотел бы."
                                show un smile pioneer at center with dspr
                                un "Можем попробовать вместе!"
                                window hide
                                menu:
                                    "Принять":
                                        window show
                                        me "Давай!"
                                        un "Хорошо, приходи как-нибудь..."
                                        $ ds_lp_un += 1
                                        $ ds_un_invite = True
                                        $ ds_skill_points['conceptualization'] += 1
                                    "Отклонить":
                                        window show
                                        me "Да нет... я не успею, наверное."
                                        show un sad pioneer at center with dspr
                                        un "Ну ладно..."
                                        $ ds_lp_un -= 1
                            "Это глупости":
                                window show
                                me "Ну это же глупости! Можно же заняться чем-нибудь более полезным..."
                                show un sad pioneer at center with dspr
                                un "Это интересно... выражать себя..."
                                show un evil_smile pioneer at center with dspr
                                show un sad pioneer at center with dspr
                                play sound ds_sfx_mot
                                res "На секунду у неё появилось какое-то... странное выражение лица."
                                if skillcheck('drama', lvl_medium, passive=True):
                                    play sound ds_sfx_int
                                    dra "Похоже, у Лены есть какие-то скелеты в шкафу, мессир. Будьте осторожны!"
                                $ ds_lp_un -= 1
                            "Промолчать":
                                window show
                                $ renpy.pause(1.0)
                "Тут оказывается, что вы доели обед."
            else:
                window show
                play sound ds_sfx_int
                rhe "Тебе не удаётся придумать темы для разговора с Леной."
                play sound ds_sfx_psy
                emp "Да и сама Лена не склонна к разговорам."
                "Вы молча съедаете обед."
                $ ds_skill_points['rhetoric'] += 1
        "Поесть молча":
            window show
            th "Лена явно не склонна к разговорам."
            "Вы молча съедаете обед."
    show un smile pioneer at center with dspr
    un "Пойдём дальше?"
    me "Пойдём."
    $ ds_had_lunch = True
    jump ds_day2_pass_un_main

label ds_day2_pass_un_sport:
    scene bg ext_playground_day with dissolve
    play ambience ambience_camp_center_day fadein 3
    if (ds_passed_places == 3) and not ds_had_lunch:
        show un shy pioneer at center with dissolve
        un "Я схожу, пообедаю пока..."
        window hide
        menu:
            "Отпустить":
                me "Ладно..."
                hide un with dissolve
                jump ds_day2_pass_alone_sport
            "Остановить":
                if skillcheck('suggestion', lvl_up_medium):
                    window show
                    sug "Вы быстро обойдёте всё остальное и сможете поесть."
                    me "Нет, подожди... мы быстренько! И сходим пообедаем."
                    un "Ладно..."
                    $ ds_lp_un -= 1
                else:
                    window show
                    sug "Ты не знаешь, что сказать - она же определённо хочет есть."
                    me "Ну, останься..."
                    show un angry pioneer at center with dspr
                    un "Нет, я пойду."
                    hide un with dissolve
                    $ ds_lp_un -= 1
                    jump ds_da2_pass_alone_sport

    show un normal pioneer at center with dissolve
    window show
    "Ты подходишь к спортплощадке."
    "Не увидев никого, ты решаешь было уйти..."
    un "Тебе туда..."
    "Лена показывает в сторону здания рядом."
    un "Только мне надо отойти... к тому же, мне не нравятся подвижные игры."
    hide un with dissolve
    "Ты направляешься туда."
    scene bg ds_int_sporthall_day with dissolve
    show us smile sport far at center with dspr
    "Зайдя в спортзал, ты видишь Ульяну бегающей по залу."
    me "Ульяна, а где я тут могу подписать обходной лист?"
    us "Давай его сюда!"
    show us laugh sport at center with dspr
    play sound ds_sfx_int
    dra "По всей видимости, она опять хочет вас провести."
    us "Я тут спортклубом руковожу!"
    play sound ds_sfx_mot
    res "Так ей же не более 14 лет! И уже руководит чем-то?"
    menu:
        "Принять":
            me "А... хорошо."
        "Усомниться":
            me "Ты? Ты же ещё маленькая!"
            show us dontlike sport at center with dspr
            us "И ничего не маленькая! Мне сама Ольга Дмитриевна доверила!"
            $ ds_lp_us -= 1
    show us normal sport at center with dspr
    us "Кстати, не хочешь записаться к нам?"
    if not ds_caught_us:
        show us laugh2 sport at center with dspr
        us "Может, и сможешь меня тогда догнать!"
    window hide
    menu:
        "Записаться":
            window show
            me "Давай!"
            show us smile sport at center with dspr
            us "Вот, бери листик и записывайся сюда!"
            "Ты вносишь своё имя в данный тебе клочок бумаги."
            me "Вот, а теперь подпиши мне обходной."
            us "Давай сюда!"
            play sound ds_pen
            "Она подписывает обходной и отдаёт лист тебе."
            play sound ds_sfx_mot
            per_eye "СОВЕТОВА У.И. {w}Теперь мы знаем её фамилию!"
            me "Cпасибо!"
            show us laugh sport
            us "Только не забывай регулярно приходить сюда!"
            $ ds_sport_member = True
            $ ds_lp_us += 1
            "Под эти слова ты выходишь из зала."
        "Отказаться":
            window show
            me "Нет, спасибо... мне просто нужен обходной лист."
            show us dontlike sport at center with dspr
            us "Ну и ладно, давай сюда свою бумажку!"
            play sound ds_pen
            "Она подписывает обходной и отдаёт лист тебе."
            play sound ds_sfx_mot
            per_eye "СОВЕТОВА У.И. {w}Теперь мы знаем её фамилию!"
            me "Cпасибо!"
            "И ты уходишь."
    $ ds_passed_places += 1
    $ ds_visited_sport = True
    scene bg ext_playground_day with dissolve
    show un smile pioneer at center with dissolve
    un "А вот и я! Пойдём!"

    jump ds_day2_pass_alone_main

label ds_day2_after_pass:
    scene black 
    with dissolve2

    window show
    "..."
    th "Итак, я собрал все подписи, следовательно, надо было зайти к Ольге Дмитриевне, чтобы отдать листок."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_house_of_mt_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 3

    show mt normal panama pioneer far at center    with dissolve
    window show
    "Вожатая сидит возле домика и читает какую-то книжку."
    th "Она сама не очень соответствует образу идеального пионера, которого хотела сделать из меня."
    th "Круг ее обязанностей сводился, видимо, только к пламенным речам на линейке, отчитыванию Ульяны и наставлению меня на путь истинный."
    show mt normal panama pioneer at center   with dissolve
    window hide
    menu:
        "Возмутиться праздностью":
            if skillcheck('authority', lvl_medium):
                window show
                play sound ds_sfx_psy
                aut "Выскажи всё, что ты думаешь о ней!"
                me "А вы так и собираетесь тут лежать?"
                me "Я, между прочим, обходной тут подписал!"
                show mt surprise panama pioneer at center with dspr
                mt "А... да..."
                $ ds_karma -= 15
                $ ds_skill_points['authority'] += 1
            else:
                window show
                play sound ds_sfx_psy
                aut "Нет, лучше будь осторожным."
                me "Вот…"
                $ ds_skill_points['authority'] += 1
        "Отдать без комментариев":
            window show
            me "Вот..."
    "Я протянул ей обходной."
    "Она, не читая, сунула его в карман."
    th "Отлично! Значит, можно было самому за всех расписаться и вообще никуда не ходить…"
    show mt smile panama pioneer at center   with dspr
    mt "Молодец! Ну как, познакомился с нашей медсестрой?"
    me "Да…"
    "Почему-то от этого ее вопроса у меня мурашки по коже побежали."
    show mt normal panama pioneer at center   with dspr
    mt "В какой кружок записался?"
    if ds_music_member and ds_cyber_member and ds_sport_member:
        me "Во все сразу!"
    elif ds_music_member and ds_cyber_member:
        me "В музыкальный и к кибернетикам."
    elif ds_cyber_member and ds_sport_member:
        me "В спортивный и к кибернетикам."
    elif ds_music_member and ds_sport_member:
        me "В музыкальный и в спортивный."
    elif ds_music_member:
        me "В музыкальный записался."
        show mt smile panama pioneer at center with dspr
        mt "Отлично!"
    elif ds_sport_member:
        me "В спортивный записался."
        show mt smile panama pioneer at center with dspr
        mt "Отлично!"
    elif ds_cyber_member:
        me "Записался к кибернетикам."
        show mt smile panama pioneer at center with dspr
        mt "Отлично!"
    else:
        me "Да пока ни в какой… Нужно время подумать."
        show mt surprise panama pioneer at center   with dspr
        mt "Ну, что же ты так! Завтра обязательно запишись куда-нибудь!"
        th "Конечно, всенепременно!"
    if (ds_music_member and ds_cyber_member) or (ds_music_member and ds_sport_member) or (ds_cyber_member and ds_sport_member):
        show mt surprise panama pioneer at center with dspr
        mt "Ничего себе... только вот ты не успеешь больше одного кружка посещать."
        mt "Да, тебе лучше будет выбрать один!"
        window hide
        menu:
            "Остаться в музклубе" if ds_music_member:
                window show
                me "Я выбираю музклуб."
                $ ds_cyber_member = False
                $ ds_sport_member = False
                $ ds_lp_us -= 2
                show mt normal panama pioneer at center with dspr
                mt "Хорошо, я скажу об этом главам остальных клубов."
            "Остаться у кибернетиков" if ds_cyber_member:
                window show
                me "Я выбираю кбиернетиков."
                $ ds_music_member = False
                $ ds_sport_member = False
                $ ds_lp_mi -= 2
                $ ds_lp_us -= 2
                show mt normal panama pioneer at center with dspr
                mt "Хорошо, я скажу об этом главам остальных клубов."
            "Остаться в спортклубе" if ds_sport_member:
                window show
                me "Я выбираю спортклуб."
                $ ds_music_member = False
                $ ds_cyber_member = False
                $ ds_lp_mi -= 2
                show mt normal panama pioneer at center with dspr
                mt "Хорошо, я скажу об этом главам остальных клубов."
            "Настоять на своём":
                if skillcheck('suggestion', lvl_medium):
                    window show
                    sug "Это же ей лучше, если ты сможешь везде ходить. Правилами это не запрещено, так что вперёд. Используй лозунги."
                    me "Ольга Дмитриевна, вы не переживаете, смогу я везде. Тем более, пионер должен быть хорош во всём!"
                    show mt smile panama pioneer at center with dspr
                    mt "Тут ты прав... Ладно, оставайся везде."
                    mt "Но чтобы везде успевал!"
                    $ ds_skill_points['suggestion'] += 1
                else:
                    window show
                    sug "Но, вообще она права - ты и правда всюду не поспеешь."
                    $ ds_skill_points['suggestion'] += 1
                    window hide
                    menu:
                        "Остаться в музклубе" if ds_music_member:
                            window show
                            me "Я выбираю музклуб."
                            $ ds_cyber_member = False
                            $ ds_sport_member = False
                            $ ds_lp_us -= 2
                        "Остаться у кибернетиков" if ds_cyber_member:
                            window show
                            me "Я выбираю кбиернетиков."
                            $ ds_music_member = False
                            $ ds_sport_member = False
                            $ ds_lp_mi -= 2
                            $ ds_lp_us -= 2
                        "Остаться в спортклубе" if ds_sport_member:
                            window show
                            me "Я выбираю спортклуб."
                            $ ds_music_member = False
                            $ ds_cyber_member = False
                            $ ds_lp_mi -= 2
                    show mt normal panama pioneer at center with dspr
                    mt "Хорошо, я скажу об этом главам остальных клубов."

    show mt normal panama pioneer at center   with dspr
    mt "Ладно, пора уже и на ужин идти."
    th "Ну наконец-то! Я уже проголодался."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_away_day 
    with dissolve

    window show
    "Вместе вы направляетесь к столовой."
    play sound ds_sfx_mot
    per_eye "Cолнце уже начало садиться."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_dining_hall_near_day 
    with dissolve

    show dv normal pioneer at fright 
    show el normal pioneer at fleft 
    with dissolve
    window show
    "На крыльце стояло несколько человек: Алиса, Электроник..."
    show us normal pioneer at cleft 
    show sl normal pioneer at cright 
    with dissolve
    "Ульяна и Славя."
    show dv angry pioneer at fright   with dspr
    show el surprise pioneer at fleft   with dspr

    play music music_list["always_ready"] fadein 5

    play sound ds_sfx_mot
    per_hea "Когда вы подошли, ты смог разобрать, о чем они говорят."
    dv "И больше не называй меня ДваЧе, а то еще получишь!"
    el "Да не называл я тебя так! Тебе показалось!"
    show us grin pioneer at cleft   with dspr
    us "Называл, называл, я все слышала!"
    show el angry pioneer at fleft   with dspr
    show sl normal pioneer at cright  behind el  with dspr
    el "Да тебя вообще там не было!"
    us "А вот и была! Я в кустах сидела!"
    hide us  with dissolve
    show sl angry pioneer at cright   with dspr
    show el angry pioneer at fleft  behind sl  with dspr
    sl "Хватит вам! Прекратите!"
    if not ds_witnessed_el_hit:
        th "Значит, Электроник свое ранение не на футболе все же получил."
    show mt normal pioneer at center   with dissolve
    "Ольга Дмитриевна подошла к ним и попыталась выяснить, что происходит:"
    mt "Что вы тут ругаетесь?"
    sl "Алиса Сыроежкину в глаз…"
    if ds_witnessed_el_hit:
        dv "Он первый начал!"
    else:
        dv "Ничего я не делала!"
    hide dv  with dissolve
    "Алиса обиженно фыркает и заходит внутрь."
    window hide
    menu:
        "Встать на сторону Алисы":
            window show
            play sound ds_sfx_psy
            sug "Ну что ж, пора сообщить им всем правду!"
            me "Позвольте, вообще-то тут действительно неправ Электроник."
            me "Я сам слышал, как он называл Алису прозвищем, которое ей очень не нравится."
            us "Вот, я же говорю!"
            show sl surprise pioneer at cright with dspr
            show mt surprise pioneer at center with dspr
            show el scared pioneer at fleft with dspr
            play sound ds_sfx_mot
            com "Показательно, как Электроник напрягся от твоих слов."
            mt "Вот как... что ж, надо будет более детально разобраться в случившемся."
            $ ds_lp_dv += 1
            $ ds_skill_points['suggestion'] += 1
            $ ds_eldv_side_taken = 1
        "Встать на сторону Электроника":
            window show
            me "Да, я видел, как Алиса врезала Электронику в глаз!"
            show mt angry pioneer at center with dspr
            mt "Значит, получит у меня Алиса как следует!"
            mt "Это уже переходит все границы!"
            $ ds_lp_dv -= 1
            if not ds_wintessed_el_hit:
                play sound ds_sfx_psy
                sug "А вдруг это не так?"
                play sound ds_sfx_int
                dra "Получится, что вы невиновную сделали виноватой."
            $ ds_eldv_side_taken = -1
        "Промолчать":
            window show
            $ ds_semtype -= 1

    stop music fadeout 3

    mt "Ладно, пора ужинать уже."
    hide mt 
    hide el 
    hide sl 
    with dissolve
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_people_day 
    with dissolve

    play ambience ambience_dining_hall_full fadein 3

    window show
    "Последним в столовую заходишь ты."
    "Похоже, свободных мест осталось не так много."
    play sound ds_sfx_mot
    per_eye "Ты окидываешь взглядом помещение."
    per_eye "Вдалеке виднелось несколько свободных стульев рядом с Алисой, но это может быть небезопасно."
    per_eye "Также свободно было рядом с Ульяной, но я не сторонник китайской традиционной кухни – «ем все, что ползает»."
    per_eye "И, наконец, свободный стул был рядом с Мику."
    th "Если выбирать из трех зол…"
    window hide
    menu:
        "Cесть с Алисой" if ds_eldv_side_taken != -1:
            window show
            $ ds_lp_dv += 1
            $ ds_skill_points['volition'] += 1
            play sound ds_sfx_psy
            vol "Ты всё-таки решаешься сесть с Алисой."
            show dv normal pioneer at center with dissolve
            play music music_list["you_won_t_let_me_down"] fadein 3
            me "Можно я сяду тут?"
            dv "Да, садись."
            if ds_eldv_side_taken == 1:
                show dv shy pioneer at center with dspr
                dv "Кстати... {w}спасибо..."
                play sound ds_sfx_psy
                emp "Ей определённо очень неловко благодарить тебя."
            show dv sad pioneer at center with dissolve
            "Ты замечаешь нехорошее настроение Алисы."
            window hide
            menu:
                "Попытаться выяснить":
                    if skillcheck('empathy', lvl_legendary):
                        play sound ds_sfx_psy
                        emp "Алису по какой-то причине сильно задевает прозвище «ДваЧе». Попробуй выяснить, с чем это связано."
                        $ ds_skill_points['empathy'] += 1
                        me "Ты чего, Алис? Почему тебя так задевает то, как Электроник тебя называет?"
                        show dv angry pioneer at center with dspr
                        dv "Не твоё это дело!"
                        window hide
                        $ renpy.pause(1)
                        window show
                        dv "Меня всю жизнь так называли! Надоело уже!"
                        emp "Она хочет сказать, что её так оскорбляли."
                        play sound ds_sfx_psy
                        aut "Немудрено - в твоём мире Двач, как и другие имиджборды, тоже с не самыми, скажем так, лучшими слоями населения ассоциируется."
                        play sound ds_sfx_int
                        lgc "Только тут, очевидно, Двача никогда не существовало. Так почему {i}тут{/i} её фамилия такую реакцию вызывает?"
                        emp "Да не в фамилии и не в имиджбордах тут дело."
                        emp "Как ты мог заметить, Алиса отличается определённым бунтарством. Почему она такая - это само по себе вопрос интересный."
                        emp "Здесь более важно то, что общество зачастую склонно отвергать своих членов, не следующих правилам - писаным или нет."
                        emp "Вероятно, тут Алиса нарушила иерархию и попала под травлю. Или ещё как-то шла поперёк правил той группы, где она находилась, и ей за это прилетело."
                        emp "В общем, пострадала из-за своих каких-то принципов, вошедших в конфликт с нормами - или «нормами» - того общества, где она жила."
                        me "То есть, тебя так оскорбляли?"
                        dv "Неужели до тебя допёрло?!"
                        dv "Ну, хотя бы до тебя... другие и этого не осилили!"
                        if ds_witnessed_el_hit:
                            dv "А Электроник уже многократно меня так называл!"
                            dv "Хотя я уже столько раз говорила ему!"
                            dv "Не сдержалась просто уже, как завидела его наглую рожу!"
                        else:
                            dv "Но Электроника я честно не била... хотела, конечно, но не била!"
                            dv "Он сам где-то заработал себе фингал, а свалил всё на меня!"
                        window hide
                        menu:
                            "Поддержать Алису":
                                me "Я тебя понимаю, Алис... похоже, тебе пришлось пережить многое..."
                                dv "Да уж достаточно... но жалости ко мне не надо, я справлюсь и сама!"
                                me "Да я просто хотел, чтобы ты знала... если что, мы можем поговорить."
                                me "Но вообще ты умница, что строго придерживаешься своих принципов."
                                show dv smile pioneer at center with dspr
                                dv "Ладно, пора уже идти!"
                                hide dv with dissolve
                                emp "Кажется, она оценила. Но снова не подала виду."
                                emp "Если ты решишь разбираться в Алисе дальше - путь определённо будет тернистым. Но, вероятно, оно того стоит."
                                $ ds_lp_dv += 1
                            "Осудить Алису":
                                me "И всё-таки это ты побила Электроника."
                                me "И обзывать тебя стали явно не просто так!"
                                dv "Да зачем я вообще тебе стала рассказывать что-то?!"
                                dv "Так и знала, что не стоило!"
                                dv "Пошёл ты!"
                                $ ds_lp_dv -= 2
                                hide dv with dissolve
                                "Она выскочила из стола и быстро ушла."
                                "Ты доел свой ужин в одиночестве."
                    else:
                        play sound ds_sfx_psy
                        emp "Видимо, Алисе не понравилась сложившаяся ситуация... но ничего больше ты понять не можешь."
                        $ ds_skill_points['empathy'] += 1
                        me "Ты чего, Алис?"
                        show dv angry pioneer at center with dspr
                        dv "Отстаньте от меня все!"
                        emp "К диалогу с тобой она не расположена."
                        "Вы молча доедаете ужин и выходите из столовой."
                        hide dv with dissolve
                "Промолчать":
                    window show
                    th "Да какая разница?"
                    "Вы молча доедаете ужин и выходите из столовой."
                    hide dv with dissolve
        "Cесть с Ульяной" if ds_eldv_side_taken != -1:
            window show
            $ ds_lp_us += 1
            # TODO: написать диалог в столовой с Ульяной
        "Сесть с Мику":
            window show
            $ ds_lp_mi += 1
            me "Не возражаешь, если я здесь присяду?"
            show mi normal pioneer at center   with dissolve

            play music music_list["so_good_to_be_careless"] fadein 5

            mi "Ой, да, конечно! То есть нет, не возражаю! То есть да, садись конечно!"
            "Ты садишься."
            show mi smile pioneer at center   with dspr
            mi "Сегодня, смотри, гречка. Ты любишь гречку? И вареная курица! Я вообще курицу не люблю. Ну, то есть не то что не люблю..."
            mi "Но если бы меня спросили, что бы мне больше всего хотелось, то бефстроганов или рагу… Нет, может быть, просто котлета! Или ромштекс! Ты любишь ромштексы?"
            me "Я не особо привередливый."
            play sound ds_sfx_int
            dra "И это сущая правда."
            mi "Понятно. Но вот десерты, знаешь, мне здесь не очень нравятся. Я мороженое люблю! Ты любишь мороженое? Особенно пломбир «48 копеек», но и «Ленинградское» тоже. Ой, прости, я все о себе!"
            mi "Может, ты больше эскимо любишь?"
            play sound ds_sfx_mot
            com "Ужин в компании этой девочки начинает превращаться в пытку."
            com "А ты по характеру такой человек, что не можешь просто так игнорировать собеседника.{w} Даже ее."
            th "Мы все же за одним столом сидим."
            window hide
            menu:
                "Потребовать замолчать":
                    window show
                    me "Да замолчи ты уже, дай мне поесть!"
                    show mi shocked pioneer at center with dspr
                    mi "Извини, пожалуйста, я правда-правда не хотела тебе помешать. Больше ни слова не скажу, честно-честно."
                    "Дальше ты быстро пытаешься съесть гречку, пока она снова не заговорила."
                    "Но её хватает секунд на пятнадцать, не больше."
                    $ ds_lp_mi -= 1
                "Поддержать диалог":
                    window show
                    me "А... нет, я тоже пломбиры предпочитаю."
                    "Но она тебя, кажется, не услышала."
                    $ ds_lp_mi += 1
                "Молчать":
                    window show
            show mi upset pioneer at center   with dspr
            mi "Знаешь, я однажды купила вафельный рожок, начала есть, а там внутри шуруп! Представляешь? Настоящий такой шуруп! Или болт… Я, честно говоря, в них не разбираюсь!"
            show mi normal pioneer at center   with dspr
            mi "Шурупы – это которыми закручивают гайки, а болты – это такие, которые отверткой, да?"
            th "Думаю, что если бы проводился чемпионат по скоростному поеданию пищи, я бы занял в нем одно из призовых мест."
            me "Ладно, я пойду, а тебе приятного аппетита!"
            "Ты встаёшь и направляешься к выходу."
            hide mi  with dissolve

            stop music fadeout 3

            stop ambience fadeout 2

            "Она что-то пытается сказать тебе вслед, но ты не слушаешь."
            window hide

    $ sunset_time()

    $ persistent.sprite_time = "sunset"
    scene bg ext_dining_hall_near_sunset 
    with dissolve2

    play ambience ambience_camp_center_evening fadein 3

    window show
    "Выйдя из столовой, ты садишься на ступеньки и ждёшь, пока переварится ужин."
    "Ты просто сидишь и смотришь на то, как на лагерь опускается ночь."
    play sound ds_sfx_fys
    shi "Здесь все такое живое днем – громкий детский смех, веселые крики, суета и беготня, шум и гам, спортивные игры и купания на пляже."
    shi "Но с наступлением темноты все это место резко преображается."
    shi "Дневные звуки сменяются тишиной, лишь изредка нарушаемой сверчками и ночными птицами."
    shi "Лагерь засыпал."
    shi "В каждой тени можно узнать кого угодно – приведение, лешего, просто дикое животное, но никак не пионера."
    shi "Все это ты понял по вчерашней ночи."
    shi "Здесь все строго следуют распорядку дня."
    shi "Дневной лагерь во власти людей, ночной же – скорее сил природы."
    window hide

    play sound sfx_pat_shoulder_hard

    $ renpy.pause(1)

    window show
    play sound ds_sfx_mot
    per_toc "Кто-то легонько похлопал тебя по плечу."

    play music music_list["lightness"] fadein 5

    "Ты оборачиваешься."
    show el normal pioneer at left   with dissolve
    "Это Электроник."
    el "Пойдем в карты играть."
    me "В карты?"
    el "Да! Я игру новую придумал. Интерееесную!"
    me "И какую же?"
    el "Ну, надо сначала карты найти, потом расскажу."
    me "Так ищи, в чем проблема?"
    show el upset pioneer at left   with dspr
    el "Они есть только у Ольги Дмитриевны, а она мне не даст…"
    me "Почему?"
    el "Ну, в прошлый раз…"
    "На крыльцо выходят Ольга Дмитриевна и Славя."
    show el normal pioneer at left 
    show mt normal pioneer at center 
    show sl normal pioneer at right 
    with dissolve
    el "Ольга Дмитриевна! А Семен хотел как раз у вас карты попросить!"
    me "Я вообще-то…"
    mt "Зачем?"
    show el smile pioneer at left   with dspr
    el "Мы игру новую придумали!"
    th "Не мы, а ты."
    show mt surprise pioneer at center   with dspr
    mt "Что за игра?"
    el "Будут карты – я покажу."
    show mt sad pioneer at center   with dspr
    mt "Ох, не нравится мне эта идея…{w} Но раз и Семен за, то, наверное, ничего страшного…"
    me "Да я вообще-то…"
    show sl smile pioneer at right   with dspr
    sl "Давайте я с ним схожу принесу!"
    window hide

    menu:
        "Пойти со Славей":
            $ ds_lp_sl += 1
            jump ds_day2_cards_sl
        "Пойти одному":
            jump ds_day2_cards_alone
        "Отказать":
            jump ds_day2_cards_reject

label ds_day2_cards_sl:
    window show
    "Ты решил, что это будет неплохой идеей."
    me "Если ты не против…"

    stop ambience fadeout 2

    sl "Конечно! Пошли."
    window hide
    $ ds_cards_sl = True
    $ persistent.sprite_time = "sunset"
    scene bg ext_houses_sunset 
    with dissolve

    window show
    "Вы направляетесь в сторону домика вожатой, но, проходя мимо палаток пионеров, Славя вдруг останавливается."
    show sl normal pioneer at center   with dspr
    sl "Ой, я же совсем забыла, что карты у меня!"
    play sound ds_sfx_mot
    res "Очень вовремя."
    me "А где твоя палатка?"
    show sl smile pioneer at center   with dspr
    sl "Да тут рядом, пойдем!"
    "..."
    window hide

    with fade

    scene bg ds_ext_sl_house_sunset with dissolve
    window show
    "Вы подходите к домику, который на самом деле больше напоминает вагончик."
    show sl normal pioneer at center   with dspr
    sl "Подожди тут минутку, я сейчас!"
    hide sl  with dissolve
    "Минуты ждать не пришлось – она возвращается через пару секунд."
    show sl normal pioneer at center   with dissolve
    sl "Вот!"
    jump ds_day2_sl_return

label ds_day2_sl_return:
    "Славя показывает тебе довольно потрепанную колоду карт."
    sl "Пойдем?"
    me "Пойдем."
    scene bg ext_houses_sunset with dissolve
    "..."
    window hide
    with fade
    menu:
        "Поговорить со Славей":
            window show
            "На обратном пути ты решаешь поговорить с ней в надежде что-нибудь выяснить."
            if ds_sl_interrogate:
                rhe "Может, в этот раз выйдет лучше."
            show sl normal pioneer at center   with dissolve
            me "А ты давно приехала?"
            sl "Ну, уже неделю здесь."
            me "Понятно…"
            if not ds_sl_interrogate:
                me "А откуда приехала?"
                sl "Я с севера."
                me "А поточнее?"
                show sl smile pioneer at center   with dspr
                sl "Холодного севера."
                "Она смотрит на тебя и улыбается."
                play sound ds_sfx_int
                rhe "Как информативно!"
                th "Кажется, никто в этом лагере не хочет отвечать даже на самые невинные мои вопросы, которые могут хоть чуть-чуть приоткрыть завесу тайны над всем происходящим."
                rhe "Возможно, стоит попробовать действовать по-другому."
                window hide
                menu:
                    "Надавить":
                        window show
                        me "И всё-таки, откуда ты?"
                        show sl angry pioneer at center with dspr
                        sl "Почему тебе так важно это? Из деревни я, ты в любом случае не знаешь всех деревень."
                    "Поинтересоваться увлечениями":
                        window show
                        me "А что тебе нравится?"
                        sl "В смысле?"
                        me "Ну, твои увлечения?"
                        show sl smile2 pioneer at center   with dspr
                        sl "Ааа… Я природу люблю."
                        rhe "Странно, но сейчас она почему-то немногословна."
                        me "Природу?.. Ясно.{w} Хочешь стать натуралистом?"
                        sl "Скорее краеведом. Всегда интересовалась историей родной страны."
                        play sound ds_sfx_int
                        dra "Это действительно похоже на нее."
                        dra "Казалось, из всех местных обитателей она единственная, кто не скрывает в себе никаких загадок."
                    "Не говорить ничего":
                        window show
                play sound ds_sfx_psy
                emp "Может быть, ее тоже как-то сюда забросило, как и тебя, и она просто, так же, как и ты, пока не доверяет никому до конца."
                play sound ds_sfx_int
                rhe "Попробуй прощупать почву аккуратно."
                rhe "Cпроси, например, почему она именно сюда поехала."
                window hide
                menu:
                    "Cпросить":
                        window show
                        me "А почему ты именно в этот лагерь поехала?"
                        show sl normal pioneer at center   with dspr
                        sl "Родителям путевку на работе дали."
                        th "Опять облом."
                        me "Ну, предположим, если бы у тебя был выбор?"
                        sl "Здесь хорошо.{w} Не думаю, что выбрала бы какое-нибудь другое место – здесь кажется, что ты становишься каким-то другим человеком!"
                        "Мне такого совсем не казалось."
                        me "В смысле «другим»?"
                        sl "Ну, столько возможностей, столькому можно научиться, стольких людей узнать!"
                        rhe "Сейчас она рассуждает точно так же, как и Ольга Дмитриевна."
                        play sound ds_sfx_fys
                        hfl "И это тебя настораживает."
                        stop music fadeout 3
                    "Не спрашивать":
                        window show
            me "А ты до этого была в лагерях?"
            show sl normal pioneer at center with dspr
            sl "Ну да, я каждый год езжу в лагеря!"
            sl "Даже в Артеке была! И в Орлёнке!"
            show sl smile pioneer at center with dspr
            sl "Но тут мне нравится больше всего!"
            me "А почему?"
            sl "Тут спокойнее. И ближе к природе, что ли."
            rhe "Ничего полезного ты выудить отсюда не можешь."
            $ ds_skill_points['rhetoric'] += 1
            play sound ds_sfx_psy
            vol "Пока прекрати расспросы."
        "Идти молча":
            window show
            "Обратно вы идёте молча."
    if ds_sl_keys:
        th "Стоп, у меня же ещё ключи остались..."
        window hide
        menu:
            "Отдать Славе":
                window show
                me "Cлавь, ты вчера в столовой ключи забыла..."
                show sl surprise pioneer at center with dspr
                sl "Правда? Спасибо, что вернул!"
                play sound sfx_keys_rattle
                $ ds_lp_sl += 1
                $ ds_sl_keys = False
                show sl smile pioneer at center with dspr
                emp "Она тебе благодарна."
            "Не отдавать":
                window show
                th "Нет, мне они ещё пригодятся..."
                $ ds_karma -= 10
            "Отцепить ключик себе":
                if skillcheck('interfacing', lvl_godly):
                    window show
                    inf "Ты ловко двигаешь пальцами у себя в кармане... "
                    window hide
                    $ renpy.pause(0.5)
                    window show
                    inf "И в итоге туда проваливается какой-то ключик."
                    $ ds_karma -= 5
                    $ ds_skill_points['interfacing'] += 1
                    inf "Остальное ты вынимаешь и протягиваешь Славе."
                    me "Cлавь, ты вчера в столовой ключи забыла..."
                    show sl surprise pioneer at center with dspr
                    sl "Правда? Спасибо, что вернул!"
                    play sound sfx_keys_rattle
                    $ ds_lp_sl += 1
                    $ ds_sl_keys = False
                    $ ds_some_key = True
                    show sl smile pioneer at center with dspr
                    emp "Она тебе благодарна."
                    play sound ds_sfx_mot
                    svf "А у тебя остался ключик! Только вот какой?"
                else:
                    window show
                    play sound sfx_keys_rattle
                    $ renpy.pause(0.5)
                    play sound ds_sfx_mot
                    inf "Но ключи слишком громко шумят, и Славя обращает внимание."
                    $ ds_skill_points['interfacing'] += 1
                    show sl serious pioneer at center with dspr
                    sl "Что за звук?"
                    window hide
                    menu:
                        "Сказать про ключи":
                            window show
                            me "Да я про ключи вспомнил, доставал их, чтобы тебе отдать."
                            show sl smile pioneer at center with dspr
                            sl "Правда? Спасибо, что вернул!"
                            play sound sfx_keys_rattle
                            $ ds_lp_sl += 1
                            $ ds_sl_keys = False
                            emp "Она тебе благодарна."
                        "Cоврать":
                            if skillcheck('drama', lvl_formidable):
                                window show
                                play sound ds_sfx_int
                                dra "Скажите, мессир, будто это кто-то другой проходил."
                                dra "И главное - покажите, что вы тоже ищете источник."
                                me "Не знаю, тут ходит кто-то, наверное. Или в лесу."
                                $ ds_skill_points['drama'] += 1
                                show sl normal pioneer at center with dspr
                                sl "А, ну ладно!"
                                dra "Про ключи лучше не говори."
                            else:
                                window show
                                play sound ds_sfx_int
                                dra "Это не вы! Это точно не вы!"
                                me "Этот звук не от меня!"
                                sl "Точно? Покажи, что у тебя в кармане!"
                                "Ты достаёшь ключи."
                                $ ds_skill_points['drama'] += 1
                                show sl angry pioneer at center with dspr
                                sl "Значит, ключи украл? А я тебя в столовую проводила..."
                                $ ds_lp_sl -= 1
                                me "Да ты просто их в столовой забыла, а я хотел вернуть."
                                sl "Ага, хотел... Отдавай их!"
                                play sound sfx_keys_rattle
                                "Тебе приходится их отдать."
                                play sound ds_sfx_psy
                                emp "Ей очень обидно, что ты хотел скрыть их от неё. Она же могла быть и наказана за потерю ключей."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_dining_hall_near_sunset 
    with dissolve

    play ambience ambience_camp_center_evening fadein 3

    show sl normal pioneer at cleft 
    show mt normal pioneer at cright 
    with dissolve
    window show
    mt "Я же вспомнила, что карты у тебя!"
    sl "Да ничего, мы принесли."
    show mt smile pioneer at cright   with dspr
    mt "Ну и отлично!"
    jump ds_day2_prepare_tour

label ds_day2_cards_alone:
    window show
    show sl normal pioneer at right   with dspr
    me "Да я и один могу сходить…"
    show mt normal pioneer at center   with dspr
    mt "Ладно. Возьмешь у меня в домике в ящике стола."

    stop ambience fadeout 2

    stop music fadeout 3

    if skillcheck('shivers', lvl_medium, passive=True):
        play sound ds_sfx_fys
        shi "Возможно, карты не там. Какое-то такое ощущение у тебя есть..."
        $ ds_skill_points['shivers'] += 1
        window hide
        menu:
            "Переспросить":
                window show
                me "А они точно у вас дома?"
                show mt surprise pioneer at center with dspr
                mt "Да... хотя погоди."
                mt "Точно! Славя же их брала. Тебе надо к ней идти, домик 12."
                me "Cпасибо..."
                jump ds_day2_cards_alone_correct
            "Не переспрашивать":
                pass
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_houses_sunset 
    with dissolve

    play ambience ambience_camp_center_evening fadein 2

    window show
    th "И чего я вообще согласился?"
    th "С другой стороны, какие у меня были еще варианты?"
    th "Ночью здесь делать особо нечего, а так хоть развлекусь немного."
    play sound ds_sfx_fys
    hfl "Но сейчас не самое лучшее время для развлечений."
    play sound ds_sfx_int
    lgc "Хотя, с другой стороны, если {i}здесь{/i} есть этот лагерь, эти пионеры, то это кому-то надо?"
    lgc "Да даже если и не надо, то самое логичное – ответы искать именно тут, а не в лесах или полях."
    lgc "А в данный момент {i}ответы{/i} собираются играть в карты..."
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "sunset"
    scene bg int_house_of_mt_sunset 
    with dissolve

    play ambience ambience_int_cabin_evening fadein 2

    window show
    "Ты открываешь дверь своим ключом и заходишь."
    "Карт в ящике стола не оказалось."
    play sound ds_sfx_mot
    res "Как так?"
    "Там есть всё, что угодно – ножи, вилки, чашки, тарелки, клейкая лента, ножницы, пара садовых перчаток, моток веревки, несколько целлофановых пакетов, карандаш и пара сломанных ручек…"
    "Но не карты."
    play sound ds_sfx_mot
    svf "Посмотри в шкафу."
    "Там в основном одежда Ольги Дмитриевны." 
    play sound ds_sfx_mot
    per_eye "Внизу есть маленький ящичек с замочной скважиной."
    "Ты тянешь его, но он не открывается."
    th "Интересно, что она там прячет?"
    play sound ds_sfx_int
    lgc "Взламывать его явно не лучшая идея, тем более ты абсолютно не уверен, что найдёшь там карты."

    if ds_sl_keys:
        "Ты уже собираешься было уходить и делаешь шаги."
        play sound ds_sfx_mot
        per_hea "В кармане что-то звенит."
        play sound ds_sfx_mot
        res "Это же ключи, которые вчера забыла Славя."
        th "А что если..."
        window hide
        menu:
            "Использовать ключи":
                window show
                "Некоторое время ты простоял в раздумьях, но потом уверенно подходишь к шкафу и начинаешь прикидывать, какой ключ может подойти к замку."
                play sound ds_sfx_int
                lgc "Конечно, на успех особо рассчитывать не стоит, ведь с какой стати у Слави мог быть ключ от личного ящика Ольги Дмитриевны..."
                play sound sfx_key_drawer
                "Но к твоему удивлению, замок приветливо проворачивается несколько раз, и ты уже собираешься потянуть на себя ручку..."
                window hide

                play sound sfx_open_door_kick

                $ renpy.pause(1)

                window show
                play sound ds_sfx_mot
                per_hea "Как вдруг сзади хлопает дверь."
                hfl "Ты подскакиваешь на месте, резко разворачиваешься, но в домике никого, кроме тебя, нет."
                th "Наверное, ветер..."
                window hide
                menu:
                    "Проверить":
                        scene bg ext_house_of_mt_sunset
                        with dissolve
                        window show
                        "Ты с опаской выглядываешь на улицу, но и там не оказывается ни одной живой души."
                        play sound ds_sfx_mot
                        com "Возможно, ничего страшного и не произошло, но тебе все равно не по себе."
                        window hide

                        with fade2

                        $ renpy.pause(2.0)

                        scene bg int_house_of_mt_sunset
                        with dissolve

                        window show
                        "После тщательного осмотра соседних кустов ты все-таки решаешь закончить начатое и уже собираешься все же узнать все страшные секреты вожатой..."
                        sl "Семен, что ты тут так долго?"
                        show sl normal pioneer at center   with dissolve
                        me "А... я... да..."
                        com "Трясущимися руками ты стараешься побыстрее закрыть ящик и вынуть ключ."
                        "Славя подходит ближе."
                        show sl smile pioneer at center   with dspr
                        sl "Ой, мои ключи! А я их обыскалась! Где ты..."
                        $ ds_sl_keys = False
                        $ ds_lp_sl += 1
                        me "Да вот по дороге... В кустах валялись..."
                        play sound ds_sfx_mot
                        res "Хоршшо, что ты таки успел замести следы."
                        me "Пойдем?"
                        th "И сейчас мне больше всего хочется поскорее убраться отсюда и забыть о попытке бесцеремонного вторжения в чужую личную жизнь."
                        jump ds_day2_sl_return
                    "Продолжить изучать":
                        window show
                        "Ты решаешь забить на шум и приступаешь к изучению содержимого ящика."
                        play sound ds_sfx_mot
                        per_eye "Впрочем, никаких секретов тут не оказывается - лишь документы членов отряда Ольги Дмитриевны."
                        th "И что же я тут могу узнать?"
                        per_eye "Посмотрим..."
                        per_eye "1. Двачевская Алиса Викентьевна{n}Дата рождения - 3 апреля 1970 года{n}Место рождения - город ..., РСФСР"
                        per_eye "ВНИМАНИЕ! Обратите особое внимание, имеются проблемы в поведении, обусловленные..."
                        sl "Семён, а что ты тут делаешь?"
                        show sl serious pioneer at center with dspr
                        hfl "Это Славя. И она немного не понимает, что тут происходит."
                        window hide
                        menu:
                            "Изобразить невинного":
                                if skillcheck('drama', lvl_godly):
                                    window show
                                    dra "Покажите, что вы, напротив, закрывали ящик, не открывали."
                                    "Ты абсолютно спокойно и естественно закрываешь ящик."
                                    $ ds_skill_points['drama'] += 1
                                    me "Да так, тут ящик открыт был, я и закрыл его."
                                    show sl normal pioneer at center with dspr
                                    sl "А, ну ладно!"
                                    sl "Карты у меня, в общем!"
                                    jump ds_day2_sl_return
                                else:
                                    window show
                                    dra "У вас, увы, не получается показать, что вы не при делах."
                                    $ ds_skill_points['drama'] += 1
                                    show sl angry pioneer at center with dspr
                                    sl "Семён, между прочим лезть в чужие вещи нехорошо!"
                                    sl "Так, всё, идём обратно!"
                                    "Ты закрываешь ящик и идёшь обратно."
                                    scene bg ext_houses_sunset with dissolve
                                    "Вы идёте молча, и через пару минут доходите до столовой."
                                    jump ds_day2_prepare_tour
                            "Нагло продолжить читать":
                                window show
                                play sound ds_sfx_mot
                                com "Ты продолжаешь читать, будто Слави тут нет вовсе."
                                $ ds_semtype += 1
                                per_eye "2. Мицгол Евгения Исааковна{n}Дата рождения - ... ... 1970 года{n}Место рождения - город Одесса, УССР"
                                play sound ds_sfx_int
                                enc "Таки она еврейской национальности..."
                                show sl surprise pioneer far at right with dspr
                                com "Тем временем Славя потеряла дар речи от такой хуцпы."
                                per_eye "3. Cоветова Ульяна Ильична{n}Дата рождения - ... ... 1973 года{n}Место рождения - город Ленинград, РСФСР"
                                per_eye "ПРИМЕЧАНИЕ: включена в первый отряд по ошибке. Исправлять не следует."
                                play sound ds_sfx_int
                                lgc "Так вот почему она в первом отряде рядом с 16-17-летними девушками!"
                                per_eye "4. Cыроежкин Сергей ...{n}Дата рождения - 23 марта 1970 года, место рождения - город Москва, РСФСР"
                                per_eye "5. Унылова Елена ...{n}Дата рождения - 25 сентября 1970 года{n}Место рождения - город ..., РСФСР"
                                per_eye "6. Феоктистова Славяна ...{n}Дата рождения - 12 мая 1970 года{n}Место рождения - деревня Мятусово, Ленинградская область, РСФСР"
                                per_eye "7. Хацуне Мику (отчество отсутствует){n}Дата рождения - 31 августа 1970 года{n}Место рождения - город Токио, Япония"
                                per_eye "ВНИМАНИЕ! На родине является известной певицей, поэтому во избежание дипломатических инцидентов следите за ней особенно пристально."
                                per_eye "Тут же есть и сведения о тебе."
                                per_eye "8. Пёрсунов Семён ...{n}Дата рождения - ... ... 1970 года{n}Место рождения - город Ленинград, РСФСР"
                                per_eye "ПРИМЕЧАНИЕ: прибывает 9 августа в связи с работой родителей. Родители - послы, поэтому будьте аккуратнее с ним."
                                per_eye "ВНИМАНИЕ! Отличается крайней рассеянностью, поэтому возможно, что приедет в неподходящей одежде без вещей."
                                lgc "Так вот почему никто не задался вопросом, почему ты в зимней одежде..."
                                play sound ds_sfx_int
                                dra "Да вы, оказывается, мажор, мессир."
                                dra "Теперь мы наконец-то знаем, кого отыгрывать!"
                                "Ты закрываешь ящик и собирался было окликнуть Славю..."
                                play sound ds_sfx_mot
                                res "Но Слави нет!"
                                $ ds_lp_sl -= 1
                                "Тебе приходится идти одному."
                            "Извиниться":
                                window show
                                me "Извини, что так долго... карты искал просто."
                                "Славя подходит ближе."
                                show sl smile pioneer at center   with dspr
                                sl "Ой, мои ключи! А я их обыскалась! Где ты..."
                                $ ds_sl_keys = False
                                $ ds_lp_sl += 1
                                me "Да вот по дороге... В кустах валялись..."
                                play sound ds_sfx_mot
                                res "Хоршшо, что ты таки успел замести следы."
                                me "Пойдем?"
                                th "И сейчас мне больше всего хочется поскорее убраться отсюда и забыть о попытке бесцеремонного вторжения в чужую личную жизнь."
                                jump ds_day2_sl_return
            "Проверить обстановку":
                if skillcheck('half_light', lvl_medium):
                    window show
                    play sound ds_sfx_fys
                    hfl "Тебе начинает казаться, что кто-то смотрит за тобой."
                    hfl "Выйди и осмотрись."
                    scene scene bg ext_house_of_mt_sunset
                    with dissolve
                    "Ты выходишь из домика."
                    hfl "Осмотри каждый куст."
                    "Ты просматриваешь каждый клочок земли вокруг домика вожатой..."
                    show sl surprise pioneer at center with dissolve
                    sl "Семён, а что ты ищешь?"
                    hfl "Ой, Славя... предчувствие не подвело тебя."
                    $ ds_skill_points['half_light'] += 1
                    me "Да так, ничего..."
                    show sl smile pioneer at center with dspr
                    sl "Карты у меня!"
                    jump ds_day2_sl_return
                else:
                    window show
                    play sound ds_sfx_fys
                    hfl "Да всё в порядке! Продолжай изучать!"
                    $ ds_skill_points['half_light'] += 1
                    "Ты приступаешь к изучению содержимого ящика."
                    play sound ds_sfx_mot
                    per_eye "Впрочем, никаких секретов тут не оказывается - лишь документы членов отряда Ольги Дмитриевны."
                    th "И что же я тут могу узнать?"
                    per_eye "Посмотрим..."
                    per_eye "1. Двачевская Алиса Викентьевна{n}Дата рождения - 3 апреля 1970 года{n}Место рождения - город ..., РСФСР"
                    per_eye "ВНИМАНИЕ! Обратите особое внимание, имеются проблемы в поведении, обусловленные..."
                    sl "Семён, а что ты тут делаешь?"
                    show sl serious pioneer at center with dspr
                    hfl "Это Славя. И она немного не понимает, что тут происходит."
                    window hide
                    menu:
                        "Изобразить невинного":
                            if skillcheck('drama', lvl_godly):
                                window show
                                dra "Покажите, что вы, напротив, закрывали ящик, не открывали."
                                "Ты абсолютно спокойно и естественно закрываешь ящик."
                                $ ds_skill_points['drama'] += 1
                                me "Да так, тут ящик открыт был, я и закрыл его."
                                show sl normal pioneer at center with dspr
                                sl "А, ну ладно!"
                                sl "Карты у меня, в общем!"
                                jump ds_day2_sl_return
                            else:
                                window show
                                dra "У вас, увы, не получается показать, что вы не при делах."
                                $ ds_skill_points['drama'] += 1
                                show sl angry pioneer at center with dspr
                                sl "Семён, между прочим лезть в чужие вещи нехорошо!"
                                sl "Так, всё, идём обратно!"
                                "Ты закрываешь ящик и идёшь обратно."
                                scene bg ext_houses_sunset with dissolve
                                "Вы идёте молча, и через пару минут доходите до столовой."
                                jump ds_day2_prepare_tour
                        "Нагло продолжить читать":
                            window show
                            play sound ds_sfx_mot
                            com "Ты продолжаешь читать, будто Слави тут нет вовсе."
                            $ ds_semtype += 1
                            per_eye "2. Мицгол Евгения Исааковна{n}Дата рождения - ... ... 1970 года{n}Место рождения - город Одесса, УССР"
                            play sound ds_sfx_int
                            enc "Таки она еврейской национальности..."
                            show sl surprise pioneer far at right with dspr
                            com "Тем временем Славя потеряла дар речи от такой хуцпы."
                            per_eye "3. Cоветова Ульяна Ильична{n}Дата рождения - ... ... 1973 года{n}Место рождения - город Ленинград, РСФСР"
                            per_eye "ПРИМЕЧАНИЕ: включена в первый отряд по ошибке. Исправлять не следует."
                            play sound ds_sfx_int
                            lgc "Так вот почему она в первом отряде рядом с 16-17-летними девушками!"
                            per_eye "4. Cыроежкин Сергей ...{n}Дата рождения - 23 марта 1970 года, место рождения - город Москва, РСФСР"
                            per_eye "5. Унылова Елена ...{n}Дата рождения - 25 сентября 1970 года{n}Место рождения - город ..., РСФСР"
                            per_eye "6. Феоктистова Славяна ...{n}Дата рождения - 12 мая 1970 года{n}Место рождения - деревня Мятусово, Ленинградская область, РСФСР"
                            per_eye "7. Хацуне Мику (отчество отсутствует){n}Дата рождения - 31 августа 1970 года{n}Место рождения - город Токио, Япония"
                            per_eye "ВНИМАНИЕ! На родине является известной певицей, поэтому во избежание дипломатических инцидентов следите за ней особенно пристально."
                            per_eye "Тут же есть и сведения о тебе."
                            per_eye "8. Пёрсунов Семён ...{n}Дата рождения - ... ... 1970 года{n}Место рождения - город Ленинград, РСФСР"
                            per_eye "ПРИМЕЧАНИЕ: прибывает 9 августа в связи с работой родителей. Родители - послы, поэтому будьте аккуратнее с ним."
                            per_eye "ВНИМАНИЕ! Отличается крайней рассеянностью, поэтому возможно, что приедет в неподходящей одежде без вещей."
                            lgc "Так вот почему никто не задался вопросом, почему ты в зимней одежде..."
                            play sound ds_sfx_int
                            dra "Да вы, оказывается, мажор, мессир."
                            dra "Теперь мы наконец-то знаем, кого отыгрывать!"
                            "Ты закрываешь ящик и собирался было окликнуть Славю..."
                            play sound ds_sfx_mot
                            res "Но Слави нет!"
                            $ ds_lp_sl -= 1
                            "Тебе приходится идти одному."
                        "Извиниться":
                            window show
                            me "Извини, что так долго... карты искал просто."
                            "Славя подходит ближе."
                            show sl smile pioneer at center   with dspr
                            sl "Ой, мои ключи! А я их обыскалась! Где ты..."
                            $ ds_sl_keys = False
                            $ ds_lp_sl += 1
                            me "Да вот по дороге... В кустах валялись..."
                            play sound ds_sfx_mot
                            res "Хоршшо, что ты таки успел замести следы."
                            me "Пойдем?"
                            th "И сейчас мне больше всего хочется поскорее убраться отсюда и забыть о попытке бесцеремонного вторжения в чужую личную жизнь."
                            jump ds_day2_sl_return
            "Не использовать ключи":
                th "Да ну его, вряд ли тут есть что-то интересное."
                "С этими мыслями ты выходишь из домика."

        window hide

    else:
        window hide

    stop ambience fadeout 2        

    $ persistent.sprite_time = "sunset"
    scene bg ext_dining_hall_near_sunset 
    with dissolve

    play ambience ambience_camp_center_evening fadein 3

    show mt normal pioneer at right 
    show sl normal pioneer at left 
    with dissolve
    window show
    mt "Ой, извини, а карты у Слави были в палатке.{w} Пока ты ходил, она сбегала."
    show sl smile2 pioneer at left   with dspr
    "Ты смотришь на Славю, она виновато улыбается."
    th "Да ладно уж, что там, не беспокойтесь обо мне…"

    jump ds_day2_prepare_tour

label ds_day2_cards_alone_correct:
    $ persistent.sprite_time = "sunset"
    scene bg ext_houses_sunset 
    with dissolve

    play ambience ambience_camp_center_evening fadein 2

    window show
    th "И чего я вообще согласился?"
    th "С другой стороны, какие у меня были еще варианты?"
    th "Ночью здесь делать особо нечего, а так хоть развлекусь немного."
    play sound ds_sfx_fys
    hfl "Но сейчас не самое лучшее время для развлечений."
    play sound ds_sfx_int
    lgc "Хотя, с другой стороны, если {i}здесь{/i} есть этот лагерь, эти пионеры, то это кому-то надо?"
    lgc "Да даже если и не надо, то самое логичное – ответы искать именно тут, а не в лесах или полях."
    lgc "А в данный момент {i}ответы{/i} собираются играть в карты..."
    window hide

    stop ambience fadeout 2

    $ persistent.sprite_time = "sunset"
    scene bg ds_ext_sl_house_sunset 
    with dissolve

    "Ты подходишь к домику Слави и заходишь в него, благо дверь открыта."
    ## TODO: BG: домик Слави вечером
    scene bg int_house_of_sl_day with dissolve

    "Карты лежат прямо на столе."
    "Ты берёшь их в руки."
    play sound ds_sfx_mot
    inf "А что если их пометить? Тогда в турнире тебе будет проще выиграть!"
    window hide
    menu:
        "Пометить карты":
            $ ds_karma -= 20
            if skillcheck('interfacing', lvl_legendary):
                window show
                inf "Ты одалживаешь у Слави немного мела, лежащего тут же и, используя его, помечаешь каждую карту."
                $ ds_cards_labeled = True
                $ ds_skill_points['interfacing'] += 1
            else:
                window show
                inf "Ты берёшь со стола мел и пытаешься пометить карты..."
                inf "Но в итоге метки получаются слишком заметными."
                $ ds_cards_damaged = True
                $ ds_skill_points['interfacing'] += 1
        "Не помечать":
            th "Нет, лучше всё же играть честно... да и вдруг спалят?"
    $ persistent.sprite_time = "sunset"
    scene bg ds_ext_sl_house_sunset 
    with dissolve
    "Забрав карты, ты выходишь из домика и спешишь обратно."
    window hide
    $ persistent.sprite_time = "sunset"
    scene bg ext_houses_sunset 
    with dissolve
    $ renpy.pause(2.0)
    $ persistent.sprite_time = "sunset"
    scene bg ext_dining_hall_near_sunset 
    with dissolve

    play ambience ambience_camp_center_evening fadein 3

    show mt normal pioneer at right 
    show sl normal pioneer at left 
    with dissolve
    window show
    sl "Как сходил за картами?"
    me "Всё хорошо, карты нашёл."
    "С этими словами ты отдаёшь их Ольге Дмитриевне."
    mt "Отлично!"
    jump ds_day2_prepare_tour

label ds_day2_cards_reject:
    window show
    show sl normal pioneer at right   with dspr
    me "Да не пойду я за картами, и вообще, я никакого отношения и идеям Электроника не имею!"
    show mt normal pioneer at center   with dspr
    mt "Ладно. Славя, сходи за картами, пожалуйста."
    sl "Хорошо."
    hide sl with dissolve
    "Ты остаёшься у крыльца с Ольгой Дмитриевной."
    window hide
    $ renpy.pause(3.0)
    window show
    show sl normal pioneer at right with dspr
    "Впрочем, максимум на пару минут - Славя быстро вернулась с картами."
    sl "Вот и карты!"
    mt "Отлично!"
    jump ds_day2_prepare_tour

label ds_day2_prepare_tour:
    hide mt 
    hide sl 
    with dissolve
    "Славя и Ольга Дмитриевна зашли внутрь."
    if not ds_beat_dv and not ds_betray_dv:
        play sound ds_sfx_mot
        per_toc "Ты уже собирался последовать за ними, как вдруг тебя кто-то резко дёргает за руку."
        show dv normal pioneer at center   with dspr

        stop ambience fadeout 2

        play music music_list["glimmering_coals"] fadein 5

        "Это Алиса."
        play sound ds_sfx_mot
        com "Она смотрит так, что у тебя мурашки побежали по спине."
        me "Тебе что-то надо?"
        dv "Что, тоже планируешь участвовать в этой дурацкой игре?"
        me "Ну... да, а что такого?"
        dv "Нет, ничего."
        show dv smile pioneer at center   with dspr:
            linear 0.5 xalign 0.72
        "Она уже собиралась было уходить, но вдруг оборачивается и внимательно смотрит на тебя, улыбнувшись."
        show dv smile pioneer at right :
            linear 0.5 xalign 0.5
        dv "А в карты-то играть умеешь?"
        me "Умею немного."
        play sound ds_sfx_int
        rhe "Что ей от тебя нужно?"
        dv "В дурака небось и все?"
        th "Ты-то как будто звезда покера."
        me "Ну, в принципе, да..."
        show dv normal pioneer at center   with dspr
        dv "Значит, тут у тебя шансов никаких."
        me "Почему?"
        show dv angry pioneer at center   with dspr
        dv "По кочану!"
        me "То есть ты правила знаешь?"
        show dv smile pioneer at center   with dspr
        dv "Конечно!"
        me "Ну, значит, у тебя будет преимущество."
        rhe "Продолжать разговор дальше нет смысла, лучше уйди."
        "Ты делаешь несколько шагов к двери."
        show dv angry pioneer at center   with dspr
        dv "Что ты все уйти-то пытаешься?!"
        th "А о чем, собственно, еще говорить..."
        show dv smile pioneer at center   with dspr
        dv "Давай поспорим."
        window hide
        menu:
            "Переспросить":
                window show
                me "Ты про что?"
                show dv normal pioneer at center   with dspr
                dv "Какой же ты тупой!{w} Про карты, про что же еще!"
            "Продолжить":
                window show
        me "И каков же предмет спора?"
        show dv smile pioneer at center   with dspr
        dv "Что я тебя обыграю!"
        window hide
        menu:
            "Не возражать":
                window show
                me "Ну, это самый вероятный исход."
                show dv normal pioneer at center   with dspr
                dv "Значит, боишься?"
                me "Я не боюсь...{w} Просто не привык спорить, когда не уверен."
                dv "И рисковать ты тоже не привык."
                play sound ds_sfx_psy
                aut "Это правда, как ни печально это признавать."
                th "Сама наблюдательность просто-таки."
                me "Ладно, тогда я..."
            "Возразить":
                window show
                me "А ты уверена?"
                show dv surprise pioneer at center with dspr
                play sound ds_sfx_psy
                aut "Для неё твой вопрос оказался неожиданностью."
                show dv grin pioneer at center with dspr
                dv "Конечно, уверена!"
                play sound ds_sfx_int
                rhe "Лучше не ввязывайся. У тебя сейчас есть возможность соскочить со спора без потери лица."
                me "А вот я уверен, что я выиграю."
                me "Поэтому, чтобы тебя не позорить, я откажусь от спора."
        show dv angry pioneer at center   with dspr 
        dv "Нет уж!"
        me "Ну что еще?"
        rhe "Алиса начинает надоедать своей пустой болтовней про какой-то бессмысленный спор."
        show dv grin pioneer at center   with dspr
        dv "Если не согласишься спорить, я всем расскажу, что ты ко мне приставал!"
        play sound ds_sfx_mot
        res "А когда ты успел к ней пристать?!"
        me "Что?!"
        dv "Что слышал!"
        th "Да, пожалуй, она вполне может..."
        me "Но это же глупо!{w} Тебе никто не поверит – я всего неполных два дня здесь, да и к тому же..."
        show dv normal pioneer at center   with dspr
        dv "Хочешь проверить?"
        me "Ну, предположим..."
        window hide
        menu:
            "Уточнить условия":
                window show
                "И что будет, если я выиграю?"
                show dv smile pioneer at center   with dspr
                dv "Я никому ничего не скажу."
                me "А если проиграю?"
                show dv normal pioneer at center   with dspr
                dv "Какой же ты тупой!{w} Расскажу, что ты ко мне приставал, говорила же уже."
                me "То есть, получается, мне нужно доказать, что я не делал того, что не делал и так?"
                dv "Считай как хочешь."
            "Не уточнять":
                window show
        play sound ds_sfx_psy
        aut "Передо тобой стоит непростой выбор."
        aut "С одной стороны, глупо соглашаться – ты не знаешь правил, да и вообще, азартные игры не были твоим коньком."
        play sound ds_sfx_fys
        hfl "Но с другой – она вполне может сильно осложнить твоё дальнейшее пребывание здесь."
        hfl "Хотя можно ли ей верить?"
        hfl "Даже если ты выиграешь, не претворит ли она свои угрозы в жизнь?"
        play sound ds_sfx_int
        dra "Вряд ли. Она вообще так просто играет с вами, не собираясь претворять угрозы в жизнь."
        dra "И лучше бы вам тоже подыгать, мессир."
        dv "Так что решил?"
        show un normal pioneer at right   with dissolve
        "Ты уже было собирался ответить, как у тебя из-за спины бесшумно выныривает Лена."
        show dv angry pioneer at center   with dspr
        dv "Чего тебе?"
        show un scared pioneer at right   with dspr
        un "Ничего..."
        hide un  with dissolve
        "Лена спешит ретироваться."
        show dv normal pioneer at center   with dspr
        dv "Ну?"
        window hide
        menu:
            "Поспорить с Алисой":
                $ ds_bet_dv = True
                $ ds_lp_dv += 1
                $ ds_lp_un -= 1
                $ ds_skill_points['authority'] += 1
                window show
                th "Возможно, я еще сто раз пожалею об этом..."
                me "Ладно, идет!"
                show dv smile pioneer at center   with dspr
                "Она улыбается."
                me "Только если я выиграю..."
                dv "Да-да, все честно, без обмана!"
                "Алиса поднимается по лестнице и входит внутрь."
                hide dv  with dissolve
                th "И зачем я во все это ввязался?"
                play sound ds_sfx_fys
                hfl "Она в любом случае найдет, как мне жизнь испортить."
                hfl "Раз уж решила..."
            "Не спорить с Алисой":
                $ ds_lp_dv -= 1
                $ ds_lp_un += 1
                window show
                th "Нет, ни в какие глупые авантюры я пускаться не намерен!"
                me "Извини уж..."
                show dv angry pioneer at center   with dspr
                dv "Слабак!"
                "Она фыркает, поднимается по лестнице и у самой двери бросает тебе."
                dv "Готовься к последствиям!"
                hide dv  with dissolve
                th "Последствиям?.."
                th "Поступил ли я правильно?"
                play sound ds_sfx_fys
                hfl "В конце концов, она вполне может до предела осложнить твою жизнь здесь."
                hfl "Но с другой стороны, у тебя просто нет права на опрометчивые шаги."

        stop music fadeout 3

        "Ты тяжело вздыхаешь и направляешься за ней в столовую."
    else:
        "Ты проходишь вслед за ними в столовую."
    window hide
    jump ds_day2_tour

label ds_day2_tour:
    $ persistent.sprite_time = "sunset"
    scene bg int_dining_hall_sunset 
    with dissolve

    play ambience ambience_medium_crowd_indoors_1 fadein 3

    window show
    "Внутри все уже было готово."
    "Тут и там толпятся пионеры, весело разговаривая о своем."
    "Помещение столовой очистили, чтобы освободить место для игроков и зрителей."
    "Ты осматриваешься."
    "В дальнем углу вокруг одного из столов что-то происходит."
    "Подойдя ближе, ты видишь большой лист ватмана с какой-то схемой."
    play sound ds_sfx_mot
    per_eye "В списке участников оказывается и твоё имя."
    me "Эй, и кто придумал такое распределение?"
    "Толкаешь ты Электроника, стоящего рядом."
    show el smile pioneer at center with dissolve
    el "Конечно же ваш покорный слуга!"
    "Он отвешивает тебе поклон"
    play sound ds_sfx_mot
    com "Тебя аж передёргивает."
    me "Ну, и зачем меня сюда включили?"
    el "Так распорядился слепой жребий."
    th "Хороший жребий – со всеми участниками турнира я так или иначе уже успел познакомиться."
    th "А ведь, помимо них, тут еще не один десяток пионеров!"
    com "Ты начинаешь испытывать необъяснимое чувство тревоги."
    com "Такое, когда кажется, что за тобой кто-то наблюдает в пустой плотно закрытой комнате без окон."
    window hide
    menu:
        "Принять участие в турнире":
            window show
            me "Ладно, так тому и быть..."
        "Отказаться от участия":
            window show
            me "И всё же я участвовать не буду!"
            show el upset pioneer at center with dspr
            el "Как? И кого же нам взять на замену?"
            me "Я не знаю, меня это не волнует! Я не соглашался участвовать в турнире!"
            el "Ладно, как хочешь..."
            if ds_bet_dv:
                $ ds_lp_dv -= 3
            $ ds_tour_result = -1
            jump ds_day2_after_tour

    show el normal pioneer at center   with dissolve
    window show
    me "А призы какие-нибудь будут?"
    th "Хочется развеяться бессмысленным разговором."
    show us grin pioneer at left   with dissolve
    "Электроник только открыл рот, чтобы ответить, как откуда ни возьмись появляется Ульянка и начала прыгать вокруг него."
    us "Призы-призы!"
    show us grin pioneer at right   with dspr
    us "Я что-то слышала про призы!"
    me "Знаешь, какой главный принцип Олимпийских игр?"
    show us laugh pioneer at right   with dspr
    us "Нет, какой?"
    me "Вот вырастешь – узнаешь!"
    show us dontlike pioneer at left   with dspr
    "Она надувает губки и обращается к Электронику."
    us "Так призы будут?"
    show el surprise pioneer at center   with dspr
    el "Ну... Я не знаю.{w} Не от меня это зависит."
    "Он обреченно разводит руками."
    th "А ведь действительно, раз уж затеяли эту дурацкую игру, то могли хотя бы шоколадными медалями озаботиться."
    hide us  with dissolve
    "Ульянка неожиданно срывается с места и куда-то бежит."
    th "Мне бы чуток ее оптимизма..."
    me "Ну так что, правила объяснишь?"
    show el normal pioneer at center   with dspr
    el "Всему свое время!{w} Еще не все собрались."
    play sound ds_sfx_mot
    per_eye "Ты окидываешь столовую взглядом и сразу же замечаешь Алису, Славю, Лену, Мику и Шурика."
    me "Вроде бы все..."
    show el surprise pioneer at center   with dspr
    el "Как же! Жени нет!"
    play sound ds_sfx_psy
    emp "Кажется, он сказал это несколько взволнованным тоном."
    me "Ну нет и нет, что теперь?"
    me "Поставь вместо нее кого-нибудь другого."
    el "Нельзя..."
    "Растягивая каждую букву, отвечает он."
    play sound ds_sfx_int
    rhe "Лучше не уточнять, почему именно нельзя."
    me "Ну сходи тогда за ней, что ли, я не знаю."
    show el normal pioneer at center   with dspr
    with None
    show mt normal pioneer at right   with dspr
    with dissolve
    mt "Не надо ему никуда ходить – он организатор, ему не положено!"
    play sound ds_sfx_mot
    res "Словно из-под земли рядом с вами возникает вожатая."
    show el upset pioneer at center   with dspr
    el "Но Ольга Дмитриевна!"
    show mt smile pioneer at right   with dspr
    mt "Семен сходит.{w} Так, Семен?"
    "Она смотрит на тебя и улыбается."
    th "Конечно, везде я..."
    window hide
    menu:
        "Cходить":
            window show
            th "Cпорить не стоит, так как в моём положении это не лучшая идея."
            jump ds_day2_find_mz
        "Отказаться":
            if skillcheck('suggestion', lvl_formidable):
                window show
                play sound ds_sfx_psy
                sug "И пусть всё-таки пойдёт Электроник, ты ведь даже не представляешь, где может быть Женя!"
                me "Я ещё плохо ориентируюсь в лагере и без понятия, где может быть Женя. Пусть лучше он пойдёт!"
                show mt normal pioneer at right with dspr
                mt "И то верно... Сходи, пожалуйста, за Женей."
                el "Ладно."
                hide el with dissolve
                window hide
                $ renpy.pause(3.0)
                window show
                show el smile pioneer at center with dissolve
                show mz normal pioneer at left with dissolve
                "Долго ждать не пришлось - Электроник нашёл Женю и привёл на место."
                $ ds_mz_brought_el = True
                el "А вот и мы!"
                mt "Отлично, тогда начнём!"
                jump ds_day2_game
            else:
                window show
                play sound ds_sfx_psy
                sug "Но ты же не хочешь!"
                me "Может, всё-таки не пойду?"
                show mt angry pioneer at right with dspr
                mt "Нет, пойдёшь! Пионер должен выручать своих товарищей!"
                me "Ладно-ладно..."
                jump ds_day2_find_mz

label ds_day2_find_mz:
    me "А где она?"
    show mt normal pioneer at right   with dspr
    mt "Наверное, в библиотеке."
    me "Ладно..."
    "Протгиваешь ты и направляешься в сторону выхода из столовой."
    hide el 
    hide mt 
    with dissolve
    el "Только быстрее!"

    stop ambience fadeout 3

    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_dining_hall_away_sunset 
    with dissolve

    play ambience ambience_camp_center_evening fadein 2

    window show
    th "Скоро и ночь уже."
    "Ты не спеша, стараясь убить как можно больше времени, направляешься в сторону библиотеки."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg ext_square_sunset 
    with dissolve

    play music music_list["your_bright_side"] fadein 5

    window show
    play sound ds_sfx_mot
    per_eye "Проходя по площади, ты замечаешь, что кто-то сидит на лавочке."
    play sound ds_sfx_int
    lgc "Странно...{w} Ведь все должны быть в столовой."
    show mz normal glasses pioneer at center   with dissolve
    per_eye "При ближайшем рассмотрении это оказывется Женя."
    me "Ты что тут делаешь?{w} Тебя все обыскались!"
    show mz angry glasses pioneer at center   with dspr
    mz "Сижу, как видишь."
    me "Пойдем скорее!"
    show mz normal glasses pioneer at center   with dspr
    mz "Не хочу."
    "Женя отворачивается от тебя."
    me "Почему?"
    mz "Не хочу и все!"
    "Ты садишься рядом."
    window hide
    menu:
        "Уговорить":
            if skillcheck('suggestion', lvl_challenging):
                window show
                $ ds_skill_points['suggestion'] += 1
                play sound ds_sfx_psy
                sug "Начни убеждать её с того, что тебе эта идея тоже не нравится."
                me "Слушай, мне тоже не очень нравится вся эта затея, но нельзя же всех подводить."
                sug "Ты слушаешь себя, словно со стороны."
                sug "Еще бы пару дней назад тебе бы и в голову не пришло сказать подобное."
                show mz bukal glasses pioneer at center   with dspr
                "Женя удивленно смотрит на тебя."
                mz "Так что, все только меня ждут?"
                th "А я тебе о чем только что говорил?"
                sug "Она уже близка к принятию."
                me "Да."
                show mz angry glasses pioneer at center   with dspr
                mz "Все равно нет!"
                "Она хмурится и снова отворачивается."
                sug "Как так?"
                play sound ds_sfx_psy
                emp "Она явно боится как раз всех подвести."
                me "Но почему?"
                show mz shy glasses pioneer at center   with dspr
                mz "Я не умею играть в карты..."
                me "Ну и что?{w} Я тоже не знаю правил."
                show mz normal glasses pioneer at center   with dspr
                mz "Ну и как тогда играть?"
                me "А что, ты умеешь только то, о чем читала в книгах?"
                show mz bukal glasses pioneer at center   with dspr
                mz "Конечно."
                "Она удивленно смотрит на тебя."
                me "А если ты попадешь в Антарктиду и тебе придется охотиться на белых медведей?"
                show mz smile glasses pioneer at center   with dspr
                mz "Белые медведи не живут в Антарктиде."
                me "Ладно, это просто пример!"
                me "В конце концов, не на корову же играем."
                "Она задумывается и внимательно смотрит на тебя."
                show mz normal glasses pioneer at center   with dspr
                mz "Просто не хочу подводить ребят."
                emp "Что и требовалось доказать."
                window hide
                menu:
                    "Поддержать":
                        window show
                        me "Я понимаю тебя..."
                        show mz angry glasses pioneer at center with dspr
                        "Вот и хорошо!"
                    "Ответить с сарказмом":
                        window show
                        me "Да-да."
                        show mz angry glasses pioneer at center   with dspr
                        mz "И не подумай ничего такого!"
                emp "Ты даже и не знаешь, что она имела в виду."

                stop music fadeout 3

                stop ambience fadeout 2
                play sound ds_sfx_psy
                sug "У любого человека есть свои слабые места."
                window hide

                $ persistent.sprite_time = "sunset"
                scene bg int_dining_hall_sunset 
                with dissolve

                play ambience ambience_medium_crowd_indoors_1 fadein 3

                window show
                "Через минуту вы уже стоите в столовой."
                jump ds_day2_game
            else:
                window show
                $ ds_skill_points['suggestion'] += 1
                play sound ds_sfx_psy
                sug "Но ты даже не знаешь, с чего начать убеждать её."
                me "Cлушай... но тебе правда надо идти, все же ждут."
                show mz bukal glasses pioneer at center   with dspr
                "Женя удивленно смотрит на тебя."
                mz "Так что, все только меня ждут?"
                th "А я тебе о чем только что говорил?"
                me "Да."
                show mz angry glasses pioneer at center   with dspr
                mz "Все равно нет!"
                "Она хмурится и снова отворачивается."
                me "Но почему?"
                show mz shy glasses pioneer at center   with dspr
                mz "Да не хочу я, не умею, только подведу всех."
                mz "Не брала я эти ваши карты никогда в руки."
                mz "Короче, всё, не пойду я никуда, даже не уговаривай!"
                "Она встаёт и собирается уходить."
                window hide
                menu:
                    "Задержать":
                        if skillcheck('physical_instrument', lvl_medium):
                            window show
                            play sound ds_sfx_fys
                            phi "Но ты хватаешь её так крепко, что она вынуждена остановится."
                            $ ds_skill_points['physical_instrument'] += 1
                            me "Нет, ты пойдёшь со мной!"
                            show mz rage glasses pioneer close at center with dspr
                            mz "Да что ты ко мне прицепился?!"
                            show mz bukal glasses pioneer at center with dspr
                            mz "Ладно-ладно, пойду я, раз тебе это так надо! Но это будет на твоей совести!"
                            window hide

                            $ persistent.sprite_time = "sunset"
                            scene bg int_dining_hall_sunset 
                            with dissolve

                            play ambience ambience_medium_crowd_indoors_1 fadein 3

                            window show
                            "Через минуту вы уже стоите в столовой."
                            jump ds_day2_game
                        else:
                            window show
                            play sound ds_sfx_fys
                            phi "Но ей удаётся вырвать свою руку из твоей и убежать."
                            $ ds_skill_points['physical_instrument'] += 1
                            hide mz with dissolve
                            $ ds_bring_mz_fail = True
                            $ ds_attack_mz = True
                            "Ты остался один."
                            window hide

                            $ persistent.sprite_time = "sunset"
                            scene bg int_dining_hall_sunset 
                            with dissolve

                            play ambience ambience_medium_crowd_indoors_1 fadein 3

                            window show
                            "Делать нечего, тебе пришлось прийти в столовую с пустыми руками."
                            jump ds_day2_game
                    "Отпустить":
                        me "Ну и иди!"
                        show mz angry glasses pioneer far at center with dspr
                        mz "Ну и пойду!"
                        hide mz with dissolve
                        "Ты остался один."
                        window hide

                        $ persistent.sprite_time = "sunset"
                        scene bg int_dining_hall_sunset 
                        with dissolve

                        play ambience ambience_medium_crowd_indoors_1 fadein 3

                        window show
                        "Делать нечего, тебе пришлось прийти в столовую с пустыми руками."
                        $ ds_bring_mz_fail = True
                        jump ds_day2_game
        "Заставить":
            if skillcheck('authority', lvl_heroic):
                $ ds_skill_points['authority'] += 1
                window show
                play sound ds_sfx_psy
                aut "Пришло время показать ей, что она {i}обязана{/i} пойти на турнир."
                aut "Напирай на то, что она задерживает начало турнира."
                me "Cлушай, я всё понимаю, но ты должна пойти на турнир. Все тебя только и ждут."
                show mz angry glasses pioneer at center with dspr
                mz "Да что вы ко мне прицепились все?!"
                me "Потому что иначе ты как раз всех подведёшь, а ты же не хочешь этого?"
                me "Все ждут только тебя, без тебя турнир не состоится!"
                me "Зачем ты соглашалась участвовать, собственно?"
                show mz bukal glasses pioneer at center with dspr
                mz "Потому что так надо, типа коллективное времяпровождение..."
                aut "Все вполне ожидаемо: заставили. Как и тебя, по сути."
                me "И всё-таки все рассчитывают на тебя! От тебя не требуется победа, но участия - ждут!"
                window hide
                $ renpy.pause(1.0)
                window show
                show mz normal glasses pioneer at center with dspr
                mz "Ладно... схожу я на турнир, раз уж ты настаиваешь, что надо..."
                show mz bukal glasses pioneer at center with dspr
                mz "Но в случае чего виноват будешь ты!"
                window hide

                $ persistent.sprite_time = "sunset"
                scene bg int_dining_hall_sunset 
                with dissolve

                play ambience ambience_medium_crowd_indoors_1 fadein 3

                window show
                "Через минуту вы уже стоите в столовой."
                jump ds_day2_game
            else:
                $ ds_skill_points['authority'] += 1 
                window show
                play sound ds_sfx_psy
                aut "Ну, попробвать можно... но, скорее, ты её отпугнёшь окончательно."
                me "А ну пошла на турнир, достала уже!"
                show mz rage glasses pioneer at center with dspr
                mz "Всё, надоели вы все мне! Я ухожу!"
                hide mz with dissolve
                "И она так быстро убегает, что ты ничего не успеваешь сделать."
                th "Вот это дела..."
                window hide

                $ persistent.sprite_time = "sunset"
                scene bg int_dining_hall_sunset 
                with dissolve

                play ambience ambience_medium_crowd_indoors_1 fadein 3

                window show
                "Делать нечего, тебе пришлось прийти в столовую с пустыми руками."
                $ ds_bring_mz_fail = True
                jump ds_day2_game
        "Уйти без Жени":
            window show
            me "Ну и ладно, не хочешь - не надо!"
            show mz bukal glasses pioneer at center with dspr
            mz "Всё, я могу быть свободна?"
            me "Да!"
            "И ты уходишь."
            window hide

            $ persistent.sprite_time = "sunset"
            scene bg int_dining_hall_sunset 
            with dissolve

            play ambience ambience_medium_crowd_indoors_1 fadein 3

            window show
            "Через минуту ты уже в столовой - один."
            $ ds_bring_mz_fail = True
            jump ds_day2_game

label ds_day2_game:
    if ds_bring_mz_fail:
        show el upset pioneer at center with dissolve
        el "А где Женя?"
        me "А она не пришла! Ни в какую не согласилась прийти!"
        el "И что нам теперь делать?"
        show mt normal pioneer at right with dissolve
        mt "Что-что? Ну, сыграешь сам. А судить буду я!"
        show mt smile pioneer at right with dspr
        mt "Не переживай, я справлюсь!"
        el "Ладно..."
    show el normal pioneer at center   with dissolve
    "Все внимательно уставились на Электроника."
    el "Итак..."
    "Прокашлялся он."
    if ds_cards_damaged:
        mt "СЕМЁН!"
        play sound ds_sfx_mot
        res "Что это такое?!"
        show mt rage pioneer at right with dissolve
        mt "Ты испортил карты! Они все измазаны мелом!"
        mt "Ты что, хотел пометить карты, чтобы всех обыграть?!"
        window hide
        menu:
            "Признать":
                window show
                me "Да... Простите."
                mt "Это единственные карты на весь лагерь были!"
                show mt angry pioneer at right with dissolve
                mt "Ладно, как-нибудь почистим и поиграем!"
                mt "Но ты отстранён от участия в турнире! Иди прочь!"
            "Отпираться":
                window show
                me "Это не я!"
                mt "А кто же? Домовой? Пушкин?"
                $ ds_karma -= 10
                play sound ds_sfx_int
                dra "Увы, но тут вообще без вариантов придумать какую-то ложь."
                mt "В общем, всё, ты дисквалифицирован! Свободен!"
        "Тебе ничего не остаётся делать, кроме как с позором удалиться."
        $ ds_lp_sl -= 2
        $ ds_lp_dv -= 3
        $ ds_lp_un -= 1
        $ ds_lp_mi -= 1
        $ ds_lp_us -= 1
        $ ds_tour_result = -2
        $ ds_morale -= 1
        jump ds_day2_after_tour
    el "Каждый тур состоит из одной игры."
    el "Если будет ничья, то тогда исход решит дополнительная партия."
    el "После этого проигравший выбывает, и начинается следующий тур."
    el "Поскольку добровольцев..."
    "Он посмотрел на тебя."
    el "Поскольку участников – восемь, то и туров будет три."
    el "Все понятно?"
    "Толпа пионеров весело загалдела."
    show us laugh pioneer at left   with dissolve
    us "А призы какие, призы?"
    show sl angry pioneer at right   with dissolve
    sl "Ульяна, хватит!"
    "Вперёд выскакивает Славя, тщетно пытаясь поймать Ульянку."
    show us laugh pioneer at right 
    show sl angry pioneer at left 
    with dissolve
    us "Пока не выиграю приз, не успокоюсь!"
    play sound ds_sfx_psy
    ine "Кажется, одной этой девочки достаточно для варп-прыжка к Альфе Центавра."
    show us laugh pioneer at left 
    show sl angry pioneer at right 
    with dissolve
    us "Призы-призы!"
    sl "Прекрати."
    show el shocked pioneer at center   with dspr
    play sound ds_sfx_psy
    emp "А у Электроника, похоже, от всей этой беготни вокруг него уже закружилась голова."
    show us laugh pioneer at right 
    show sl angry pioneer at left 
    with dissolve
    me "Давайте начинать."
    if skillcheck('suggestion', lvl_easy):
        play sound ds_sfx_psy
        sug "И обращаешься к Ульяне."
        me "А то никаких призов не получишь."
        sug "Такой аргумент, похоже, подействовал, так как она возвращается на свое место."
        hide us  with dissolve
        show sl smile pioneer at left   with dspr
        "За ней следует и Славя, бросив тебе на прощание улыбку благодарности."
        hide sl  with dissolve
    else:
        hide us with dissolve
        hide sl with dissolve
    show el normal pioneer at center   with dspr
    "Пионеры наконец угомонились."
    hide el  with dissolve
    # TODO: написать турнир
    window hide
    menu:
        "Желаемый результат турнира (ОТЛАДКА!)"
        "Проиграл в первой игре":
            $ ds_tour_result = 0
        "Проиграл в полуфинале":
            $ ds_tour_result = 1
        "Проиграл в финале":
            $ ds_tour_result = 2
        "Выиграл турнир":
            $ ds_tour_result = 3
            if ds_bet_dv:
                $ ds_lp_dv += 1
        "Дисквалифицировали" if ds_cards_labeled:
            jump ds_day2_disqual
    menu:
        "C кем играл четвертьфинал?"
        "С Алисой":
            if ds_tour_result > 0:
                $ ds_lp_dv += 1
        "C Леной":
            if ds_tour_result == 0:
                $ ds_lp_un += 1
            if not ds_bet_dv:
                $ ds_lp_sl += 1
        "Cо Славей":
            if ds_tour_result == 0:
                $ ds_lp_sl += 1
            if not ds_bet_dv:
                $ ds_lp_sl += 1
        "С Ульяной":
            if ds_tour_result == 0:
                $ ds_lp_us += 1
            if not ds_bet_dv:
                $ ds_lp_sl += 1
        "C Мику":
            if ds_tour_result == 0:
                $ ds_lp_mi += 1
            if not ds_bet_dv:
                $ ds_lp_sl += 1
        "C Женей":
            if not ds_bet_dv:
                $ ds_lp_sl += 1
        "С Шуриком":
            pass
    if ds_tour_result > 0:
        menu:
            "C кем играл полуфинал?"
            "С Алисой":
                if ds_tour_result > 1:
                    $ ds_lp_dv += 1
            "C Леной":
                if ds_tour_result == 1:
                    $ ds_lp_un += 1
                if not ds_bet_dv:
                    $ ds_lp_sl += 1
            "Cо Славей":
                if ds_tour_result == 1:
                    $ ds_lp_sl += 1
                if not ds_bet_dv:
                    $ ds_lp_sl += 1
            "С Ульяной":
                if ds_tour_result == 1:
                    $ ds_lp_us += 1
                if not ds_bet_dv:
                    $ ds_lp_sl += 1
            "C Мику":
                if ds_tour_result == 1:
                    $ ds_lp_mi += 1
                if not ds_bet_dv:
                    $ ds_lp_sl += 1
            "C Женей":
                if not ds_bet_dv:
                    $ ds_lp_sl += 1
            "С Шуриком":
                pass
    if ds_tour_result > 1:
        menu:
            "C кем играл финал?"
            "С Алисой":
                if ds_tour_result > 2:
                    $ ds_lp_dv += 1
            "C Леной":
                if ds_tour_result == 2:
                    $ ds_lp_un += 1
                if not ds_bet_dv:
                    $ ds_lp_sl += 1
            "Cо Славей":
                if ds_tour_result == 2:
                    $ ds_lp_sl += 1
                if not ds_bet_dv:
                    $ ds_lp_sl += 1
            "С Ульяной":
                if ds_tour_result == 2:
                    $ ds_lp_us += 1
                if not ds_bet_dv:
                    $ ds_lp_sl += 1
            "C Мику":
                if ds_tour_result == 2:
                    $ ds_lp_mi += 1
                if not ds_bet_dv:
                    $ ds_lp_sl += 1
            "C Женей":
                if not ds_bet_dv:
                    $ ds_lp_sl += 1
            "С Шуриком":
                pass
    window show
    "Ты выходишь из столовой."
    play sound ds_sfx_fys
    edr "Спать ложиться ещё рано, так что небольшая прогулка кажется отличным вариантом."
    th "Куда же направиться?"
    th "А может, всё-таки просто спать пойти?"
    jump ds_day2_after_tour

label ds_day2_after_tour:
    window hide

    stop ambience fadeout 3

    $ persistent.sprite_time = 'night'
    $ night_time()

    $ disable_all_zones_ds_small()
    $ set_zone_ds_small("medic_house", "ds_day2_medic")
    $ set_zone_ds_small("square","ds_day2_square")
    $ set_zone_ds_small("beach","ds_day2_beach")
    $ set_zone_ds_small("boathouse","day2_dock_eve")
    $ set_zone_ds_small("entrance", "ds_day2_entrance")
    $ set_zone_ds_small("scene","ds_day2_scene")
    $ set_zone_ds_small("sport_area","ds_day2_badminton")
    $ set_zone_ds_small("library", "ds_day2_library")
    $ set_zone_ds_small("house_me_mt", "ds_day2_night")
    $ show_small_map_ds()

label ds_day2_medic:
    scene bg ext_aidpost_night
    with dissolve
    window show
    if (ds_health == ds_skill_points['endurance']) and not ds_cs_invite:
        "Ты просто шёл куда-то и вышел к медпункту."
        play sound ds_sfx_fys
        edr "Тебе тут делать нечего - со здоровьем у тебя всё в порядке."
        $ disable_current_zone_ds_small()
        jump ds_day2_after_tour
    if ds_cs_invite:
        play sound ds_sfx_fys
        ins "Ну вот ты и пришёл к медсестре."
        ins "Она уже ждёт - нет, жаждет тебя."
    if ds_health < ds_skill_points['endurance']:
        play sound ds_sfx_fys
        edr "Ты чувствуешь себя плоховато, так что медпункт - то, что надо!"
    scene bg int_aidpost_night
    with dissolve
    show cs normal far at center with dissolve
    "Ты заходишь в медпункт."
    ins "Виола уже определённо ждёт тебя."
    cs "Ну привет... пионер."
    cs "Так скоро ко мне вернулся."
    show cs shy far at center with dissolve
    cs "Что, понравилась я тебе?"
    window hide
    menu:
        "Согласиться":
            me "Да, есть такое... Вы такая чудесная женщина!"
        "Сослаться на здоровье" if ds_health < ds_skill_points['endurance']:
            me "Да мне просто бы провериться... чувствую себя не очень."
            cs "Между прочим, я знаю отличное средство от всех невзгод!"
        "Возразить":
            me "Честно говоря, не особо. Мне другие девушки по вкусу."
            cs "Ну так мы это можем исправить..."
    show cs smile at center with dspr
    cs "Кстати, можешь обращаться на «ты»."
    cs "Ну что, займёмся {i}лечением{/i}?"
    window hide
    menu:
        "Продолжать":
            if skillcheck('instinct', lvl_medium):
                play sound ds_sfx_fys
                ins "Она явно намекает тебе на то, что хочет тебя."
                ins "Более того, ты тоже - во всяком случае, внизу у тебя радости полные штаны."
                me "Да... давайте..."
                $ ds_skill_points['instinct'] += 1
            else:
                play sound ds_sfx_fys
                ins "Ты не понимаешь, к чему она произнесла «лечение» с такой интонацией."
                $ ds_skill_points['instinct'] += 1
                me "Ну, давайте, у меня голова побаливает."
                show cs normal at center with dspr
                cs "Так, ладно. Сейчас выдам тебе таблетки."
                "Она отдаёт тебе таблетки, и ты собираешься уходить."
                cs "Если что, приходи обязательно, пионер. Буду ждать тебя..."
                ins "Ты всё ещё в непонимании, чего она от тебя хочет."
                me "Спасибо, до свидания."
                scene bg ext_aidpost_night
                with dissolve
                jump ds_day2_night
        "Остановить":
            me "Нет, со мной всё в порядке."
            cs "Ну как же, а если проверить."
            me "Нет, со мной всё абсолютно точно в порядке!"
            "Ты выходишь из медпункта, бросая лишь пару слов."
            me "Спасибо за помощь!"
            scene bg ext_aidpost_night
            with dissolve
            jump ds_day2_night

label ds_day2_square:
    scene bg ext_square_night
    with dissolve
    window show
    "Ты выходишь на площадь и садишься на скамейку."
    th "Эх, хорошо памятнику - стоит себе, его никто не трогает..."
    play sound ds_sfx_psy
    ine "А ещё видит всё происходящее в лагере!"
    ine "Кстати, может, попробовать {i}поговорить{/i} с ним?"
    window hide
    menu:
        "Поговорить с Гендой":
            window show
            th "А что, можно попробовать..."
            window hide
            if skillcheck('inland_empire', lvl_impossible):
                window show
                $ ds_skill_points['inland_empire'] += 1
                ine "Давай!"
                me "Генда?"
            else:
                window show
                ine "Нет, ты не можешь заставить памятник заговорить."
                $ ds_skill_points['inland_empire'] += 1
                th "И в чём смысл просто таращиться на памятник?"
                "Ты встаёшь со скамейки."
                $ disable_current_zone_ds_small()
                jump ds_day2_after_tour
        "Не заговаривать":
            window show
            th "Да не, бред какой-то."
            th "И вообще, в чём смысл просто таращиться на памятник?"
            "Ты встаёшь со скамейки и уходишь."
            $ disable_current_zone_ds_small()
            jump ds_day2_after_tour
    gn "Семён..."
    play sound ds_sfx_mot
    res "Вот это поворот! Он и правда заговорил!"
    ine "Не теряйся, продолжай."
    me "Здравствуйте..."
    gn "Здравствуй, Семён. Приятно познакомиться."
    gn "Жаль, не могу пожать руку, да и вообще пошевелиться..."
    gn "Думаю, ты и так знаешь, что меня звать Гендой."
    me "Да... а ты кто?"
    gn "Вообще я генеральный секретарь Коммунистической партии Советского Союза!"
    play sound ds_sfx_int
    enc "Так, стоп, а Горбачёва куда девали?"
    ine "Ну, никто и не обещал, что это такой же СССР, как у нас."
    window hide
    menu:
        "Спросить":
            window show
            me "А как же Горбачёв?"
            gn "А, тот изменник и приспешник американских империалистов?"
            gn "Так его лет десять назад раскрыли и расстреляли!"
            gn "А почему тебя он так интересует... так, подожди?"
            play sound ds_sfx_fys
            hfl "Он что, теперь держит нас за сообщника?"
            hfl "Впрочем, это же памятник! Он ничего не сделает... наверное."
        "Не спрашивать":
            window show
            gn "А как ты можешь этого не знать?"
    gn "А, да, я забыл."
    gn "Ты же из альтернативной реальности."
    play sound ds_sfx_psy
    aut "Чего это сразу альтернативной? Это {i}его{/i} реальность альтернативная!"
    play sound ds_sfx_int
    rhe "Не стоит этого озвучивать - для него как раз твоя реальность альтернативная, всё верно."
    me "Ну... да..."
    window hide
    menu:
        "Спросить о мире":
            window show
            me "А что это за лагерь? И что за мир?"
            gn "Какие интересные вопросы ты задаёшь..."
            gn "Ну... это пионерлагерь. Неожиданно, правда?"
            gn "А мы в нерушимом Советском Союзе!"
            play sound ds_sfx_int
            lgc "Кстати, вполне возможно, что тут Союз просуществует и до наших времён, с другим-то правителем."
            me "Нет, вы меня не поняли."
        "Спросить о цели":
            window show
        "Завершить разговор":
            window show
            me "Ладно, я пойду."
            me "До свидания!"
            "С этими словами ты уходишь с площади."
            jump ds_day2_night
    me "Для чего этот мир? Почему я попал в него?"
    gn "Узнаешь... пока не время..."
    play sound ds_sfx_fys
    edr "Тут ты чувствуешь, как у тебя начинает кружиться голова."
    edr "Ты пытаешься противостоять этому, но безуспешно."
    show blink
    edr "Ты откидываешься на скамейку и падаешь в обморок..."
    window hide
    scene black
    play music ds_dream fadein 3
    $ renpy.pause(1.0)
    window show
    arb "Что, уже вернулся?"
    arb "В небытие всё-таки лучше?"
    lim "Пытаешься выяснить, почему ты тут? Зачем ты нужен?"
    lim "А для чего всё это?"
    window hide
    menu:
        "Чтобы выбраться":
            window show
            me "Я хоче вернуться в свой мир."
            arb "Ой ли..."
            arb "Туда, где ты ничтожество, ты хочешь вернуться?"
        "Чтобы наладить отношения":
            window show
            me "Я отношения тут налаживаю!"
            arb "С Алисой? А ты уверен, что она тебя {i}такого{/i} захочет?"
            arb "С Леной? Да она тебя боится!"
            arb "Со Славей? Она слишком правильная для такого раздолбая как ты!"
            arb "С Ульяной? Она ещё ребёнок, и то ей будет неинтересно с тобой!"
            arb "С Мику? Да ты песчинка по сравнению с ней-горой: она столько умеет, а ты - ни-че-го!"
            arb "С Электроником? Да даже парень на тебя не обратит внимания!"
            arb "С вожатой... ну, интересный выбор... но не думаю, что её заинтересует какой-то пионер!"
            arb "С Женей? Да её в принципе мужики не интересуют, как ты этого не понимаешь?"
            arb "Тебе разве что Генда остаётся!"
        "Чтобы развлечься":
            window show
            me "Тут весело! Закачаешься!"
            arb "Именно поэтому ты постоянно думаешь не то о девушках, не то о побеге?"
            arb "Не отрицай: ты не веселиться сюда попал. Ты уже {i}не можешь{/i} веселиться."
        "Непонятно":
            window show
            me "Да мне бы самому понять!"
        "Послать всё к чёрту":
            window show
            me "Да пошло оно всё! Я остаюсь тут!"
    lim "Вспомни {i}ту самую{/i}..."
    me "Кого?"
    lim "Твою любовь всей жизни."
    arb "Что, уже забыл всё? Впрочем, оно и правильно..."
    window hide
    menu:
        "Согласиться":
            window show
            me "И правда: мне это не надо!"
            lim "Но ты не можешь выбросить из головы мысли об этом."
        "Выяснить":
            window show
            me "Нет, скажи мне, про кого это ты?"
            lim "Про то, что называется «отношения»..."
            lim "Про эмоции, захлёстывавшие тебя, пока в твоей жизни была {i}она{/i}."
            lim "И про ещё большие эмоции, когда {i}она{/i} тебя оставила."
            me "Как грустно..."
            lim "Да, грустно."
            play sound ds_sfx_psy
            vol "Так, нет, лучше пока что об этом не вспоминай."
    arb "Хотя, возможно, не всё ещё потеряно?"
    lim "Может, ты ещё сможешь вернуть себе любовь?"
    lim "Вернуть утерянные нежность, тепло, ласку?"
    lim "Ну нет, ты уже очень давно поставил на себе крест..."
    arb "А может, не стоит и выбираться? Тебе же так комфортно тут!"
    arb "Ни боли. Ни страданий."
    window hide
    $ ds_knowing += 1
    $ renpy.pause(0.5)
    window show
    dvv "Семён! А ну просыпайся!"
    play sound ds_sfx_psy
    vol "Тебя зовёт какой-то голос. {i}Женский{/i} голос."
    play sound ds_sfx_psy
    emp "И этому голосу ты небезразличен."
    stop music fadeout 5
    hide blink
    show unblink
    scene bg ext_square_night
    show dv scared pioneer close at center with dissolve
    play sound ds_sfx_mot
    per_eye "Тебя встречает испуганное лицо... {w}Алисы."
    play sound ds_sfx_mot
    res "Алиса?!"
    me "Алиса?.."
    show dv angry pioneer at center with dspr
    dv "Нет, Славя!"
    dv "Ты чего пугаешь так?! Ты выглядел как мёртвый!"
    if (ds_tour_result >= 0) and (ds_tour_result < 3):
        dv "Я, конечно, понимаю, что ты турнир продул, но не в обморок теперь падать же!"
    elif ds_tour_result == -2:
        dv "Дисквалификация - это обидно, конечно, но ты сам виноват, и нечего в обморок падать!"
    elif ds_tour_result == 3:
        dv "Ты вообще-то победил в турнире, а не проиграл. Или настолько перенапрягся для победы?!"
    dv "Как ты себя чувствуешь, в общем?"
    me "Уже лучше..."
    window hide
    menu:
        "Поблагодарить":
            window show
            me "Спасибо..."
            show dv grin pioneer at center with dspr
            dv "Ты мне должен будешь!"
            if ds_beat_dv or ds_betray_dv:
                dv "Причём, {i}очень{/i} много должен."
        "Усомниться":
            window show
            me "Тебя я увидеть не ожидал..."
            show dv rage pioneer at center with dspr
            dv "Что, вообще меня за бессердечную держишь?!"
            $ ds_lp_dv -= 1
            dv "Не поверишь, но у меня тоже есть эта... как её..."
            me "Эмпатия?"
            dv "А ты не подсказывай, сама догадаюсь!"
            show dv angry pioneer at center with dspr
            dv "В общем, есть она у меня!"
            if ds_beat_dv or ds_betray_dv:
                dv "Даже к таким, как ты!"
        "Спросить причину":
            window show
            me "Но почему ты обратила на меня внимание?"
            dv "Потому что мне, совершенно внезапно, на других не плевать!"
            if ds_beat_dv or ds_betray_dv:
                dv "Даже если эти другие сильно меня обидели ранее!"
        "Промолчать":
            window show
    show dv normal pioneer at center with dspr
    dv "Так, всё, а теперь иди к себе!"
    dv "И нет, я тебя не отведу!"
    show dv laugh pioneer at center with dspr
    dv "Ты уже взрослый мужик, сам доберёшься!"
    dv "Бывай!"
    hide dv with dissolve
    res "Ты не успел даже попрощаться."
    jump ds_day2_night

label ds_day2_dock_eve:
    $ persistent.sprite_time = "night"
    scene bg ext_boathouse_night 
    with dissolve

    play ambience ambience_boat_station_night fadein 2

    window show
    "Ты пошёл на пристань."
    play sound ds_sfx_int
    con "Солнце еще не полностью скрылось за горизонтом, и река вдалеке красиво окрашивается во все оттенки красного, желтого и оранжевого."
    con "Кажется, что вода там горит ярким пламенем, но чем дольше ты стоишь, тем пожар становится меньше и в конце концов совсем потух."
    $ ds_skill_points['conceptualization'] += 1
    if not ds_find_hairpin:
        play sound ds_sfx_psy
        vol "Тебе тут больше делать нечего. Иди домой."
        "Ты встаёшь и уходишь."
        stop ambience fadeout 2
        jump ds_day2_night
    th "Меня ещё Мику просила найти заколку..."
    window hide
    menu:
        "Поискать":
            window show
            play sound ds_sfx_mot
            per_eye "Ты приглядываешься к песку на причале."
            window hide
            if skillcheck('perception', lvl_challenging):
                window show
                per_eye "И вот в одном из последних лучей солнца что-то блестит!"
                "Ты подходишь к подмеченному месту и видишь ту самую заколку!"
                $ ds_skill_points['perception'] += 1
                $ ds_mi_hairpin = True
            else:
                window show
                per_eye "Но ты ничего разглядеть не можешь: совсем стемнело."
                per_eye "И вообще не факт, что заколка тут!"
                "Ты уходишь несолоно хлебавши."
                $ ds_skill_points['perception'] += 1
                stop ambience fadeout 2
                jump ds_day2_night
        "Забить":
            window show
            th "Вот мне заняться нечем, кроме как рыться в песке!"
            "С этими мыслями ты уходишь к себе домой."
            stop ambience fadeout 2
            jump ds_day2_night
    $ ds_mi_hairpin = True
    th "Итак, и что мне теперь делать с заколкой?"
    window hide
    menu:
        "Отнести Мику":
            window show
            lgc "Итак, заколку можно отнести в домик или в музклуб..."
            th "Куда пойти?"
        "Оставить у себя":
            window show
            th "Лучше оставлю у себя. Отдам Мику попозже."
            th "Вcё равно сейчас я её не найду!"
            stop ambience fadeout 2
            jump ds_day2_night
    stop ambience fadeout 2
    jump ds_day2_find_mi_house

label ds_day2_find_mi_house:
    window hide
    $ disable_all_zones_ds_small()
    $ set_zone_ds_small('house_el_sh', 'ds_day2_house3')
    $ set_zone_ds_small('house_sl_mz', 'ds_day2_house12')
    $ set_zone_ds_small('house_un_mi', 'ds_day2_house13')
    $ set_zone_ds_small('house_me_mt', 'ds_day2_house17')
    $ set_zone_ds_small('house_dv_us', 'ds_day2_house23')
    $ set_zone_ds_small('music_club', 'ds_day2_music')
    $ show_small_map_ds()

label ds_day2_music:
    window show
    "Ты направляешься в музклуб."
    $ renpy.pause(1.0)
    scene bg ext_square_night with dissolve
    $ renpy.pause(1.5)
    scene bg ds_ext_musclub_night with dissolve
    "Ты подходишь к музклубу."
    per_eye "Но тут никого нет."
    play sound ds_sfx_psy
    lgc "Значит, нужно искать домик..."
    stop ambience fadeout 2
    $ disable_current_zone_ds_small()
    jump ds_day2_find_mi

label ds_day2_house3:
    $ persistent.sprite_time = "night"
    scene bg ds_ext_el_house_night
    with dissolve
    "Ты подходишь к домику номер 3."
    window hide
    menu:
        "Зайти без стука":
            window show
            play sound sfx_open_door_1
            # TODO: CG: "борьба" Электроника с Шуриком
            play sound ds_sfx_mot
            res "Вот это номер..."
            window hide
            $ renpy.pause(2.0)
            me "Кхем!"
            scene bg ds_int_el_house_night with dissolve
            show el scared naked far at left with dissolve
            show sh upset pioneer far at right with dissolve
            el "А ты что тут делаешь?"
            me "Эм... ищу Мику..."
            sh "Мику тут нет."
            play sound ds_sfx_int
            vic "Ты это и так уже понял."
            me "Тогда не буду вам мешать в ваших... развлечениях."
            play sound sfx_open_door_1
            "С этими словами ты выходишь."
            scene bg ds_ext_el_house_night
            with dissolve
            play sound ds_sfx_fys
            ins "Может, тебе стоило присоединиться к ним?"
            ins "Может, тебя на самом деле привлекают мужчины? Подумай над этим!"   
        "Постучаться":
            window show
            play sound sfx_knocking_door_2
            el "Подождите!"
            $ renpy.pause(2.0)
            play sound sfx_open_door_1
            show el normal pioneer at center with dissolve
            el "О, Семён! А что ты тут делаешь?"
            me "Мику ищу..."
            show el serious pioneer at center with dspr
            el "Мику тут нет. Где она живёт - я не знаю..."
            el "Ну, найдёшь, думаю."
            sh "Ты где, Эл?"
            el "Уже иду!"
            el "Спокойной ночи!"
            play sound sfx_open_door_1
            hide el with dissolve
    play sound ds_sfx_int
    lgc "Итак, Мику тут нет."
    th "Идти дальше?"
    window hide
    menu:
        "Идти сейчас":
            window show
            th "Нужно отдать сегодня!"
            $ disable_current_zone_ds_small()
            jump ds_day2_find_mi_house
        "Отложить до завтра":
            window show
            th "Нет, лучше до завтра подожду..."
            jump ds_day2_night

label ds_day2_house12:
    $ persistent.sprite_time = "night"
    scene bg ds_ext_sl_house_night
    with dissolve
    "А вот и домик 12."
    if ds_cards_sl:
        play sound ds_sfx_int
        enc "Это же домик Слави!"
        enc "Мику тут точно нет, тут Женя живёт."
        $ ds_skill_points['encyclopedia'] += 1
        $ disable_current_zone_ds_small()
        jump ds_day2_find_mi_house
    th "Итак, попробуем удачу тут..."
    window hide
    menu:
        "Зайти без стука":
            window show
            play sound sfx_knock_door6_closed
            "Ты пытаешься открыть дверь, но она заперта."
            window hide
            menu:
                "Постучать":
                    window show
                    play sound sfx_knocking_door_2
                    "Ты стучишь в дверь."
                "Вломиться в домик":
                    if skillcheck('physical_instrument', lvl_challenging):
                        play sound sfx_break_cupboard
                        $ renpy.pause(0.5)
                        window show
                        play sound ds_sfx_fys
                        phi "Дверь тут не сильно прочная, так что ты с лёгкостью её выламываешь и попадаешь в домик."
                        window hide
                        scene bg ds_int_sl_house_night
                        with dissolve
                        with vpunch
                        $ ds_sl_door_broken = True
                        $ ds_karma -= 30
                        window show
                        "Все обитатели уже проснулись и буквально таращатся на тебя."
                    else:
                        play sound sfx_knock_door6_closed
                        $ renpy.pause(0.5)
                        window show
                        play sound ds_sfx_fys
                        phi "Ты толкаешь дверь, но она не поддаётся."
                        phi "Всё, что ты сделал - это разбудил обитателей."
                    $ ds_skill_points['physical_instrument'] += 1
                "Уйти":
                    window show
                    play sound ds_sfx_psy
                    vol "Лучше не лезть дальше."
                    "И ты уходишь."
                    $ disable_current_zone_ds_small()
                    jump ds_day2_find_mi
        "Постучать":
            window show
            play sound sfx_knocking_door_2
            "Ты стучишь в дверь."
    if ds_sl_door_broken:
        scene bg ds_int_sl_house_night_light
        with dissolve
        show sl surprise naked far at right with dissolve
        show mz rage pioneer far at left with dissolve
        mz "Что тут происходит?! Почему посреди ночи к нам в дом вламываются какие-то парни?!"
        sl "Cемён?"
        play sound ds_sfx_psy
        emp "Они, мягко говоря, удивлены таким поворотом событий."
        show sl angry naked at right with dspr
        sl "И зачем ты выломал нам дверь?"
        $ ds_lp_sl -= 1
        window hide
        menu:
            "Нужно найти Мику":
                window show
                me "Мне нужна была Мику..."
                mz "Нет тут твоей Мику!"
                show sl serious naked at right with dspr
                sl "Да, она живёт в тринадцатом домике."
                me "Спасибо..."
            "В гости зайти":
                window show
                me "Да просто захотел к вам зайти..."
                mz "Прекрасно! Мы тебя не звали вообще-то!"
                mz "К тому же, мы вообще спали, пока ты не занялся разрушением социалистической собственности!"
                mz "Короче, иди уже прочь!"
                show sl serious naked at right with dspr
                sl "Да, тебе пора..."
                me "А может подскажете, где живёт Мику тогда?"
                sl "В домике 13, не 12!"
                me "Cпасибо, я пойду..."
            "Извиниться":
                window show
                me "Извините..."
                mz "Дверь от твоего «извините» не починится!"
                mz "Короче, иди уже прочь!"
                show sl serious naked at right with dspr
                sl "Да, тебе пора..."
                me "А может подскажете, где живёт Мику?"
                sl "В домике 13, не 12!"
                me "Cпасибо, я пойду..."
        mz "CТОЯТЬ!"
        play sound ds_sfx_psy
        aut "Она сказала это таким голосом, что ты не смог ослушаться."
        mz "А дверь-то кто чинить будет?!"
        show sl normal naked far at right with dspr
        sl "Успокойся, Жень, Семён нам завтра её и починит."
        show mz angry pioneer far at left with dissolve
        sl "Да, Семён?"
        window hide
        menu:
            "Принять":
                window show
                me "Да, починю..."
            "Возразить":
                window show
                aut "Ещё чего, командовать тобой будут!"
                me "Ничего я чинить не буду!"
                $ ds_lp_sl -= 1
                $ ds_karma -= 10
                show sl angry naked far at right with dspr
                sl "Значит, вожатая тебя убедит, раз не хочешь по-хорошему..."
        sl "В общем, спокойной ночи и иди отсюда!"
        mz "Да, и чтобы мы тут тебя больше не видели!"
        me "Cпокойной ночи..."
        "И ты уходишь."
        scene bg ds_ext_sl_house_night
        with dissolve
        play sound ds_sfx_psy
        vol "Нажил ты себе неприятностей, конечно..."
        play sound ds_sfx_fys
        ins "За всем этим обсуждением ты пропустил, что Славя всё это время была голой!"
        th "Так, мне надо уходить поскорее..."
    else:
        $ renpy.pause(0.5)
        show sl surprise naked far at center with dissolve
        play sound ds_sfx_fys
        ins "Вот это тебе повезло... Перед тобой вживую стоит голая женщина!"
        th "Охренеть..."
        sl "Ты чего?"
        window hide
        menu:
            "Начать домогаться":
                if skillcheck('instinct', lvl_trivial):
                    window show
                    ins "Вперёд, на покорение этой цели!"
                    me "Прекрасная фигура, мне так нравится. Я бы тебя того..."
                    show sl shy naked at center with dspr
                    sl "Приятно слышать, конечно... но ты же не за этим пришёл?"
                    me "А как же, именно что за этим!"
                    show sl tender naked at center with dspr
                    sl "Ну хватит, мне стыдно слышать все эти комплименты!"
                    $ ds_lp_sl += 1
                    play sound ds_sfx_mot
                    res "А, то есть голой стоять ей не стыдно."
                    show sl serious naked at center with dspr
                    sl "Ты кого-то потерял?"
                else:
                    window show
                    ins "На таком идеальном моменте ты умудрился перенервничать!"
                    ins "Тебе ничего не приходит в голову."
                $ ds_skill_points['instinct'] += 1
            "Спросить про наготу":
                window show
                me "А тебе как... вот так вот выходить..."
                play sound ds_sfx_mot
                com "Тебе с трудом удаётся выговаривать слова, настолько ты перевозбуждён от открывшейся картины."
                show sl smile naked at center with dspr
                sl "Да нормально"
                sl "Я же говорила, что люблю природу и стремлюсь быть ближе к ней."
                play sound ds_sfx_fys
                edr "Да уж, ближе некуда!"
                show sl serious naked at center with dspr
                sl "Так ты чего пришёл?"
            "Спросить про Мику":
                window show
                show sl normal naked at center with dspr
            "Подарить заколку":
                window show
                me "Это тебе!"
                "C этими словами ты достаёшь заколку и вручаешь её Славе."
                show sl shy naked at center with dspr
                sl "Ой, спасибо, мне так приятно..."
                $ ds_lp_sl += 1
                $ ds_karma -= 10
                show sl surprise naked at center with dspr
                sl "Только почему так поздно?"
                window hide
                menu:
                    "Соврать":
                        window show
                        play sound ds_sfx_psy
                        sug "Ты вёз эту заколку специально для неё! Скажи так, в смысле."
                        me "Да я как раз вёз эту заколку, чтобы отдать понравившейся девушке."
                        me "И этой девушкой оказалась ты!"
                        show sl shy naked at center with dspr
                        sl "Ой, как мило!"
                        $ ds_gave_hairpin_sl = True
                        $ ds_mi_hairpin = False
                        sl "Cпокойной ночи!"
                        me "Cпокойной ночи..."
                        hide sl with dissolve
                        "Ты направляешься к себе."
                        jump ds_day2_night
                    "Признаться":
                        window hide
                        me "Ну, я нашёл заколку и решил отдать её тебе."
                        show sl serious naked at center with dspr
                        sl "Нет, так нельзя. Нужно отдать эту заколку!"
                        $ ds_lp_sl -= 1
                        $ ds_karma += 5
                        sl "Сам отнесёшь или мне поискать владелицу?"
                        window hide
                        menu:
                            "Отнести самому":
                                window show
                                me "Да сам отнесу..."
                                show sl normal naked at center with dspr
                                sl "Хорошо! Только отнеси обязательно!"
                                sl "Cпокойной ночи!"
                                me "Cпокойной ночи..."
                                hide sl with dissolve
                                play sound ds_sfx_psy
                                sug "Не получилось... можем попробовать с кем-нибудь другим."
                                sug "Или же отложить на завтра."
                                window hide
                                menu:
                                    "Идти сейчас":
                                        window show
                                        th "Нужно отдать сегодня!"
                                        $ disable_current_zone_ds_small()
                                        jump ds_day2_find_mi_house
                                    "Отложить до завтра":
                                        window show
                                        th "Нет, лучше до завтра подожду..."
                                        jump ds_day2_night
                            "Оставить Славе":
                                window show
                                me "Отнеси лучше ты... ты же знаешь тут всех."
                                show sl normal naked at center with dspr
                                sl "Ладно."
                                $ ds_mi_hairpin = False
                                sl "Cпокойной ночи!"
                                me "Cпокойной ночи..."
                                hide sl with dissolve
                                "Ты направляешься к себе."
                                jump ds_day2_night
            "Уйти":
                window show
                me "Эм... извини, я ошибся..."
                show sl normal naked far at center with dspr
                sl "А, ну ладно. Спокойной ночи!"
                play sound sfx_close_door_campus_1
                hide sl with dissolve
                th "Что это было?"
                ins "Бездарно пропущенный шанс это был!"
                th "Ладно, пойдём дальше..."
                $ disable_current_zone_ds_small()
                jump ds_day2_find_mi_house
        me "Слушай, а Мику не здесь живёт?"
        show sl normal naked at center with dspr
        sl "Ты ошибся ровно на один! Мику живёт не в двенадцатом, а в тринадцатом домике!"
        me "Cпасибо большое!"
        show sl smile naked at center with dspr
        sl "Да не за что!"
        sl "Спокойной ночи!"
        me "Спокойной..."
        play sound sfx_close_door_campus_1
        hide sl with dissolve
    play sound ds_sfx_int
    lgc "Итак, теперь мы можем пойти прямо к Мику!"
    lgc "Или же отложить на завтра."
    window hide
    menu:
        "Идти сейчас":
            window show
            th "Нужно отдать сегодня!"
            jump ds_day2_house13
        "Отложить до завтра":
            window show
            th "Нет, лучше до завтра подожду..."
            jump ds_day2_night

label ds_day2_house17:
    $ persistent.sprite_time = "night"
    scene bg ext_house_of_mt_night
    with dissolve

    "Ты подходишь к своему домику."
    play sound ds_sfx_int
    rhe "Попробуй выяснить у вожатой, она должна знать, где Мику."

    play sound sfx_open_door_1

    scene bg int_house_of_mt_night
    with dissolve
    show mt normal night far at center with dissolve

    "Ты открываешь дверь и заходишь."
    show mt normal night at center with dissolve
    mt "Cемён, привет, а где ты так задержался?"
    window hide
    menu:
        "Искал Мику":
            window show
            me "Мику ищу... кстати, вы не знаете, где она?"
            show mt normal night at center with dissolve
            mt "Она живёт в домике 13."
            mt "Только лучше уже завтра к ней пойти."
            window hide
            menu:
                "Согласиться":
                    me "Ладно, вы правы..."
                    jump ds_day2_sleep
                "Настоять на походе сегодня":
                    if skillcheck('suggestion', lvl_formidable):
                        window show
                        play sound ds_sfx_psy
                        sug "Вспомни о столь любимых ею обязанностях пионера."
                        me "Между прочим, я ей обещал сегодня отдать."
                        me "Разве это не обязанность пионера - выполнять данное слово?"
                        show mt surprise night at center with dissolve
                        mt "И то верно... ладно, иди."
                        mt "Но чтоб вернулся до полуночи!"
                        scene bg ext_house_of_mt_night
                        with dissolve
                        "Ты выходишь из домика."
                        $ ds_skill_points['suggestion'] += 1
                        $ disable_current_zone_ds_small()
                        jump ds_day2_find_mi
                    else:
                        window show
                        play sound ds_sfx_psy
                        sug "Но тебе надо пойти!"
                        me "Извините, но мне правда нужно идти!"
                        mt "Завтра, всё завтра..."
                        "Ты вынужден отложить заколку Мику на завтра."
                        $ ds_skill_points['suggestion'] += 1
                        jump ds_day2_sleep
        "Гулял":
            window show
            me "Да просто прогуляться."
            show mt smile night at center with dissolve
            mt "Это хорошо."
            mt "Но уже пора спать!"
        "Нагрубить":
            window show
            me "Не ваше это дело!"
            show mt angry night at center with dissolve
            mt "Ты чего это грубишь мне?!"
            mt "Покуда ты в моём отряде - это как раз моё дело, где ты шляешься!"
    show mt normal night at center with dspr
    mt "Всё, отправляйся в кровать."
    window hide
    menu:
        "Отпроситься":
            window show
            play sound ds_sfx_psy
            sug "Но тебе надо пойти!"
            me "Извините, но мне правда нужно идти!"
            mt "Завтра, всё завтра..."
            "Ты вынужден отложить заколку Мику на завтра."
        "Не отпрашиваться":
            window show
            th "Ладно, завтра отдам..."
    jump ds_day2_sleep

label ds_day2_house23:
    $ persistent.sprite_time = "night"
    scene bg ext_hosue_of_dv_night
    with dissolve

    "А вот и домик 23."
    play sound ds_sfx_mot
    per_eye "В темноте ты всё ещё можешь разглядеть пиратский флаг!"
    play sound ds_sfx_fys
    hfl "Здесь мало шансов найти Мику и много - неприятностей, кажется."
    window hide
    menu:
        "Открыть дверь":
            window show
            play sound sfx_knock_door6_closed
            "Ты пытаешься открыть дверь, но она заперта."
            per_hea "Ты уже хотел было постучаться, как услышал голос."
        "Постучаться":
            window show
            play sound sfx_knock_door6_closed
            "Ты стучишься в дверь."
            per_hea "В ответ слышишь голос."
        "Уйти":
            window show
            th "И то верно."
            $ ds_skill_points['half_light'] += 1
            $ disable_current_zone_ds_small()
            jump ds_day2_find_mi
    dv "Кого тут посреди ночи привалило?!"
    hfl "Ой-ёй, это Алиса..."
    hfl "Сразу побежишь или дождёшься расправы?"
    window hide
    menu:
        "Бежать":
            scene bg ds_ext_houses_night:
                zoom 1.05 anchor (48,27)
                ease 0.20 pos (0, 0)
                ease 0.20 pos (25,25)
                ease 0.20 pos (0, 0)
                ease 0.20 pos (-25,25)
                repeat
            with dissolve
            hfl "Ты бежишь так далеко, как можешь!"
            scene bg ext_square_night
            "Наконец, ты останавливаешься на площади."
            th "Что ж, куда теперь?"
            $ disable_current_zone_ds_small()
            jump ds_day2_find_mi
        "Ждать":
            window show
    $ renpy.pause(0.5)
    show dv angry swim far at center with dissolve
    dv "Это ты?!"
    show dv rage swim at center with dspr
    dv "Ты вообще в своём уме будить нас посреди ночи?!"
    dv "Что тебе приспичило так поздно?"
    window hide
    menu:
        "Cпросить про Мику":
            window show
            me "Да мне бы к Мику попасть..."
            show dv angry swim at center with dspr
            dv "Твоя Мику в другом конце лагеря, нет её тут!"
            dv "Это всё? Тогда иди!"
        "Подарить заколку":
            window show
            me "Это тебе!"
            "C этими словами ты протягиваешь ей заколку."
            show dv surprise swim at center with dspr
            dv "Эм... чего?"
            dv "Где ты это достал?"
            show dv shy swim at center with dspr
            dv "Cпасибо, конечно..."
            show dv angry swim at center with dspr
            dv "Но мне не требуется! И вообще, нечего ночами ходить!"
            "Она возвращает тебе заколку."
            window hide
            menu:
                "Настоять":
                    if skillcheck('suggestion', lvl_formidable):
                        window show
                        play sound ds_sfx_psy
                        sug "Нет, это подарок, который она примет."
                        me "Ты должна принять этот подарок. Если не нужен - отдашь кому-нибудь, я не обижусь."
                        me "Но я бы хотел, чтобы ты приняла его."
                        show dv shy swim at center with dspr
                        dv "Ладно... спасибо."
                        "Она забирает у тебя заколку."
                        $ ds_lp_dv += 1
                        $ ds_mi_hairpin = False
                        $ ds_gave_hairpin_dv = True
                        show dv normal swim at center with dspr
                        dv "Cпокойной ночи!"
                    else:
                        window show
                        sug "Нет, она не примет у тебя её, она ясно дала понять..."
                        me "Ну ладно..."
                        show dv normal swim at center with dspr
                        dv "Cпокойной ночи!"
                    $ ds_skill_points['suggestion'] += 1
                "Оставить":
                    window show
                    me "Ну ладно..."
                    show dv normal swim at center with dspr
                    dv "Cпокойной ночи!"
        "Потребовать быть вежливее":
            if skillcheck('authority', lvl_up_medium):
                window show
                aut "Она ведёт себя, мягко говоря, агрессивно."
                me "А ты чего сразу наезжаешь? Может, мне помощь нужна!"
                show dv angry swim at center with dspr
                dv "Ладно, но всё равно зачем будить-то?!"
                dv "Так что тебе надо-то?!"
                window hide
                menu:
                    "Спросить про Мику":
                        window show
                        me "Да мне бы к Мику попасть..."
                        show dv angry swim at center with dspr
                        dv "Твоя Мику в другом конце лагеря, нет её тут!"
                    "Не спрашивать":
                        window show
                        me "Да ничего мне уже не надо!"
                        $ ds_lp_dv -= 1
                        show dv angry swim at center with dspr
                        dv "Ну и иди тогда!"
            else:
                window show
                aut "Ну, ты её и правда разбудил..."
                me "Зачем так агрессивно?"
                show dv angry swim at center with dspr
                dv "А чтобы не будил посреди ночи!"
                dv "Короче, ищи помощи в другом месте! Пока!"
            $ ds_skill_points['authority'] += 1
        "Начать домогаться":
            if skillcheck('instinct', lvl_medium):
                play sound ds_sfx_fys
                ins "Ты её хочешь! И наверняка это взаимно! Покажи ей!"
                me "Знаешь, а я к {i}тебе{/i} пришёл..."
                me "Мне очень хочется прикоснуться к тебе, прижаться..."
                ins "Ты тянешься к её груди, столь манящей."
                show dv rage swim at center with dspr
                play sound sfx_face_slap
                with hpunch
                play sound ds_sfx_fys
                pat "Она больно бьёт тебя по руке."
                dv "Ты вообще в своём уме?! Куда свои лапы тянешь?!"
                $ ds_lp_dv -= 2
                dv "Беги, пока живой! А то прибью на месте!" 
            else:
                play sound ds_sfx_fys
                ins "Однако, ты слишком её боишься, чтобы включать свой хорни-режим."
                $ ds_morale -= 1
                me "Да... к тебе... но, пожалуй, ты не рада меня видеть."
                dv "Уж точно не сейчас!"
                dv "Иди уже!"
            $ ds_skill_points['instinct'] += 1
        "Вежливо уйти":
            window show
            me "Я, пожалуй, пойду..."
            dv "Вали, пока жив!"
        "Быстро свалить":
            if skillcheck('savoir_faire', lvl_medium):
                window show
                scene bg ds_ext_houses_night:
                    zoom 1.05 anchor (48,27)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (25,25)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (-25,25)
                    repeat
                with dissolve
                play sound ds_sfx_mot
                svf "У тебя получается легко и быстро убежать."
                $ ds_skill_points['savoir_faire'] += 1
                scene bg ext_square_night
                svf "Наконец, ты останавливаешься на площади."
                th "Что ж, куда теперь?"
                $ disable_current_zone_ds_small()
                jump ds_day2_find_mi
            else:
                window show
                play sound ds_sfx_mot
                svf "Ты пытаешься убежать, но Алиса останавливает тебя."
                $ ds_skill_points['savoir_faire'] += 1
                dv "А ну стоять!"
                dv "Чего бежишь, как девчонка?"
                window hide
                menu:
                    "Извиниться":
                        window show
                        me "Извини, что побеспокоил, я не хотел тебя будить..."
                        show dv angry swim at center with dspr
                        dv "Не хотел, но разбудил."
                        dv "Ладно, иди уже!"
                    "Обозвать":
                        window show
                        play sound ds_sfx_psy
                        aut "Вспомни: её можно задеть кое-каким прозвищем."
                        me "А тебе чего, ДваЧе?"
                        show dv rage swim close at center with dspr
                        play sound sfx_angry_ulyana
                        $ renpy.pause(0.5)
                        play sound ds_sfx_psy
                        vol "Додумался же ты ляпнуть это..."
                        dv "Ты там вообще берега потерял что ли?!"
                        $ ds_lp_dv -= 2
                        $ ds_karma -= 10
                        dv "Ну так мы их тебе сейчас поправим!"
                        window hide
                        if skillcheck('reaction_speed', lvl_godly):
                            window show
                            play sound ds_sfx_mot
                            res "У тебя получается поставить блок как раз вовремя."
                            show dv surprise swim close at center with dspr
                            aut "Алиса удивлена, что ты смог отбить её удар."
                            dv "Ладно... тут тебе повезло..."
                        else:
                            window show
                            play sound ds_sfx_mot
                            res "Ты не успеваешь отреагировать на её удар."
                            play sound sfx_lena_hits_alisa
                            with vpunch
                            $ ds_health -= 1
                            play sound ds_sfx_fys
                            pat "Удар Алисы пришёлся прямо по лицу."
                            pat "И от него тебе по-настоящему больно."
                            $ ds_skill_points['pain_threshold'] += 1
                        $ ds_skill_points['reaction_speed'] += 1
                        dv "И чтобы больше я от тебя такого не слышала!"
                    "Осудить":
                        if skillcheck('authority', lvl_up_medium):
                            window show
                            aut "Она тоже ведёт себя, мягко говоря, агрессивно."
                            me "А ты чего сразу наезжаешь? Может, мне помощь нужна!"
                            show dv angry swim at center with dspr
                            dv "Ладно, но всё равно зачем будить-то?!"
                        else:
                            window show
                            aut "Ну, ты её и правда разбудил..."
                            me "Зачем так агрессивно?"
                            show dv angry swim at center with dspr
                            dv "А чтобы не будил посреди ночи!"
                        $ ds_skill_points['authority'] += 1
                        dv "Короче, ищи помощи в другом месте! Пока!"
    play sound sfx_close_door_1
    hide dv with dissolve
    if ds_mi_hairpin:
        play sound ds_sfx_int
        lgc "Итак, Мику тут нет."
        th "Идти дальше?"
        window hide
        menu:
            "Идти сейчас":
                window show
                th "Нужно отдать сегодня!"
                $ disable_current_zone_ds_small()
                jump ds_day2_find_mi_house
            "Отложить до завтра":
                window show
                th "Нет, лучше до завтра подожду..."
                jump ds_day2_night
    else:
        th "Что ж, заколку сплавили, теперь пойдём спать..."
        jump ds_day2_night

label ds_day2_house13:
    $ persistent.sprite_time = 'night'
    scene bg ds_ext_un_night
    with dissolve

    "Ты подходишь к домику с тринадцатым номером."
    window hide
    menu:
        "Зайти без стука":
            window show
            play sound sfx_knock_door6_closed
            "Ты пытаешься открыть дверь... но безуспешно."
            play sound ds_sfx_mot
            per_hea "Изнутри доносится какой-то шум."
        "Постучать":
            window show
            play sound sfx_knocking_door_2
            "Ты стучишь в дверь."
    $ renpy.pause(0.5)
    show un surprise swim far at center with dissolve
    un "Ой, Семён? А зачем ты пришёл?"
    window hide
    menu:
        "Спросить Мику":
            me "Привет, а ты не знаешь, где Мику?"
            show un smile swim far at center with dspr
            un "Да, она тут, позвать?"
            me "Да, если можно..."
            hide un with dissolve
        "Подарить заколку":
            window show
            me "Это тебе!"
            "C этими словами ты достаёшь заколку и даёшь её Лене."
            show un surprise swim at center with dspr
            un "Что?"
            me "Заколку тебе дарю, говорю."
            show un shy swim at center with dspr
            un "Cпасибо..."
            hide un with dissolve
            "И она уходит, нет, убегает."
            play sound ds_sfx_psy
            emp "Неудивительно: она такая стеснительная."
            $ ds_lp_un += 1
            $ ds_mi_hairpin = False
            $ ds_gave_hairpin_un = True
            "Ты тоже уходишь к себе."
            jump ds_day2_night
        "Начать домогаться":
            if skillcheck('instinct', lvl_easy):
                window show
                ins "Ну что ж, давай, покажи ей, как ты её хочешь."
                me "К тебе пришёл. Хочу посмотреть на тебя... и потрогать."
                ins "Ты говоришь это максимально заигрывающим голосом."
                show un scared swim far at center with dspr
                un "Не надо!"
                hide un with dissolve
                $ ds_lp_un -= 1
                play sound ds_sfx_psy
                emp "Ну нельзя так резко с ней: она же очень стестнительная!"
                play sound ds_sfx_int
                dra "Или же изображает стеснительную."
                emp "Короче, не стоило с ней этого делать."
                $ ds_skill_points['instinct'] += 1
                "Ты вынужден уйти с заколкой."
                $ disable_current_zone_ds_small()
                jump ds_day2_find_mi_house
            else:
                window show
                ins "Однако, тебе слишком неудобно приставать к ней."
                play sound ds_sfx_psy
                vol "Поэтому лучше всё-таки спроси про Мику."
                me "А ты не знаешь, где Мику?"
                show un smile swim far at center with dspr
                un "Да, она тут, позвать?"
                me "Да, если можно..."
                hide un with dissolve
                $ ds_skill_points['instinct'] += 1
        "Уйти":
            window show
            me "Извини, я... ошибся домиком."
            show un smile swim far at center with dspr
            un "А, ну ладно. Спокойной ночи..."
            me "Cпокойной ночи."
            hide un with dissolve
            "И ты уходишь."
            jump ds_day2_night
    "Ты ждёшь."
    window hide
    $ renpy.pause(1.0)
    window show
    show mi normal swim far at center with dissolve
    mi "О, привет, Семён-кун! А ты зачем так поздно пришёл? Разве тебе не надо спать?"
    show mi smile swim at center with dspr
    "Она замечает у тебя заколку."
    mi "Ой, ты принём мою заколку. Спасибо тебе большое! Я так рада, что ты нашёл её для меня!"
    $ ds_lp_mi += 1
    play sound ds_sfx_psy
    aut "Она {i}должна{/i} с тобой расплатиться."
    window hide
    menu:
        "Не за что":
            window show
            me "Да не за что..."
        "Покичиться":
            window show
            me "Вот видишь, какой я!"
            "Мику безмолвна."
            $ renpy.pause(0.5)
        "Потребовать взамен":
            window show
            me "А что взамен?"
            mi "Ну, надо подумать..."
            if not ds_music_member:
                mi "О, давай я тебя научу играть на чём-нибудь! Приходи в музклуб завтра!"
                window hide
                menu:
                    "Принять":
                        window show
                        me "Хорошо..."
                        mi "Ой, отлично-то как! Нас теперь будет трое!"
                        $ ds_music_member = True
                        $ ds_lp_mi += 1
                    "Отклонить":
                        window show
                        me "Нет, спасибо, боюсь, я не успею."
                        show mi sad swim at center with dspr
                        mi "Ну ладно..."
            else:
                show mi upset swim at center with dspr
                mi "Я даже не знаю, что тебе предложить... Короче, приходи завтра в музклуб, придумаем, как тебя отблагодарить!"
        "Начать домогаться":
            if skillcheck('instinct', lvl_easy):
                play sound ds_sfx_fys
                ins "Расплатиться она вполне может и натурой, как думаешь?"
                me "Ну, я думаю, что ты вполне можешь кое-что для меня сделать взамен..."
                ins "Ты демонстрируешь максимально пошлое выражение лица."
                show mi scared swim at center with dspr
                mi "Ты о чём, Семён-кун?"
                me "Ну, знаешь, не будь бы Лены, мы могли бы в твоём домике кое-чем заняться..."
                show mi angry swim at center with dspr
                mi "Не понимаю, о чём ты говоришь, но мне не нравится твой настрой! Ты пугаешь! Своим выражением лица! Своими словами! Да всем!"
                
                $ ds_lp_mi -= 1
            else:
                play sound ds_sfx_fys
                ins "Ну, покажи ей, что ты её хочешь."
                ins "Стой, нет... у тебя не получаются намёки. А сказав прямо, ты её отпугнёшь!"
                me "Я думаю, нам с тобой нужно переспать!"
                show mi scared swim at center with dspr
                mi "Чего-чего?"
                me "Что сказал."
                show mi angry swim at center with dspr
                mi "Не буду я с тобой спать! Мне неуютно будет спать с другим человеком в одной кровати!"
                $ ds_lp_mi -= 2
            $ ds_skill_points['instinct'] += 1
            $ ds_karma -= 20
            play sound ds_sfx_psy
            emp "Когда-нибудь ты поймёшь, что с такими открытыми домогательствами тебе никто не даст..."
        "Промолчать":
            window show
    show mi normal swim far at center with dspr
    mi "В общем, спокойной ночи ещё раз и спасибо, Семён-кун! Ой, то есть наоборот!"
    me "Пока..."
    hide mi with dissolve
    "И она уходит."
    "Ты тоже идёшь к себе."
    jump ds_day2_night

label ds_day2_beach:
    $ persistent.sprite_time = "night"
    scene bg ext_beach_night 
    with dissolve

    $ night_time()

    stop ambience fadeout 2

    window show
    "Ты приходишь на пляж."
    play sound ds_sfx_fys
    edr "После турнира тебе было бы неплохо искупаться и освежиться."
    window hide
    menu:
        "Искупаться":
            window show
        "Не купаться":
            window show
            th "Нет, мне чего-то не хочется."
            "И ты идёшь назад"
            $ disable_current_zone_ds_small()
            jump ds_day2_after_tour
    play sound ds_sfx_mot
    svf "По правде говоря, ты и плавать-то толком не умеешь..."
    edr "Но возможность окунуться в прохладную воду на пляже при Луне представлялась мне не самой плохой перспективой."
    edr "Тем более после вчерашнего дня, проведенного в зимней одежде, тебя можно было выжимать от пота, так что и помыться не мешает."
    "Ты раздеваешься до трусов и входишь в воду."
    svf "Однако плескаться возле берега тебе кажется недостаточным."

    stop music fadeout 3

    if ds_tour_result == 3:
        svf "Обычно тебе вполне хватает 15-20 метров, но в этот раз эйфория от победы на турнире подталкивает тебя на попытку побить свой рекорд."
    else:
        svf "Обычно тебе вполне хватает 15-20 метров, но в этот раз горечь от поражения на турнире подталкивает тебя на попытку побить свой рекорд."
    svf "Ты плывёшь медленно и размеренно, следя за каждым движением рук и ног, за каждым вдохом и выдохом."
    $ ds_skill_points['endurance'] += 1
    $ ds_health += 1
    window hide

    $ renpy.pause(1.0)

    if (not ds_bet_dv) or (ds_tour_result < 3):
        "Наконец, ты заканчиваешь плавать, выходишь из воды, одеваешься и идёшь к себе."
        jump ds_day2_night

    play music music_list["that_s_our_madhouse"] fadein 3

    scene bg ext_beach_night :
        linear 0.05 pos (-5,-5)
        linear 0.05 pos (0,0)
        linear 0.05 pos (5,5)
        linear 0.05 pos (0,5)
        linear 0.05 pos (5,0)
        linear 0.05 pos (0,0)
        repeat

    window hide

    play sound sfx_shoulder_dive_water

    show blink 

    $ renpy.pause(1)

    window show
    play sound ds_sfx_mot
    per_toc "Уже почти доплыв до буйков, ты почувствовал сильный удар по спине."
    play sound ds_sfx_mot
    svf "От этого ты чуть не ушёл под воду."
    if skillcheck('savoir_faire', lvl_legendary, passive=True):
        svf "Ты начинаешь захлёбываться, но усилием воли берёшь себя в руки и удерживаешься на воде, схватившись за буек."
    else:
        svf "Ты начинаешь тонуть, но тут кто-то тебя подхватывает за плечи и закидывает на буёк."
        $ ds_dv_rescued = True
    window hide

    scene cg d2_water_dan 
    show unblink 
    with dissolve

    play sound sfx_water_emerge

    $ renpy.pause(1)

    window show
    "Ты оборачиваешься и видишь Алису, плывущую за тобой."
    me "Ты что делаешь?!"
    dv "Как что? Приветствую победителя."
    play sound ds_sfx_fys
    hfl "Находиться здесь попросту опасно – утопит еще, не ровен час."
    play sound ds_sfx_mot
    com "Но лучше тебе показать, что всё хорошо."
    window hide
    menu:
        "Возмутиться":
            window show
            me "А если бы я утонул?!"
            if ds_dv_rescued:
                dv "Так я же тебя спасла."
            else:
                dv "Ну, я бы тебя спасла."
            me "Ага, как же…"
        "Пихнуть в ответ":
            play sound ds_sfx_fys
            hfl "Ты толкаешь её в воду..."
            play sound sfx_alisa_falls
            scene bg ext_beach_night 
            with dissolve
            stop music fadeout 3
            hfl "И, пока она не успела очухаться, выплываешь на берег и бежишь куда подальше."
            $ ds_lp_dv -= 2
            $ ds_beat_dv = True
            $ ds_karma -= 20
            jump ds_day2_night
        "Рассмеяться":
            window show
            me "А прикольно ты приветстуешь победителей!"
            dv "А то!"
            $ ds_lp_dv += 1
            $ ds_semtype += 1
        "Молча уплыть":
            window show

    stop music fadeout 3

    "Вложив последние силы на рывок, ты плывёшь к берегу."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_beach_night 
    with dissolve

    play ambience ambience_boat_station_night fadein 3

    window show
    "Растянувшись на песке, ты пытаешься отдышаться."
    window hide
    $ renpy.pause(0.5)
    window show
    show dv normal swim at center   with dissolve
    "Через некоторое время из воды выходит и Алиса."
    dv "А ты неплохо плаваешь!"
    th "Я бы не сказал."
    play sound ds_sfx_psy
    aut "Она похвалила? Алиса похвалила?! Да не может быть такого!"
    window hide
    menu:
        "Поблагодарить":
            window show
            me "Спасибо..."
        "Ответить комплиментом":
            window show
            me "Ага, и ты тоже."
            show dv smile swim at center   with dspr
            dv "Ну, я-то понятно…"
        "Промолчать":
            window show
    dv "Ты сегодня у меня уже два раза выиграл.{w} Значит, тебе прощаются те два долга."
    play sound ds_sfx_mot
    res "Какие долги, за что?"
    res "Она, похоже, не совсем здраво воспринимает действительность."
    window hide
    menu:
        "Съязвить":
            window show
            me "Радушно благодарю…"
            $ ds_skill_points['drama'] += 1
        "Искренне поблагодарить":
            window show
            me "Спасибо..."
            aut "За что ты её благодаришь?!"
        "Промолчать":
            window show
    dv "Знаешь, а ты не такой уж и неудачник…"
    aut "Да что с ней не так сегодня?"
    aut "Но больше интересно, с чего она решила, что ты неудачник?"
    window hide

    scene cg d2_2ch_beach  with dissolve:
        pos (0,-1920)
        linear 10.0 pos (0,0)
        linear 2.0 pos (0, -250)

    window show
    "После этих слов ты поворачиваешь голову в ее сторону."
    play sound ds_sfx_fys
    ins "Она одета в купальник, который хорошо подчеркивает все прелести ее фигуры."
    th "Да, при всех минусах характера Двачевской этот плюс у нее не отнимешь."
    window hide
    menu:
        "Возмутиться":
            if skillcheck('authority', lvl_easy):
                window show
                aut "И ничего ты не неудачник!"
                me "А с чего это вдруг я неудачник?"
                dv "А что, разве не так?"
                me "Нет конечно!"
                dv "И чем докажешь?"
                me "Не собираюсь я тебе ничего доказывать!"
                dv "Ах, вот так, значит..."
                play sound ds_sfx_psy
                emp "Она говорит беззлобно."
                me "Да, вот так..."
                "Наступает молчание."
            else:
                window show
                aut "Но, с другой стороны, тебе и правда нечем крыть."
                "Ты молчишь."
            $ ds_skill_points['authority'] += 1
        "Сделать комплимент":
            window show
            me "А у тебя прекрасная фигура."
            dv "И без тебя знаю. А вот тебе много зырить на меня нельзя, а то накажу!"
            play sound ds_sfx_psy
            emp "Она шутит."
            "Наступает молчание."
        "Начать приставать":
            if skillcheck('instinct', lvl_easy):
                window show
                ins "Ты моментально ощущаешь реакцию своего тела от её вида. Вперёд, бери её!"
                "Ты подходишь к ней и хватаешь её за бока."
                dv "Что ты творишь? Домогаться до меня вздумал?!"
                dv "Да я тебе..."
                "И она отпрыгивает от тебя."
                dv "Ладно, на первый раз прощаю. Понимаю, что ты впечатлён моей красотой!"
                $ ds_lp_dv -= 1
            else:
                window show
                ins "Однако, ты слишком её боишься..."
                "Ты молчишь."
            $ ds_skill_points['instinct'] += 1
        "Промолчать":
            window show
    "Тихий ночной ветерок лениво играет волнами, то обрушивая их на берег, то забирая назад, чтобы собраться с силами и перегруппироваться."
    th "Алиса все так же смотрит словно сквозь меня, словно забыла о том, что я вообще все еще здесь."
    me "Эй, Земля вызывает Алису!"
    emp "В ее взгляд вмиг возвращается осмысленность."
    dv "Ладно, бывай."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_beach_night 
    with dissolve

    window show
    "Она забирает лежащую рядом одежду и уходит."
    window hide
    with fade2

    if skillcheck('reaction_speed', lvl_heroic, passive=True):
        window show
        res "Она и твою одежду забрала!"
        $ ds_skill_points['reaction_speed'] += 1
    else:
        window show
        play sound ds_sfx_psy
        ine "Было уже поздно, но ты решаешь еще некоторое время полежать и посмотреть на звезды."
        window hide

        scene stars 
        with dissolve

        window show
        th "В конце концов, раньше мне редко представлялась такая возможность."
        th "Или просто я сам редко себе ее создавал."
        th "Ведь если подумать, свет от далеких звезд долетает до нас за миллионы лет…"
        th "Вот сейчас я вижу звезду, потому что она светила тогда, а для нее это {i}тогда{/i} – далекое прошлое."
        th "И сейчас она, возможно, уже взорвалась…"

        stop ambience fadeout 0

        th "Стоп!{w} Она же и мою одежду забрала!"
    play music music_list["that_s_our_madhouse"] fadein 1
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_beach_night 
    with dissolve

    window show
    "Ты вскакиваешь и начинаешь осматривать пляж."
    play sound ds_sfx_mot
    per_eye "Действительно, Алиса унесла и твою пионерскую форму."
    th "Черт возьми!"
    th "А ведь я только начинал думать, что она, может быть, и не такая уж плохая…"
    play sound ds_sfx_psy
    emp "А ты уверен, что она со зла это сделала?"
    th "Надо что-то срочно придумать."
    th "Конечно, можно пожаловаться Ольге Дмитриевне, но вернуться к ней в одних мокрых трусах…"
    play sound ds_sfx_int
    enc "В какой палатке живет Алиса, ты не знаешь."
    aut "Стучаться во все подряд тоже не вариант…"
    play sound ds_sfx_psy
    vol "Может быть, зайти к Славе?"
    aut "Да, точно, ночью в одних трусах…{w} Только розы в зубах не хватает…"
    aut "С какой стороны ни посмотри, ты попал, причем попал серьезно…"
    vol "Но делать что-то надо в любом случае."
    window hide
    menu:
        "Догнать Алису":
            window show
            play sound ds_sfx_fys
            hfl "К счастью, не так много времени прошло, и ты еще успеваешь ее догнать..."

            stop music fadeout 3

            play sound ds_sfx_fys
            phi "... бегом!"
            window hide

            $ persistent.sprite_time = "night"
            scene bg ext_square_night 
            with dissolve

            play ambience ambience_camp_center_night fadein 3

            window show
            "Буквально через пару секунд ты оказываешься на площади."
            show dv normal pioneer2 at center   with dissolve
            play sound ds_sfx_mot
            per_eye "К твоему огромному удивлению, Алиса сидит на лавочке и явно скучает."
            per_eye "Она уже успела переодеться."
        "Подождать":
            window show
            stop music fadeout 3
            th "Лучше не буду никуда бежать..."
            window hide
            $ renpy.pause(3.0)
            window show
            show dv guilty pioneer2 at center with dissolve
            "Через некоторое время на пляж возвращается Алиса."
        "Пойти к Ольге Дмитриевне":
            window show
            scene bg ds_ext_houses_night with dissolve
            "Ты идёшь прямо к Ольге Дмитриевне."
            window hide
            $ renpy.pause(1.0)
            window show
            scene bg ext_house_of_mt_night with dissolve
            "Ты уже собирался было войти..."
            play sound ds_sfx_mot
            with vpunch
            per_toc "Как тебя кто-то одёргивает!"
            show dv guilty pioneer2 at center   with dspr
            "Ты оборачиваешься и видишь Алису."
            dv "Ты чего, прям пойдёшь и обо всём скажешь вожатой?"
            window hide
            menu:
                "Пойти дальше":
                    window show
                    me "Да, это недопустимо - то, что ты творишь!"
                    show dv angry pioneer2 at center with dspr
                    dv "Да забирай ты свою форму!"
                    "Она бросает в тебя форму и уходит."
                    hide dv with dissolve
                    $ ds_lp_dv -= 1
                    jump ds_day2_night
                "Передумать":
                    window show
                    me "Нет, я просто пошёл за запасной..."
                    me "Но раз уж ты тут..."
        "Пойти к Славе":
            window show
            scene bg ds_ext_houses_night with dissolve
            "Ты направляешься к домику Слави..."
            play sound ds_sfx_int
            enc "Только вот незадача: ты не знаешь, где домик Слави."
            play sound ds_sfx_mot
            with vpunch
            per_toc "Тут кто-то тебя одёргивает."
            "Ты оборачиваешься и видишь Алису."
    show dv guilty pioneer2 at center   with dspr
    me "Отдай!"
    dv "Да бери…"
    "Ответила она каким-то виноватым тоном и протянула мне мою форму."
    me "…"
    show dv shy pioneer2 at center   with dspr
    dv "Только не думай, что я это специально для тебя и все такое..."
    play sound ds_sfx_psy
    emp "Врёт, нагло врёт!"
    play sound ds_sfx_int
    dra "Эй, враньё - это по моей части вообще-то!"
    show dv guilty pioneer2 far at fright with dspr
    "Алиса разворачивается и не спеша идёт в сторону палаток."
    "Ты остаёшься стоять как вкопанный."
    play sound ds_sfx_fys
    hfl "В любом случае с ней нужно быть поосторожнее, и события сегодняшнего вечера ничего не меняют."
    window hide
    menu:
        "Задуматься об её поведении":
            window show
            th "Что это было?"
            th "Возможно, у нее проснулась совесть…"
            th "Хотя какое там…"
            window hide
            if skillcheck('empathy', lvl_challenging):
                window show
                emp "Ты так и не понял? Она таким образом привлекает твоё внимание."
                emp "Она изначально и понимала, что поступает не совсем правильно."
                emp "Но, по всей видимости, она просто не умеет иначе."
                emp "Ты её чем-то привлёк. И потому она украла твои вещи, чтобы ты обратил на неё внимание."
                window hide
                menu:
                    "Начать давить":
                        window show
                        me "Спасибо, конечно, но это очень плохо, что ты утащила форму!"
                        me "Обязательно расскажу о твоих проделках Ольге Дмитриевне!"
                        dv "Да знаю я, знаю..."
                        hide dv with dissolve
                        "И она уходит окончательно."
                        $ ds_lp_dv -= 1
                    "Отпустить":
                        window show
                        hide dv with dissolve
                    "Приободрить":
                        window show
                        play music music_list["i_dont_blame_you"] fadein 2
                        me "Эй, подожди!"
                        show dv guilty pioneer2 far at center with dspr
                        "Алиса останавливается и слушает тебя."
                        me "Я не обижаюсь на тебя."
                        me "Напротив, это было в какой-то степени... весело."
                        me "Да, весело было, заставила меня побегать!"
                        show dv shy pioneer2 far at center with dspr
                        dv "Правда?.."
                        $ ds_lp_dv += 1
                        me "Да, правда..."
                        show dv smile pioneer2 far at center with dspr
                        dv "Ну вот и отлично! Бывай!"
                        show dv guilty pioneer2 far at fright with dspr
                        dv "Но ты всё равно извини..."
                        hide dv with dissolve
                        th "Как же у неё настроение меняется..."
                        stop music fadeout 3
            else:
                window show
                emp "Да, скорее всего в ней проснулась совесть."
                window hide
                menu:
                    "Начать давить":
                        window show
                        me "Спасибо, конечно, но это очень плохо, что ты утащила форму!"
                        me "Обязательно расскажу о твоих проделках Ольге Дмитриевне!"
                        dv "Да знаю я, знаю..."
                        hide dv with dissolve
                        "И она уходит окончательно."
                        $ ds_lp_dv -= 1
                    "Отпустить":
                        window show
            $ ds_skill_points['empathy'] += 1
        "Начать давить":
            window show
            me "Спасибо, конечно, но это очень плохо, что ты утащила форму!"
            me "Обязательно расскажу о твоих проделках Ольге Дмитриевне!"
            dv "Да знаю я, знаю..."
            "И она уходит окончательно."
            $ ds_lp_dv -= 1
        "Отпустить":
            window show
            hide dv with dissolve

    stop ambience fadeout 2

    "Ты направляешься к домику Ольги Дмитриевны."
    window hide
    jump ds_day2_night

label ds_day2_entrance:
    play sound ds_sfx_mot
    per_hea "Ты вдруг слышишь какой-то шум за воротами."
    th "И кого еще принесло?.."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_clubs_night 
    with dissolve

    window show
    per_eye "Быстро дойдя до здания кружков, ты замечаешь, что кто-то идет по лесной тропинке."
    per_eye "Было темно, так что, кроме размытого силуэта, разглядеть ничего не удалось."
    play sound ds_sfx_int
    lgc "Кто же это ночью ещё не спит?"
    play sound ds_sfx_psy
    aut "Пионер, нарушающий режим? Ай-яй-яй!"
    window hide
    menu:
        "Преследовать":
            window show
        "Не преследовать":
            th "Да ну зачем мне это делать?"
            play sound ds_sfx_psy
            emp "Тем более, что этим ты можешь сделать неудобно тому пионеру..."
            $ ds_karma += 5
            stop ambience fadeout 2
            $ disable_current_zone_ds_small()
            jump ds_day2_after_tour

    stop ambience fadeout 2

    play sound ds_sfx_mot
    svf "Ты быстро, но по возможности осторожно направляешься за таинственной тенью."
    window hide

    play ambience ambience_forest_night fadein 3

    $ persistent.sprite_time = "night"
    scene bg ext_path_night 
    with dissolve

    window show
    "Тропинки сменяли друг друга, и вскоре ты оказываешься в чаще леса, окончательно потеряв из виду незнакомца."
    th "Может, стоило повернуть назад?"
    "Деревья расступились, и перед тобой открылся замечательный вид на небольшое лесное озеро."
    window hide

    scene cg d2_slavya_forest 
    with dissolve

    play music music_list["forest_maiden"] fadein 5

    play sound ds_sfx_mot
    per_eye "И тут ты видишь Славю…{w} Она идёт по бережку вприпрыжку, даже не идёт – порхает, на ходу стягивая пионерский галстук и расправляя рубашку."
    play sound ds_sfx_int
    con "Все это зрелище кажется тебе даже более фантастическим, чем само твоё пребывание в этом лагере."
    con "Славя видится тебе каким-то духом леса, может быть, нимфой."
    con "Она настолько сливается с природой, что уже становилась не просто человеком, а чем-то вроде древнего божества."
    play sound ds_sfx_int
    enc "Ты вспоминаешь все теологические теории, о которых читал когда-то."
    enc "Эта ситуация больше всего напоминает пантеизм – растворение Бога в природе, во всём сущем."
    play sound ds_sfx_psy
    ine "Вдруг это не какие-то инопланетяне или провал во времени, а божественное провидение закинуло тебя сюда?"
    play sound ds_sfx_int
    lgc "Действительно, Славя говорила, что любит природу…"
    lgc "Получается, что и в ней скрыта какая-то загадка…"
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_path_night 
    with dissolve

    window show
    play sound ds_sfx_psy
    vol "Ты решаешь не делать поспешных выводов и последовать за ней…"
    play sound ds_sfx_mot
    svf "Славя неслышно плывёт между деревьями, выбирая самые удобные тропки и изящно обходя поваленные деревья, ямки и коряги."
    svf "Тебе составляет большого труда не отставать, к тому же ты совершенно не хочешь, чтобы меня обнаружили – во-первых, подглядывать просто нехорошо, во-вторых, еще неизвестно до конца, что именно она тут делала."
    play sound ds_sfx_psy
    ine "Хотя почему-то казалось, что ничего такого – и дело даже не в том, что ничего фантастического или связанного с моим попаданием в этот мир..."
    ine "Просто – {i}ничего такого{/i}.{w} Ничего, за чем бы стоило подглядывать."
    window hide
    if skillcheck('savoir_faire', lvl_formidable):
        window show
        svf "Тебе удаётся следовать за ней незамеченным вплоть до площади."
        $ ds_skill_points['savoir_faire'] += 1
        window hide
    
        $ persistent.sprite_time = "night"
        scene bg ext_square_night 
        with dissolve

        window show
        "Славя останавливается и оборачивается в твою сторону."
        show sl normal pioneer far at center    with dissolve 
        sl "Думаешь, я тебя не заметила?"
        play sound ds_sfx_mot
        com "Ты немного растерялся, но стараешься сохранить хотя бы видимость спокойствия."
        me "И давно?"
        show sl normal pioneer at center   with dissolve
        sl "Не знаю..."
        "Славя подходит ближе."
        show sl smile pioneer at center   with dspr
        sl "Может быть, минут пять."
        me "То есть и там, на озере?.."
        show sl surprise pioneer at center   with dspr
        sl "На каком озере?"
        me "Ну как же..."
        play sound ds_sfx_psy
        emp "Она выглядит искренне удивленной, поэтому ты никак не можешь понять – она просто притворяется и делает вид, что ничего не произошло, или..."
        play sound ds_sfx_psy
        vol "Лучше поступи галантно (насколько это вообще возможно в таких обстоятельствах) и промолчи."
        window hide
        menu:
            "Давить дальше":
                window show
                me "Нет, я тебя видел на озере."
                sl "Тебе показалось..."
                play sound ds_sfx_int
                dra "Врёт, ты это и сам прекрасно понимаешь."
                dra "Но тебе нечем крыть. Придётся пока принять."
            "Отступить":
                window show
                me "Ладно, забудь."
                show sl happy pioneer at center   with dspr
                sl "Хорошо."
                "Неожиданно легко согласилась она."
        sl "Какая сегодня ночь замечательная!"
        "Славя садится на скамейку и поднимает глаза на небо."
        play sound ds_sfx_int
        dra "Пытается вас отвлечь мессир... но тут вам придётся подыграть."
        me "Наверное, тут часто бывают такие ночи."
        show sl smile2 pioneer at center   with dspr
        sl "Ну, наверное..."
        me "Почему так неуверенно?"
        sl "Нет, просто задумалась."
        me "О чем?"
        show sl normal pioneer at center   with dspr
        "Она внимательно смотрит на тебя, словно что-то ищет на лице, но затем вновь возвращается к созерцанию звезд."
        sl "Просто иногда по ночам такое настроение бывает...{w} Днем – вся в делах, даже отдохнуть порой некогда, а ночью тут так тихо."
        sl "Если бы не сверчки и ночные птицы, то кажется, как будто остался наедине с космосом."
        play sound ds_sfx_psy
        ine "Почему-то тебе казалось, что Славя – не та девочка, которая будет рассуждать о подобных материях."
        me "Да для меня тут даже слишком спокойно."
        show sl serious pioneer at center   with dspr
        sl "Правда?"
        me "Да, правда, а что такого?"
        show sl smile pioneer at center   with dspr
        sl "Ничего..."
        show sl normal pioneer at center   with dspr
        sl "Ладно!"
        "Она резким движением встаёт и поправляет юбку."
        show sl smile pioneer at center   with dspr
        sl "Уже и спать пора!"
        me "Спокойной ночи!"
        hide sl  with dissolve
        "Ты провожаешь её взглядом."
        $ ds_lp_sl += 1
        ine "Возможно, ваш разговор и был ни о чем, но для тебя почему-то он кажется наполненным каким-то особенным, таинственным смыслом, который мог родиться только {i}здесь{/i}, только вместе со Славей."
        ine "И пусть даже ты не знаешь, где ты и почему ты именно здесь, но такие минуты тишины и покоя, почти что единения со Вселенной необходимы и тебе."
        ine "Просто жизненно необходимы – особенно сейчас!"
        "..."
        window hide

        with fade2

        window show
        "..."

        stop ambience fadeout 2

        stop music fadeout 3

        play sound ds_sfx_fys
        edr "Ты не знаешь, сколько просидел, но вскоре тебя начинает клонить в сон."
        window hide
    else:
        queue sound sfx_break_cupboard
        queue sound sfx_body_bump
        $ renpy.pause(0.5)
        window show
        play sound ds_sfx_mot
        svf "Тебе под ноги предательски попадает коряга, и ты падаешь."
        svf "Громкий звук хруста и падения привлекает внимание Слави."

        show sl surprise naked far at center with dissolve
        sl "Семён?.."
        show sl surprise naked at center with dspr
        play sound ds_sfx_fys
        ins "Она стоит перед тобой совершенно голая... не успела одеться до того, как встретила тебя."
        ins "Тебя этот вид определённо возбудил."
        window hide
        menu:
            "Начать домогаться":
                if skillcheck('instinct', lvl_easy):
                    window show
                    ins "Давай: она явно говорит своим телом, что хочет тебя!"
                    me "Ой, как ты замечательно выглядишь, какая фигура..."
                    show sl surprise naked close at center with dspr
                    ins "С этими словами ты притягиваешь её к себе..."
                    show sl scared naked close at center with dspr
                    sl "Что ты делаешь?"
                    show sl scared naked at center with dspr
                    "С этими словами она отводит твои руки и отходит на безопасное расстояние."
                    me "Хочу прикоснуться к твоей красе..."
                    show sl serious naked at center with dspr
                    sl "Приятно, конечно... но не так резко!"
                    $ ds_lp_sl -= 1
                else:
                    window show
                    ins "Однако, даже тут ты слишком боишься и нервничаешь, чтобы показать своё желание."
            "Спросить про неё":
                window show
            "Откланяться и уйти":
                window show
                me "Ой, извини, я тут случайно забрёл... уже ухожу."
                svf "И бросаешься бежать к своему домику что есть мочи."
                $ ds_lp_sl -= 1
                window hide
                jump ds_day2_night
        me "А что ты тут делаешь... в таком виде?"
        show sl smile naked at center with dspr
        sl "Просто иногда по ночам такое настроение бывает...{w} Днем – вся в делах, даже отдохнуть порой некогда, а ночью тут так тихо."
        sl "Если бы не сверчки и ночные птицы, то кажется, как будто остался наедине с космосом."
        play sound ds_sfx_psy
        ine "Почему-то тебе казалось, что Славя – не та девочка, которая будет рассуждать о подобных материях."
        play sound ds_sfx_int
        enc "Её слова очень напоминают идеи натуристов (они же нудисты) - те тоже заявляют, что наготой приближаются к природе."
        me "Да, для меня тут даже слишком спокойно."
        show sl serious naked at center   with dspr
        sl "Правда?"
        me "Да, правда, а что такого?"
        show sl smile naked at center   with dspr
        sl "Ничего..."
        show sl normal naked at center   with dspr
        sl "Ладно!"
        "Она резким движением встаёт, поднимает свою одежду."
        show sl smile naked at center   with dspr
        sl "Уже и спать пора!"
        me "Спокойной ночи!"
        hide sl  with dissolve
        "Ты провожаешь её взглядом."
        $ ds_lp_sl += 1
        ine "Возможно, ваш разговор и был ни о чем, но для тебя почему-то он кажется наполненным каким-то особенным, таинственным смыслом, который мог родиться только {i}здесь{/i}, только вместе со Славей."
        ine "И пусть даже ты не знаешь, где ты и почему ты именно здесь, но такие минуты тишины и покоя, почти что единения со Вселенной необходимы и тебе."
        ine "Просто жизненно необходимы – особенно сейчас!"
    jump ds_day2_night

label ds_day2_badminton:
    $ persistent.sprite_time = "night"
    scene bg ext_playground_night 
    with dissolve

    play ambience ambience_camp_center_night fadein 3

    window show
    play sound ds_sfx_psy
    vol "Тебе хочется уйти подальше ото всех."
    th "Самым подходящим местом уединения будет спортивная площадка."
    th "И правда, кому вечером взбредет в голову играть в футбол?"
    "Ты садишься на лавочку рядом с полем и принимаешься размышлять о произошедшем."
    play sound ds_sfx_mot
    per_hea "Вдруг со стороны волейбольной площадки послышались какие-то звуки."

    play sound sfx_lena_plays_tennis_fail

    per_eye "Кто-то отчаянно машет рукой."
    th "И кому он там семафорит?.."
    per_eye "Это Лена."
    per_eye "Она подкидывает воланчик и пытается попасть по нему ракеткой."
    per_eye "Однако выходиn это у неё паршиво."
    "Ты некоторое время просто смотришь..."
    window hide
    menu:
        "Подойти":
            if skillcheck('volition', lvl_challenging):
                window show
                vol "Подойди к ней."
                $ ds_skill_points['volition'] += 1
            else:
                window show
                vol "Лучше не стоит ей мешать..."
                "И ты уходишь."
                jump ds_day2_after_tour
        "Не подходить":
            window show
            th "Да нет, не буду ей мешать..."
            $ ds_semtype -= 1
            jump ds_day2_after_tour
    "Обойдя волейбольную площадку, ты заходишь внутрь так, чтобы она меня видела."
    play sound ds_sfx_psy
    sug "С учётом её привычки пугаться даже малейшего шороха, не стоит повторять прошлых ошибок."
    show un normal sport at center   with dissolve
    me "Привет!"
    "Она смотрит на тебя и тут же прячет за спину ракетку и воланчик."
    me "Бадминтон любишь?"
    un "Ну, не то чтобы…"
    me "Смотрю, у тебя не очень получается..."
    play sound ds_sfx_psy
    emp "Сочувствие тут не поможет, скорее испортит."
    window hide
    menu:
        "Посочувствовать":
            window show
            me "Сочувствую..."
            show un sad sport at center with dspr
            un "Ладно, я пойду, всё равно не получается..."
            hide un with dissolve
            "И она сбегает так быстро, что ты не успеваешь ничего сказать."
            th "Пойду к себе тогда..."
            jump ds_day2_night
        "Посмеяться":
            window show
            me "Эх ты, даже по воланчику попасть не можешь!"
            show un cry sport at center with dspr
            un "Я...  настолько... неудачливая?"
            emp "Ты её по-настоящему сильно обидел."
            $ ds_lp_un -= 1
            $ ds_karma -= 10
            hide un with moveoutleft
            "Она в слезах сбегает."
            th "Пойду к себе тогда..."
            jump ds_day2_night
        "Предложить научить":
            window show
    me "Может, тебя научить?"
    play sound ds_sfx_mot
    cor "По правде говоря, ты и сам толком не умеешь, но, как и всем детям, в свое время тебе приходилось пару раз играть."
    me "Давай покажу."
    show un shy sport at center   with dspr
    un "Спасибо."
    un "Хочу попасть в команду по бадминтону, но, видишь, у меня не очень выходит…"
    un "Я бы сегодня и не пришла, но…"
    show un smile sport at center   with dspr
    "Она поднимает глаза на тебя."
    un "Мне никогда в карты не везло, а сегодня выиграла и подумала, что, может, и с этим получится…"
    play sound ds_sfx_psy
    aut "Да уж, после этих слов ты понимаешь, что поражение от Лены – это вдвойне обидно."
    me "Никогда бы не подумал, что ты увлекаешься спортом."
    show un shy sport at center   with dspr
    me "Ой, прости…{w} Давай, сейчас покажу!"
    cor "Ты берёшь ракетку, подбрасываешь воланчик и…"
    window hide

    if skillcheck('coordination', lvl_legendary):
        play sound sfx_tennis_serve_1

        show un surprise sport at center   with dspr
        cor "Ты бьёшь по воланчику точно как надо."
        cor "Он приземляется на траву."
        $ ds_skill_points['coordination'] += 1
        show un smile sport at center with dspr
        un "Понятно..."
        me "Теперь повтори."
        "Лена берёт у тебя из рук ракетку."
        "Ты подаёшь ей воланчик, и она делает бросок."

        play sound sfx_tennis_serve_1
        "У неё тоже получается. И успешно."
        show un smile sport at center with dspr
        un "Спасибо!"
        $ ds_lp_un += 1
        me "Не за что..."
        show un normal sport at center with dspr
        un "Ну, я пойду!"
        un "Спокойной ночи!"
        me "Спокойной ночи..."
        hide un with dissolve
        "И она уходит."
        "Недолго думая, ты тоже уходишь к себе."
        jump ds_day2_night
    else:
        play sound sfx_tennis_serve_1

        show un surprise sport at center   with dspr
        cor "Ты бьёшь с такой силой, что он перелетает ограду и скрывается где-то между деревьями."
        me "Ой, прости!"
        cor "Ты даже не ожидал от себя такой силы."
        $ ds_skill_points['coordination'] += 1
        show un normal sport at center   with dspr
        un "Ничего…{w} Правда, это был последний…"
        window hide
        menu:
            "Отправить Лену":
                window show
                me "Ну так иди за ним, раз последний!"
                show un scared sport at center with dspr
                un "Ладно..."
                play sound ds_sfx_psy
                emp "Она очень боится леса, а ты отправляешь её туда одну..."
                $ ds_lp_un -= 1
                hide un with dissolve
                "Она ушла."
                window hide
                menu:
                    "Подождать":
                        window show
                        "Ты принимаешься её ждать."
                        "Проходит пять минут, десять, пятнадцать..."
                        play sound ds_sfx_int
                        lgc "Да ушла она уже. К себе ушла. Иди и ты."
                    "Пойти домой":
                        window show
                        th "Зачем мне её ждать ещё?"
                "И ты уходишь к себе."
            "Пойти одному":
                window show
                me "Последний? Тогда пойду поищу тут!"
                me "Подожди меня здесь!"
                show un scared sport at center with dspr
                un "Ладно..."
                hide un with dissolve
                window hide
                scene bg ext_path_night 
                with dissolve

                window show
                "Ты выходишь с площадки и начинаешь осматривать деревья."
                window hide
                if skillcheck('perception', lvl_heroic):
                    play sound ds_sfx_mot
                    per_eye "Ты осматриваешь каждое дерево в поисках воланчика..."
                    per_eye "И наконец видишь его! Вот он!"
                    "Ты берёшь воланчик и возвращаешься на спортплощадку."
                else:
                    play sound ds_sfx_mot
                    per_eye "Ты осматриваешь каждое дерево в поисках воланчика..."
                    per_eye "Но нигде его нет!"
                    "Осмотрев каждый куст в округе, ты всё ещё не находишь воланчика."
                    th "Печально... придётся сказать Лене, что воланчиков больше нет..."
                    "Ты возвращаешься на спортплощадку."
                $ ds_skill_points['perception'] += 1
                scene bg ext_playground_night 
                with dissolve
                play sound ds_sfx_mot
                res "Лены тут нет!"
                th "Она ушла? Она всё-таки ушла?"
                per_eye "Да, ты нигде не видишь ни намёка на присутствие Лены."
                th "Ладно, пойду к себе..."
            "Пойти с Леной":
                window show
                me "Последний? Пойдем тогда поищем его!"
                un "Нет, не стоит…{w} Там в лесу…"
                me "Кто, леший?"
                "Ты смеёшься."
                un "Может быть…"
                play sound ds_sfx_psy
                emp "Ты-то шутишь, а вот она, похоже, нет."
                play sound ds_sfx_psy
                sug "Но с тобой она пойдёт."
                me "Да никого там нет, не бойся, пойдем!"
                un "Ну, если только с тобой…"
                $ ds_lp_un += 1
                window hide

                $ persistent.sprite_time = "night"
                scene bg ext_path_night 
                with dissolve

                window show
                "Вы выходите с площадки, и ты начинаешь осматривать деревья."
                window hide
                play sound sfx_owl_far
                $ renpy.pause(0.5)
                window show
                play sound ds_sfx_mot
                per_hea "Вдруг тишину ночи нарушило уханье совы."
                window hide

                stop ambience fadeout 2

                scene cg d2_sovenok 
                with dissolve

                play music music_list["confession_oboe"] fadein 5

                window show
                play sound ds_sfx_psy
                emp "Лена, видимо, так испугалась, что схватила тебя сзади, обвив руками."
                play sound ds_sfx_fys
                ins "Она настолько крепко прижалась к тебе, что ты смутился."
                ins "Так близко чувствовать тело девочки, ее тепло."
                emp "Тебя обуяла нежность."
                emp "Тебе хочется защищать ее, не давать в обиду никому, пусть это будет даже всего лишь сова или какая другая ночная птица."
                ins "Осталось лишь одно желание – чтобы она не отпускала…"
                ins "Впрочем, хорошее имеет свойство заканчиваться…"
                play sound ds_sfx_int
                vic "Через некоторое время ты определяешь, откуда исходят звуки, и видишь на ветке рядом с собой маленького совенка, держащего ваш воланчик."
                me "Это вот его ты боялась?"
                un "Угу…"
                window hide
                menu:
                    "Успокоить":
                        window show
                        me "Посмотри, он совсем не страшный."
                        "Она выглядывает у тебя из-за спины, все так же продолжая крепко тебя обнимать."
                        un "Не страшный…"
                        me "Сейчас, подожди."
                        window hide

                        stop music fadeout 3

                        $ persistent.sprite_time = "night"
                        scene bg ext_path_night 
                        with dissolve

                        play ambience ambience_camp_center_night fadein 3

                        show un shy sport at center   with dissolve
                        window show
                        "Ты мягко освобождаешься от её объятий и подходишь к совенку."
                        th "Совёнок должен испугаться и улететь, выпустив из клюва воланчик."
                        "Однако он и не собирается двигаться с места."
                        play sound ds_sfx_mot
                        svf "Тебе удаётся схватить воланчик и аккуратно отобрать его у совёнка."
                        me "Смотри, он совсем ручной!{w} Хочешь его погладить?"
                        un "Может, в другой раз?.."
                        $ ds_lp_un += 1
                        $ ds_skill_points['empathy'] += 1
                    "Посмеяться":
                        window show
                        me "Он же такой маленький, как его можно бояться?"
                        "Она выглядывает у тебя из-за спины, все так же продолжая крепко тебя обнимать."
                        un "Да, маленький... но страшный..."
                        me "Сейчас, подожди."
                        window hide

                        stop music fadeout 3

                        $ persistent.sprite_time = "night"
                        scene bg ext_path_night 
                        with dissolve

                        play ambience ambience_camp_center_night fadein 3

                        show un scared sport at center   with dissolve
                        window show
                        "Ты мягко освобождаешься от её объятий и подходишь к совенку."
                        th "Совёнок должен испугаться и улететь, выпустив из клюва воланчик."
                        "Однако он и не собирается двигаться с места."
                        play sound ds_sfx_mot
                        svf "Тебе удаётся схватить воланчик и аккуратно отобрать его у совёнка."
                        $ ds_lp_un -= 1
                        $ ds_karma -= 5
                "Ты протягиваешь Лене воланчик."
                show un smile sport at center   with dspr
                un "Спасибо тебе."
                "Она еле заметно улыбается."
                show un normal sport at center   with dspr
                un "Мне пора."
                me "Успехов тебе в бадминтоне."
                show un smile sport at center   with dspr
                "Она вновь улыбается и побежала в сторону лагеря."
                hide un  with dissolve
                th "Какая она все же милая."

                stop ambience fadeout 2

                window hide
    jump ds_day2_night

label ds_day2_scene:
    scene black 
    with dissolve

    window show
    play sound ds_sfx_psy
    ine "События прошедшего дня все еще ярко мелькают у тебя в голове – чертов никому не нужный обходной, глупый турнир…"
    play sound ds_sfx_psy
    vol "Сегодня тебе не хочется больше ничего делать, ни с кем разговаривать, и даже разбираться со своей непростой ситуацией у меня не было никакого желания."
    "Ты идёшь на север.{w} По крайней мере в ту сторону, где он по твоим прикидкам есть."
    ine "Твоя традиция с молодости – ходить на север."
    ine "Ты больше любил эту часть своего родного города, чем южные районы."
    ine "Также тебя никогда не прельщал отдых на черноморских курортах – бескрайние леса и поля тебе куда милее, чем пляжи и барханы."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_stage_big_night 
    with dissolve

    play ambience ambience_camp_center_evening fadein 2

    window show
    "Вскоре ты выходишь к концертной площадке."
    "Она представляла из себя несколько рядов деревянных скамеек и деревянную же эстраду."
    "Я поднялся на сцену."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_stage_normal_night 
    with dissolve

    window show
    "Тут довольно много всякого музыкального оборудования: колонки, микрофонная стойка и даже пианино."
    ine "Я представил, что передо мной толпа зрителей, все кричат, приветствуют меня, а в глаза бьет слепящий свет прожекторов."
    ine "Вообрази, что в руках у тебя гитара. Исполни соло."
    window hide
    menu:
        "Сыграть":
            if skillcheck('inland_empire', lvl_medium):
                window show
                ine "Ты начинаешь двигать руками, будто держишь гитару."
            else:
                window show
                ine "Твои движения неуклюжи, у тебя не получается нормально представить игру на гитаре."
            $ ds_skill_points['inland_empire'] += 1
            play sound ds_sfx_psy
            aut "Наверное, со стороны это смотрится смешно – парень на сцене размахивает руками, бегает туда-сюда, корчится и кривляется, при этом строя глупые гримасы."
            aut "Хорошо бы тебя здесь никто не увидел."
        "Не играть":
            window show
            th "Да ну зачем?"
        "Уйти":
            window show
            th "Зачем мне вообще эта сцена."
            "Ты уходишь назад."
            window hide
            jump ds_day2_after_tour

    stop ambience fadeout 2

    play music music_list["glimmering_coals"] fadein 5

    us "Ого!"
    play sound ds_sfx_mot
    per_hea "Голос доносится откуда-то сверху."
    show us laugh pioneer  with dissolve:
        xalign 0.5
        yanchor 0.116
        rotate 180
    "Ты поднимаешь глаза и видишь Ульянку, свесившуюся с балки под потолком сцены."
    us "Что это мы тут делаем?"
    me "Да я тут просто…"
    play sound ds_sfx_int
    rhe "Оправдываться явно бесполезно."
    me "Сама все видела."
    show us laugh2 pioneer  with dspr:
        xalign 0.5
        yanchor 0.116
        rotate 180
    us "В тебе, я погляжу, умирает талант великого гитариста."
    play sound ds_sfx_int
    rhe "Не отвечай ей."
    show us smile pioneer  with dspr:
        xalign 0.5
        yanchor 0.116
        rotate 180
    us "Ну, ладно тебе, не дуйся, смотрелось забавно!"
    me "Забавно говоришь?"
    "Ты ехидно ухмыляешься."
    us "Да."
    play sound ds_sfx_mot
    com "Она говорит абсолютно спокойно."
    show us grin pioneer  with dspr:
        xalign 0.5
        yanchor 0.116
        rotate 180
    us "Подойди-ка сюда."
    me "Куда?"
    us "Ко мне!"
    me "Я туда лезть не собираюсь, не думай даже!"
    play sound ds_sfx_fys
    hfl "Не то чтобы ты боялся высоты, но какой смысл был забираться на эту балку?"
    us "Да нет! Просто сюда."
    hfl "Ты чувствуешь что-то недоброе..."
    window hide
    if skillcheck('half_light', lvl_medium, passive=True):
        window show
        hfl "Она хочет спрыгнуть! Беги за ней!"
        $ ds_skill_points['half_light'] += 1
        "Ты бежишь в её сторону."
        "Когда ты оказываешься точно под ней, она кричит."
    else:
        window show
        hfl "Но чего она хочет?"
        window hide
        menu:
            "Подойти":
                window show
                "Но, так как сразу не смог понять, в чем подвох, медленно направился в ее сторону."
                "Когда ты оказываешься точно под ней, она крикнула."
            "Не подходить":
                window show
                me "Да ну тебя, не подойду."
    us "Лови!"
    window hide

    scene cg d2_ussr_falling 
    with dissolve

    window show
    "И она прыгает…"
    window hide
    menu:
        "Ловить":
            if skillcheck('reaction_speed', lvl_up_medium):
                window show
                play sound ds_sfx_mot
                res "Не задумываясь, ты бросаешься за ней."
                res "В последний момент тебе удаётся захватить её в свои руки."
                $ ds_skill_points['reaction_speed'] += 1
                window hide

                stop music fadeout 3

                $ persistent.sprite_time = "night"
                scene bg ext_stage_normal_night 
                with dissolve

                play ambience ambience_camp_center_evening fadein 2

                show us laugh pioneer at center with dissolve

                $ renpy.pause(1.0)
                window show
                us "Поймал! Всё-таки поймал!"
                me "Да, поймал..."
                us "А ты быстрый! Впечатляет!"
                $ ds_lp_us += 1
            else:
                window show
                play sound ds_sfx_mot
                res "Как ты её поймаешь? А надо ли вообще ловить? А что, если она разобьется? А что, если она тебе что-то сломает? Да и почему именно ты?!"
                res "Тем временем, пока ты всё обдумывал, она уже коснулась земли..."
                $ ds_skill_points['reaction_speed'] += 1
                window hide

                stop music fadeout 3

                $ persistent.sprite_time = "night"
                scene bg ext_stage_normal_night 
                with dissolve

                play ambience ambience_camp_center_evening fadein 2

                show us upset pioneer at center   with dissolve

                $ renpy.pause(1)

                show us sad pioneer at center   with dspr
                window show
                "Ульянка мягко приземлилась, перекувыркнулась, мгновенно вскочила на ноги и обиженно посмотрела на меня."
                us "Почему не поймал?"
                me "Ну ты же не разбилась..."
                "Ответил я, отведя взгляд."
                show us shy2 pioneer at center   with dspr
                us "А если бы разбилась?"
                me "Не разбилась!{w} Да и что это вообще такое? Дешевых фильмов обсмотрелась?"
        "Не ловить":
            window show
            th "Да вряд ли она разобьётся..."
            play sound ds_sfx_mot
            res "Как ты её поймаешь? А надо ли вообще ловить? А что, если она разобьется? А что, если она тебе что-то сломает? Да и почему именно ты?!"
            th "Она сама виновата – нечего дурью маяться!"
            th "Удивительно, сколько мыслей приходят и уходят за долю секунды."
            th "А ведь иногда, чтобы родить хотя бы одну, уходят годы."
            "В конце концов, логика и инстинкт самосохранения выигрывают, и ты просто отходишь в сторону."
    show us grin pioneer at center   with dspr
    us "А что, волнуешься за меня?"
    window hide
    menu:
        "Волнуюсь":
            window show
            me "В такой ситуации… Ну, естественно, волнуюсь."
            show us surp3 pioneer at center   with dspr
            us "Я польщена."
            $ ds_lp_us += 1
        "Не волнуюсь":
            window show
            me "Да не то чтобы..."
            show us dontlike pioneer at center with dspr
            us "Эй! Чего это так?"
            $ ds_lp_us -= 1
    me "Эй, ты не подумай…"
    show us laugh pioneer at center   with dspr
    us "Ладно-ладно. Прощаю тебе карты."
    me "А вот я тебе это прощать не…"
    hide us  with dissolve
    "Ты не успеваешь закончить – Ульянка спрыгивает со сцены и убегает в сторону лагеря."
    hfl "Очередная идиотская выходка этой глупой девчонки."
    hfl "Да, конечно, ты испугался за нее."
    hfl "Да и будь любой другой на ее месте…"
    "Ты направляешься в сторону своей палатки."
    window hide

    stop ambience fadeout 2

label ds_day2_night:
    $ persistent.sprite_time = "night"
    scene bg ext_house_of_mt_night_without_light 
    with dissolve

    play music music_list["a_promise_from_distant_days"] fadein 5

    window show
    play sound ds_sfx_fys
    edr "На подходе к домику вожатой тебя накрывает дикая усталость."
    play sound ds_sfx_int
    lgc "Свет в окне не горит, значит, Ольга Дмитриевна уже спит."
    th "Странно, ведь вчера она меня ждала…"
    th "Может, доверять начала?"
    lgc "Да вряд ли…"
    window hide

    window show
    "Ты заходишь."
    jump ds_day2_sleep

label ds_day2_sleep:
    $ persistent.sprite_time = "night"
    scene bg int_house_of_mt_night2 
    with dissolve
    "Ты раздеваешься и ложишься спать."
    th "Если поразмыслить, то моя ситуация за сегодня совершенно не прояснилась."
    th "Я не узнал, ни где я, ни почему я тут."
    th "В сущности, я весь день занимался бесполезными делами; в реальном мире мне бы и в голову не пришло тратить свое время на что-то подобное."
    th "Хотя как раз там у меня этого времени было хоть отбавляй."
    th "А сколько его тут – совершенно неизвестно."
    th "Может быть, целая вечность, а может, всего несколько минут."
    play sound ds_sfx_psy
    vol "Тебе не хочется больше думать о прошлом, о том, как ты попал в этот лагерь."
    vol "Впервые за очень долгое время ты по-настоящему устал – не только эмоционально, но и физически, психологически и Бог знает как еще..."
    vol "Ты хочешь лишь, чтобы от тебя все отстали – в первую очередь твои мысли.{w} Хочешь, чтобы все разрешилось как-нибудь само собой."
    vol "Ну, или по крайней мере без твоего деятельного участия."
    play sound ds_sfx_psy
    ine "А вдруг ты тут навсегда?"
    ine "Тогда придется привыкать..."
    th "Но как вот так просто... Я... Я не готов...{w} Эх..."
    vol "Сознание улетает всё дальше, и всё сложнее сконцентрироваться на чем-то конкретном."
    th "Наверное, лучше отложить на завтра..."
    "Ты переворачиваешься на другой бок и засыпаешь."
    window hide

    stop music fadeout 3

    scene bg black 
    with fade3

    $ renpy.pause(3)
    jump ds_day2_dream

label ds_day2_dream:
    $ prolog_time()
    scene bg int_liaz with dissolve2
    play music ds_dream

    "Ты открываешь глаза и видишь вокруг себя салон автобуса."
    th "Как? Я же уснул в домике... В лагере..."
    play sound ds_sfx_psy
    ine "Это тот самый автобус, на котором ты уехал перед попаданием в «Совёнок»."
    play sound sfx_bus_stop
    window hide
    $ renpy.pause(1.0)
    play sound ds_sfx_psy
    window show
    vol "Выходи! Твоя остановка."
    "Ты выходишь."
    window hide
    scene bg bus_stop with dissolve
    $ renpy.pause(1.0)

    window show
    show dvw normal at left with dissolve
    play sound ds_sfx_mot
    per_eye "Вдали ты замечаешь девушку."
    vol "Почему-то тебя тянет к ней..."
    "Ты подходишь ближе. Она поворачивается к тебе."
    show dvw normal at center with dissolve
    "Это Алиса. У неё в руках сумка. Похоже, она куда-то спешит."
    play sound ds_sfx_int
    enc "Стоп. Почему-то её лицо тебе кажется знакомым."
    enc "Причём, знакомым {i}до{/i} «Совёнка»."
    play sound ds_sfx_psy
    sug "Не начинай сразу о вас. Попробуй поговорить с ней о чём-нибудь отвлечённом. Так получится, что вы {i}уже{/i} разговариваете."
    vol "Она будет настроена к тебе враждебно. Лучше просто пройди мимо."
    enc "Как? И упустить такой шанс узнать ценную информацию? Тебе нужно поговорить с ней - так мы сможем заполучить её назад."
    play sound ds_sfx_int
    lgc "А что она вообще забыла {i}тут{/i}? В твоём мире-то."
    window hide
    menu:
        "Поздороваться":
            window show
            me "П-привет..."
            dv "Привет..."
            play sound ds_sfx_psy
            emp "Она говорит с плохо скрываемым неудовольствием."
            me "И это всё?"
            dv "Ну ладно, привет тебе!"
            me "Ты как?"
            dv "У меня всё хорошо. Во всём. Я пришла к восхитительному периоду в моей жизни."
            dv "А ты как?"
            window hide
            menu:
                "Не очень":
                    window show
                    me "Не очень... всё плохо."
                    show dvw smile at center with dspr
                    dv "Не говори так, Семён. Ты должен быть счастлив. Слышишь: должен! И ты будешь... когда-нибудь."
                "Я скучаю":
                    window show
                    me "Это всё в моей голове. Я скучаю по тебе."
                    show dvw rage at center with dspr
                    dv "Я тоже. Все мы в своих головах! Ты о чём вообще говоришь?!"
                    me "А ты скучала?"
                    show dvw normal at center with dspr
                    dv "Только иногда... Много времени прошло уже. Больше, чем можно представить."
                    "Она смотрит себе под ноги. Избегает зрительного контакта с тобой."
                "Великолепно":
                    window show
                    me "Всё просто великолепно!"
                    show dvw laugh at center with dspr
                    dv "Да кому ты врёшь! Великолепно всё у него..."
            play sound ds_sfx_psy
            ine "Об этом тебя и предупреждали..."
        "Нужно поговорить":
            window show
        "Уйти":
            window show
            play sound ds_sfx_psy
            vol "Но ты {i}не можешь{/i} уйти. Какая-то сила тебя не отпускает от неё. Прости."
    window show
    me "Нам {i}нужно{/i} поговорить!"
    show dvw rage at center with dspr
    dv "О чём нам разговаривать? Мы всё уже обсудили ранее..."
    dv "И вообще, мне надо ехать. Уехать отсюда навсегда!"
    show dvw normal at center with dspr
    dv "Слушай. Мы уже выбрали все темы для разговора."
    dv "Все мыслимые комбинации слов мы использовали. Мы больше не составляем единое целое - больше нет ни «нас», ни наших детей."
    dv "Всё прошло, и мне нужно уезжать. А ты останешься один - навеки."
    play sound ds_sfx_mot
    svf "Не пытайся её поцеловать {i}сейчас{/i}. Ты слишком на нервах из-за услышанного."
    me "Но... разве так должно быть?"
    dv "Нет, конечно... но..."
    me "Что? Есть что-то хорошее?"
    "Она смотрит вниз."
    dv "Я не знаю, зачем сказала это «но». Нет никаких «но»!"
    me "Это всё?"
    show dvw rage at center with dspr
    dv "Да, это всё! Переживёшь ты это, как пережила я, как пережили все остальные!"
    me "Мне кажется, ты не совсем Алиса..."
    dv "Что ты несёшь?!"
    window hide
    menu:
        "Ты..."
        "Бывшая кто-то там":
            window show
            me "Ты, кажется, моя бывшая... кто-то там."
            dv "Значит, я теперь просто бывшая?! Ты меня только запутал!"
            dv "И я пропустила автобус! Ладно, подожду следующего..."
            show dvw normal at center with dspr
            ine "А мы все тебя предупреждали..."
            th "Все?"
            arb "Да, все."
            lim "{i}Буквально{/i} все. От глубин подсознания до последнего нейрона твоего неокортекса."
            me "Рептильный мозг был прав... не нужно было об этом вспоминать..."
            dv "Я не понимаю, о чём ты..."
        "Мой траур":
            window show
            me "Я в трауре из-за тебя... а ты ведь даже не умерла."
            show dvw rage at center with dspr
            dv "О боже, Семён! Я не желаю от тебя слышать такого! Траур по живой девушке - где это слыхано?!"
            dv "С меня довольно! Я не восьмидесятилетняя бабка, чтобы только вздыхать! Мне семнадцать лет - мне нужно жить!"
            play sound ds_sfx_fys
            pat "Тебе невыносимо больно это слышать. Твоё сердце сжимается от давления."
            "Ты хватаешься за грудь."
            dv "Что за цирк ты устраиваешь?!"
        "Моя жена":
            window show
            me "Ты моя жена!"
            show dvw laugh at center with dspr
            dv "Да как бы нет!"
            me "Но мы... были женаты."
            dv "И это не так! Мы просто были в отношениях. Пожили вместе и разбежались!"
            show dvw normal at center with dspr
            dv "«Ленина 49»... Это было очень давно, миллионы лет назад!"
            enc "Ленина 49 - адрес того дома, где вы жили вместе."
            dv "{i}Тогда{/i} я тебя любила... больше, чем кто-либо когда-либо кого-либо любил!"
            dv "Но это в прошлом. От этого ничего не осталось. Ни детей - ничего! Мы живём в самом холодном мире... где всем плевать!"
            dv "И вообще, мне надо ехать!"
            me "Да что ты всё «ехать» и «ехать»?!"
            dv "Потому что у меня сейчас есть дело даже важнее, чем то, чем была любовь к тебе!"
        "Зло":
            window show
            me "Ты зло! Абсолютное зло! Убийца!"
            show dvw rage at center with dspr
            dv "Да пусть так! Как будто мне очень важно твоё мнение!"
            me "Ты хочешь сказать, что тебе неважно моё мнение?"
            show dvw laugh at center with dspr
            dv "Когда я тебя любила - твоё мнение мне было важнее всякого иного."
            dv "Но это в прошлом. Теперь ты для меня никто. Такой же человек, как и все остальные."
            me "Ты доводишь меня до истерик!"
            dv "Нет, это {i}ты{/i} доводишь себя до истерик!"
        "Просто Алиса":
            window show
            me "А впрочем да. Ты всего лишь Алиса и никто больше."
            show dvw rage at center with dspr
            dv "Да ты определись уже, Алиса я, не Алиса... Может, я там Славя, Лена или вообще Шурик."
            me "А ты не знаешь, кто ты?"
            dv "Конечно же знаю! А вот ты - нет! Хотя должен бы был!"
    show dvw normal at center with dspr
    dv "А впрочем, неважно. Мне надо ехать. Мои друзья ждут меня. Заставлять их ждать нехорошо."
    play sound ds_sfx_psy
    aut "ЧЕГО?! Ей какие-то друзья важнее {i}тебя{/i}?"
    me "Ну, передай привет от меня..."
    dv "Обязательно!.."
    play sound ds_sfx_fys
    ins "Ты вспоминаешь кровать... Множество раз ты задирал покрывало. То, что ты видел, тебя успокаивало, всегда успокаивало и делало приятно."
    play sound ds_sfx_int
    con "В своих фантазиях ты по-прежнему единственный мужчина, имеющий туда доступ."
    sug "Теперь попробуй... пора."
    window hide
    menu:
        "Поцеловать":
            $ skillcheck('suggestion', lvl_medium)
            window show
            show dvw normal:
                xalign 0.5 yalign 0.5
                linear 0.5 zoom 120
            sug "Трясущимися ногами ты пододвигаешься ближе к ней. Её тело приближается к тебе. Такое тёплое... Закрыв глаза, ты тянешься своим ртом к её губам."
            sug "Вот ты соприкасаешься... но она не отвечает."
            per_sme "Ты можешь почувствовать её запах... такой приятный."
            per_tas "Ты можешь почувствовать вкус её губ... сладкий как ничто иное."
            per_toc "Ты чувствуешь теплоту, излучаемую ею, её дыхание."
            emp "Но ты не чувствуешь любви."
            me "Ты... не отвечаешь..."
            "Этот момент кончается. Она отводит своё лицо от тебя."
            show dvw normal:
                xalign 0.5 yalign 0.5
                zoom 120
                linear 0.5 zoom 100
            "Она старается на тебя не смотреть."
            sug "Ты должен меня придушить. Нет слов, чтобы описать, как я тебя подвёл..."
            me "Но... почему?"
            dv "Ты зачем себе врёшь, Семён? Ты же знаешь - я не изменяю. Никогда!"
        "Не целовать":
            window show
    me "И это всё?"
    show dvw smile at center with dspr
    dv "Нет. Ты должен знать кое о чём ещё."
    dv "Я беременна..."
    me "От меня?"
    show dvw rage at center with dspr
    dv "Нет, конечно! От тебя я аборт сделала! Как ты мог это забыть?!"
    dv "Давай дальше! Спрашивай ещё! Мало же поговорили, надо ещё!"
    me "И что, это всё?"
    show dvw normal at center with dspr
    dv "Наверное, да."
    pat "Это надо заканчивать."
    vol "Нет, спрашивай ещё!"
    window hide
    menu:
        "Продолжать":
            window show
            me "Не уходи..."
            dv "А с чего бы мне не уходить?"
            dv "Слушай, мне надо ехать. Я уже пропустила один рейс, не хочу пропустить ещё один."
            aut "Но она просила, чтобы ты её не отпускал. Напомни об этом!"
            me "Но ты же требовала... чтобы я тебя не отпускал..."
            dv "Это была другая я... Теперь это не та девушка... Я заменила её."
            me "А ты не можешь вернуть {i}ту{/i} себя?"
            show dvw rage at center with dspr
            dv "Нет... ты убил ту меня!"
            dv "Раньше, когда мы встретились, ты был крут..."
            dv "Я {i}хотела{/i} тебя, я гордилась тобой!"
            dv "Но потом... я не потянула то, что с тобой стало потом."
            dv "Моя любовь к тебе... убывала, пока не исчезла совсем."
            dv "И тебе придётся жить с этим!"
        "Попрощаться":
            window show
            me "Прощай..."
    show dvw normal at center with dspr
    dv "А теперь мне точно пора."
    if ds_know_face:
        show piw normal at right with dissolve
        play sound ds_sfx_mot
        res "А это кто?"
        dv "Познакомься... Это мой новый мужчина."
        me "Ты нашла мне... замену?"
        show dvw smile at center with dspr
        dv "Я нашла себе лучшую версию тебя."
        dv "Он, я уверена, меня не предаст. У нас всё будет хорошо."
        "К остановке подъезжает автобус."
        hide dvw with dissolve
        hide piw with dissolve
        "Алиса и тот парень заходят в него вместе."
    else:
        "К остановке подъезжает автобус."
        hide dvw with dissolve
        "Алиса заходит в него."
    play sound sfx_bus_honk
    scene bg black
    with dissolve2
    stop music fadeout 5
    $ renpy.pause(5.0)
    jump ds_day3_morning
