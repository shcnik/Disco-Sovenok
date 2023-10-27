# DISCO SOVENOK
# КОНЦОВКИ

## EPIC FAIL

label ds_end_out_of_health:
    play sound ds_sfx_fys
    edr "Ты чувствуешь, как по твоему телу расходится ощущение боли..."
    me "Аааа... всё, я не могу..."
    edr "Ты падаешь, теряя сознание. Это конец."
    show blink
    scene black with dissolve2
    play music ds_endgame
    $ set_mode_nvl()
    "Cегодня в пионерлагере «Совёнок» от сердечного приступа скончался пионер Пёрсунов Семён."
    "Попытки местной медсестры, Коллайдер Виолетты Церновны, реанимировать его оказались безуспешны."
    "В силу отдалённости лагеря от ближайшего населённого пункта, пгт Работино, скорая помощь не сумела добраться вовремя."
    "Пионерлагерь был закрыт на время проверки качества работы его медслужбы и соблюдения норм безопасности."
    "Остальные пионеры были переданы в руки законных представителей в целости и сохранности."
    define menu = nvl_menu
    menu:
        "Завершить":
            hide blink
            return

label ds_end_out_of_morale:
    play sound ds_sfx_psy
    vol "Это оказывается для тебя последней каплей. Тебя охватывает отчаяние."
    me "Да пошло оно всё куда подальше!"
    vol "На свете не осталось слов, которые могли бы сделать тебе лучше."
    vol "Ты убегаешь в сторону леса."
    scene black with dissolve2
    play music ds_endgame
    $ set_mode_nvl()
    "Сегодня в лесу при пионерлагере «Совёнок» был найден повесившимся пионер Пёрсунов Семён."
    "Несколько пионеров, по сообщениям свидетелей, пытались его остановить, но к сожалению не преуспели."
    "Основная версия случившегося - самоубийство. Но мотивы установить на данный момент не удалось. Предсмертных записок обнаружено не было."
    "Родители тов. Пёрсунова, как по их словам, так и со слов знакомых, обеспечивали своего сына достойно. Проблем в личной жизни также не наблюдалось."
    "Пионерлагерь был закрыт на время проверки качества воспитательной работы."
    "Вожатую 1-го отряда, к которому принадлежал Семён, Миронову Ольгу Дмитриевну отстранили от должности за некомпетентность."
    "Отметим, что остальные пионеры были переданы в руки законных представителей в целости и сохранности."
    define menu = nvl_menu
    menu:
        "Завершить":
            return

label ds_end_bus_crash:
    # play sound sfx_achievement
    # show ds_ach_fail3 at achievement_trans
    # with dspr
    # $ renpy.pause(3, hard=True)
    # hide ds_ach_fail3

    scene black with dissolve2
    play music ds_endgame
    $ set_mode_nvl()
    "Cегодня в лесу неподалёку от пионерлагеря «Совёнок» был найден разбившийся автобус."
    "Внутри был найден единственный человек - школьник возраста 17 лет, находившийся в водительском кресле."
    "Он был опознан как Пёрсунов Семён, единственный сын советского посла в Японии."
    "К сожалению, он погиб, вылетев от удара в лобовое стекло и разбив голову о ствол дерева."
    "Предварительная причина аварии - тов. Пёрсунов не справился с управлением."
    "По нашим данным, он должен был приехать в лагерь на этом автобусе. Однако, по неизвестным причинам водитель пропал."
    "Пионерлагерь принёс свои соболезнования родителям Семёна. Начато расследование."
    define menu = nvl_menu
    menu:
        "Завершить":
            return

label ds_end_us_gone:
    scene black with dissolve2
    play music ds_endgame
    $ set_move_nvl()
    "Пионерлагерь «Совёнок» сегодня оказался под пристальным вниманием контролирующих органов."
    "Направленная в лагерь пионерка Советова Ульяна была найдена в товарном вагоне на ж/д станции Работино."
    "К счастью, девочка оказалась цела и невредима. На данный момент она передана родителям."
    "Пионерлагерь временно закрыт для проверки. Отдыхавшие в нём дети направлены по домам."
    "Поставлен вопрос об отстранении администрации лагеря и вожатой 1-го отряда, к которому принадлежала тов. Советова, Мироновой Ольги Дмитриевны."
    
    nvl clear

    "Во время перевозки пионеров из лагеря «Совёнок» на вокзал случилось таинственное происшествие."
    "Из автобуса ночью исчез пионер Пёрсунов Семён. Присутствовавшим в автобусе ничего об этом неизвестно."
    "Только водитель не спал, но он не видел, чтобы тов. Пёрсунов пытался выбраться из автобуса."
    "Также, все двери и окна целы, признаков попыток открыть их не обнаружено."
    "На данный момент ведутся поиски тов. Пёрсунова, на момент написания статьи безуспешно."
    "Данное происшествие окончательно убедило руководство пионерской организации в необходимости закрытия лагеря."
    "Миронова Ольга Дмитриевна, бывшая вожатая 1-го отряда, к которому принадлежали тт. Советова и Пёрсунов, признана некомпетентой, ей впредь запрещено занимать должность вожатой."
    "Отметим, что остальные дети были переданы в руки законных представителей в целости и сохранности."
    define menu = nvl_menu
    menu:
        "Завершить":
            return

label ds_end_mi_rape:
    $ set_mode_nvl()
    "13 августа 1989 г. в лагере «Совёнок» совершилось чудовищное преступление."
    "Один из пионеров, Пёрсунов Семён, совершил изнасилование известной японской певицы Хацуне Мику, приехавшей в Советский Союз в рамках кульутрного обмена."
    "Этот инцидент вызвал взрыв возмущения в японском обществе. Министерство иностранных дел СССР прикладывает все усилия для улаживания конфликта."
    "Посол СССР в Японии, Пёрсунов Александр Николаевич, чьим сыном и оказался преступник, отстранён с должности и отправлен в отставку."
    "Сам насильник был безоговорочно признан виновным по статье 117 УК РСФСР и приговорён к высшей мере наказания."
    "Пострадавшей тов. Хацуне оказывается вся необходимая медицинская и психологическая помощь."
    "Пионерлагерь, где было совершено преступление, закрыт. Все сотрудники и вожатые проверяются на предмет профпригодности."
    "Вожатая 1-го отряда, к которому принадлежал преступник, Миронова Ольга Дмитриевна, отстранена с запретом на занятие поста вожатой."
    define menu = nvl_menu
    menu:
        "Завершить":
            return

label ds_end_electrocution:
    play music ds_endgame
    $ set_move_nvl()
    "Сегодня в пионерлагере «Совёнок» из-за нарушения правил техники безопасности случилось сметрельное происшествие."
    "Как сообщили тт. Сыроежкин и Демьяненко, пионер Пёрсунов Семён, работая со своими товарищами над роботом, получил удар электрическим током."
    "В нарушение правил у детей в клубе кибернетиков имелся свободный доступ к электросети 220 В, что вкупе с употреблением чая в процессе работы над роботом и привело к трагедии."
    "Лагерь закрыт до устранения нарушений. Рассматривается вопрос об отстранении администрации лагеря и вожатой 1-го отряда Мироновой Ольги Дмитриевны от должностей."
    "Похороны тов. Пёрсунова планируются в ближайшее время. Остальные дети переданы законным представителям в целости и сохранности."
    define menu = nvl_menu
    menu:
        "Завершить":
            return

## АЛИСА

## ЛЕНА

## CЛАВЯ

## УЛЬЯНА

label ds_end_escape_with_us:
    scene bg ext_path2_day
    with dissolve
    "Вы идёте из города в сторону леса."
    "Наконец, вы решаете сделать привал."
    show us calml sport at center
    with dissolve
    us "Всё, я устала!"
    me "Да, давай отдохнём..."
    me "Кстати, нам надо будет сделать себе жильё..."
    show us smile sport at center
    with dissolve
    us "Мы с тобой прям как Пятница и Робинзон!"
    "Она тебя не слушает."
    me "Ага, по-русски..."
    "Ты собираешь ветки в округе, чтобы построить шалаш."
    hide us with dissolve
    window hide
    $ renpy.pause(3.0)
    window show
    me "Всё, готово!"
    show us surp1 sport at center
    with dissolve
    us "А где домик?"
    me "Ветки я собрал! А домик будем строить сейчас!"
    show us smile2 sport at center
    with dissolve
    us "О, давай! Приступаем!"
    hide us with dissolve
    window hide
    $ renpy.pause(3.0)
    scene ext_path2_sunset
    with dissolve
    window show
    "К вечеру вы достраиваете какой-никакой шалаш."
    show us upset sport
    with dissolve
    us "Всё, я устала..."
    hide us with dissolve
    "C этими словами она залезает в домик."
    "Ты забираешься вслед за ней."
    scene stars 
    with dissolve
    play sound ds_sfx_psy
    vol "Ты же понимаешь, что берёшь этим шагом на себя большую ответственность?"
    vol "Не только за себя - за Ульянку. А ведь она же ещё ребёнок..."
    th "Да, наверное, будет нелегко... но я справлюсь!"
    vol "Ну смотри... твой выбор. Удачи тебе на пути!"
    show blink
    scene black
    with dissolve
    hide blink
    $ renpy.pause(3.0)
    scene ext_path2_day
    show unblink
    show us smile sport at center
    with dissolve
    us "Подъём! Проснись и пой!"
    me "Уже встаю..."
    show us sad sport at center
    with dspr
    us "Я проголодалась уже..."
    play sound ds_sfx_fys
    edr "И ты тоже, между прочим."
    edr "Вам не остаётся ничего, кроме как идти к людям."
    play sound ds_sfx_int
    lgc "Лучший вариант - в деревню."
    me "Тут есть деревни?"
    show us normal sport at center
    with dissolve
    us "Ну да... а, я поняла!"
    show us laugh sport at center
    with dissolve
    us "Мы будем как дядя Фёдор с Матроскиным в Простоквашино жить!"
    me "Ага, типа того..."
    "И вы выдвигаетесь."
    scene bg ds_field_day
    with dissolve
    "Спустя некоторое время вы выходите на поле. Вдали виднеется деревня."
    show us normal sport at center
    with dissolve
    me "Идём туда!"
    us "Идём!"
    me "Кстати... а ты не беспокоишься о своих родных, они же искать тебя будут?"
    show us dontlike sport at center
    with dspr
    us "Да я умоляю тебя: никто искать меня не будет!"
    show us sad sport at center
    with dspr
    us "Никогда я не волновала своих родителей! Они только рады будут от меня избавиться!"
    play sound ds_sfx_psy
    emp "Вот как... так вот почему она так легко всё бросила..."
    play sound ds_sfx_psy
    vol "Ты же понимаешь, что теперь ты должен стать для неё кем-то вроде отца?"
    th "Да... я постараюсь..."
    show us normal sport at center
    with dspr
    us "А ты? Ты-то почему решил со мной сбежать?"
    me "А... да так, отношения не сложились... расстался с любимой девушкой, теперь не вижу смысла в жизни в обществе."
    show us smile sport at center
    with dspr
    us "Да ладно тебе! Всё наладится! Будут у тебя отношения!"
    show us laugh sport at center
    with dspr
    us "Со мной! Когда я подрасту!"
    "И она целует тебя в щёку."
    me "Да... у нас всё обязательно получится!"
    hide us with dissolve
    "И с этими словами ты направляешься в деревню, ведя Ульянку за собой."
    "Что готовит вам грядущее? Неясно. Но вы уверены, что справитесь со всем - вместе."
    scene black with dissolve2
    $ renpy.movie_cutscene('mods/disco_sovenok/video/titles_us_escape.ogv')
    return

## МИКУ

## ЭЛЕКТРОНИК

## ОЛЬГА

## ЖЕНЯ

## ЯНА

## ВИОЛА

## ОДИНОЧКА