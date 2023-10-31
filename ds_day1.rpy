# DISCO SOVENOK
# ОБЩИЙ РУТ. ДЕНЬ 1
init:
    $ mods["disco_sovenok"] = u"Disco Sovenok"

    $ ds_ran = False
    $ ds_cry = False
    $ ds_beat_sl = False
    $ ds_ran_from_un = False
    $ ds_beat_dv = False
    $ ds_fake_name = False
    $ ds_accept_el = False
    $ ds_play_football = False
    $ ds_caught_us = False
    $ ds_betray_dv = False
    $ ds_sl_beach_invite = False
    $ ds_sl_keys = False
    $ ds_some_key = False
    $ ds_no_sl_dinner = False
    $ ds_dinner_dv = False
    $ ds_sl_distracted = False
    $ ds_know_novel_content = False
    $ ds_get_novel_content_failed = False
    $ ds_rude_mt = False
    $ ds_keys_return = False

label ds_day1:
    $ backdrop = "days"
    $ new_chapter(1, u"Disco Sovenok. День 1.")
    $ save_name = u"Disco Sovenok. Общий рут. День 1."
    $ day_time()
    $ meet('me', u"Ты")

    scene bg black

    play music music_list["no_tresspassing"] fadein 0

    $ renpy.pause(2)

    $ persistent.sprite_time = "day"

    show blink
    scene bg int_bus

    hide blink
    show unblink

    window show

    "В глаза тебе ударяет яркий солнечный свет."
    res "Но подожди... {w}мы же уезжали в ночь!"
    "Ты оглядываешь автобус... "
    play sound ds_sfx_mot
    per_eye "И не видишь двери! И автобус какой-то другой..."
    if skillcheck('encyclopedia', lvl_easy, passive=True):
        play sound ds_sfx_int
        enc "{result}Это самый настоящий Икарус!"
    th "Как?..{w} Что?.. {w} Я всё-таки умер?"
    th "Или меня похитили?"

    play sound sfx_punch_medium
    with vpunch

    "Ты лихорадочно щупаешь своё тело и бьёшь себя по щекам, и даже сильно прикладываешься лбом о спинку одного из кресел..."
    play sound ds_sfx_fys
    pat "Больно!"
    th "Но это значит, что я жив! Или же в загробном мире все чувства сохраняются..."
    th "Но как такое могло произойти?"
    th "Может быть, я проспал слишком долго, и меня увезли в депо?"
    play sound ds_sfx_int
    lgc "Ага, и пересадили на другой автобус..."
    window hide

    scene cg ds_day1_bus_exit
    with dissolve

    $ renpy.pause(0.5, hard=True)

    scene bg ext_camp_entrance_day
    with dspr

    $ renpy.pause(0.5, hard=True)

    scene bg ext_bus
    with dspr

    window show
    "Ты выскакиваешь на улицу и оглядываешься. {w}Везде буйство зелёного цвета: трава на обочине дороги, деревья, цветы..."
    th "Лето! {w}Но как же так? {w}Только что была зима!"
    play sound ds_sfx_fys
    pat "У тебя нестерпимо болит голова, словно готова взорваться."
    if skillcheck('inland_empire', lvl_easy, passive=True):
        play sound ds_sfx_psy
        ine "{result}А тут поспевают и воспоминания..."

        window hide

        scene anim intro_14 
        with fade2

        play sound sfx_intro_bus_transition

        $ renpy.pause(3, hard=True)
        scene anim intro_15 
        with fade
        $ renpy.pause(3, hard=True)

        play ambience ambience_day_countryside_ambience fadein 5

        scene anim intro_16 
        with fade
        $ renpy.pause(3)

        window show

        play sound ds_sfx_psy
        ine "У тебя в сознании проявляются какие-то образы: длинная дорога, леса, степи, поля, озёра, вновь леса..."
        th "Хотя я и спал, но всё же запомнил всё это..."
        ine "А потом какая-то девушка склонилась над тобой... {w}нежно нашёптывая на ухо."

        stop ambience fadeout 3
        window hide

        $ renpy.pause(2)

        $ persistent.sprite_time = "day"
        scene bg ext_bus 
        with fade2

        window show

        ine "И ты очнулся здесь."
        th "Что же это была за странная девушка?"
        th "Или это всё сон?"
        play sound ds_sfx_psy
        vol "Почему-то от воспоминаний о ней тебе становится спокойнее. Некое приятное тепло расходится по всему телу."
        play sound ds_sfx_int
        lgc "Может, это она привезла тебя сюда? {w}Тогда её надо найти!"
    play sound ds_sfx_fys
    hfl "Но отсюда исходит какая-то угроза... Тебе нужно бежать, спасаться!"
    "Ты дёргаешься в разные стороны, затем останавливаешься в нерешительности..."
    window hide
    menu:
        "Бежать":
            window show
            $ ds_ran = True
            $ ds_semtype -= 1
            stop music fadeout 3

            "..."
            window hide

            scene bg ext_road_day:
                zoom 1.05 anchor (48,27)
                ease 0.20 pos (0, 0)
                ease 0.20 pos (25,25)
                ease 0.20 pos (0, 0)
                ease 0.20 pos (-25,25)
                repeat
            with dspr

            play ambience ambience_ext_road_day fadein 3

            $ renpy.pause(3)
            scene bg ext_road_day
            window show
            "..."
            "Физические упражнения освежают мозг, мысли проясняются, становится легче оценивать окружающую действительность."
            play sound ds_sfx_fys
            edr "Впрочем, это все совершенно не про тебя – ты сидишь на обочине дороги, хрипя и пытаясь жадными глотками раскаленного воздуха хоть немного успокоить обожженные легкие."
            play sound ds_sfx_psy
            vol "В любом случае пробежка пошла тебе на пользу – страх на некоторое время отступил."
            th "Может, я и правда сплю?.."
            play sound ds_sfx_int
            lgc "Вспомни самоистязания в автобусе."
            me "Я не сплю и не умер..."
            "Вдаль уносится узкая дорога через поле."
            play sound ds_sfx_psy
            ine "Та самая, из твоего сна."
            th "Наверное, я очень далеко от дома."
            play sound ds_sfx_mot
            per_eye "Но тут все какое-то не такое, как в реальной жизни!"
            per_eye "И дело даже не в том, что вчера была зима, а сейчас – самое что ни на есть лето."
            per_eye "Дело в окружающей природе."
            per_eye "Нет, конечно, летом обычно так и бывает – красиво, зелено и жарко"
            per_eye "Но трава – слишком уж сочная, кусты – не такие, какими должны быть кусты – пышные, сквозь них ничего не видно, как кроны деревьев, ей-богу..."
            per_eye "А уж сами деревья...{w} До леса было довольно далеко, но казалось, что они сомкнули свои стройные ряды и только и ждут приказа, чтобы начать наступление на поля и степи."
            "Ты, отдышавшись, смотришь на автобус, который уже почти скрылся из виду."
            th "Неплохо пробежался..."
            play sound ds_sfx_psy
            vol "Страх с новой силой захлёстывает тебя."
            play sound ds_sfx_int
            lgc "Хотя бы эти ЛЭП...{w} Значит, тут есть люди."
            lgc "Хотя что это {i}значит{/i}?"
            lgc "Ведь ровным счетом ничего!{w} Почему в аду не может быть линий электропередач?"
            lgc "Жарить грешников на угле? Прошлый век..."
            "Похоже, ты дошел до той точки невозвращения, когда надо либо уже сходить с ума, либо все-таки попытаться как-то понять, что же с тобой произошло."
            play sound ds_sfx_mot
            com "И пока еще есть возможность, стоит выбрать второй вариант!"
            "Ты медленно направляешься назад к автобусу."
            th "Конечно, страшно, но вряд ли в полях и лесах скрываются какие-либо ответы, а это чертово ведро с гайками все же единственное, что хоть как-то связывает меня с реальным миром."
        "Не бежать":
            window show
            "Ты остаёшься около автобуса. {w}И смотришь вокруг."
            stop music fadeout 3

            "..."
            window hide

            $ persistent.sprite_time = "day"
            scene bg ext_road_day 
            with dissolve2

            play ambience ambience_ext_road_day fadein 3

            window show
            th "Может, я и правда сплю?.."
            lgc "Вспомни самоистязания в автобусе."
            me "Я не сплю и не умер..."
            "Вдаль уносится узкая дорога через поле."
            play sound ds_sfx_psy
            ine "Та самая, из твоего сна."
            th "Наверное, я очень далеко от дома."
            play sound ds_sfx_mot
            per_eye "Но тут все какое-то не такое, как в реальной жизни!"
            per_eye "И дело даже не в том, что вчера была зима, а сейчас – самое что ни на есть лето."
            per_eye "Дело в окружающей природе."
            per_eye "Нет, конечно, летом обычно так и бывает – красиво, зелено и жарко."
            per_eye "Но трава – слишком уж сочная, кусты – не такие, какими должны быть кусты – пышные, сквозь них ничего не видно, как кроны деревьев, ей-богу..."
            per_eye "А уж сами деревья...{w} До леса было довольно далеко, но казалось, что они сомкнули свои стройные ряды и только и ждут приказа, чтобы начать наступление на поля и степи."
            play sound ds_sfx_psy
            vol "Страх с новой силой захлёстывает тебя."
            play sound ds_sfx_int
            lgc "Хотя бы эти ЛЭП...{w} Значит, тут есть люди."
            lgc "Хотя что это {i}значит{/i}?"
            lgc "Ведь ровным счетом ничего!{w} Почему в аду не может быть линий электропередач?"
            lgc "Жарить грешников на угле? Прошлый век..."
            "Похоже, ты дошел до той точки невозвращения, когда надо либо уже сходить с ума, либо все-таки попытаться как-то понять, что же с тобой произошло."
            play sound ds_sfx_mot
            com "И пока еще есть возможность, стоит выбрать второй вариант!"

    scene bg ext_camp_entrance_day
    with dissolve2

    window show
    play sound ds_sfx_mot
    per_eye "Ты приглядываешься к местности повнимательнее."
    per_eye "Перед тобой кирпичная ограда с воротами, над которыми красуется надпись «Совёнок»."
    per_eye "По бокам стоят статуи пионеров, а рядом на вывеске написан номер маршрута – «410»."
    me "Сегодня рейс что-то затянулся."
    play sound ds_sfx_int
    enc "Когда-то тебе доводилось слышать, что человек, попав в экстремальную ситуацию, иногда начинает вести себя неадекватно."
    th "Возможно, сейчас со мной происходит что-то подобное."
    per_eye "Место кажется совсем не заброшенным – ворота не заржавели, кладка не осыпалась."
    me "«Совёнок»…"
    th "Что может так называться?"
    if skillcheck('logic', lvl_trivial, passive=True):
        play sound ds_sfx_int
        lgc "{result}Судя по статуям пионеров, наверное, детский лагерь.{w} Причем лагерь действующий."
        lgc "Но это самое простое объяснение, которое при этом ничего не объясняет."
    th "Незнакомка, изменившийся автобус, лето, пионерлагерь..."
    play sound ds_sfx_psy
    ine "В голове за долю секунды проносятся тысячи теорий – от похищения инопланетянами до летаргического сна, от галлюцинаций до сдвига пространства и времени…"
    play sound ds_sfx_int
    vic "Ни одна из них не хуже другой, но в то же время при ближайшем рассмотрении не выдерживает никакой критики."
    if skillcheck('interfacing', lvl_trivial, passive=True):
        play sound ds_sfx_mot
        inf "{result}А почему бы тебе не позвонить?!"
        window hide
        menu:
            "Попробовать":
                window show
                inf "Ты достаёшь мобильник и набираешь первый попавшийся номер из телефонной книги."
                $ ds_skill_points['interfacing'] += 1
                window hide
                play sound sfx_cellular_phone_error fadein 0

                $ renpy.pause(3)

                window show
                inf "Однако спустя пару секунд понимаешь, что вместо палочек приема на экране горит жирный крест."
                th "Ладно, возможно, в такой глуши связи нет."
            "Забить":
                window show
    play sound ds_sfx_int
    lgc "Но не мог же ты сюда попасть один!"
    lgc "Автобусы ведь сами по себе не ездят!"
    window hide

    scene bg ext_bus 
    with dissolve

    menu:
        "Обойти автобус":
            window show
            "Ты решаешь обойти его и убедиться, что все это тебе не кажется."
            play sound ds_sfx_mot
            per_eye "Комья грязи на днище, кое-где виднеющаяся ржавчина, выцветшая краска и потертая резина – нет, это определенно самый обычный автобус."
            th "Да, именно такие тебя увозят непонятно куда, если нечаянно заснешь."
            "У тебя вырывается нервный смешок."
            play sound ds_sfx_mot
            com "Именно вырывается. Сам по себе, непроизвольно.{w} Ведь не место и не время шутить..."
            th "Но где же тогда водитель?"
        "{check=interfacing:10}Попытаться уехать на автобусе":
            show bg int_bus with dissolve
            "Ты запрыгиваешь в автобус в водительское кресло..."
            th "Что ж, попробуем куда-нибудь уехать..."
            window hide
            if skillcheck('interfacing', lvl_medium):
                window show
                play sound ds_sfx_mot
                inf "{result}У тебя получается завести мотор - просто повернув ключ!"
                play sound_loop sfx_bus_idle
                me "Поехали!"
                play sound_loop sfx_bus_interior_moving
                "Автобус трогается с места, и ты едешь."
                window hide
                $ renpy.pause(1.0)
                window show
                inf "Но ты же не умеешь водить автобусы!"
                scene bg ds_int_bus_forest with dissolve
                "Ты с ужасом замечаешь, что поехал прямиком в лес."
                scene black with dissolve2
                stop sound_loop fadeout 2
                jump ds_end_bus_crash
            else:
                window show
                play sound ds_sfx_mot
                inf "{result}Но ты не можешь управиться с автобусом!"
                th "Ладно, не судьба..."
                show bg ext_bus with dissolve
                "Ты выходишь из автобуса."
        "Просто ждать":
            window show
    "Ты осторожно садишься на бордюр рядом с автобусом и принимаешься ждать."
    window hide

    with fade2

    window show
    play sound ds_sfx_psy
    vol "Однако, хватает тебя ненадолго."
    vol "Кажется, твоё волнение достигло пика, и ты потихоньку начинаешь сходить с ума."
    "Наверное, в подобной ситуации любой человек испытывал бы что-то подобное."
    play sound ds_sfx_mot
    com "Ты уже и думать забыл про инопланетян и параллельные реальности, тебя просто трясёт, а в голове пустота и мрак."
    window hide

    with flash

    window show
    th "Неужели все так и закончится? Моя жизнь – закончится?"
    th "Ведь я столько всего хотел сделать, столько не успел..."
    window hide
    menu:
        "{check=composure:10}Попытаться удержать себя в руках":
            if skillcheck('composure', lvl_medium):
                window show
                com "{result}Тебе удаётся удержать себя в руках."
                $ ds_skill_points['composure'] += 1
                jump ds_day1_approach
            else:
                window show
                $ ds_skill_points['composure'] += 1
                сom "{result}Тебя охватывает уверенность, что это конец."
            $ ds_semtype += 1
        "Начать истерить":
            window show
            $ ds_semtype -= 1
            com "Тебя охватывает уверенность, что это конец."
    th "Но почему?!"
    th "Это несправедливо! Неужели я хуже других?!"
    th "Господи, за что?.."
    window hide

    show blink  with dissolve
    $ renpy.pause(3)
    hide blink 
    show unblink 

    $ renpy.pause(3)
    window show

    play sound ds_sfx_fys
    pat "Слезы нестерпимо жгут глаза"
    com "Ты сворачиваешься калачиком и начинаешь кататься по траве."
    $ ds_cry = True

    hide unblink 

    me "ЗА ЧТО?! ПОЧЕМУ?! ПОЧЕМУ Я?!"
    $ ds_damage_morale()
    "Но твои крики слышат лишь безмолвные статуи пионеров да свесившаяся с ветки птица, лениво таращащаяся на какого-то идиота, посмевшего нарушить ее послеобеденный сон."
    "Ты окончательно захлебнулся рыданиями и просто тихо лежишь, изредка поскуливая."
    "..."
    window hide

    with fade2

    window show
    com "Через несколько минут тебе удаётся все-таки взять себя в руки."
    jump ds_day1_approach

label ds_day1_approach:
    play sound ds_sfx_psy
    vol "В голове немного проясняется, а ужас и страх смерти если не отпустили, то как будто сделали передышку."
    play sound ds_sfx_int
    lgc "В конце концов, если бы тебя хотели убить, давно бы это сделали!"
    th "На опыты это тоже мало похоже."
    th "Если это какое-то чудовищное совпадение, то, возможно, оно не несет в себе угрозы."
    th "Как бы там ни было, пока что, кажется, нет никакой опасности."
    play sound ds_sfx_mot
    com "Ты более-менее успокаиваешься, насколько это возможно в твоём положении."
    play sound ds_sfx_fys
    pat "Бой в висках и дрожание рук никуда не ушли"
    com "Но теперь, по крайней мере, появилась возможность трезво соображать."
    th "Сейчас от меня все равно ничего не зависит!{w} Поэтому я могу сколько угодно думать, накручивать себя – от этого ничего не изменится."
    lgc "Пока не появятся какие-нибудь факты…"
    window hide

    scene bg ext_camp_entrance_day 
    with dissolve

    window show
    lgc "В любом случае, околачиваясь здесь, ты ничего не узнаешь."
    lgc "Судя по всему, этот лагерь (если это, конечно, лагерь) - единственное место, где могут быть люди, поэтому тебе следует пойти туда"
    if skillcheck('half_light', lvl_medium, passive=True):
        play sound ds_sfx_fys
        hfl "{result}Сюда кто-то идёт! Лучше спрячься!"
        window hide
        menu:
            "Пойти":
                window show
                $ ds_semtype += 1
                "Ты уже почти дошел до ворот, как..."
            "Ждать":
                $ renpy.pause(1)
                window show
            "Спрятаться":
                window show
                "Ты прячешься за ближайшей статуей."
                $ ds_skill_points['half_light'] += 1
                scene cg ds_day1_hide with dissolve
                "Из ворот выходит девочка. Она одета в пионерскую форму."
                slp "И где он спрятался?"
                window hide
                menu:
                    "Вылезти":
                        window show
                        scene bg ext_camp_entrance_day 
                        with dissolve
                        show sl surprise pioneer at center with dissolve
                        play music ds_sl_theme
                        "Ты вылезаешь и здороваешься с ней."
                        me "Привет..."
                        $ ds_met['sl'] = 1
                        jump ds_day1_sl_dialogue
                    "Ждать дальше":
                        $ renpy.pause(1.0)
                        window show
                        slp "Ну ладно, не приехал, наверное..."
                        "И девочка уходит."
                        "Только теперь ты вылезаешь и заходишь вслед за ней в ворота."
                        jump ds_day1_entered
    else:
        window hide
        menu:
            "Пойти":
                window show
                $ ds_semtype += 1
                "Ты уже почти дошел до ворот, как..."
            "Не идти":
                $ renpy.pause(1)
                window show
        "Оттуда выглядывает девочка..."

    play music ds_sl_theme
    show sl normal pioneer far at center    with dissolve
    $ ds_met['sl'] = 1
    "Она была одета в пионерскую форму."
    th "Логика меня не подвела."
    lgc "Спасибо за комплимент!"
    play sound ds_sfx_int
    vic "Впрочем, пионерская форма в XXI веке…"
    vic "Впрочем, девочки {i}здесь{/i}..."
    play sound ds_sfx_mot
    com "Ты застываешь на месте не в силах сделать ни шагу."
    play sound ds_sfx_fys
    hfl "Очень хочется убежать.{w} Подальше отсюда, подальше от этого автобуса, ворот, статуй, подальше от этой чертовой птицы с ее сиестой."
    hfl "Просто бежать, бежать свободно, словно ветер, бежать все быстрее, маша рукой пролетающим мимо планетам, подмигивая галактикам."
    hfl "Бежать, став лучом пульсара, превратившись в реликтовое излучение, бежать навстречу неизвестности."
    hfl "Бежать куда угодно, но {b}подальше{/b} отсюда!"
    show sl smile pioneer at center   with dissolve
    "Тем временем девочка подходит к тебе и улыбается."
    jump ds_day1_sl_dialogue

label ds_day1_sl_dialogue:
    play sound ds_sfx_int
    con "Она красива, даже страх не мешает тебе это отметить."
    play sound ds_sfx_fys
    ins "Человеческие инстинкты работают вопреки сознанию, и если только 5%% мозга отвечают за мыслительную деятельность, то остальные 95 всегда заняты поддержанием {i}жизне{/i}деятельности, в том числе и обеспечивают стабильное функционирование гормональной системы."
    con "Приятное славянское лицо, длинные косы, похожие на две толстые охапки свежескошенного сена, и голубые глаза, в которых, казалось, можно было утонуть."
    slp "Привет, наверное, только что приехал?"
    window hide

    menu:
        "Не отвечать ей":
            $ ds_karma -= 5
            window show
            com "Ты делаешь вид, будто её совсем нет. {w}Ну, или пытаешься."
            show sl normal pioneer at center   with dspr
            slp "Чего молчишь?"
            com "Ты всё ещё ничего не отвечаешь."
            play sound ds_sfx_psy
            emp "Ты её этим немного пугаешь."
            $ renpy.pause(1)
            slp "Ладно, наверное, сильно перенервничал."
            slp "В общем, тебе к вожатой надо сразу, она все расскажет!"
            slp "Смотри.{w} Сейчас идешь прямо-прямо, доходишь до площади, затем сворачиваешь налево, дальше будут палатки."
            "Она показала в сторону ворот."
            slp "Ну спросишь у кого-нибудь, где домик Ольги Дмитриевны!"
            slp "А мне пора."
            hide sl  with dissolve
            "Девочка помахала мне рукой и скрылась за воротами."
            emp "Кажется, ты для нее что-то такое...{w} нормальное."
        "{check=volition:8}Ответить":
            if skillcheck('volition', lvl_easy):
                window show
                play sound ds_sfx_psy
                vol "{result}Ответь спокойно. Решительно."
                me "Да, я новенький."
            else:
                window show
                play sound ds_sfx_psy
                vol "{result}Тебе тяжело говорить от страха. Запинаясь, ты произносишь..."
                me "Ну… да…"
            $ ds_skill_points['volition'] += 1
            $ ds_lp['sl'] += 1
            show sl smile2 pioneer at center   with dspr
            slp "Что же, добро пожаловать!"
            "Она широко улыбнулась."
            vic "И все же перед тобой как будто совершенно обычная девочка."
            if ds_ran:
                th "Эх, не стоило вообще сюда возвращаться – лучше уж в леса, в поля..."
            vol "Необходимо решить, что делать дальше – попытаться общаться с ней как с человеком, бежать или еще что-то..."
            edr "В голове невыносимо стучит кровь, словно намеревающаяся взорвать ее изнутри и забрызгать бедную девочку неприглядным содержимым моей черепной коробки."
            show sl normal pioneer at center   with dspr
            slp "Что смешного?"
            "Девочка окинула меня взглядом с ног до головы."
            "По спине побежали мурашки, а колени начали подкашиваться."
            me "Н... ничего..."
            show sl smile pioneer at center   with dspr
            slp "Ну и славно."
            th "Славно? Что тут может быть славного?"
            "Я еще раз внимательно осмотрел ее."
            "Внезапно захотелось плюнуть на все, забыть о стоящем сзади автобусе, вчерашней зиме и будущем лете, скинуть чесоточный свитер и просто поверить, что все это на самом деле, что так и надо, что так и должно быть, что все это, в конце концов, к лучшему..."
            me "А ты, наверное, знаешь…"
            show sl normal pioneer at center   with dspr
            slp "Тебе к вожатой надо сразу, она все расскажет!"
            slp "Смотри.{w} Сейчас идешь прямо-прямо, доходишь до площади, затем сворачиваешь налево, дальше будут палатки."
            "Она показала в сторону ворот, как будто я знал, что за ними."
            slp "Ну спросишь у кого-нибудь, где домик Ольги Дмитриевны!"
            me "Я… эээ…"
            slp "Надеюсь, все понял?"
            com "Естественно, ничего ты не понял."
            window show
            menu:
                "Да, понял":
                    window show
                    me "Ну да, я всё понял!"
                    $ ds_semtype += 1
                "Нет, не понял":
                    window show
                    me "Не-а, я ничего не понял..."
                    "Но она тебя не слышит."
                "Промолчать":
                    window show
                    $ ds_semtype -= 1
            slp "А мне пора."
            hide sl  with dissolve
            "Девочка помахала мне рукой и скрылась за воротами."
            emp "Кажется, ты для нее что-то такое...{w} нормальное."
            "И весь этот цирк с автобусом, путешествиями во сне и наяву волнует только меня, а здесь все так, как и должно быть."
        "Проследовать в ворота":
            $ ds_karma -= 5
            $ ds_lp['sl'] -= 1
            window show
            $ ds_semtype += 1
            com "Ты решительно идёшь в ворота, совершенно не замечая девочки."
            show sl scared pioneer close at center with dspr
            slp "Ты чего?"
            play sound ds_sfx_psy
            emp "Она явно не то удивлена, не то напугана таким поворотом."
            play sound ds_sfx_mot
            svf "А ещё она заблокировала проход собой, так что просто пройти не выйдет... разве что толкнуть её."
            window hide
            menu:
                "Послушать её":
                    window show
                    show sl normal pioneer close at center with dspr
                "{check=physical_instrument:8}Толкнуть её":
                    $ ds_beat_sl = True
                    if skillcheck('physical_instrument', lvl_easy):
                        window show
                        phi "{result}Ты её отталкиваешь как пушинку."
                        show sl angry pioneer close at left with dspr
                        slp "Да что с тобой не так-то?!"
                        $ ds_karma -= 20
                        $ ds_lp['sl'] -= 2
                        $ ds_lp['dv'] -= 1
                        $ ds_lp['us'] -= 1
                        $ ds_lp['mi'] -= 1
                        $ ds_lp['mt'] -= 1
                        $ ds_lp['mz'] -= 1
                        $ ds_lp['el'] -= 1
                        emp "Ты её определённо разозлил своим поведением. Зачем, собственно?"
                        $ renpy.pause(1)
                        show sl normal pioneer at left with dspr
                        emp "Однако, она собирается и всё-таки решает назло тебе сказать то, что хотела."
                    else:
                        window show
                        phi "{result}Однако, толчок получается слабеньким, она даже не пошевелилась."
                        slp "Что это было?"
                        $ ds_karma -= 10
                        show sl normal pioneer at left with dspr
                        emp "Однако, она всё-таки собирается тебе сказать то, что хотела."
            slp "В общем, тебе к вожатой надо сразу, она все расскажет!"
            slp "Смотри.{w} Сейчас идешь прямо-прямо, доходишь до площади, затем сворачиваешь налево, дальше будут палатки."
            slp "Ну спросишь у кого-нибудь, где домик Ольги Дмитриевны!"
            show sl normal pioneer at left with dspr
            "Наконец, она уступает тебе проход, и ты входишь в ворота."
            hide sl with dissolve
            "Она остаётся за тобой."

    stop music fadeout 2
    th "Вожатая, пионерская форма…"
    th "Они что, здесь устроили историческую реконструкцию?"
    th "Надеюсь, на этой площади я не увижу Ленина на броневике?"
    th "Хотя сейчас меня и это не удивит…"

    stop ambience fadeout 2

    "Ты направляешься по указанному девочкой маршруту, ибо других альтернатив все равно не предвидится."
    window hide
    jump ds_day1_entered

label ds_day1_entered:
    scene bg ext_clubs_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 5

    window show
    "Буквально через 50 метров слева словно из-под земли вырастает небольшое одноэтажное здание.{w} Вывеска рядом с дверью гласит «Клубы»."
    play sound ds_sfx_mot
    per_eye "Ниже что-то написано неразборчивым почерком."
    window hide
    menu:
        "{check=perception:8}Вчитаться в написанное":
            if skillcheck('perception', lvl_easy):
                window show
                $ ds_skill_points['perception'] += 1
                per_eye "{result}Ниже всего лишь список имеющихся тут клубов."
                per_eye "ШАШКИ"
                per_eye "ЗНАТОКИ"
                per_eye "И внизу приписано: КИБЕРНЕТИКИ"
                per_eye "Это точно то, что тебе так нужно было знать?"
            else:
                window show
                $ ds_skill_points['perception'] += 1
                per_eye "{result}Как бы ты ни вглядывался, ничего разобрать не можешь... да и нужно ли?"
        "Забить":
            window show
    stop music fadeout 5

    "Ты уже собираешься подойти поближе..."

    play sound sfx_open_door_clubs fadein 0

    show un normal pioneer far at left   with dissolve
    $ ds_met['un'] = 1   
    "Как дверь открывается, и оттуда выходит девочка в пионерской форме."
    "Она невысокого роста с довольно странной прической из четырех хвостиков."
    play sound ds_sfx_psy
    emp "Лицо ее, кажется, выражает просто-таки вселенскую грусть и муку за судьбы всего человечества"
    play sound ds_sfx_int
    con "Но при этом весьма красиво."
    "Девочка останавливается и оборачивается в твою сторону."
    show un surprise pioneer far at left   with dspr
    play sound ds_sfx_psy
    vol "Ты застыл на месте, думая, как лучше поступить – подойти первым или подождать, пока она сама проявит инициативу."
    play sound ds_sfx_fys
    hfl "Или все же побежишь?.."
    hfl "От тебя на данный момент мало что зависит и если этот мир захочет тебя убить, то сделает это."
    hfl "И не в твоих силах ему помешать..."
    window hide
    menu:
        "Подойти к ней":
            window show
            "Ты уже собираешься было подойти к ней..."
            $ ds_semtype += 1
        "Побежать":
            window show
            "Ты сбегаешь отсюда в глубь этого места."
            $ ds_semtype -= 1
            $ ds_lp['un'] -= 1
            $ ds_ran_from_un = True
            jump ds_day1_inside_camp
        "Подождать":
            window show

    play music music_list["i_want_to_play"] fadein 5

    show us grin sport far at right   with dissolve 
    $ ds_met['us'] = 1
    play sound sfx_bush_leaves fadein 0

    "Неожиданно из соседних кустов выскакивает другая девочка..."
    "Она одета в футболку с надписью «СССР»."
    play sound ds_sfx_int
    enc "Как точно соблюден антураж эпохи."
    "Девочка издалека казалась совсем маленькой и, наверное, по возрасту была младше первых двух встреченных мной."
    show un surprise pioneer far at left   with dspr
    show us surp3 sport far at right   with dspr:
        linear 1.0 xalign 0.28
    play sound ds_sfx_int
    con "Будем звать её «СССР» пока что."
    "Ты решаешь все-таки подойти, как вдруг «СССР» подскакивает к первой девочке и начинает что-то говорить, при этом яростно размахивая руками."
    show un shy pioneer far at left   with dspr
    "Та же, в свою очередь, потупила взгляд и ничего не ответила."
    emp "Видимо, смутилась."
    "Ты бы, наверное, так и наблюдал их занимательный диалог, если бы «СССР» вдруг не достала что-то из кармана и не начала трясти им перед лицом первой девочки."
    window hide

    scene cg ds_day1_grasshopper_f1
    $ renpy.pause(0.1, hard=True)
    scene cg ds_day1_grasshopper_f2
    $ renpy.pause(0.1, hard=True)
    scene cg ds_day1_grasshopper_f3

    if skillcheck('perception', lvl_trivial, passive=True):
        window show
        play sound ds_sfx_mot
        per_eye "{result}Это кузнечик."
    window show
    play sound ds_un_scream
    unp "Ииииии-иии-иииииии!"
    "Она моментально убегает в сторону, где, по идее, Ленин когда-то читал речь о свершившейся рабоче-крестьянской революции."
    "Ну, то есть в сторону площади…"
    play sound ds_sfx_int
    lgc "Видимо, она не очень любит насекомых."

    scene bg ext_clubs_day 
    show us grin sport at left   with dspr:
        linear 2.0 xalign 2.0
    with dissolve

    "«СССР» смотрит на тебя, хитро улыбается и бежит за ней."
    hide us  with dissolve
    th "Неплохое начало дня."
    th "Я совершенно не знаю, где я, да еще тут какие-то дети играют в пионеров."

    stop music fadeout 5

    th "И все это, судя по всему, в тысячах километров от дома.{w} Или вообще в другой реальности…"
    play sound ds_sfx_int
    vic "И ведь {i}реальности{/i}..."
    vic "То есть все кажется настолько реальным (хоть и несколько приукрашенным), что ты уже начинаешь иногда забываться, а вдруг вся твоя жизнь до этого – всего лишь сон..."
    th "И что теперь делать?"
    "..."
    window hide

    with fade2

    menu:
        "Войти в здание клубов":
            window show
            play sound ds_sfx_mot
            inf "Ты подходишь к двери и пытаешься её открыть."
            play sound sfx_campus_door_rattle
            inf "Но она оказывается заперта!"
            th "Так ведь только что оттуда выходила девушка."
            inf "Вероятно, ты просто не заметил, как она за собой закрыла."
            inf "Или же могли закрыть изнутри."
            th "Ладно..."
            window hide
        "Не подходить":
            pass

    window show
    "Ты ковыряешь носком ботинка трещины в плитах, которыми была вымощена дорожка, и бесцельно смотришь на здание «клубов»."
    play sound ds_sfx_psy
    vol "И все-таки пора что-то решать..."
    if ds_cry:
        "И тут ты вспоминаешь, как катался по траве и рыдал..."
        play sound ds_sfx_mot
        com "Тебя передёргивает от отвращения."
        play sound ds_sfx_int
        enc "Это еще один инстинкт – когда все силы на нытье и жалость к себе израсходованы, организм либо впадает в спячку, либо мобилизует резервы."
        vol "Видимо, твой выбрал второй вариант, потому что откуда ни возьмись появилась решимость понять, что же здесь происходит, и, насколько это вообще возможно, вести себя по-мужски, да просто по-человечески – не ронять в грязь лицом достоинство представителя {i}моего мира{/i}."
    else:
        vol "Откуда ни возьмись появилась решимость понять, что же здесь происходит, и, насколько это вообще возможно, вести себя по-мужски, да просто по-человечески – не ронять в грязь лицом достоинство представителя {i}моего мира{/i}."
    window hide
    jump ds_day1_inside_camp

label ds_day1_inside_camp:
    scene bg ext_houses_day 
    with dissolve
    window show
    "Ты идёшь по дорожке, слева и справа стояли небольшие домики"
    play sound ds_sfx_int
    lgc "По-видимому, палатки местных пионеров."
    "В принципе, снаружи они выглядят довольно уютно."
    play sound ds_sfx_int
    enc "Ты сам, хоть и родился в Советском Союзе, никогда не был ни пионером, ни даже октябренком."
    enc "И представлял себе быт обычного пионерлагеря несколько по-другому: огромные бараки с рядами железных коек, подъем в 6 утра по сирене, одна минута на то, чтобы заправить кровать, затем построение на плацу…"
    th "Стоп!{w} Или я что-то с чем-то путаю…"

    play sound sfx_punch_medium
    with vpunch
    play sound ds_sfx_mot
    per_toc "Из этих мыслей тебя выводит удар по спине."
    play sound ds_sfx_fys
    pat "Довольно сильный, попрошу заметить."
    play sound ds_sfx_mot
    cor "Ты пошатнулся, но устоял на ногах."
    play sound ds_sfx_fys
    hfl "Вот оно, началось – не может быть все так просто"
    "Ты развернулся и уже приготовился стать героем, спасая свою жизнь..."
    show dv angry pioneer2 at center   with dissolve
    $ ds_met['dv'] = 1
    "Но перед тобой стоит всего лишь еще одна девочка."
    play sound ds_sfx_mot
    res "От удивления ты открыл рот."
    dvp "Челюсть с пола подними."
    "Ты послушно закрыл рот."
    "Она была тоже одета в пионерскую форму."
    play sound ds_sfx_fys
    ins "Однако на ней она сидит вызывающе…"
    play sound ds_sfx_int
    con "Как и все предыдущие девочки, которых ты встретил здесь, эта весьма симпатична, но лицо ее кажется слишком надменным."
    play sound ds_sfx_int
    vic "Также тебя удивила ее довольно странной формы прическа."
    dvp "Новенький, значит?"
    window hide
    menu:
        "{check=physical_instrument:11}Ударить в ответ":
            $ ds_beat_dv = True
            $ ds_lp['dv'] -= 3
            if skillcheck('physical_instrument', lvl_up_medium):
                window show
                play sound ds_sfx_fys
                phi "{result}Ты замахиваешься кулаком и наносишь удар по её лицу."
                $ ds_skill_points['physical_instrument'] += 1
                "Но ей удаётся удержаться на ногах."
                play sound ds_sfx_psy
                emp "Что ты натворил?! Ей определённо очень неприятно от твоего хода. Она же не со зла ударила тебя."
                $ ds_karma -= 20
                show dv rage pioneer2 at center   with dspr
                emp "Видимо, поэтому она так разозлилась..."
            else:
                window show
                play sound ds_sfx_fys
                phi "{result}Ты пытаешься её ударить... но всё, на что тебя хватает - шлёпнуть её по щеке."
                play sound ds_sfx_psy
                emp "Но она всё равно разозлилась на такой поворот..."
                show dv rage pioneer2 at center   with dspr
                dvp "Мало того, что на девушку руку поднимаешь... {w}даже ударить нормально не можешь!"
                $ ds_karma -= 20
                $ ds_damage_morale()
            dvp "Да пошёл ты!"
            show dv cry pioneer2 at center with dspr
            hide dv with moveoutright
            "И быстро убегает."
            play sound ds_sfx_mot
            per_hea "Кажется, она тихонько всхлипнула."
            $ ds_lp['sl'] -= 2
            $ ds_lp['us'] -= 2
            $ ds_lp['mi'] -= 2
            $ ds_lp['un'] += 1
            $ ds_lp['mt'] -= 1
            $ ds_lp['el'] -= 1
            $ ds_lp['mz'] -= 1
        "Промолчать":
            window show
            $ ds_semtype -= 1
            show dv normal pioneer2 at center   with dspr
            dvp "Ладно, увидимся!"
            "Она как-то злобно улыбнулась одними глазами и прошла мимо тебя."
            hide dv  with dissolve
        "Ответить осторожно":
            window show
            me "Да..."
            show dv normal pioneer2 at center   with dspr
            dvp "Ладно, увидимся!"
            "Она как-то злобно улыбнулась одними глазами и прошла мимо тебя."
            hide dv  with dissolve
        "{check=rhetoric:10}Сделать комплимент":
            if skillcheck('rhetoric', lvl_medium):
                window show
                play sound ds_sfx_int
                rhe "{result}Скажи ей, что у неё красивая причёска, например."
                play sound ds_sfx_int
                con "А она, чёрт возьми, и правда красивая!"
                me "Да... А у тебя красивая причёска, кстати."
                show dv shy pioneer2 at center with dspr
                dvp "Да что ты несёшь?"
                show dv normal pioneer2 at center   with dspr
                dvp "Ладно, увидимся!"
                "Она как-то злобно улыбнулась одними глазами и прошла мимо меня."
                hide dv  with dissolve
                play sound ds_sfx_psy
                emp "На самом деле твой комплимент ей запал в душу. Но почему-то она боится это показать."
                $ ds_lp['dv'] += 2
                $ ds_skill_points['rhetoric'] += 1
            else:
                window show
                rhe "{result}Но у тебя не получается подобрать нужных слов."
                me "Да... А ты такая..."
                show dv angry pioneer2 at center with dspr
                dvp "Какая?"
                "Разозлилась было."
                show dv normal pioneer2 at center   with dspr
                "Но тут она внезапно успокаивается."
                dvp "Ладно, увидимся!"
                "Она как-то злобно улыбнулась одними глазами и прошла мимо меня."
                hide dv  with dissolve
                $ ds_skill_points['rhetoric'] += 1
        "Ответить с юмором":
            window show
            me "Да! А это у вас ритуал встречи такой."
            me "Забавный, надо сказать."
            "И ты начинаешь смеяться."
            $ ds_semtype += 1
            show dv surprise at center with dspr
            "Пионерка несколько смутилась от такого твоего поведения."
            show dv smile pioneer2 at center with dspr
            dvp "А ты, видимо, всё-таки понимаешь шутки."
            dvp "Ладно, увидимся!"
            "Она как-то злобно улыбнулась одними глазами и прошла мимо меня."
            hide dv  with dissolve
            $ ds_lp['dv'] += 1
    play sound ds_sfx_fys
    hfl "Лучше подожди, пока пионерка скроется за поворотом, ибо мало ли что она еще может выкинуть."
    "Самое интересное, что даже эта враждебная девочка кажется мне совершенно нормальной"
    hfl "В ней не ощущается какой-либо смертельной опасности."
    hfl "Разве что страх получить по носу..."
    play sound ds_sfx_psy
    ine "А ещё её лицо кого-то тебе напоминает..."
    ine "А впрочем забудь!"
    window hide

    scene bg ext_square_day 
    with dissolve

    window show
    "Итак, ты все-таки добрался до площади."
    "Ленина с броневиком там не оказалось, хотя после всего случившегося вполне можно было бы ожидать чего-то подобного."
    "Зато в центре возвышается памятник неизвестному мне товарищу."
    play sound ds_sfx_int
    lgc "Наверное, какой-то партийный деятель."
    play sound ds_sfx_mot
    per_eye "Под памятником написано: ГЕНДА."
    play sound ds_sfx_int
    enc "Странно... тебе на ум никаких партийных деятелей с подобной фамилией не приходит..."
    lgc "Возможно, это какой-то местный видный партиец."
    play sound ds_sfx_psy
    ine "Или же ты вообще не в своём мире!"
    "По бокам стоят скамеечки."
    th "Довольно уютненько."
    th "Куда же мне сказала идти та девочка?{w} Налево или направо?"
    th "Налево, направо, налево, направо…"
    play sound ds_sfx_psy
    sug "И зачем ты вообще туда идёшь?.."
    th "Я же решил казаться нормальным..."
    window hide
    menu:
        "Пойти направо":
            scene bg ext_path_day 
            with dissolve

            stop music fadeout 5

            window show
            "Через небольшой пролесок..."
            window hide

            stop ambience fadeout 2

            scene bg ext_boathouse_day 
            with dissolve

            play ambience ambience_boat_station_day fadein 5

            window show
            "Ты вышел на пристань."
            th "Наверное, не туда свернул."
            "Ты уже собирался пойти назад, как…"
            slp "Ой, так тебе не сюда!"

            play music music_list["take_me_beautifully"] fadein 5

            "Я обернулся."
            show sl smile swim at center   with dissolve
            "Перед тобой стоит та первая девочка."
            slp "Я же тебе сказала повернуть налево на площади, а ты куда пошел?"
            "Пионерская форма на ней сменилась на купальник."
            play sound ds_sfx_fys
            ins "Какие формы, какая фигура!"
            window hide
            menu:
                "Извиниться":
                    window show
                    me "Извини, я ошибся"
                    slp "Ну ничего, бывает."
                "Нагрубить":
                    window show
                    me "Куда захотел, туда и пошёл!"
                    $ ds_semtype += 1
                    show sl sad swim at center with dissolve
                    slp "Ну зачем сразу так грубо?"
                    $ ds_lp['sl'] -= 1
                "Отговориться":
                    window show
                    me "Да просто решил посмотреть, что в другой стороне..."
                    slp "А... ну ладно. Только лучше бы ты сначала зашёл к вожатой."
                "{check=instinct:8}Начать домогаться":
                    if skillcheck('instinct', lvl_easy):
                        window show
                        ins "{result}Начинай приставать к ней, такой шанс!"
                        me "Какая у тебя прекрасная фигура, позволь потрогать..."
                        show sl angry swim at center with dspr
                        slp "Нет, не позволю! Что ты себе позволяешь?"
                        $ ds_lp['sl'] -= 1
                    else:
                        window show
                        ins "{result}Ты слишком нервничаешь."
                    show sl normal swim at center with dspr
                    $ ds_skill_points['instinct'] += 1
                    $ ds_semtype += 1
                "Промолчать":
                    window show
                    $ ds_semtype -= 1
            slp "Ой, я же так и не представилась!{w} Меня Славя зовут!"
            $ ds_met['sl'] = 2
            slp "Вообще, полностью я Славяна Феоктистова, но все меня Славей зовут.{w} И ты тоже зови!"
            if skillcheck('composure', lvl_up_medium, passive=True):
                play sound ds_sfx_mot
                com "{result}Тебе удаётся взять себя в руки и ответить чётко."
                me "Хорошо, понял тебя."
            else:
                play sound ds_sfx_mot
                com "{result}Ты все еще был несколько растерян, так что на более осмысленные ответы тебя не хватает."
                me "А… да…"
            sl "А тебя?"
            play sound ds_sfx_psy
            vol "Кажется, ее взгляд пронизывает тебя насквозь."
            window hide
            menu:
                "Назвать имя":
                    window show
                    me "А… я… да… Семен…"
                    show sl smile2 swim at center   with dspr
                    sl "Очень приятно, Семен."
                "{check=conceptualization:14}Придумать себе имя":
                    if skillcheck('conceptualization', 14):
                        window show
                        $ ds_skill_points['conceptualization'] += 1
                        $ ds_fake_name = True
                        play sound ds_sfx_int
                        con "{result}Ну что ж, сейчас тебе будет самое отличное имя!"
                        con "Как тебе Семенитиус? Какой пафос, какая красота!"
                        me "Зови меня Семенитиус!"
                        show sl surprise swim at center with dissolve
                        sl "Странно... а вожатая говорила, что тебя Семёном зовут."
                        show sl smile2 swim at center with dissolve
                        sl "Впрочем, ладно, буду звать тебя так, если тебе так комфортнее."
                    else:
                        window show
                        $ ds_skill_points['conceptualization'] += 1
                        play sound ds_sfx_int
                        con "{result}Однако же ничего особо интересного в голову не приходит."
                        con "Придётся всё-таки назвать тебе своё настоящее имя... ну, или промолчать."
                        sl "Ты чего? Всё нормально?"
                        me "А... да... просто задумался."
                        show sl surprise swim at center with dissolve
                        sl "Об имени?"
                        show sl smile2 swim at center with dissolve
                        sl "А, точно... вожатая же говорила, что тебя Семёном звать."
                "Нагрубить":
                    window show
                    me "А не твоё это дело!"
                    show sl sad swim at center with dissolve
                    sl "Ты чего?"
                    $ ds_lp['sl'] -= 1
                    $ ds_karma -= 5
                    play sound ds_sfx_psy
                    emp "Её такое твоё отношение расстроило, но она решила не подавать виду."
                    show sl smile swim at center with dissolve
                    sl "А, точно... вожатая же говорила, что тебя Семёном звать."
                "Проигнорировать":
                    window show
                    $ ds_semtype -= 1
                    th "Пока лучше промолчу, не буду отвечать."
                    "..."
                    sl "Ты чего? Всё нормально?"
                    me "А... да... просто задумался."
                    show sl smile2 swim at center with dissolve
                    sl "Об имени?"
                    show sl smile2 swim at center with dissolve
                    sl "А, точно... вожатая же говорила, что тебя Семёном звать."
            sl "Ладно, я уже заканчиваю.{w} Ты подожди меня тут минутку, я сейчас переоденусь, и вместе пойдем к Ольге Дмитриевне, хорошо?"
            me "Хорошо…"
            hide sl  with dissolve
            "После этих слов она куда-то убежала, а ты садишься на мостик, свесив ноги в воду."
            "На тебе до сих пор тёплые зимние ботинки, так что по такой погоде ты совсем не боишься их промочить."
            play sound ds_sfx_fys
            edr "Более того, это хоть немного может тебя охладить."
            play sound ds_sfx_int
            lgc "Смотря на реку, ты размышляешь о происходящем."
            lgc "Если это что-то вроде тайного заговора, то он какой-то очень странный, а местами и дружелюбный чересчур."
            lgc "Нет, все же это больше похоже на случайность."
            lgc "Какую-то очень непонятную случайность."
            sl "Пошли?"
            show sl smile pioneer at center   with dissolve
            "Ты оборачиваешься."
            "Рядом с тобой стоит Славя, вновь одетая в пионерскую форму."
            me "Пошли…"
            play sound ds_sfx_fys
            hfl "Из всех встреченных тобой за все недолгое время пребывания в этом лагере она вызывает наименьшие подозрения."

            stop ambience fadeout 4

            hfl "Хотя сам этот факт уже подозрителен…"
            
            window hide

            scene bg ext_square_day 
            with dissolve

            window show
            "Вы вышли на площадь."
            show dv smile pioneer2 far at left    with dissolve   
            show us grin sport far at right    with dissolve
            "По ней друг за другом бегают «СССР» и девочка, ударившая меня по спине."
            th "Это у них игра, что ли, такая?"
            show sl angry pioneer at center   with dissolve
            sl "Ульяна, хватит бегать! Я все Ольге Дмитриевне расскажу!"

            show us laugh sport far at right   behind sl  with dspr
            us "Есть, гржнинначаник!"
            "Обе девочки убежали."
            hide dv 
            hide us 
            with dissolve
            show sl normal pioneer at center   with dspr
            play sound ds_sfx_int
            enc "Ульяна, значит... запомним."
            $ ds_met['us'] = 2
            enc "Может, стоит узнать и про вторую?"
            window hide
            menu:
                "Спросить":
                    window show
                    me "Славя, вот первую зовут Ульяна, а вторую, ту, которая рыжая, как звать."
                    sl "А... это Алиса Двачевская, местная хулиганка."
                    $ ds_met['dv'] = 2
                    $ ds_skill_points['encyclopedia'] += 1
                    sl "Советую тебе быть осторожнее при общении с ней. {w}Или вы уже познакомились?"
                    play sound ds_sfx_fys
                    pat "Да не то слово, так познакомились..."
                "Не спрашивать":
                    window show
                    th "Не буду расспрашивать до поры до времени Славю о происходящем здесь, о местных обитателях."
                    th "Лучше сначала дойти до этой таинственной Ольги Дмитриевны."
                    th "Она у них главная вроде бы."
            window hide

            scene bg ext_houses_day
            with dissolve

            stop music fadeout 5

            play ambience ambience_camp_center_day fadein 5

            window show
        "Пойти налево":
            window show
            "Ты прошёл площадь, обошёл памятник."
            
            scene bg ext_houses_day
            with dissolve

            stop music fadeout 5

            play ambience ambience_camp_center_day fadein 5

            "Передо мной предстали ряды домиков."
            play sound ds_sfx_int
            vic "И что делать дальше? Придётся подождать кого-нибудь."
            "И ты ждёшь."
            lgc "Смотря на домики, ты размышляешь о происходящем."
            lgc "Если это что-то вроде тайного заговора, то он какой-то очень странный, а местами и дружелюбный чересчур."
            lgc "Нет, все же это больше похоже на случайность."
            lgc "Какую-то очень непонятную случайность."

            $ renpy.pause(3)
            slp "Ой, а чего ты тут стоишь? Некому отвести тебя?"

            play music music_list["take_me_beautifully"] fadein 5

            "Ты оборачиваешься."
            show sl smile pioneer at center   with dissolve
            "Перед тобой стоит та первая девочка."
            slp "Ой, я же так и не представилась!{w} Меня Славя зовут!"
            $ ds_met['sl'] = 2
            slp "Вообще, полностью Славяна Феоктистова, но все меня Славей зовут.{w} И ты тоже зови!"
            if skillcheck('composure', lvl_up_medium, passive=True):
                play sound ds_sfx_mot
                com "{result}Тебе удаётся взять себя в руки и ответить чётко."
                me "Хорошо, понял тебя."
            else:
                play sound ds_sfx_mot
                com "{result}Ты все еще был несколько растерян, так что на более осмысленные ответы тебя не хватает."
                me "А… да…"
            sl "А тебя?"
            "Кажется, ее взгляд пронизывает тебя насквозь."
            window hide
            menu:
                "Назвать имя":
                    window show
                    me "А… я… да… Семен…"
                    show sl smile2 pioneer at center   with dspr
                    sl "Очень приятно, Семен."
                "{check=conceptualization:14}Придумать себе имя":
                    if skillcheck('conceptualization', 14):
                        window show
                        $ ds_skill_points['conceptualization'] += 1
                        $ ds_fake_name = True
                        play sound ds_sfx_int
                        con "{result}Ну что ж, сейчас тебе будет самое отличное имя!"
                        con "Как тебе Семенитиус? Какой пафос, какая красота!"
                        me "Зови меня Семенитиус!"
                        show sl surprise pioneer at center with dissolve
                        sl "Странно... а вожатая говорила, что тебя Семёном зовут."
                        show sl smile2 pioneer at center with dissolve
                        sl "Впрочем, ладно, буду звать тебя так, если тебе так комфортнее."
                    else:
                        window show
                        $ ds_skill_points['conceptualization'] += 1
                        play sound ds_sfx_int
                        con "{result}Однако же ничего особо интересного в голову не приходит."
                        con "Придётся всё-таки назвать тебе своё настоящее имя... ну, или промолчать."
                        sl "Ты чего? Всё нормально?"
                        me "А... да... просто задумался."
                        show sl surprise pioneer at center with dissolve
                        sl "Об имени?"
                        show sl smile2 pioneer at center with dissolve
                        sl "А, точно... вожатая же говорила, что тебя Семёном звать."
                "Нагрубить":
                    window show
                    me "А не твоё это дело!"
                    show sl sad pioneer at center with dissolve
                    sl "Ты чего?"
                    $ ds_lp['sl'] -= 1
                    $ ds_karma -= 5
                    play sound ds_sfx_psy
                    emp "Её такое твоё отношение расстроило, но она решила не подавать виду."
                    show sl smile pioneer at center with dissolve
                    sl "А, точно... вожатая же говорила, что тебя Семёном звать."
                "Проигнорировать":
                    window show
                    $ ds_semtype -= 1
                    th "Пока лучше промолчу, не буду отвечать."
                    "..."
                    sl "Ты чего? Всё нормально?"
                    me "А... да... просто задумался."
                    show sl smile2 pioneer at center with dissolve
                    sl "Об имени?"
                    show sl smile2 pioneer at center with dissolve
                    sl "А, точно... вожатая же говорила, что тебя Семёном звать."
            sl "Пошли?"
            me "Пошли…"
            play sound ds_sfx_fys
            hfl "Из всех встреченных тобой за все недолгое время пребывания в этом лагере она вызывает наименьшие подозрения."

            stop ambience fadeout 4

            hfl "Хотя сам этот факт уже подозрителен…"
            window hide

            window show
    "Пройдя через ряды одинаковых палаток, вы наконец останавливаетесь перед небольшим одноэтажным домиком."
    window hide
    scene bg ext_house_of_mt_day 
    with dissolve

    window show
    if skillcheck('conceptualization', lvl_medium, passive=True):
        play sound ds_sfx_int
        con "{result}Он словно сошел с картины какого-то художника: выцветшая, местами облупившаяся от старости краска сверкала на солнце, приоткрытые ставни еле заметно качались на ветру, а по краям росли огромные кусты сирени."
        con "Казалось, что эта ветхая хижинка словно утопает в пурпурном бархатном шторме, как судно, несущееся по волнам бушующего моря, борется с бурей, уходит под воду и снова всплывает, но все же не может побороть стихию."
        con "Так и здесь – сирень была стихией, неотвратимо уничтожающей домик вожатой."
    show sl normal pioneer at center   with dissolve
    sl "Что стоишь? Пойдем!"
    "Славя вывела тебя из раздумий."
    per_hea "Кажется, в домике кто-то есть."
    mtp "Ульяна, и хватит издеваться над Леной…"
    $ ds_met['un'] = 2
    $ ds_met['us'] = 2
    window hide

    if skillcheck('inland_empire', lvl_challenging, passive=True):
        play sound sfx_scary_sting
        scene cg d1_rena_sunset 

        with vpunch
        with hpunch

        $ renpy.pause(2)

        window show
        play sound ds_sfx_psy
        ine "{result}Реной?!"
        window hide

    scene bg ext_house_of_mt_day 
    show sl normal pioneer at center 
    with dissolve

    window show

    play sound sfx_open_dooor_campus_1 fadein 0

    show us grin sport far at left   behind sl  with dissolve   

    "И точно, через мгновение дверь открывается, оттуда выбегает Ульяна и проносится мимо меня, все так же хитро улыбаясь."
    hide us  with dissolve

    show un normal pioneer far at left   behind sl  with dissolve   
    "За ней выходит девочка с хвостиками."
    sl "Лена, не обижайся ты на нее!"

    play sound ds_sfx_mot
    res "Значит, ее зовут Лена…"
    show un shy pioneer at left  behind sl  with dissolve
    un "Да я не…"
    "Она, покраснев и потупив взгляд в пол, проходит мимо тебя."
    hide un  with dissolve
    play sound ds_sfx_psy
    vol "Ты почему-то хочешь обернуться и посмотреть, куда она направится"
    "Но тут Славя говорит."

    stop ambience fadeout 3

    sl "Пойдем."
    window hide

    menu:
        "Оглядеться":
            window show
            me "Сейчас, подожди."
            play sound ds_sfx_mot
            per_eye "Ты оборачиваешься, но она уже куда-то исчезла."
            me "Ладно..."
            window hide
        "Пойти":
            pass

    scene bg int_house_of_mt_day 
    with dissolve

    play music music_list["smooth_machine"] fadein 5

    window show
    "Вы заходите в домик."
    "Внутри он выглядит примерно так, как ты себе его и представлял: две кровати, стол, пара стульев, простенький ковер на полу, шкаф."
    "Ничего особенного, но при этом создаётся ощущение какого-то уюта, хотя в плане порядка эта комнатка не сильно далеко ушла от твоей квартиры."
    show mt normal pioneer far at center    with dissolve
    "Возле окна стоит девушка."
    $ ds_met['mt'] = 1
    play sound ds_sfx_int
    vic "На вид ей что-то около 25 лет."
    play sound ds_sfx_fys
    ins "Внешностью вместе с фигурой ее природа не обделила..."
    ins "Хоть одна вещь в этом пандемониуме не может не радовать – это красота его обитателей."
    window hide
    menu:
        "{check=rhetoric:11}Подкатить":
            if skillcheck('rhetoric', lvl_up_medium):
                play sound ds_sfx_int
                rhe "{result}Начни говорить про то, какая она прекрасная!"
                me "А вы всегда такая красивая, или только сегодня?"
                $ ds_skill_points['rhetoric'] += 1
                $ ds_lp['mt'] += 1
                show mt surprise pioneer far at center with dspr
                mtp "Эм... {w}спасибо."
                show mt normal pioneer at center with dspr
                mtp "Меня Ольга Дмитриевна зовут, я вожатая."
            else:
                play sound ds_sfx_int
                rhe "{result}Но тебе приходит совсем уж банальность..."
                me "Простите, а вам зять не нужен?"
                $ ds_skill_points['rhetoric'] += 1
                $ ds_lp['mt'] -= 1
                show mt surprise pioneer far at center with dspr
                mtp "Чего?"
                rhe "Она удивлена тем, что ты ляпнул... и удивлена не в хорошем смысле."
                mtp "Э... {w}ладно."
                mtp "Меня Ольга Дмитриевна зовут, я вожатая."
            $ ds_semtype += 1
        "Ничего не говорить":
            mtp "Пришел-таки!{w} Отлично!{w} Меня Ольга Дмитриевна зовут, я вожатая."
    $ ds_met['mt'] = 2
    play sound ds_sfx_int
    rhe "Говори так, как будто всё происходящее совсем тебя не удивляет."
    me "Очень приятно, Семен."
    show mt normal pioneer at center   with dissolve
    "Она подходит ближе."
    mt "Мы тебя с утра ждем."
    me "Ждете? Меня?.."
    show mt smile pioneer at center   with dspr
    mt "Да, конечно!"
    window hide
    menu:
        "Начать расспрашивать":
            window show
            me "А когда автобус следующий будет, а то я…"
            show mt surprise pioneer at center   with dspr
            mt "А тебе зачем?"
            th "Действительно, зачем мне…"
            rhe "Прямые вопросы задавать не стоит – они могут вызвать совсем не ту реакцию, которую тебе хочется."
            rhe "Да и ответы ты вряд ли получишь."
            play sound ds_sfx_int
            dra "А если подыграете им, примете свою роль в представлении - то в итоге наверняка сможете что-то выяснить, мессир."
            me "Нет, просто интересно…"
            me "А, кстати, а где мы точно находимся?{w} Ну, адрес там?"
            me "Я родителям хотел письмо написать, что удачно добрался."
            show mt normal pioneer at center   with dspr
            mt "Так мне твои родители полчаса назад звонили! Тебе привет передавали."
            play sound ds_sfx_mot
            res "Вот это поворот!"
            me "Значит, я могу им позвонить, а то я перед отъездом забыл сказать кое-что."
            show mt smile pioneer at center   with dspr
            mt "Нет."
            "Она мило и непринужденно улыбнулась."
            me "А почему?"
            mt "А у нас телефона нет."
            res "А как тогда они позвонили?"
            me "Так как же они сюда позвонили?"
            mt "Я только из райцентра вернулась, там с ними и поговорила."
            th "Ах, вот так, значит?"
            me "А мне можно как-нибудь в этот райцентр?"
            mt "Нет."
            "Она все так же улыбается."
            me "А почему?"
            mt "Потому что следующий автобус будет только через неделю."
            play sound ds_sfx_int
            rhe "Не спрашивай, как она тогда сумела добраться туда и обратно - вряд ли получишь ответ."
            play sound ds_sfx_psy
            aut "Ну нет, нам нужно это выяснить!"
            window hide
            menu:
                "Спросить":
                    window show
                    me "А как {i}вы{/i} тогда добрались?"
                    mt "Кажется, кто-то задаёт слишком много вопросов."
                    mt "Успокойся, твои родители знают, где ты находишься и что ты в надёжных руках."
                    play sound ds_sfx_fys
                    hfl "В надёжных ли?"
                "Не спрашивать":
                    window show
            show mt normal pioneer at center   with dspr
            show sl normal pioneer at right   with dissolve

            "Все это время Славя стоит рядом с тобой и, кажется, не находит в вышем диалоге ничего такого."
        "Не расспрашивать":
            window show
    show mt surprise pioneer at center   with dspr
    mt "Ой, надо тебе форму подобрать!"
    th "Не имею ровным счетом никакого желания наряжаться в пионерские шортики и завязывать нелепый красный галстук"
    play sound ds_sfx_fys
    edr "Но и ходить в зимней одежде летом тоже не лучшая идея."
    me "Да, спасибо…"
    show mt normal pioneer at center   with dspr
    th "Интересно, только я один считал странным, что в такую жару кто-то ходит в пальто и зимних ботинках?"
    show mt smile pioneer at center   with dspr
    mt "Ладненько, я побежала, а ты пока можешь осмотреть лагерь!{w} Вечером приходи на ужин, не забудь!"
    hide mt  with dissolve
    "С этими словами она вышла из домика."
    "Нет, даже не вышла – выпорхнула."
    show sl smile pioneer at right   with dspr:
        linear 1.0 xalign 0.5
    "Ты остался наедине со Славей."
    sl "Мне тоже пора – дела."
    sl "Ты походи, осмотрись.{w} Вечером увидимся."
    hide sl  with dissolve
    th "Если здесь не скрыто никакого подвоха или угрозы, то такая реальность в лице Слави мне начинает нравиться все больше!"
    hfl "Если..."
    "Что же, единственным твоим вариантом остаётся воспользоваться советом и пойти осматривать лагерь."

    stop music fadeout 5

    play sound ds_sfx_int
    rhe "Заодно попробуешь что-нибудь выяснить по дороге."
    window hide

    scene bg ext_houses_day 
    with dissolve

    play ambience ambience_camp_center_day fadein 5

    window show
    "Проходя через местный «жилой квартал», ты видишь идущего навстречу мне пионера."
    show el normal pioneer far at center    with dissolve
    play sound ds_sfx_mot
    res "Именно пионера, а не пионерку – и в этом царстве амазонок есть мужчины."
    $ ds_met['el'] = 1

    play music music_list["eat_some_trouble"] fadein 2

    elp "Привет, ты новенький, наверное, Семён, так?"
    me "Да, а ты откуда…"
    show el grin pioneer at center   with dissolve 
    elp "Да уже все знают! Я, кстати, Электроник. Настоящий. Можешь меня так и звать."
    $ ds_met['el'] = 2
    res "Электроник? Настоящий?"
    me "Ясно..."
    show el smile pioneer at center   with dspr
    el "Ульянка меня еще Сыроежкой зовет."
    me "Сыроежкой?"
    th "Не подосиновиком?"
    el "Фамилия у меня такая – Сыроежкин."
    me "Ясно…"
    el "Давай я тебе тут все покажу!"
    play sound ds_sfx_psy
    sug "Так будет лучше - один ты будешь это всё изучать гораздо дольше."
    window hide
    menu:
        "Согласиться":
            window show
            me "Что же, давай."
            $ ds_accept_el = True
            $ ds_lp['el'] += 1
        "Отказаться":
            window show
            me "Не... лучше я сам."
            play sound ds_sfx_mot
            svf "Но он тебя не слышит и буквально хватает за руку так, что не вырваться."
            svf "Тебе {i}придётся{/i} пойти с ним."
    window hide

    scene bg ext_square_day 
    with dissolve

    window show
    "Вы направляетесь в сторону площади."
    "Там на одной из лавочек сидит Лена и читает какую-то книжку.{w} Электроник уверенным шагом подходит к ней."
    show el normal pioneer at cleft   with dspr
    show un normal pioneer at cright   with dspr
    with dissolve
    el "Лена, привет! Это новенький, Семен, знакомься!"
    "Бойко начинает он."
    play sound ds_sfx_psy
    aut "Впечатляет..."
    me "Привет.{w} Ну, мы уже заочно знакомы."
    show un shy pioneer at cright   with dspr
    un "Да…"
    "Она на секунду отрывает глаза от книжки, смотрит на тебя, краснеет и вновь принимается за чтение, словно не замечая, что вы все еще здесь."
    el "Ладно, пойдем дальше."
    th "И это всё знакомство?"
    play sound ds_sfx_psy
    emp "А ты не заметил скромность Лены? Она же бросается в глаза! {w}Скромность, в смысле."
    emp "А ещё Электроник очень уж активный..."
    play sound ds_sfx_psy
    sug "В общем, хочешь с ней познакомиться по-настоящему - это нужно делать наедине."
    sug "И очень осторожно."
    me "Пойдем."
    window hide

    stop music fadeout 5

    scene bg ext_dining_hall_away_day 
    with dissolve

    window show
    "Вы выходите к некоей постройке."
    if skillcheck('logic', lvl_trivial, passive=True):
        play sound ds_sfx_int
        lgc "{result}Думаю, излишне пояснять, что это столовая."
        show el normal pioneer at center   with dissolve
        el "А вот это…"
        me "Я понял, здесь вы принимаете органическую пищу!"
        show el smile pioneer at center   with dspr
        el "Ну, что-то вроде того…"
    else:
        show el normal pioneer at center   with dissolve
        el "А вот это столовая!"
    show el normal pioneer at center   with dspr
    show dv normal pioneer2 far at left    with dissolve   
    "На крыльце столовой стоит недружелюбная девочка, которая до этого ударила меня по спине."
    if ds_beat_dv:
        play sound ds_sfx_psy
        emp "И которую ты ударил!"
    play sound ds_sfx_mot
    com "Когда ты увидел ее, твоё шутливое настроение вмиг куда-то исчезло."
    th "Действительно, сейчас не самая подходящая ситуация, чтобы прикалываться над этим пареньком, хоть он и весьма потешен."
    th "Сначала надо понять, что к чему и где я вообще нахожусь!"
    show el scared pioneer at center   with dspr
    el "А вот она – Алиса Двачевская. Ты с ней поосторожнее."
    $ ds_met['dv'] = 2
    play sound ds_sfx_fys
    hfl "Он говорит шепотом. Видимо, почему-то её боится."
    play sound ds_sfx_mot
    per_hea "Правда, таким шёпотом говорит, чтобы эта Алиса наверняка услышала."

    stop ambience fadeout 2

    el "Никогда не называй ее ДваЧе, она этого не любит!"
    play sound ds_sfx_psy
    emp "Интересно, с чем это связано? Детская травма?"
    play sound ds_sfx_int
    lgc "Двачевская... Дваче... А по фамилии-то её можно называть?"
    hfl "Наверное, лучше не стоит."

    play music music_list["awakening_power"] fadein 2

    show dv angry pioneer2 far at left   with dspr
    dv "Чего ты сказал? Как ты меня назвал?"
    play sound ds_sfx_mot
    res "Кажется, она услышала."
    "В мгновение ока Алиса спрыгивает с крыльца и бросается в вашу сторону."
    show el shocked pioneer at center   with dspr
    el "Ладно, ты дальше сам как-нибудь…"
    "Электроник бросается бежать так, что только пятки засверкали."
    play sound ds_sfx_psy
    aut "Как трусливо... девочки испугался."
    hide el  with dissolve

    if ds_beat_dv:
        dv "А тут ещё ты?! Ты! Побил меня, девушку!"
        play sound ds_sfx_psy
        emp "Видишь, как ты её обидел? Доволен?"

    window hide

    menu:
        "Побежать за ним":
            stop music fadeout 3

            window show
            "Ты решил, что не хочешь еще раз сталкиваться с этой агрессивной девочкой, Алисой, и бросился вслед за Электроником."
            $ ds_semtype -= 1
            window hide

            $ persistent.sprite_time = "day"
            scene bg ext_square_day 
            with dissolve

            play ambience ambience_camp_center_day fadein 5

            window show
            "Выбежав на площадь, ты понял, что потерял его из виду."
            "Но и Двачевская за тобой не гонится."
            th "Впрочем, наверное, не стоит ее так называть.{w} Даже про себя..."
            if not ds_beat_dv:
                "Отдышавшись, ты задумываешься о причинах своего поступка."
                th "Ну девочка... Ну агрессивная...{w} Но зачем бежать было?.."

            stop ambience fadeout 2

            "Так и не найдя никакого подходящего ответа, ты садишься на лавочку и смотришь в небо."
        "Ничего не делать" if not ds_beat_dv:
            $ ds_lp['dv'] += 1
            show dv angry pioneer2 at left   with dissolve
            window show
            "Алиса, пробегая мимо тебя, останавливается на мгновение и бросает:"
            dv "А с тобой мы позже разберемся!"
            me "А я что? Я ничего!"
            com "Ты кривишь виноватую улыбку, хотя в чем бы ты должен был быть виноват перед ней?.."
            "Она не ответила и побежала догонять Электроника."

            stop music fadeout 5

            hide dv  with dissolve
        "Одобрить действия Алисы":
            window show
            me "Правильно, так его! А то ещё смеет обзывать {i}тебя{/i}, такую девушку."
            dv "А ты не подлизывайся!"
            dv "Впрочем, ладно, позже с тобой разберёмся!"
            $ ds_lp['dv'] += 2
            $ ds_lp['el'] -= 1
            $ ds_karma -= 5
            me "А я что? Я только за тебя!"
            "Она не отвечает и побежала догонять Электроника."

            stop music fadeout 5

            hide dv  with dissolve
        "{check=physical_instrument:11}Остановить Алису":
            $ ds_semtype += 1
            if skillcheck('physical_instrument', lvl_up_medium, modifiers=[('ds_beat_dv', -2, 'Алиса научена опытом')]):
                $ ds_skill_points['physical_instrument'] += 1
                window show
                play sound ds_sfx_fys
                phi "{result}Ты встаёшь перед ней и останавливаешь её."
                show dv angry pioneer2 close at center with dissolve
                $ ds_lp['dv'] -= 1
                $ ds_lp['el'] += 1
                dv "Что ты творишь?!"
                me "Успокойся, он просто предупредил меня, чтобы я тебя так не называл."
                dv "Зачем он это делал так, чтобы я услышала?!"
                dv "Ладно ты, но ему прекрасно известно, что я терпеть не могу это прозвище!"
                dv "Отпусти меня, в общем!"
                window hide
                menu:
                    "Отпустить":
                        window show
                        me "Ладно уж, беги."
                    "Держать дальше":
                        window show
                        play sound ds_sfx_mot
                        svf "И всё-таки она вырывается из твоих рук и убегает."
                        hide dv with dissolve
                    "{check=savoir_faire:10}Сбить с ног":
                        if skillcheck('savoir_faire', lvl_medium):
                            window show
                            play sound ds_sfx_mot
                            svf "{result}Ловким и резким движением ты сбиваешь её с ног и укладываешь на траву."
                            play sound sfx_alisa_falls
                            scene cg ds_day1_dv_on_grass with dissolve
                            dv "Да что же ты творишь в конце концов-то?!"
                            me "Просто... Кстати, так приятно лежать вместе."
                            dv "А вот мне как-то не особо! Начали оскорблениями, а кончаете домогательствами!"
                            $ ds_lp['dv'] -= 1
                            $ ds_lp['mt'] -= 1
                            $ ds_karma -= 20
                            scene bg ext_dining_hall_away_day with dissolve
                            show dv angry pioneer2 close at center with dissolve
                            "C этими словами она буквально выскальзывает из-под тебя и сбегает."
                            hide dv with dissolve
                            $ ds_skill_points['savoir_faire'] += 1
                        else:
                            window show
                            play sound ds_sfx_mot
                            svf "{result}Но у тебя не получается сбить её с ног."
                            svf "Более того, ты теряешь концентрацию, и она сбегает."
                            hide dv with dissolve
                            $ ds_skill_points['savoir_faire'] += 1
                    "Дать пощёчину":
                        window show
                        play sound sfx_face_slap
                        phi "В ответ ты бьёшь её по щеке."
                        show dv shocked pioneer2 close at center with dspr
                        me "Да успокойся ты наконец уже!"
                        dv "Да что с тобой не так?! Что я тебе вообще сделала-то?"
                        $ ds_lp['dv'] -= 2
                        show dv cry pioneer2 close at center with dspr
                        emp "И правда, зачем ты её бьёшь?"
                        me "Я... Просто зачем ты так агрессивно себя ведёшь со всеми?.."
                        show dv angry pioneer2 close at center with dspr
                        dv "Да пошёл ты!"
                        hide dv with dissolve
                        "И всё-таки она убегает."
                        $ ds_beat_dv = True
                        $ ds_lp['sl'] -= 1
                        $ ds_lp['us'] -= 1
                        $ ds_lp['mi'] -= 1
                        $ ds_lp['mz'] -= 1
                        $ ds_lp['mt'] -= 1
                        $ ds_karma -= 20
                    "{check=rhetoric:15}Успокоить её словами":
                        if skillcheck('rhetoric'. lvl_heroic):
                            play sound ds_sfx_int
                            rhe "{result}Акцентируй внимание на том, что он просто хотел тебя предупредить."
                            me "Послушай, я тут новенький, но не хотел бы обидеть тебя случайно."
                            me "Думаю, для этого важно знать, что тебя задевает."
                            me "Вот он меня и предупредил. Теперь я знаю, что так тебя называть нельзя."
                            me "А про голос - он, скорее всего, от нервов сказал немного громче, чем надо."
                            $ ds_karma += 10
                            show dv grin pioneer2 close at center with dspr
                            dv "Вот как? И как же меня нельзя называть?"
                            rhe "Вопрос с подвохом. Не вздумай давать правильный ответ!"
                            window hide
                            menu:
                                "ДваЧе":
                                    window show
                                    me "Конечно же тебя нельзя называть ДваЧе!"
                                    show dv rage pioneer2 close at center with dspr
                                    dv "Плохо усвоил урок словами! Значит, усвоишь его кулаками!"
                                    $ ds_lp['dv'] -= 1
                                    show bg ext_dining_hall_away_day with flash_red
                                    $ ds_damage_health()
                                    dv "Что, понял теперь?"
                                    me "Да, понял..."
                                    dv "То-то же!"
                                    hide dv with dissolve
                                "Нельзя этого говорить":
                                    window show
                                    me "А нельзя этого говорить!"
                                    show dv smile pioneer2 close at center with dspr
                                    dv "Молодец, усвоил урок!"
                                    dv "Ладно, бывай!"
                                    $ ds_lp['dv'] += 1
                                    hide dv with dissolve
                        else:
                            play sound ds_sfx_int
                            rhe "{result}Можешь попробовать, но, похоже, ты исчерпал все способы убеждения."
                            me "Послушай, он ничего плохого не хотел же!"
                            dv "Если бы не хотел - не называл бы меня так!"
                            play sound ds_sfx_mot
                            res "Тут она вырывается и быстро убегает."
                            hide dv with dissolve
                            th "Вот дела..."
            else:
                window show
                phi "{result}Но у тебя не получается её удержать, и всё-таки она сбегает."
                hide dv with dissolve
                $ ds_skill_points['physical_instrument'] += 1
            dv "А с тобой я ещё разберусь позже!"
            per_hea "Это последнее, что ты услышал от неё."
    play sound ds_sfx_int
    lgc "Похоже, оставшееся время до ужина тебе предстоит коротать в одиночестве."
    "Ты идёшь на восток.{w} По крайней мере туда, где он по твоим представлениям должен быть."
    window hide

    scene bg ext_playground_day 
    with dissolve

    play ambience ambience_soccer_play_background fadeout 2

    play music music_list["went_fishing_caught_a_girl"] fadein 5

    window show
    "Спустя некоторое время ты оказываешься около футбольного поля."
    "Там вовсю шел матч."
    window hide
    menu:
        "Понаблюдать":
            window show
            "Ты встаёшь в сторонке, чтобы немного понаблюдать."
            play sound ds_sfx_fys
            phi "В детстве и юношестве ты довольно неплохо играл сам и даже подумывал о профессиональной карьере, но несколько травм подряд отбили у тебя желание рисковать здоровьем ради туманной перспективы."
            "На поле бегают дети совершенно разных возрастов – вот мальчик лет 10 и девочка лет 14…"
            th "Девочка…{w} Так это же Ульяна!"
            th "Впрочем, ничего удивительного в том, что она и в футбол играет, нет."
            th "С ее-то неугомонностью."
            "Ты стоишь на приличном отдалении от поля, но каким-то образом она все же замечает тебя."
            show us laugh sport far at center    with dissolve   
            us "Эй ты!"
            us "Играть будешь?"
            play sound ds_sfx_fys
            phi "С одной стороны, ничего страшного в том, чтобы побегать минут десять, нет."
            play sound ds_sfx_fys
            hfl "С другой – в твоей ситуации любой неверный шаг может оказаться фатальным."
            play sound ds_sfx_fys
            edr "И, как минимум, одет ты явно не по погоде."
            edr "Играть в зимних ботинках и теплых джинсах – верный путь к тому, что тебя потом можно будет выжимать от пота."
            th "А играть босиком и в трусах попросту неэтично."
            window hide
            menu:
                "Согласиться":
                    window show
                    $ ds_play_football = True
                    $ ds_lp['us'] += 1
                    "И всё-таки ты выбегаешь на футбольное поле и решаешь поиграть."
                    esp "Давай, покажи всем класс, поддержи играющих детей!"
                    scene bg black 
                    with dissolve2
                    $ renpy.pause(2)
                    scene bg ext_playground_day with dissolve
                    "Но вскоре ты чувствуешь себя слишком тяжело и вынужден прекратить игру."
                    play sound ds_sfx_fys
                    edr "Всё-таки твоя одежда совершенно не подходит для спортивных игр. Теперь ты ощущаешь себя очень тяжело!"
                    $ ds_damage_health()
                "Отказаться":
                    window show
                    me "Давай в другой раз!"
                    "Крикнул я ей, развернулся и пошел назад."
                    hide us  with dissolve

            stop music fadeout 5

            "Она что-то вопила мне вслед, но я не слушал."
            window hide
        "Пойти своей дорогой":
            window show
            th "А какое мне до этого дело?"
            "И ты уходишь."
            window hide

    stop ambience fadeout 2

    scene bg black 
    with dissolve2

    play ambience ambience_camp_center_evening fadeout 2

    window show
    "..."
    "День клонится к вечеру, который несёт с собой усталость и опустошение от бесцельно прожитого дня."
    "..."
    window hide

    scene bg ext_square_day 
    with dissolve2

    window show
    "Ты возвращаешься на площадь, садишься на лавочку и обессилено вздыхаешь."
    th "Буду сидеть здесь и ждать ужина.{w} В конце концов, искать ответы лучше сытым."
    th "Их же тут кормят, наверное?.."
    th "А ведь интересно, как самые простые потребности человека отбивают желание мыслить, стремиться к чему-то."
    th "Вот, я чувствую голод, и меня уже меньше волнует, где я и что со мной."
    th "Неужели великие люди тоже подвержены подобному?"
    th "И как тогда, к примеру, Спартак в древности поднимал восстание рабов?.."
    th "Остается только один вывод – я не великий человек, и мне в принципе все равно в какой машине быть шестеренкой – в социуме, матрице или непонятном пионерлагере."

    play sound sfx_dinner_jingle_speaker

    "Не успеваешь ты закончить мысль, как из динамика на фонаре начинает играть какая-то музыка."
    play sound ds_sfx_int
    lgc "Наверняка это сигнал к ужину."
    "Ты направляешься в сторону столовой – благо, теперь знаешь, где она."
    window hide

    scene bg ext_dining_hall_away_day 
    with dissolve

    stop sound fadeout 2

    window show
    "На крыльце стоит Ольга Дмитриевна."
    show mt normal pioneer far at center    with dissolve   
    "Ты останавливаешься и пристально смотришь на нее, словно ожидая чего-то."
    "Она тоже некоторое время смотрит на тебя, но потом все же подходит."
    show mt normal pioneer at center   with dissolve
    mt "Семен, чего стоишь? Проходи!"
    play sound ds_sfx_fys
    hfl "Наверное, ничего страшного не случится, если ты пойдёшь с ней."
    play sound ds_sfx_fys
    edr "Да, тебе определённо пора поесть."
    window hide

    stop ambience fadeout 3

    scene bg int_dining_hall_people_day 
    with dissolve

    play ambience ambience_dining_hall_full fadein 5

    window show
    "Вы вместе заходите внутрь."
    "Столовая представляет из себя…{w} столовую."
    play sound ds_sfx_int
    enc "Тебе в свое время доводилось бывать в заводской столовой…{w} Эта была в точности такая же, разве что почище и поновее."
    enc "Железные стулья, столы, кафель на стенах и на полу, не отличающаяся изысканностью потрескавшаяся посуда."
    enc "Наверное, такой и должна быть столовая в пионерлагере."
    show mt normal pioneer at center   with dissolve
    mt "Семен, сейчас мы тебе место найдем…"
    "Она окидывает взглядом помещение."
    show mt rage pioneer at center   with dspr
    mt "Стой, Двачевская!"
    "Ольга Дмитриевна прикрикивает на проходящую мимо Алису."
    show dv normal pioneer2 at left   with dissolve
    dv "А что такое?"
    mt "Ты как одета?"
    dv "А как я одета?"
    ins "Действительно, наряд ее несколько вызывающий…"
    window hide
    menu:
        "{check=authority:13}Заступиться":
            if skillcheck('authority', lvl_formidable):
                play sound ds_sfx_psy
                window show
                aut "{result}Скажи-ка этой вожатой про то, что надо бы дать Алисе поужинать."
                aut "Ну же, давай, покажи себя и защити девушку!"
                me "Отстаньте от Алисы, дайте ей поужинать спокойно!"
                show mt shocked pioneer at center with dissolve
                show dv surprise pioneer2 at left with dissolve
                aut "Ты состроил такое выражение лица, будто попытка тебя ослушаться приведёт к непоправимым последствиям."
                aut "Кажется, вся столовая смотрит за дальнейшим развитием событий."
                mt "Я, конечно, всё понимаю... но правила всё-таки надо бы соблюдать."
                show mt normal pioneer at center with dissolve
                mt "Алиса, переодень всё-таки, пожалуйста, форму."
                dv "Ладно..."
                show dv normal pioneer at left with dissolve
                "Алиса поправляет рубашку и проходит мимо, бросив на тебя какой-то смешанный взгляд."
                play sound ds_sfx_psy
                emp "Её твой заход всё-таки впечатлил, по глазам видно."
                hide dv with dissolve
                $ ds_skill_points['authority'] += 1
            else:
                play sound ds_sfx_psy
                window show
                aut "{result}Ну нет, тут без вариантов. Она всё-таки тут главная."
                me "Может... всё-таки простите Алису?"
                if ds_beat_dv:
                    show dv surprise pioneer2 at left with dspr
                mt "Ну так вот она переоденет форму, и ничего ей не будет!"
                show dv sad pioneer2 at left   with dspr
                dv "Ладно-ладно…"
                show dv normal pioneer at left   with dissolve
                "Алиса поправляет рубашку и проходит мимо, бросив на тебя не очень приятный взгляд."
                if ds_beat_dv:
                    show dv angry pioneer at left with dissolve
                    play sound ds_sfx_psy
                    emp "Даже, скорее, злобно-обиженный."
                hide dv  with dissolve
                $ ds_skill_points['authority'] += 1
            $ ds_lp['dv'] += 1
            $ ds_semtype += 1
        "Не вмешиваться":
            window show
            $ ds_semtype -= 1
            mt "Немедленно приведи в порядок форму!"
            show dv sad pioneer2 at left   with dspr
            dv "Ладно-ладно…"
            show dv normal pioneer at left   with dissolve
            "Алиса поправляет рубашку и проходит мимо, бросив на тебя не очень приятный взгляд."
            if ds_beat_dv:
                show dv angry pioneer at left with dissolve
                play sound ds_sfx_psy
                emp "Даже, скорее, злобно-обиженный."
            hide dv  with dissolve
        "Поддакивать":
            window show
            me "Да, что это такое! Форму нужно носить по уставу!"
            show mt smile pioneer at center with dissolve
            show dv angry pioneer2 at left with dissolve
            mt "Вот видишь, даже твой товарищ говорит, что так форму не носят."
            $ ds_lp['mt'] += 1
            dv "Да переодену я вашу форму!"
            $ ds_lp['dv'] -= 1
            mt "Она не моя, а твоя."
            dv "Отстаньте уже."
            "Алиса поправляет рубашку и проходит мимо, бросив на тебя злобный взгляд."
            hide dv with dissolve
    show mt normal pioneer at center   with dspr
    mt "Итак, куда бы нам тебя посадить?"
    "Она обводит взглядом столовую."
    mt "Давай вот сюда, к Ульяне!"
    window hide
    menu:
        "Протестовать":
            window show
            me "Это… А может…"
        "Смириться":
            window show
            $ ds_semtype -= 1
    show mt smile pioneer at center   with dspr
    mt "Да, точно, как раз уже и еда стоит!"
    "Тебе не остаётся ничего другого, кроме как согласиться."
    scene bg ds_int_dininghall_table1_day with dissolve
    play sound ds_sfx_fys
    hfl "Конечно, есть некая доля вероятности, что в котлетах яд кураре, пюре обильно сдобрено мышьяком, а вместо компота мне налили отличный антифриз…"
    play sound ds_sfx_psy
    vol "Но это так аппетитно выглядит - ты не можешь устоять!"

    if not ds_play_football:
        show us normal pioneer at center   with dissolve
        us "Эй!"
        "Ты оборачиваешься."
        me "Чего тебе?"
        show us dontlike pioneer at center   with dspr
        us "Почему с нами в футбол не стал играть?"
        window hide
        menu:
            "Не захотел":
                window show
                me "Я просто не захотел"
                play sound ds_sfx_psy
                emp "Определённо, она обиделась."
                $ ds_lp['us'] -= 1
                "И ушла."
            "Не был в форме":
                window show
                me "Я не в форме."
                "И показываешь на свою одежду."
                show us grin pioneer at center   with dspr
                us "А, ну тогда ладно, ешь."
            "Игнорировать":
                window show
                "Ты делаешь вид, будто её нет."
        hide us with dissolve

    play music music_list["i_want_to_play"] fadein 0

    "Ты поворачиваешься к своей тарелке."
    play sound ds_sfx_mot
    res "Котлета пропала!"
    play sound ds_sfx_int
    lgc "Это могла сделать только она."
    lgc "Нет, точнее, это не мог сделать никто другой, кроме Ульяны!"
    show us grin pioneer at center   with dissolve
    me "Отдай котлету!"
    us "В большой семье рта не разевай!{w} Отвернулся – и нет котлеты!"
    me "Отдай, кому говорят!"
    window hide

    menu:
        "Попытаться отнять котлету":
            $ ds_lp['us'] += 1
            window show
            play sound ds_sfx_fys
            hfl "Ты грозно посмотрел на нее и уже было вытянул вперед руку..."
        "Ничего не делать":
            $ ds_semtype += 1
            window show
    us "Нету у меня ее, смотри!"
    play sound ds_sfx_mot
    per_eye "Действительно, ее тарелка пуста – похоже, она уже все съела…"
    show us laugh pioneer at center   with dspr
    us "Ты не расстраивайся, сейчас что-нибудь придумаем!"
    hide us  with dissolve
    "Она хватает твою тарелку и убегает куда-то так быстро, что ты даже не успеваешь опомниться."
    play sound ds_sfx_int
    lgc "Если уж они и хотели бы тебя отравить, можно было это сделать куда проще."
    "Ты решил не догонять ее."
    "Примерно через минуту Ульянка возвращается и протягивает тебе тарелку, на которой лежит дымящаяся котлета."
    window hide

    scene cg d1_food_normal 
    with dissolve

    window show
    us "Вот тебе, голодающий Поволжья!"
    window hide
    menu:
        "Принять":
            window show
            me "Спасибо…"
            sug "Только и смог сказать ты."
            $ ds_lp['us'] += 1
            $ ds_semtype -= 1
        "Гордо отказаться":
            window show
            me "Не очень-то мне и надо!"
            us "Бери уже, или ужинать не хочешь?"
            me "Нет, от тебя я не возьму!"
            $ ds_lp['us'] -= 1
            us "Ну не хочешь - как хочешь!"
            stop music fadeout 3
            scene bg int_dining_hall_people_day 
            with dissolve
            "Ты встаёшь и выходишь из столовой."
            $ ds_semtype += 1
            scene bg int_dining_hall_day 
            with dissolve
            jump ds_day1_think_square
        "{check=authority:13}Принять, но с гордостью":
            if skillcheck('suggestion', lvl_formidable):
                window show
                play sound ds_sfx_psy
                aut "{result}Обрати внимание: она побежала за тобой, а ты не просил!"
                me "Ну, я не просил, обошёлся бы и без еды."
                me "Только из уважения к тому, что ты бегала, возьму!"
            else:
                window show
                play sound ds_sfx_psy
                aut "{result}Всё-таки есть тебе хочется, и она знает об этом. Не выделывайся."
                me "Ладно, так уж и быть, возьму еду у тебя..."
            us "Да бери уже!"
            sug "Что-то тут всё-таки не так..."
            $ ds_skill_points['authority'] += 1

    stop music fadeout 3

    "Все подозрения вмиг развеялись – так тебе хотелось есть – ты подцепил вилкой котлету и…"
    play sound ds_sfx_fys
    hfl "И зря развеялись!"
    window hide

    scene cg d1_food_skolop 
    with vpunch

    play music music_list["doomed_to_be_defeated"] fadein 0

    window show
    th "Что это?!{w} Какой-то жук!{w} Нет, не жук!{w} Насекомое!{w} С ножками, шевелится!"
    window hide

    scene bg int_dining_hall_people_day 
    with dissolve

    if skillcheck('composure', lvl_up_medium, passive=True):
        play sound ds_sfx_mot
        window show
        com "{result}Но тебе удаётся не подать виду."
    else:
        play sound sfx_broken_dish
        play sound2 sfx_dropped_chair

        window show
        play sound ds_sfx_mot
        com "{result}Ты дёргаешься так, что тарелка летит на пол и разбивается вдребезги, а стул, падает."
        play sound ds_sfx_fys
        pat "И больно бьёт тебя по ноге."
        "Я с детства недолюбливаю насекомых, но если бы не такая неожиданность, то вряд ли бы {b}так{/b} испугался."
        th "Однако в такой ситуации…"
        th "Думаю, любой на моем месте…"
        $ ds_damage_morale()
        me "Ах ты, маленькая…"
    show us laugh2 pioneer far at center    with dissolve
    play sound ds_sfx_psy
    aut "Ульянка, похоже готовая к такому развитию событий, стоит уже в дверях и смеётся так, как будто услышала свежую шутку Петросяна."

    stop ambience fadeout 2

    play sound ds_sfx_mot
    res "Беги, пока не сбежала!"
    aut "Она как раз на это тебя и провоцирует. Не поддавайся."
    window hide
    menu:
        "{check=endurance:15}Бежать за ней":
            window show
            $ ds_lp['us'] += 1
            scene bg int_dining_hall_people_day 
            with dissolve
            "Ты бросаешься за ней."
            window hide
            if skillcheck('endurance', lvl_heroic):
                $ ds_skill_points['endurance'] += 1
                $ ds_caught_us = True
                scene bg ext_dining_hall_away_day:
                    zoom 1.05 anchor (48,27)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (25,25)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (-25,25)
                    repeat
                with dissolve

                window show
                play sound ds_sfx_fys
                edr "{result}Вы выбегаете из столовой."
                edr "Вас разделяет всего несколько десятков метров, и тебе кажется, что ты легко догонишь эту маленькую девочку."
                edr "Так и происходит - тебе удаётся её догнать."
                scene bg ext_dining_hall_away_day
                show us laugh pioneer close at center with dissolve
                play sound ds_sfx_mot
                us "Ай, отпусти, отпусти!"
                me "Ладно, но больше так не делай."
                hide us with dissolve
                "Ты отпускаешь её, и она убегает со смехом."
                th "Ну и ладно!"
                "И ты идёшь куда глаза глядят."
                jump ds_day1_think_square
            else:
                $ ds_skill_points['endurance'] += 1

                scene bg ext_dining_hall_away_day:
                    zoom 1.05 anchor (48,27)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (25,25)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (-25,25)
                    repeat

                window show
                play sound ds_sfx_fys
                edr "{result}Вы выбегаете из столовой."
                edr "Вас разделяет всего несколько десятков метров, и тебе кажется, что ты легко догонишь эту маленькую девочку."
                window hide

                scene bg ext_square_day:
                    zoom 1.05 anchor (48,27)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (25,25)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (-25,25)
                    repeat

                window show
                edr "Вы пробежали площадь…"
                window hide
                scene bg ext_clubs_day:
                    zoom 1.05 anchor (48,27)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (25,25)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (-25,25)
                    repeat

                window show
                edr "Помещение клубов…"
                window hide

                scene bg ext_path_day:
                    zoom 1.05 anchor (48,27)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (25,25)
                    ease 0.20 pos (0, 0)
                    ease 0.20 pos (-25,25)
                    repeat

                window show
                edr "Выбегаете на лесную тропинку."
                edr "Ты уже задыхаешься."
                edr "Потому что кое-кто так и не бросил курить!"

                stop music fadeout 5
                scene bg ext_path_day
                play sound ds_sfx_mot
                per_eye "Ульянка скрылась за очередным поворотом, и ты потерял ее из виду."
                th "Просто не может такого быть, что бы я не смог ее догнать!"
                th "Не может, и все тут!"
                edr "Ты стоял и пытаешься отдышаться."
                $ ds_damage_health()
                "..."
                window hide

                with fade2

                window show
                "Вечереет."
                th "Кажется, ты заблудился…"
                shi "Давай, возвращайся в лагерь! Ночью в лесу тебе точно делать нечего."
                "Однако ты совершенно, в какую сторону идти."
                th "Что же, придется наугад."
                "..."
                            
                window hide

                with fade2

                window show
                "..."
                window hide

                $ persistent.sprite_time = "sunset"
                scene bg ext_no_bus_sunset 
                with dissolve2

                $ sunset_time()

                play ambience ambience_camp_center_evening fadein 2

                window show
                "Через некоторое время ты выходишь к воротам лагеря."
                th "Все возвращается на круги своя."
                me "Автобус исчез..."
                play sound ds_sfx_int
                lgc "С одной стороны, в этом не было ничего странного, ведь не мог он тут просто так стоять вечно."
                lgc "С другой – значит, был все же водитель, он же не мог сам по себе..."
                play sound ds_sfx_psy
                ine "Или мог?"
                ine "Этот мир кажется слишком нормальным, но каждое явление здесь имеет как минимум два объяснения – обычное, реальное, повседневное и фантастическое."
                lgc "Да, конечно, водитель мог просто отойти перекусить, а ты слишком быстро ушел и вот..."
                th "Но в любом случае, мне здесь не место!"
                lgc "Есть у этого автобуса водитель или нет – это, наверное, важно, но куда важнее то, как ты вообще сюда попал."
                lgc "И куда это – {i}сюда{/i}..."
                "Ты уставился вдаль, словно пытаясь узнать в уносящихся к горизонту полях и лесах что-то знакомое."
                window hide

                with fade2

                window show
                "..."
                play sound ds_sfx_fys
                shi "Но ничего знакомого в окружающем тебя пейзаже нет."
                shi "Странный, непонятный, чужой мир.{w} Но при этом совсем не страшный."
                th "То ли окончательно отказал инстинкт самосохранения, то ли вся это беготня по лагерю, местные пионеры настолько меня убаюкали своей беззаботной нормальностью, что я иногда просто забывал о том, что со мной произошло буквально пару часов назад."
                play sound ds_sfx_mot
                com "Хотя, возможно, просто нет больше сил волноваться."
                th "Хочется тишины, спокойствия, просто отдохнуть от всего и уже потом со свежей головой продолжить искать ответы."
                th "Но это будет потом..."
                th "А что сейчас? Имею ли я право расслабляться?"

                stop ambience fadeout 2

                "..."
                window hide

                $ persistent.sprite_time = "night"
                scene bg ext_no_bus_night 
                with dissolve2

                $ night_time()

                play ambience ambience_camp_center_night fadein 2

                window show
                "Неведомо, сколько времени прошло, но уже совсем стемнело"
                play sound ds_sfx_fys
                hfl "и при всех прочих раскладах ночевать тебе все же лучше в лагере."
                "Ты уже собирался было идти назад, как вдруг кто-то бесшумно выныривает у меня из-за спины."
                jump ds_day1_sl_night
        "Не бежать":
            window show
            th "Да какая разница?"
            $ ds_semtype += 1
            svf "Да и вряд ли ты её догонишь."
            scene bg ext_dining_hall_away_day
            "Ты выходишь из столовой и идёшь куда-то."
            jump ds_day1_think_square

label ds_day1_think_square:
    scene bg ext_square_day with dissolve
    play ambience ambience_camp_center_day fadein 1
    "Ты выходишь на площадь и решаешь присесть на скамейку."
    play sound ds_sfx_fys
    shi "Ты прислушиваешься к шуму лагеря."
    shi "Ты не видишь и не слышишь ничего знакомого."
    shi "Впрочем, лагерь выглядит обычным лагерем. Пионеры ходят туда-сюда, как и вожатые."
    shi "Этот мир хоть и чужой, но выглядит совершенно не страшным."
    th "То ли окончательно отказал инстинкт самосохранения, то ли вся это беготня по лагерю, местные пионеры настолько меня убаюкали своей беззаботной нормальностью, что я иногда просто забывал о том, что со мной произошло буквально пару часов назад."
    play sound ds_sfx_mot
    com "Хотя, возможно, просто нет больше сил волноваться."
    th "Хочется тишины, спокойствия, просто отдохнуть от всего и уже потом со свежей головой продолжить искать ответы."
    th "Но это будет потом..."
    th "А что сейчас? Имею ли я право расслабляться?"
    window hide
    "..."
    window show
    $ sunset_time()
    scene bg ext_square_sunset with dissolve
    play ambience ambience_camp_center_evening fadein 1
    "Вечереет."
    "Ты уже ни о чём не думаешь, просто сидишь."
    play sound ds_sfx_mot
    per_hea "Потихоньку лагерь стихает."
    play sound ds_sfx_int
    lgc "Cобственно, оно и логично - пора спать."
    play sound ds_sfx_psy
    ine "Но если у всех тут есть дом, пусть и и виде палатки - то у тебя-то нет."
    ine "Ты всё-таки чужой для этого мира, хоть он и не подаёт виду."
    ine "А вот сможешь ли ты стать своим?"
    ine "Да и нужно ли тебе это?"
    ine "Возможно, стоит уделить больше времени возвращению домой?"
    play sound ds_sfx_int
    enc "Но как? Ты ничего не знаешь об этом мире, кроме того, что он похож на СССР."
    enc "Но CССР ли это?"
    lgc "И вообще, мы можем находиться за тысячи километров и десятилетия от нашего дома."
    th "И что же делать?"
    ine "Наверное, всё-таки стоит больше узнать об этом мире."
    ine "Возможно, сможешь узнать и причины."
    $ night_time()
    scene bg ext_square_night with dissolve
    play ambience ambience_camp_center_night fadein 1
    "За раздумьями ты не заметил, как наступила ночь."
    play sound ds_sfx_fys
    edr "Всё-таки пора бы уже найти себе хоть какой-то ночлег."
    edr "Попробуй спросить об этом у вожатой."
    "Ты встаёшь со скамейки и собрался было уходить с площади, как из-за спины у тебя кто-то выныривает."
    jump ds_day1_sl_night

label ds_day1_sl_night:
    show sl normal pioneer at center   with dissolve

    sl "Привет, что тут так поздно делаешь?"
    me "…"
    "Передо тобой стоит Славя."
    play sound ds_sfx_mot
    com "От неожиданности ты даже вздрогнул."
    if not ds_caught_us:
        show sl smile pioneer at center   with dspr
        sl "Не догнал Ульяну?"
        "Она улыбается."
        "Ты расстроенно киваешь головой и вздыхаешь."
        sl "Неудивительно.{w} Никто не может."
        play sound ds_sfx_psy
        ine "Да уж, девочка-ракета прямо.{w} Только вот сопла у нее в разные стороны…"
        show sl normal pioneer at center   with dspr
    sl "Ты, наверное, есть хочешь, поужинать-то тебе не удалось…"

    play sound sfx_stomach_growl channel 7
    $ renpy.pause(1)
    play sound ds_sfx_fys
    edr "Действительно, тебе бы следовало наконец поесть."
    show sl smile pioneer at center   with dspr
    "Славя улыбнулась."
    sl "Ну, тогда пойдем."
    window hide
    menu:
        "Согласиться":
            window show
            me "Ладно... только..."
        "{check=endurance:16}Отказаться и пойти спать":
            if skillcheck('endurance', lvl_godly):
                window show
                edr "{result}А впрочем можешь и без еды обойтись... наверное."
                me "Да нет... я пойду..."
                show sl normal pioneer at center with dspr
                sl "Ну ладно. Спокойной ночи!"
                hide sl with dissolve
                "А ты идёшь спать."
                jump ds_day1_meet_un
            else:
                window show
                edr "{result}Нет, ты слишком хочешь есть."
                sl "Ну я же вижу, что ты хочешь есть!"
                me "Ну ладно, как скажешь..."
        "Отказаться, но пойти самому":
            window show
            me "Да нет... я пойду..."
            show sl normal pioneer at center with dspr
            sl "Ну ладно. Спокойной ночи!"
            hide sl with dissolve
            "А ты идёшь спать."
            $ ds_no_sl_dinner = True
    if not ds_no_sl_dinner:
        me "А разве столовая уже не закрыта?"
        sl "Да ничего, у меня ключи есть."
        me "Ключи?"
        sl "Да, у меня от всех помещений лагеря ключи есть."
        me "А откуда?"
        sl "Ну, я здесь что-то вроде помощницы вожатой."
        me "Понятно.{w} Ну пойдем."
        play sound ds_sfx_psy
        sug "От такого предложения грех отказываться."
        window hide

        scene bg ext_square_night 
        with dissolve

        window show
        "Славя внезапно останавливается."
        show sl normal pioneer at center   with dissolve
        sl "Слушай, мне надо соседку предупредить, что я попозже буду, а то она сама такая пунктуальная – будет волноваться."
        sl "Ты иди пока к столовой, а я через минутку, хорошо?"
        me "Да…"
        window hide

    scene bg ext_dining_hall_away_night 
    with dissolve

    window show
    play sound ds_sfx_mot
    per_hea "Внезапно ты слышишь какие-то звуки у столовой."
    play sound ds_sfx_fys
    hfl "В столь поздний час там может быть кто-то, кроме тебя?"

    play sound sfx_campus_door_rattle

    per_eye "Хоть в темноте и невозможно точно разглядеть, но этот кто-то явно безуспешно пытается открыть дверь."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_dining_hall_near_night 
    with dissolve

    window show

    "Без всякой задней мысли ты поднимаешься на крыльцо."
    show dv normal pioneer at center   with dissolve
    per_eye "Это Алиса."
    th "Наверное, стоило подождать в сторонке..."
    "Она некоторое время пристально смотрит на меня, а потом начинает говорить."
    if not ds_beat_dv:
        dv "Что стоишь-то, помоги, что ли!"
        me "Что?"
        show dv angry pioneer at center   with dspr
        dv "Что-что… Дверь открыть, что!"
        me "Зачем?"
        dv "Булок я хочу… С кефиром! Не наелась!"
        me "Эээ…{w} А может, не стоит все же?"
        show dv smile pioneer at center   with dspr
        dv "А ты сам не хочешь есть, что ли?{w} Ульянка-то тебе поужинать нормально не дала!"
        "Она ехидно ухмыляется."
        play sound ds_sfx_fys
        edr "И то верно."
        play sound ds_sfx_psy
        sug "Вообще-то, сейчас Славя придёт... Она же помощница вожатой, явно сообщит ей."
    else:
        show dv angry pioneer at center   with dspr
        dv "Опять ты?!"
        dv "Пришёл вожатую позвать, небось?!"
    window hide
    menu:
        "{check=interfacing:12}Помочь Алисе" if not ds_beat_dv:
            $ ds_lp['dv'] += 2
            $ ds_karma -= 10
            window show
            th "Я видел в кино, как вскрывают замки... Что ж, попробуем применить навыки в жизни."
            play sound ds_sfx_mot
            inf "Прежде всего тебе нужен инструмент. Заколка подойдёт. {w}А тут как раз девушка, у которой их аж две!"
            me "Дай, пожалуйста, заколку."
            "Она дала мне нужный предмет."
            if skillcheck('interfacing', lvl_challenging):
                play sound_loop sfx_alisa_picklock
                inf "{result}Ты вставляешь заколку в замочную скважину... {w}шевелишь ею, прислушиваясь к звукам."
                inf "Замок тут несложный, так что он открывается на раз-два"
                $ renpy.pause(1.5)
                stop sound_loop
                $ ds_skill_points['interfacing'] += 1
                me "Прошу, заходи!"
                show dv smile pioneer at center with dspr
                "И вы заходите в столовую."
                $ ds_lp['sl'] -= 1
                jump ds_day1_dining_dv
            else:
                play sound_loop sfx_alisa_picklock
                inf "{result}Ты вставляешь заколку в замочную скважину... {w}и с ужасом осознаёшь, что не знаешь, что делать!"
                $ ds_skill_points['interfacing'] += 1
                show dv angry pioneer at center   with dspr
                dv "И чего ты там возишься?"
                dv "Не умеешь - не берись!"
                $ ds_damage_morale()
                play sound_loop sfx_far_steps
                "Тут послышались шаги."
                play sound ds_sfx_mot
                per_hea "Это шаги Слави."
                dv "Тогда я отчаливаю!"
                dv "А тебе это припомню!{w} За тобой уже второй должок!"
                "С этими словами она скрывается в ночи."
                hide dv  with dissolve
                play sound ds_sfx_mot
                res "А первый-то за что?"
                "..."
                window hide
                with fade
                window show
                stop sound_loop
                if ds_no_sl_dinner:
                    "И ты уходишь спать."
                    $ ds_damage_health()
                    jump ds_day1_meet_un
                else:
                    "Через некоторое время приходит Славя."
                    show sl normal pioneer at center   with dissolve
                    jump ds_day1_dining_sl
        "Предупредить Алису":
            $ ds_lp['dv'] += 1
            window show
            me "Так сейчас Славя придет и…"
            show dv rage pioneer at center   with dspr
            dv "ЧЕГО?!"
            th "Похоже, не стоило мне этого говорить."
            show dv angry pioneer at center   with dspr
            dv "Тогда я отчаливаю!"
            dv "А тебе это припомню!{w} За тобой уже второй должок!"
            "С этими словами она скрылась в ночи."
            hide dv  with dissolve
            play sound ds_sfx_mot
            res "А первый-то за что?"
            "..."
            window hide
            with fade
            window show
            if ds_no_sl_dinner:
                "И ты уходишь спать."
                $ ds_damage_health()
                jump ds_day1_meet_un
            else:
                "Через некоторое время приходит Славя."
                show sl normal pioneer at center   with dissolve
                jump ds_day1_dining_sl
        "Позвать Славю" if not ds_no_sl_dinner:
            $ ds_lp['dv'] -= 1
            $ ds_karma += 5
            window show
            "Ты решаешь проучить Алису и кричишь что есть мочи."
            me "Славя, иди сюда скорее! Тут режим нарушают!"
            show dv rage pioneer at center   with dspr
            dv "Ах ты предатель! Я тебе это обязательно припомню!"
            "С этими словами она скрылась в ночи."
            hide dv  with dissolve
            show sl normal pioneer at center   with dspr
            th "А вот и Славя."
            sl "Что такое? Зачем звал меня?"
            me "Да тут в столовую проникнуть решили..."
            sl "Кто?"
            window hide
            menu:
                "Рассказать":
                    window show
                    me "Алиса."
                    $ ds_betray_dv = True
                "Утаить":
                    window show
                    me "Не успел рассмотреть."
            sl "Ясно, завтра обязательно расскажу об этом вожатой."
            jump ds_day1_dining_sl
        "Молча наблюдать" if not ds_beat_dv:
            window show
            th "Лучше просто постою, не буду лезть."
            $ ds_semtype -= 1
            show dv normal pioneer at center with dspr
            $ renpy.pause(1.0)
            "Алиса продолжает увлечённо пытаться вскрыть замок."
            if ds_no_sl_dinner:
                window hide
                $ renpy.pause(2.0)
                window show
                show dv angry pioneer at center with dspr
                dv "Ты так и будешь смотреть и лыбиться?!"
                dv "Да пошло оно всё!"
                $ ds_lp['dv'] -= 1
                hide dv with dissolve
                "И ты уходишь спать."
                $ ds_damage_health()
                jump ds_day1_meet_un
            else:
                "В это время тихо появляется Славя."
                show sl smile pioneer at right with dspr
                "Она показывает тебе, чтобы ты молчал, а сама подкрадывается к Алисе."
                show sl smile pioneer at cright with dspr
                sl "Алиса, может, помочь тебе?"
                show dv scared pioneer at center with dspr
                dv "Cлавя?"
                show dv angry pioneer at center with dspr
                dv "Да что ты ко мне прицепилась? Поесть уже нельзя!"
                sl "Ну, правила есть правила."
                dv "Да идите вы все!"
                hide dv with dissolve
                show sl normal pioneer at center with dspr
                sl "Завтра доложу об этом вожатой."
                menu:
                    "Cогласиться":
                        me "Да, обязательно нужно сказать об этом."
                    "Возразить":
                        me "Ну, может, не стоит всё-таки?"
                        sl "Нет, я обязательно об этом скажу как помощница вожатой."
                jump ds_day1_dining_sl
        "{check=endurance:16}Уйти":
            if skillcheck('endurance', lvl_godly):
                window show
                play sound ds_sfx_fys
                edr "{result}Впрочем, сегодня ты и без ужина прекрасно проживёшь."
                "И ты уходишь."
                $ ds_semtype -= 1
                $ ds_lp['sl'] -= 1
                jump ds_day1_meet_un
            else:
                window show
                play sound ds_sfx_fys
                edr "{result}Твой желудок настаивает: тебе НАДО поесть!"
                "Ты пытаешься уйти, но из-за голода тебе становится тяжело передвигать ноги..."
                show dv laugh pioneer at center with dspr
                dv "Что ты тут за кривляния устраиваешь?"
                $ ds_damage_morale()
                if ds_no_sl_dinner:
                    window hide
                    $ renpy.pause(2.0)
                    window show
                    show dv angry pioneer at center with dspr
                    dv "Ты так и будешь смотреть и лыбиться?!"
                    dv "Да пошло оно всё!"
                    $ ds_lp['dv'] -= 1
                    hide dv with dissolve
                    "И ты уходишь спать."
                    $ ds_damage_health()
                    jump ds_day1_meet_un
                else:
                    show sl smile pioneer at cright with dspr
                    sl "Да, Семён, ты чего?"
                    show dv scared pioneer at center with dspr
                    dv "Cлавя?"
                    sl "Да, Алиса, это я. Смотрю, удачно зашла."
                    show dv angry pioneer at center with dspr
                    dv "Да что ты ко мне прицепилась? Поесть уже нельзя!"
                    sl "Ну, правила есть правила."
                    dv "Да идите вы все!"
                    $ ds_lp['dv'] -= 1
                    hide dv with dissolve
                    show sl normal pioneer at center with dspr
                    sl "Завтра доложу об этом вожатой."
                    menu:
                        "Cогласиться":
                            me "Да, обязательно нужно сказать об этом."
                        "Возразить":
                            me "Ну, может, не стоит всё-таки?"
                            sl "Нет, я обязательно об этом скажу как помощница вожатой."
                    jump ds_day1_dining_sl

            window show
            "Ты решаешь, что лучше вообще не лезть и обойтись без ужина, и уходишь."
            

label ds_day1_dining_sl:
    stop ambience fadeout 2

    sl "Ну что, пойдем?"
    window hide

    $ ds_lp['sl'] += 1

    scene bg int_dining_hall_night 
    with dissolve

    play music music_list["a_promise_from_distant_days"] fadein 5

    window show
    "Вы заходите в столовую."
    show sl normal pioneer at center   with dissolve
    sl "Подожди здесь, я сейчас что-нибудь принесу."
    hide sl  with dissolve
    "Ты садишься на стул и покорно ждёшь свою спасительницу."
    window hide

    show cg d1_sl_dinner 
    with dissolve

    window show
    "Ужин твой нехитрый – несколько булочек и стакан кефира."
    th "Немудрено – голодные пионеры, наверное, все съели подчистую."
    play sound ds_sfx_fys
    edr "Впрочем, и это куда лучше, чем большая часть твоего обычного рациона."
    "Пока ты ешь, Славя сидит напротив и смотрит на тебя."
    window hide
    menu:
        "Обратить внимание":
            window show
            me "Что, у меня что-то на лице?"
            show cg d1_sl_dinner_0  with dspr
            sl "Нет, просто…"
            "Она улыбается."
        "Промолчать":
            window show
            show cg d1_sl_dinner_0  with dspr
            "Она улыбается."
    sl "И как тебе первый день в лагере?"
    "Славя мечтательно уставилась в окно."
    window hide
    menu:
        "Класс!":
            window show
            me "Классно!"
            "Я посчитал, что не так-то уж и плохо здесь."
            sl "Отличный настрой, так держать!"
            $ ds_lp['sl'] += 1
        "Не знаю...":
            window show
            me "Ну, я даже не знаю..."
            $ ds_semtype -= 1
            "Глупо спрашивать у человека, попавшего в одночасье в другую реальность, понравились ли ему меню в столовой, вожатая и отведенное койкоместо."
            sl "Ничего, скоро привыкнешь!"
            th "По правде говоря, привыкать к подобному совершенно не хочется, но ведь она не знает..."
            th "Или по крайней мере делает вид, что не знает."
        "Не очень":
            window show
            me "Что-то не очень... не нравится мне тут."
            sl "Ну ничего... первый день, он часто такой."
            sl "Следующие будут лучше, вот увидишь!"

    show cg d1_sl_dinner  with dspr

    me "Ну а так, вообще, здесь мило."
    "Сказал я, чтобы прервать неловкое молчание."
    sl "Да?"
    "Без интереса спросила она."
    me "Да. Здесь так..."
    play sound ds_sfx_int
    rhe "Тебе хочется сказать «в стиле ретро», но лучше сдержаться."
    rhe "В конце концов, это для тебя – ретро, а для них?{w} Может, они другой жизни и не знают."
    rhe "Если тут вообще уместно понятие {i}жизнь{/i}..."
    sl "Как?"
    "Она внимательно смотрит на тебя.{w} Так, как будто от твоего ответа зависит что-то серьезное."
    me "Ну, я не знаю... мило. Да! Тут мило."

    show cg d1_sl_dinner_0  with dspr

    sl "Пожалуй."
    "Она вновь улыбнулась."
    sl "Очень хорошо, что ты так думаешь."
    me "Почему?"
    sl "Ну, не всем здесь нравится..."
    window hide
    menu:
        "Поинтересоваться её отношением":
            window show
            me "А тебе?"
            sl "Мне?"
            if skillcheck('empathy', lvl_trivial, passive=True):
                play sound ds_sfx_psy
                emp "{result}Кажется, она немного занервничала на этом вопросе."
            me "Да..."
            sl "Нравится, тут здорово."
            window hide
            menu:
                "Поддержать":
                    window show
                    me "Ну, тогда и не стоит волноваться о чужом мнении."
                    sl "А я и не волнуюсь особо."
                    "Славя еле заметно рассмеялась."
                    $ ds_lp['sl'] += 1
                "Промолчать":
                    window show
                "Обратить внимание на чужое мнение":
                    window show
                    me "Но другие же не просто так говорят, что им не нравится."
                    sl "Наверное, ты прав..."
        "Не интересоваться":
            window show
    th "Кажется, этот разговор уводит меня куда-то далеко, совсем не туда, куда я хотел попасть."
    sl "А вот ты волнуешься..."
    "Она прерывает твои размышления."
    me "Да? Почему?"
    sl "Ну, когда кто-то так сосредоточенно жует..."
    play sound ds_sfx_fys
    hfl "Ты никак не можешь себя заставить быть более осторожным с этой девочкой."
    hfl "Впрочем, почему именно с ней? С любым местным обитателем."
    hfl "Все они кажутся тебе совершенно нормальными."
    play sound ds_sfx_psy
    ine "А Славя еще и...{w} милой?"
    me "Извини."
    sl "Ничего."
    "Ты украдкой смотришь на нее, не зная что сказать."

    show cg d1_sl_dinner  with dspr

    sl "Прости, надо было показать тебе лагерь, а я совсем забегалась сегодня."
    me "Да я сам... Вроде осмотрел все более-менее."

    show cg d1_sl_dinner_0  with dspr

    sl "Прям-таки все-все?"
    play sound ds_sfx_mot
    com "Она улыбается так, что тебе приходится от смущения прятать глаза."
    me "Ну, откуда я знаю – все или нет, я же здесь первый день."
    sl "Ну хорошо, и что видел уже?"
    window hide
    menu:
        "Рассказать":
            window show
            me "Площадь, столовую вот видел, футбольную площадку..."
            sl "А пляж?"
            me "Только издалека."
            sl "Обязательно сходи! Или давай вместе сходим!"
            th "Пляж? Какой пляж? Одно место лучше другого – столовая, пляж. Какой пляж, вообще не понимаю..."
            window hide
            menu:
                "Принять":
                    window show
                    me "А... ну да, хорошо... сходим..."
                    $ ds_lp['sl'] += 1
                    $ ds_sl_beach_invite = True
                "Отклонить":
                    window show
                    me "Не... я пока не готов..."
                    sl "Ну ладно..."
        "Не рассказывать":
            window show
            me "Я сказал всё - значит всё."
            sl "Ты чего?.."
            sl "А, хотя понимаю, ты нервничаешь, наверное..."
    hfl "Естественность Слави тебя уже начинает пугать."
    th "А вдруг так все и должно быть, вдруг весь этот мир непонятен только мне, а для них он...{w} родной?"
    th "Может быть, я попал в прошлое?.."
    play sound ds_sfx_int
    lgc "Да, это бы многое объяснило."
    me "А можно задать глупый вопрос?"
    sl "Да, конечно, но..."
    window hide

    stop music fadeout 5

    $ persistent.sprite_time = "night"
    scene bg int_dining_hall_night 
    show sl normal pioneer at center 
    with dissolve

    window show
    "Славя быстро встаёт из-за стола."
    sl "Ой, уже так поздно... Сам дорогу до Ольги Дмитриевны найдешь?"

    me "Найду, конечн, но..."
    window hide
    menu:
        "Спросить, зачем":
            window show
            me "...зачем мне к ней?"
            sl "В палатку тебя поселит к кому-нибудь."
            me "Зачем?"
            show sl laugh pioneer at center   with dspr
            play sound ds_sfx_psy
            aut "Наверное, со стороны ты выглядишь глупо, потому что Славя рассмеялась."
            sl "Ну так спать тебе где-то надо!"
            me "Логично..."
        "Не спрашивать":
            window show
            me "Ай, ладно..."
    show sl smile pioneer at center   with dspr
    sl "Ладно, я побежала тогда.{w} Спокойной ночи!"
    me "Спокойной..."

    hide sl  with dissolve

    th "Странно, чего это она так внезапно убежала..."
    if skillcheck('perception', 8, passive=True):
        play sound ds_sfx_mot
        per_eye "{result}Твоё внимание привлекает связка ключей, торчащая из двери."
        th "Нужно её догнать, чтобы отдать ключи!"
        play sound ds_sfx_psy
        ine "А ты знаешь, где она живет? Или будешь стучаться посреди ночи во все палатки?"
        window hide

        menu:
            "Взять ключи":
                window show
                $ ds_sl_keys = True
                th "Все же лучше взять – завтра отдам – а то мало ли, что тут по ночам творится."
                hfl "Это тебе в первую очередь стоит опасаться."
                window hide
            "Не трогать":
                window show
                th "Хотя, с другой стороны, зачем они мне..."
                window hide

    scene bg ext_dining_hall_near_night 
    with dissolve

    play ambience ambience_camp_center_night fadein 5

    window show
    play sound ds_sfx_mot
    per_hea "Ночь хоть и тёмная, но совсем не тихая – отовсюду доносится стрекотание сверчков, пение ночных птиц, какие-то шорохи и прочие непонятные звуки."
    play sound ds_sfx_psy
    vol "Внезапно тебе очень захотелось последовать совету Слави и поскорее пойти к домику вожатой."
    window hide

    jump ds_day1_meet_un

label ds_day1_dining_dv:
    $ ds_dinner_dv = True
    stop ambience fadeout 2
    window hide
    scene bg int_dining_hall_night 
    with dissolve

    play music music_list["a_promise_from_distant_days"] fadein 5

    window show
    "Вы заходите в столовую."
    show dv smile pioneer at center   with dissolve

    dv "Чего стоишь, пойдём еду искать?"
    hide dv with dissolve
    window hide

    "Без особого труда вы попадаете на кухню."

    $ renpy.pause(1)

    "И возвращаетесь уже с едой."
    scene cg ds_day1_dv_dinner
    "Ужин твой нехитрый – несколько булочек и стакан кефира."
    th "Немудрено – голодные пионеры, наверное, все съели подчистую."
    play sound ds_sfx_fys
    edr "Впрочем, и это куда лучше, чем большая часть твоего обычного рациона."

    $ ds_up_health()

    $ renpy.pause(2)

    th "Может, попробовать заговорить с Алисой?"
    if skillcheck('perception', lvl_medium, passive=True):
        play sound_loop sfx_far_steps
        play sound ds_sfx_mot
        per_hea "{result}Не в этот раз! Шаги! {w}А вот и Славя!"
        play sound ds_sfx_fys
        hfl "Если не хотите поиметь проблем с вожатой - вам бы спрятаться..."
        window hide
        menu:
            "Спрятаться":
                window show
                me "Алиса, прячемся!"
            "Ждать расправы":
                window show
                "Ты делаешь вид, будто ничего не происходит."
                "И вот Славя заходит и видит вас сидящими в столовой."
                jump ds_day1_caught_dv
            "{check=savoir_faire:18}Cбежать одному":
                if skillcheck("savoir_faire", lvl_unimaginable):
                    window show
                    play sound ds_sfx_mot
                    svf "{result}Ты срываешься с места и быстро-быстро прыгаешь в открытое окно."
                    svf "Так, что ни Алиса, ни тем более Славя не успевают тебя поймать."
                    scene bg ext_dining_hall_away_night
                    with dissolve
                    $ ds_betray_dv = True
                    $ ds_lp['dv'] -= 5
                    "Славя зашла в столовую. До тебя доносятся обрывки её возмущённых речей."
                    sl "Алиса... ты... не по-пионерски... вожатой..."
                    play sound ds_sfx_psy
                    emp "Точно ли ты правильно поступил, подставив Алису?"
                    th "Никого я не подставлял..."
                    jump ds_day1_meet_un
                else:
                    window show
                    play sound ds_sfx_mot
                    svf "{result}Ты встаёшь со стула и собираешься было уйти, но Алиса окликивает тебя."
                    scene bg int_dining_hall_night
                    show dv angry pioneer at center
                    with dissolve
                    dv "Куда собрался?!"
                    $ ds_lp['dv'] -= 1
                    sl "И правда, куда собрался, Семён? Нам с тобой и Алисой надо поговорить."
                    play sound ds_sfx_mot
                    res "Cлавя. Поймала тебя."
                    dv "Ещё и Славя тут..."
                    jump ds_day2_caught_dv
    else:
        me "Алиса, а как тебе тут?"
        dv "В смысле? В лагере что ли?"
        dv "Да замечательно, только вот вожатая постоянно лезет со своими правилами, да и Славя тоже!"
        "Ты хотел было ответить, но тут тебе перебивают."
        sl "Кто тут звал Славю? А вот и я!"
        jump ds_day1_caught_dv
    scene bg int_dining_hall_night 
    with dissolve
    show dv surprise pioneer at center with dissolve

    dv "Чего?! Зачем?"
    me "Ты слышишь шаги?"
    me "Это Славя, она... {w}я слышал, что она собиралась в столовую зайти!"
    show dv scared pioneer at center with dissolve
    dv "Залезай под стол! Быстро!"
    play sound ds_sfx_mot
    res "Тебя упрашивать долго не пришлось - ты быстро залезаешь под стол."
    window hide

    scene cg ds_day1_dv_hiding with dissolve
    play music ds_evading fadein 5
    stop sound_loop

    window show
    sl "Кто тут?"
    sl "Выходите!"
    sl "Я вас всё равно найду! И расскажу обо всём Ольге Дмитриевне!"

    "Она начинает смотреть под столами."
    play sound ds_sfx_mot
    cor "Но ты успел захватить кружку! Попробуй отвлечь её!"
    cor "Как раз сейчас она отвернулась спиной к вам."
    window hide
    menu:
        "{check=coordination:10}Отвлечь":
            if skillcheck('coordination', lvl_medium):
                $ ds_skill_points['coordination'] += 1
                window show
                cor "{result}Ты бросаешь кружку куда-то в сторону кухни."
                play sound sfx_broken_dish
                sl "Вы на кухне?"
                th "Она идёт на кухню! Теперь можно бежать."
                $ ds_lp['dv'] += 1
                $ ds_sl_distracted = True
            else:
                $ ds_skill_points['coordination'] += 1
                window show
                play sound sfx_broken_dish
                cor "{result}Но увы, кружка выпадает у тебя из рук и падает, разбившись."
                dv "Ну ты и неумёха!"
                $ ds_damage_morale()
                "Славя подходит прямо к вашему столу и видит, что это вы."
                jump ds_day1_caught_dv
        "Не отвлекать":
            window show
        "Намеренно привлечь внимание":
            window show
            "Ты роняешь кружку вниз рядом с собой."
            "Само собой, Славя это слышит и приходит прямо к вам."
            jump ds_day1_caught_dv
    th "Попробовать бежать?"
    th "Но куда?"
    window hide
    menu:
        "В окно":
            window show
            me "Давай в окно! Только тихо."
            dv "Сама поняла уже!"
            scene bg int_dining_hall_night
            show dv normal pioneer at center with dissolve
            "И она легко и аккуратно пробегает к окну и прыгает туда."
            show dv normal pioneer:
                linear 1 xalign -0.5
            hide dv with dissolve
            window hide
            menu:
                "{check=savoir_faire:15}Прыгать":
                    window show
                    play sound ds_sfx_mot
                    svf "Теперь твоя очередь!"
                    if skillcheck('savoir_faire', lvl_heroic, modifiers=[('True', 1, 'Побег через окно'), ('ds_sl_distracted', 2, 'Отвлёк Славю')]):
                        svf "{result}У тебя тоже получается незаметно проскочить к окну и прыгнуть."
                        svf "Ты приземляешься на траву."
                        scene bg ext_dining_hall_away_night with dissolve
                        show dv smile pioneer at center with dissolve
                        dv "А ты всё-таки не совсем бестолковый. Сообразил, молодец!"
                        $ ds_up_morale()
                    else:
                        svf "{result}Но ты замешкиваешься, и Славя тебя замечает."
                        jump ds_day1_caught_alone
                "Подождать Славю":
                    window show
                    play sound ds_sfx_mot
                    svf "Что ты делаешь?"
                    jump ds_day1_caught_alone
        "В дверь":
            window show
            scene bg ds_int_dininghall_door_night 
            with dissolve
            show dv normal pioneer at center with dissolve
            show dv normal pioneer:
                linear 1 xalign 1.5
            hide dv with dissolve
            "Впрочем, Алиса уже пробежала в дверь, пока ты думал."
            window hide
            menu:
                "{check=savoir_faire:15}Бежать":
                    window show
                    play sound ds_sfx_mot
                    svf "Теперь твоя очередь!"
                    if skillcheck('savoir_faire', lvl_heroic, modifiers=[('ds_sl_distracted', 2, 'Отвлёк Славю')]):
                        $ ds_skill_points['savoir_faire'] += 1
                        svf "{result}У тебя тоже получается незаметно проскользнуть в дверь."
                        scene bg ext_dining_hall_away_night with dissolve
                        show dv smile pioneer at center with dissolve
                        dv "Фух, смогли проскочить незаметными!"
                    else:
                        $ ds_skill_points['savoir_faire'] += 1
                        svf "{result}Но ты замешкиваешься, и Славя тебя замечает."
                        jump ds_day1_caught_alone
                "Подождать Славю":
                    window show
                    play sound ds_sfx_mot
                    svf "Что ты делаешь?"
                    jump ds_day1_caught_alone
    stop music
    dv "Ладно, я побежала. Пока!"
    hide dv with dissolve
    "Ты решил пойти на площадь, а там и к вожатой."
    jump ds_day1_meet_un

label ds_day1_caught_dv:
    stop music
    scene bg int_dining_hall_night with dissolve
    show dv angry pioneer at left with dissolve
    show sl angry pioneer far at center with dissolve
    sl "Алиса? {w}И Семён?"
    show sl angry pioneer at center with dissolve
    sl "Ну ладно Алиса, у неё уже это не в первый раз..."
    dv "Да чтоб тебя!"
    sl "Но ты? Тебя же я и так хотела в столовую провести..."
    show dv rage pioneer at left with dissolve
    dv "Значит, это ты Славю и притащил?!"
    sl "Алиса, вообще-то я всё ещё тут!"
    sl "Ну так что ты скажешь, Семён?"
    window hide
    menu:
        "Взять вину на себя":
            window show
            me "Это я взломал столовую и утащил за собой Алису."
            $ ds_semtype += 1
            show sl surprise pioneer at center with dissolve
            show dv surprise pioneer at left with dissolve
            sl "То есть, это ты, а не Алиса, инициатор?!"
            me "Да."
            show sl serious pioneer at center with dissolve
            sl "Что ж, вожатая разберётся!"
            sl "А теперь идите."
            hide sl with dissolve
            scene bg ext_dining_hall_away_night with dissolve
            show dv shy pioneer at center with dissolve
            dv "Не поверила она, похоже..."
            dv "Но всё равно ты взял вину на себя..."
            dv "Даже не знаю, что сказать... спасибо, что ли."
            $ ds_lp['dv'] += 1
            window hide
            menu:
                "Не за что":
                    window show
                    me "Да не за что..."
                    $ ds_semtype -= 1
                "Покичиться":
                    window show
                    me "Вот видишь, какой я молодец!"
                    $ ds_semtype += 1
                    show dv angry pioneer at center with dspr
                    dv "А ты не зазнавайся!"
                "{check=instinct:11}Нужно оплатить натурой":
                    $ ds_semtype += 1
                    if skillcheck('instinct', lvl_up_medium):
                        window show
                        play sound ds_sfx_fys
                        ins "{result}Здесь идеальный момент... пусть заплатит за твою помощь натурой. Это непременно привлечёт её к тебе."
                        me "Ну, чего сказать... отсосёшь мне за завтраком."
                        show dv rage pioneer at center with dspr
                        dv "Ага, щас, разбежалась!"
                        dv "Не будь поблизости цербера в лице Слави - врезала бы тебе за такие слова!"
                        $ ds_lp['dv'] -= 1
                        $ ds_skill_points['instinct'] += 1
                    else:
                        window show
                        play sound ds_sfx_fys
                        ins "{result}Тебе кажется неуместным приплетать к этому секс."
                        $ ds_skill_points['instinct'] += 1
                "Помощь в долг":
                    window show
                    $ ds_semtype += 1
                    me "Ну... ты мне будешь должна за это."
                    show dv grin pioneer at center with dspr
                    dv "Вообще-то у тебя тоже есть должки!"
                    dv "Но так уж и быть, я тебе их спишу!"
                    play sound ds_sfx_psy
                    aut "Какая наглая особа!"
                    window hide
                    menu:
                        "{check=authority:8}Настаивать":
                            if skillcheck('authority', lvl_easy):
                                window show
                                aut "{result}Сбей с неё спесь: скажи, что ты уже учёл списывание долгов."
                                me "Ты не поняла: ты списываешь свои должки и остаёшься мне должна."
                                show dv angry pioneer at center with dspr
                                dv "Не преувеличивай свою значимость!"
                                dv "Да, ты помог, но выслуживаться перед тобой я не буду!"
                                $ ds_lp['dv'] -= 1
                                $ ds_skill_points['authority'] += 1
                            else:
                                window show
                                aut "{result}Но вообще она говорит разумно: по сути вы в расчёте."
                                $ ds_skill_points['authority'] += 1
                        "Отступить":
                            window show
                            th "Ладно, фиг с тобой!"
                            $ ds_semtype -= 1
                "Промолчать":
                    window show
            show dv smile pioneer at center with dissolve
            dv "Спокойной ночи, в общем!"
            hide dv with dissolve
        "Свалить вину на Алису":
            window show
            me "Это всё Алиса! Она вломилась в столовую!"
            $ ds_semtype -= 1
            dv "Это ты вообще-то взламывал замок!"
            me "Неправда!"
            dv "Да пошли вы все!"
            $ ds_lp['dv'] -= 4
            $ ds_betray_dv = True
            hide dv with dissolve
            sl "Стой, Алиса!"
            dv "Пусть вожатая разговаривает, отстаньте!"
            play sound ds_sfx_psy
            emp "Ну, вообще-то ты соврал. И этим очень обидел Алису."
            show sl serious pioneer at center with dissolve
            sl "Но тебя это от ответственности не освобождает!"
            sl "Ольга Дмитриевна во всём разберётся."
            hide sl with dissolve
            scene bg ext_dining_hall_away_night with dissolve
        "{check=half_light:13}Шугануть Славю":
            if skillcheck('half_light', lvl_formidable):
                window show
                play sound ds_sfx_fys
                hfl "{result}Просто дёрни рукой (но не бей её!), и бегите!"
                "Ты так и делаешь."
                $ ds_lp['sl'] -= 1
                $ ds_skill_points['half_light'] += 1
                show sl scared pioneer at center with dspr
                me "Бежим!"
                dv "Ладно..."
                "Вы выбегаете через дверь."
                scene bg ext_dining_hall_away_night with dissolve
                show dv normal pioneer at center with dissolve
                dv "Фух, всё-таки сбежали..."
                stop music
                dv "Ладно, я побежала. Пока!"
                hide dv with dissolve
                "Ты решил пойти на площадь, а там и к вожатой."
                jump ds_day1_meet_un
            else:
                window show
                play sound ds_sfx_fys
                hfl "{result}Ты пытаешься помахать кулаками, чтобы Славя напугалась... но безуспешно."
                show sl laugh pioneer at center with dspr
                sl "Что ты делаешь?"
                show dv angry pioneer at left with dspr
                dv "Вот и я без понятия!"
                play sound ds_sfx_psy
                aut "Ты лишь выставил себя посмешищем."
                $ ds_damage_morale()
                $ ds_skill_points['half_light'] += 1
                show sl serious pioneer at center with dspr
                sl "Ладно, идите!"
                scene bg ext_dining_hall_away_night with dissolve
                show dv angry pioneer at center with dissolve
                dv "И что это за цирковое представление ты устроил?"
                me "Да я хотел напугать её..."
                dv "А в итоге только рассмешил!"
                dv "Ладно, удачи!"
                hide dv with dissolve
                "Ты решил пойти на площадь, а там и к вожатой."
                jump ds_day1_meet_un
        "{check=physical_instrument:8}Атаковать Славю":
            if skillcheck('physical_instrument', lvl_easy):
                window show
                play sound ds_sfx_fys
                phi "{result}Это же девушка! Нанести ей удар - проще простого!"
                "И ты бьёшь её."
                $ ds_skill_points['physical_instrument'] += 1
                play sound sfx_lena_hits_alisa
                hide sl with dspr
                show dv shocked pioneer at center with dspr
                "Славя оказывается на полу без сознания."
                me "Алиса, бежим!"
                show dv angry pioneer at center with dspr
                dv "Ты что натворил, идиот?!"
                dv "Я никуда с тобой не побегу!"
                dv "Беги сам, раз уж тебе это так важно!"
                $ ds_lp['sl'] -= 3
                $ ds_lp['dv'] -= 2
                $ ds_lp['mt'] -= 1
                $ ds_karma -= 20
                $ ds_beat_sl = True
                show dv rage pioneer at center with dspr
                dv "А то тебя сейчас изобью до смерти!"
                "Алиса бросается к Славе, чтобы помочь ей."
                "А ты уходишь к себе."
                jump ds_day1_meet_un
            else:
                window show
                play sound ds_sfx_fys
                phi "{result}Однако, у тебя не получается ничего больше шлепка по щеке."
                $ ds_skill_points['physical_instrument'] += 1
                show sl angry pioneer at center with dspr
                show dv angry pioneer at left with dspr
                sl "Что ты делаешь, Семён?"
                dv "Да, что ты творишь?!"
                $ ds_lp['sl'] -= 1
                $ ds_lp['dv'] -= 1
                $ ds_karma -= 10
                show sl serious pioneer at center with dspr
                sl "Ладно, идите! Но вожатая узнает обо всём!"
                scene bg ext_dining_hall_away_night with dissolve
                show dv angry pioneer at center with dissolve
                dv "И что это было?"
                me "Да я хотел напугать её..."
                dv "А в итоге только хуже сделал!"
                dv "Cпокойной ночи!"
                hide dv with dissolve
                "Ты решил пойти на площадь, а там и к вожатой."
                jump ds_day1_meet_un
        "{check=savoir_faire:18}Улизнуть":
            if skillcheck('savoir_faire', lvl_unimaginable, modifiers=[('True', -1, 'Нужно увести и Алису')]):
                window show
                svf "{result}Ты быстро, резко проскальзываешь в дверь, утягивая Алису за собой."
                svf "Cлавя настолько удивлена, что не догадывается побежать за вами."
                $ ds_skill_points['savoir_faire'] += 1
                scene bg ext_dining_hall_away_night with dissolve
                show dv smile pioneer at center with dissolve
                dv "Фух, всё-таки смогли убежать!"
                show dv angry pioneer at center with dspr
                dv "Только в чём смысл?! Она знает, что это были мы, и теперь обо всём доложит вожатой!"
                dv "В общем, спокойной ночи!"
                hide dv with dissolve
                "Ты решил пойти на площадь, а там и к вожатой."
                jump ds_day1_meet_un
            else:
                window show
                svf "{result}Однако, Славя перегораживает вам проход."
                $ ds_skill_points['savoir_faire'] += 1
                scene bg ds_int_dininghall_door_night
                show sl angry pioneer at center
                show dv angry pioneer close at right
                with dissolve
                sl "Не так быстро!"
                dv "Да всё, дай нам уйти! Мы поняли, что поступили нехорошо бла-бла-бла..."
                show sl serious pioneer at center with dspr
                sl "Это серьёзное нарушение! Вожатая в любом случае узнает!"
                sl "Всё, теперь идите!"
                scene bg ext_dining_hall_away_night with dissolve
                show dv angry pioneer at center with dissolve
                dv "И в чём смысл этой акции был?! Она знает, что это были мы, и теперь обо всём доложит вожатой!"
                dv "В общем, спокойной ночи!"
                hide dv with dissolve
                "Ты решил пойти на площадь, а там и к вожатой."
                jump ds_day1_meet_un
    "Ты решил пойти на площадь, а там и к вожатой."
    jump ds_day1_meet_un

label ds_day1_caught_alone:
    stop music
    show sl surprise pioneer far at center with dissolve
    sl "Семён?"
    show sl angry pioneer at center with dissolve
    sl "И зачем ты залез в столовую?!"
    sl "Я же тебя и так собиралась провести сюда!"
    window hide
    menu:
        "Взять вину на себя":
            window show
            me "Да я просто... {w}слишком уж хотелось есть, а ты шла долго."
            me "Вот я и не выдержал и вломился в столовую."
            $ ds_lp['dv'] += 1
            $ ds_semtype += 1
        "Сдать Алису":
            window show
            me "Да это всё Алиса! Она взломала столовую."
            $ ds_semtype -= 1
            $ ds_lp['dv'] -= 4
            $ ds_betray_dv = True
            me "А я увидел открытую дверь и вошёл."
            sl "А ты естественно побежал нарушать."
            sl "В общем, с Алисой разберётся вожатая."
            sl "А что до тебя..."
        "{check=half_light:13}Шугануть Славю":
            if skillcheck('half_light', lvl_formidable):
                window show
                play sound ds_sfx_fys
                hfl "{result}Просто дёрни рукой (но не бей её!) и беги!"
                "Ты так и делаешь."
                $ ds_lp['sl'] -= 1
                $ ds_skill_points['half_light'] += 1
                show sl scared pioneer at center with dspr
                "Ты выбегаешь через дверь."
                scene bg ext_dining_hall_away_night with dissolve
                stop music
                "Ты решил пойти на площадь, а там и к вожатой."
                jump ds_day1_meet_un
            else:
                window show
                play sound ds_sfx_fys
                hfl "{result}Ты пытаешься помахать кулаками, чтобы Славя напугалась... но безуспешно."
                show sl laugh pioneer at center with dspr
                sl "Что ты делаешь?"
                play sound ds_sfx_psy
                aut "Ты лишь выставил себя посмешищем."
                $ ds_damage_morale()
                $ ds_skill_points['half_light'] += 1
                show sl serious pioneer at center with dspr
                sl "Ладно, иди!"
                scene bg ext_dining_hall_away_night with dissolve
                "Ты решил пойти на площадь, а там и к вожатой."
                jump ds_day1_meet_un
        "{check=physical_instrument:8}Атаковать Славю":
            if skillcheck('physical_instrument', lvl_easy):
                window show
                play sound ds_sfx_fys
                phi "{result}Это же девушка! Нанести ей удар - проще простого!"
                "И ты бьёшь её."
                play sound sfx_lena_hits_alisa
                hide sl with dspr
                "Славя оказывается на полу без сознания."
                $ ds_karma -= 20
                $ ds_lp['sl'] -= 3
                $ ds_lp['mt'] -= 1
                $ ds_beat_sl = True
                window hide
                menu:
                    "Помочь Славе":
                        window show
                        "Ты подбегаешь к Славе."
                        me "Славя! Славя!"
                        "Она приоткрывает глаза."
                        sl "А... что это было, Семён..."
                        me "Извини, я не хотел..."
                        show sl normal pioneer at center with dspr
                        sl "Да ладно... всё нормально... иди..."
                        "И ты уходишь."
                        scene bg ext_dining_hall_away_night
                    "Cбежать":
                        window show
                        $ ds_karma -= 10
                        "И ты сбегаешь."
                        scene bg ext_dining_hall_away_night
                "Ты идёшь к себе."
                jump ds_day1_meet_un
            else:
                window show
                play sound ds_sfx_fys
                phi "{result}Однако, у тебя не получается ничего больше шлепка по щеке."
                show sl angry pioneer at center with dspr
                sl "Что ты делаешь, Семён?"
                $ ds_lp['sl'] -= 1
                $ ds_karma -= 10
                show sl serious pioneer at center with dspr
                sl "Ладно, иди! Но вожатая узнает обо всём!"
                scene bg ext_dining_hall_away_night with dissolve
                "Ты решил пойти на площадь, а там и к вожатой."
                jump ds_day1_meet_un
        "{check=savoir_faire:18}Улизнуть":
            if skillcheck('savoir_faire', lvl_unimaginable):
                window show
                svf "{result}Ты быстро, резко проскальзываешь в дверь."
                svf "Cлавя настолько удивлена, что не догадывается побежать за тобой."
                scene bg ext_dining_hall_away_night with dissolve
                "Ты решил пойти на площадь, а там и к вожатой."
                jump ds_day1_meet_un
            else:
                window show
                svf "{result}Однако, Славя перегораживает тебе проход."
                scene bg ds_int_dininghall_door_night
                show sl angry pioneer at center
                sl "Не так быстро!"
                show sl serious pioneer at center with dspr
                sl "Это серьёзное нарушение! Вожатая в любом случае узнает!"
                sl "Всё, теперь иди!"
                scene bg ext_dining_hall_away_night with dissolve
                "Ты решил пойти на площадь, а там и к вожатой."
                jump ds_day1_meet_un
    show sl serious pioneer at center with dissolve
    sl "Чтоб это было в первый и последний раз! А то вожатой всё расскажу!"
    sl "А теперь иди!"
    hide sl with dissolve
    scene bg ext_dining_hall_away_night with dissolve
    "Ты решил пойти на площадь, а там и к вожатой."
    jump ds_day1_meet_un

label ds_day1_meet_un:
    scene bg ext_square_night 
    with dissolve

    window show
    play sound ds_sfx_psy
    vol "Непонятно почему, но вид неизвестного бронзового строителя коммунизма настраивает тебя на созидательный лад."
    "Ты присаживаешься на лавочку и начинаешь прокручивать в голове события минувшего дня."
    play sound ds_sfx_mot
    per_eye "Тут куда светлее, чем у столовой, да и изредка мимо пробегают запоздавшие пионеры, так что особого страха это место у тебя не вызывает."
    th "Автобус, лагерь, девочки…"
    "Ты так устал от всего нового и непонятного, что не можешь придумать ровным счетом ни единого объяснения всему происходящему…"
    play sound ds_sfx_mot
    per_hea "Со стороны соседней лавочки доносится тихое шуршание."
    "Я вздрогнул и посмотрел в ту сторону."
    scene cg ds_day1_un_book with dissolve
    th "Девочка.{w} Читает книгу."
    play music music_list["lets_be_friends"] fadein 5
    th "Лена."
    window hide
    menu:
        "{check=volition:10}Подойти":
            if skillcheck('volition', lvl_medium, modifiers=[('ds_ran_from_un', -1, 'Убежал ранее')]):
                window show
                play sound ds_sfx_psy
                vol "{result}Подойди и поговори с ней."
                th "Она единственная из новых знакомых, с кем мне не удалось сегодня перекинуться и парой слов."
            else:
                window show
                play sound ds_sfx_psy
                vol "{result}Не, у тебя не хватает решимости подойти к ней."
                "И ты проходишь мимо"
                jump ds_day1_home
        "Не подходить":
            window show
            play sound ds_sfx_psy
            vol "Ты решаешь не подходить к ней, и просто проходишь мимо."
            $ ds_semtype -= 1
            jump ds_day1_home
    scene bg ext_square_night with dissolve
    show un normal pioneer at center   with dissolve
    me "Привет, чего читаешь?"
    $ ds_lp['un'] += 1
    show un surprise pioneer at center   with dspr
    "Лена от удивления аж подпрыгивает на лавочке."
    me "Извини, не хотел тебя напугать!"
    show un shy pioneer at center   with dspr
    un "Ничего…"
    "Она краснеет и снова смотрит в книжку."
    me "Так что читаешь?"
    "Она показывает обложку – «Унесённые ветром»."
    jump ds_day1_un_dialogue

label ds_day1_un_dialogue:
    window hide
    menu:
        "Похвалить книгу":
            window show
            $ ds_lp['un'] += 1
            me "Хорошая книжка…"
            un "Спасибо..."
            th "Правда, я ее не читал, но ей, кажется, такая литература вполне подходит."
        "Спросить, про что книга" if not ds_know_novel_content:
            window show
            me "А про что она?"
            un "Да так, про любовь..."
            $ ds_skill_points['encyclopedia'] += 1
            $ ds_lp['un'] += 1
            jump ds_day1_un_dialogue
        "{check=encyclopedia:14}Вспомнить эту книгу" if (not ds_know_novel_content) and (not ds_get_novel_content_failed):
            if skillcheck('encyclopedia', lvl_legendary):
                play sound ds_sfx_int
                enc "{result}«Унесённые ветром» - роман американской писательницы Маргарет Митчелл, события которого происходят в южных штатах США до, во время и сразу после Гражданской войны."
                enc "Главная героиня - южная красавица Скарлетт О\'Хара - старшая дочь эмигранта-ирландца. Она считается первой невестой округи, но тайно влюблена в сына соседского плантатора Эшли Уилкса."
                enc "Узнав о предстоящей свадьбе Эшли с его кузиной Мелани Гамильтон, Скарлетт решает первая признаться ему в любви, надеясь, что он не сможет устоять и предпочтет бежать из дома, чтобы тайно сочетаться браком с ней. Однако благородный джентльмен Эшли, признаваясь в своей ответной любви к Скарлетт, всё же не может нарушить данное слово и отказаться от союза с кузиной."
                enc "Если кратко - типичный любовный роман."
                $ ds_know_novel_content = True
            else:
                play sound ds_sfx_int
                enc "{result}Нет, эту книгу ты точно не читал."
                $ ds_get_novel_content_failed = True
            $ ds_skill_points['encyclopedia'] += 1
            jump ds_day1_un_dialogue
        "Выразить неприятие":
            window show
            $ ds_lp['un'] -= 1
            me "И как можно такое читать?"
            un "Ну, мне нравится..."
            play sound ds_sfx_psy
            emp "Она с трудом скрывает обиду от твоих слов."
        "Ничего не говорить":
            window show
    play sound ds_sfx_psy
    emp "Лена, похоже, не собирается продолжать разговор."
    me "Ну, если я тебе мешаю..."
    show un normal pioneer at center   with dspr
    un "Нет."
    "Не отрывая взгляд от книжки, говорит она."
    window hide
    menu:
        "Посидеть с Леной":
            $ ds_lp['un'] += 1
            window show
            me "Можно я посижу с тобой тогда немного?"
            show un surprise pioneer at center   with dspr
            un "Зачем?"
            th "А ведь и правда – зачем?.."
            play sound ds_sfx_psy
            vol "Наверное, просто потому что очень устал и потому что в компании с кем-то лучше, чем одному."
            play sound ds_sfx_int
            lgc "А может быть, ты сможешь от нее что-то узнать."
            show un shy pioneer at center   with dspr
            "Ты внимательно осматриваешь Лену, от чего та краснеет."
            th "Нет, вряд ли..."
            me "Ну, просто так, не знаю... А что, нельзя?"
            un "Можно..."
            me "Но если я мешаю..."
            un "Нет, не мешаешь."
            me "Да нет, я могу и уйти..."
            un "Все в порядке."
            me "Ну, раз так..."
            "Ты аккуратно садишься на край лавочки."
            vol "После такого разговора тебе меньше всего хочется вообще находиться здесь, но и встать и уйти было как-то неудобно."
            me "Как-то нехорошо получилось..."
            "Лена ничего не отвечает."
            play sound ds_sfx_psy
            aut "Похоже, ты выставил себя дураком."
            aut "Будь на ее месте, допустим, Ульянка, наверняка бы тебя засмеяла."
            window hide
            menu:
                "{check=rhetoric:8}Попытаться завязать разговор":
                    window show
                    if not ds_dinner_dv:
                        play sound ds_sfx_int
                        rhe "Вспомни вопрос Слави. Он как нельзя лучше подойдет для начала разговора."
                        me "А тебе здесь нравится?"
                        $ ds_skill_points['rhetoric'] += 1
                        show un smile pioneer at center   with dspr
                        un "Да."
                        "Она еле заметно улыбается."
                        $ ds_lp['un'] += 1
                        me "И мне, наверное, нравится..."
                        show un normal pioneer at center   with dspr
                        play sound ds_sfx_psy
                        emp "Очевидно, что Лена не очень общительна и вряд ли в состоянии поддержать непринужденную беседу ни о чем, как Славя."
                        "Но в то же время в ней есть что-то (или тебе просто показалось), что привлекает внимание."
                        "Что-то такое мимолетное, как отблеск на очках дождливым осенним вечером, заставляющий обернуться и долго всматриваться в темноту, силясь увидеть там что-то, что мелькнуло на краю поля зрения."
                        play sound ds_sfx_mot
                        per_eye "Конечно, ты не успел это ни рассмотреть, ни даже хоть немного понять, что это вообще было."
                        play sound ds_sfx_fys
                        ins "Но почему-то оно кажется таким манящим..."
                        "Лена продолжает читать книгу, не обращая на тебя никакого внимания."
                        play sound ds_sfx_psy
                        vol "У тебя не возникает ни малейшего желания расспрашивать ее о происходящем в этом лагере, об этом мире вообще."
                        vol "Почему-то ты уверен, что она может знать об этом в последнюю очередь."
                        me "Красивая ночь..."
                        un "Да..."
                        play sound ds_sfx_int
                        rhe "Как завязать с ней разговор?!"
                    else:
                        window hide
                        if skillcheck('rhetoric', lvl_easy):
                            window show
                            play sound ds_sfx_int
                            rhe "{result}Спроси про лагерь. Хороший способ поддержать разговор... наверное."
                            me "А тебе здесь нравится?"
                            $ ds_skill_points['rhetoric'] += 1
                            show un smile pioneer at center   with dspr
                            un "Да."
                            "Она еле заметно улыбается."
                            $ ds_lp['un'] += 1
                            me "И мне, наверное, нравится..."
                            show un normal pioneer at center   with dspr
                            play sound ds_sfx_psy
                            emp "Очевидно, что Лена не очень общительна и вряд ли в состоянии поддержать непринужденную беседу ни о чем, как Славя."
                            "Но в то же время в ней есть что-то (или тебе просто показалось), что привлекает внимание."
                            "Что-то такое мимолетное, как отблеск на очках дождливым осенним вечером, заставляющий обернуться и долго всматриваться в темноту, силясь увидеть там что-то, что мелькнуло на краю поля зрения."
                            play sound ds_sfx_mot
                            per_eye "Конечно, ты не успел это ни рассмотреть, ни даже хоть немного понять, что это вообще было."
                            play sound ds_sfx_fys
                            ins "Но почему-то оно кажется таким манящим..."
                            "Лена продолжает читать книгу, не обращая на тебя никакого внимания."
                            play sound ds_sfx_psy
                            vol "У тебя не возникает ни малейшего желания расспрашивать ее о происходящем в этом лагере, об этом мире вообще."
                            vol "Почему-то ты уверен, что она может знать об этом в последнюю очередь."
                            me "Красивая ночь..."
                            un "Да..."
                            play sound ds_sfx_int
                            rhe "Как завязать с ней разговор?!"
                        else:
                            window show
                            rhe "{result}Но идей, как продолжить разговор, у тебя не возникает."
                            $ ds_skill_points['rhetoric'] += 1
                            "И мы просидели немного в тишине."
                "Уйти":
                    window show
            show un shy pioneer at center   with dspr
            un "Поздно уже, мне пора…"
            me "Да, поздновато…"
        "Пойти":
            window show
            me "Ладно, мне пора."
    un "Спокойной ночи."
    me "Спокойной…"
    hide un  with dissolve
    play sound ds_sfx_psy
    ine "Что-то в этой девочке тебе кажется странным."
    ine "Вроде бы и вполне типичный образ застенчивой, скромной пионерки, но…"
    ine "Запишем загадку Лены в массивный список загадок этого лагеря."

label ds_day1_home:
    scene bg ext_square_night with dissolve

    stop music fadeout 5
    "..."
    window hide

    with fade2

    window show
    th "Дело было вечером, делать было нечего…"

    stop ambience fadeout 2

    "Ты направляешься к домику Ольги Дмитриевны."
    window hide

    $ persistent.sprite_time = "night"
    scene bg ext_house_of_mt_night 
    with dissolve

    window show
    "В окне горит свет."
    "Ты входишь."
    window hide

    $ persistent.sprite_time = "sunset"
    scene bg int_house_of_mt_noitem_night 
    with dissolve

    play music music_list["smooth_machine"] fadein 5

    show mt normal pioneer at center   with dissolve

    window show

    mt "Привет, Семен!{w} Что-то ты долго!"
    me "Да…{w} Гулял, с лагерем знакомился."
    mt "Ладно.{w} Спать будешь здесь."
    "Она указывает на одну из кроватей."
    play sound ds_sfx_mot
    res "Ты несколько удивляешься такому повороту событий."
    window hide
    menu:
        "Принять":
            window show
            me "Ладно..."
        "Спросить":
            window show
            me "Здесь?.."
            show mt surprise pioneer at center   with dspr
            mt "Ну да, а что такого?{w} Все равно других свободных мест нет."
            show mt smile pioneer at center   with dspr
            "Вожатая улыбнулась, больше из вежливости, как мне показалось."
            mt "Ты же хочешь стать порядочным пионером?"
            "Она акцентировала внимание на слове «порядочным»."
            me "Да… Конечно…"
            "Ты задумываешься на мгновение."
    window hide
    menu:
        "Нагрубить":
            window show
            $ ds_rude_mt = True
            $ ds_semtype += 1
            me "Но ты-то не против?"
            $ ds_lp['mt'] -= 1
            show mt surprise pioneer at center   with dspr
            "Она как-то странно на тебя смотрит."
            play sound ds_sfx_psy
            emp "В ее взгляде читаются удивление и что-то вроде обиды."
            show mt angry pioneer at center   with dspr
            mt "Пионер должен уважать старших!"
            $ ds_karma -= 10
            me "Должен, конечно, кто же спорит…"
            "Лепечешь ты в ответ, не понимая, что же не так."
            mt "Или ты?.."
            show mt rage pioneer at center   with dspr
            "Она пристально смотрит на тебя."
            play sound ds_sfx_psy
            aut "От такого взгляда, расплавился бы и мифрил, выкованный в самых глубоких подземельях лучшими мастерами гномов."
            me "Что я?{w} Да что не так-то?"
            aut "От обиды и непонимания ты переходишь на тон выше."
            mt "Взрослых надо называть на Вы!"
            "Ты уставился на нее с широко открытым ртом."
            th "Нет, конечно, в этом лагере много странного…{w} Но эта девушка в лучшем случае на пару лет меня старше..."
            th "А возможно, и младше даже..."
            aut "Но тут лучше не спорить – несмотря на ее возраст крутым характером ее природа не обделила."
            aut "Да и с любым характером в твоём положении спорить не престало."
            me "Как скажете…"
            "Промямлил ты."
            show mt smile pioneer at center   with dspr
            mt "Так-то лучше!{w} Так и должен вести себя порядочный пионер!"
            th "По правде говоря, я не хотел становиться ни порядочным, ни беспорядочным пионером.{w} Ни даже стохастическим..."
            th "Да и вообще пионером становиться еще вчера в мои планы никак не входило."
            th "Но делать было нечего."
            th "«Не хочешь – заставим» – кажется, именно этим девизом планировала руководствоваться Ольга Дмитриевна."
        "Поинтересоваться местом и временем":
            window show
            me "Кстати, можете напомнить, где мы... и когда?"
            show mt surprise pioneer at center with dspr
            mt "В смысле? {w}Что с тобой?"
            $ ds_damage_morale()
            play sound ds_sfx_int
            dra "Мораль сей басни: не забывай, что для них ты не попаданец, а пионер."
            me "Просто... немного подзабыл."
            show mt smile pioneer at center   with dspr
            mt "Ладно..."
            mt "Сегодня 1987 год, 9 августа"
            mt "А мы в Калининской области, недалеко от ПГТ Работино"
            me "Да... точно, спасибо."
            $ ds_knowing += 1
        "Промолчать":
            window show
    if ds_beat_dv:
        show mt rage pioneer at center with dspr
        play music music_list["you_lost_me"] fadein 5
        mt "Кстати, позволь спросить у тебя."
        me "Да?"
        th "Что ей надо от меня ещё?"
        mt "А зачем ты побил Алису?!"
        play sound ds_sfx_psy
        emp "Ну и зачем это делать надо было?"
        emp "Нет, ты объясни: зачем ты избил девочку?"
        play sound ds_sfx_fys
        hfl "И зачем ты проявлял агрессию в неизвестном тебе месте?!"
        mt "И даже не вздумай отнекиваться: весь лагерь уже об этом знает!"
        mt "И да, кстати, это не Алиса про тебя сказала!"
        mt "И вообще говорила, что это ваше дело... но я так не считаю!"
        mt "Пионеру девушек бить вообще нельзя!"
        mt "Так зачем ты сотворил это?"
        window hide
        menu:
            "Самооборона":
                window show
                me "Она первая меня ударила, а я защищался."
                mt "Я, конечно, всё понимаю: Алиса - не самая покладистая девочка."
                mt "Но она всё ещё девочка! Бить девочек нельзя!"
            "Случайно вышло":
                window show
                me "Да это случайность..."
                mt "Ага, слишком уж нарочная случайность!"
            "Она заслуживает":
                window show
                me "Я считаю, она этого заслужила, совсем распоясалась."
                mt "Наказываю здесь я, а это не в твоих полномочиях. Ты лишь пионер!"
                mt "Да даже я не позволяю себе кого-либо бить, тем более девочек!"
        mt "Короче, завтра как хочешь, но ты должен перед ней извиниться. При мне!"
        stop music fadeout 5
    show mt normal pioneer at center with dspr
    mt "А теперь спать!"
    if ds_sl_keys:
        th "У меня же ещё ключи от столовой, те, что Славя забыла, остались..."
        window hide
        menu:
            "Отдать ключи Слави":
                window show
                me "Ольга Дмитриевна, я тут ключи нашёл."
                show mt surprise pioneer at center with dspr
                mt "Какие? {w}А, Славя потеряла..."
                mt "Видимо, не стоило ей их доверять..."
                mt "Ладно, завтра она своё получит."
                $ ds_lp['sl'] -= 1
                $ ds_lp['mt'] += 1
                $ ds_sl_keys = False
                $ ds_karma += 10
                $ ds_keys_return = True
            "Оставить ключи при себе":
                window show
                th "Нет, лучше отдам их самой Славе... или оставлю себе."
            "{check=interfacing:16}Отдать, но отцепить ключ себе":
                if skillcheck('interfacing', lvl_godly):
                    window show
                    inf "{result}Ты ловко двигаешь пальцами у себя в кармане... "
                    window hide
                    $ renpy.pause(0.5)
                    window show
                    inf "И в итоге туда проваливается какой-то ключик."
                    $ ds_karma -= 5
                    $ ds_skill_points['interfacing'] += 1
                    inf "Остальное ты вынимаешь и протягиваешь вожатой."
                    me "Ольга Дмитриевна, я тут ключи нашёл."
                    show mt surprise pioneer at center with dspr
                    mt "Какие? {w}А, Славя потеряла..."
                    mt "Видимо, не стоило ей их доверять..."
                    mt "Ладно, завтра она своё получит."
                    $ ds_lp['sl'] -= 1
                    $ ds_lp['mt'] += 1
                    $ ds_sl_keys = False
                    $ ds_karma += 10
                    $ ds_keys_return = True
                    play sound ds_sfx_mot
                    svf "А у тебя остался ключик! Только вот какой?"
                else:
                    window show
                    play sound sfx_keys_rattle
                    $ renpy.pause(0.5)
                    play sound ds_sfx_mot
                    inf "{result}Но ключи слишком громко шумят, и Ольга Дмитриевна обращает внимание."
                    $ ds_skill_points['interfacing'] += 1
                    show mt surprise pioneer at center with dspr
                    mt "Что это за звук?"
                    window hide
                    menu:
                        "Сказать про ключи":
                            window show
                            me "Да я про ключи вспомнил, доставал их, чтобы вам отдать."
                            show mt surprise pioneer at center with dspr
                            mt "Какие? {w}А, Славя потеряла..."
                            mt "Видимо, не стоило ей их доверять..."
                            mt "Ладно, завтра она своё получит."
                            $ ds_lp['sl'] -= 1
                            $ ds_lp['mt'] += 1
                            $ ds_sl_keys = False
                            $ ds_karma += 10
                            $ ds_keys_return = True
                        "{check=drama:13}Cоврать":
                            if skillcheck('drama', lvl_formidable):
                                window show
                                play sound ds_sfx_int
                                dra "{result}Скажите, мессир, будто это кто-то другой проходил."
                                dra "И главное - покажите, что вы тоже ищете источник."
                                me "Не знаю, тут ходит кто-то, наверное."
                                $ ds_skill_points['drama'] += 1
                                show mt normal pioneer at center with dspr
                                mt "А, ну ладно!"
                                dra "Про ключи лучше не говори."
                            else:
                                window show
                                play sound ds_sfx_int
                                dra "{result}Это не вы! Это точно не вы!"
                                me "Этот звук не от меня!"
                                mt "Точно? Покажи, что у тебя в кармане!"
                                "Ты достаёшь ключи."
                                $ ds_skill_points['drama'] += 1
                                $ ds_karma -= 10
                                show mt angry pioneer at center with dspr
                                mt "Значит, ключи украл? У Слави?!"
                                window hide
                                menu:
                                    "Прикрыть Славю":
                                        window show
                                        me "Да... извините..."
                                    "Рассказать правду":
                                        window show
                                        me "Да она просто их в столовой забыла, а я хотел вернуть."
                                        $ ds_lp['sl'] -= 1
                                        $ ds_karma += 5
                                mt "Отдавай ключи!"
                                play sound sfx_keys_rattle
                                "Тебе приходится их отдать."
                                $ ds_sl_keys = False
    window hide

    stop music fadeout 5

    scene bg black 
    with fade2

    window show
    "Ты ложишься, закрываешь глаза."
    play sound ds_sfx_fys
    edr "И только сейчас ты наконец-то обратил внимание, что вообще-то смертельно устал."
    play sound ds_sfx_fys
    pat "В голове что-то ужасно стучит, как будто у извилин началась ночная смена."
    "Однако они, похоже, больше были настроены на выпуск сталепроката, чем на работу с тонкой электроникой, так как ни о чем думать ты решительно не можешь."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_bus 
    show prologue_dream 
    with fade

    window show
    th "Перед глазами пролетал автобус..."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_square_day 
    show prologue_dream 
    with fade

    window show
    th "Площадь и памятник..."
    window hide

    $ persistent.sprite_time = "day"
    scene bg int_dining_hall_people_day 
    show us laugh pioneer at center 
    show prologue_dream 
    with fade

    window show
    th "Столовая, полная пионеров...{w} И наглое лицо Ульянки."
    window hide

    $ persistent.sprite_time = "day"
    scene bg ext_boathouse_day 
    show sl smile swim at center 
    show prologue_dream 
    with fade

    window show
    th "Славя..."
    window hide

    scene bg ext_square_night 
    show un night at center 
    show prologue_dream 
    with fade

    window show
    th "Лена..."
    window hide

    scene bg ext_houses_day 
    show dv angry pioneer2 at center 
    show prologue_dream 
    with fade
    play music ds_dream fadein 2
    $ persistent.sprite_time = "day"

    window show
    th "И даже воспоминания об Алисе не вызвали каких-то особо отрицательных эмоций."
    play sound ds_sfx_psy
    ine "Ну, разве что она о чём-то тебе напомнила. О чём-то, что ты ещё не осознал."
    play sound ds_sfx_psy
    vol "И лучше не осознавать..."
    window hide

    scene black 
    with fade3

    $ renpy.pause(2)

    window show
    th "Кажется, что я нахожусь в каком-то вакууме, а рядом со мной никого и ничего нет."
    th "Но не только рядом – нет вообще ничего, кроме меня."
    th "Я единственное существо во Вселенной."
    th "Как будто она вернулась в некое сингулярное состояние перед самым Большим Взрывом."
    th "И вот-вот что-то должно было произойти."
    "И вдруг ты слышишь голос."
    "Невозможно различить слов, но он кажется тебе знакомым."
    "Голос что-то нежно нашептывает, как будто убаюкивая."
    play sound ds_sfx_psy
    ine "Это был голос той Незнакомки из автобуса.{w} Той девушки из твоего сна."
    th "Но что она хочет мне сказать? Кто она?.."
    window hide

    window show
    play sound ds_sfx_mot
    per_hea "Её слова становятся отчётливее. Ты можешь разобрать, что она говорит."
    voice "Семён... Иди сюда."
    play sound ds_sfx_psy
    vol "Какая-то неведомая сила {i}заставляет{/i} тебя двигаться в сторону голоса."
    window hide
    # TODO: Заменить на изображение с более подходящим телом
    scene cg epilogue_mi_4 with hell_dissolve
    $ renpy.pause(10.0)
    window show
    ine "Пространство вокруг тебя начинает сгущаться, формируя какой-то образ..."
    voice "Cемён... Ты помнишь меня?"
    voice "Мы с тобой встречались уже..."
    ine "Спасибо, капитан (вернее капитанка) Очевидность!"
    me "Ты кто?"
    voice "Твои эмоции... Твои чувства... Твои воспоминания..."
    lim "Твои воспоминания о прошлом пробуждаются. Они несут в себе много боли. Много печали."
    arb "Ты уверен, что хочешь погрузиться в пучину горя и страданий?"
    arb "Разве не лучше будет пребывать в сладком забвении?"
    window hide
    menu:
        "Согласиться":
            window show
            vol "К сожалению, ты уже {i}не можешь{/i} остановить процесс."
            vol "Он полностью подсознательный. Прости, это не в моих силах."
        "Нырнуть глубже":
            window show
    lim "Ты боишься. Ты печалишься. Твоё прошлое преследует тебя, делая тебе хуже."
    arb "Подумай, что с тобой станет, если ты {i}продолжишь{/i} копаться в своём прошлом."
    arb "Куда ты зайдёшь, если продолжишь вспоминать былое, носящее в себе боль и утрату?"
    "Перед тобой проявилось дерево. На дереве подвешен труп."
    play sound ds_sfx_mot
    per_sme "Смрад отвратительный!"
    lim "Ты думаешь, тебе стоит подходить туда? Ты уверен, что {i}готов{/i} увидеть и услышать это?"
    me "Что?"
    arb "Унижение. Боль. Горе. Ненависть."
    "Ты подходишь к дереву."
    # TODO: CG с повешенным поблизости
    cr "Ты помнишь... свою юность?"
    me "Ты кто?"
    cr "То, что ты видишь... отвечай: помнишь?"
    me "Н-нет..."
    cr "Конечно, не помнишь... ты постарался это всё забыть... но оно всегда будет с тобой."
    cr "Ты помнишь... руку своей любимой на твоём лице?"
    me "Кого-кого?"
    cr "Помнишь... тепло её тела, тепло между ног, во рту?"
    cr "Куда это всё пропало?"
    window hide
    menu:
        "Я ушёл":
            window show
            me "Я ушёл..."
            cr "Нет, мой дорогой. Ты так пытаешься думать, что это зависело от тебя."
            cr "Это мир уходил от тебя. Пока ты лежал да яйца чесал - {i}она{/i} уходила от тебя."
        "Меня бросили":
            window show
            me "Меня бросили."
            cr "А ты просто позволил этому случиться. Даже не попытался побороться..."
            cr "И правда - зачем? Лучше лежать да яйца чесать, правда?"
            cr "Ну вот всё и ушло от тебя."
        "Отстань":
            window show
            me "Отстань! Слышишь, ОТСТАНЬ!"
            cr "Я - самый плохой день в твоей жизни. Я - твои неудачи. Думаешь, неудачи просто уходят, если их попросить?"
            cr "Нет, мой дорогой. Они всегда будут с тобой."
            cr "А вот {i}она{/i} - нет."
            me "Да о ком ты говоришь?!"
            cr "О той, которой ты позволил уйти..."
            cr "Пока ты лежал да яйца чесал - {i}она{/i} уходила от тебя."
    cr "А как же твои друзья? Где друзья? У человека должны быть друзья!"
    me "Я могу всё исправить..."
    cr "Да кого ты обманываешь? Ты уже провалился по полной."
    cr "Ты подвёл себя. Ты подвёл меня. Ты подвёл {i}весь мир{/i}."
    me "Я смогу... я смогу всё исправить!"
    cr "Ты не сможешь. Ты прекрасно знаешь, что не сможешь. Ты не сможешь подняться из того дна, куда сам себя и загнал!"
    me "Мой разум устал и разбит... Помоги мне!"
    arb "Помочь тебе? Извини, не слышу тебя. Всё это просто сон."
    scene black with hell_dissolve
    arb "Картины растворяются. Из пучины проявляется твоя кровать."
    arb "Твой сон и сном не назовёшь - ты ещё больше устал после него..."
    lim "Что-то не так... сны не должны быть такими ужасными."
    lim "Ты... начал вспоминать то, что давным-давно предпочёл забыть..."
    scene black with flash
    lim "Яркий луч света прорывается сквозь тьму."
    lim "Пора вставать и одеваться, Семён."
    play sound sfx_hell_alarm_clock
    lim "Добро пожаловать в наш дерьмовый мир обратно!"
    stop music fadeout 3

    jump ds_day2_morning
