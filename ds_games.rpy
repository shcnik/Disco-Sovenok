# DISCO SOVENOK.
# РЕАЛИЗАЦИЯ МИНИ-ИГР (кроме карт)

init python:
    def ds_generate_poem():
        global ds_options
        global ds_cur_text
        result = ''
        if len(ds_cur_text) > 0:
            result += ds_cur_text[0]
        if len(ds_cur_text) > 1:
            result += ' ' + ds_cur_text[1]
        if len(ds_cur_text) > 2:
            result += ' ' + ds_cur_text[2] + '.'
        if len(ds_cur_text) > 3:
            result += '\n' + ds_cur_text[3]
        if len(ds_cur_text) > 4:
            result += ' ' + ds_cur_text[4] + '!'
        if len(ds_cur_text) > 5:
            result += '\nКак ' + ds_cur_text[5]
        if len(ds_cur_text) > 6:
            result += ' ' + ds_cur_text[6] + ','
        if len(ds_cur_text) > 7:
            result += '\nКак ' + ds_cur_text[7]
        if len(ds_cur_text) > 8:
            result += ' ' + ds_cur_text[8]
        if len(ds_cur_text) > 9:
            result += ' ' + ds_cur_text[9] + '.'
        return result
 
init:
    default ds_cur_text = []

    define ds_options = [
        ['Я помню', 'Не помню', 'Забыть бы', 'Купите', 'И на фиг', 'Какое', 'Угробил', 'Не очень', 'Открою', 'Ты чуешь?'],
        ["чудное", "странное", "некое", "вкусное", "пьяное", "свинское", "чёткое", "сраное", "нужное", "конское"],
        ["мгновенье", "затменье", "хотенье", "варенье", "творенье", "везенье", "рожденье", "смущенье", "печенье", "ученье"],
        ["Передо мной", "Под косячком", "На кладбище", "В моих мечтах", "Под скальпелем", "В моих штанах", "Из-за угла", "Промеж ушей", "В ночном горшке", "Из головы"],
        ["явилась ты", "добилась ты", "торчат кресты", "стихов листы", "забилась ты", "мои трусы", "поют дрозды", "из темноты", "помылась ты", "удар поддых"],
        ["мимолётное", "детородное", "психотропное", "нейролептиков", "очевидное", "невменяемо", "нам не чуждое", "благородное", "межушанское", "зело злобное"],
        ["виденье", "сиденье", "паренье", "сужденье", "вращенье", "сношенье", "смятенье", "паденье", "сплетенье", "бухтенье"],
        ["гений", "сторож", "символ", "булки", "правда", "ангел", "водка", "пиво", "злоба", "зависть"],
        ["чистой", "вечной", "тухлой", "просит", "грязной", "типа", "стрёмной", "в пене", "жаждет", "женской"],
        ["красоты", "мерзлоты", "суеты", "наркоты", "срамоты", "школоты", "пустоты", "простоты", "гопоты", "наготы"],
    ]

screen ds_poet(cur_text, options):
    add "mods/disco_sovenok/gui/games/poet.jpg"
    text cur_text:
        font "mods/disco_sovenok/gui/fonts/gogol_regular.otf"
        color "#5481db"
        size 24
        xpos 355
        ypos 200
    vbox:
        xpos 1035
        ypos 200
        for i in range(0, len(options)):
            textbutton "[i]. " + options[i - 1]:
                text_font "mods/disco_sovenok/gui/fonts/gogol_regular.otf"
                text_idle_color "#5481db"
                text_hover_color "#86cd4d"
                text_size 24
                xpos 355
                ypos 200
                action AddToSet(ds_cur_text, i)

label ds_day3_compose:
    show mi normal pioneer at center
    with dspr
    mi "Смотри. Выбери некоторые слова. Я буду подгонять под них другие слова."
    play sound ds_sfx_psy
    vol "Похоже, ничего сложного."
    mi "Итак, выбери первое слово. Зачин, начало, старт."
    $ ds_cur_text.clear()
    window hide
    show screen ds_poet(cur_text='', options=ds_options[0])
    with dissolve
    $ ui.interact()
    show screen ds_poet(cur_text=ds_generate_poem(), options=[])
    window show
    mi "Отлично! Теперь доверши строчку до конца!"
    window hide
    show screen ds_poet(cur_text=ds_generate_poem(), options=ds_options[1])
    $ ui.interact()
    show screen ds_poet(cur_text=ds_generate_poem(), options=ds_options[2])
    $ ui.interact()
    show screen ds_poet(cur_text=ds_generate_poem(), options=[])
    window show
    mi "Очень хорошо! Теперь позволь мне дописать за тебя вторую строчку согласно выбранному тобой настроению!"
    $ ds_cur_text.append(renpy.random.randint(0, 9))
    $ ds_cur_text.append(renpy.random.randint(0, 9))
    show screen ds_poet(cur_text=ds_generate_poem(), options=[])
    mi "Продолжай!"
    window hide
    show screen ds_poet(cur_text=ds_generate_poem(), options=ds_options[5])
    $ ui.interact()
    show screen ds_poet(cur_text=ds_generate_poem(), options=ds_options[6])
    $ ui.interact()
    show screen ds_poet(cur_text=ds_generate_poem(), options=[])
    window show
    mi "Теперь последняя строчка!"
    $ ds_cur_text.append(renpy.random.randint(0, 9))
    $ ds_cur_text.append(renpy.random.randint(0, 9))
    show screen ds_poet(cur_text=ds_generate_poem(), options=[])
    mi "А последнее слово я оставлю за тобой!"
    window hide
    show screen ds_poet(cur_text=ds_generate_poem(), options=ds_options[9])
    $ ui.interact()
    window show
    hide screen ds_poet
    scene bg int_musclub_day
    show mi smile pioneer at center
    with dissolve
    mi "Вот, смотри, что у нас получилось!"
    mi "{i}[ds_generate_poem()]{/i}"
    window hide
    menu:
        "Одобрить":
            window show
            me "Классно получилось!"
            show mi happy pioneer at center
            with dspr
            mi "Я согласна, Семён-кун! И это {i}ты{/i} сочинил. Поздравляю, ты молодец!"
        "Раскритиковать":
            window show
            me "Что-то как-то не очень..."
            show mi sad pioneer at center
            with dspr
            mi "А мне показалось неплохо..."
            me "Возможно... тебе виднее, наверное..."
    return
