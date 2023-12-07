# Конфиг для ESTool v1.001.
{

# Если `True`, выполняется тестовый прогон. Он ничего не меняет и не создает никаких файлов
# (кроме лога), но выявляет большую часть ошибок. Настоятельно рекомендуется сначала запустить
# с `True`, посмотреть лог, все ли верно отработало, и только потом сменить на `False`.
"dry_run": True,

# Если `False`, то портированный мод кладется в отдельную папку рядом. Если `True`, то он кладется
# *вместо* исходных файлов. С `True` работает быстрее за счет того, что не приходится копировать
# музыку и видео.
# Внимание: если вы поставите `True` и накосячите, то исправить будет СЛОЖНО. Если не уверены
# на 100% - лучше не трогайте эту настройку.
"in_place": False,

# При "in_place":True делаются резервные копии .rpy-скриптов (только скриптов!).
# Эта настройка задает, куда их класть:
# * Если "separate", то бэкапы создаются в отдельной папке (см. ниже).
# * Если "nearby", то бэкапы кладутся рядом с исходными файлами (с расширением ._rpy).
# * Если "none", то бэкапы НЕ создаются вообще.
# При "in_place":False эта настройка игнорируется (в бэкапах нет необходимости, поскольку исходные
# файлы остаются в целости и сохранности).
"backup_style": "nearby",

# При "backup_style":"separate" задает путь к папке с бэкапами. В него можно вписать
# дату и/или время. Полный перечень %-спецификаторов: http://strftime.org
"backup_location": "backups/%y-%m-%d_%H.%M.%S",

# Путь к папке с модом, который требуется портировать.
"src_path": "/home/src",

# Путь, куда класть результат. При "in_place":True переименовывает "src_path" в "dest_path".
"dest_path": "/home/dst",

# Если `True`, переименовывает файлы, чтобы в названиях была только латиница и базовая пунктуация.
# Кириллица транслитерируется на латинский.
"rename_non_ascii": True,

# Если `True`, умножает координаты в коде на 2/3.
"rescale_coordinates": True,

# К каждой строке кода, где были изменены координаты, дописывается комментарий особого вида.
# Эта настройка задает его тип:
# * Если "long", то в комментарий пишется исходная строка целиком.
# * Если "short", то просто делается пометка, что строка была изменена.
# * Если "none", то не дописывается никакого комментария. Внимание: если при "in_place":True
#   запустить скрипт два раза подряд с "none", то координаты будут изменены дважды! Остальные режимы
#   защищены от такого.
"comments_style": "long",

# Если `True`, сжимает изображения (в полтора раза). Требует наличия Python Image Library (PIL).
# Внимание: если при "in_place":True запустить скрипт два раза, картинки будут сжаты дважды!
"resize_images": True,

# Если в коде скриптов для доступа к файлам используется какой-то префикс, не отраженный в структуре
# каталогов (например, "mods/"), следует вписать его сюда. Иначе не будет работать замена путей.
"old_virtual_root": "",

# Аналогично, если в ходе портирования требуется добавить такой префикс, он указывается здесь.
"new_virtual_root": "Samantha",

# Шаблоны файлов, которые следует исключить из мода. `?` - любой одиночный символ,
# `*` - любое количество любых символов, `**` - любые подпапки.
# Внимание: при "in_place":True эти файлы будут УДАЛЕНЫ!
"exclude_patterns": [
    "**.rpyc", # Скомпилированные в байт-код скрипты.
    # "**/*.rpyc", # Эквивалентно выше написанному.
    "**/Thumbs.db", # Свойства папки (Windows).
    "**/.DS_Store", # Свойства папки (macOS).
    "**._rpy", # Наши бэкапы стиля "nearby" (старые удаляются, новые создаются).
],

# Правила по перемещению файлов. Задаются тройками: (префикс, шаблон, новый_префикс). Если путь
# к файлу начинается с указанного префикса и удовлетворяет шаблону, то этот префикс срезается и
# заменяется новым. Файл копируется/перемещается (в зависимости от "in_place") в новое место;
# также переписываются пути в скриптах.
# Правила пытаются примениться последовательно, так что порядок объявления важен.
"path_rewrite_rules": [
    # (prefix_to_strip, glob_to_test, prefix_to_prepend),
    ("/samantha/sprites.rpy", "",      "/ss_sprites.rpy"),
    ("/samantha/",            "*.rpy", "/"),
    ("/images/1080/bg/",      "**",    "/samantha/image/"),
    ("/images/1080/",         "**",    "/samantha/image/"),
    # Под это правило попадают все загружаемые в скриптах файлы, но оно ничего не меняет.
    # Необходимо для корректного переписывания путей в коде.
    ("/samantha/",            "**",    "/samantha/"),
],

# Дополнительные файлы, которые требуется добавить в мод.
"extra_files": [
    # (src, dest),
    ("sprites_lol.rpy", "/"),
],

}
