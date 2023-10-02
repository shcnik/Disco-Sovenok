# DISCO SOVENOK.
# РЕАЛИЗАЦИЯ ИГРЫ В КАРТЫ 2 ДНЯ
# Код турнира взят из мода «7 дней лета» (с переименованиями во избежание конфликтов и некоторыми модификациями)

init -1000 python:
    from functools import partial

init -50 python:
    """
    Стили игры:
    'defense' - защищаемся (если есть хоть что-то на руках - защищаем эту комбинацию)
    'gamble' - рискуем (если "недофлеш", "недострит" - 4 из 5 - и есть пара или 2+2 - допускаем разбитие комбинации)
    'succumb' - играем в поддавки (специальный слив партии) - "защита" наоборот
    'foolplay' - валяем дурака(анализ проводится, но ходы - 100% рандом)
    для вышеперечисленного возможен рандом на "ошибку" ('foolplay') ; вероятность меняется:
    5 - рандом исключен,
    4, 3, 2, 1 - соответственно 20, 40, 60, 80 % вероятность ошибки.
    """
    import random

    class DSCardGameRivalWise:                                                  # УМНЫЙ (ну, почти) СОПЕРНИК

        def __init__(self, avatar, name, behavior = 'defense', skill = 5):      # свойства нашего соперника (аватар и имя передаются при вызове, поведение и "навык" МОЖНО передать при вызове)
            self.name = name                                                    # имя - передаём
            self.mood = 0                                                       # режим аватара - присваиваем по ходу дела
            self.avatar = avatar                                                # аватарку передаём
    # ---------------------------------------------------------------------
            self.combo_in_hand = None                                           # комбинация в руке
            self.combo_was_before = None                                        # комбинация, что была раньше
            self.as_changed_combo = 'unclear'                                   # как комбинация изменилась (никак, хуже, лучше) ('does', 'worse', 'better')
            if behavior in ['defense','gamble','succumb','foolplay']:           # если стиль игры из предопределённых
                self.playstyle = behavior                                       # поведение в игре - по переданному
            else:                                                               # Если же стиль не опознали
                self.playstyle = 'defense'                                      # поведение в игре - принимаем защитное
            if skill > 5:                                                       # если переданный "навык игры" больше 5
                self.mistake_chance = 5                                         # принимаем шанс ошибиться 0
            elif skill < 1:                                                     # если переданный "навык игры" меньше 1
                self.mistake_chance = 1                                         # принимаем шанс ошибиться 80%
            else:                                                               # если от 1 до 5
                self.mistake_chance = skill                                     # шанс ошибиться - по переданному
            self.make_mistakes = False                                          # при очередном ходе ошибаемся ?
            self.yourself_need_cards = []                                       # нужные нам карты - карты входят в актуальную комбинацию
            self.would_not_want_give = []                                       # карты, которые не хотелось бы отдавать
            self.can_give_in_a_pinch = []                                       # карты, которые можно отдать в крайнем случае
            self.waste_cards = []                                               # мусор (не входят в актуальную комбинацию)
            self.this_give_definitely_succumb = []                              # список карт, которые нужно отдать, если 'succumb'
            self.its_urgent_shove = []                                          # это срочно спихнуть (первый приоритет на обмен/отдачу)
            self.these_proposed_to_take = []                                    # эти карты предлагать на обмен/отдачу
            self.pick_this_cards_urgently = []                                  # забрать эти карты у Семёна СРОЧНО
            self.pick_this_cards_afterwards = []                                # забрать эти карты у Семёна ПОТОМ
            self.never_touch_cards = []                                         # а эти карты у Семёна не трогать
            self.pulled_player_card = 7                                         # за какой картой потянулся Семён (7 - такой в игре нет, для проверки)
            self.what_we_trying_foist_7 = 7                                     # что нам хочет отдать Сеня на 7 картах
            self.dragged_player_card = 7                                        # какую карту вытащил Семён
            self.degree_usefulness_card = 0                                     # степень "полезности" вытащенной карты
            self.inserted_player_card = 7                                       # в каком месте у Семёна наша карта
            self.table_card_points = []                                         # таблица очков карт на руках
            self.table_card_suit = []                                           # потенциальный флеш
            self.table_card_sequence_min = []                                   # потенциальный стрит младший/минимальный (от пятёрки)
            self.table_card_sequence_max = []                                   # потенциальный стрит старший/максимальный
            self.table_card_possible_combo = []                                 # возможная комбинация (флеш, стрит)
            self.player_conceal_card = False                                    # "прячет" ли Семён эту карту
            self.player_unnecessary_card = 7                                    # эта карта у нас Семёну, вероятно, не нужна (отдал сразу или подсунул на 7-ми картах)
            self.player_accept_card = 7                                         # эта карта у нас Семёну, вероятно, нужна (защищал её)
            self.last_selected_card = 7                                         # последняя выбранная карта (используется в режиме слива)

    # МЕТОДЫ НОВЫЕ ========================================================================================
        def what_we_have(self):                                                 # что же мы таки имеем на руках
            self.combo_in_hand = ds_what_category(cards_rival)                 # вызываем определение своей комбинации
            self.choice_need_cards()                                            # получаем индексы нужных нам карт
            self.choice_waste_cards()                                           # а также - индексы ненужных
            self.what_cards_have()                                              # и получаем значения очков
# ----------------------------------------------------
        def check_for_four_suit(self):                                          # проверим на ЧЕТЫРЕ в мастях
            global types                                                        # понадобится список мастей
            self.table_card_suit = []                                           # очищаем таблицу
        #-------------------------------------------
            total_2ch = 0                                                       # количество карт масти 2ch
            total_ussr = 0                                                      # количество карт масти ussr
            total_utan = 0                                                      # количество карт масти utan
            total_uvao = 0                                                      # количество карт масти uvao
            suit_max = 0                                                        # количество карт максимальной масти
            suit = None                                                         # максимальная масть
        #-------------------------------------------
            for i in range(0,n_cards):                                          # перебираем свои карты
                if cards_rival[i].name[1] == "2ch":                             # если карта ЭТОЙ масти
                    total_2ch += 1                                              # увеличиваем счетчик ЭТОЙ масти на 1
                elif cards_rival[i].name[1] == "ussr":
                    total_ussr += 1
                elif cards_rival[i].name[1] == "utan":
                    total_utan += 1
                elif cards_rival[i].name[1] == "uvao":
                    total_uvao += 1
        #-------------------------------------------
            suit_max = max(total_2ch,total_ussr,total_utan,total_uvao)          # выясняем максимум карт одной масти
        #-------------------------------------------
            if suit_max >= 4:                                                   # если максимальное количество карт в масти 4 или больше
                if suit_max == total_2ch:                                       # если max = ЭТОЙ масти
                    suit = types[0]                                             # масть = из списка мастей [номер в нём] - ["2ch","ussr","utan","uvao"]
                elif suit_max == total_ussr:
                    suit = types[1]
                elif suit_max == total_utan:
                    suit = types[2]
                elif suit_max == total_uvao:
                    suit = types[3]
                for j in range(0,n_cards):                                      # ещё раз перебираем карты
                    if cards_rival[j].name[1] == suit:                          # если очередная карта нужной масти
                        self.table_card_suit.append(j)                          # добавляем её номер в список мастей
# ----------------------------------------------------
        def check_for_four_sequence(self):                                      # проверим на ЧЕТЫРЕ подряд
            cardset_tmp = cards_rival[:]                                        # копируем кардсет, упражняемся с ним, не трогаем основной
            self.table_card_sequence_min = []                                   # очищаем таблицы
            self.table_card_sequence_max = []                                   # очищаем таблицы
            values_max = []                                                     # возможная максимальная последовательнось (туз старший)
            values_min = []                                                     # возможная минимальная последовательнось (туз младший)
            values_max_1 = []                                                   # очищаем таблицу первой возможной последовательности
            values_max_2 = []                                                   # очищаем таблицу второй возможной последовательности
            values_max_3 = []                                                   # очищаем таблицу третьей возможной последовательности
            values_max_com_12 = []                                              # очищаем таблицу первой последовательности на 2-х
            values_max_com_23 = []                                              # очищаем таблицу второй последовательности на 2-х
            triplex_seq = 0                                                     # сколько последовательностей по три
        #-------------------------------------------
            len_seq_max = 0                                                     # количество карт в максимальной последовательности
            seq_value_max = 0                                                   # старшая карта в последовательности
            len_seq_1 = 0                                                       # количество карт в первой последовательности
            seq_value_1 = 0                                                     # старшая карта в первой последовательности
            len_seq_2 = 0                                                       # количество карт во второй последовательности
            seq_value_2 = 0                                                     # старшая карта во второй последовательности
            len_seq_3 = 0                                                       # количество карт в третьей последовательности
            seq_value_3 = 0                                                     # старшая карта в третьей последовательности
        #-------------------------------------------
            cardset_tmp.sort(cmp,partial(ds_card_value, True))                         # сортируем список от 2
            val_i = 0                                                           # количество очков текущей карты в переборе
            val_prev = 0                                                        # количество очков предыдущей карты в переборе
            run_number = 0                                                      # номер результативного прохода
            len_seq_run = 0                                                     # количество карт в возможных последовательностях на проходах
            for i in range(0,n_cards):                                          # перебираем карты
                val_i = ds_card_value(True, cardset_tmp[i])                     # читаем значение очередной карты; туз = 14
                if val_i != 0:                                                  # если карта нормальная
                    run_number += 1                                              # увеличиваем счетчих проходов (отсеиваем пустую карту)
                    if run_number == 1:                                         # на первом проходе
                        len_seq_run = 1                                         # длину текущей последовательности принимаем = 1
                        len_seq_max = 1                                         # длину максимальной последовательности принимаем = 1
                    else:                                                       # на следующих проходах
                        if val_i == (val_prev + 1):                             # если очередная карта в последовательности
                            len_seq_run += 1                                    # длину текущей последовательности увеличиваем на 1
                            if len_seq_run > len_seq_max:                       # если текущая последовательность больше максимальной
                                len_seq_max = len_seq_run                       # максимальную последовательность принимаем по текущей
                                seq_value_max = val_i                           # старшую карту принимаем по текущей
                        elif val_i == val_prev:                                 # если карты равны
                            pass                                                # карту пропускаем, последовательность не сбрасываем
                        elif val_i > (val_prev + 1):                            # если очередная карта не в последовательности
                            if len_seq_run >= 2:                                # если была набрана последовательность в 2 карты или более - смотрим, что это за последовательность
                                if len_seq_1 == 0:                              #   … и эта последовательность первая
                                    len_seq_1 = len_seq_run                     # длина первой последовательности = длине текущей последовательности
                                    seq_value_1 = val_prev                      # старшая карта первой последовательности = предыдущей карте
                                elif (len_seq_1 != 0) and (len_seq_2 == 0):     #   … и эта последовательность вторая
                                    len_seq_2 = len_seq_run                     # длина второй последовательности = длине текущей последовательности
                                    seq_value_2 = val_prev                      # старшая карта второй последовательности = предыдущей карте
                                elif (len_seq_1 != 0) and (len_seq_2 != 0) and (len_seq_3 == 0): #   … и эта последовательность третья
                                    len_seq_3 = len_seq_run                     # длина третьей последовательности = длине текущей последовательности
                                    seq_value_3 = val_prev                      # старшая карта третьей последовательности = предыдущей карте
                            len_seq_run = 1                                     # длину текущей последовательности принимаем = 1
                    val_prev = val_i                                            # значение карты для сравнения принимаем: значение текущей карты
        #-------------------------------------------
            if len_seq_max >= 4:                                                # если на максимуме набрали последовательность в 4 и более
                values_max = []                                                 # готовим таблицу очков карт
                cardset_tmp.sort(cmp,partial(ds_card_value, True))                     # сортируем таблицу (туз = 14)
                cardset_tmp.reverse()                                           # и "переворачиваем" её (старшая - первая)
                val = seq_value_max                                             # ожидаемое значение = значению старшей карты
                for i in range(0,n_cards):                                      # перебираем сортированный сет
                    if ds_card_value(True, cardset_tmp[i]) == val:            # значение очередной карты = ожидаемому
                        values_max.append(val)                                  # добавляем такое значение в набор
                        val -= 1                                                 # уменьшаем ожидаемое значение
        #------------------------------------------
            if len_seq_max == 3:                                                # если максимальная последовательность = 3 - какая из трёх
                values_max = []                                                 # готовим таблицу очков карт
                if len_seq_1 == 3:                                              # если первая
                    triplex_seq += 1                                             # считаем последовательности по три
                    above_1 = seq_value_1 + 2                                   # возможная доп. карта старше трёх
                    below_1 = seq_value_1 - 4                                   # возможная доп. карта младше трёх
                    if (above_1 in self.table_card_points) or (below_1 in self.table_card_points): # если есть одна из карт по схеме 3+1
                        values_max_1 = [seq_value_1,seq_value_1-1,seq_value_1-2] # вставляем в таблицу три карты последовательности - старшая первая
                        if above_1 in self.table_card_points:                   # если есть старшая карта
                            values_max_1.insert(0,above_1)                      # вставляем её в начало списка
                        if below_1 in self.table_card_points:                   # если есть и младшая карта
                            values_max_1.append(below_1)                        # добавляем её к набору
                if len_seq_2 == 3:                                              # если вторая
                    triplex_seq += 1                                             # считаем последовательности по три
                    above_2 = seq_value_2 + 2                                   # возможная доп. карта старше трёх
                    below_2 = seq_value_2 - 4                                   # возможная доп. карта младше трёх
                    if (above_2 in self.table_card_points) or (below_2 in self.table_card_points): # если есть одна из карт по схеме 3+1
                        values_max_2 = [seq_value_2,seq_value_2-1,seq_value_2-2] # вставляем в таблицу три карты последовательности - старшая первая
                        if above_2 in self.table_card_points:                   # если есть старшая карта
                            values_max_2.insert(0,above_2)                      # вставляем её в начало списка
                        if below_2 in self.table_card_points:                   # если есть и младшая карта
                            values_max_2.append(below_2)                        # добавляем её к набору
                if len_seq_3 == 3:                                              # если третья
                    triplex_seq += 1                                             # считаем последовательности по три
                    above_3 = seq_value_3 + 2                                   # возможная доп. карта старше трёх
                    below_3 = seq_value_3 - 4                                   # возможная доп. карта младше трёх
                    if (above_3 in self.table_card_points) or (below_3 in self.table_card_points): # если есть одна из карт по схеме 3+1
                        values_max_3 = [seq_value_3,seq_value_3-1,seq_value_3-2] # вставляем в таблицу три карты последовательности - старшая первая
                        if above_3 in self.table_card_points:                   # если есть старшая карта
                            values_max_3.insert(0,above_3)                      # вставляем её в начало списка
                        if below_3 in self.table_card_points:                   # если есть и младшая карта
                            values_max_3.append(below_3)                        # добавляем её к набору
                if len(values_max_3) !=0:                                       # начинаем с третьей - потенциально старшей
                    values_max = values_max_3[:]                                # добавляем всё оттуда в максимальную последовательность
                    # дальнейшая проверка смысла не имеет - если треться последовательность тройная - первые две могут быть только по две
                else:                                                           # если третья последовательность не тройная
                    if len(values_max_2) !=0:                                   # проверяем вторую последовательность - если не пустая (вторая - тройная, первая тоже может быть тройной)
                        values_max = values_max_2[:]                            # добавляем всё оттуда в максимальную последовательность
                        if len(values_max_1) !=0:                               # проверяем первую последовательность - если не пустая
                            for i in range (0,len(values_max_1)):               # перебираем ёё
                                if values_max_1[i] not in values_max:           # и если в ней найдётся цифра, которой ёще нет в максимальной последовательности
                                    values_max.append(values_max_1[i])          # добавляем её туда.
                    else:                                                       # если и вторая последовательность не тройная
                        if len(values_max_1) !=0:                               # проверяем первую последовательность - если не пустая (может и лишнее, но чтоб не вылетело)
                            values_max = values_max_1[:]                        # добавляем всё оттуда в максимальную последовательность
        #------------------------------------------
            if (len_seq_max == 2) or (triplex_seq == 1):                        # если максимальная последовательность = 2 или одна тройная последовательность, проверяем двойные
                if len_seq_1 in [2,3]:                                          # если первая последовательность = 2 или 3
                    if len_seq_2 == 2:                                          # если вторая последовательность = 2
                        if seq_value_2 == (seq_value_1+3):                      # если старшая второй последовательности = старшая первой +3
                            values_max_com_12 = [seq_value_2,seq_value_2-1,seq_value_1,seq_value_1-1]     # добавляем числа второй последовательности и два старшие первой
                        if len_seq_3 == 2:                                      # если третья последовательность = 2
                            if seq_value_3 == (seq_value_2+3):                  # если старшая третьей последовательности = старшая второй +3
                                values_max_com_23 = [seq_value_3,seq_value_3-1,seq_value_2,seq_value_2-1]     # добавляем числа третьей последовательности и два старшие второй
                        elif len_seq_3 == 3:                                    # если третья последовательность = 3
                            if seq_value_3 == (seq_value_2+4):                  # если старшая третьей последовательности = старшая второй +4
                                values_max_com_23 = [seq_value_3-1,seq_value_3-2,seq_value_2,seq_value_2-1]     # добавляем два младшие числа третьей последовательности и два старшие второй
                    elif len_seq_2 == 3:                                        # если вторая последовательность = 3
                        if seq_value_2 == (seq_value_1+4):                      # если старшая второй последовательности = старшая первой +4
                            values_max_com_12 = [seq_value_2-1,seq_value_2-2,seq_value_1,seq_value_1-1]     # добавляем 2 младшие числа второй последовательности и два старшие первой
                if len(values_max) == 0:                                        # если максимальной последовательности в тройках не было
                    if len(values_max_com_23) != 0:                             # что-то нашли во 2-3 паре
                        values_max = values_max_com_23[:]                       # добавляем все из этого списка в максимальный
                        if len(values_max_com_12) != 0:                         # и что-то нашли в 1-2 паре
                            for i in range (0,len(values_max_com_12)):          # перебираем эту последовательность
                                if values_max_com_12[i] not in values_max:      # и если такого числа в максимальной нет
                                    values_max.append(values_max_com_12[i])     # добавляем его туда
                    else:                                                       # список по 2-3 паре пустой
                        if len(values_max_com_12) != 0:                         # что-то нашли в 1-2 паре
                            values_max = values_max_com_12[:]                   # добавляем все из этого списка в максимальный
                else:                                                           # если на тройке есть максимальная последовательность уже
                    if len(values_max_com_23) != 0:                             # что-то нашли во 2-3 паре
                        for i in range (0,len(values_max_com_23)):              # перебираем эту последовательность
                            if values_max_com_23[i] not in values_max:          # и если такого числа в максимальной нет
                                values_max.append(values_max_com_23[i])         # добавляем его туда
                    if len(values_max_com_12) != 0:                             # что-то нашли в 1-2 паре
                        for i in range (0,len(values_max_com_12)):              # перебираем эту последовательность
                            if values_max_com_12[i] not in values_max:          # и если такого числа в максимальной нет
                                values_max.append(values_max_com_12[i])         # добавляем его туда
                    values_max.sort()                                           # сортируем максимальную от минимума
                    values_max.reverse()                                        # и "переворачиваем" - от максимума.
        #-------------------------------------------
        # проверка на потенциальный стрит от пятёрки (младший)
            values_min = []                                                     # готовим таблицу очков карт
            for mix in [[2,3,4,14],[2,3,5,14],[2,4,5,14],[3,4,5,14]]:           # проверяем 4-ре возможных сочетания с тузом
                                                                                # если все очки карт из сочетания входят в списое очков наших карт
                if (mix[0] in self.table_card_points) and (mix[1] in self.table_card_points) and (mix[2] in self.table_card_points) and (mix[3] in self.table_card_points):
                    values_min = mix[:]                                         # принимаем это сочетание, как таблицу очков минимума
                    break                                                       # на том цикл заканчиваем
        #-------------------------------------------
            for i in range(0,n_cards):                                          # перебираем СВОИ КАРТЫ
                if ds_card_value(True, cards_rival[i]) in values_max:         # если значение очередной карты в списке максимальных значений
                    self.table_card_sequence_max.append(i)                      # индекс карты добавляем в таблицу

                if ds_card_value(False, cards_rival[i]) in values_min:         # если значение очередной карты в списке минимальных значений
                    self.table_card_sequence_min.append(i)                      # индекс карты добавляем в таблицу
# ----------------------------------------------------
        def what_cards_have(self):                                              # какие карты у нас на руках (значения очков)
            self.table_card_points = []                                         # обнуляем таблицу на вызове функции
            for i in range(0,n_cards):                                          # перебираем свои карты
                if cards_rival[i].name == name_of_none:                         # если карта пустая
                    val = 99                                                    # очков - 99 (чтобы её не выбрать)
                else:                                                           # если карта нормальная
                    val = ds_card_value(True, cards_rival[i])                 # читаем ёе значение (туз старший)
                self.table_card_points.append(int(val))                         # добавляем значение в список
            if self.combo_in_hand[0] < 5:                                       # если меньше флеша
                self.check_for_four_suit()                                      # проверяем на 4 в масти
            else:
                self.table_card_suit = []                                       # убираем недофлеш
                self.table_card_sequence_max = []                               # и недостриты
                self.table_card_sequence_min = []
            if self.combo_in_hand[0] < 4:                                       # если меньше стрита
                self.check_for_four_sequence()                                  # проверяем на 4 последовательные
            else:
                self.table_card_sequence_max = []                               # убираем недостриты
                self.table_card_sequence_min = []
# ----------------------------------------------------
        def remember_combo(self):                                               # запоминаем комбинацию
            self.combo_was_before = []                                          # создаём пустой список
            if self.combo_in_hand != None:                                      # если получили комбо "на руках"
                self.combo_was_before = self.combo_in_hand[:]                   # запоминаем его
# ----------------------------------------------------
        def compare_combo(self):                                                # сравниваем комбинации до и после
            if self.combo_in_hand != None and self.combo_was_before != None:    # если определили новую и запомнили старую комбо
                if self.combo_in_hand[0] > self.combo_was_before[0]:            # если новая комбинация старше
                    self.as_changed_combo = 'better'                            # результат - стало лучше
                elif self.combo_in_hand[0] < self.combo_was_before[0]:          # если новая комбинация младше
                    self.as_changed_combo = 'worse'                             # результат - стало хуже
                else:                                                           # если комбинации равного достоинства
                    if self.combo_in_hand[1] > self.combo_was_before[1]:        # если новая старшая карта больше
                        self.as_changed_combo = 'better'                        # результат - стало лучше
                    elif self.combo_in_hand[1] < self.combo_was_before[1]:      # если новая старшая карта меньше
                        self.as_changed_combo = 'worse'                         # результат - стало хуже
                    else:                                                       # если старшие карты одинаковы
                        if self.combo_in_hand[3] > self.combo_was_before[3]:    # если новая младшая пара больше
                            self.as_changed_combo = 'better'                    # результат - стало лучше
                        elif self.combo_in_hand[3] < self.combo_was_before[3]:  # если новая младшая пара меньше
                            self.as_changed_combo = 'worse'                     # результат - стало хуже
                        else:                                                   # если младшие пары одинаковы
                            self.as_changed_combo = 'does'                      # результат - ситуация не поменялась
            else:
                self.as_changed_combo = 'unclear'                               # непонятно: наборов карт не обнаружено
# ----------------------------------------------------
        def remember_cards(self):                                                   # запоминаем возможные недокомбинации
            self.table_card_possible_combo = []                                     # возможная комбинация - очищаем
            if self.combo_in_hand[0] < 4:                                           # если меньше стрита на руках
                if len(self.table_card_suit) != 0:                                      # если недофлеш
                    self.table_card_possible_combo = self.table_card_suit[:]            # принимаем его, как возможную комбинацию
                if len(self.table_card_sequence_max) != 0:                              # если что-то есть в большом стрите
                    for i in range(0,len(self.table_card_sequence_max)):                # перебираем его
                        if self.table_card_sequence_max[i] not in self.table_card_possible_combo: # если такой карты там ещё нет
                            self.table_card_possible_combo.append(self.table_card_sequence_max[i]) # добавляем её туда
                if len(self.table_card_sequence_min) != 0:                              # если что-то есть в малом стрите
                    for i in range(0,len(self.table_card_sequence_min)):                # перебираем его
                        if self.table_card_sequence_min[i] not in self.table_card_possible_combo: # если такой карты там ещё нет
                            self.table_card_possible_combo.append(self.table_card_sequence_min[i]) # добавляем её туда
                if len(self.table_card_possible_combo) !=0:                             # если список возможных комбинаций не пустой
                    self.table_card_possible_combo.sort()                               # сортируем список
# ----------------------------------------------------
        def choice_need_cards(self):                                                        # отбираем карты в комбинации
            self.yourself_need_cards = []                                                   # очищаем список
            for i in range(0,n_cards):                                                      # перебираем свои карты
                if cards_rival[i].in_combo:                                                 # если карта в комбинации карт
                    self.yourself_need_cards.append(i)                                      # добавляем индекс этой карты в сет
# ----------------------------------------------------
        def choice_waste_cards(self):                                                       # отбираем мусор (не в комбинации)
            self.waste_cards = []                                                           # очищаем список
            for i in range(0,n_cards):                                                      # перебираем свои карты
                if not cards_rival[i].in_combo and cards_rival[i].name != name_of_none:     # если карта НЕ в комбинации карт и она НЕ пустая
                    self.waste_cards.append(i)                                              # добавляем индекс этой карты в сет
# ----------------------------------------------------
        def selection_cards_for_defense(self):                                              # отбор карт на защиту
            self.would_not_want_give = self.yourself_need_cards[:]                          # не отдавать - то, что в комбинации
            if len(self.table_card_suit) != 0:                                              # если есть что-то в недофлешах
                for i in range(0,len(self.table_card_suit)):                                # перебираем сет
                    if (self.table_card_suit[i] not in self.can_give_in_a_pinch) and (self.table_card_suit[i] not in self.yourself_need_cards):# такой карты ещё не добавлено и её нет в нужных
                        self.can_give_in_a_pinch.append(self.table_card_suit[i])            # добавляем эту карту
            if len(self.table_card_sequence_max) != 0:                                      # что-то есть в старшем недострите
                for i in range(0,len(self.table_card_sequence_max)):                        # переберём его и
                    if (self.table_card_sequence_max[i] not in self.can_give_in_a_pinch) and (self.table_card_sequence_max[i] not in self.yourself_need_cards):#  карта не добавлена и не нужна
                        self.can_give_in_a_pinch.append(self.table_card_sequence_max[i])    # добавляем эту карту
            if len(self.table_card_sequence_min) != 0:                                      # что-то есть в младшем недострите
                for i in range(0,len(self.table_card_sequence_min)):                        # переберём его и
                    if (self.table_card_sequence_min[i] not in self.can_give_in_a_pinch) and (self.table_card_sequence_min[i] not in self.yourself_need_cards):# карта не добавлена и не нужна
                        self.can_give_in_a_pinch.append(self.table_card_sequence_min[i])    # добавляем эту карту
        # что предлагаем
            for j in range (0, n_cards):                                                    # смотрим, что мы можем предложить из своего
                if cards_rival[j].name != name_of_none:                                     # если карта не пустая
                    if (j not in self.yourself_need_cards) and (j not in self.can_give_in_a_pinch):     # очередная карта нам не особенно и нужна-то
                        self.these_proposed_to_take.append(j)                               # добавим её в список предлагаемых
        # в первую очередь предлагаем
            if len(self.these_proposed_to_take) != 0:                                       # если есть, что предлагать к обмену
                self.its_urgent_shove = self.find_low_cards(self.these_proposed_to_take)    # на отдачу в первую очередь - младшие из предлагаемых к обмену
            else:                                                                           # если предлагать нечего:
                self.its_urgent_shove = self.find_low_cards(self.can_give_in_a_pinch)       # на отдачу в первую очередь - младшие из тех, что на крайний случай
# ----------------------------------------------------
        def selection_cards_for_gamble_not_give(self):                                      # отбор карт на риск - НЕ ОТДАВАТЬ
            if len(self.table_card_suit) != 0:                                              # если есть что-то в недофлешах
                self.would_not_want_give = self.table_card_suit[:]                          # не отдавать - недофлеш
            if len(self.table_card_sequence_max) != 0:                                      # что-то есть в старшем недострите
                for i in range(0,len(self.table_card_sequence_max)):                        # переберём его и
                    if self.table_card_sequence_max[i] not in self.would_not_want_give:     # если карта ещё не добавлена
                        self.would_not_want_give.append(self.table_card_sequence_max[i])    # добавляем эту карту в нужные
            if len(self.table_card_sequence_min) != 0:                                      # что-то есть в младшем недострите
                for i in range(0,len(self.table_card_sequence_min)):                        # переберём его и
                    if self.table_card_sequence_min[i] not in self.would_not_want_give:     # если карта ещё не добавлена
                        self.would_not_want_give.append(self.table_card_sequence_min[i])    # добавляем эту карту в нужные
# ----------------------------------------------------
        def selection_cards_for_gamble_proposed(self):                                      # отбор карт на риск - ПРЕДЛАГАТЬ
            if len(self.table_card_possible_combo) == 0:                                    # если нам предкомбинацию не разрушали
                for j in range (0, n_cards):                                                    # смотрим, что мы можем предложить из своего
                    if cards_rival[j].name != name_of_none:                                     # если карта не пустая
                        if (j not in self.would_not_want_give) and (j not in self.can_give_in_a_pinch):     # очередная карта не в крайнем случае
                            self.these_proposed_to_take.append(j)                               # добавим её в список предлагаемых
                self.selection_cards_for_gamble_urgent_shove()                                  # отбираем самые ненужные карты
            else:                                                                           # если предкомбинация разрушена
                for j in range (0, n_cards):                                                    # смотрим, что мы можем предложить из своего
                    if cards_rival[j].name != name_of_none:                                     # если карта не пустая
                        if j not in self.table_card_possible_combo:                             # если карта не входила в предкомбинацию
                            if (j not in self.would_not_want_give) and (j not in self.can_give_in_a_pinch):     # очередная карта не в нужных и не в крайнем случае
                                self.these_proposed_to_take.append(j)                               # добавим её в список предлагаемых
                self.selection_cards_for_gamble_urgent_shove()                                  # отбираем самые ненужные карты
# ----------------------------------------------------
        def selection_cards_for_gamble_urgent_shove(self):                                  # отбор карт на риск в первую очередь - ПРЕДЛАГАТЬ
            if len(self.these_proposed_to_take) != 0:                                       # если есть, что предлагать к обмену
                self.its_urgent_shove = self.find_low_cards(self.these_proposed_to_take)    # на отдачу в первую очередь - младшие из предлагаемых к обмену
            else:                                                                           # если предлагать нечего:
                if len(self.can_give_in_a_pinch) !=0:                                       # если есть что отдать в крайнем случае
                    self.its_urgent_shove = self.find_low_cards(self.can_give_in_a_pinch)   # на отдачу в первую очередь - младшие из тех, что на крайний случай
                else:                                                                       # если ВСЕ карты нужны
                    self.its_urgent_shove = self.find_low_cards(self.would_not_want_give)   # самые младшие из нужных
# ----------------------------------------------------
        def sort_cards_on_usefulness(self):                                                 # сортировка карт по категориям "полезности"
            self.would_not_want_give = []                                                   # очищаем список - что и самому надо (не отдавать)
            self.can_give_in_a_pinch = []                                                   # очищаем список - что можно отдать (в крайнем случае)
            self.these_proposed_to_take = []                                                # очищаем список - что предлагать Семёну
            self.its_urgent_shove = []                                                      # очищаем список - что отдать в первую очередь
        # -----------------------------------------------------------
            self.what_we_have()                                                             # смотрим, что на руках есть
            self.how_skill()                                                                # проверяем навык
        # ----------------------------------------------------------
            if self.playstyle == 'defense':                                                 # если защищаемся
                self.selection_cards_for_defense()                                          # сортируем карты под защиту
        # -----------------------------------------------------------
            elif self.playstyle == 'gamble':                                                        # если рискуем
                if self.combo_in_hand[0] < 4:                                                       # если на руках ДО стрита (карта, пара, две пары, тройка)
                    self.selection_cards_for_gamble_not_give()                                      # сортируем карты под риск - не отдавать
                    if len(self.would_not_want_give) == 0:                                          # если нет недокомбинаций
                        self.selection_cards_for_defense()                                          # сортируем карты под защиту
                    else:                                                                           # есть чем рискнуть
                        if self.combo_in_hand[0] in [0,1,3]:                                        # если на руках старшая карта, пара или тройка
                            for i in range(0,len(self.yourself_need_cards)):                        # перебираем карты в комбинации
                                if self.yourself_need_cards[i] not in self.would_not_want_give:     # если карты из комбинации нет в нужных
                                    self.can_give_in_a_pinch.append(self.yourself_need_cards[i])    # добавляем эту карту в список первоочередных
                            self.selection_cards_for_gamble_proposed()                              # сортируем карты под риск - предлагать
                        elif self.combo_in_hand[0] == 2:                                                    # если на руках две пары
                            for i in range(0,len(self.yourself_need_cards)):                                # перебираем карты в комбинации
                                if self.table_card_points[self.yourself_need_cards[i]] == self.combo_in_hand[1]: # если текущая карта - в старшей паре
                                    if self.yourself_need_cards[i] not in self.would_not_want_give:         # если карты из комбинации нет в нужных
                                        self.would_not_want_give.append(self.yourself_need_cards[i])        # добавляем эту карту в НУЖНЫЕ
                                else:                                                                       # если текущая карта в младшей паре
                                    if self.yourself_need_cards[i] not in self.would_not_want_give:         # если карты из комбинации нет в нужных
                                        self.can_give_in_a_pinch.append(self.yourself_need_cards[i])        # добавляем эту карту в список первоочередных
                            self.selection_cards_for_gamble_proposed()                                      # сортируем карты под риск - предлагать
                else:                                                                               # если на руках от стрита и выше
                    self.selection_cards_for_defense()                                              # сортируем карты под защиту
        # -----------------------------------------------------------
            elif self.playstyle == 'succumb':                                                       # если сливаемся
                if self.combo_in_hand[0] in [7,6,3,2]:                                              # если две пары, тройка, фулл-хаус, покер
                    for i in range(0,n_cards):                                                      # перебираем свои карты
                        if ds_card_value(True, cards_rival[i]) == self.combo_in_hand[1]:          # если значение очередной карты - равно старшей карте комбинации
                            if i not in self.this_give_definitely_succumb:                          # если ещё такой карты в списке нет
                                self.this_give_definitely_succumb.insert(0,i)                       # вставляем на 0-ю позицию
                    if (self.combo_in_hand[0] == 2) and (len(self.this_give_definitely_succumb)>2): # если 2 пары и список больше 2-х
                        del self.this_give_definitely_succumb[2:len(self.this_give_definitely_succumb)]# удаляем лишнее
                    if (self.combo_in_hand[0] in [3,6]) and (len(self.this_give_definitely_succumb)>3):# если тройка или фулл и список больше 3-х
                        del self.this_give_definitely_succumb[3:len(self.this_give_definitely_succumb)]# удаляем лишнее
                    if (self.combo_in_hand[0] == 7) and (len(self.this_give_definitely_succumb)>4): # если покер и список больше 4-х
                        del self.this_give_definitely_succumb[4:len(self.this_give_definitely_succumb)]# удаляем лишнее
                self.its_urgent_shove = self.find_older_cards(self.yourself_need_cards)             # В список на срочную отдачу - старшие карты из комбинации
                self.these_proposed_to_take = self.yourself_need_cards[:]                           # предлагать к обмену - остальные карты комбинации
                if len(self.table_card_suit) != 0:                                                  # если есть что-то в недофлешах
                    for i in range(0,len(self.table_card_suit)):                                    # переберём его и
                        if self.table_card_suit[i] not in self.these_proposed_to_take:              # такой карты ещё не добавлено
                            self.these_proposed_to_take.append(self.table_card_suit[i])             # добавляем её
                if len(self.table_card_sequence_max) != 0:                                          # что-то есть в старшем недострите
                    for i in range(0,len(self.table_card_sequence_max)):                            # переберём его и
                        if self.table_card_sequence_max[i] not in self.these_proposed_to_take:      # такой карты ещё не добавлено
                            self.these_proposed_to_take.append(self.table_card_sequence_max[i])     # добавляем её
                if len(self.table_card_sequence_min) != 0:                                          # что-то есть в младшем недострите
                    for i in range(0,len(self.table_card_sequence_min)):                            # переберём его и
                        if self.table_card_sequence_min[i] not in self.these_proposed_to_take:      # такой карты ещё не добавлено
                            self.these_proposed_to_take.append(self.table_card_sequence_min[i])     # добавляем её
                for j in range (0,len(self.waste_cards)):                                           # перебираем мусор
                    if self.waste_cards[j] not in self.these_proposed_to_take:                      # если очередной карты нет в списке предлагаемых
                        if self.waste_cards[j] not in self.this_give_definitely_succumb:            # и её же нет в списке на срочный слив
                            self.would_not_want_give.append(self.waste_cards[j])                    # добавляем её в список нужных нам
        # -----------------------------------------------------------
            elif self.playstyle == 'foolplay':                                                      # если включили дурака
                pass
        # -----------------------------------------------------------
            if self.player_unnecessary_card < 7:                                                    # если определена карта, отданная Семёном у нас - НЕНУЖНАЯ ему
                if self.playstyle in ['defense', 'gamble']:                                         # если защищаемся или рискуем
                    if (self.player_unnecessary_card in self.would_not_want_give) or (self.player_unnecessary_card in self.can_give_in_a_pinch):    # если эта карта попала в нужные
                        pass
                    elif self.player_unnecessary_card in self.these_proposed_to_take:                   # если она попала в предлагаемые к отдаче
                        if self.player_unnecessary_card not in self.its_urgent_shove:                   # эта карта ещё не попала в первую очередь на отдачу
                            self.its_urgent_shove.insert(0,self.player_unnecessary_card)                # вставляем её туда
                elif self.playstyle == 'succumb':                                                       # если сливаемся
                    if self.player_unnecessary_card in self.its_urgent_shove:                           # если эта карта в списке на срочную отдачу
                        self.its_urgent_shove.remove(self.player_unnecessary_card)                      # удаляем её оттуда
                    if self.player_unnecessary_card in self.these_proposed_to_take:                     # если эта карта в списке предлагаемых
                        self.these_proposed_to_take.remove(self.player_unnecessary_card)                # удаляем её оттуда
                    if self.player_unnecessary_card in self.can_give_in_a_pinch:                        # если эта карта в списке на крайний случай
                        self.can_give_in_a_pinch.remove(self.player_unnecessary_card)                   # удаляем её оттуда
                    if self.player_unnecessary_card not in self.would_not_want_give:                    # если не попала в список " не отдавать"
                        self.would_not_want_give.append(self.player_unnecessary_card)                   # добавляем её в список "не отдавать"
                elif self.playstyle == 'foolplay':                                                      # если включили дурака
                    pass                                                                                # пропускаем
            # -----------------------------------------------------------
            if self.player_accept_card < 7:                                                         # если определена карта, отданная Семёном, как НУЖНАЯ ему
                if self.playstyle in ['defense', 'gamble']:                                         # если защищаемся или рискуем
                    if (self.player_accept_card in self.its_urgent_shove) and (len(self.its_urgent_shove)>1):   # если эта карта в списке на срочную отдачу и она там не одна
                        self.its_urgent_shove.remove(self.player_accept_card)                                   # удаляем её оттуда
                    if (self.player_accept_card in self.these_proposed_to_take) and (len(self.these_proposed_to_take)>1):# если эта карта в списке предлагаемых и она там не одна
                        self.these_proposed_to_take.remove(self.player_accept_card)                                   # удаляем её оттуда
                    if self.player_accept_card in self.can_give_in_a_pinch:                             # если эта карта в списке на крайний случай
                        self.can_give_in_a_pinch.remove(self.player_accept_card)                        # удаляем её оттуда
                    if self.player_accept_card not in self.would_not_want_give:                         # если не попала в список " не отдавать"
                        if (self.player_accept_card not in self.its_urgent_shove) and (self.player_accept_card not in self.these_proposed_to_take): # и её нет в списках на отдачу
                            self.would_not_want_give.append(self.player_accept_card)                    # добавляем её в список "не отдавать"
                elif self.playstyle == 'succumb':                                                       # если сливаемся
                    pass
                elif self.playstyle == 'foolplay':                                                      # если включили дурака
                    pass
# ----------------------------------------------------
        def find_low_cards(self,table):                                             # функция поиска младших карт в наборе
            min_in_combo = 15                                                       # минимальная карта в предлагаемых - принимаем 15
            i_min = []                                                              # индексы минимальных карт
            res = []                                                                # результат
            for j in range (0,len(table)):                                          # перебираем предлагаемые
                ind = table[j]                                                      # указатель на список своих карт
                if self.table_card_points[ind] < min_in_combo:                      # если очередная карта в списке по индексу меньше минимальной
                    min_in_combo = self.table_card_points[ind]                      # принимаем её за минимальную
            for j in range (0,len(table)):                                          # перебираем предлагаемые
                ind = table[j]                                                      # указатель на список своих карт
                if self.table_card_points[ind] in [min_in_combo, min_in_combo+1] :  # если очередная карта в списке минимальная или на 1 больше
                    i_min.append(j)                                                 # в список индексов минимальных карт из предлагаемых добавляем значение
            for i in i_min:                                                         # переберём индексы минимальных карт
                res.append(table[i])                                                # и добавим младшие карты из передлагаемых в список ненужных
            return res                                                              # возвращаем таблицу
# ----------------------------------------------------
        def find_older_cards(self,table):                                           # функция поиска старших карт в наборе
            max_in_combo = 0                                                        # максимальная карта в комбинации - принимаем 0
            i_max = []                                                              # индексы максимальных карт
            res = []                                                                # результат
            for j in range (0,len(table)):                                          # перебираем комбинацию
                ind = table[j]                                                      # указатель на список своих карт
                if self.table_card_points[ind] > max_in_combo:                      # если очередная карта в списке по индексу больше максимальной
                    max_in_combo = self.table_card_points[ind]                      # принимаем её за максимальную
            for j in range (0,len(table)):                                          # перебираем комбинацию
                ind = table[j]                                                      # указатель на список своих карт
                if self.table_card_points[ind] >= max_in_combo:                     # если очередная карта в списке по индексу больше или равна максимальной
                    i_max.append(j)                                                 # в список индексов максимальных карт комбинации добавляем значение
            for i in i_max:                                                         # переберём индексы максимальных карт
                res.append(table[i])                                                # и добавим старшие карты комбинации в список ненужных
            return res                                                              # возвращаем таблицу
# ----------------------------------------------------
        def what_pulled_player(self):                                           # что собрался вытащить игрок
            for i in range(0,n_cards):                                          # перебираем свои карты
                if cards_rival[i].interesting:                                  # если Семён потянулся за этой картой
                    self.pulled_player_card = i                                 # то это она и есть
# ----------------------------------------------------
        def do_we_need_this_card(self):                                         # что игрок вытащил и насколько эта карта важна
            self.degree_usefulness_card = 0                                     # степень "полезности" вытащенной карты
            self.what_pulled_player()                                           # смотрим, куда Сёма нацелился
            self.dragged_player_card = self.pulled_player_card                  # и эту карту он сейчас заберёт
            if self.dragged_player_card in self.would_not_want_give:            # если карта из тех, что не отдавать
                self.degree_usefulness_card = 3                                 # забрать её срочно
            elif self.dragged_player_card in self.can_give_in_a_pinch:          # если карта из тех, что в крайнем случае
                self.degree_usefulness_card = 2                                 # запомнить её, заберём в другой раз, это не срочно
            elif (self.dragged_player_card in self.its_urgent_shove) or (self.dragged_player_card in self.these_proposed_to_take): # если карта из числа ненужных
                self.degree_usefulness_card = 1                                 # то и хрен с нею
# ----------------------------------------------------
        def to_give_just_card(self):                                            # а может, сразу отдать карту Семёну?
            min_cards = 15                                                      # значение очков карты = 15 (такого нет точно)
            i_min = 7                                                           # индекс карты = 7 (такого нет точно)
            global changes_left                                                 # понадобится количество оставшихся обменов
            self.how_skill()                                                    # проверяем навык
            if (self.playstyle in ['defense','gamble','succumb']) and (not self.make_mistakes): # если стиль игры из определённых и не ошибаемся
                self.sort_cards_on_usefulness()                                 # рассортировали своё по степени нужности
                self.what_pulled_player()                                       # смотрим, куда потянулся Семён
        #-------------------------------------------
                if self.pulled_player_card in self.this_give_definitely_succumb:    # если потянулся к той карте, которая у нас в срочном сливе
                    if self.combo_in_hand[0] not in [4,5,8,9]:                  # если на руках НЕ флэш или стрит
                        renpy.pause(1.0)                                        # немного подумали и…
                        changes_left = 0                                        # сбрасываем обмены (Сеня заберёт карту)
                    else:                                                       # если флеш или стрит
                        pass                                                    # таки будем менять карты
                elif self.pulled_player_card in self.its_urgent_shove:          # если эта карта - в списке сплавляемых в первую очередь
                    if (len(self.its_urgent_shove) == 1) or (self.playstyle == 'succumb'): # и такая карта всего одна ИЛИ игра в поддавки
                        renpy.pause(1.0)                                        # немного подумали и…
                        changes_left = 0                                        # сбрасываем обмены (Сеня заберёт карту)
                    elif len(self.its_urgent_shove) > 1:                        # и совсем ненужных несколько
                        k = random.choice([1,2,3])                              # решаем - отдавать карту сразу (1,2) или нет (3) - вероятность 0,66
                        if k in [1,2]:                                          # и если да
                            renpy.pause(1.0)                                    # немного подумали и…
                            changes_left = 0                                    # сбрасываем обмены (Сеня заберёт карту)
                elif (self.pulled_player_card in self.these_proposed_to_take) and (self.playstyle != 'succumb'):    # если эта карта - в списке предлагаемых на обмен и НЕ слив
                    k = random.choice([1,2,3,4])                                # решаем - отдавать карту сразу (1) или нет (2,3,4) - вероятность 0,25
                    if k == 1:                                                  # и если да
                        renpy.pause(1.0)                                        # немного подумали и…
                        changes_left = 0                                        # сбрасываем обмены (Сеня заберёт карту)
        #-------------------------------------------
            elif (self.playstyle == 'foolplay') or (self.make_mistakes):        # если включили дурака или ошибаемся
                k = random.choice([1,2,3,4,5,6,7])                              # решаем - отдавать карту сразу (1) или нет (2..7) - вероятность 0,15
                if k == 1:                                                      # и если да
                    renpy.pause(1.0)                                            # немного подумали и…
                    changes_left = 0                                            # сбрасываем обмены (Сеня заберёт карту)
# ----------------------------------------------------
        def what_to_xchange_think(self):                                        # думаем, какие карты будем менять
            self.how_skill()                                                    # проверяем навык
        #-------------------------------------------
            if (self.playstyle in ['defense','gamble','succumb']) and (not self.make_mistakes): # если стиль игры из определённых и не ошибаемся
                self.what_pulled_player()                                       # смотрим, куда потянулся Семён
                i = self.pulled_player_card                                     # первая карта на обмен - она же
                j = 7                                                           # вторую - принимаем = 7
                if (i in self.would_not_want_give) or (i in self.can_give_in_a_pinch): # если карта в списках нужных
                    if len(self.its_urgent_shove) != 0:                         # если есть, что срочно отдать
                        j = random.choice(self.its_urgent_shove)                # случайная карта из ненужных
                    elif len(self.these_proposed_to_take) != 0:                 # если срочного нет, но есть, что можно предложить на обмен
                        j = random.choice(self.these_proposed_to_take)          # случайная карта из обменных
                    elif len(self.can_give_in_a_pinch) != 0:                    # если ненужных нет, но есть что отдать в крайнем случае
                        j = random.choice(self.can_give_in_a_pinch)             # случайная из крайнего случая
                        while i == j:                                           # если (а затем - пока) индексы одинаковы
                            j = random.choice(self.can_give_in_a_pinch)         # ещё рандомим вторую карту
                elif i in self.these_proposed_to_take:                          # если карта в списке предлагаемых
                    if len(self.its_urgent_shove) != 0:                         # если есть, что срочно отдать
                        j = random.choice(self.its_urgent_shove)                # случайная карта из ненужных
                    else:                                                       # если срочно отдавать нечего
                        j = random.choice(self.these_proposed_to_take)          # случайная карта из обменных
                        while i == j:                                           # если (а затем - пока) индексы одинаковы
                            j = random.choice(self.these_proposed_to_take)      # ещё рандомим вторую карту
                elif i in self.its_urgent_shove:                                # если карта в списке срочного сброса, но попали сюда
                    j = random.choice(self.its_urgent_shove)                    # случайная карта из ненужных
                    while i == j:                                               # если (а затем - пока) индексы одинаковы
                        j = random.choice(self.its_urgent_shove)                # ещё рандомим вторую карту
                if j == 7:                                                      # каким-то образом карты для обмена не нашлось
                    j = random.choice(self.yourself_need_cards+self.waste_cards)    # вторая карта для обмена из числа нужных + ненужных
                    while i == j:                                                   # если (а затем - пока) индексы одинаковы
                        j = random.choice(self.yourself_need_cards+self.waste_cards)# ещё рандомим вторую карту
        #-------------------------------------------
            elif (self.playstyle == 'foolplay') or (self.make_mistakes):        # если включили дурака или ошибаемся
                i = random.choice(self.yourself_need_cards+self.waste_cards)    # первая карта для обмена из числа нужных + ненужных
                j = random.choice(self.yourself_need_cards+self.waste_cards)    # вторая карта для обмена из числа нужных + ненужных
                while i == j:                                                   # если (а затем - пока) индексы одинаковы
                    j = random.choice(self.yourself_need_cards+self.waste_cards)# ещё рандомим вторую карту
        #-------------------------------------------
            if self.player_unnecessary_card == i:                               # если выбранная карта - не нужная Семёну
                self.player_unnecessary_card = j                                # меняем её позицию
            elif self.player_unnecessary_card == j:                             # если одна из карт - не нужная Семёну
                self.player_unnecessary_card = i                                # меняем её позицию
            if self.player_accept_card == i:                                    # если выбранная карта - НУЖНАЯ Семёну
                self.player_accept_card = j                                     # меняем её позицию
            elif self.player_accept_card == j:                                  # если одна из карт - НУЖНАЯ Семёну
                self.player_accept_card = i                                     # меняем её позицию
        #-------------------------------------------
            if len (self.this_give_definitely_succumb) !=0:                     # если список старших карт на отдачу не пуст
                if j in self.this_give_definitely_succumb:                      # если выбранная для обмена карта в списке
                    self.this_give_definitely_succumb.remove(j)                 # удаляем её
                    self.this_give_definitely_succumb.append(i)                 # добавляем ту, за которой потянулся Семён
        #-------------------------------------------
            return (i,j)                                                        # выдаём позиции для обмена
# ----------------------------------------------------
        def what_at_us_took(self,z):                                                # а что у нас Семён забрал - нужную или ненужную
            if self.degree_usefulness_card == 3:                                    # если забрал нужную
                self.pick_this_cards_urgently.insert(0,self.inserted_player_card)   # добавляем вынутую у нас карту в список "забрать срочно"
            elif self.degree_usefulness_card == 2:                                  # если забрал из тех, что на крайний случай
                self.pick_this_cards_afterwards.insert(0,self.inserted_player_card) # добавляем вынутую у нас карту в список "забрать потом"
            elif self.degree_usefulness_card == 1:                                  # если забрал ненужную
                self.never_touch_cards.insert(0,self.inserted_player_card)          # добавляем вынутую у нас карту в список ненужных у Семёна
            if z == self.player_unnecessary_card:                                   # сбагрили Семёну его же ненужную ему карту
                self.player_unnecessary_card = 7                                    # присваиваем индекс 7
            if z == self.player_accept_card:                                        # Семён забрал у нас нужную ему карту
                self.player_accept_card = 7                                         # присваиваем индекс 7

            if z in self.this_give_definitely_succumb:                              # если забрал ту, которая в списке слива
                if self.inserted_player_card not in self.never_touch_cards:         # если такой карты ещё нет в списке
                    self.never_touch_cards.insert(0,self.inserted_player_card)          # добавляем её в список "не трогать"
                self.this_give_definitely_succumb.remove(z)                         # удаляем эту карту у себя
# ----------------------------------------------------
        def what_card_we_gave_7(self,x,y):                                          # какая карта отдана при игре на 7 картах (карта игрока, карта Семёна)
            if x in self.would_not_want_give:                                       # если карта У СЕБЯ и нам нужна
                self.pick_this_cards_urgently.insert(0,y)                           # вставляем её индекс У СЕМЁНА в список на срочное изъятие
            if x in self.can_give_in_a_pinch:                                       # если карта У СЕБЯ из тех, что на крайний случай
                self.pick_this_cards_afterwards.insert(0,y)                         # вставляем её индекс У СЕМЁНА в список на "забрать потом"
            if (x in self.its_urgent_shove) or (x in self.these_proposed_to_take):  # и если карта У СЕБЯ из тех, что надо срочно спихнуть
                self.never_touch_cards.insert(0,y)                                  # вставляем её индекс У СЕМЁНА в список "не трогать"
            if x in self.this_give_definitely_succumb:                              # если карта их сливного списка
                self.never_touch_cards.insert(0,y)                                  # вставляем её индекс У СЕМЁНА в список "не трогать"
                self.this_give_definitely_succumb.remove(x)                         # и удаляем у себя
# ----------------------------------------------------
        def tracked_movement(self,i,j):                                         # отслеживаем перемещение интересующих нас карт (какие вообще переместились)
            temp_x1 = temp_x2 = temp_x3 = temp_y1 = temp_y2 = temp_y3 = 7       # такой карты точно нет, потому временные именно такие
            x1 = x2 = x3 = y1 = y2 = y3 = 7                                     # индексы также принимаем по 7
        #-------------------------------------------
            if i in self.never_touch_cards:                                     # если первая карта пары в блоке ненужных
                x1 = self.never_touch_cards.index(i)                            # индекс нахождения этой карты в списке
                temp_x1 = j                                                     # запоминаем вторую карту пары
            elif i in self.pick_this_cards_afterwards:                          # если первая карта пары в списке "забрать потом"
                x2 = self.pick_this_cards_afterwards.index(i)                   # индекс нахождения этой карты в списке
                temp_x2 = j                                                     # запоминаем вторую карту пары
            elif i in self.pick_this_cards_urgently:                            # если первая карта пары в списке "забрать срочно"
                x3 = self.pick_this_cards_urgently.index(i)                     # индекс нахождения этой карты в списке
                temp_x3 = j                                                     # запоминаем вторую карту пары
        #-------------------------------------------
            if j in self.never_touch_cards:                                     # если вторая карта пары в блоке ненужных
                y1 = self.never_touch_cards.index(j)                            # индекс нахождения этой карты в списке
                temp_y1 = i                                                     # запоминаем первую карту пары
            elif j in self.pick_this_cards_afterwards:                          # если вторая карта пары в списке "забрать потом"
                y2 = self.pick_this_cards_afterwards.index(j)                   # индекс нахождения этой карты в списке
                temp_y2 = i                                                     # запоминаем первую карту пары
            elif j in self.pick_this_cards_urgently:                            # если вторая карта пары в списке "забрать срочно"
                y3 = self.pick_this_cards_urgently.index(j)                     # индекс нахождения этой карты в списке
                temp_y3 = i                                                     # запоминаем первую карту пары
        #-------------------------------------------
            if temp_x1 != 7:                                                    # первая карта попала в список ненужных
                self.never_touch_cards[x1] = temp_x1                            # меняем на место второй карты в паре
            if temp_y1 != 7:                                                    # вторая карта попала в список ненужных
                self.never_touch_cards[y1] = temp_y1                            # меняем на место первой карты в паре
            if temp_x2 != 7:                                                    # первая карта попала в список "на потом"
                self.pick_this_cards_afterwards[x2] = temp_x2                   # меняем на место второй карты в паре
            if temp_y2 != 7:                                                    # вторая карта попала в список "на потом"
                self.pick_this_cards_afterwards[y2] = temp_y2                   # меняем на место первой карты в паре
            if temp_x3 != 7:                                                    # первая карта попала в список "забрать срочно"
                self.pick_this_cards_urgently[x3] = temp_x3                     # меняем на место второй карты в паре
            if temp_y3 != 7:                                                    # вторая карта попала в список забрать срочно
                self.pick_this_cards_urgently[y3] = temp_y3                     # меняем на место первой карты в паре
# ----------------------------------------------------
        def usual_card_choose(self):                                            # "обычный" выбор карты у Семёна
            temp = []                                                           # пустой слот для отдачи
            if len(self.pick_this_cards_urgently) != 0:                         # если список "забрать срочно" не пустой
                res = self.pick_this_cards_urgently[0]                          # а вот самую первую оттедова и тянем
            elif len(self.pick_this_cards_afterwards) != 0:                     # если список "забрать потом" не пустой
                res = self.pick_this_cards_afterwards[0]                        # а вот самую первую оттедова и тянем
            else:                                                               # если срочно ничего забирать не надо
                if len(self.never_touch_cards) != 0:                            # если список ненужных карт не пустой
                    for item in set(range(0,n_cards)).difference(self.never_touch_cards): #перебрали список от 0 до числа карт; выводим те, которых нет в ненужных
                        if cards_my[item].name != name_of_none:             # если очередная карта не пустая
                            temp.append(item)                               # добавим её в список на вытягивание
                    res = random.choice(temp)                               # выбираем рандомно из списка на забор
                else:                                                       # если ненужных карт нет
                    res = random.randrange(0,n_cards)                       # рандом изо всех
                    if cards_my[res].interesting:                           # если карта уже отмечена
                        y = random.choice([True,False])                     # подумаем, а не выбрать ли другую
                        if y:                                               # если выбрать другую
                            res = random.randrange(0,n_cards)               # выбираем ёщё раз рандомно из всех
                            while cards_my[res].name == name_of_none:       # пока попадается карта пустая
                                res = random.randrange(0,n_cards)           # выбираем другую
                    else:                                                   # если карта не отмечена
                        while cards_my[res].name == name_of_none:           # пока попадается карта пустая
                            res = random.randrange(0,n_cards)               # выбираем другую
            return res
# ----------------------------------------------------
        def random_card_choose(self):                                       # "случайный" выбор карты у Семёна
            x = random.randrange(0,n_cards)                                 # рандом изо всех
            while cards_my[x].name == name_of_none:                         # если карта пустая
                x = random.randrange(0,n_cards)                             # выбираем другую
            return x
# ----------------------------------------------------
        def what_card_choose(self):                                             # какую карту будем выбирать у Семэна?
            global cycles_left                                                  # потребуется количество оставшихся циклов
            self.how_skill()                                                            # проверяем навык
            if (self.playstyle in ['defense','succumb']) and (not self.make_mistakes):  # если защита или слив и не ошибаемся
                res = self.usual_card_choose()                                          # "обычный выбор" у Семёна
        #-------------------------------------------
            elif (self.playstyle =='gamble') and (not self.make_mistakes):          # если рискуем и не ошибаемся
                self.what_cards_have()                                              # проверяем, что там у нас на руках

                if self.combo_was_before == None:                                   # если комбинации еще не сравнивали
                    self.combo_was_before = []                                      # создаём пустой список
                if len(self.combo_was_before) == 0:                                 # если список пустой
                    self.combo_was_before = [0,0,0,0]                               # создаём заполнитель для проверки

                if (self.combo_was_before[0] >= 4) and (self.as_changed_combo == 'worse'):  # если был стрит и выше и положение ухудшилось
                    res = self.usual_card_choose()                                          # "обычный выбор" у Семёна, нефиг рисковать
                else:                                                                       # во всех других случаях
                    if (len(self.table_card_suit) !=0) or (len(self.table_card_sequence_min) !=0) or (len(self.table_card_sequence_max) !=0): # если осталось, из-за чего рисковали
                        if cycles_left == 3:                                            # если осталось три круга
                            res = self.random_card_choose()                             # "случайный выбор" у Семёна - рискуем, однако
                        elif cycles_left == 2:                                          # если осталось два круга
                            if len(self.pick_this_cards_urgently) <= 1:                 # если количество карт, что надо забрать строчно - нет или одна
                                res = self.random_card_choose()                         # "случайный выбор" у Семёна - рискуем, однако
                                while res in self.never_touch_cards:                    # если "случайная" карта и нам не нужна
                                    res = self.random_card_choose()                     # ещё "случайный выбор" у Семёна
                            else:                                                       # если срочно забрать надо две карты
                                res = self.usual_card_choose()                          # "обычный выбор" у Семёна
                        elif cycles_left == 1:                                          # если остался один круг
                            if len(self.pick_this_cards_urgently) == 0:                 # вдруг ничего срочно забрать не надо
                                res = self.random_card_choose()                         # "случайный выбор" у Семёна - рискуем до упора
                                while res in self.never_touch_cards:                    # если "случайная" карта и нам не нужна
                                    res = self.random_card_choose()                     # ещё "случайный выбор" у Семёна
                            else:                                                       # свою карту надо забирать и срочно
                                res = self.usual_card_choose()                          # "обычный выбор" у Семёна
                    else:                                                               # если рисковать уже смысла нет
                        if self.combo_in_hand[0] >=4:                                   # если риск оправдался
                            self.pick_this_cards_urgently = []                          # удаляем карты "забрать срочно"
                            self.pick_this_cards_afterwards = []                        # удаляем карты "забрать потом"
                        res = self.usual_card_choose()                                  # "обычный выбор" у Семёна
        #-------------------------------------------
            elif (self.playstyle == 'foolplay') or (self.make_mistakes):        # если включили дурака или ошибаемся
                res = self.random_card_choose()                                 # "случайный выбор" у Семёна
        #-------------------------------------------
            return res
# ----------------------------------------------------
        def pick_my_card_last_think(self):                                      # последняя выделенная карта игрока - используется в режиме (соперник забирает)
            self.how_skill()                                                    # проверяем навык
            if (self.playstyle in ['defense','gamble']) and (not self.make_mistakes): # если защита или риск и не ошибаемся
                x = self.pick_my_card_last_usual()                              # обычный выбор последней карты

            elif (self.playstyle == 'succumb') and (not self.make_mistakes):    # если слив и не ошибаемся
                if self.last_selected_card !=7 :                                # если определена последняя выбранная карта
                    if self.last_selected_card not in self.never_touch_cards:   # если последняя выбранная НЕ в списке тех, которые "не трогать"
                        x = self.last_selected_card                             # выбираем ту карту, которую нам подсунули
                    else:                                                       # Семён подсунул ту карту, что "не трогать"
                        if len(self.pick_this_cards_urgently) !=0:              # список "забрать срочно" НЕ пустой
                            x = self.pick_this_cards_urgently[0]                # а вот самую первую и выбираем
                        elif len(self.pick_this_cards_afterwards) !=0:          # список "забрать потом" НЕ пустой
                            x = self.pick_this_cards_afterwards[0]              # а вот самую первую и выбираем
                        else:                                                   # списки "забрать эти карты" пустые
                            x = self.pick_my_card_last_usual()                  # обычный выбор последней карты
                else:                                                           # последний выбор не определен
                    x = self.pick_my_card_last_random()                         # рандомный выбор

            elif (self.playstyle == 'foolplay') or (self.make_mistakes):        # если включили дурака или ошибаемся
                x = self.pick_my_card_last_random()                             # рандомный выбор

            self.last_selected_card = 7                                         # сбрасываем последнюю выбранную карту
            self.what_is_pulled_out(x)                                          # проверяем, что вынули у Семёна
            return x
# ----------------------------------------------------
        def pick_my_card_last_usual(self):                                      # последняя выделенная карта игрока - обычный режим
            for i in range(0,n_cards):                                          # перебрать карты
                if  cards_my[i].interesting:                                    # если карта игрока выделена соперником
                    x = i                                                       # вернуть место карты в стеке
            return x
# ----------------------------------------------------
        def pick_my_card_last_random(self):                                     # последняя выделенная карта игрока - ослучайный выбор
            x = random.randrange(0,n_cards)                                     # рандом изо всех
            while cards_my[x].name == name_of_none:                             # если карта пустая
                x = random.randrange(0,n_cards)                                 # выбираем другую
            return x
# ----------------------------------------------------
        def what_is_pulled_out(self,i):                                         # проверяем, что вынули у Семёна (номер его карты)
            if i in self.pick_this_cards_urgently:                              # если карта входит в список карт "забрать срочно"
                self.pick_this_cards_urgently.remove(i)                         # удаляем эту карту
            if i in self.pick_this_cards_afterwards:                            # если карта входит в список карт "забрать потом"
                self.pick_this_cards_afterwards.remove(i)                       # удаляем эту карту
            if i in self.never_touch_cards:                                     # если карта входит в список карт "не забирать"
                self.never_touch_cards.remove(i)                                # удаляем эту карту
# ----------------------------------------------------
        def give_away_card_think(self):                                         # что отдаём при игре на 7 картах ?
            self.how_skill()                                                    # проверяем навык
            if (self.playstyle in ['defense','succumb']) and (not self.make_mistakes): # если защищаемся или сливаем и не ошибаемся
                if len (self.this_give_definitely_succumb) != 0:                    # если список срочного слива не пустой
                    if self.combo_in_hand[0] not in [4,5,8,9]:                      # если НЕ флэш или стрит
                        i = random.choice(self.this_give_definitely_succumb)        # случайную карту из срочного слива предлагаем
                    else:                                                           # если есть что сливать, но комбинация старше
                        i = self.give_away_card_think_usual()                       # предлагаем на обмен то, что обычно
                else:                                                               # список срочного слива пустой
                    i = self.give_away_card_think_usual()                           # предлагаем на обмен то, что обычно
            elif (self.playstyle =='gamble') and (not self.make_mistakes):      # если рискуем и не ошибаемся
                if self.combo_in_hand[0] < 4:                                       # если меньше стрита
                    if len(self.table_card_possible_combo) !=0:                     # если что-то есть в возможной комбинации
                        i = 7                                                       # индекс отдаваемой карты принимаем 7
                        if len(self.its_urgent_shove) !=0:                          # если список того, что надо сдать, не пустой
                            for j in range (0,len(self.its_urgent_shove)):          # перебираем его и..
                                if self.its_urgent_shove[j] not in self.table_card_possible_combo:  # если очередная карта не в потенциальной комбинации
                                    i = self.its_urgent_shove[j]                    # первую же такую карту и отдаём
                                    break                                           # и цикл завершаем
                        if i == 7:                                                  # не нашли подходящую карту в срочном сбросе
                            if len(self.these_proposed_to_take) !=0:                # есть что предлагать вообще
                                for j in range (0,len(self.these_proposed_to_take)):# перебираем его и..
                                    if self.these_proposed_to_take[j] not in self.table_card_possible_combo:  # если очередная карта не в потенциальной комбинации
                                        i = self.these_proposed_to_take[j]          # первую же такую карту и отдаём
                                        break                                       # и цикл завершаем
                        if i == 7:                                                  # не нашли подходящую карту в предлагаемых на сброс
                            if len(self.can_give_in_a_pinch) !=0:                   # что-то есть в крайнем случае
                                for j in range (0,len(self.can_give_in_a_pinch)):   # перебираем его и..
                                    if self.can_give_in_a_pinch[j] not in self.table_card_possible_combo:  # если очередная карта не в потенциальной комбинации
                                        i = self.can_give_in_a_pinch[j]             # первую же такую карту и отдаём
                                        break                                       # и цикл завершаем
                        if i == 7:                                                  # что-то найти была не судьба
                            i = self.give_away_card_think_usual()                   # предлагаем на обмен то, что обычно
                    else:                                                           # если в возможной комбинации ничего нет
                        i = self.give_away_card_think_usual()                       # предлагаем на обмен то, что обычно
                else:                                                               # если стрит и выше
                    i = self.give_away_card_think_usual()                           # предлагаем на обмен то, что обычно
            elif (self.playstyle == 'foolplay') or (self.make_mistakes):        # если включили дурака или ошибаемся
                i = random.randrange(0,n_cards)                                 # отдаём случайную карту (из нужных и ненужных)
            return i
# ----------------------------------------------------
        def give_away_card_think_usual(self):                                   # что отдаём при игре на 7 картах - обычно
            if len(self.its_urgent_shove) != 0:                                 # если список того, что надо сдать, не пустой
                i = random.choice(self.its_urgent_shove)                        # случайная карта из списка на срочное впаривание
            elif len(self.these_proposed_to_take) !=0:                          # если вдруг случится так, что срочно впарить нечего  и есть, что предложить на обмен
                i = random.choice(self.these_proposed_to_take)                  # случайная карта из предлагаемых к отдаче
            elif len(self.can_give_in_a_pinch) !=0:                             # если ничего нет в первых вариантах, но не пустой список крайнего случая
                i = random.choice(self.can_give_in_a_pinch)                     # случайная карта из отдаваемых в крайнем случае
            return i
# ----------------------------------------------------
        def how_skill(self):                                                    # проверка навыка (вероятность ошибки)
            self.make_mistakes = True                                           # включаем режим ошибки
            i = random.choice([1,2,3,4,5])                                      # рандомно выбираем значение вероятности ошибки, шанс ошибки: 5-0%, 4-20%, 3-40% 2-60% 1-80%
            if i <= self.mistake_chance:                                        # если вероятность ошибки меньше или равна навыку
                self.make_mistakes = False                                      # не ошибаемся
# ----------------------------------------------------



##########################  ИГРОКИ  #####################################



# =======================================================================
    class DSCardGameRivalWiseUsual(DSCardGameRivalWise):                    # обычный игрок
        def allow_to_take(self):                                            # разрешение на выбор карт у соперника при ходе игрока (обычный соперник)
            for i in range(0,n_cards):                                      # перебираем карты
                cards_rival[i].allow = True                                 # для каждой карты = доступна для выбора
# ----------------------------------------------------
        def allow_to_defend(self):                                          # режим защиты обычного игрока
            return True
# ----------------------------------------------------
        def want_to_defend(self):                                           # разрешение ИГРОКУ на защиту (отличается у Ульяны в классике)
            return True

# =======================================================================
    class DSCardGameRivalWiseLikeUS(DSCardGameRivalWise):                   # стиль игры - как у Ульяны
        def what_card_choose(self):                                         # переопределённый метод - за Ульяну выбирает Семён
            type,index = ds_cards_interact()                               # из-за этой строки
            return index
# ----------------------------------------------------
        def allow_to_take(self):                                            # разрешение на выбор карт у соперника при ходе игрока (Ульяна)
            for i in range(0,n_cards):                                      # перебираем карты
                cards_rival[i].allow = False                                # делаем ВСЕ карты соперника недоступными для выбора
            self.how_skill()                                                # проверяем навык
        #-------------------------------------------
            if (self.playstyle in ['defense','gamble','succumb']) and (not self.make_mistakes): # если стиль игры из определённых и не ошибаемся
                if len(self.its_urgent_shove) != 0:                             # если есть, что срочно отдать
                    i = random.choice(self.its_urgent_shove)                    # случайная карта из ненужных
                elif len(self.these_proposed_to_take) != 0:                     # если срочного нет, но есть, что можно предложить на обмен
                    i = random.choice(self.these_proposed_to_take)              # случайная карта из обменных
                elif len(self.can_give_in_a_pinch) != 0:                        # если ненужных нет, но есть что отдать в крайнем случае
                    i = random.choice(self.can_give_in_a_pinch)                 # случайная из крайнего случая
        #-------------------------------------------
            elif (self.playstyle == 'foolplay') or (self.make_mistakes):        # если включили дурака или ошибаемся
                i = random.choice(self.yourself_need_cards+self.waste_cards)    # отдаём случайную карту из числа нужных + ненужных
        #-------------------------------------------
            cards_rival[i].allow = True                                         # выбранную карту делаем доступной для выбора
            cards_rival[i].interesting = True                                   # и её же выделяем стрелкой
# ----------------------------------------------------
        def want_to_defend(self):                                               # режим защиты Ульяны
            return False
# ----------------------------------------------------
        def allow_to_defend(self):                                              # разрешение Ульяне на защиту (нет)
            return False

init 1 python:                                              # начинаем на шаг позже оригинала
    ds_hint_poker = False                                  # окна с подсказками отключены
    ds_my_poker_hand = None                                # моя комбинация (цифры)
    ds_rival_poker_hand = None                             # комбинация соперника (цифры)
    ds_name_my_poker_hand = None                           # моя комбинация для подсказки
    ds_name_rival_poker_hand  = None                       # комбинация соперника для подсказки
    ds_whose_first_move = 'rival'                          # кто первый ходит (соперник - 'rival'; игрок - 'player')
    ds_name_my_rival_r = "соперника"                       # подписываем "подсказку" соперника

# ---------------------------------------------------------------------------------------------
    def ds_show_cards():
        renpy.scene('underlay')
        renpy.show(cards_bg,layer='underlay')
        ui.layer('underlay')
        for i in range(0,n_cards):
            if  cards_rival[i].interesting :
                x = int(card_dx*i+card_left_dx+card_width/2.0-arrow_width/2.0)
                y = card_top_dy+card_height+20
                ui.at( Move( (x,y), (x,y), 1 ) )
                ui.image(card_up,xpos=x,ypos=y)
            if  cards_state == "me_select_2" and cards_rival[i].allow:
                card_button(cards_rival[i], card_dx*i+card_left_dx, card_top_dy+cards_rival[i].dy, ("rival",i))
            else:
                card_button(cards_rival[i], card_dx*i+card_left_dx, card_top_dy+cards_rival[i].dy, "ignore")
            if  cards_my[i].interesting:
                x = int(card_dx*i+card_left_dx+card_width/2.0-arrow_width/2.0)
                y = card_bottom_dy-100
                ui.at( Move( (x,y), (x,y), 1 ) )
                ui.image(card_down,xpos=x,ypos=y)
            if  cards_state in ["me_select_1","me_defend_1","me_defend_2","rival_select"] or (cards_state == "me_select_2" and i==my_card) :
                card_button(cards_my[i], card_dx*i+card_left_dx, card_bottom_dy+cards_my[i].dy, ("my",i))
            else:
                card_button(cards_my[i], card_dx*i+card_left_dx, card_bottom_dy+cards_my[i].dy, "ignore")

        if  cards_state in ["interuption","init"]:
            ui.close()
            return

        avatar = LiveComposite(
            (210,210),
            (0,0), avatar_frame,
            (5,5), rival.avatar
        )

        ui.imagebutton(avatar,avatar,clicked=None,
            xpos=card_dx*(n_cards)+card_left_dx+20,
            ypos=card_top_dy,
        )

        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
            xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
            ypos=card_top_dy+220,
            style=style.cards_button,
        )
        ui.text(u"Соперник:",style="button_text",size=15)

        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
            xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
            ypos=card_top_dy+240,
            style=style.cards_button,
        )
        ui.text(rival.name,style="button_text",size=25)

        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
            xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
            ypos=card_bottom_dy+0,
            style=style.cards_button,
        )
        ui.text(u"Чей ход:",style="button_text",size=15)

        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
            xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
            ypos=card_bottom_dy+20,
            style=style.cards_button,
        )
        if  cards_state in ["me_defend_1","me_defend_2","me_get","me_select_1","me_select_2"]:
            ui.text(u"Твой",style="button_text",size=25)
        if  cards_state in ["rival_defend","rival_get","rival_select"]:
            ui.text(u"Чужой",style="button_text",size=25)
        if  cards_state in ["results"]:
            ui.text(u"---",style="button_text",size=25)

        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
            xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
            ypos=card_bottom_dy+90 - button_dy,
            style=style.cards_button,
        )
        ui.text(u"Фаза игры:",style="button_text",size=15)

        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
            xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
            ypos=card_bottom_dy+110 - button_dy,
            style=style.cards_button,
        )
        if  cards_state in ["me_defend_1","me_defend_2","rival_defend"]:
            ui.text(u"Защита",style="button_text",size=25)
        if  cards_state == "me_select_1":
            ui.text(u"Сброс",style="button_text",size=25)
        if  cards_state in ["me_select_2","rival_select"]:
            ui.text(u"Захват",style="button_text",size=25)
        if  cards_state in ["me_get","rival_get"]:
            if  CARD_GAME_WITH_EXCHANGE:
                ui.text(u"Обмен",style="button_text",size=25)
            else:
                ui.text(u"Вытягивание",style="button_text",size=25)
        if  cards_state in ["results"]:
            ui.text(u"Итоги",style="button_text",size=25)

        if  cards_state in ["me_defend_1","me_defend_2"]:
            ui.button(clicked=ui.returns("end_of_turn"), xanchor=1.0, xpadding=6, xminimum=25,
                xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
                ypos=card_bottom_dy+110 - button_dy,
                style=style.cards_button,
            )
            ui.text(u"X",style="button_text",size=25)

        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
            xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
            ypos=card_bottom_dy+180 - button_dy,
            style=style.cards_button,
        )
        ui.text(u"Кругов осталось:",style="button_text",size=15)

        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
            xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
            ypos=card_bottom_dy+200 - button_dy,
            style=style.cards_button,
        )
        ui.text("%d"%cycles_left,style="button_text",size=25)

        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
            xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
            ypos=card_bottom_dy+270 - button_dy,
            style=style.cards_button,
        )
        ui.text(u"Обменов осталось:",style="button_text",size=15)

        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
            xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
            ypos=card_bottom_dy+290 - button_dy,
            style=style.cards_button,
        )
        if  changes_left == 0:
            changes_left_text = "---"
        else:
            changes_left_text = "%d"%changes_left
        ui.text(changes_left_text,style="button_text",size=25)

        if VISIBLE and ds_hint_poker:
            ui.button(clicked=None, xanchor=0.5, xpadding=10, xminimum=400,
                xpos = screen_width/2,
                ypos = screen_height - card_top_dy - bottom_dy,
                style=style.cards_button,
            )
            ui.text("%s — %s" % ("У меня", ds_name_my_poker_hand),style="button_text",size=23)

        if (INVISIBLE or cards_rival[0].visible == 'VISIBLE') and ds_hint_poker:
            ui.button(clicked=None, xanchor=0.5, xpadding=10, xminimum=400,
                xpos = screen_width/2,
                ypos = card_top_dy - 28,
                style=style.cards_button,
            )
            ui.text("%s %s — %s" % ("У", ds_name_my_rival_r, ds_name_rival_poker_hand),style="button_text",size=23)

        if  result_status != 'in_progress':
            renpy.block_rollback()
            ui.button(clicked=ui.returns("ok"), xanchor=1.0, xpadding=6, xminimum=200,
                xpos=screen_width/2+100,
                ypos=screen_height/2-35 - bottom_dy - bottom_dy_result,
                style=style.cards_button,
            )
            if  result_status == 'win':
                ui.text(u"Победа",style="button_text",size=72)
            if  result_status == 'draw':
                ui.text(u"Ничья",style="button_text",size=72)
            if  result_status == 'fail':
                ui.text(u"FAIL",style="button_text",size=72)
        ui.close()

# -----------------------------------------------------------------------------------------------------------------------------------------------------
    def ds_cards_interact():
        ds_show_cards()
        answer = ui.interact()
        if  answer=="ignore":
            ui.jumps("ds_cards_gameloop")()
        if cards_state == "me_defend_1":
            renpy.music.play("sound/sfx/cardgame/new/choose_card_2.ogg", channel="sound")
        elif cards_state == "me_defend_2":
            renpy.music.play("sound/sfx/cardgame/new/choose_card_1.ogg", channel="sound")
        return answer
# -----------------------------------------------------------------------------------------------------------------------------------------------------
    def ds_card_value(ace_high, x): # Получаем значения карт
        if  (x.name[0] == 1) and ace_high:
            return 14
        else:
            return x.name[0]
# -----------------------------------------------------------------------------------------------------------------------------------------------------
    def ds_sort_cards(ace_high=True): # сортировка
        cards_rival.sort(cmp, partial(ds_card_value, ace_high))
        cards_my.sort(cmp, partial(ds_card_value_as_max, ace_high))

    def ds_sort_cards_upshot(): # итоговая сортировка карт
        global cards_rival
        global cards_my

        rival_hand = ds_what_category(cards_rival)                     # посмотрели, что на руках у соперника
        my_hand = ds_what_category(cards_my)                           # посмотрели, что у нас на руках

        cards_rival.sort(cmp,partial(ds_card_value,
            not (rival_hand[0] in [4,8] and rival_hand[1] == 5)))       # сортируем карты соперника
        cards_rival.reverse()                                           # "переворачиваем" карты - старшая карта слева
        if not CARD_GAME_WITH_EXCHANGE:                                 # если сдавалось по шести карт
            temp = cards_rival.pop(n_cards-1)                           # "вынимаем" последнюю (правую) - пустую карту
            cards_rival.insert(0,temp)                                  # .. и "вставляем" её в начало (слева)

        cards_rival.sort(cmp,partial(ds_card_value,
            not (rival_hand[0] in [4,8] and rival_hand[1] == 5)))       # сортируем свои карты
        cards_my.reverse()                                              # "переворачиваем" карты - старшая карта слева
        if not CARD_GAME_WITH_EXCHANGE:                                 # если сдавалось по шести карт
            temp = cards_my.pop(n_cards-1)                              # "вынимаем" последнюю (правую) - пустую карту
            cards_my.insert(0,temp)                                     # .. и "вставляем" её в начало (слева)

# -----------------------------------------------------------------------------------------------------------------------------------------------------
    def ds_interuption_region():
        global cycles_left
        global cards_state
        if cards_state == "me_select_1" or cards_state == "me_defend_1": #Ошибка?
            renpy.music.play("sound/sfx/cardgame/new/choose_card_2.ogg", channel="sound")
        elif cards_state == "rival_defend":
            renpy.music.play("sound/sfx/cardgame/new/choose_card_1.ogg", channel="sound")
        position = (cycles_left,cards_state,"call")
        if  position in game_interuptions:
            tmp_state = cards_state
            cards_state = "interuption"
            ds_show_cards()
            renpy.call_in_context(game_interuptions[position])
            renpy.block_rollback()
            cards_state = tmp_state
            del game_interuptions[position]
        position = (cycles_left,cards_state,"jump")
        if  position in game_interuptions:
            tmp_state = cards_state
            cards_state = "interuption"
            renpy.scene('underlay')
            ui.jumps(game_interuptions[position])()
# -----------------------------------------------------------------------------------------------------------------------------------------------------
# Покерные комбинации (по старшинству):
#  9 - Роял-флеш      (royal flush)       = Т,К,Д,В,10 одной масти
#  8 - Стрит-флеш     (straight flush)    = 5 карт по порядку ОДНОЙ масти, туз может быть первым (роял-флеш) и последним (..3,2,Т)
#  7 - Каре           (quads)             = 4 карты одного достоинства
#  6 - Фул-хауз       (full house)        = тройка + пара
#  5 - Флеш           (flush)             = 5 карт ОДНОЙ масти
#  4 - Стрит          (straight)          = 5 карт по порядку ЛЮБОЙ масти, туз может быть первым (Т,К,Д..) и последним (..3,2,Т)
#  3 - Тройка         (three of a kind)   = 3 карты одного достоинства
#  2 - Две пары       (two pairs)         = две двойки
#  1 - Одна пара      (one pair)          = 2 карты одного достоинства
#  0 - Старшая карта  (high card)         = ни одной вышеперечисленной комбинации, берется старшая карта
#
# Если комбинации одинаковы = выигрыш по большей карте в комбинации
#
# Масти: "2ch","ussr","utan","uvao"
# Картинки: В = 11, Д = 12, К = 13, Т = 1 / 14
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def ds_what_suit_cards(cardset):                               # определяем количество карт в мастях - передаем кардсет
        cardset_tmp = cardset[:]                                    # копируем кардсет, упражняемся с ним, не трогаем основной
    # ----------------------------------------------------
        total_2ch = 0                                               # количество карт масти 2ch
        total_ussr = 0                                              # количество карт масти ussr
        total_utan = 0                                              # количество карт масти utan
        total_uvao = 0                                              # количество карт масти uvao
        value_2ch = 0                                               # старшая карта масти 2ch
        value_ussr = 0                                              # старшая карта масти ussr
        value_utan = 0                                              # старшая карта масти utan
        value_uvao = 0                                              # старшая карта масти uvao
        suit_max = 0                                                # количество карт максимальной масти
        suit_value = 0                                              # старшая карта максимальной масти
        suit_numb = None                                            # номер максимальной масти
    # ----------------------------------------------------
        cardset_tmp.sort(cmp,partial(ds_card_value, True))                 # сортируем список от 2
    # ----------------------------------------------------
        for i in range(0,n_cards):
            if cardset_tmp[i].name[1] == "2ch":                     # если карта ЭТОЙ масти
                total_2ch += 1                                      # увеличиваем счетчик ЭТОЙ масти на 1
                value_2ch = cardset_tmp[i].name[0]                  # значение максимума принимаем по значению карты
            elif cardset_tmp[i].name[1] == "ussr":
                total_ussr += 1
                value_ussr = cardset_tmp[i].name[0]
            elif cardset_tmp[i].name[1] == "utan":
                total_utan += 1
                value_utan = cardset_tmp[i].name[0]
            elif cardset_tmp[i].name[1] == "uvao":
                total_uvao += 1
                value_uvao = cardset_tmp[i].name[0]
    # ----------------------------------------------------
        suit_max = max(total_2ch, total_ussr, total_utan, total_uvao) # выясняем максимум карт одной масти
        if suit_max >= 5:                                           # если максимальное количество карт в масти >= 5
            if suit_max == total_2ch:                               # если max = ЭТОЙ масти
                suit_numb = 0                                       # номер масти = ЭТОЙ масти
                suit_value = value_2ch                              # старшая карта - по ЭТОЙ масти
            elif suit_max == total_ussr:
                suit_numb = 1
                suit_value = value_ussr
            elif suit_max == total_utan:
                suit_numb = 2
                suit_value = value_utan
            elif suit_max == total_uvao:
                suit_numb = 3
                suit_value = value_uvao
    # ----------------------------------------------------
            if suit_value == 1:                                     # если туз определился, как младший
                suit_value = 14                                     # возвращаем 14 очков
    # ----------------------------------------------------
        return suit_numb, suit_value                                # возвращаем имя масти, максмальную карту масти
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def ds_what_sequence_cards(cardset):                            # определяем последовательность карт у нас на руках - передаем кардсет
        cardset_tmp = cardset[:]                                    # копируем кардсет, упражняемся с ним, не трогаем основной
    # ----------------------------------------------------
        combo_sequence = False                                      # последовательности нет
        orders = ['min','max']                                      # туз - младший, старший
        order = None
        len_seq_max_k = [0,0]                                       # количество карт в максимальной последовательности [мин, макс]
        seq_value_k = [0,0]                                         # старшая карта в последовательности  [мин, макс]
        len_seq_max = 0                                             # количество карт в максимальной последовательности ИТОГО
        seq_value = 0                                               # старшая карта в последовательности ИТОГО
    # ----------------------------------------------------
        for k in range(0,2):                                        # для минимума (0) и максимума (1)
            order = orders[k]    
            cardset_tmp.sort(cmp,partial(ds_card_value, order=='max'))  # сортировка по порядку
            val_i = 0                                                   # количество очков текущей карты в переборе
            val_prev = 0                                                # количество очков предыдущей карты в переборе
            run_number = 0                                              # номер результативного прохода
            len_seq_run = 0                                             # количество карт в возможных последовательностях на проходах
            for i in range(0,n_cards):                              # цикл в цикле - перебираем карты
                val_i = ds_card_value(order=='max', cardset_tmp[i])
    # ----------------------------------------------------
                if val_i != 0:                                          # если карта нормальная
                    run_number += 1                                      # увеличиваем счетчих проходов
                    if run_number == 1:                                 # на первом проходе
                        len_seq_run = 1                                 # длину текущей последовательности принимаем = 1, карты не сравниваем - не с чем
                        len_seq_max_k[k] = 1                            # длину максимальной последовательности принимаем = 1, карты не сравниваем - не с чем
                    else:                                               # на следующих проходах
                        if val_i == (val_prev + 1):                     # если очередная карта в последовательности
                            len_seq_run += 1                            # длину текущей последовательности увеличиваем на 1
                            if len_seq_run > len_seq_max_k[k]:          # если текущая последовательность больше максимальной
                                len_seq_max_k[k] = len_seq_run          # максимальную последовательность принимаем по текущей
                                seq_value_k[k] = val_i                  # старшую карту принимаем по текущей
                        elif val_i == val_prev:                         # если карты равны
                            pass                                        # карту пропускаем, последовательность не сбрасываем
                        elif val_i > (val_prev + 1):                    # если очередная карта не в последовательности
                            len_seq_run = 1                             # длину текущей последовательности принимаем = 1
                    val_prev = val_i                                    # значение карты для сравнения принимаем: значение текущей карты
    # ----------------------------------------------------
        len_seq_max = max(len_seq_max_k)                                # максимальную длину последовательности принимаем по максимальной из мин-макс
        if len_seq_max == len_seq_max_k[1]:                             # если максимальная последовательность, когда туз старший
            seq_value = seq_value_k[1]                                  # очки старшей карты - по старшей карте, когда туз старший
        else:                                                           # если последовательности равны или минимальная больше
            seq_value = seq_value_k[0]                                  # очки старшей карты - по старшей карте, когда туз младший
            cardset_tmp.sort(cmp,ds_card_value_as_min)                 # и пересортировываем список от 1
    # ----------------------------------------------------
        if len_seq_max >= 5:                                            # если набрали последовательность в 5 карт или больше
            combo_sequence = True                                       #  - есть последовательность
    # ----------------------------------------------------
        return combo_sequence, seq_value                                # возвращаем наличие последовательности, значение старшей карты, набор карт
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def ds_what_amount_cards(cardset):                             # определяем количество карт по достоинству - передаем кардсет
        cardset_tmp = cardset[:]                                    # копируем кардсет, упражняемся с ним, не трогаем основной
    # ----------------------------------------------------
        amount_cards = []                                           # пустой список значений карт на руках
        val_i = 0                                                   # количество очков текущей карты в переборе, туз = 14
        is_four = False                                             # есть четверка
        is_triple = False                                           # есть тройка
        is_pair_one = False                                         # есть пара
        is_pair_two = False                                         # есть вторая пара
        amount_value_four = 0                                       # старшинство в комбинации 4
        amount_value_triple = 0                                     # старшинство в комбинации 3
        amount_value_pair = 0                                       # старшинство в комбинации 2
        amount_value_one = 0                                        # старшинство в комбинации 1
        combo_number = 0                                            # номер комбинации
        amount_value = 0                                            # старшая карта = 0
        amount_minor = 0                                            # старшинство младшей пары = 0
    # ----------------------------------------------------
        cardset_tmp.sort(cmp,partial(ds_card_value, True))                 # сортируем список от 2
    # ----------------------------------------------------
        for i in range(0,n_cards):
            val_i = ds_card_value(True, cardset_tmp[i])           # читаем значение очередной карты; туз = 14
            if val_i != 0:                                          # если карта нормальная
                amount_cards.append (val_i)                         # добавляем значение текущей карты в список
    # ----------------------------------------------------
        for j in range(2,15):                                       # пробежимся по значениям карт, (старшая - туз+1)
            if amount_cards.count(j) == 4:                          # проверяем четверку
                amount_value_four = j                               # старшинство в комбинации 4
                is_four = True                                      # есть черверка
                break                                               # есть четверка - дальнейшая проверка смысла не имеет
            elif amount_cards.count(j) == 3:                        # проверяем тройку
                if is_triple:                                       # если УЖЕ есть тройка
                    is_pair_two = True                              # младшую тройку назначаем парой
                    amount_minor = amount_value_triple              # старшинство младшей пары - по старой тройке
                    amount_value_triple = j                         # старшинство в комбинации 3
                    break                                           # есть вторая тройка - дальнейшая проверка смысла не имеет
                else:                                               # тройки еще нет
                    is_triple = True                                # есть тройка
                    amount_value_triple = j                         # старшинство в комбинации 3
                    continue                                        # эту цифру на пару не проверяем
            elif amount_cards.count(j) == 2:                        # проверяем пару
                if is_pair_one:                                     # пара УЖЕ есть
                    is_pair_two = True                              # принимаем вторую пару
                    amount_minor = amount_value_pair                # старшинство младшей пары - по старой паре
                    amount_value_pair = j                           # старшинство в комбинации 2
                    continue                                        # и проверяем следующую цифру
                else:                                               # пары еще нет
                    is_pair_one = True                              # есть пара
                    amount_value_pair = j                           # старшинство в комбинации 2
                    continue                                        # и проверяем следующую цифру
            elif amount_cards.count(j) == 1:                        # если комбинаций нет, но есть карта
                amount_value_one = j                                # назначается старшей
    # ----------------------------------------------------
        if is_four:                                                 # если нашли четверку
            amount_value = amount_value_four                        # старшинство - по четверке
            combo_number = 7                                        # комбинация = 'quads' = 7
        elif is_triple:                                             # если тройка
            amount_value = amount_value_triple                      # старшинство - по тройке
            if is_pair_one or is_pair_two:                          # + одна из пар
                combo_number = 6                                    # комбинация = 'full_house' = 6
                amount_minor = amount_value_pair                    # старшинство пары - по старшей паре
            else:                                                   # пар нет
                combo_number = 3                                    # комбинация = 'three_of_a_kind' = 3
        elif is_pair_one:                                           # если пара
            amount_value = amount_value_pair                        # старшинство - по паре
            if is_pair_two:                                         # + вторая пара
                combo_number = 2                                    # комбинация = 'two_pairs' = 2
            else:                                                   # второй пары нет
                combo_number = 1                                    # комбинация = 'one_pair' = 1
        else:
            amount_value = amount_value_one                         # старшинство - по карте
            combo_number = 0                                        # комбинация = 'нет' = 0
        return combo_number, amount_value, amount_minor             # возвращаем: номер комбинации, старшинство в комбинации, старшинство младшей пары
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def ds_mark_suit_cards(cardset,suit_numb):                     # маркируем карты в мастях - передаем кардсет
        cardset_tmp = cardset[:]                                    # копируем кардсет, упражняемся с ним, не трогаем основной
        cardset_tmp.sort(cmp,ds_card_value_as_max)                 # сортируем список от 2
        j = n_cards-1                                               # счетчик = количество карт -1
        k = 0                                                       # признак достаточности
        while j >= 0:                                                # перебираем карты со старшей
            if cardset_tmp[j].suit == suit_numb:                    # если номер масти карты = номер масти
                cardset_tmp[j].in_combo = True                      # карта в комбинации
                k += 1                                              # к признаку достаточности +1
                if k == 5:                                          # насчитали 5 карт
                    break                                           # перебор можно закончить
            j -= 1                                                  # уменьшаем счетчик
        return cardset_tmp                                          # возвращаем набор карт
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def ds_mark_sequence_cards(cardset, seq_value):                # маркируем карты в последовательности - передаем кардсет, старшую карту
        cardset_tmp = cardset[:]                                    # копируем кардсет, упражняемся с ним, не трогаем основной
        cardset_tmp.sort(cmp,partial(ds_card_value, seq_value==14)) # сортируем список
        j = n_cards-1                                               # счетчик = количество карт -1
        k = 0                                                       # признак достаточности
        val = seq_value                                             # ожидаемое значение очков = максимальному
        while j >= 0:                                                # перебираем карты со старшей
            if ds_card_value(True, cardset_tmp[j]) == val or ds_card_value(False, cardset_tmp[j]) == val:  # значение очередной карты = ожидаемому
                cardset_tmp[j].in_combo = True                      # карта в комбинации
                k += 1                                              # к признаку достаточности +1
                val -= 1                                             # уменьшаем ожидаемое значение
            if k == 5:                                              # если насчитали 5 карт
                break                                               # перебор можно закончить
            j -= 1                                                  # уменьшаем счетчик
        return cardset_tmp                                          # возвращаем набор карт
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def ds_mark_amount_cards(cardset, combo, value, minor):        # маркируем карты по количеству - передаем кардсет, комбинацию, старшую карту, младшую пару
        cardset_tmp = cardset[:]                                    # копируем кардсет, упражняемся с ним, не трогаем основной
        cardset_tmp.sort(cmp,ds_card_value_as_max)                 # сортируем список от 2
        j = n_cards-1                                               # счетчик = количество карт -1
        k = 0                                                       # признак достаточности
        if combo == 1:                                              # если пара
            m = 2                                                   # количество для сравнения
        elif combo == 3:                                            # если тройка
            m = 3                                                   # количество для сравнения
        elif combo in [2,7]:                                        # если две пары или покер
            m = 4                                                   # количество для сравнения
        elif combo == 6:                                            # если фулл-хаус
            m = 5                                                   # количество для сравнения
        while j >= 0:                                                # перебираем карты со старшей
            if combo == 0:                                          # если одна карта
                cardset_tmp[j].in_combo = True                      # её и маркируем
                break                                               # и прерываем цикл
            elif combo in [7,3,1]:                                  # если простая последовательность
                if ds_card_value_as_max(cardset_tmp[j]) == value:  # если количество очков карты совпадает с максимальным
                    cardset_tmp[j].in_combo = True                  # карта в комбинации
                    k += 1                                          # к признаку достаточности +1
                if k == m:                                          # если насчитали нужное количество карт
                    break                                           # перебор можно закончить
            elif combo == 2:                                        # если две пары
                if ds_card_value_as_max(cardset_tmp[j]) == value:  # если количество очков карты совпадает с максимальным
                    cardset_tmp[j].in_combo = True                  # карта в комбинации
                    k += 1                                          # к признаку достаточности +1
                if k == 2:                                          # если насчитали две карты
                    i = j                                           # устанавливаем счетчик - по последней карте старшей пары
                    while i >= 0:                                    # перебираем карты со старшей
                        if ds_card_value_as_max(cardset_tmp[i]) == minor:  # если количество очков карты совпадает с минорной парой
                            cardset_tmp[i].in_combo = True          # карта в комбинации
                            k += 1                                  # к признаку достаточности +1
                        if k == m:                                  # если насчитали нужное количество карт
                            break                                   # перебор можно закончить
                        i -= 1                                      # уменьшаем счетчик
            elif combo == 6:                                        # если 3+2
                if ds_card_value_as_max(cardset_tmp[j]) == value:  # если количество очков карты совпадает с максимальным
                    cardset_tmp[j].in_combo = True                  # карта в комбинации
                    k += 1                                          # к признаку достаточности +1
                if k == 3:                                          # если насчитали три карты
                    i = n_cards-1                                   # устанавливаем счетчик по максимуму (перебор по новой)
                    while i >= 0:                                    # перебираем карты со старшей
                        if ds_card_value_as_max(cardset_tmp[i]) == minor:  # если количество очков карты совпадает с минорной парой
                            cardset_tmp[i].in_combo = True          # карта в комбинации
                            k += 1                                  # к признаку достаточности +1
                        if k == m:                                  # если насчитали нужное количество карт
                            break                                   # перебор можно закончить
                        i -= 1                                      # уменьшаем счетчик
            j -= 1                                                  # уменьшаем счетчик
        return cardset_tmp                                          # возвращаем набор карт
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def ds_what_category(cardset): # пытаемся определить, что же у нас на руках, цифры
        global cards_state
        cardset_tmp = cardset[:] # копируем кардсет, упражняемся с ним, не трогаем основной
    # ----------------------------------------------------
        combo_suit = False                                                              # нет 5 карт в масти
        value_suit = 0                                                                  # нет старшей карты в последовательности
        name_suit = None                                                                # нет масти в последовательности
        combo_sequence = False                                                          # нет 5 карт в последовательности
        value_sequence = 0                                                              # нет старшей карты в последовательности
        combo_amount = 0                                                                # нет комбинаций по достоинству ( = одна карта)
        value_amount = 0                                                                # нет старшей карты по достоинству
        combo_result = 0                                                                # нет номера комбинации в итоге ( = одна карта)
        value_result = 0                                                                # нет старшей карты комбинации в итоге
        poker_hand = None                                                               # нет комбинации [№ комбинации, значение старшей карты]
        straight_flush = False                                                          # нет стрит-флеша
    # ----------------------------------------------------
        number_suit, value_suit = ds_what_suit_cards(cardset_tmp)                      # вызов функции подсчета карт по мастям
        if number_suit != None:                                                         # если определено имя масти
            combo_suit = True                                                           # 5 карт в масти есть
    # ----------------------------------------------------
        combo_sequence, value_sequence = ds_what_sequence_cards(cardset_tmp)           # вызов функций проверки последовательностей, туз = 1 / 14 (перебор внутри)

    # ----------------------------------------------------
        combo_amount, value_amount, minor_amount = ds_what_amount_cards(cardset_tmp)   # вызов функций подсчета карт по достоинству

    # ----------------------------------------------------
    # что же мы таки имеем
        if combo_suit and combo_sequence:                                               # собрали масть и 5 по порядку = стрит-флеш - а вот вам дуля - на 6/7 картах могут пересечься комбинации
            straight_flush = ds_really_straight_flush(cardset_tmp, number_suit)        # назначаем дополнительную проверку (Кардсет, № масти)
            if not straight_flush:                                                      # если нам показалось, а на самом деле нет стрит-флеша
                combo_result = 5                                                        # это простой флеш
                value_result = value_suit                                               # старшая карта - по старшей в масти
            else:                                                                       # если таки да
                value_result = value_sequence                                           # старшая карта - по старшей в последовательности
                if value_sequence == 14:                                                # если еще и туз - старший
                    combo_result = 9                                                    # Роял-флеш
                else:                                                                   # если не туз
                    combo_result = 8                                                    # стрит-флеш
        elif combo_amount > 5 and combo_result < 8:                                     # если покер (4) или фулл-хауз (3+2)  и не стрит-флеш
            value_result = value_amount                                                 # старшая карта - по старшей в комбинации
            combo_result = combo_amount                                                 # комбинация - по количеству карт
        elif combo_suit and not combo_sequence and combo_result < 6:                    # собрали масть без последовательности и нет комбинации старше
            value_result = value_suit                                                   # старшая карта - по старшей в масти
            combo_result = 5                                                            # флеш
        elif not combo_suit and combo_sequence and combo_result < 6:                    # собрали последовательность без масти и нет комбинации старше
            value_result = value_sequence                                               # старшая карта - по старшей в последовательности
            combo_result = 4                                                            # стрит
        elif combo_result < 4:                                                          # ничего старше не собрали
            value_result = value_amount                                                 # старшая карта - по старшей в комбинации
            combo_result = combo_amount                                                 # комбинация - по количеству карт

        poker_hand = [combo_result, value_result, number_suit, minor_amount]            # в руке: [комбинация, старшая карта, масть, младшая пара]
    # ----------------------------------------------------
        for i in range(0,n_cards):
            cardset[i].in_combo = False                                                 # для начала сбасываем принадлежность к комбинации
    # определяем, какие карты входят в комбинацию
        if combo_result in [9,8,5]:                                                     # если флеши
            cardset_suit = ds_mark_suit_cards(cardset,number_suit)                     # вызываем маркировку флешей, передаём карты и масть флешей
        elif combo_result == 4:                                                         # если стрит
            cardset_sequence = ds_mark_sequence_cards(cardset, value_sequence)         # вызываем маркировку стритов, передаём карты и старшую карту
        else:                                                                           # если количество карт
            cardset_amount = ds_mark_amount_cards(cardset, combo_result, value_result, minor_amount) # вызываем маркировку по количеству карт, передаём карты, комбинацию, старшинство, младшую пару
    # ----------------------------------------------------
    # обработка результата
        if cards_state == "results":
            for i in range(0,n_cards):                          # для индекса от 0 до 7 (кол-во карт в сете)
                cardset[i].interesting = False                  # карты не интересны
            for i in range(0,n_cards):                          # для индекса от 0 до 7 (кол-во карт в сете)
                if cardset[i].in_combo == True:                 # если карта в комбинации
                    cardset[i].interesting = True               # карта нам интересна
    # ----------------------------------------------------
        return poker_hand

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def ds_really_straight_flush(cardset, number_suit):                                # А не врёшь, что стрит-флеш (карсет, N масти)
        result = False                                                                  # стрит-флеша нет
        int_cardset = []                                                                # сюда отбираем карты
    # ----------------------------------------------------
        for i in range (0,len(cardset)):                                                # перебираем переданные карты
            if cardset[i].suit == number_suit:                                          # если масть очередной карты = масти комбинации
                int_cardset.append(cardset[i])                                          # добавляем эту карту в набор
    # ----------------------------------------------------
        if len(int_cardset) >= 5:                                                       # если набрали 5 карт и больше
            for k in [0,1]:                                                             # проверяем на минимум и максимум
                val_j = 0                                                               # количество очков текущей карты в переборе
                val_prev = 0                                                            # количество очков предыдущей карты в переборе
                len_seq_run = 0                                                         # количество карт в возможных последовательностях на проходах
                len_seq_max = 0                                                         # длина максимальной последовательности
                int_cardset.sort(cmp,partial(ds_card_value, k == 0)) 
                int_cardset.reverse()                                                   # и "переворачиваем" его: [0] - старшая карта
                for j in range (0,len(int_cardset)):                                    # перебираем отобранные карты
                    val_j = ds_card_value(k == 0, int_cardset[j])
                    if j == 0:                                                          # на первом проходе
                        len_seq_run = 1                                                 # длину текущей последовательности принимаем = 1, карты не сравниваем - не с чем
                    else:                                                               # на следующих проходах
                        if val_j == (val_prev-1):                                       # если очередная карта в последовательности
                            len_seq_run += 1                                            # длину текущей последовательности увеличиваем на 1
                            if len_seq_run > len_seq_max:                               # если текущая последовательность больше максимальной
                                len_seq_max = len_seq_run                               # максимальную последовательность принимаем по текущей
                        elif val_j == val_prev:                                         # если карты равны
                            pass                                                        # карту пропускаем, последовательность не сбрасываем
                        elif val_j < (val_prev-1):                                      # если очередная карта не в последовательности
                            len_seq_run = 1                                             # длину текущей последовательности принимаем = 1
                    val_prev = val_j                                                    # значение карты для сравнения принимаем: значение текущей карты
                if len_seq_max >= 5:                                                    # если набрали последовательность в 5 карт или больше на каком-то проходе
                    result = True                                                       # таки это стрит-флеш
    # ----------------------------------------------------
        return result

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def ds_name_of_poker_hands(cardset): # называем покерную комбинацию словами
        cardset_tmp = cardset[:] # копируем кардсет, упражняемся с ним, не трогаем основной
    # ----------------------------------------------------
        name_of_combo = ["старшая карта","пара","две пары","тройка","стрит","флеш","фулл-хаус","покер","стрит-флеш","роял-флеш"]    # комбинации
        name_of_card = ["","туз","двойка","тройка","четвёрка","пятёрка","шестёрка","семёрка","восьмёрка","девятка","десятка","валет","дама","король","туз"]
        name_of_cards = ["","","двойки","тройки","четвёрки","пятёрки","шестёрки","семёрки","восьмёрки","девятки","десятки","вальты","дамы","короли","тузы"]
        name_of_suit = ["Дваче","СССР","Унылок","ЮВАО"]     # масти
    # ----------------------------------------------------
        poker_hand = None                                   # пустая комбинация
        combo_name = None                                   # имени комбинации нет
        value_name = None                                   # имени старшей карты нет
        suit_name = None                                    # имени масти нет
        combo_in_hand = None                                # В руке (строка): пусто
    # ----------------------------------------------------
        poker_hand = ds_what_category(cardset_tmp)
        combo_name = name_of_combo[poker_hand[0]]           # получаем имя комбинации
        if poker_hand[0] in [0,4,5,8]:                      # если старшая карта или масти, кроме рояля, или стрит
            value_name = name_of_card[poker_hand[1]]        # получаем имя карты - единственное число
        else:                                               # если любая комбинация, кроме старшей карты
            value_name = name_of_cards[poker_hand[1]]       # получаем имя карт - множественное число
        if poker_hand[0] in [5,8,9]:                        # если собраны масти
            suit_name = name_of_suit[poker_hand[2]]         # получаем имя масти
    # ----------------------------------------------------
        if poker_hand[0] == 0:                                                                  # если старшая карта
            combo_in_hand = "%s: %s" % (combo_name, value_name)                                 # строка для старшей карты
        elif poker_hand[0] in [5,8]:                                                            # если масти, кроме рояля
            combo_in_hand = "%s %s, старшая карта: %s" % (combo_name, suit_name, value_name)    # строка для мастей
        elif poker_hand[0] == 9:                                                                # собрали роял-флеш
            combo_in_hand = "%s %s" % (combo_name, suit_name)                                   # собрали роял-флеш
        elif poker_hand[0] == 4:                                                                # собрали стрит
            combo_in_hand = "%s, старшая карта: %s" % (combo_name, value_name)                  # строка для стрита
        else:                                                                                   # если ничего особенного
            combo_in_hand = "%s, старшие карты: %s" % (combo_name, value_name)                  # строка для прочих случаев
    # ----------------------------------------------------
        return combo_in_hand, poker_hand

# =========================================================================================================================
# Сравнение сетов карт, победа/поражение
# а) сравниваем комбинации - победа/поражение/разница в номерах
# б) если комбинации одинаковые - сравниваем старшие карты - победа\поражение
# в) если комбинации и старшие карты одинаковы - сравниваем младшую пару - победа/поражение
# г) если все одинаково - ничья

    def ds_count_score():
        poker_hand_my = ds_what_category(cards_my)                         # посмотрели, что у нас на руках
        poker_hand_rival = ds_what_category(cards_rival)                   # посмотрели, что на руках у соперника

        if poker_hand_my[0] > poker_hand_rival[0]:                          # если моя комбинация старше
            return 'win'                                                    # я выиграл
        elif poker_hand_my[0] < poker_hand_rival[0]:                        # если моя комбинация младше
            return 'fail'                                                   # соперник выиграл
        else:                                                               # комбинации равны
            if poker_hand_my[1] > poker_hand_rival[1]:                      # если моя старшая карта больше
                return 'win'                                                # я выиграл
            elif poker_hand_my[1] < poker_hand_rival[1]:                    # если моя старшая карта меньше
                return 'fail'                                               # соперник выиграл
            else:                                                           # и старшие карты равны
                if poker_hand_my[3] > poker_hand_rival[3]:                  # если моя младшая пара больше
                    return 'win'                                            # я выиграл
                elif poker_hand_my[3] < poker_hand_rival[3]:                # если моя младшая пара меньше
                    return 'fail'                                           # соперник выиграл
                else:                                                       # если и это одинаково
                    return 'draw'                                           # похоже, ничья

# =========================================================================================================================

init 3 python:                              # начинаем на шаг позже оригинала
# ==============================================================================================================================================
    def ds_generate_cards(bg,dialogs): # генерация карт, вызываем из кода, передавая основу и диалоги
        global cards_bg                 # подложка, далее присваиваем bg, переданное из кода
        global game_interuptions        # прерываение игры - далее присваиваем диалоги
        global cards_my                 # сет моих карт
        global cards_rival              # сет карт соперника
        global cycles_left              # осталось циклов
        global changes_left             # осталось обменов
        global cards_state              # стадия игры
        global result_status            #

        cards_bg = bg                   # берем подоснову, переданную из кода
        game_interuptions = dialogs     # присваиваем переданные диалоги
        cycles_left  = n_cycles         # оставщиеся циклы принимаем = 3 (в ините)
        changes_left = n_xchanges       # оставщиеся обмены принимаем = 2 (в ините)
        cards_state = "init"            # Стадия игры = "начало"
        result_status = "in_progress"   #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
        k = 0 # обнуляем счетчик раздачи?
        cset = [] # пустой сет карт в игре
        while k<2*n_cards: # пока: счетчик < 2 х колво_карт (7 в init'е) = k < 14 - делаем 14 карт (12 в игре)
            name = (renpy.random.randint(1,13),types[renpy.random.randint(0,3)]) # имя = рандом (1..13), рандом из типов, например, имя = '5uvao'
            if  not name in cset: # если такого имени в наборе еще нет
                cset.append(name) # добавляем в набор игровых карт такое имя
                k += 1 # увеличиваем счетчик на 1
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
        cards_rival = [] #карты соперника, по началу пусто
        for i in range(0,n_cards): # от 0 до 7 = 7 позиций, старшая не считается, формируем сет карт соперника
            rival = [] # очередная карта соперника
            rival.visible = 'INVISIBLE' # видимость карты соперника - "НЕВИДИМА" должна быть
            rival.name = cset[i] # имя карты соперника - принимаем по индексу из сета карт в игре 0…7 карта
            rival.suit = types.index(rival.name[1])     # номер масти карты - по вхождению масти в список

            rival.interesting = False # карта неинтересна
            rival.in_combo = False # карта не в комбинации

            rival.hot = False #
            rival.allow = False #
            rival.x = int((screen_width - card_width )/2.0) #
            rival.y = int((screen_height - card_height)/2.0) #
            rival.dy = 0 #
            cards_rival.append(rival) # добавляем очередную карту в сет карт соперника
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
        cards_my    = [] #мои карты, по началу пусто
        for i in range(0,n_cards): # от 0 до 7 = 7 позиций, старшая не ситается, формируем сет своих карт
            my = [] # очередная моя карта
            my.visible = 'VISIBLE' # видимость моей карты - "ВИДИМА" должна быть
            my.name = cset[n_cards+i] # имя моей карты - принимаем по индексу из сета карт в игре 7…14 карта
            my.suit = types.index(my.name[1])       # номер масти карты - по вхождению масти в список

            my.interesting = False #
            my.in_combo = False # карта не в комбинации

            my.hot = False #
            my.allow = False #
            my.x = int((screen_width - card_width )/2.0) #
            my.y = int((screen_height - card_height)/2.0) #
            my.dy = 0 #
            cards_my.append(my) # добавляем очередную карту в сет своих карт
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
        if not  CARD_GAME_WITH_EXCHANGE: # если (False) играем 6 карт, левые карты - "пустые"; если (True) - играем 7 карт
            cards_rival[0].name = name_of_none # "нулевая" карта в сете соперника - пустое изображение
            cards_my[0].name = name_of_none # "нулевая" карта в своем сете - пустое изображение

        if cards_state == "init":
            deal_cards = {"1":"sound/sfx/cardgame/new/deal_card_1.ogg","2":"sound/sfx/cardgame/new/deal_card_2.ogg","3":"sound/sfx/cardgame/new/deal_card_3.ogg","4":"sound/sfx/cardgame/new/deal_card_4.ogg" }
            from random import randint
            deal_card = deal_cards[str(randint(1,4))]
            renpy.music.play(deal_card, channel="sound")

init 10 python:
# -----------------------------------------------------------------------------------------------
# спрайты соперников
    ds_sprites_rival_recognition = {             # ['эмоция', 'аксессуар', 'одежда', положение]
        "un":   ['shy',    '',        'pioneer',  cright],
        "sl":   ['smile2', '',        'pioneer',  cright],
        "dv":   ['grin',   '',        'pioneer2', cright],
        "mi":   ['smile',  '',        'pioneer',  cright],
        "us":   ['laugh',  '',        'pioneer',  cright],
        "sh":   ['normal', '',        'pioneer',  cright],
        "mz":   ['normal', 'glasses', 'pioneer',  cright]
    }
# ------------------------------------------------
init python:
# ------------------------------------------------
    if persistent.ds_cards_won_rivals == None:             # Выигрывали ли когда-то у этого соперника
        persistent.ds_cards_won_rivals = {
            'un':   False,
            'sl':   False,
            'dv':   False,
            'mi':   False,
            'us':   False,
            'sh':   False,
            'mz':   False,
            'ya':   False
        }
# ------------------------------------------------
    ds_day2_gamblers_summary = {                           # результат турнира — кто на каком этапе как сыграл.
        'me':   [0,0,0],                                    # в списке:  0 — 1 тур, 1 — полуфинал, 2 — финал
        'un':   [0,0,0],                                    # значение:  0 — результат не определен, 2 — победа, 1 — поражение
        'sl':   [0,0,0],                                    # в итоге: результат = 10 х индекс + значение
        'dv':   [0,0,0],                                    # 0 — не участвовал, 2/1 — победа/поражение в 1 коне; 12/11 — в 1/2; 22/21 — в финале
        'mi':   [0,0,0],
        'us':   [0,0,0],
        'sh':   [0,0,0],
        'mz':   [0,0,0],
        'ya':   [0,0,0]
        }

    ds_day2_gamblers_result = {
        'me':   0,
        'un':   0,
        'sl':   0,
        'dv':   0,
        'mi':   0,
        'us':   0,
        'sh':   0,
        'mz':   0,
        'ya':   0
        }
    
    def ds_get_winner():
        for ch in ['me', 'un', 'sl', 'dv', 'mi', 'us', 'sh', 'mz', 'ya']:
            if ds_day2_gamblers_summary[ch][2] == 2:
                return ch
        return None

# ------------------------------------------------
label ds_day2_cards_tournament_vars:
# Переменные турнира — тур до двух побед
    $ ds_day2_my_win = 0                                   # Количество побед Семёна в коне
    $ ds_day2_rival_win = 0                                # Количество побед соперника в коне
    $ ds_day2_game_played_out = 0                          # сколько раз сыграли в коне
    $ ds_day2_result_current_game = 0                      # результат текущей игры
    $ ds_hint_poker_contractual = False                    # Комбинации на руках не показываются при игре
    $ ds_day2_revanche = False                             # Реванша не было
    $ ds_day2_detour_number = 0                            # Выбор соперника для финала

# Переменные турнира — рассадка и прочее
    $ wipedown2 = CropMove(1.3, "wipedown")

    $ ds_day2_result_tour = 0                                                          # Итог тура (0-начало, 2/1 — победа/поражение в 1 коне; 12/11 — в 1/2; 22/21 — в финале )
    $ ds_day2_detour_1_tour = False                                                    # Пропуск 1 тура (если скип турнира)
    $ ds_day2_detour_semifinal = False                                                 # Пропуск 1/2  (если скип турнира)
    $ ds_day2_detour_final = False                                                     # Пропуск финала  (если скип турнира)
    $ ds_day2_tournament_fast_win = False                                              # Победа в финале (если скип турнира)
    $ ds_tournament_state = None                                                       # этап турнира
    $ ds_my_rival_semifinal = None                                                     # Неуловимый второй финалист
    $ ds_mstt = 0                                                                      # глобальный счетчик турнирной таблицы
    $ ds_day2_gamblers_begin = []                                                      # Пустой список игроков при рассадке
    $ ds_winners_1_tour = []                                                           # Пустой список победителей 1 тура
    $ ds_losers_1_tour = []                                                            # Пустой список проигравших в 1 туре
    $ ds_winners_semifinal = []                                                        # Пустой список победителей полуфинала
    $ ds_losers_semifinal = []                                                         # Пустой список проигравших в полуфинале

init:
# Новые persistent'ы турнира
    if persistent.ds_cards_max_stage == None:
        $ persistent.ds_cards_max_stage = -1

# ------------------------------------------------
    # КАРТИНКИ МАСТЕЙ В ОПИСАНИЕ ПРАВИЛ ТУРНИРА
    image suit_2ch_S = im.Scale("mods/disco_sovenok/gui/cards/suit/suit_2ch.png",21,28)
    image suit_2ch_L = im.Scale("mods/disco_sovenok/gui/cards/suit/suit_2ch.png",26,35)
    image suit_ussr_S = im.Scale("mods/disco_sovenok/gui/cards/suit/suit_ussr.png",21,28)
    image suit_ussr_L = im.Scale("mods/disco_sovenok/gui/cards/suit/suit_ussr.png",26,35)
    image suit_utan_S = im.Scale("mods/disco_sovenok/gui/cards/suit/suit_utan.png",21,28)
    image suit_utan_L = im.Scale("mods/disco_sovenok/gui/cards/suit/suit_utan.png",26,35)
    image suit_uvao_S = im.Scale("mods/disco_sovenok/gui/cards/suit/suit_uvao.png",21,28)
    image suit_uvao_L = im.Scale("mods/disco_sovenok/gui/cards/suit/suit_uvao.png",26,35)

# ------------------------------------------------
    # АВАТАРКИ ПЕРСОНАЖЕЙ (ПЕРЕОПРЕДЕЛЁННЫЕ)
init python:
    ds_avpath_base = "mods/disco_sovenok/gui/cards/avatars/"

    ds_dv_avatar = ds_avpath_base+"dv.png"
    ds_un_avatar = ds_avpath_base+"un.png"
    ds_sl_avatar = ds_avpath_base+"sl.png"
    ds_us_avatar = ds_avpath_base+"us.png"
    ds_mi_avatar = ds_avpath_base+"mi.png"
    ds_sh_avatar = ds_avpath_base+"sh.png"
    ds_mt_avatar = ds_avpath_base+"mt.png"
    ds_mz_avatar = ds_avpath_base+"mz.png"
    ds_ya_avatar = ds_avpath_base+"ya.png"

# ------------------------------------------------

init 2 python:
# ===============================================================================================
#                   СЛОВАРИ, ТАУНТЫ, ПРЕДСТВАЛЕНИЯ СТОЛОВ, ДИАЛОГИ И Т. П.
# -----------------------------------------------------------------------------------------------



# ===============================================================================================
# ОСОБЫЕ РАСКЛАДЫ — ПРЕДСТАВЛЕНИЕ СТОЛА ВМЕСТО СТАНДАРТНОГО, ПРИ ДАННОМ СОЧЕТАНИИ ИГРОКОВ
# -----------------------------------------------------------------------------------------------
# Ключ: me+sh (по алфафиту); Значения: суффикс представления, падеж стола, падежи игроков
    ds_table_special_name = {
        "me+sh":    ["образовалась мужская компания:","t","i"],                                                 # Семён + Шурик, стол: ТП, игроки: ИП
        "dv+us":    ["оккупировали рыжие:","i","i"],                                                            # Алиса + Ульяна, стол: ИП, игроки: ИП
        "dv+mi":    ["заняли наши музыкантши:","i","i"]                                                          # Алиса + Мику, стол: ИП, игроки: ИП

        }

# ===============================================================================================
# ВЗАИМНЫЕ ТАУНТЫ ИГРОКОВ — ПОКАЗЫВАЮТСЯ ВМЕСТО СТАНДАРТНЫХ (ПРИОРИТЕТ 1 — ВЫСШИЙ)
# отсортировано по возможным сочетаниям ников в алфавитном порядке
# -----------------------------------------------------------------------------------------------
    ds_table_mutual_taunt = {
        "dv+me":    "Двачевская с вызовом уставилась на тебя, явно напоминая о беседе на крыльце.", # Алиса + ты
        "dv+mi":    "Мику настороженно косится на Алису, пока та с видом победителя устраивается за столом.", # Алиса + Мику
        "dv+mz":    "Алиса пытается хорохориться, а вот Женя в противовес ей совершенно спокойна.", # Алиса + Женя
        "dv+sh":    "Алиса плотоядно уставилась на Шурика, но тот, похоже, вообще не обращает на неё внимания.", # Алиса + Шурик
        "dv+sl":    "Идеальное решение. Человек, который хочет выиграть во что бы то ни стало, против человека, которому все эти глупости не нужны.", # Алиса + Славя
        "dv+un":    "Алиса подмигнула, а Лена слабо улыбается и что-то говорит рыжей.", # Алиса + Лена
        "dv+us":    "Две бестии сцепились взглядами — ни та, ни другая явно не собираются уступать!", # Алиса + Ульяна
        "dv+ya":    "Алиса всем своим видом показывает, что победит она, но Яна настроена совершенно безразлично.", # Алиса + Яна
        "me+mi":    "Кажется, Мику понятия не имеет о том, что за игра грядёт, но всеми силами старается получать удовольствие.", # Ты + Мику
        "me+mz":    "Жужелица сидит с видом величайшего одолжения. Видимо, она очень хочет, чтобы всё это завершилось побыстрее.", # Ты + Женя
        "me+sh":    "Шурик поправляет очки на переносице, складывает руки крестом на груди, и задумчиво смотрит на крышку стола. Витает в своих мыслях, не иначе.", # Ты + Шурик
        "me+sl":    "Славя тепло улыбается тебе, видимо, подбадривая, а ты только и смог, что пожать плечами да криво улыбнуться.",    # Ты + Славя
        "me+un":    "Лена садится напротив, съёживается и старается глядеть куда угодно, лишь бы не на тебя и уж тем более не в глаза.",    # Ты + Лена
        "me+us":    "Мелкая, поглядев, не смотрит ли кто, украдкой показывает тебе язык.", # Ты + Ульяна
        "me+ya":    "Яна, кажется, совершенно не обращает внимания на творящуюся вокруг суматоху." # Ты + Яна
        "mi+mz":    "Женя смотрит на свою оппонентку, сокрушенно вздыхает, и садится напротив.",    # Мику + Женя
        "mi+sh":    "Стоило Шурику сесть за стол, Мику сразу прошибает его словесной «очередью». Кибернетик невозмутимо кивает и что-то отвечает.",    # Мику + Шурик
        "mi+sl":    "Славя занимает место напротив Мику. Девочки обмениваются парой фраз и желают друг другу удачи.",    # Мику + Славя
        "mi+un":    "Мику обрадовалась, когда напротив неё села Лена. Её чувства оказываются взаимными — зеленоглазка улыбается.",    # Мику + Лена
        "mi+us":    "Девочка-ракета, увидев, что ты смотришь в их сторону, показывает тебе язык, а Мику машет рукой.",    # Мику + Ульяна
        "mi+ya":    "Мику начинает было говорить, но, заметив, что Яна совершенно отрешена, быстро умолкает." # Мику + Яна
        "mz+sh":    "И тот, и другая молчаливо взирают друг на друга поверх очков, дожидаясь начала игры.",    # Женя + Шурик
        "mz+sl":    "Интересная пара. Славя, которой все эти глупости не нужны, против Жени, которая предпочла бы занятие полезнее, чем игра в карты.",    # Женя + Славя
        "mz+un":    "Человеку, который старается избежать лишнего внимания, в оппоненты выпал человек, которому нет до тебя никакого дела.",    # Женя + Лена
        "mz+us":    "К счастью для Ульяны, взглядом испепелять нельзя. Егоза тоже не в восторге от того, что рандом послал ей в оппоненты Жужелицу.",    # Женя + Ульяна
    #   "mz+ya":    Женя + Яна - невозможная по сюжету комбинация
        "sh+sl":    "Славя приветливо улыбается Шурику, на что тот отвечает кивком.",    # Шурик + Славя
        "sh+un":    "Шурик занимает место напротив Лены и о чём-то спрашивает пионерку. Что-то про «плакаты для стенда».",    # Шурик + Лена
        "sh+us":    "Ульянка тут же шепчет что-то Шурику на ухо, ты успеваешь расслышать что-то вроде «вступлю в клуб».", # Шурик + Ульяна
        "sh+ya":    "Шурик и Яна - два, хоть и по-разному, но отрешённых от мира человека." # Шурик + Яна
        "sl+un":    "Хоть Славя и приободрила Лену, но с таким настроем она вряд ли дойдёт до финала.",    # Славя + Лена
        "sl+us":    "Ульянка плюхается на стул напротив Слави и показывает той язык. Славя, поглядев, не смотрит ли кто, украдкой показывает язык в ответ, чем тебя удивляет.",    # Славя + Ульяна
        "sl+ya":    "Славя поздоровалась с Яной, та тихо ответила. Дальше они сидят молча." # Славя + Яна
        "un+us":    "Лена сильно вздрагивает, когда к ней подскакивает мелкая, а затем заливается краской, после того как Ульянка что-то шепчет ей на ухо. Рыжая бандитка хохочет на всю столовую, но после замечания Электроника всё же садится за стол.", # Лена + Ульяна
        "un+ya":    "Лена и Яна - две тихони. Идеальное сочетание. Им явно комфортнее всего друг с другом." # Лена + Яна
        "us+ya":    "Ульяна пытается разными способами растормошить Яну: показывает ей язык, прыгает вокруг неё... Но Яне всё равно. Наконец, Славя окрикивает Ульяну, и та успокаивается." # Ульяна + Яна
        }

# -----------------------------------------------------------------------------------------------
# ТАУНТЫ ДЛЯ ИГРОКОВ В ПАРЕ С СЕМЁНОМ — (ПРИОРИТЕТ 2)
# отсортировано по условному номеру игрока
# Количество фраз для каждого соперника может быть ЛЮБЫМ (не обязательно одинаковым), выбор рандомный
# -----------------------------------------------------------------------------------------------
    ds_table_taunt_with_me = {
        "un":   [           # Лена
                    "Лена сидит напротив тебя.",
                    "С противоположной стороны стола тебе робко улыбается Лена."
                ],
        "sl":   [           # Славя
                    "Напротив тебя сидит Славя."
                ],
        "dv":   [           # Алиса
                    "Алиса, улыбаясь, сидит напротив меня.",
                    "С противоположной стороны ехидно усмехается Двачевская."
                ],
        "mi":   [           # Мику
                    "Японка лучезарно улыбается тебе по ту сторону стола.",
                    "С противоположной стороны стола располагается девочка, будто вышедшая из аниме.",
                    "Мику удобно устраивается напротив тебя."
                ],
        "us":   [           # Ульяна
                    "Ульянка корчит тебе рожи с той стороны стола.",
                    "На противоположном стуле ёрзает мелкая."
                ],
        "sh":   [           # Шурик
                    "Шурик протягивает тебе руку, ты её пожимаешь."
                ],
        "mz":   [           # Женя (картинки без очков)
                    "С противоположной стороны стола на тебя зыркает нелюдимая библиотекарша."
                ],
        "ya":   [           # Яна
                    "С той стороны стола на тебя апатичным взглядом смотрит Яна."
                ]
        }

# ===============================================================================================
# ТАУНТЫ ДЛЯ ИГРОКОВ, ЕСЛИ СИДЯТ ДРУГ С ДРУГОМ = ПО ВТОРОМУ ИГРОКУ В ПАРЕ — (ПРИОРИТЕТ 3)
# отсортировано по условному номеру игрока
# Количество фраз для каждого соперника может быть ЛЮБЫМ (не обязательно одинаковым), выбор рандомный
# ПЛОХИЕ НОВОСТИ — внутритекстовые теги работать не будут.
# -----------------------------------------------------------------------------------------------
    ds_table_taunt_gamblers = {
        "un":   [           # Лена
                    "Лена перехватывает твой взгляд и вся краснеет.",
                    "Лена притворяется, что не замечает, как ты смотришь на неё.",
                    "Тебя удивляет, что Лена согласилась участвовать в публичном мероприятии."
                ],
        "sl":   [           # Славя
                    "Славя чувствует, что ты на неё смотришь, и улыбается.",
                    "Славя ободряюще кивает тебе.",
                    "Странно видеть «правильную» девочку с картами в зубах."
                ],
        "dv":   [           # Алиса
                    "Двачевская расхохоталась, увидев, как ты притворяешься, будто не смотришь на неё.",
                    "Ты надеешься, что Алиса слетит в этом же раунде.",
                    "Ну уж Двачевская своего не упустит."
                ],
        "mi":   [           # Мику
                    "Вид у японки забавный — она изо всех сил притворяется, что знает, зачем здесь находится.",
                    "За японку переживать не приходится — она, похоже, вообще к картам равнодушна.",
                    "Японка явно чем-то взволнована. И дело совсем не в картах."
                ],
        "us":   [           # Ульяна
                    "Ульяна показывает тебе язык и отворачивается.",
                    "Ульяна занята запугиванием оппонента.",
                    "Ульяна улыбается и качает головой, готовясь к решительной победе!"
                ],
        "sh":   [           # Шурик
                    "Он подмигивает тебе и выставляет большой палец.",
                    "Прикрыв глаза, кибернетик что-то высчитывает в уме. Шансы на победу?",
                    "Парень, похоже, и в самом деле ни разу не слышал про такую игру — выглядел он растерянным."
                ],
        "mz":   [           # Женя
                    "Женя, как обычно, игнорирует.",
                    "Видно, что Женя рада бы всё бросить и пойти в библиотеку.",
                    "Вот уж кто тут явно выглядит чужеродно, так это Женя."
                ],
        "ya":   [           # Яна
                    "Яне, кажется, совершенно всё равно на карты. Ей просто сказали поиграть - она и села играть."
                ]
        }

# ===============================================================================================
#  Для каждой пары "победитель/проигравший" приоритет 1
#  отсортировано по сочетаниям ников в алфавитном порядке (победитель > проигравший)
#           МОЖНО добавить варианты — с дальнейшим рандомным выбором
#
#    Сначала идут фразы победителя
#    разделитель блоков "*"
#    ниже — фразы проигравшего
#    если сочетание "xx>yy" не найдено — обработчик эту таблицу пропустит
#    если не найден разделитель "*" или их найдено больше одного — обработчик пропустит таблицу
#    одной из частей, либо обеих частей может не быть (т.е. "*" стоит вначале или конце списка)
#    если  в одной из частей нет строк, или первая строка блока [None, None] или [None, " "] или [] —
#    обрабочик пропустит этот блок — т. е. будет считать его пустым
#
#   структура: [кто говорит (или None  — если "от автора"), что говорит]
#   если несколько строк — и выводиться будет в несколько строк
#
#
#   ПЛОХИЕ НОВОСТИ — внутритекстовые теги (например, {w}) работать не будут.
# -----------------------------------------------------------------------------------------------
    ds_table_mutual_gamblers_win_los = {
# ------------------------------------------- Алиса
        "dv>me":    [       # Алиса > Семён
                        [None, " "],
                        "*",
                        [aut, "Ты всё-таки проиграл ей... Страшно представить, что она сделает теперь с тобой."]
                    ],
        "dv>mi":    [       # Алиса > Мику
                        [None, "Двачевская вскакивает из-за стола и улюлюкает."],
                        [dv, "Оле-оле-оле! Алиса, вперёд!"],
                        [None, "Она радуется своей победе так, будто выиграла как минимум машину."],
                        "*",
                        [mi, "Ничего-ничего, Алисочка. Я тебе всё-ё-ё припомню."],
                        [None, "Мику задирает нос и отходит к зрителям."]
                    ],
        "dv>mz":    [       # Алиса > Женя
                        [emp, "Несмотря на разгромную победу, она почему-то не выглядит счастливой."],
                        [dv, "Всё, да?"],
                        [com, "Она спрашивает растерянно."],
                        "*",
                        [mz, "Аллилуйя, наконец, я могу быть свободна."],
                        [None, "Скрипит Женя и убирается прочь из столовой."]
                    ],
        "dv>sh":    [       # Алиса > Шурик
                        [None, "Победив, она встаёт из-за стола и, приложив к глазам вывернутые ладони в жесте очкарика, качает локтями."],
                        [dv, "Очкарики в пролёте! Адью."],
                        "*",
                        [sh, "Зачем только шёл…"],
                        [None, "Шурик безразлично пожимает плечами и встаёт из-за стола."]
                    ],
        "dv>sl":    [       # Алиса > Славя
                        [None, "Проиграв, Славя улыбается и кивает ей."],
                        [sl, "Всё? Я могу идти?"],
                        [None, "Алиса кивком разрешает."],
                        [emp, "Её интересует только победа."],
                        "*",
                        [dv, "А ты ничего, выскочка, играть умеешь."],
                        [sl, "Скажешь тоже."],
                    ],
        "dv>un":    [       # Алиса > Лена
                        [None, "Она снисходительно смотрит на Лену."],
                        [dv, "Будто кто-то сомневался, что будет иначе!"],
                        [None, "Перегнувшись, она щёлкает оппонентку по лбу."],
                        "*",
                        [un, "Да не особо и хотелось."],
                        [None, "Лена сделала вид, что её не волнуют результаты матча."]
                    ],
        "dv>us":    [       # Алиса > Ульяна
                        [None, "Победив свою подругу, рыжая высокомерно задрала нос:"],
                        [dv, "Слишком юн ты, падаван, попробуй в следующем году."],
                        [res, "Стоп, какие падаваны в Советском Союзе? Тут же «Звёздные войны» должны быть неизвестны!"]
                        "*",
                        [us, "Смотрите на эту старую грымзу."],
                        [emp, "Ульянку задело поражение, и она не скрывает это."]
                    ],
        "dv>ya":    [
                        [None, "Обыграв Яну, Алиса начала было торжествовать."],
                        [dv, "Вот так-то!"]
                        "*",
                        [emp, "Но явно безразличное к итогу выражение лица Яны вкус победы изрядно подпортило."]
                    ],
# ------------------------------------------- Семён
        "me>dv":    [       # Семён > Алиса
                        [sug, "Двачевская до самого конца не рассматривала тебя как серьёзного противника, и это сыграло против неё."],
                        "*",
                        [vol, "Победа над рыжей врединой пробуждает в тебе азарт."]
                    ],
        "me>mi":    [       # Семён > Мику
                        [emp, "Хотя ты не можешь принять победу над хафу как своё личное достижение. Она просто не до конца поняла правила."],
                        "*",
                        [lgc, "Если бы у Мику была возможность отыграться, тебя ждало бы поражение."]

                    ],
        "me>mz":    [       # Семён > Женя
                        [th, "Простая задача, когда твой противник заинтересован в скорейшем поражении."],
                        "*",
                        [per_eye, "Краем глаза ты замечаешь, как грустно вздыхает Электроник."],
                        [emp, "Переживает за Жужелицу? Или «из-за»?"]
                    ],
        "me>sh":    [       # Семён > Шурик

                        [None, "Шурик оказывается достойным противником."],
                        "*",
                        [None, "Тебе пришлось постараться, чтобы одолеть его."],



                    ],
        "me>sl":    [       # Семён > Славя
                        [sug, "Расслабляться сейчас рано. Основные трудности ещё впереди."],
                        "*",
                        [esp, "Нетрудно выиграть, когда твой противник живое воплощение фразы «главное — не победа, главное — участие»."],


                    ],
        "me>un":    [       # Семён > Лена
                        [emp, "Ты надеешься, что Лена не будет сильно расстраиваться."],
                        "*",
                        [esp, "Это же всего лишь игра, верно?"]

                    ],
        "me>us":    [       # Семён > Ульяна

                        [aut, "Похоже, птица удачи сегодня прочно обосновалась на твоём плече, а Ульянка познакомилась с птицей «обломинго»."],
                        "*",
                        [hfl, "Ну что, ждём ещё одну «котлету по-Ульяновски»?"],
                        [hfl, "Хотя нет, девчушка изобретательная, придумает месть пострашнее."],
                        [hfl, "Или махнёт рукой на дурака и простит."],
                        [lgc, "Как карта ляжет."],
                        [th, "Каламбур, однако."]

                    ],
        "me>ya":    [
                        [None, " "],
                        "*",
                        [ya, "Спасибо за игру..."],
                        [None, "Тихо говорит Яна и уходит, словно испаряется."]
                    ],
# ------------------------------------------- Мику
        "mi>dv":    [       # Мику > Алиса
                        [None, " "],
                        "*",
                        [None, " "]

                    ],
        "mi>me":    [       # Мику > Семён
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "mi>mz":    [       # Мику > Женя
                        [mi, " "],
                        "*",
                        [None, " "]
                    ],
        "mi>sh":    [       # Мику > Шурик
                        [mi, " "],
                        "*",
                        [None, " "]
                    ],
        "mi>sl":    [       # Мику > Славя
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "mi>un":    [       # Мику > Лена
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "mi>us":    [       # Мику > Ульяна
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "mi>ya":    [
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
# ------------------------------------------- Женя
        "mz>dv":    [       # Женя > Алиса
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "mz>me":    [       # Женя > Семён
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "mz>mi":    [       # Женя > Мику
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "mz>sh":    [       # Женя > Шурик
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "mz>sl":    [       # Женя > Славя
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "mz>un":    [       # Женя > Лена
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "mz>us":    [       # Женя > Ульяна
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
    #   "mz>ya":    - невозможный расклад
# ------------------------------------------- Шурик
        "sh>dv":    [       # Шурик > Алиса
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sh>me":    [       # Шурик > Семён
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sh>mi":    [       # Шурик > Мику
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sh>mz":    [       # Шурик > Женя
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sh>sl":    [       # Шурик > Славя
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sh>un":    [       # Шурик > Лена
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sh>us":    [       # Шурик > Ульяна
                        [None, "Шурик снисходительно смотрит на Ульяну — мол, знай наших."],
                        [sh, "Спасибо за игру."],
                        [None, "Подчёркнуто вежливо поблагодарил он."],
                        "*",
                        [us, "Бу-бу-бу, вредина, не дал ребёнку победить!"],
                        [None, "Ульяна надувается и отворачивается."]
                    ],
        "sh>ya":    [
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
# ------------------------------------------- Славя
        "sl>dv":    [       # Славя > Алиса
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sl>me":    [       # Славя > Семён
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sl>mi":    [       # Славя > Мику
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sl>mz":    [       # Славя > Женя
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sl>sh":    [       # Славя > Шурик
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sl>un":    [       # Славя > Лена
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sl>us":    [       # Славя > Ульяна
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "sl>ya":    [
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
# ------------------------------------------- Лена
        "un>dv":    [       # Лена > Алиса
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "un>me":    [       # Лена > Семён
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "un>mi":    [       # Лена > Мику
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "un>mz":    [       # Лена > Женя
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "un>sh":    [       # Лена > Шурик
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "un>sl":    [       # Лена > Славя
                        [sl, "Удачи."],
                        "*",
                        [un, "С-спасибо."],
                        [None, "Растерянно отвечает Лена."]
                    ],
        "un>us":    [       # Лена > Ульяна
                        [None, "Она сама до конца, видимо, ещё не поверила, что победила."],
                        [un, "Я что, я…"],
                        "*",
                        [us, "А-а-а, Ленка-пенка-колбаса, вредная сосиска!"],
                        [None, "Ульяна хотела было добавить ещё что-то, но подоспевшая вожатая оттаскивает её в сторону."]
                    ],
        "un>ya":    [
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
# ------------------------------------------- Ульяна
        "us>dv":    [       # Ульяна > Алиса
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "us>me":    [       # Ульяна > Семён
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "us>mi":    [       # Ульяна > Мику
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "us>mz":    [       # Ульяна > Женя
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "us>sh":    [       # Ульяна > Шурик
                        [None, "Победив, Ульяна повела себя предсказуемо."],
                        [us, "И так будет с каждым!"],
                        "*",
                        [sh, "И тебе спасибо."],
                        [None, "Поднявшись, Шурик отходит в сторону."]
                    ],
        "us>sl":    [       # Ульяна > Славя
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "us>un":    [       # Ульяна > Лена
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "us>ya":    [
                        [None, "Помня о прошлом неудачном опыте, Ульяна даже не пытается как-то задеть Яну."]
                        "*",
                        [dra, "И немудрено - скучно разыгрывать представления, когда зрителям всё равно."]
                    ],
# ------------------------------------------- Яна
        "ya>dv":    [
                        [th, "Кажется, что победит Яна, что проиграет - реакция у неё будет одинаково безразличная."],
                        "*",
                        [th, "Даже если она победила саму Алису!"]
                    ],
        "ya>me":    [
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "ya>mi":    [
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
    #   "ya>mz"     - невозможный расклад
        "ya>sh":    [
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "ya>sl":    [
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "ya>un":    [
                        [None, " "],
                        "*",
                        [None, " "]
                    ],
        "ya>us":    [
                        [None, " "],
                        "*",
                        [None, " "]
                    ]
        }

# ===============================================================================================
# ДЛЯ ИГРОКОВ — ПОБЕДИТЕЛЕЙ 1 тура
# отсортировано по условному номеру игрока
#      МОЖНО добавить варианты — с дальнейшим рандомным выбором
# структура: [кто говорит (или None  — если "от автора"), что говорит]
# если несколько строк — и выводиться будет в несколько строк
# ПЛОХИЕ НОВОСТИ — внутритекстовые теги работать не будут.
# -----------------------------------------------------------------------------------------------
    ds_table_gamblers_winner_1_tour = {
        "me":   [           # Сёма
                    [vol, "Ты направляешься к победе!"]
                ],
        "un":   [           # Лена
                    [None, "Ей пришлось потрудиться, но победа оказалась за ней."]
                ],
        "sl":   [           # Славя
                    [None, "Активистка, похоже, не поняла, что произошло, но покорно пересела за стол полуфиналистов."]
                ],
        "dv":   [           # Алиса
                    [None, "Она раскатала противника с разгромным счётом — кажется, наслаждается игрой."]
                ],
        "mi":   [           # Мику
                    [None, "Да уж, талантливый человек талантлив во всём."]
                ],
        "us":   [           # Ульяна
                    [None, "Мелкая не заморачивается над такой глупостью, как правила игры."],
                    [None, "Вместо этого она играет по своим собственным."]
                ],
        "sh":   [           # Шурик
                    [lgc, "Честно сказать, ты не удивлён. У него были все шансы."]
                ],
        "mz":   [           # Женя
                    [emp, "Она с неудовольствием скривилась — кажется, понимает, что победа значит ещё и дальнейшее участие в этой дурацкой игре."]
                ],
        "ya":   [
                    [None, "Яна покорно и молча пересаживается за стол полуфиналистов. Видно, она просто следует тому, что ей сказали."]
                ]
    }

# ===============================================================================================
# ДЛЯ ИГРОКОВ — ПОБЕДИТЕЛЕЙ ПОЛУФИНАЛА
# отсортировано по условному номеру игрока
#      МОЖНО добавить варианты — с дальнейшим рандомным выбором
# структура: [кто говорит (или None  — если "от автора"), что говорит]
# если несколько строк — и выводиться будет в несколько строк
# ПЛОХИЕ НОВОСТИ — внутритекстовые теги работать не будут.
# -----------------------------------------------------------------------------------------------
    ds_table_gamblers_winner_semifinal = {
        "me":   [           # Сёма
                    [None, "Ты проходишь в финал."]
                ],
        "un":   [           # Лена
                    [lgc, "Вот уже вторую игру подряд она сидит с потерянным видом, но ей достаются всё более сильные комбинации. Не подыгрывает ли ей крупье?"]
                ],
        "sl":   [           # Славя
                    [None, "Девушка ворчит и пожимает плечами, не особо желая продолжать игру. Кажется, она и присоединиться-то решила из одного лишь чувства товарищества."]
                ],
        "dv":   [           # Алиса
                    [None, "Рыжая идёт бульдозером, не задерживаясь ни на одном из оппонентов. Её цель - финал, и никак иначе!"]
                ],
        "mi":   [           # Мику
                    [None, "Она радуется каждой удачной карте, как маленький ребёнок."]
                ],
        "us":   [           # Ульяна
                    [None, "Мелкая сегодня в ударе."],
                    [None, "Вторая игра подряд без знания правил — практически как вождение автомобиля без рук."]
                ],
        "sh":   [           # Шурик
                    [com, "Его невозмутимости позавидовал бы сам Будда. Быть может, в этом и есть его секрет?"]
                ],
        "mz":   [           # Женя
                    [None, "Тебя откровенно забавляет то, что она-то как раз меньше всего хотела играть."],
                    [None, "А ушла так далеко."]
                ],
        "ya":   [
                    [None, "Кажется, даже если Яна победит в игре - даже малейшей улыбки на её лице ты не увидишь."]
                ]
    }

# ===============================================================================================
# ДЛЯ ИГРОКОВ — ПОБЕДИТЕЛЕЙ ФИНАЛА
# отсортировано по условному номеру игрока
#      МОЖНО добавить варианты — с дальнейшим рандомным выбором
#  (заготовка словаря, фразы можно дописать по аналогии с 1 туром и 1\2)
# структура: [кто говорит (или None  — если "от автора"), что говорит]
# если несколько строк — и выводиться будет в несколько строк
# Если [None, None] или [None, " "] — обработчик не выведет ничего
# ПЛОХИЕ НОВОСТИ — внутритекстовые теги работать не будут.
# -----------------------------------------------------------------------------------------------
    ds_table_gamblers_winner_final = {
        "me":   [           # Сёма
                    [vol, "Ты не думал, что с твоим везением дойдёшь хотя бы до полуфинала."],
                    [vol, "Потому и красивых речей и благодарностей проигравшим от тебя не будет, ты морально к этому не готовился."]
                ],
        "un":   [           # Лена
                    [None, "Пребывающая в лёгком шоке Лена вздрагивает от неожиданности, услышав своё имя."]
                ],
        "sl":   [           # Славя
                    [None, "Славя сильно смущается, оказавшись в центре внимания и оваций."]
                ],
        "dv":   [           # Алиса
                    [None, "Рыжая возвышается над остальными, забравшись на стул, и вскидывает руки вверх."],
                    [th, "Аве мне, да?"]
                ],
        "mi":   [           # Мику
                    [None, "Мику кланяется зрителям из зала и благодарит всех за поддержку."]
                ],
        "us":   [           # Ульяна
                    [emp, "Ульяна выглядит как человек, который ни на секунду не сомневался в своей победе."]
                ],
        "sh":   [           # Шурик
                    [None, "Шурик напускает на себя невозмутимый вид, достойный нашего бронзового деятеля."]
                ],
        "mz":   [           # Женя
                    [None, "Жужелица морщится, когда зал взрывается овациями и аплодисментами в её честь."]
                ],
        "ya":   [
                    [None, "В ответ на овации Яна лишь тихо благодарит и спешит ретироваться."]
                ]
    }

# ===============================================================================================
# ДЛЯ ИГРОКОВ — ПРОИГРАВШИХ в 1 туре
# отсортировано по условному номеру игрока
#             МОЖНО добавить варианты — с дальнейшим рандомным выбором
# структура: [кто говорит (или None  — если "от автора"), что говорит]
# если несколько строк — и выводиться будет в несколько строк
# ПЛОХИЕ НОВОСТИ — внутритекстовые теги работать не будут.
# -----------------------------------------------------------------------------------------------
    ds_table_gamblers_loser_1_tour = {
        "me":   [           # Сёма
                    [None, "Ты остаёшься в первом коне."],
                    [None, "Всё, что ты можешь - побыть болельщиком."]
                ],
        "un":   [           # Лена
                    [None, "Лена тихо поднимается и присоединяется к болельщикам. Вид у неё расстроенный."]
                ],
        "sl":   [           # Славя
                    [None, "Славя пожимает плечами, поднимается, и, миновав вожатую и что-то ей сказав, занимает место среди болельщиков."]
                ],
        "dv":   [           # Алиса
                    [aut, "Увидеть лицо Двачевской, терпящей поражение — бесценно!"],
                    [None, "Ты хохочешь, прикрываясь рукой, но она, похоже, услышала — обожигает тебя взглядом."]
                ],
        "mi":   [           # Мику
                    [None, "Мику поднимается, машет всем и встаёт к болельщикам."],
                    [emp, "Она чем-то очень довольна."]
                ],
        "us":   [           # Ульяна
                    [None, "Ульяна надувается, кричит что-то и пробует топать ногами, но Ольга Дмитриевна быстро успокаивает её."],
                    [None, "Понурившись, мелкая было побрела прочь из столовой, но окрик вожатой вынуждает её сменить курс на места для болельщиков."]
                ],
        "sh":   [           # Шурик
                    [None, "Шурик реагирует так, как ты и ожидал — поправляет очки, резким движением отбрасывает чёлку со лба и встаёт."],
                    [None, "Коротко наклоняет голову и занимает своё место в толпе."]
                ],
        "mz":   [           # Женя
                    [None, "С видом величайшего облегчения Женя бросает карты на стол и, встав, направляется на улицу."]
                ],
        "ya":   [
                    [None, "Яна никак не реагирует на проигрыш. Лишь встаёт и идёт к детям-болельщикам."]
                ]
    }

# ===============================================================================================
# ДЛЯ ИГРОКОВ — ПРОИГРАВШИХ в ПОЛУФИНАЛЕ
# отсортировано по условному номеру игрока
#             МОЖНО добавить варианты — с дальнейшим рандомным выбором
# структура: [кто говорит (или None  — если "от автора"), что говорит]
# если несколько строк — и выводиться будет в несколько строк
# ПЛОХИЕ НОВОСТИ — внутритекстовые теги работать не будут.
# -----------------------------------------------------------------------------------------------
    ds_table_gamblers_loser_semifinal = {
        "me":   [           # Сёма
                    [aut, "А ты продул. Что тут ещё скажешь?"]
                ],
        "un":   [           # Лена
                    [None, "Лена тихо поднимается и присоединяется к болельщикам."]
                ],
        "sl":   [           # Славя
                    [None, "Славя замученно улыбается и с огромным облегчением отодвигает карты."],
                    [sl, "Всё, наигралась на год вперёд."],
                    [None, "Она поднимается и подходит к ждущей её Ольге Дмитриевне."]
                ],
        "dv":   [           # Алиса
                    [emp, "Алиса не хочет верить в то, что проиграла."],
                    [None, "Она пытается заставить судью назначить переигровку — безрезультатно."],
                    [None, "Двачевская встаёт из-за стола."],
                    [per_hea, "Ты можешь услышать разные непечатные выражения в её исполнении."]
                ],
        "mi":   [           # Мику
                    [None, "Мику смотрит на свои карты ещё раз, видимо, пытаясь запомнить получше."],
                    [None, "А может, она так и не усвоила правил игры."],
                    [lgc, "Ты бы не удивился."]
                ],
        "us":   [           # Ульяна
                    [us, "Эй, вы все неправильно играли! Вы все жулики, жулики!"],
                    [None, "Минут десять только ушло на то, чтобы немного успокоить её и привести в чувство."],
                    [None, "В итоге мелкая топает ногой и выбегает из зала."]
                ],
        "sh":   [           # Шурик
                    [None, "Шурик кивает и поднимается из-за стола."],
                    [None, "Кажется, у него проблемы с проявлением эмоций."]
                ],
        "mz":   [           # Женя
                    [None, "Давненько ты не видел, чтобы так бурно радовались поражению."],
                    [None, "Женя улыбается, вздыхает, расправляют плечи."],
                    [mz, "Ну наконец-то!"],
                    [None, "Рявкает она и выходит вон из столовой."]
                ],
        "ya":   [
                    [None, "Кажется, Яну поражение не задело никак. Она просто встаёт и идёт к детям."]
                ]
    }

# ===============================================================================================
# ДЛЯ ИГРОКОВ — ПРОИГРАВШИХ в ФИНАЛЕ
# отсортировано по условному номеру игрока
#             МОЖНО добавить варианты — с дальнейшим рандомным выбором
#  (заготовка словаря, фразы можно дописать по аналогии с 1 туром и 1\2)
# структура: [кто говорит (или None  — если "от автора"), что говорит]
# если несколько строк — и выводиться будет в несколько строк
# ПЛОХИЕ НОВОСТИ — внутритекстовые теги работать не будут.
# -----------------------------------------------------------------------------------------------
    ds_table_gamblers_loser_final = {
        "me":   [           # Сёма
                    [th, "Не зря говорят, что третье место лучше второго."],
                    [th, "Ведь третье место — все равно призовое, а вот второе могло бы быть первым, и от этого обиднее."]
                ],
        "un":   [           # Лена
                    [None, "Лена тихонько отходит в сторону, оставляя победителя греться в лучах славы."]
                ],
        "sl":   [           # Славя
                    [None, "Болельщиков у активистки оказывается даже больше, чем у победителя. В основном это ребятишки из младших отрядов."]
                ],
        "dv":   [           # Алиса
                    [None, "Алиса недовольно цокает, но тем и ограничивается."]
                ],
        "mi":   [           # Мику
                    [None, "Лена подходит к Мику, желая утешить, но та улыбается, как ни в чём не бывало, говорит, что всё хорошо, что она нисколько не переживает, и…"],
                    [th, "Бррр!"],
                    [rhe, "Тараторишь прям как Мику."]
                ],
        "us":   [           # Ульяна
                    [None, "Ульяна категорически не согласна и требует от Электроника переигровки."],
                    [None, "Причём так активно, что для усмирения приходится подключиться вожатой."]
                ],
        "sh":   [           # Шурик
                    [None, "Шурик воспринимает поражение спокойно, как досадное, но малозначительное обстоятельство."]
                ],
        "mz":   [           # Женя
                    [emp, "Библиотекарша выглядит как человек, чьи страдания наконец окончены."],
                    [mz, "Теперь то можно я пойду?"],
                    [mt, "Нет."]
                ],
        "ya":   [
                    [None, "Яна молча встаёт и идёт к детям, пытающимся её приободрить."]
                ]
    }

# ===============================================================================================
# словарь склонений номеров столов, стола № 0 — нет, тут склоняем "стол"
# верхний полуфинал = 5, нижний полуфинал = 6, финал = 7
# ПОКА ВЫЗЫВАЮТСЯ НЕ ВСЕ — ЭТО ЦИФРЫ
    ds_table_name_cases = {                                                                                    # словарь склонений столов
        "i": ["стол","Первый","Второй","Третий","Последний","Первый полуфинальный","Второй полуфинальный","финал"],                     # именительный падеж
        "r": ["стола","Первого","Второго","Третьего","Последнего","Первого полуфинального","Второго полуфинального","финал"],               # родительный падеж
        "d": ["столу","Первому","Второму","Третьему","Последнему","Первому полуфинальному","Второму полуфинальному","финал"],               # дательный падеж
        "v": ["стол","Первый","Второй","Третий","Последний","Первый полуфинальный","Второй полуфинальный","финал"],               # винительный падеж
        "t": ["столом","За первым","За вторым","За третьим","За последним","За первым полуфинальным","За вторым полуфинальным","финал"],      # творительный падеж
        "p": ["столе","Первом","Втором","Третьем","Последнем","Первом полуфинальном","Втором полуфинальном","финал"]                    # предложный падеж
    }

# ===============================================================================================
# словарь суффиксов принадлежности столов
# ДОЛЖНО БЫТЬ НЕ МЕНЕЕ 4-х значений (максимум 4 стола в проходе, вызванный вариант далее не вызывается)
    ds_table_affiliation = {
        1:  ["заняли","v","i"],                 # если "заняли" = стол: винительный падеж, игроки: именительный падеж
        2:  ["принадлежал","i","d"],            # если "принадлежал" = стол: именительный падеж, игроки: дательный падеж
        3:  ["расположились","t","i"],          # если "расположились" = стол: творительный падеж, игроки: именительный падеж
        4:  ["встречаются","t","i"],            # если "встречаются" = стол: творительный падеж, игроки: именительный падеж
        5:  ["прочно оккупировали","v","i"]     # если "оккупировали" = стол: винительный падеж, игроки: именительный падеж
    }

# ===============================================================================================
# словарь суффиксов принадлежности столов — победители
# ДОЛЖНО БЫТЬ НЕ МЕНЕЕ 4-х значений (максимум 4 стола в проходе, вызванный вариант далее не вызывается)
    ds_table_winner = {
        1:  [" победа ушла","t","d"],                                        # если "победа ушла" = стол: творительный падеж, игроки: дательный падеж
        2:  [" принёс удачу","i","d"],                                       # если "принёс удачу" = стол: именительный падеж, игроки: дательный падеж
        3:  [", кажется, всё подыгрывало","t","d"],                         # если "всё подыгрывало" = стол: творительный падеж, игроки: дательный падеж
        4:  [" удача сегодня совершенно определённо улыбалась","t","d"]      # если "удача..улыбалась" = стол: творительный падеж, игроки: дательный падеж
    }

# ==============================================================================
#                               ФУНКЦИИ РАССАДКИ
#
# ==============================================================================

init 3 python:
# ----------------------------------------------------------------------------------------
# называем турнирный стол (по его номеру)
    def ds_declare_tournament_tables(table_no):
        global ds_day2_gamblers_1_tour
        global ds_day2_gamblers_semifinal
        global ds_tournament_state
        global ds_table_special_name
        global ds_table_mutual_taunt
        global ds_table_taunt_with_me
        global ds_table_taunt_gamblers
        global ds_table_name_cases
        global ds_table_affiliation
        global ds_random_box_1
        gamblers_tmp = ds_day2_gamblers_1_tour[0:8]                        # копируем список картежников 1 тура (с 0 по 8), рассаженных по столам, упражняемся с копией
        if ds_tournament_state == "1_round_start":                         # если начало 1 тура
            pass
        elif ds_tournament_state == "semifinal_start":                     # если начало полуфинала
            gamblers_tmp.extend(ds_day2_gamblers_semifinal)                # добавляем в конец список картежников полуфинала
        nicks = [gamblers_tmp[2*table_no-2].take, gamblers_tmp[2*table_no-1].take]              # получаем список ников
        nicks.sort()                                                                            # сортируем его по алфавиту
        combine_nicks = "+".join(nicks)                                                         # .. и комбинируем через +
        if combine_nicks in ds_table_special_name:                                                 # если для комбинации игроков предусмотрено специальное представление стола
            table_name = ds_table_name_cases[ds_table_special_name[combine_nicks][1]][table_no]       # склоняем номер стола
            table_title = ds_table_name_cases[ds_table_special_name[combine_nicks][1]][0]             # склоняем слово "стол"
            table_suffix = ds_table_special_name[combine_nicks][0]                                 # склоняем принадлежность стола
            gamblers_case = ds_table_special_name[combine_nicks][2]                                # получаем падеж для игроков
        else:                                                                                   # специального представления стола не предусмотрено
            tab_var = renpy.random.choice(ds_random_box_1)                                 # выбираем из количества оставшихся вариантов
            ds_random_box_1.remove(tab_var)                                                    # из списка вариантов удаляем использованный вариант
            table_name = ds_table_name_cases[ds_table_affiliation[tab_var][1]][table_no]              # склоняем номер стола
            table_title = ds_table_name_cases[ds_table_affiliation[tab_var][1]][0]                    # склоняем слово "стол"
            table_suffix =  ds_table_affiliation[tab_var][0]                                       # склоняем принадлежность стола
            gamblers_case = ds_table_affiliation[tab_var][2]                                       # получаем падеж для игроков
        table = " ".join([table_name,table_title,table_suffix])                  #собираем представление стола в массив .. и комбинируем через " "
        gambler_upper = gamblers_tmp[2*table_no-2].name[gamblers_case]              # получаем имя верхнего игрока в нужном падеже
        gambler_lover = gamblers_tmp[2*table_no-1].name[gamblers_case]              # получаем имя нижнего игрока в нужном падеже
        if combine_nicks in ds_table_mutual_taunt and ds_table_mutual_taunt[combine_nicks] != " ":    # если определен парный таунт
            taunt = ds_table_mutual_taunt[combine_nicks]                                               # … его и покажем
        elif gamblers_tmp[2*table_no-2].take == 'me':                                       # если в паре первый игрок — Сёмен
            # показываем таунт второго игрока с Семеном (рандом 1/длина списка)
            taunt = ds_table_taunt_with_me[gamblers_tmp[2*table_no-1].take][renpy.random.randint(0,len(ds_table_taunt_with_me[gamblers_tmp[2*table_no-1].take])-1)]
        elif gamblers_tmp[2*table_no-1].take == 'me':                                       # если в паре второй игрок — Сёмен
            # показываем таунт первого игрока (рандом 1/длина списка)
            taunt = ds_table_taunt_with_me[gamblers_tmp[2*table_no-2].take][renpy.random.randint(0,len(ds_table_taunt_with_me[gamblers_tmp[2*table_no-2].take])-1)]
        else:                                                                                           # если нет особых условий
            # таунт второго игрока в списке (рандом 1/длина списка)
            taunt = ds_table_taunt_gamblers[gamblers_tmp[2*table_no-1].take][renpy.random.randint(0,len(ds_table_taunt_gamblers[gamblers_tmp[2*table_no-1].take])-1)]
        return table, gambler_upper, gambler_lover, taunt

# ----------------------------------------------------------------------------------------
# Проверяем, есть ли что в общем словаре
    def ds_whats_in_mutual_table_win_los(winner_take, loser_take):
        global ds_table_mutual_gamblers_win_los
        winner_sentence = loser_sentence = None                                 # считаем, для победителя и проигравшего совместных фраз нет
        combine_nicks = ">".join([winner_take, loser_take])                     # комбинируем ники через ">"
        if combine_nicks in ds_table_mutual_gamblers_win_los:                  # если есть такая комбинация  в словаре
            united_sentence = ds_table_mutual_gamblers_win_los[combine_nicks]  # загружаем список фраз по ключу
            if united_sentence.count("*") == 1:                                 # если найден только один разделитель "*"
                delimiter = united_sentence.index("*")                          # получаем позицию разделителя списка
                if delimiter != 0:                                              # если позиция разделителя не в начале списка
                    if len(united_sentence[0]) != 0:                            # если первая фраза не пустая
                        if united_sentence[0][1] not in [None, " "]:            # если собственно фраза не пустая
                            winner_sentence = united_sentence[0:delimiter]      # получаем список фраз победителя
                if delimiter !=  united_sentence[-1]:                           # если позиция разделителя не в конце списка
                    if len(united_sentence[delimiter+1]) != 0:                  # если первая фраза после разделителя не пустая
                        if united_sentence[delimiter+1][1] not in [None, " "]:  # если собственно фраза не пустая
                            loser_sentence = united_sentence[delimiter+1:len(united_sentence)]      # получаем список фраз проигравшего
        return winner_sentence, loser_sentence

# ----------------------------------------------------------------------------------------
# подводим итоги стола (по его номеру, список игроков)
    def ds_declare_results_tables(table_no, gamblers):
        global ds_table_name_cases
        global ds_table_gamblers_winner_1_tour
        global ds_table_gamblers_loser_1_tour
        global ds_table_gamblers_winner_semifinal
        global ds_table_gamblers_loser_semifinal
        global ds_table_winner
        global ds_random_box_1
        tab_var = renpy.random.choice(ds_random_box_1)                                     # выбираем из количества оставшихся вариантов
        ds_random_box_1.remove(tab_var)                                                    # из списка вариантов удаляем использованный вариант
        table_name = ds_table_name_cases[ds_table_winner[tab_var][1]][table_no]                     # склоняем номер стола
        table_title = ds_table_name_cases[ds_table_winner[tab_var][1]][0]                    # склоняем слово "стол"
        table_suffix =  ds_table_winner[tab_var][0]                                       # склоняем принадлежность стола
        winner_case = ds_table_winner[tab_var][2]                                       # получаем падеж для победителя
        table = " ".join([table_name,table_title])                                       # собираем представление стола в массив .. и комбинируем через " "
        table = table + table_suffix
        if table_no <= 4:                                                       # если № стола 1..4
            m = table_no                                                        # указатель — по номеру стола
        else:
            m = table_no - 4                                                    # указатель = номер стола — 4
        gambler_winner = gamblers[2*m-2].name[winner_case]                      # получаем имя победителя в нужном падеже
        winner_take = gamblers[2*m-2].take                                      # получаем ник победителя
        loser_take = gamblers[2*m-1].take                                       # получаем ник проигравшего
        winner_sentence, loser_sentence = ds_whats_in_mutual_table_win_los(winner_take, loser_take) # проверяем. есть ли что в общем словаре, если есть — вытаскиваем фразы оттуда
        if winner_sentence != None:                                             # если разыскали что-то в общем словаре для победителя
            winner_remark = winner_sentence[:]                                  # фразы победителей берём из общего словаря
        else:
            if table_no <= 4:                                                   # если № стола 1..4
                w = ds_table_gamblers_winner_1_tour                            # фразы победителей — по словарю 1 тура
            else:
                w = ds_table_gamblers_winner_semifinal                         # фразы победителей — по словарю полуфинала
            j = len(w[winner_take])                                             # получаем количество фраз
            winner_remark = []                                                  # ремарка победителя
            for i in range (0,j):                                               # читаем строки из словаря победителей
                winner_remark.append(w[winner_take][i])                         # добавляем в список очередную фразу
        if loser_sentence != None:                                              # если в совместном блоке для проигравшего что-то есть
            loser_remark = loser_sentence[:]                                    # фразы проигравших берём из общего словаря
        else:
            if table_no <= 4:                                                   # если № стола 1..4
                l = ds_table_gamblers_loser_1_tour                             # фразы проигравших — по словарю 1 тура
            else:                                                               # если № стола 5 и выше
                l = ds_table_gamblers_loser_semifinal                          # фразы проигравших — по словарю полуфинала
            j = len(l[loser_take])                                              # получаем количество фраз
            loser_remark = []                                                   # ремарка проигравшего
            for i in range (0,j):                                               # читаем строки из словаря проигравших
                loser_remark.append(l[loser_take][i])                           # добавляем в список очередную фразу
        return table, gambler_winner, winner_remark, loser_remark

# ----------------------------------------------------------------------------------------
# подводим итоги финала (победитель, проигравший)
    def ds_declare_results_final(winner_take, loser_take):
        global ds_table_gamblers_winner_final
        global ds_table_gamblers_loser_final
        winner_sentence, loser_sentence = ds_whats_in_mutual_table_win_los(winner_take, loser_take) # проверяем. есть ли что в общем словаре, если есть — вытаскиваем фразы оттуда
        if winner_sentence != None:                                             # если разыскали что-то в общем словаре для победителя
            winner_remark = winner_sentence[:]                                  # фразы победителей берём из общего словаря
        else:
            w = ds_table_gamblers_winner_final                             # фразы победителей — по словарю финала
            j = len(w[winner_take])                                                 # получаем количество фраз
            winner_remark = []                                                      # ремарка победителя
            for i in range (0,j):                                                   # читаем строки из словаря победителей
                winner_remark.append(w[winner_take][i])                             # добавляем в список очередную фразу
        if loser_sentence != None:                                             # если разыскали что-то в общем словаре для проигравшего
            loser_remark = loser_sentence[:]                                   # фразы победителей берём из общего словаря
        else:
            l = ds_table_gamblers_loser_final                              # фразы проигравших — по словарю финала
            j = len(l[loser_take])
            loser_remark = []
            for i in range (0,j):
                loser_remark.append(l[loser_take][i])
        return winner_remark, loser_remark

# ----------------------------------------------------------------------------------------
# тащим картинку картёжника
    def ds_get_img_playon(gamblers):
        prefix  = "mods/disco_sovenok/gui/cards/table/"
        suffix = ".png"
        return prefix+gamblers+suffix

# ----------------------------------------------------------------------------------------
# создаём игроков
    def ds_set_gamblers(mz_part):
        gamblers = []                                       # Картежники: (ники) 0:Семён, 1:Лена, 2:Славя, 3:Алиса, 4:Мику, 5:Ульяна, 6:Шурик, 7:Женя, 8:Яна
        nick_of_gamblers = [me,un,sl,dv,mi,us,sh,mz,ya]                                                            # ХАРАКТЕРЫ
        take_of_gamblers = ['me','un','sl','dv','mi','us','sh','mz','ya']                                            # ники (текст)
    # Склоняем картежников (имена):
        #name_me = [u'я',u'меня',u'мне',u'меня',u'мной',u'мне']                                                  # имена Семёна (именительный..предложный)
        name_me = [u'ты','тебя','тебе','тебя','тобой','тебе']
        name_un = [u'Лена',u'Лены',u'Лене',u'Лену',u'Леной',u'Лене']                                            # имена Лены (именительный..предложный)
        name_sl = [u'Славя',u'Слави',u'Славе',u'Славю',u'Славей',u'Славе']                                      # имена Слави (именительный..предложный)
        name_dv = [u'Алиса',u'Алисы',u'Алисе',u'Алису',u'Алисой',u'Алисе']                                      # имена Алисы (именительный..предложный)
        name_mi = [u'Мику']*6                                                                                   # имя Мику - не склоняется
        name_us = [u'Ульяна',u'Ульяны',u'Ульяне',u'Ульяну',u'Ульяной',u'Ульяне']                                # имена Ульяны (именительный..предложный)
        name_sh = [u'Шурик',u'Шурика',u'Шурику',u'Шурика',u'Шуриком',u'Шурике']                                 # имена Шурика (именительный..предложный)
        name_mz = [u'Женя',u'Жени',u'Жене',u'Женю',u'Женей',u'Жене']                                            # имена Жени (именительный..предложный)
        name_ya = [u'Яна',u'Яны',u'Яне',u'Яну',u'Яной',u'Яне']                                                  # именя Яны (именительный..предложный)
        name_of_gamblers = [name_me,name_un,name_sl,name_dv,name_mi,name_us,name_sh,name_mz,name_ya]                    # список списков имен картежников
        cases = ['i','r','d','v','t','p']                                              # Список используемых падежей
    # Создаем картежников
        for i in range (0,9):                                                           # для 9 картежников (номер элемента списка = номер картежника)
            if (i == 7) and not mz_part:
                continue                                                                # если Женя не участвует - не добавляем её
            gambler = []                                                                # очередной картежник
            gambler.nick = nick_of_gamblers[i]                                          # ник картежника (ХАРАКТЕР)
            gambler.take = take_of_gamblers[i]                                          # ник картежника (текст)
            gambler.name = {}                                                           # имя картёжника (словарь падежей) — пустой
            for j in range (0,6):                                                       # перебираем падежи
                gambler.name[cases[j]] = name_of_gamblers[i][j]                         # имя картежника = словарь "падеж":"имя в падеже"
            gambler.face = ds_get_img_playon(gambler.take)                             # иконка игрока в турнире, путь к файлу
            gambler.image = gambler.take+"_playon"                                      # иконка игрока в турнире, псевдоним
            gambler.place = None                                                        # № места игрока
            gambler.place_xy = None                                                     # координаты места игрока [x,y]
            gambler.table = None                                                        # № стола игрока
            gambler.winner = False                                                      # Игрок победил
            gamblers.append(gambler)                                                    # добавляем очередного картёжника в список
            if (i == 7) and mz_part:
                break                                                                   # если Женя участвует - не участвует Яна
        return gamblers                                                                 # функция возвращает список картежников

# ----------------------------------------------------------------------------------------
# округляем пару чисел мест — для № стола
    def ds_round_up(x):
        y = int(round((x+1.5)/2))                                                       # 1,5 добавляем из-за особенностей округления питона
        return y

# ----------------------------------------------------------------------------------------
# рассаживаем  картёжников по столам (начальный расклад) — ВЫЗЫВАЕТСЯ ОДИН РАЗ
    def ds_gamblers_shuffler(mz_part):
        global ds_winners_1_tour
        global ds_losers_1_tour
        places_1_round = range(8)                                                       # список мест в 1 раунде — для рандома
    # первоначальная рассадка (снизу вверх) 0-3 слева, 4-7 справа
        x_gamblers_1_round = [459,1315]                                                 # координаты x начальных мест рассадки (слева, справа)
        y_gamblers_1_round = [157,312,620,775]                                          # координаты y начальных мест рассадки (сверху вниз)
        places_gamblers_1_round = []                                                    # места первоначальной рассадки
    # полуфинал места 8-9-10-11
        x_gamblers_semifinal = [648,1135]                                               # координаты x полуфинала (слева, справа)
        y_gamblers_semifinal = [235,698]                                                # координаты y полуфинала (сверху вниз)
        places_gamblers_semifinal = []                                                  # места полуфинала (0-3), добавляем 8
    # финал места 12-13
        places_gamblers_final = [[888,358],[888,573]]*2                                 # места финала, 1-3 стол — верхнее, 2-4 стол — нижнее
        for i in range (0,2):                                                           # запускаем цикл в цикле по x, y
            for j in range (0,4):
                places_gamblers_1_round.append([x_gamblers_1_round[i],y_gamblers_1_round[j]]) # очередному месту присваиваем координаты
        for i in range (0,2):                                                           # запускаем цикл в цикле по x, y
            for j in range (0,2):
                places_gamblers_semifinal.append([x_gamblers_semifinal[i],y_gamblers_semifinal[j]]) # очередному месту присваиваем координаты
        gamblers = ds_set_gamblers(mz_part)                                                   # формируем список игроков (ссылка)
        if (ds_day2_detour_number != 0):                                               # если выбрали конкретного соперника для финала
            for k in (0, ds_day2_detour_number):                                       # сначала рассаживаем Семёна и соперника для финала
                if k == 0:
                    place = 0                                                           # Семёна - за первый стол
                elif k == ds_day2_detour_number:
                    place = 7                                                           # соперника для финала - за четвёртый стол
                gamblers[k].place = place                                                   # Даём игроку место
                gamblers[k].place_xy = places_gamblers_1_round[place]                       # Даём игроку координаты места
                gamblers[k].table = ds_round_up(place)                                     # № стола = округлвверх (№ места)
                gamblers[k].place_sm_xy = places_gamblers_semifinal[gamblers[k].table-1]    # Даём игроку координаты места в полуфинале
                gamblers[k].place_f_xy = places_gamblers_final[gamblers[k].table-1]         # Даём игроку координаты места в финале
                gamblers[k].place_w_xy = [1049,458]                                         # координаты победителя турнира 1051.460
                gamblers[k].winner = False                                                  # сбрасываем флаг победителя
                places_1_round.remove(place)                                                # из списка мест удаляем присвоенное место
        k = 0                                                                           # Счетчик циклов рандома
        while k < 8:                                                                    # Пока счетчик < 8 (места с 0 по 7)
            if (k in (0, ds_day2_detour_number)) and (ds_day2_detour_number != 0):    # если игроку уже присвоено место (Семён или соперник для финала)
                k += 1                                                                  # переходим к следующему
            else:                                                                       # обычная рандомная рассадка
                place = renpy.random.choice(places_1_round)                                 # Место = случайное из списка оставшихся мест
                gamblers[k].place = place                                                   # Даём игроку место
                gamblers[k].place_xy = places_gamblers_1_round[place]                       # Даём игроку координаты места
                gamblers[k].table = ds_round_up(place)                                     # № стола = округлвверх (№ места)
                gamblers[k].place_sm_xy = places_gamblers_semifinal[gamblers[k].table-1]    # Даём игроку координаты места в полуфинале
                gamblers[k].place_f_xy = places_gamblers_final[gamblers[k].table-1]         # Даём игроку координаты места в финале
                gamblers[k].place_w_xy = [1049,458]                                         # координаты победителя турнира 1051.460
                gamblers[k].winner = False                                                  # сбрасываем флаг победителя
                places_1_round.remove(place)                                                # из списка мест удаляем присвоенное место
                k += 1                                                                      # увеличиваем счетчик на 1
        ds_winners_1_tour = []                                                             # Победители  1 тура — очищаем
        ds_losers_1_tour = []                                                              # Проигравшие в 1 туре — очищаем
        return gamblers                                                                     # функция возвращает список картежников, "рассаженных" по столам

# ----------------------------------------------------------------------------------------
# узнаём своего соперника
    def ds_get_me_rival(gamblers):
        gamblers_tmp = gamblers[:]                                                      # копируем сет игроков, упражняемся с ним, не трогаем основной
        for i in range (0,len(gamblers_tmp)):                                           # перебираем игроков
            if gamblers_tmp[i].take == 'me':                                            # если очередной игрок — Семён
                table = gamblers_tmp[i].table                                           # узнаём номер своего стола
                del gamblers_tmp[i]                                                     # удаляем себя из списка
                break                                                                   # на этом цикл заканчиваем
        for i in range (0,len(gamblers_tmp)):                                           # перебираем оставшихся
            if gamblers_tmp[i].table == table:                                          # если № стола очередного игрока совпадает с моим
                rival = gamblers_tmp[i]                                                 # он и есть мой соперник
                break                                                                   # на этом цикл заканчиваем
        return rival                                                                    # функция возвращает моего соперника

# ----------------------------------------------------------------------------------------
# узнаём второго соперника в финале
    def ds_get_me_rival_final(gamblers,gambler):
        gamblers_tmp = gamblers[:]                                                      # копируем сет игроков, упражняемся с ним, не трогаем основной
        for i in range (0,len(gamblers_tmp)):                                           # перебираем игроков
            if gamblers_tmp[i].take != gambler.take:                                    # если очередной игрок не Семён или его победитель в 1/2
                rival = gamblers_tmp[i]                                                 # он и есть второй соперник
                index = i                                                               # .. и индекс соперника в списке
        return rival, index                                                             # функция возвращает второго соперника

# ----------------------------------------------------------------------------------------
# Получаем номер места игрока для сортировки
    def ds_sort_gamblers_by_place(x):
        return x.place

# ----------------------------------------------------------------------------------------
# Упорядочиваем игроков по номерам мест
    def ds_gamblers_arrange(gamblers):
        gamblers_tmp = gamblers[:]                                                      # копируем сет игроков, упражняемся с ним, не трогаем основной
        gamblers_tmp.sort(cmp,ds_sort_gamblers_by_place)                               # сортируем список по номеру мест (от 0 до 7)
        return gamblers_tmp

# ----------------------------------------------------------------------------------------
# Узнаём своё место
    def ds_get_my_table(gamblers):
        for i in range(1,9):                                                            # перебираем столы — все (1-4 начало, 5-6 полуфинал)
            if gamblers[2*i-2].take == 'me':                                            # если в паре первый игрок — Сёмен
                table = gamblers[2*i-2].table                                           # номер стола
                places = [2*i-2, 2*i-1, table]                                          # места Семёна и соперника, № стола
                break                                                                   # на этом цикл заканчиваем
            elif gamblers[2*i-1].take == 'me':                                          # если в паре второй игрок — Сёмен
                table = gamblers[2*i-1].table                                           # номер стола
                places = [2*i-1, 2*i-2, table]                                          # места Семёна и соперника, № стола
                break                                                                   # на этом цикл заканчиваем
        return places

# ----------------------------------------------------------------------------------------
# Где там Алиса?
    def ds_get_result_dv(gamblers, count):
        me_table = dv_table_los = dv_table_win = 0                                      # столы = 0
        result = 0                                                                      # результат = 0 (мы продули ДваЧе)
        for i in range(0, count):                                                       # переберем игроков
            if gamblers[i].take == "me":                                                # если очередной игрок — Семён
                if gamblers[i].winner == False:                                         # и он — проигравший
                    break                                                               # на том анализ заканчиваем
                else:                                                                   # а вот если выиграл
                    me_table = gamblers[i].table                                        # получаем стол Семёна
                    continue                                                            # следующий игрок
            elif gamblers[i].take == "dv":                                              # если очередной игрок — Алиса
                if gamblers[i].winner == False:                                         # и она — проиграла
                    dv_table_los = gamblers[i].table                                    # получаем стол Алисы — проигравшей
                    continue                                                            # следующий игрок
                else:                                                                   # Если Алиса победила
                    dv_table_win = gamblers[i].table                                    # получаем стол Алисы — победившей
        else:                                                                           # если Семён не проиграл
            if me_table == dv_table_los:                                                # и номера столов Семёна и Алисы-проигравшей совпали
                result = 1                                                              # Дваче продула именно Семёну
            elif me_table != dv_table_los and dv_table_los != 0:                        # Если номера столов Семёна и Алисы-проигравшей НЕ совпали, и стол Алисы не 0
                result = 2                                                              # Дваче продула, но не Семёну
            if dv_table_win != 0:                                                       # Дваче кого-то таки нагнула
                if me_table == dv_table_win:                                            # Если номера столов одинаковые
                    result = 3                                                          # Сёма и Алиса встретятся за одним столом
                else:
                    result = 4                                                          # Сёма и Алиса будут за разными столами
        return result

# ----------------------------------------------------------------------------------------
# Показываем турнирную таблицу перед первым раундом (игроки)
    def ds_show_tournament_table_1_round(gamblers):
        global ds_mstt
        background = 'bg int_dining_hall_sunset'
        table = 'ds_tournament'
        if ds_mstt == 9:
            renpy.scene('underlay')
            renpy.scene('master')
            renpy.show(background,layer='underlay')                                 # показываем подоснову
            renpy.show(table,layer='underlay')                                      # показываем турнирную таблицу
            renpy.with_statement(dissolve)
            return
        elif ds_mstt < 9:
            j = ds_mstt                                                            # локальный счетчик — по глобальному
            ui.layer('underlay')
            while j < 8:                                                            # пока счетчик меньше 8
                for i in range(0,j+1):                                              # пока счетчик изображений в диапазоне 0 — очередной игрок
                    ui.image(gamblers[i].face,xpos=gamblers[i].place_xy[0],ypos=gamblers[i].place_xy[1])    # показываем очередную картинку (от 1 до всех)
                    renpy.transition(diam,layer='underlay')
                j += 1                                                               # увеличиваем счётчик
                ui.close()                                                          # закрываем слой
                ds_mstt = j                                                        # глобальный счетчик — по локальному
                if ds_mstt >= 8:                                                   # если счетчик добрался до 8 (показали всех)
                    ds_mstt = 0                                                    # обнуляем счетчик
                return                                                              # возвращаемся

# ----------------------------------------------------------------------------------------
# показываем турнирную таблицу после 1 раунда и перед полуфиналом (игроки)
    def ds_show_tournament_table_semifinal(gamblers,gamblers_2 = None):
        global ds_mstt
        global ds_table_no
        global ds_winners_1_tour
        global ds_losers_1_tour
        global ds_day2_gamblers_semifinal
        background = 'bg int_dining_hall_sunset'
        table = 'ds_tournament'
        if (ds_table_no == 0) or ((ds_table_no == 5) and (ds_mstt == 8)):
            renpy.scene('underlay')
            renpy.scene('master')
            renpy.show(background,layer='underlay')                                 # показываем подоснову
            ui.layer('underlay')                                                    # выводим монохромные картинки 1 тура
            ui.image(ImageReference(table))                                         # показываем турнирную таблицу
            for i in range(0,8):
                gray = im.MatrixColor(gamblers[i].face, im.matrix.brightness(-0.1)*im.matrix.saturation(0.05))
                alpha = im.Alpha(gray, 0.7)
                ui.imagebutton(gray, gray, clicked=None, xpos=gamblers[i].place_xy[0], ypos=gamblers[i].place_xy[1])
            if (ds_table_no == 5) and (ds_mstt == 8):
                for j in range(0,4):
                    color =  im.MatrixColor(gamblers_2[j].face,im.matrix.brightness(-0.1)*im.matrix.saturation(0.9))
                    ui.imagebutton(color, color, clicked=None, xpos=gamblers_2[j].place_sm_xy[0], ypos=gamblers_2[j].place_sm_xy[1])
                    ds_day2_gamblers_semifinal[j].winner = False
            ui.close()                                                              # закрываем слой
            if ds_table_no == 0:
                ds_winners_1_tour = []                                         # очищаем победителей 1 тура
                ds_losers_1_tour =[]                                           # очищаем проигравших 1 тура
                for i in range(0,8):
                    renpy.show(gamblers[i].image, at_list=[Transform(xpos=gamblers[i].place_xy[0],ypos=gamblers[i].place_xy[1],xanchor=0,yanchor=0)], layer='underlay')
                    if gamblers[i].winner == True:
                        ds_winners_1_tour.append(gamblers[i])
                    else:
                        ds_losers_1_tour.append(gamblers[i])
                for j in range(0,4):
                    gamblers[2*j:2*j+1] = [ds_winners_1_tour[j],ds_losers_1_tour[j]]
                ds_day2_gamblers_semifinal = ds_winners_1_tour[:]                     # полуфиналисты — копия победителей 1 тура
                temp = ds_day2_gamblers_semifinal.pop(2)                               # меняем местами 1 и 2 элементы
                ds_day2_gamblers_semifinal.insert(1,temp)                              #
                for k in range(0,4):                                                    # перебираем игроков
                    ds_day2_gamblers_semifinal[k].place = k+8                          # присваиваем новое место (с 8-го)
                    ds_day2_gamblers_semifinal[k].table = ds_round_up(k+8)            # присваиваем новый номер стола (5, 6)
                    ds_table_no = 1
            renpy.with_statement(dissolve)
            return
        elif ds_table_no < 5:
            j = ds_mstt                                                # локальный счетчик — по глобальному
            while j < 8:                                                # пока счетчик меньше 8
                if gamblers[j].winner == True:
                    x1 = gamblers[j].place_xy[0]
                    y1 = gamblers[j].place_xy[1]
                    x2 = gamblers[j].place_sm_xy[0]
                    y2 = gamblers[j].place_sm_xy[1]
                    renpy.hide(gamblers[j].image, layer='underlay')
                    renpy.show(gamblers[j].image, at_list=[Move((x1,y1), (x2,y2), 1.5)], layer='underlay')
                else:
                    renpy.transition(wipedown2, layer='underlay')
                    renpy.hide(gamblers[j].image, layer='underlay')
                j += 1                                                   # увеличиваем счётчик
                ds_mstt = j
                return
        elif (ds_table_no >= 5) and (ds_mstt < 5):
            j = ds_mstt                                                # локальный счетчик — по глобальному
            while j < 4:                                                # пока счетчик меньше 4
                renpy.show(gamblers_2[j].image, at_list=[Transform(xpos=gamblers_2[j].place_sm_xy[0],ypos=gamblers_2[j].place_sm_xy[1],xanchor=0,yanchor=0)], layer='underlay')
                renpy.transition(diam, layer='underlay')
                j += 1                                                   # увеличиваем счётчик
                ds_mstt = j
                return

# ----------------------------------------------------------------------------------------
# показываем турнирную таблицу после полуфинала (игроки)
    def ds_show_tournament_table_final(gamblers,gamblers_2 = None):
        global ds_mstt
        global ds_table_no
        global ds_day2_gamblers_1_tour
        global ds_winners_semifinal
        global ds_losers_semifinal
        global ds_day2_gamblers_final
        background = 'bg int_dining_hall_sunset'
        table = 'ds_tournament'
        if ds_table_no == 4:
            gamblers_0 = ds_day2_gamblers_1_tour[:]
            renpy.scene('underlay')
            renpy.scene('master')
            renpy.show(background,layer='underlay')                                 # показываем подоснову
            ui.layer('underlay')                                                    # выводим монохромные картинки 1 тура
            ui.image(ImageReference(table))                                         # показываем турнирную таблицу
            for i in range(0,8):                                                    # вывели первый тур
                gray = im.MatrixColor(gamblers_0[i].face, im.matrix.brightness(-0.1)*im.matrix.saturation(0.05))
                ui.imagebutton(gray, gray, clicked=None, xpos=gamblers_0[i].place_xy[0], ypos=gamblers_0[i].place_xy[1])
            for j in range(0,4):
                gray = im.MatrixColor(gamblers[j].face, im.matrix.brightness(-0.1)*im.matrix.saturation(0.05))
                ui.imagebutton(gray, gray, clicked=None, xpos=gamblers[j].place_sm_xy[0], ypos=gamblers[j].place_sm_xy[1])
            ui.close()
            ds_winners_semifinal = []
            ds_losers_semifinal =[]
            for k in range(0,4):
                renpy.show(gamblers[k].image, at_list=[Transform(xpos=gamblers[k].place_sm_xy[0],ypos=gamblers[k].place_sm_xy[1],xanchor=0,yanchor=0)], layer='underlay')
                if gamblers[k].winner == True:
                    ds_winners_semifinal.append(gamblers[k])
                else:
                    ds_losers_semifinal.append(gamblers[k])
            for f in range(0,2):
                gamblers[2*f:2*f+1] = [ds_winners_semifinal[f],ds_losers_semifinal[f]]
            ds_day2_gamblers_final = ds_winners_semifinal[:]
            ds_table_no = 5
            renpy.with_statement(dissolve)
            return
        elif ds_table_no > 4:
            j = ds_mstt                                                # локальный счетчик — по глобальному
            while j < 4:                                                # пока счетчик меньше 4
                if gamblers[j].winner == True:
                    x1 = gamblers[j].place_sm_xy[0]
                    y1 = gamblers[j].place_sm_xy[1]
                    x2 = gamblers[j].place_f_xy[0]
                    y2 = gamblers[j].place_f_xy[1]
                    renpy.hide(gamblers[j].image, layer='underlay')
                    renpy.show(gamblers[j].image, at_list=[Move((x1,y1), (x2,y2), 1.5)], layer='underlay')
                else:
                    renpy.transition(wipedown2, layer='underlay')
                    renpy.hide(gamblers[j].image, layer='underlay')
                j += 1                                                   # увеличиваем счётчик
                ds_mstt = j
                return

# ----------------------------------------------------------------------------------------
# Показываем турнирную таблицу — победа в финале (игроки)
    def ds_show_tournament_table_win(gamblers_1,gamblers_2,gamblers_3):
        global ds_mstt
        global ds_tournament_state
        background = 'bg int_dining_hall_sunset'
        table = 'ds_tournament'
        if ds_mstt == 2 and ds_tournament_state == "final_start":
            for m in range(0,2):
                gamblers_3[m].winner = False
        if ds_mstt == 2 or (ds_mstt == 3 and ds_tournament_state == "final_end"):
            renpy.scene('underlay')
            renpy.scene('master')
            renpy.show(background,layer='underlay')
            ui.layer('underlay')
            ui.image(ImageReference(table))
            for i in range(0,8):                                                                                            # вывели первый тур
                gray = im.MatrixColor(gamblers_1[i].face, im.matrix.brightness(-0.1)*im.matrix.saturation(0.05))
                ui.imagebutton(gray, gray, clicked=None, xpos=gamblers_1[i].place_xy[0], ypos=gamblers_1[i].place_xy[1])
            for j in range(0,4):                                                                                            # вывели полуфинал
                gray = im.MatrixColor(gamblers_2[j].face, im.matrix.brightness(-0.1)*im.matrix.saturation(0.05))
                ui.imagebutton(gray, gray, clicked=None, xpos=gamblers_2[j].place_sm_xy[0], ypos=gamblers_2[j].place_sm_xy[1])
            for k in range(0,2):                                                                                            # вывели финал
                gray = im.MatrixColor(gamblers_3[k].face, im.matrix.brightness(-0.1)*im.matrix.saturation(0.05))
                ui.imagebutton(gray, gray, clicked=None, xpos=gamblers_3[k].place_f_xy[0], ypos=gamblers_3[k].place_f_xy[1])
            renpy.with_statement(dissolve)
            ui.close()
            for m in range(0,2):
                renpy.show(gamblers_3[m].image, at_list=[Transform(xpos=gamblers_3[m].place_f_xy[0],ypos=gamblers_3[m].place_f_xy[1],xanchor=0,yanchor=0)], layer='underlay')
            if ds_mstt == 2:
                return
        if ds_mstt == 3:
            if gamblers_3[0].winner == False:
                temp = gamblers_3.pop(1)
                gamblers_3.insert(0,temp)
            return
        if ds_mstt < 2:
            j = ds_mstt
            if gamblers_3[j].winner == True:
                x1 = gamblers_3[j].place_f_xy[0]
                y1 = gamblers_3[j].place_f_xy[1]
                x2 = gamblers_3[j].place_w_xy[0]
                y2 = gamblers_3[j].place_w_xy[1]
                renpy.hide(gamblers_3[j].image, layer='underlay')
                renpy.show(gamblers_3[j].image, at_list=[Move((x1,y1), (x2,y2), 1.3)], layer='underlay')
            else:
                renpy.transition(wipedown2, layer='underlay')
                renpy.hide(gamblers_3[j].image, layer='underlay')
            renpy.with_statement(dissolve)
            return

# ----------------------------------------------------------------------------------------
# Рандомизатор пропуска игры (поражение в 1 туре)
    def ds_drawing_of_detour():
        global ds_day2_gamblers_1_tour
        global ds_day2_gamblers_semifinal
        global ds_day2_my_seat
        winners_1 = []
        ds_day2_my_seat = None
        ds_day2_gamblers_semifinal = []                        # очищаем полуфиналистов
        for i in range(0,8):                                    # сортируем игроков 1 тура
            if ds_day2_gamblers_1_tour[i].winner == True:
                winners_1.append(ds_day2_gamblers_1_tour[i])
            if ds_day2_gamblers_1_tour[i].take == 'me':        # смотрим, где там наш Сёма сидел
                ds_day2_my_seat = i
            ds_day2_gamblers_1_tour[i].winner = False          # сбрасываем всем флаги побед
        ds_day2_gamblers_semifinal = winners_1[:]              # копируем победителей в полуфинальный список
        temp = ds_day2_gamblers_semifinal.pop(2)               # меняем местами 2 и 3 полуфиналиста
        ds_day2_gamblers_semifinal.insert(1,temp)
        return

# ----------------------------------------------------------------------------------------
# Рандомизатор пропуска игры (поражение в 1 туре — идём через полуфинал)
    def ds_drawing_of_detour_semifinal():
        global ds_day2_gamblers_semifinal
        for j in [0,2]:                                         # сортируем игроков 1 тура
            ds_day2_gamblers_semifinal[j+renpy.random.choice([0,1])].winner = True        # два рандомных победителя (между 0 и 1, 2 и 3)
        return

# ----------------------------------------------------------------------------------------
# Рандомизатор пропуска игры (поражение в 1 туре — идём через финал)
    def ds_drawing_of_detour_final():
        global ds_day2_my_seat
        global ds_day2_gamblers_final
        global ds_rival_final
        if ds_day2_my_seat in [0,1,4,5]:                                  # если Сэмэн сидел сверху
            ds_rival_final = ds_day2_gamblers_final[0]        # то его "победитель" — первый финалист
        elif ds_day2_my_seat in [2,3,6,7]:                                # если Сэмэн сидел снизу
            ds_rival_final = ds_day2_gamblers_final[1]        # то его "победитель" — второй финалист
        return

# ----------------------------------------------------------------------------------------
# Сопоставление покерных комбинаций на руках у соперников
    def ds_comparison_poker_hands(winner_hand, loser_hand, winner, loser):
        name_of_combo = {                                           # склонения комбинаций по падежам
            0:  {                                                   # Старшая карта
                    'i':    ["старший", "старшая", "старшие карты"],
                    'r':    ["старшего", "старшей", "старших карт"],
                    'd':    ["старшему", "старшей", "старшим картам"],
                    'v':    ["старшего", "старшую", "старшие карты"],
                    't':    ["старшим", "старшей", "старшими картами"],
                    'p':    ["старшем", "старшей", "старших картах"],
                    'num':  0,                                      # число карты — единственное
                    'case': None,                                   # падеж — транзит на карту
                    'cas0': 'i',                                    # падеж для 0 — именительный
                    'pr':   None,                                   # приставки нет
                    'me':   None                                    # Сёмино местоимение — транзит на карту
                    },
            1:  {                                                   # Пара
                    'i':    ["пара", "", "пары"],
                    'r':    ["пары", "", "пар"],
                    'd':    ["паре" "", "парам"],
                    'v':    ["пару", "", "пары"],
                    't':    ["парой", "", "парами"],
                    'p':    ["паре" "", "парах"],
                    'num':  1,                                      # число карты — множественное
                    'case': 'r',                                    # падеж — родительный (пара двоек)
                    'cas0': 'r',                                    # падеж для 0 — родительный (из троек)
                    'pr':   "из ",                                  # приставка для 0
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            2:  {                                                   # Две пары (добавить куда-то "и")
                    'i':    ["две пары", "", "две пары"],
                    'r':    ["двух пар" "", "двух пар"],
                    'd':    ["двум парам", "", "двум парам"],
                    'v':    ["две пары", "", "две пары"],
                    't':    ["двумя парами", "", "двумя парами"],
                    'p':    ["двух парах" "", "двух парах"],
                    'num':  1,                                      # число карты — множественное
                    'case': 'r',                                     # падеж — родительный (пара троек и двоек)
                    'cas0': 'r',                                    # падеж для 0 — родительный (из дам и шестёрок)
                    'pr':   "из ",                                  # приставка для 0
                    'me':   2                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            3:  {                                                   # Тройка
                    'i':    ["тройка", "", "тройки"],
                    'r':    ["тройки" "", "троек"],
                    'd':    ["тройке" "", "тройкам"],
                    'v':    ["тройку" "", "тройки"],
                    't':    ["тройкой" "", "тройками"],
                    'p':    ["тройке" "", "тройках"],
                    'num':  1,                                      # число карты — множественное
                    'case': 'r',                                     # падеж — родительный (тройка дам)
                    'cas0': 'r',                                    # падеж для 0 — родительный (из девяток)
                    'pr':   "из ",                                  # приставка для 0
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            4:  {                                                   # Стрит
                    'i':    ["стрит от", "", "стриты"],
                    'r':    ["стрита от", "", "стритов"],
                    'd':    ["стриту от", "", "стритам"],
                    'v':    ["стрит от", "", "стриты"],
                    't':    ["стритом от", "", "стритами"],
                    'p':    ["стрите от", "", "стритах"],
                    'num':  0,                                      # число карты — единственное
                    'case': 'r',                                     # падеж — родительный (стрит от короля, стрит от семёрки)
                    'cas0': 'r',                                    # падеж для 0 — родительный (от семёрки)
                    'pr':   "от ",                                  # приставка для 0
                    'me':   0                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            5:  {                                                   # Флеш ("от" добавить в мастях)
                    'i':    ["флеш", "", "флеши"],
                    'r':    ["флеша", "", "флешей"],
                    'd':    ["флешу", "", "флешам"],
                    'v':    ["флеш", "", "флеши"],
                    't':    ["флешем", "", "флешами"],
                    'p':    ["флеше", "", "флешах"],
                    'num':  0,                                      # число карты — единственное
                    'case': 'r',                                     # падеж — родительный (флеш (хх) от короля, флеш (хх) от семёрки)
                    'cas0': 'r',                                    # падеж для 0 — родительный (от дамы)
                    'pr':   "от ",                                  # приставка для 0
                    'me':   0                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            6:  {                                                   # Фулл-хаус (добавить "из", "и")
                    'i':    ["фулл-хаус из трёх", "", "фулл-хаусы"],
                    'r':    ["фулл-хауса из трёх", "", "фулл-хаусов"],
                    'd':    ["фулл-хаусу из трёх", "", "фулл-хаусам"],
                    'v':    ["фулл-хаус из трёх", "", "фулл-хаусы"],
                    't':    ["фулл-хаусом из трёх", "", "фулл-хаусами"],
                    'p':    ["фулл-хаусе из трёх", "", "фулл-хаусах"],
                    'num':  1,                                      # число карты — множественное
                    'case': 'r',                                     # падеж — родительный (фулл-хаус из тройки королей и двойки шестёрок)
                    'cas0': 'r',                                    # падеж для 0 — родительный (из вальтов и пятёрок)
                    'pr':   "из ",                                  # приставка для 0
                    'me':   0                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            7:  {                                                   # Покер
                    'i':    ["покер из", "", "покеры"],
                    'r':    ["покера из", "", "покеров"],
                    'd':    ["покеру из", "", "покерам"],
                    'v':    ["покер из", "", "покеры"],
                    't':    ["покером из", "", "покерами"],
                    'p':    ["покере из", "", "покерах"],
                    'num':  1,                                      # число карты — множественное
                    'case': 'r',                                     # падеж — родительный (покер из десяток)
                    'cas0': 'r',                                    # падеж для 0 — родительный (из тузов)
                    'pr':   "из ",                                  # приставка для 0
                    'me':   0                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            8:  {                                                   # Стрит-флеш ("от" перенести в масти)
                    'i':    ["стрит-флеш", "", "стрит-флеши"],
                    'r':    ["стрит-флеша", "", "стрит-флешей"],
                    'd':    ["стрит-флешу", "", "стрит-флешам"],
                    'v':    ["стрит-флеш", "", "стрит-флеши"],
                    't':    ["стрит-флешем", "", "стрит-флешами"],
                    'p':    ["стрит-флеше", "", "стрит-флешах"],
                    'num':  0,                                      # число карты — единственное
                    'case': 'r',                                     # падеж — родительный (стрит-флеш (хх) от короля, стрит-флеш (хх) от семёрки)
                    'cas0': 'r',                                    # падеж для 0 — родительный (от дамы)
                    'pr':   "от ",                                  # приставка для 0
                    'me':   0                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            9:  {                                                   # Роял-флеш ("от" НЕ надо, от туза он); и не сравниваем по одинаковым комбинациям, ибо ничья
                    'i':    ["роял-флеш"],
                    'r':    ["роял-флеша"],
                    'd':    ["роял-флешу"],
                    'v':    ["роял-флеш"],
                    't':    ["роял-флешем"],
                    'p':    ["роял-флеше"],
                    'num':  False,                                      # число карты — НЕТ (про туза не говорим)
                    'case': False,                                       # падежа тоже нет
                    'me':   0                                       # Сёмино местоимение — [мой, моя, мои]
                    }
            }
        value_name = {                                             # склонения значений карт по падежам и количеству
            1:  {                                                  # вот тут туза на всякий случай впишем
                    'i':    ["туз", "тузы"],
                    'r':    ["туза", "тузов"],
                    'd':    ["тузу", "тузам"],
                    'v':    ["туза", "тузов"],
                    't':    ["тузом", "тузами"],
                    'p':    ["тузе", "тузах"],
                    'me':   0                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            2:  {                                                  #
                    'i':    ["двойка", "двойки"],
                    'r':    ["двойки", "двоек"],
                    'd':    ["двойке", "двойкам"],
                    'v':    ["двойку", "двойки"],
                    't':    ["двойкой", "двойками"],
                    'p':    ["двойке", "двойках"],
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            3:  {                                                  #
                    'i':    ["тройка", "тройки"],
                    'r':    ["тройки", "троек"],
                    'd':    ["тройке", "тройкам"],
                    'v':    ["тройку", "тройки"],
                    't':    ["тройкой", "тройками"],
                    'p':    ["тройке", "тройках"],
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            4:  {                                                  #
                    'i':    ["четвёрка", "четвёрки"],
                    'r':    ["четвёрки", "четвёрок"],
                    'd':    ["четвёрке", "четвёркам"],
                    'v':    ["четвёрку", "четвёрки"],
                    't':    ["четвёркой", "четвёрками"],
                    'p':    ["четвёрке", "четвёрках"],
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            5:  {                                                  #
                    'i':    ["пятёрка", "пятёрки"],
                    'r':    ["пятёрки", "пятёрок"],
                    'd':    ["пятёрке", "пятёркам"],
                    'v':    ["пятёрку", "пятёрки"],
                    't':    ["пятёркой", "пятёрками"],
                    'p':    ["пятёрке", "пятёрках"],
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            6:  {                                                  #
                    'i':    ["шестёрка", "шестёрки"],
                    'r':    ["шестёрки", "шестёрок"],
                    'd':    ["шестёрке", "шестёркам"],
                    'v':    ["шестёрку", "шестёрки"],
                    't':    ["шестёркой", "шестёрками"],
                    'p':    ["шестёрке", "шестёрках"],
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            7:  {                                                  #
                    'i':    ["семёрка", "семёрки"],
                    'r':    ["семёрки", "семёрок"],
                    'd':    ["семёрке", "семёркам"],
                    'v':    ["семёрку", "семёрки"],
                    't':    ["семёркой", "семёрками"],
                    'p':    ["семёрке", "семёрках"],
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            8:  {                                                  #
                    'i':    ["восьмёрка", "восьмёрки"],
                    'r':    ["восьмёрки", "восьмёрок"],
                    'd':    ["восьмёрке", "восьмёркам"],
                    'v':    ["восьмёрку", "восьмёрки"],
                    't':    ["восьмёркой", "восьмёрками"],
                    'p':    ["восьмёрке", "восьмёрках"],
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            9:  {                                                  #
                    'i':    ["девятка", "девятки"],
                    'r':    ["девятки", "девяток"],
                    'd':    ["девятке", "девяткам"],
                    'v':    ["девятку", "девятки"],
                    't':    ["девяткой", "девятками"],
                    'p':    ["девятке", "девятках"],
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            10: {                                                  #
                    'i':    ["десятка", "десятки"],
                    'r':    ["десятки", "десяток"],
                    'd':    ["десятке", "десяткам"],
                    'v':    ["десятку", "десятки"],
                    't':    ["десяткой", "десятками"],
                    'p':    ["десятке", "десятках"],
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            11: {                                                  # Валет
                    'i':    ["валет", "вальты"],
                    'r':    ["вальта", "вальтов"],
                    'd':    ["вальту", "вальтам"],
                    'v':    ["вальта", "вальтов"],
                    't':    ["вальтом", "вальтами"],
                    'p':    ["вальте", "вальтах"],
                    'me':   0                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            12: {                                                  # Дама
                    'i':    ["дама", "дамы"],
                    'r':    ["дамы", "дам"],
                    'd':    ["даме", "дамам"],
                    'v':    ["даму", "дам"],
                    't':    ["дамой", "дамами"],
                    'p':    ["даме", "дамах"],
                    'me':   1                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            13: {                                                  # Король
                    'i':    ["король", "короли"],
                    'r':    ["короля", "королей"],
                    'd':    ["королю", "королям"],
                    'v':    ["короля", "королей"],
                    't':    ["королём", "королями"],
                    'p':    ["короле", "королях"],
                    'me':   0                                       # Сёмино местоимение — [мой, моя, мои]
                    },
            14: {                                                  # Туз
                    'i':    ["туз", "тузы"],
                    'r':    ["туза", "тузов"],
                    'd':    ["тузу", "тузам"],
                    'v':    ["туза", "тузов"],
                    't':    ["тузом", "тузами"],
                    'p':    ["тузе", "тузах"],
                    'me':   0                                       # Сёмино местоимение — [мой, моя, мои]
                    }
            }
        name_of_suit = ["Дваче","СССР","Унылок","ЮВАО"]     # масти
        combo_difference = {                                                            # разница комбинаций
            0:  {                                                                       # комбинации одинаковы
                    'm':     "почти удалось добиться ничьей.",                          # тут первая фраза ПРОИГРАВШЕГО м
                    'f':     "почти удалось свести игру вничью.",                       # тут первая фраза ПРОИГРАВШЕГО ж
                    'p2':    ["Хотя у нас обоих на руках оказались","но у","а у"],      # 1,3,6 части фразы
                    'cc':    "i",                                                       # падеж комбинации
                    'nc':    2                                                          # индекс в списке комбинаций
                    },
            1:  {                                                                       # разница 1..3
                    'm':     "выиграл с небольшим перевесом.",                          # первая фраза ПОБЕДИТЕЛЯ м
                    'f':     "выиграла с небольшим перевесом.",                         # первая фраза ПОБЕДИТЕЛЯ ж
                    'p2':    ["Всё-таки","по отношению к","хоть ненамного, но младше."], # 1,4,7 части фразы
                    'ccL':   "i",                                                       # падеж первой комбинации
                    'ccw':   "d"                                                        # падеж второй комбинации
                    },
            2:  {                                                                       # разница 4..6
                    'm':     "победил со значительным преимуществом.",                  # первая фраза ПОБЕДИТЕЛЯ м
                    'f':     "победила с подавляющим преимуществом.",                 # первая фраза ПОБЕДИТЕЛЯ ж
                    'p2':    ["С такими картами, как","против","нужно было сдаваться сразу."], # 1,4,7 части фразы
                    'ccL':   "i",                                                       # падеж первой комбинации
                    'ccw':   "r"                                                        # падеж второй комбинации
                    },
            3:  {                                                                       # разница 7..9
                    'm':     "победил с разгромным счётом, можно сказать «всухую».",    # первая фраза ПОБЕДИТЕЛЯ м
                    'f':     "победила с разгромным счётом, можно сказать «всухую».",   # первая фраза ПОБЕДИТЕЛЯ ж
                    'p2':    ["Что ни говори, но","по сравнению с","— это меньше, чем ничего."], # 1,4,7 части фразы
                    'ccL':   "i",                                                       # падеж первой комбинации
                    'ccw':   "t"                                                        # падеж второй комбинации
                    }
            }
        rivals = {                                                                  # сопернички
            'me':   ["Мне","Я",[["мой","моя","мои"],["моему","моей","моим"],["моего","моей","моих"],["моим","моей","моими"]],"","меня","меня"],
            'un':   ["Лене","Лена","её","её","Лены","неё"],
            'sl':   ["Славе","Славя","её","её","Слави","неё"],
            'dv':   ["Алисе","Алиса","её","её","Алисы","неё"],
            'mi':   ["Мику","Мику","её","её","Мику","неё"],
            'us':   ["Ульяне","Ульяна","её","её","Ульянки","неё"],
            'sh':   ["Шурику","Шурик","его","его","Шурика","него"],
            'mz':   ["Жене","Женя","её","её","Жени","неё"]
            }
        residual = winner_hand[0]-loser_hand[0]
        if residual == 0:
            d_combo = 0
        elif residual in [1,2]:
            d_combo = 1
        elif residual in [3,4,5]:
            d_combo = 2
        else:
            d_combo = 3
        if winner in ['me','sh']:                               # Если Семён или Шурик
            g_w = 'm'
        else:
            g_w = 'f'
        if loser in ['me','sh']:                               # Если Семён или Шурик
            g_L = 'm'
        else:
            g_L = 'f'
        if d_combo == 0:                                               # Комбинации одинаковые
            pref_1 = rivals[loser][0]
            suff_1 = combo_difference[d_combo][g_L]
        else:
            pref_1 = rivals[winner][1]
            suff_1 = combo_difference[d_combo][g_w]
        phrase_1 = " ".join([pref_1,suff_1])
        if d_combo != 0:
            if loser == 'me':                                       # проблемы только с Сёмой, с остальными проще
                m_S = name_of_combo[loser_hand[0]]['me']            # местоимение Семёна(цифра) — лезем в комбинации
                if m_S == None:                                     # если в комбинациях его не нашли
                    m_S = value_name[loser_hand[1]]['me']           # смотрим в очках карт
                phr_2_2 =  rivals[loser][2][0][m_S]                 # первое местоимение
            else:                                                   # не Семён
                phr_2_2 = rivals[loser][2]                          # местоимение одно, выбирать не нужно
            if winner == 'me':                                       # проблемы только с Сёмой, с остальными проще
                m_S = name_of_combo[winner_hand[0]]['me']            # местоимение Семёна(цифра) — лезем в комбинации
                if m_S == None:                                      # если в комбинациях его не нашли
                    m_S = value_name[winner_hand[1]]['me']           # смотрим в очках карт
                phr_2_5 =  rivals[winner][2][d_combo][m_S]           # второе местоимение
            else:
                phr_2_5 = rivals[winner][3]                          # местоимение одно, выбирать не нужно
            c_c_L = combo_difference[d_combo]['ccL']                  # падеж первой комбинации  — лузера
            c_c_w = combo_difference[d_combo]['ccw']                  # падеж второй комбинации — победителя
            c_k_L = name_of_combo[loser_hand[0]]['case']            # падеж карт комбинации лузера
            c_k_w = name_of_combo[winner_hand[0]]['case']           # падеж карт комбинации победителя
            k_k_L = name_of_combo[loser_hand[0]]['num']             # число карт комбинации лузера (0 = ед. 1 = мн.)
            k_k_w = name_of_combo[winner_hand[0]]['num']            # число карт комбинации победителя (0 = ед. 1 = мн.)
            if c_k_L == None:
                c_k_L = c_c_L
            if c_k_w == None:
                c_k_w = c_c_w
            if loser_hand[0] == 0 and loser_hand[1] not in [1,11,13,14]: # если старшая карта и НЕ туз, король, валет
                k_L = 1
            else:
                k_L = 0
            if winner_hand[0] == 0 and winner_hand[1] not in [1,11,13,14]: # если старшая карта и НЕ туз, король, валет
                k_w = 1
            else:
                k_w = 0
            if loser_hand[2] == None:                               # если масти нет
                combo_L_s = None
            else:                                                   # масть есть
                combo_L_s = name_of_suit[loser_hand[2]] + " от"        # рояла не будет по определению — читаем масть и добавляем "от"
            if winner_hand[2] == None:                              # если масти нет
                combo_w_s = None
            else:                                                   # масть есть
                if winner_hand[0] == 9:                             # если роял
                    combo_w_s = name_of_suit[winner_hand[2]]           # читаем масть
                else:
                    combo_w_s = name_of_suit[winner_hand[2]] + " от"   # читаем масть и добавляем "от"
            combo_L_c = name_of_combo[loser_hand[0]][c_c_L][k_L]
            combo_w_c = name_of_combo[winner_hand[0]][c_c_w][k_w]
            combo_L_k = value_name[loser_hand[1]][c_k_L][k_k_L]
            if winner_hand[0] != 9:                                     # Если не королевский
                combo_w_k = value_name[winner_hand[1]][c_k_w][k_k_w]
            if loser_hand[0] in [2,6]:                                                # если две пары или фулл-хаус
                combo_L_k_2 = value_name[loser_hand[3]][c_k_L][k_k_L]
            else:
                combo_L_k_2 = None
            if winner_hand[0] in [2,6]:                                                # если две пары или фулл-хаус
                combo_w_k_2 = value_name[winner_hand[3]][c_k_w][k_k_w]
            else:
                combo_w_k_2 = None
            if loser_hand[0] in [5,8]:                                          # если флеши (королевской у лезера не будет всяко)
                phr_2_3 = " ".join([combo_L_c, combo_L_s, combo_L_k])
            elif loser_hand[0] == 6:                                               # если фул-хаус
                phr_2_3 = " ".join([combo_L_c, combo_L_k, "и двух", combo_L_k_2])
            elif loser_hand[0] == 2:                                               # если две пары
                phr_2_3 = " ".join([combo_L_c, combo_L_k, "и", combo_L_k_2])
            else:
                phr_2_3 = " ".join([combo_L_c, combo_L_k])
            if winner_hand[0] == 9:                                                 # на королевском — только масти без карт
                phr_2_6 = " ".join([combo_w_c, combo_w_s])
            elif winner_hand[0] in [5,8]:                                           # если флеши
                phr_2_6 = " ".join([combo_w_c, combo_w_s, combo_w_k])
            elif winner_hand[0] == 6:                                               # если фул-хаус
                phr_2_6 = " ".join([combo_w_c, combo_w_k, "и двух", combo_w_k_2])
            elif winner_hand[0] == 2:                                               # если две пары
                phr_2_6 = " ".join([combo_w_c, combo_w_k, "и", combo_w_k_2])
            else:
                phr_2_6 = " ".join([combo_w_c, combo_w_k])
            phr_2_3 += ","
            if d_combo != 3:
                phr_2_6 += ","
            phr_2_1 = combo_difference[d_combo]['p2'][0]
            phr_2_4 = combo_difference[d_combo]['p2'][1]
            phr_2_7 = combo_difference[d_combo]['p2'][2]
            phrase_2 = " ".join([phr_2_1,phr_2_2,phr_2_3,phr_2_4,phr_2_5,phr_2_6,phr_2_7])
        else:
            phr_2_4 = rivals[winner][4] + " -"                             # Для победителя — либо имя (не Семён), либо местоимение
            phr_2_7 = rivals[loser][5] + " -"                              # Для проигравшего (7 часть) только местоимения
            c_c_0 = combo_difference[d_combo]['cc']                  # падеж комбинации
            c_n_0 = combo_difference[d_combo]['nc']                  # ссылка в список
            phr_2_2 = name_of_combo[loser_hand[0]][c_c_0][c_n_0] + ","
            c_k_w = name_of_combo[winner_hand[0]]['cas0']                   # падеж карты победителя для 0
            c_k_L = name_of_combo[loser_hand[0]]['cas0']                    # падеж карты лузера для 0
            n_k_w = name_of_combo[winner_hand[0]]['num']                    # число карты победителя для 0
            n_k_L = name_of_combo[loser_hand[0]]['num']                     # число карты лузера для 0
            p_k_w = name_of_combo[winner_hand[0]]['pr']                     # приставка карты победителя для 0
            p_k_L = name_of_combo[loser_hand[0]]['pr']                      # приставка карты лузера для 0
            if p_k_w != None:                                               # если приставка есть
                card_w = p_k_w + value_name[winner_hand[1]][c_k_w][n_k_w]   # с приставкой
            else:
                card_w = value_name[winner_hand[1]][c_k_w][n_k_w]           # без приставки (старшая карта)
            if p_k_L != None:                                               # если приставка есть
                card_L = p_k_L + value_name[loser_hand[1]][c_k_L][n_k_L]    # с приставкой
            else:
                card_L = value_name[loser_hand[1]][c_k_L][n_k_L]            # без приставки (старшая карта)
            if winner_hand[0] in [2,6]:                                     # если две пары или фулл-хаус
                phr_2_5 = card_w + " и " + value_name[winner_hand[3]][c_k_w][n_k_w]
            else:
                phr_2_5 = card_w
            if loser_hand[0] in [2,6]:                                     # если две пары или фулл-хаус
                phr_2_8 = card_L + " и " + value_name[loser_hand[3]][c_k_L][n_k_L]
            else:
                phr_2_8 = card_L
            phr_2_5 += ","                                                   #карта победителя
            phr_2_8 += "."                                                   #карта проигравшего
            phr_2_1 = combo_difference[d_combo]['p2'][0]
            phr_2_3 = combo_difference[d_combo]['p2'][1]
            phr_2_6 = combo_difference[d_combo]['p2'][2]
            phrase_2 = " ".join([phr_2_1,phr_2_2,phr_2_3,phr_2_4,phr_2_5,phr_2_6,phr_2_7,phr_2_8])
        return phrase_1, phrase_2

# ----------------------------------------------------------------------------------------
# как кто играет в карты — считаем и запоминаем.
    def ds_who_how_plays_poker():
        global ds_day2_gamblers_summary
        global ds_day2_gamblers_result
        global ds_losers_1_tour
        global ds_winners_1_tour
        global ds_losers_semifinal
        global ds_winners_semifinal
        global ds_day2_gamblers_final
        for k in ds_day2_gamblers_summary.keys():
            ds_day2_gamblers_result[k] = 0
            for m in range(0,3):
                ds_day2_gamblers_summary[k][m] = 0
        for i in range(0,4):
            ds_day2_gamblers_summary[ds_losers_1_tour[i].take][0] = 1
            ds_day2_gamblers_summary[ds_winners_1_tour[i].take][0] = 2
        for j in range(0,2):
            ds_day2_gamblers_summary[ds_losers_semifinal[j].take][1] = 1
            ds_day2_gamblers_summary[ds_winners_semifinal[j].take][1] = 2
            ds_day2_gamblers_summary[ds_day2_gamblers_final[j].take][2] = 2-j
        for x in ds_day2_gamblers_summary.keys():
            for y in range(0,3):
                if ds_day2_gamblers_summary[x][y] == 0:        # не участвовали — пропускаем
                    continue
                elif ds_day2_gamblers_summary[x][y] == 1:      # проиграли — считаем и пропускаем
                    ds_day2_gamblers_result[x] = 10*y+1
                    continue
                elif ds_day2_gamblers_summary[x][y] == 2:      # выиграли — считаем
                    ds_day2_gamblers_result[x] = 10*y+2
        return

# ==============================================================================================================================================
#                                                        ИГРА В КАРТЫ. Покер. Новые соперники
# =====================================================================================================================================================
label ds_cards_gameloop:
    window hide
    python:
        renpy.block_rollback()
        renpy.scene('underlay')
        renpy.scene('master')
#------------------------------------------------------------------------------------
        if cards_state == "init":                                               # если стадия "начало"
            ds_show_cards()                                                    # показываем карты
            rival.sort_cards_on_usefulness()                                    # соперник оценивает свою комбинацию
            renpy.pause(1)
            if ds_whose_first_move == 'rival':                                 # если первым ходит соперник
                new_state = "rival_select"                                      # следующая стадия = "соперник выбирает"
            elif ds_whose_first_move == 'player':                              # если первым ходит игрок
                rival.allow_to_take()                                           # установка разрешений на выбор карт у соперника
                new_state = "me_select_1"                                       # следующая стадия = "игрок выбирает"
#------------------------------------------------------------------------------------
        if cards_state == "rival_select":                                       # если стадия "соперник выбирает"
            rival.sort_cards_on_usefulness()                                    # соперник оценивает свои карты
            ds_interuption_region()                                            # прерывание - если есть диалог => идем по метке
            my_card = rival.what_card_choose()                                  # что же мы будем тянуть у Семёна?

            rival.last_selected_card = my_card                                  # запоминаем последнюю выбранную карту (под слив)

            for i in range(0,n_cards):                                          # перебираем карты
                cards_my[i].interesting = False                                 # сброс маркировки с карт игрока
                cards_rival[i].interesting = False                              # сброс маркировки с карт соперника
            cards_my[my_card].interesting = True                                # маркируем карту игрока, выбранную соперником
            ds_show_cards()                                                    # показываем карты
            renpy.pause(1)
            if  not rival.allow_to_defend():                                    # если нет разрешения на защиту (актуально для Ульяны в классике)
                rival.player_conceal_card = True                                # Семён карту сбросил без борьбы
                new_state = "rival_get"                                         # следующая стадия = "соперник забирает карту"
            else:                                                               # если разрешение на защиту есть
                new_state = "me_defend_1"                                       # следующая стадия = "защита игрока _ 1"
#------------------------------------------------------------------------------------
        if cards_state == "me_defend_1":                                        # Семён защищается - 1
            ds_interuption_region()                                            # Обработка прерывания
            answer = ds_cards_interact()                                       # действие - интерактив.
            if  answer == "end_of_turn":                                        # если нажата кнопка "конец тура"
                rival.player_conceal_card = True                                # Семён карту сбросил без борьбы
                new_state = "rival_get"                                         # соперник получает карту
            else:
                if rival.want_to_defend():                                      # если НЕ Ульяна
                    rival.player_conceal_card = False                           # Семён карту защищал
                else:                                                           # для Ульяны
                    rival.player_conceal_card = True                            # Семён карту сбросил без борьбы
                type,index = answer
                cards_my[index].dy = -40
                prev_answer = index
                new_state = "me_defend_2"
#------------------------------------------------------------------------------------
        if cards_state == "me_defend_2":                                        # Семён защищается - 2
            #ds_interuption_region()                                            # Обработка прерывания - перенесено ниже
            answer = ds_cards_interact()                                       # действие - интерактив.
            cards_my[prev_answer].dy = 0                                        # выдвинутую карту смещаем назад
            if  answer == "end_of_turn":                                        # если нажата кнопка "конец тура"
                ds_interuption_region()                                        # Обработка прерывания
                rival.player_conceal_card = True                                # Семён карту сбросил без борьбы
                new_state = "rival_get"                                         # соперник получает карту
            else:
                if rival.want_to_defend():                                      # если НЕ Ульяна
                    rival.player_conceal_card = False                           # Семён карту защищал
                else:                                                           # для Ульяны
                    rival.player_conceal_card = True                            # Семён карту сбросил без борьбы
                type,index = answer
                if  prev_answer == index:
                    cards_my[prev_answer].dy = 0
                    new_state = "me_defend_1"
                else:
                    move_buttons(cards_my,prev_answer,cards_my,index)               # игрок тасует карты
                    rival.tracked_movement(prev_answer,index)                       # отслеживаем перемещение интересующих нас карт Сэмэна
                    changes_left -= 1
                    ds_interuption_region()                                        # Обработка прерывания
                    if  changes_left == 0:
                        new_state = "rival_get"
                    else:
                        new_state = "rival_select"
#------------------------------------------------------------------------------------
        if cards_state == "rival_get":
            if  changes_left == 0:
                my_card = rival.pick_my_card_last_think()                           # какую карту забираем у игрока
            for i in range(0,n_cards):
                cards_my[i].interesting = False
                cards_rival[i].interesting = False
            cards_my[my_card].interesting = True
            ds_show_cards()
            renpy.pause(1)
            ds_interuption_region()
            if CARD_GAME_WITH_EXCHANGE:                                             # если игра на 7 картах
                rival_card = rival.give_away_card_think()                           # какую карту отдаём игроку ?
                rival.what_card_we_gave_7(rival_card,my_card)                       # смотрим, ЧТО отдали и КУДА вставили - заносим в соответствующий список
                cards_rival[rival_card].interesting = True
                ds_show_cards()
                renpy.pause(1)
            else:
                for i in range(0,n_cards):
                    if  cards_rival[i].name == name_of_none:
                        rival_card = i
            xchange_cards()                                                         # обменялись картами
            if rival.player_conceal_card:                                           # если Семён карту сбросил
                rival.player_unnecessary_card = rival_card                          # запоминаем её - вернуть ему обратно её
            else:                                                                   # Семён защищал эту карту
                rival.player_accept_card = rival_card                               # запоминаем её - потянется ли за ней?
            if not CARD_GAME_WITH_EXCHANGE:                                         # если НЕ игра на 7 картах
                rival.what_is_pulled_out(my_card)                                   # смотрим, что же мы забрали, вносим корректировку
            ds_show_cards()                                                        # показываем стол
            rival.remember_combo()                                                  # если соперник забирает, сначала запоминает
            rival.sort_cards_on_usefulness()                                        # потом оценивает новую комбинацию
            rival.compare_combo()                                                   # … и сравнивает комбинации
            if ds_whose_first_move == 'player':                                    # минус цикл на ходе соперника, если игрок начинает
                cycles_left -= 1
            if cycles_left != 0:
                changes_left = n_xchanges
                rival.allow_to_take()
                renpy.pause(1)
                new_state = "me_select_1"
            else:
                new_state = "results"
#------------------------------------------------------------------------------------
        if cards_state == "me_select_1":
            ds_interuption_region()
            if  CARD_GAME_WITH_EXCHANGE:
                answer = ds_cards_interact()
                type,index = answer
                cards_my[index].dy = -40
                my_card = index
                rival.what_we_trying_foist_7 = index                        # номер карты, которую нам хочет всучить Семён на 7 картах
            else:
                rival.what_we_trying_foist_7 = 7                            # "обнуляем" отдаваемую карту при игре на 7-ми картах
                for i in range(0,n_cards):
                    if  cards_my[i].name == name_of_none:
                        my_card = i
            new_state = "me_select_2"
#------------------------------------------------------------------------------------
        if cards_state == "me_select_2":
            ds_interuption_region()
            answer = ds_cards_interact()
            type,index = answer
            if type == "my":
                cards_my[index].dy = 0
                new_state = "me_select_1"
            else:
                rival_card = index
                for i in range(0,n_cards):
                    cards_rival[i].interesting = False
                    cards_my[i].interesting = False
                cards_rival[index].interesting = True
                new_state = "rival_defend"
#------------------------------------------------------------------------------------
        if cards_state == "rival_defend":
            ds_show_cards()                                                    # показали карты
            renpy.pause(1)
            ds_interuption_region()                                            # обработали прерывания
            rival.to_give_just_card()                                           # подумали - а может, сразу отдать
            if  changes_left == 0:                                              # если обменов не осталось
                rival.do_we_need_this_card()                                    # смотрим, что заберут и проверяем, не пригодилась бы эта карта
                new_state = "me_get"
            else:
                if  not rival.want_to_defend():                                 # если игрок не готов к отдаче (Ульяна)
                    changes_left == 0
                    rival.player_conceal_card = True                            # Семён карту сбросил без борьбы
                    new_state = "me_get"
                else:
                    i,j = rival.what_to_xchange_think()                         # решаем, какие карты будем менять
                    changes_left -= 1                                           # уменьшаем число доступных обменов
                    move_buttons(cards_rival,i,cards_rival,j)                   # меняем свою карту
                    rival.sort_cards_on_usefulness()                            # после обмена карт - ещё раз смотрим, где нужные
                    tmp_interest = cards_rival[i].interesting
                    cards_rival[i].interesting = cards_rival[j].interesting
                    cards_rival[j].interesting = tmp_interest
                    new_state = "me_select_2"
#------------------------------------------------------------------------------------
        if cards_state == "me_get":
            ds_interuption_region()
            cards_my[my_card].dy = 0
            rival.remember_combo()                                      # когда игрок должен забрать карту, перед самым обменом карт, соперник запоминает, что было
            if CARD_GAME_WITH_EXCHANGE:                                 # ЕСЛИ играли на 7-ми картах
                rival.player_unnecessary_card = rival_card              # Эту карту нам отдал Семён - она ему, походу, не нужна
                rival.what_is_pulled_out(rival.what_we_trying_foist_7)  # контролируем стеки карт, убираем неактуальные
            rival.inserted_player_card = my_card                        # Семён нашу карту забрал в это место

            if rival.playstyle == 'gamble':                             # если рискуем
                rival.remember_cards()                                  # запоминаем недокомбинации, если были
            xchange_cards()                                             # обменялись картами
            rival.sort_cards_on_usefulness()                            # потом оцениваем новую комбинацию
            rival.compare_combo()                                       # … и сравниваем комбинации
            rival.what_at_us_took(rival_card)                           # а что он у нас забрал, собственно ?
            if ds_whose_first_move == 'rival':                         # минус цикл на своём ходе - если соперник начинает
                cycles_left -= 1
            if  cycles_left != 0:
                changes_left = n_xchanges
                new_state = "rival_select"
            else:
                new_state = "results"
#------------------------------------------------------------------------------------
        if cards_state == "results":
            ds_interuption_region()
            ds_show_cards()
            renpy.pause(2)
            ds_sort_cards_upshot()                                         # сортируем карты на итог
            if not VISIBLE:
                VISIBLE = True
            for i in range(0,n_cards):
                cards_rival[i].visible = 'VISIBLE'
                cards_my[i].visible = 'VISIBLE'
            ds_hint_poker = True
            result_status = ds_count_score()                               # вызываем подсчет очков
            answer = "ignore"
            while answer=="ignore":
                ds_show_cards()
                answer = ui.interact()
            new_state = result_status
#------------------------------------------------------------------------------------
        if cards_state in ["win","draw","fail"]:
            ds_hint_poker = False                                          # "закрываем" подсказку
            ds_interuption_region()
            renpy.error("out of end-of-card-game interruption")
        cards_state = new_state                                             # меняем стадию игры на новую
        ds_name_my_poker_hand, ds_my_poker_hand = ds_name_of_poker_hands(cards_my)
        ds_name_rival_poker_hand, ds_rival_poker_hand = ds_name_of_poker_hands(cards_rival)
#------------------------------------------------------------------------------------
    jump ds_cards_gameloop

# =====================================================================================================================================================
#                                                        ПОКАЗЫВАЕМ ТУРНИРНУЮ ТАБЛИЦУ
# =====================================================================================================================================================
label ds_show_tournament_table:                                                                                        # сюда ныряем из турнира
    if ds_tournament_state == "1_round_start":                                                                     # если начало 1-го раунда
        $ ds_show_tournament_table_1_round(ds_day2_gamblers_1_tour)                                               # вызываем турнирную таблицу — там показывается очередная фишка
    elif ds_tournament_state == "1_round_end":
        $ ds_show_tournament_table_semifinal(ds_day2_gamblers_1_tour)
    elif ds_tournament_state == "semifinal_start":
        $ ds_show_tournament_table_semifinal(ds_day2_gamblers_1_tour,ds_day2_gamblers_semifinal)
    elif ds_tournament_state == "semifinal_end":
        $ ds_show_tournament_table_final(ds_day2_gamblers_semifinal)
    elif ds_tournament_state in ["final_start","final_end"]:
        $ ds_show_tournament_table_win(ds_day2_gamblers_1_tour, ds_day2_gamblers_semifinal,ds_day2_gamblers_final)
    return

# ================================================================================================
#                                            начало турнира
# ================================================================================================
label ds_cards_tournament:
    "Настроение у всех приподнятое и праздничное."
    "Ты приглядываешься, смотря по соперникам и прикидывая шансы."

    show sh normal pioneer far at right
    show us laugh2 pioneer far at left
    with dissolve
    play sound ds_sfx_mot
    per_eye "Шурик, как и ты, не совсем понимающий, что он здесь забыл, сидит рядом с Ульяной."
    show sh serious pioneer far
    show us laugh pioneer far
    with dspr
    per_eye "Егоза нетерпеливо раскачивается на стуле и пытается вытянуть из Шурика какие-то сведения о предстоящей игре, на что тот только недовольно хмурится и делает вид, что он вообще не с ней."
    hide sh
    hide us
    with dissolve

    show sl normal pioneer far at right
    if ds_bring_mz_fail:
        show ya normal pioneer far at left
    else:
        show mz normal glasses pioneer far at left
    with dissolve
    if not ds_bring_mz_fail:
        "Следующий стол занимает та самая Женя, против неё играет Славя."
    else:
        "Следующий стол занимает Яна, заменяющая Женю, против неё играет Славя."
    play sound ds_sfx_psy
    sug "Пожелай Славе удачи."
    window hide
    menu:
        "Пожелать удачи":
            window show
            "Ты, поймав её взгляд, ободряюще улыбаешься."
            me "Удачи."
            show sl smile pioneer far with dspr
            sl "Спасибо."
            "Она улыбается в ответ."
            $ ds_lp['sl'] += 1
        "Промолчать":
            window show
    hide sl
    hide mz
    hide ya
    with dissolve

    show dv smile pioneer2 far at left
    show mi normal pioneer far at right
    with dissolve
    "Алисе в жертвы досталась Мику. "
    play sound ds_sfx_psy
    emp "Тебе на секунду становится жаль несчастную японскую девочку."
    play sound ds_sfx_psy
    aut "То, каким азартом горят глаза Алисы, говорит лишь об одном — хищница настроена на победу и ни на что иное!"
    if ds_bet_dv:
        show dv laugh pioneer2 far with dspr
        pause(0.3)
        show dv smile pioneer2 far with dspr
        "Поймав твой взгляд, Алиса подмигивает."
        aut "Она напоминает о пари."
        window hide
        menu:
            "Кивнуть в ответ":
                window show
                "Ты киваешь в ответ."
            "Проигнорировать":
                window show
                "Ты делаешь вид, будто не замечаешь её."
    else:
        show dv sad pioneer2 far with dspr
        "Встретившись со мной глазами, она почему-то вздрагивает и мгновенно отворачивается."
        hide dv with dissolve
        emp "Кажется, твой отказ задел её. Видимо, ей был {i}важен{/i} спор с тобой."
    hide dv
    hide mi
    with dissolve

    show un normal pioneer far with dissolve
    "Пустует одно место — напротив Лены."
    play sound ds_sfx_int
    lgc "Кажется, тебе предстоит играть с ней."
    "Всё остальное пространство занято болельщиками и зрителями."
    show un smile pioneer with dspr
    me "Привет ещё раз."
    "Ты опускаешься на стул напротив."
    me "Кажется, нам предстоит выступить друг против друга."
    show un shy pioneer with dissolve
    un "Да…"
    emp "От внимания зрителей она явно чувствует себя не в своей тарелке."
    window hide
    menu:
        "Поддержать":
            window show
            me "Значит, удачи нам обоим."
        "Промолчать":
            window show
    emp "Возможно, стоит сдать партию, чтобы немного приободрить эту грустную девочку."
    hide un with dissolve

    $ persistent.sprite_time = "day"
    $ day_time()
    with dissolve
# ------------------------------------------------------------- ADD загоняем БГ зала на нижний слой
    python:
        renpy.scene('underlay')
        renpy.show('bg int_dining_hall_day',layer='underlay')
        renpy.scene('master')
        renpy.transition(dissolve)
# ------------------------------------------------------------- /ADD
    show el smile pioneer at right with dissolve
    "Закончив считать карты, Электроник поворачивается в вашу сторону и с нездоровым даже для него оживлением обращается к вам."
    el "Карты у нас есть, все на местах. Начинаем турнир!"
    play sound ds_sfx_mot
    res "А какие у игры правила-то? Не в настоящий покер же вы играете."
    show el normal pioneer with dspr
    me "Погоди, торопыга."
    me "Как насчёт правил? Или мы в техасский холдем поиграть присели?"
    show el surprise pioneer with dspr
    el "Ой, правила. Точно."
    show el normal pioneer with dspr
    "Электроник берёт маркер, которым чертил схемы игры, и погружается в размышления, машинально покусывая колпачок."
    show el serious pioneer with dspr
    el "Так вот."
    "Он показывает на схему."
# ------------------------------------------------------------- ADD Показываем схему турнира на фоне зала
    python:
        renpy.show('ds_tournament',layer='underlay')
        renpy.transition(dissolve)
# ------------------------------------------------------------- /ADD
    el "Это схема турнира, и…"
    show dv angry pioneer2 at left
    show el normal pioneer at cright
    with dissolve
    dv "Да уж не тупые. Поняли, что проигравший выбывает."
    dv "О правилах игры давай."
    hide dv
    show el sad pioneer at center
    with dissolve
# ------------------------------------------------------------- ADD Убираем схему турнира
    python:
        renpy.hide('ds_tournament',layer='underlay')
        renpy.transition(dissolve)
# ------------------------------------------------------------- /ADD
    el "Ладно."
    "Смутившийся было Электроник мгновенно набирает привычный темп."
    show el smile pioneer at center with dspr
    el "Основное правило — проигравший выбывает. Поэтому никаких вторых шансов, переигровок, реваншей и прочего!"
    "Он отмахивается от тянущей руку Ульянки, и продолжает."
    el "Каждый тур состоит из одной игры, если у игроков ничья, исход решает новая партия. После этого проигравшие в туре выбывают, и начинается сле…"
    play sound ds_sfx_int
    rhe "Он снова про то, что проигравший выбывает?"
    me "Я тебя умоляю."
    me "Хватит уж о системе плей-офф! Мы все прекрасно знаем, как она работает! Давай о правилах игры!"
    el "Я уже почти перешёл к ним."
    el "Поскольку добровольцев…"
    "Он кидает взгляд в твою сторону и мгновенно поправляется."
    el "Участников будет восемь, то туров, будет, соответственно, три."
    show el laugh pioneer with dspr
    "Тут он поднимает указательный палец."
    el "Победитель последнего тура получит огромный приз!"
    play sound ds_sfx_int
    dra "Точно-точно огромный приз? Что-то сомнения грызут вас, мессир..."
    show dv angry pioneer2 at left
    show el surprise pioneer at cright
    dv "К игре!"
    window hide
    menu:
        "Присоединиться":
            window show
            me "К игре!"
            "Ты сказал это одновременно с Алисой."
        "Промолчать":
            window show
    el "Да я уже почти там. Чего вы, в самом деле!"
    play sound ds_sfx_mot
    com "Он прячет растерянность, делая вид, что прочищает горло."
    hide dv
    show el normal pioneer at center
    with dissolve
    el "Итак, все комбинации покерные, вы должны собрать у себя комбинацию сильнее, чем у противника. Двойку, тройку, четвёрку…"
    show us grin pioneer at cleft
    show el normal pioneer at cright
    with dissolve
    us "Пятёрку!"
    "Крикнула Ульяна, видимо, уставшая от того, что её игнорируют."
    el "Если кто-то не в курсе относительно ценности комбинаций."
    "Проигнорировал реплику Эл."
    hide us
    show el normal pioneer at center
    with dissolve
    el "Их можно посмотреть на таблице."
    "И он показал на другую половину бумажного листа."
# ----------------------------------------------------------------------------------- ADD Показываем правила игры
    if skillcheck('encyclopedia', lvl_up_medium, passive=True):
        play sound ds_sfx_int
        enc "Ты прекрасно знаешь комбинации и так."
        window hide
        menu:
            "Показать комбинации":
                jump ds_cards_rules
            "Не показывать комбинации":
                $ ds_hint_poker_contractual = True
                jump ds_cards_rules_known
    else:                                                       # если ещё правил не читали — читаем.
        play sound ds_sfx_int
        enc "Было бы неплохо ознакомиться над комбинациями."
        jump ds_cards_rules

label ds_cards_rules:
    $ ds_hint_poker_contractual = True
    $ set_mode_nvl()
    "{size=35}{u}Возможные комбинации карт в порядке увеличения достоинства:{/u}{/size}{nw}"
    ""

    "- {b}Старшая карта{/b} (англ. {i}high card{i}): ни одна из вышеописанных комбинаций,{nw}"
    if persistent.font_size == 'small':
        "например: {b}{color=#FF6600}Т{image=suit_2ch_S} 10{image=suit_2ch_S}{color=#009833} 9{image=suit_utan_S} 5{image=suit_uvao_S} 4{image=suit_uvao_S}{/color}{color=#FF6600} 2{image=suit_ussr_S}{/color}{/color}{/b}."
    elif persistent.font_size == 'large':
        "например: {b}{color=#FF6600}Т{image=suit_2ch_L} 10{image=suit_2ch_L}{color=#009833} 9{image=suit_utan_L} 5{image=suit_uvao_L} 4{image=suit_uvao_L}{/color}{color=#FF6600} 2{image=suit_ussr_L}{/color}{/color}{/b}."
    "Вышеприведённая комбинация называется «старший туз»."
    "Если у соперников на руках оказывается по старшей карте,{nw}"
    "победитель определяется по старшей из имеющихся на руках карт."
    "Если старшие карты у игроков равны, объявляется ничья.{nw}"
    ""

    if persistent.font_size == 'small':
        "- {b}Пара{/b}/Двойка (англ. {i}one pair{/i}): две карты одного достоинства, например: {b}{color=#FF6600}9{image=suit_ussr_S}{color=#009833} 9{image=suit_utan_S}{/color}{/b}."
    elif persistent.font_size == 'large':
        "- {b}Пара{/b}/Двойка (англ. {i}one pair{/i}): две карты одного достоинства, например: {b}{color=#FF6600}9{image=suit_ussr_L}{color=#009833} 9{image=suit_utan_L}{/color}{/b}."
    "При наличии этой комбинации у двух игроков, преимущество у того, у кого выше{nw}"
    "достоинство карт, составляющих пару. Если пары идентичны, объявляется ничья.{nw}"
    ""

    pause(1)
    nvl clear

    if persistent.font_size == 'small':
        "- {b}Две пары{/b}/Две двойки/Два плюс два (англ. {i}two pairs{/i}): две пары карт, например: {b}{color=#009833}8{image=suit_uvao_S} 8{image=suit_utan_S} {color=#FF6600}4{image=suit_ussr_S} 4{image=suit_2ch_S}{/color}{/b}."
    elif persistent.font_size == 'large':
        "- {b}Две пары{/b}/Две двойки/Два плюс два (англ. {i}two pairs{/i}): две пары карт, например: {b}{color=#009833}8{image=suit_uvao_L} 8{image=suit_utan_L} {color=#FF6600}4{image=suit_ussr_L} 4{image=suit_2ch_L}{/color}{/b}."
    "Если на руках {b}три{/b} пары, пара карт самого младшего достоинства не учитывается,{nw}"
    "{i}комбинации «Три пары» в игре нет{/i}."
    "Когда у двух игроков на руках окажутся по две пары, старшей является та,{nw}"
    "в которую входят две наиболее высокие по достоинству карты."
    "В случае, когда старшие пары карт оказываются идентичными, старшинство{nw}"
    "комбинации в целом определяется по младшей паре карт."
    "Победителем будет считаться игрок, у которого младшая пара состоит из старших карт.{nw}"
    "Если у обоих игроков комбинации по достоинству карт полностью идентичны, объявляется ничья.{nw}"
    ""

    "- {b}Тройка{/b}/Сет/Триплет/Трипс (англ. {i}three of a kind, set{/i} — «три одинаковых», «набор»):{nw}"
    if persistent.font_size == 'small':
        "три карты одного достоинства, например: {b}{color=#009833}7{image=suit_uvao_S} 7{image=suit_utan_S} {color=#FF6600}7{image=suit_2ch_S}{/color}{/b}."
    elif persistent.font_size == 'large':
        "три карты одного достоинства, например: {b}{color=#009833}7{image=suit_uvao_L} 7{image=suit_utan_L} {color=#FF6600}7{image=suit_2ch_L}{/color}{/b}."
    "Когда у двух соперников на руках одновременно окажутся тройки, победителем объявляется{nw}"
    "тот игрок, у которого тройку составляют карты более высокого достоинства."
    "Идентичных троек, как и покеров, и фулл-хаусов, в игре быть не может.{nw}"
    ""

    pause(1)
    nvl clear

    "- {b}Стрит{/b} (англ. {i}straight{/i} — «порядок»): пять карт по порядку любых мастей,{nw}"
    if persistent.font_size == 'small':
        "например: {b}{color=#FF6600}5{image=suit_2ch_S} 4{image=suit_ussr_S} {color=#009833}3{image=suit_utan_S} {color=#FF6600}2{image=suit_2ch_S} Т{image=suit_2ch_S}{/color}{/color}{/b}."
    elif persistent.font_size == 'large':
        "например: {b}{color=#FF6600}5{image=suit_2ch_L} 4{image=suit_ussr_L} {color=#009833}3{image=suit_utan_L} {color=#FF6600}2{image=suit_2ch_L} Т{image=suit_2ch_L}{/color}{/color}{/b}."
    "Если на руках оказывается {b}шесть{/b} карт по порядку, младшая карта в комбинации не участвует.{nw}"
    "Туз может как начинать порядок, так и заканчивать его."
    if persistent.font_size == 'small':
        "В приведённом выше примере {b}{color=#FF6600}Т{image=suit_2ch_S}{/color}{/b} заканчивает комбинацию и его достоинство{nw}"
        "оценивается в единицу, а {b}{color=#FF6600}5{image=suit_2ch_S}{/color}{/b} считается старшей картой."
        "Вышеприведённая комбинация является самым младшим стритом; самый старший стрит —{nw}"
        "это стрит от туза: {b}{color=#FF6600}Т{image=suit_ussr_S} {color=#009833}К{image=suit_uvao_S} {color=#FF6600}Д{image=suit_2ch_S} В{image=suit_2ch_S} 10{image=suit_ussr_S}{/color}{/color}{/b}."
    elif persistent.font_size == 'large':
        "В приведённом выше примере {b}{color=#FF6600}Т{image=suit_2ch_L}{/color}{/b} заканчивает комбинацию и его достоинство{nw}"
        "оценивается в единицу, а {b}{color=#FF6600}5{image=suit_2ch_L}{/color}{/b} считается старшей картой."
        "Вышеприведённая комбинация является самым младшим стритом; самый старший стрит —{nw}"
        "это стрит от туза: {b}{color=#FF6600}Т{image=suit_ussr_L} {color=#009833}К{image=suit_uvao_L} {color=#FF6600}Д{image=suit_2ch_L} В{image=suit_2ch_L} 10{image=suit_ussr_L}{/color}{/color}{/b}."
    "При одновременном наличии стритов у двух игроков победитель определяется по старшей{nw}"
    "карте комбинации; если и старшие карты окажутся одинаковыми — объявляется ничья.{nw}"
    ""

    if persistent.font_size == 'small':
        "- {b}Флеш{/b} (англ. {i}flush{/i} — «масть»): пять карт одной масти, например: {b}{color=#009833}К{image=suit_utan_S} В{image=suit_utan_S} 8{image=suit_utan_S} 4{image=suit_utan_S} 3{image=suit_utan_S}{/b}.{nw}"
    elif persistent.font_size == 'large':
        "- {b}Флеш{/b} (англ. {i}flush{/i} — «масть»): пять карт одной масти, например: {b}{color=#009833}К{image=suit_utan_L} В{image=suit_utan_L} 8{image=suit_utan_L} 4{image=suit_utan_L} 3{image=suit_utan_L}{/b}.{nw}"
    "Такую комбинацию для оценки называют «флеш от короля» — старшей карты комбинации."
    "Самая старшая комбинация — с тузом.{nw}"
    "Если на руках оказывается {b}шесть{/b} карт одной масти, младшая карта комбинации игнорируется."
    "Если у обоих соперников на руках будет такая комбинация, преимущество отдаётся тому,{nw}"
    "у кого старшая карта в комбинации окажется более высокого достоинства."
    "Если же получится так, что достоинство старших карт одинаково, объявляется ничья.{nw}"
    ""

    pause(1)
    nvl clear

    "- {b}Фулл-хаус{/b}/Полный дом/Три плюс два (англ. {i}full house, full boat{/i} — «полный дом», «полная лодка»):{nw}"
    if persistent.font_size == 'small':
        "одна тройка и одна пара, например: {b}{color=#FF6600}10{image=suit_ussr_S} 10{image=suit_2ch_S} {color=#009833}10{image=suit_utan_S} 8{image=suit_uvao_S} {color=#FF6600}8{image=suit_ussr_S}{/color}{/color}{/b}{/b}."
    elif persistent.font_size == 'large':
        "одна тройка и одна пара, например: {b}{color=#FF6600}10{image=suit_ussr_L} 10{image=suit_2ch_L} {color=#009833}10{image=suit_utan_L} 8{image=suit_uvao_L} {color=#FF6600}8{image=suit_ussr_L}{/color}{/color}{/b}{/b}."
    "Если на руках две тройки, тройка карт младшего достоинства считается, как пара карт;{nw}"
    "{i}комбинации «Две тройки» в игре нет{/i}."
    "Если у соперников одновременно оказались на руках такие комбинации,{nw}"
    "старшей считается та, в которой тройку составляют более высокие по достоинству карты,"
    if persistent.font_size == 'small':
        "например: {b}{color=#009833}В{image=suit_uvao_S} {color=#FF6600}В{image=suit_2ch_S} В{image=suit_ussr_S} {color=#009833}9{image=suit_uvao_S} 9{image=suit_utan_S}{/color}{/color}{/b}{/b} старше, чем {b}{color=#FF6600}7{image=suit_2ch_S} 7{image=suit_ussr_S} {color=#009833}7{image=suit_utan_S} Т{image=suit_uvao_S} {color=#FF6600}Т{image=suit_2ch_S}{/color}{/color}{/b}."
    elif persistent.font_size == 'large':
        "например: {b}{color=#009833}В{image=suit_uvao_L} {color=#FF6600}В{image=suit_2ch_L} В{image=suit_ussr_L} {color=#009833}9{image=suit_uvao_L} 9{image=suit_utan_L}{/color}{/color}{/b}{/b} старше, чем {b}{color=#FF6600}7{image=suit_2ch_L} 7{image=suit_ussr_L} {color=#009833}7{image=suit_utan_L} Т{image=suit_uvao_L} {color=#FF6600}Т{image=suit_2ch_L}{/color}{/color}{/b}."
    "Два фулл-хауса, как и два покера, одинаковыми быть не могут (джокеров в колоде нет).{nw}"
    ""

    "- {b}Покер{/b}/Каре/Четвёрка (англ. {i}four of a kind, quads{/i} — «четыре одинаковых»): четыре карты{nw}"
    if persistent.font_size == 'small':
        "одинакового достоинства, например: {b}{color=#FF6600}8{image=suit_ussr_S} 8{image=suit_2ch_S} {color=#009833}8{image=suit_uvao_S} 8{image=suit_utan_S}{/color}{/b}{/b}, остальные карты не важны."
    elif persistent.font_size == 'large':
        "одинакового достоинства, например: {b}{color=#FF6600}8{image=suit_ussr_L} 8{image=suit_2ch_L} {color=#009833}8{image=suit_uvao_L} 8{image=suit_utan_L}{/color}{/b}{/b}, остальные карты не важны."
    "Если в дополнение к покеру на руках у игрока имеется ещё и пара, она не считается;{nw}"
    "{i}комбинации «Четыре + два» в игре нет{/i}."
    "Два покера принципиально не могут быть одинаковыми, так что когда у двух игроков в наличии{nw}"
    "такие комбинации, побеждает тот, у кого покер состоит из карт более высокого достоинства.{nw}"
    ""

    pause(1)
    nvl clear

    "- {b}Стрит-флеш{/b} (англ. {i}straight flush{/i} — «масть по порядку»): любые пять карт одной масти по порядку,{nw}"
    if persistent.font_size == 'small':
        "например: {b}{color=#009833}9{image=suit_utan_S} 8{image=suit_utan_S} 7{image=suit_utan_S} 6{image=suit_utan_S} 5{image=suit_utan_S}{/color}{/b}. Туз может как начинать порядок (роял-флеш),{nw}"
        "так и заканчивать его: {b}{color=#009833}5{image=suit_uvao_S} 4{image=suit_uvao_S} 3{image=suit_uvao_S} 2{image=suit_uvao_S} Т{image=suit_uvao_S}{/color}{/b}."
        "Комбинации карт {b}{color=#FF6600}2{image=suit_ussr_S} Т{image=suit_ussr_S} К{image=suit_ussr_S} Д{image=suit_ussr_S} В{image=suit_ussr_S}{/color}{/b} или {b}{color=#FF6600}4{image=suit_2ch_S} 3{image=suit_2ch_S} 2{image=suit_2ch_S} Т{image=suit_2ch_S} К{image=suit_2ch_S}{/color}{/b} — не являются стрит-флешами.{nw}"
    elif persistent.font_size == 'large':
        "например: {b}{color=#009833}9{image=suit_utan_L} 8{image=suit_utan_L} 7{image=suit_utan_L} 6{image=suit_utan_L} 5{image=suit_utan_L}{/color}{/b}. Туз может как начинать порядок (роял-флеш),{nw}"
        "так и заканчивать его: {b}{color=#009833}5{image=suit_uvao_L} 4{image=suit_uvao_L} 3{image=suit_uvao_L} 2{image=suit_uvao_L} Т{image=suit_uvao_L}{/color}{/b}."
        "Комбинации карт {b}{color=#FF6600}2{image=suit_ussr_L} Т{image=suit_ussr_L} К{image=suit_ussr_L} Д{image=suit_ussr_L} В{image=suit_ussr_L}{/color}{/b} или {b}{color=#FF6600}4{image=suit_2ch_L} 3{image=suit_2ch_L} 2{image=suit_2ch_L} Т{image=suit_2ch_L} К{image=suit_2ch_L}{/color}{/b} — не являются стрит-флешами.{nw}"
    "Если на руках у игрока оказывается {b}шесть{/b} карт по порядку, младшая карта игнорируется."
    "Если у двух игроков одновременно на руках оказывается стрит-флеш, выигрывает тот,{nw}"
    "у кого комбинация начинается с карты более высокого достоинства."
    "Если у обоих игроков стрит-флеши идентичные, объявляется ничья.{nw}"
    ""

    "- {b}Роял-флеш{/b} (англ. {i}royal flush{/i} — «королевская масть»): не является отдельной комбинацией,{nw}"
    "а является частным случаем стрит-флеша, старшим из всех возможных, и состоит из 5 старших{nw}"
    if persistent.font_size == 'small':
        "(туз, король, дама, валет, десять) карт одной масти, например: {b}{color=#FF6600}Т{image=suit_ussr_S} К{image=suit_ussr_S} Д{image=suit_ussr_S} В{image=suit_ussr_S} 10{image=suit_ussr_S}{/color}{/b}."
    elif persistent.font_size == 'large':
        "(туз, король, дама, валет, десять) карт одной масти, например: {b}{color=#FF6600}Т{image=suit_ussr_L} К{image=suit_ussr_L} Д{image=suit_ussr_L} В{image=suit_ussr_L} 10{image=suit_ussr_L}{/color}{/b}."
    "Если хотя бы одна из пяти карт не совпадает по масти с остальными, в таком случае получившаяся{nw}"
    "комбинация будет расцениваться как стрит от туза."
    "Эта комбинация выпадает достаточно редко; может быть, кому-то и повезёт…{nw}"
    ""

    pause(1)
    $ set_mode_adv()
    jump ds_cards_rules_known

label ds_cards_rules_known:
# ----------------------------------------------------------------------------------- /ADD
    el "Ну а сейчас для лучшего усвоения материала, давайте сыграем пробную партию."
    el "На сторону сдаётся по шесть карт…"
    show us dontlike pioneer at left
    show el angry pioneer at right
    with dissolve
    el "По шесть, а не по двенадцать!"
    "Кричит он, кинув косой взгляд на столик Шурика и Ульяны."
    "Немудрено — рыжая бестия забрала себе все 12 карт и разглядывает их, выбирая покрасивее."
    hide us with dissolve
    "После нескольких минут споров и ругани Ульянка фыркает и возвращает карты на родину, после чего, перемешав колоду, сдаёт себе и Шурику по шесть карт."
# --------------------------------------------------------------------- ADD Блокировка роллбэка включена
    $ d2_cardgame_block_rollback = True
# --------------------------------------------------------------------- /ADD
    stop music fadeout 2

    window hide
    menu:
        "Пройти обучение":
            jump ds_cards_demo
        "Пропустить обучение":
            jump ds_cards_continue

label ds_cards_demo:
    python:
        dialogs = {
                        (3, 'rival_select','call'): 'ds_cards_demo_intro',
                        (3, 'me_defend_1','call'):  'ds_cards_demo_play_me_defend_1',
                        (3, 'me_defend_2','call'):  'ds_cards_demo_play_me_defend_2',
                        (3, 'me_select_1','call'):  'ds_cards_demo_play_me_select_1',
                        (3, 'rival_defend','call'): 'ds_cards_demo_play_rival_defend',
                        (2, 'rival_select','jump'): 'ds_cards_demo_play_after_loop'
                    }
        ds_generate_cards('bg int_dining_hall_sunset', dialogs)
        rival = CardGameRivalWiseUsual(ds_un_avatar, u"Пробная игра", 'foolplay', 5)
        ds_name_my_rival_r = "Лены"
        VISIBLE = False
        ds_whose_first_move = 'rival'
    jump ds_cards_gameloop

label ds_cards_demo_intro:
    play music music_list["get_to_know_me_better"] fadein 2
    show el normal pioneer at cleft with dissolve
    $ show_cards_alt()
    $ renpy.transition(dissolve)
    el "Это не просто карты."
    play sound ds_sfx_int
    con "Это ещё и наш способ оставить противника без штанов."
    con "Если бы вы играли на деньги…"
    play sound ds_sfx_fys
    ins "Или на раздевание…"
    el "Это ваши войска специального назначения. {w}Элита!"
    el "Вы дорожите каждым из них, ведь его жизнь неповторима."
    el "Потеря каждого из них критична."
    el "А теперь переверните карты и посмотрите."
    $ VISIBLE = True
    $ ds_hint_poker = True
    $ INVISIBLE = ds_cards_labeled
    $ show_cards_alt()
    $ renpy.transition(dissolve)
    play sound ds_sfx_int
    lgc "Чего и следовало ожидать, Ульянка перевернула карты Шурика и задумчиво изучает их."
    show el angry pioneer at cleft with dspr
    el "Свои карты!"
    el "Свои! А не чужие."
    us "А это была разведка! Вот!"
    con "По сравнению с непрошибаемым Шуриком, Ульяна являет собой образец неуправляемой стихии."
    "Вздохнув, Шурик собирает свои карты и, тщательно перемешав, сдаёт себе ещё шестёрку карт."
    show el normal pioneer at cleft with dspr
    "Между тем, Электроник продолжает объяснение."
    el "Итак, вы во главе элитных войск."
    el "Но само сражение ещё впереди. А пока вам надо укрепить порядки."
    con "Окопаться, не иначе."
    el "А для этого… Необходимо сманивать элиту противника на свою сторону!"
    us "Сманивать в смысле «красть»?"
    play sound ds_sfx_psy
    emp "В голосе Ульяны слышится неприкрытый восторг."
    show el upset pioneer at cleft with dspr
    el "В целом, д-да…"
    emp "Ведущего немного смутил эпитет, но крыть было нечем, и он согласился."
    show el normal pioneer at cleft with dspr
    el "В целом. Но не всё так просто."
    el "Первым ходом вы намечаете себе цель, и пытаетесь её сманить."
    el "Вы не видите, кто это, поэтому здесь работает удача."
    us "Мой дедушка — офицер!"
    show el smile pioneer at cleft with dspr
    el "Итак, противник тянется к карте, но и вы не должны дремать!"
    el "У вас есть две попытки запутать врага, поменяв карты местами!"
    show el serious pioneer at cleft with dspr
    el "Или можно не менять, если под ударом ненужная вам карта. Просто пропускаете ход, и карта отходит к атакующему."
    el "Естественно, обороняющийся рано или поздно становится атакующим — и вот тогда может вернуть карту или забрать нужную карту у противника."
    show el grin pioneer at cleft with dspr
    el "Но от слов к делу. На практике это легче понять, правда?"
    el "Так что… Играем!"

    hide el with dissolve
    me "Первый ход твой…"
    "Ты, как мог, разложил карты поудобнее."
    "И Лена, смутившись ещё больше обычного, тянется к твоим картам…"
    return

label ds_cards_demo_play_me_defend_1:
    "Но тут её рука застывает на полпути."
    un "Т-ты будешь…"
    play sound ds_sfx_mot
    res "Точно! Ты же должен защищать свою карту!"
    play sound ds_sfx_int
    enc "Чтобы попытаться запутать соперника, можно поменять карты местами — и так два раза. А можно и не менять…"
    th "Защищать мне эту карту или нет?"
    return

# ============================================ добавлена одна метка
label ds_cards_demo_play_me_defend_2:
    th "И Лена может изменить свой выбор, взяв другую карту, а может и не менять."
    play sound ds_sfx_psy
    vol "Понемногу всё становится понятно!"
    return
# ============================================ добавлена одна метка

label ds_cards_demo_play_me_select_1:
    me "Теперь моя очередь."
    th "Я могу вернуть украденную карту или выбрать любую другую…"
    if ds_cards_labeled:
        play sound ds_sfx_mot
        inf "А зная карты противника, легко выбрать нужную…"
        play sound ds_sfx_psy
        vol "Ты никогда бы не подумал, что будешь жульничать на турнире, но, возможно, как раз это тебя и спасёт…"
    return

label ds_cards_demo_play_rival_defend:
    th "Лена может попробовать защитить свою карту."
    play sound ds_sfx_mot
    res "Но если ты будешь внимательным, то всё равно возьмёшь ту, что выбрал с самого начала…"
    return

label ds_cards_demo_play_after_loop:
    $ show_cards_alt()
    $ renpy.transition(dissolve)
    th "Получилось!"
    window auto
    $ ui.jumpsoutofcontext('ds_cards_continue')

label ds_cards_continue:
    scene bg int_dining_hall_sunset with dissolve
    python:
        renpy.scene('underlay')
    $ persistent.altCardsDemo = True
    play music music_list["my_daily_life"] fadein 5
    "Электроник, до этого наблюдавший за нами, удовлетворённо кивает."
    play sound ds_sfx_int
    lgc "Похоже, теперь вы действительно разобрались в его игре."
    show el normal pioneer at center with dissolve
    el "Итак, во время игры противники три раза обмениваются своими бойцами, а потом открывают карты."
    el "И мы смотрим, чья армия сильнее."
    hide el with dissolve
    "Электроник отходит к своему ватману, а Ульяна не выдерживает и кричит."
    show us laugh pioneer with dissolve
    us "Моя армия будет самой сильной!"
    show us grin pioneer with dspr
    us "Давайте уже играть!"
    hide us with dissolve
    jump ds_cards_prep

label ds_cards_prep:
    scene bg int_dining_hall_sunset with dissolve
    show mt normal pioneer with dissolve
    mt "Давайте-ка мы немного разнообразим игру!"
    show el surprise pioneer at left with dissolve
    el "Что вы имеете в виду?"
    show mt laugh pioneer with dspr
    mt "Я вижу, тут кое-кто очень настроен на победу, так что внесём элемент случайности."
    hide mt with dissolve
    "Она достаёт из кармана несколько бумажек и, быстро нарвав их, пишет на них номера, ссыпает в панамку и обносит присутствующих."
    show el sad pioneer with dspr
    el "Воооот, лишние хлопоты."
    "Вздыхает парень."
    show mt normal pioneer with dissolve
    mt "Всё хорошо! {w}Тянем жребий и по нему распределяемся на пары."
    mt "А то знаю я эти договорные матчи!"
    "Не прошло и пяти минут, а вы уже разбились по парам."
    window hide
    if persistent.ds_cards_max_stage >= 0:
        menu:
            "При желании вы можете пропустить турнир с желаемым результатом (не превышающим максимальный достигнутый)"
            "Играть самостоятельно":
                pass
            "Победа в финале" if persistent.ds_cards_max_stage == 3:
                $ ds_day2_detour_1_tour = True                         # Пропускаем 1 тур
                $ ds_day2_detour_semifinal = True                      # Пропускаем полуфинал
                $ ds_day2_detour_final = True                          # Пропускаем финал
                $ ds_day2_tournament_fast_win = True                   # Победа в финале на халяву
                menu:
                    "Против случайного соперника":
                        pass
                    "Против Лены":
                        $ ds_day2_detour_number = 1
                    "Против Слави":
                        $ ds_day2_detour_number = 2
                    "Против Алисы":
                        $ ds_day2_detour_number = 3
                    "Против Мику":
                        $ ds_day2_detour_number = 4
                    "Против Ульяны":
                        $ ds_day2_detour_number = 5
                    "Против Шурика":
                        $ ds_day2_detour_number = 6
                    "Против Жени" if not ds_bring_mz_fail:
                        $ ds_day2_detour_number = 7
                    "Против Яны" if ds_bring_mz_fail:
                        $ ds_day2_detour_number = 8
            "Поражение в финале" if persistent.ds_cards_max_stage >= 2:
                $ ds_day2_detour_1_tour = True                         # Пропускаем 1 тур
                $ ds_day2_detour_semifinal = True                      # Пропускаем полуфинал
                $ ds_day2_detour_final = True                          # Пропускаем финал
                menu:
                    "Против случайного соперника":
                        $ ds_day2_detour_number = 0
                    "Против Лены":
                        $ ds_day2_detour_number = 1
                    "Против Слави":
                        $ ds_day2_detour_number = 2
                    "Против Алисы":
                        $ ds_day2_detour_number = 3
                    "Против Мику":
                        $ ds_day2_detour_number = 4
                    "Против Ульяны":
                        $ ds_day2_detour_number = 5
                    "Против Шурика":
                        $ ds_day2_detour_number = 6
                    "Против Жени" if not ds_bring_mz_fail:
                        $ ds_day2_detour_number = 7
                    "Против Яны" if ds_bring_mz_fail:
                        $ ds_day2_detour_number = 8
            "Поражение в полуфинале" if persistent.ds_cards_max_stage >= 1:
                $ ds_day2_detour_1_tour = True                         # Пропускаем 1 тур
                $ ds_day2_detour_semifinal = True                      # Пропускаем полуфинал
            "Поражение в первом туре":
                $ ds_day2_detour_1_tour = True                         # Пропускаем 1 тур
    jump ds_cards_tour_1

# ---------------------------------------------------------------------------------
label ds_cards_tour_1:
    $ ds_tournament_state = "1_round_start"                                                # устанавливаем начало 1-го раунда
    $ ds_day2_gamblers_begin = ds_gamblers_shuffler()                                     # вызываем рандомизатор — получаем список игроков, отсортированный по уcловным номерам.
    $ ds_my_rival_1_tour = ds_get_me_rival(ds_day2_gamblers_begin)                       # узнаём своего соперника
    $ ds_name_my_rival_i = ds_my_rival_1_tour.name['i']                                   # узнаём ИМЯ своего соперника (в именительном падеже)
    $ ds_name_my_rival_r = ds_my_rival_1_tour.name['r']                                   # узнаём ИМЯ своего соперника (в родительном падеже)
    $ ds_name_my_rival_d = ds_my_rival_1_tour.name['d']                                   # узнаём ИМЯ своего соперника (в дательном падеже)
    $ ds_name_my_rival_v = ds_my_rival_1_tour.name['v']                                   # узнаём ИМЯ своего соперника (в винительном падеже)
    $ ds_name_my_rival_t = ds_my_rival_1_tour.name['t']                                   # узнаём ИМЯ своего соперника (в творительном падеже)
    $ ds_spr_my_rival = ds_my_rival_1_tour.take                                           # получаем спрайт соперника — заголовок
    $ ds_emo_my_rival = ds_sprites_rival_recognition[ds_spr_my_rival][0]                 # эмоция (строка)
    $ ds_acc_my_rival = ds_sprites_rival_recognition[ds_spr_my_rival][1]                 # аксессуар (строка)
    $ ds_clot_my_rival = ds_sprites_rival_recognition[ds_spr_my_rival][2]                # одежда (строка)
    $ ds_pos_my_rival = ds_sprites_rival_recognition[ds_spr_my_rival][3]                 # положение
    $ ds_nick_my_rival = ds_my_rival_1_tour.nick                                          # получаем характер соперника (для диалога)
# ---------------------------------------------------------------------------------
    scene bg int_dining_hall_sunset with dissolve
    $ renpy.fix_rollback()                                                                  # фиксируем выбор — "откатом" поменять будет нельзя
    "Рандом послал тебе в оппоненты {nw}%(ds_name_my_rival_v)s.{w}"                             # называем своего соперника

# ------------------------------------------------- ДИАЛОГИ
    if ds_my_rival_1_tour.take == 'un':
        show un shy pioneer at cright with dissolve
        me "И снова добрый вечер."
        show un smile pioneer with dspr
        "Она смущённо улыбается, но ничего не говорит."

    elif ds_my_rival_1_tour.take == 'sl':
        show sl smile2 pioneer at cright with dissolve
        sl "Знаешь, я не очень хороша в картах."
        me "Да я вообще ничего про эту игру не знаю."
        "Славя улыбается тебе и садится напротив."

    elif ds_my_rival_1_tour.take == 'dv':
        show dv grin pioneer2 at cright with dissolve
        dv "Ну что, готов к сокрушительному поражению?"
        "Усмехается она, садясь на противоположное место."
        window hide
        menu:
            "Съязвить":
                if skillcheck('authority', lvl_easy):
                    window show
                    play sound ds_sfx_psy
                    aut "Не давай себя запугать!"
                    me "А как же. {w}Я принесу на твою могилку два гладиолуса."
                    $ ds_semtype += 1
                else:
                    window show
                    play sound ds_sfx_psy
                    aut "Она, похоже, настроена воинственно - не то, что ты."
                    me "Всенепременно..."
                $ ds_skill_points['authority'] += 1
            "Разжалобить":
                window show
                me "Алис, может, всё-таки не надо?.."
                dv "Надо, Сёма, надо."
                $ ds_semtype -= 1
            "Проигнорировать":
                window show

    elif ds_my_rival_1_tour.take == 'mi':
        show mi smile pioneer at cright with dissolve
        if ds_lp['mi'] >= 0:
            mi "И снова здравствуй, Сенечка."
        else:
            mi "Ой, привет, Семён!"
        me "Ну привет, Мику."
        if ds_lp['mi'] > 0:
            show mi laugh pioneer with dspr
            mi "Как здорово, что ты достался мне в противники! Я очень хотела, чтобы это был ты!"
            play sound ds_sfx_mot
            res "Ты немного опешил."
            me "Зачем?"
            show mi grin pioneer with dspr
            mi "Ну как же, как же!"
            show mi smile pioneer with dspr
            mi "Ты же новый человек в лагере, а мы с тобой ещё толком не поговорили друг с другом!"
            play sound ds_sfx_int
            rhe "Так вот она о чём."
            play sound ds_sfx_int
            con "Сказать по правде, ты бы с радостью променял карточную игру на беседу с Мику."
            con "Она может и болтушка, но болтушка красивая."
            rhe "Главное умело фильтровать поток её слов и вычленять самое главное."
            rhe "А там глядишь и увидишь в ней ещё что-то."
            th "Однако…"
            window hide
            menu:
                "Предложить поговорить после":
                    window show
                    me "Давай после игры, ладно?"
                    me "Раз уж взялись за гуж… — и далее по тексту."
                    show mi happy pioneer with dspr
                    mi "Мы можем побеседовать в процессе."
                    show mi smile pioneer with dspr
                    mi "Как говорит мой Па — ничто не мешает совместить приятное с полезным!"
                    th "Я бы не назвал турнир «полезным»."
                    me "По рукам."
                    $ ds_lp['mi'] += 1
                "Предложить поговорить в процессе":
                    window show
                    me "А давай поговорим во время игры!"
                    show mi smile pioneer with dspr
                    mi "Как говорит мой Па — ничто не мешает совместить приятное с полезным!"
                    th "Я бы не назвал турнир «полезным»."
                    me "По рукам."
                    $ ds_lp['mi'] += 2
                "Потребовать молчать":
                    window show
                    me "Нет уж, я хочу сконцентрироваться на игре."
                    show mi sad pioneer with dspr
                    mi "Ну ладно..."
                    $ ds_lp['mi'] -= 1

    elif ds_my_rival_1_tour.take == 'us':
        stop music fadeout 2
        show us laugh pioneer at cright with dissolve
        us "Готов поддаваться?"
        window hide
        menu:
            "Согласиться":
                window show
                me "Ну ладно, так уж и быть!"
                us "Вот и отлично, будем играть по моим правилам!"
            "Cогласиться (соврать)":
                window show
                me "Обязательно!"
                play sound ds_sfx_int
                dra "Она ребёнок, так что обмануть её насчёт своих намерений не легко, а очень легко!"
                us "Вот и отлично, будем играть по моим правилам!"
            "Отказать":
                me "И не мечтай."
                show us calml pioneer with dspr
                us "И не надо! Но играть будем по моим правилам!"
        me "Это по каким это?"
        us "Увидишь!"

    elif ds_my_rival_1_tour.take == 'sh':
        show sh normal pioneer at cright with dissolve
        sh "Ну что, пусть победит сильнейший?"
        window hide
        menu:
            "Согласиться":
                window show
                me "Пусть победит сильнейший!"
                "С этими словами ты пожимаешь ему руку."
            "Молча пожать руку":
                window show
                "Ты молча пожимаешь ему руку."

    elif ds_my_rival_1_tour.take == 'mz':
        show mz normal glasses pioneer at cright with dissolve
        mz "Я твой противник."
        "Скрипит она, присаживаясь напротив."
        window hide
        menu:
            "Пожелать удачи":
                window show
                me "Удачи!"
                "Но она не реагирует."
            "Сделать комплимент":
                window show
                me "Прекрасно выглядишь."
                "Но она не реагирует."
            "Кивнуть молча":
                window show
                "Ты молча киваешь в ответ."
    elif ds_my_rival_1_tour.take == 'ya':
        show ya normal pioneer at cright with dissolve
        ya "Привет..."
        me "Привет."
        play sound ds_sfx_psy
        emp "Она не склонна к разговорам. И вообще играет только потому, что её попросили."
    jump ds_cards_participate
# ------------------------------------------------- /ДИАЛОГИ

label ds_cards_participate:
    $ ds_day2_gamblers_1_tour = ds_gamblers_arrange(ds_day2_gamblers_begin)      # получаем список игроков, рассаженных по столам попарно (1 тур)
    $ renpy.fix_rollback()                                                          # фиксируем выбор — "откатом" поменять будет нельзя
    $ places_my_table = ds_get_my_table(ds_day2_gamblers_1_tour)                  # Стол Семёна = [место Семёна, место соперника, № их стола]

    if not ds_day2_detour_1_tour:                                                  # если НЕ пропуск 1 тура
        scene bg int_dining_hall_sunset with dissolve
        play sound ds_sfx_psy
        vol "Пока суд да дело, разузнай, какая диспозиция сложилась на игровом поле."
        $ ds_mstt = 9
        call ds_show_tournament_table                                                  # показываем турнирную таблицу — ПУСТУЮ


    $ ds_table_no = 1                                                              # № стола = 1 (начинаем с первого)
    $ ds_mstt = 0                                                                  # обнуляем глобальный счетчик таблицы
    $ ds_random_box_1 = range(1,len(ds_table_affiliation)+1)                      # черный ящик — список от 1 до длины представлений столов +1
    while ds_table_no <= 4:                                                        # перебираем столы от 1 до 4
        if not ds_day2_detour_1_tour:                                              # если НЕ пропуск 1 тура
            $ sitting_at_table,gambler_upper,gambler_lower,must_taunt = ds_declare_tournament_tables(ds_table_no)  #расссадка, игроки, таунты — по номеру стола
            "%(sitting_at_table)s"
            call ds_show_tournament_table                                                  # переход по метке — вызов очередной фишки
            extend " %(gambler_upper)s"                                                 # выводим в окно имя верхнего игрока
            call ds_show_tournament_table                                                  # переход по метке — вызов очередной фишки
            extend " и %(gambler_lower)s."                                              # выводим в окно имя нижего игрока
            if must_taunt != None:                                                      # если таунт есть
                "%(must_taunt)s"                                                        # выводим его

            if ds_table_no == 1 and ds_table_no != places_my_table[2]:
                "С первым столом разобрались, кто-то из них сегодня не дойдёт до финала."
            elif ds_table_no == 2 and places_my_table[2] == 1:
                "Со вторым столом разобрались, кто-то из них сегодня не дойдёт до финала."

        if ds_table_no != places_my_table[2]:                                                       # если номер стола — НЕ свой
            $ ds_day2_gamblers_1_tour[2*ds_table_no - renpy.random.choice([1,2])].winner = True    # тогда один из игроков (рандомно) — победитель в этапе
            $ renpy.block_rollback()                                                                 # блокируем роллбак
        $ ds_table_no += 1                                                                          # следующий стол
    if (ds_day2_detour_number != 0):                                                                # если выбрали конкретного соперника для финала
        $ ds_day2_gamblers_1_tour[6].winner = False                                                 # его соперник в первом коне проигрывает
        $ ds_day2_gamblers_1_tour[7].winner = True                                                  # а он сам выигрывает в первом коне
    if not ds_day2_detour_1_tour:                                                                   # если НЕ пропуск 1 тура
        "Таким нехитрым образом тебе удалось немного разобраться с тем, кто и против кого играет."
        th "Что ж…"
        if ds_bet_dv:
            play sound ds_sfx_psy
            aut "Пусть тебе повезёт, а одна рыжая зазнайка утрётся!"
        "Ты киваешь, сигнализируя о готовности."

    if ds_day2_detour_1_tour and not ds_day2_detour_semifinal:                # если пропуск 1 тура и не пропуск полуфинала
        jump ds_cards_participate_fail_end                                  # переход на  поражение в 1 туре
    elif ds_day2_detour_semifinal:                                             # если пропуск полуфинала
        jump ds_cards_participate_win_end                                  # переход на победу в 1 туре
    jump ds_cards_tournament_start

label ds_cards_tournament_start:                                            # начало 1 тура — сюда переходим при реванше
    call ds_day2_stipulation                                               # определяемся, кто первый ходит

#-------------------------------------------------------------------------------------------------
    # первоначальные "настройки" игроков — могут меняться по результатам игры
    # 'defense' — защита, 'gamble' — риск, 'succumb' — слив, 'foolplay' — рандом
    # вероятность ошибки: 1 = 80%, …, 4 = 20%, 5 — ошибок нет.

    if ds_my_rival_1_tour.take == 'un':                                                    # Лена
        if not ds_bet_dv:                                                              # если с Алисой не спорить
            $ ds_day2_gambler_behavior = 'gamble'                                              # Лена пытается рискнуть
            $ ds_day2_gambler_skill = 3                                                        # правда, ошибок многовато — 40%(3)
        else:
            $ ds_day2_gambler_behavior = 'succumb'                                             # Если поспорить — то также игра в поддавки
            $ ds_day2_gambler_skill = 4                                                        # может ошибиться  — 20%(4)
    elif ds_my_rival_1_tour.take == 'sl':                                                  # Славя будет защищаться, ошибок — 40%(3)
        $ ds_day2_gambler_behavior = 'defense'
        $ ds_day2_gambler_skill = 3
    elif ds_my_rival_1_tour.take == 'dv':                                                  # Алиса рискует, ошибок — 20%(4)
        $ ds_day2_gambler_behavior = 'gamble'
        $ ds_day2_gambler_skill = 4
    elif ds_my_rival_1_tour.take == 'mi':                                                  # Мику будет защищаться, ошибок — 40%(3)
        $ ds_day2_gambler_behavior = 'defense'
        $ ds_day2_gambler_skill = 3
    elif ds_my_rival_1_tour.take == 'us':                                                  # Ульяна будет защищаться
        $ ds_day2_gambler_behavior = 'defense'
        $ ds_day2_gambler_skill = 1                                                        # ошибок — 80%(1)
    elif ds_my_rival_1_tour.take == 'sh':                                                  # Шурик экспериментирует, так что может и рискнуть, и защищаться, и слить; ошибки 40%(3)
        $ ds_day2_gambler_behavior = renpy.random.choice(['defense', 'gamble'])            # у него своя кухня — набор из возможных вариантов
        $ ds_day2_gambler_skill = 3
    elif ds_my_rival_1_tour.take == 'mz':                                                  # Женя играет рандомно, как в классике, ошибки = 5
        $ ds_day2_gambler_behavior = 'foolplay'
        $ ds_day2_gambler_skill = 5
    elif ds_my_rival_1_tour.take == 'ya':
        $ ds_day2_gambler_behavior = 'defense'
        $ ds_day2_gambler_skill = 5
#-------------------------------------------------------------------------------------------------

label ds_day2_1_tour_re_game:                                                              # игра 1 тура — сюда возвращаемся на повторную игру
    $ ds_my_poker_hand = None
    $ ds_rival_poker_hand = None

    $ VISIBLE = True
    $ INVISIBLE = ds_cards_labeled

    python:
        dialogs = {
                        (0, 'win','jump'):'ds_cards_participate_win_end',
                        (0, 'fail','jump'):'ds_cards_participate_fail_end',
                        (0, 'draw','jump'):'ds_cards_draw'
                    }
        generate_cards_alt('bg hall', dialogs)

# ****************   НОВЫЕ  СОПЕРНИКИ   ******************************************
        if ds_my_rival_1_tour.take == 'un':
            rival = CardGameRivalWiseUsual(ds_un_avatar, u"Лена", ds_day2_gambler_behavior, ds_day2_gambler_skill)
        elif ds_my_rival_1_tour.take == 'sl':
            rival = CardGameRivalWiseUsual(ds_sl_avatar, u"Славя", ds_day2_gambler_behavior, ds_day2_gambler_skill)
        elif ds_my_rival_1_tour.take == 'dv':
            rival = CardGameRivalWiseUsual(ds_dv_avatar, u"Алиса", ds_day2_gambler_behavior, ds_day2_gambler_skill)
        elif ds_my_rival_1_tour.take == 'mi':
            rival = CardGameRivalWiseUsual(ds_mi_avatar, u"Мику", ds_day2_gambler_behavior, ds_day2_gambler_skill)
        elif ds_my_rival_1_tour.take == 'us':
            rival = CardGameRivalWiseLikeUS(ds_us_avatar, u"Ульяна", ds_day2_gambler_behavior, ds_day2_gambler_skill)
        elif ds_my_rival_1_tour.take == 'sh':
            rival = CardGameRivalWiseUsual(ds_sh_avatar, u"Шурик", ds_day2_gambler_behavior, ds_day2_gambler_skill)
        elif ds_my_rival_1_tour.take == 'mz':
            rival = CardGameRivalWiseUsual(ds_mz_avatar, u"Женя", ds_day2_gambler_behavior, ds_day2_gambler_skill)
        elif ds_my_rival_1_tour.take == 'ya':
            rival = CardGameRivalWiseUsual(ds_ya_avatar, u"Яна", ds_day2_gambler_behavior, ds_day2_gambler_skill)
# ************************************************************************************

    $ ds_hint_poker = ds_hint_poker_contractual                                           # подсказки комбинаций — по просмотру правил
    jump ds_cards_gameloop                                                            # переход карточный стол

#-------------------------------------------------------------------------------------------------
label ds_cards_participate_fail_end:
    $ ds_day2_result_tour = 1                                              # Семён проиграл в 1 туре

    $ persistent.altCardsFail = True

    $ ds_day2_gamblers_1_tour[places_my_table[1]].winner = True            # соперник выиграл
    $ ds_tournament_state = "1_round_end"                                  # устанавливаем конец 1-го раунда

    scene bg int_dining_hall_sunset with dissolve
    call ds_cards_summary_round

# ---------------------------------------------------- ДИАЛОГИ
    if ds_my_rival_1_tour.take == 'un':
        $ ds_lp['un'] += 1
        stop music fadeout 2
        if ds_bet_dv:
            show un angry2 pioneer at center with dissolve
            un "Ты поддался… Ты чёртов жулик, ты поддался…"
            play music music_list["you_lost_me"] fadein 2
            play sound ds_sfx_mot
            res "О чем это она? Ещё и жуликом обозвала."
            res "И вообще, это точно Лена?"
            if ds_cards_labeled:
                th "Впрочем, она не так уж и далека от истины."
            me "Лена, извини, но…"
            un "Не говори ничего. Я знаю, о чём ты спорил с этой рыжей."
            un "И я знаю — что на кону!"
            show un sad pioneer with dspr
            un "Ты не понимаешь, что никому такая победа не нужна? А тебя завтра… на весь лагерь…"
            window hide
            menu:
                "Показать безразличие":
                    window show
                    me "А ты правда думаешь, что мне не плевать? Пусть говорит, что хочет. Я сделал так, как считал правильным."
                "Извиниться":
                    window show
                    me "Извини, я не подумал..."
        else:
            $ ds_lp['sl'] += 1
            show un angry2 pioneer with dspr
            un "Что ты наделал?"
            play music music_list["you_lost_me"] fadein 2
            "Она приподнялась было над столом и тут же падает обратно."
            un "Зачем? Кому нужна такая победа…"
            me "Мне?"
            th "Она такая симпатичная, когда сердится."
        show un angry2 pioneer with dspr
        "А Лена хлопает ладонью по столу, да так, что на секунду все смолкают и оборачиваются на неё."
        un "Кому нужна такая победа…"
        "Повторяет она."
        window hide
        menu:
            "Победа нужна..."
            "Мне":
                window show
                me "Эта победа была нужна мне."
                "В гробовой тишине произносишь ты."
                show un serious pioneer with dspr
                me "Просто для того, чтобы указать кое-кому, что не всё решают угрозы или шантаж."
                me "Наслаждайся вечером."
                stop music fadeout 3
                hide un with dissolve
                "Ты киваешь и выходишь из-за стола, оставляя Лену беззвучно хватать ртом воздух."
            "Лене":
                window show
                me "Эта победа для тебя!"
                "В гробовой тишине произносишь ты."
                show un rage pioneer with dspr
                un "Да не нужна мне такая победа!"
                stop music fadeout 3
                hide un with dissolve
                "Но ты уже вышел, не обращая внимания на возмущение Лены."
            "Судьбе":
                window show
                me "Так решила судьба!"
                "В гробовой тишине произносишь ты."
                show un serious pioneer with dspr
                un "Думаешь? Думаешь, мне повезло просто?!"
                me "Ну да..."
                stop music fadeout 3
                hide un with dissolve
                "С этими словами ты выходишь из столовой, оставляя Лену беззвучно хватать ртом воздух."
        if skillcheck('drama', lvl_medium, passive=True):
            play sound ds_sfx_int
            dra "Вам не кажется, мессир, что с Леной было что-то не так?"
            th "И то верно... какая-то она слишком агрессивной оказалась."
            dra "Будьте с ней осторожны: возможно, она что-то скрывает."
            $ ds_skill_points['drama'] += 1
        play music music_list["my_daily_life"] fadein 5


    elif ds_my_rival_1_tour.take == 'sl':
        show sl smile pioneer with dissolve
        sl "Семён, если ты захочешь сыграть ещё раз, я не против."
        play sound ds_sfx_psy
        sug "Забавная девочка, готова даже поступиться собственной победой."
        window hide
        menu:
            "Согласиться":
                window show
                me "Ну ладно, раз ты так хочешь..."
                show el serious pioneer at right with dissolve
                el "Нет уж, никаких переигровок!"
                hide el with dissolve
            "Отказаться":
                window show
                me "Нет уж, сегодня моя очередь быть благородным."
                $ ds_lp['sl'] += 1
        window hide
        menu:
            "Пожелать удачи":
                window show
                "Ты наклоняешься над столом."
                me "Желаю тебе удачи в полуфинале!"
                sl "Но я же просто за компанию играть села!"
                sl "Я вообще карты не люблю."
                me "А что поделаешь. {w}Записалась — так играй до конца!"
                show sl sad pioneer with dspr
                me "К тому же, мне очень хочется, чтобы сегодня ты победила. Сумеешь?"
                show sl normal pioneer with dspr
                "Славя неуверенно кивает, а ты поднимаешься и показываешь ей большой палец."
                play sound ds_sfx_psy
                sug "Чуточку уверенности в себе вне привычной сферы обитания — вот что ей нужно."
                $ ds_lp['sl'] += 1
            "Молча уйти":
                window show
                "Ты выходишь, просто попрощавшись со Славей и участниками."

    elif ds_my_rival_1_tour.take == 'dv':
        if ds_bet_dv:
            show dv grin pioneer2 with dspr
            dv "Ну что, ты уже приготовился?"
            "Она упивается моментом."
            if ds_cards_labeled:
                th "Мда, и стоило карты метить, если они мне не помогли?"
            me "К чему?"
            dv "Как к чему? К рассказу о том, куда смотрел, за что трогал."
            dv "Очень интересный рассказ будет, чувствую!"
            show dv laugh pioneer2 with dspr
            dv "Но ладно."
            me "Да?"
            play sound ds_sfx_mot
            com "Ты аж приподнимаешься на месте."
            th "Неужели передумала!"
            show dv smile pioneer2 with dspr
            dv "Я расскажу всё в финале, когда меня будут приветствовать как победителя!"
            play sound ds_sfx_fys
            hfl "Да, зря надеялся."
            hfl "Это же Двачевская, в конце-то концов!"
            hfl "Ничего хорошего от неё ожидать нельзя."
            window hide
            menu:
                "Промолчать":
                    window show
                "Устроить скандал":
                    if skillcheck('authority', lvl_challenging, passive=True, [('ds_karma >= 20', 1)])
                    window show
                    play sound ds_sfx_psy
                    aut "Начинай скандалить, напугай её."
                    me "Да что ты говоришь?! Люди добрые, тут клевещут на меня!"
                    show dv shocked pioneer2 with dspr
                    dv "Что ты делаешь?.."
                    play sound ds_sfx_psy
                    aut "Она удивлена таким твоим ходом."
                    me "Честной народ обвиняют в домогательствах! Вы представьте только!"
                    show mt angry pioneer at right with dissolve
                    show dv scared pioneer2 with dspr
                    dv "Успокойся!"
                    mt "Что тут происходит?"
                    me "Клевета тут происходит! Попытка засудить невиновного!"
                    mt "Так, Алиса, ты снова разыгрываешь парней?!"
                    play sound ds_sfx_mot
                    res "Стоп, это был розыгрыш?!"
                    show dv guilty pioneer2 with dspr
                    dv "Извините..."
                    mt "Так, ладно! Давайте продолжать."
        "Я постарался сохранить лицо."
        "Вежливо встал, наклонил голову, и сказал:"
        me "Поздравляю тебя с победой."
        me "И удачи в полуфинале."
        "Развернулся и ушёл к болельщикам."
        th "Может быть, удастся затеряться в толпе?"

    elif ds_my_rival_1_tour.take == 'mi':
        show mi happy pioneer with dspr
        mi "Ой, какое счастье! А то мне никогда-никогда не везло в картах, я и решила, что это не моё, а тут попросили, и я согласилась."
        mi "Я даже не думала, что сумею победить! Сенечка, ты не обижаешься? А то хочешь, переиграем, мне не жалко! Нет, правда-правда не обижаешься?"
        show mi smile pioneer with dspr
        mi "Просто я не хочу, чтобы мне было хорошо за счёт других, это плохо, мне всегда Па говорил, что счастья на чужих слезах не построишь."
        me "Всё в порядке. Ты здорово играешь, поэтому и победила."
        me "Удачи тебе в полуфинале."
        hide mi with dissolve
        "Пожелал я и, отвернувшись, удалился."

    elif ds_my_rival_1_tour.take == 'us':
        show us laugh pioneer with dissolve
        us "Хы! Продул!"
        "Спасибо, кэп."
        me "Обязательно орать об этом на всю столовую?"
        us "Ну конечно же!"
        show us grin pioneer with dspr
        us "А хочешь, ещё сыграем? {w}На просто так."
        us "Пока остальные тормозят, как раз партию успеем. Ну что?"
        me "В чём подвох?"
        us "Подвоха нет."
        us "Так что, будешь?"
        me "Спасибо, но нет."
        show us dontlike pioneer with dissolve
        us "Зануда! {w}И что, даже отыграться не хочешь?"
        us "Неужели не обидно проиграть девчонке?"
        me "Да мне фиолетово, на самом-то деле."
        th "Кто там что думает и решает, остаётся его достоянием."
        "Мудрый совет на все случаи жизни: болтать поменьше."
        us "Зануда! {w}Зануда."
        "Кричала она."
        show us dontlike pioneer at fright with move
        "А потом резко вскочила и пошла к столику, отведённому под следующую игру."
        us "Просто боишься проиграть ещё раз! Слабак!"
        me "Да, возьми меня ещё раз на «слабо», детка."
        me "Наслаждайся вечером."
        stop music fadeout 3
        hide us with dissolve
        "Я отправился в сторону толпы зрителей. Пришёл мой черёд сменить амплуа."
        play music music_list["my_daily_life"] fadein 3

    elif ds_my_rival_1_tour.take == 'sh':
        show sh normal pioneer with dissolve
        sh "Это была достойная игра. Спасибо."
        if loki:
            me "Взаимно."
        elif herc:
            "Он протянул мне руку, которую я с достоинством пожал."
        else:
            "Мы обменялись рукопожатиями."
            "Всё же крепкая у него хватка для того, кто тяжелее паяльника ничего не поднимает."
        sh "А я пошёл дальше громить вражеские порядки."

    elif ds_my_rival_1_tour.take == 'mz':
        show mz normal glasses pioneer with dissolve
        "Женя пожала плечами и встала из-за стола."
        mz "Похоже, это будет ещё проще, чем мне казалось."
# ---------------------------------------------------- \\Диалоги

    scene bg int_dining_hall_sunset with dissolve
    "А ситуация, между тем, складывалась следующая:"
    pause(.5)
    call ds_day2_1_tour_analizer                                                   # Вызов анализатора 1 раунда
    $ renpy.block_rollback()                                                          # блокируем роллбак
    stop music fadeout 3
    $ ds_drawing_of_detour()                                                       # вызываем рандомизатор пропуска полуфинала и финала
    $ renpy.fix_rollback()                                                          # фиксируем выбор — "откатом" поменять будет нельзя
    jump ds_day2_semifinal                                                     # переход в полуфинал ?

#------------------------------------------------------------------------------------------------
label ds_day2_participate_win_end:
    $ ds_day2_result_tour = 2                                              # Семён выиграл в 1 туре
    if not ds_day2_detour_semifinal:                                       # если не "выигрыш" в 1 туре скипом
        $ persistent.altCardsWonRivals[ds_spr_my_rival] = True         # Выиграли у этого соперника
    $ persistent.altCardsWon1 = True
    $ ds_day2_gamblers_1_tour[places_my_table[0]].winner = True            # Семён выиграл
    $ ds_tournament_state = "1_round_end"                                  # устанавливаем конец 1-го раунда

# -------------------------------------------------------------------------
# ЕСЛИ Славя, Мику или Шурик и НЕ скип тура — итоги ДО диалогов
    if (ds_my_rival_1_tour.take in ['sl','mi','sh']) and not ds_day2_detour_semifinal:
        scene bg int_dining_hall_sunset with dissolve
        "Первый тур закончился."
        "Ситуация, между тем, складывалась следующая:"
        call ds_day2_1_tour_analizer                                                   # вызываем анализатор 1 тура
        $ renpy.block_rollback()                                                          # блокируем роллбак
# -------------------------------------------------------------------------
    pause(1)
    scene bg int_dining_hall_sunset with dissolve
    call ds_day2_summary_poker_round

# ---------------------------------------------------- ДИАЛОГИ
    if ds_my_rival_1_tour.take == 'un':
        if ds_day2_rival_win == 0:
            "У неё не было ничего."
            "А с тем, что было, я бы постеснялся открывать карты."
        else:
            "Лене досталась за эти игры пара-другая хороших карт."
            "К сожалению, для победы этого оказалось недостаточно."
        "Бедная девочка."
        show un sad pioneer with dissolve
        "Она сидела, будто сама не способная поверить в то, что только что произошло."
        if lp_un >= 6 and not ds_day2_detour_semifinal:
            menu:
                "Предложить матч-реванш":
                    $ karma += 5
                    $ lp_un += 1
                    me "Неудачная партия."
                    un "Да…"
                    me "Может, ещё разок?"
                    show un smile pioneer with dspr
                    "Лена улыбнулась."
                    un "Предложение соблазнительное, но я откажусь."
                    me "Почему?"
                    show un shy pioneer with dspr
                    un "Ну…"
                    pause(0.5)
                    if dr:
                        me "Ладно, можешь не говорить."
                        me "Не хочешь — твоё право."
                        me "Не могу же я тебя заставлять."
                        show un smile pioneer with dspr
                        "Лена благодарно улыбнулась."
                        un "Удачи. Я буду болеть за тебя."
                        me "Угу…{w} Спасибо."
                    else:
                        me "Да?…"
                        th "Прости, Лена, но я чуточку поработаю клещами."
                        show un sad pioneer with dspr
                        un "Я не слишком люблю такие игры, и играть в них совсем не умею."
                        un "Поэтому к победе я не рвусь. Ещё до начала решила для себя — будь что будет."
                        un "А реванш… {w}Реванш — это не то."
                        "А на лице явственно читалось — я не хочу больше проигрывать."
                        me "Право твоё. Настаивать не буду."
                        show un cry_smile pioneer with dspr
                        un "Спасибо."
                        show un shy pioneer with dspr
                        un "Лучше я буду болеть за тебя."
                    hide un with dissolve
                    "Она встала из-за стола и исчезла за болельщиками."
                    jump ds_day2_1_tour_end                                                 # В ПОЛУФИНАЛ
                "Ничего не делать":
                    pass
        $ lp_un -= 1
        $ lp_dv += 1
        "Я улыбнулся."
        me "Спасибо за игру!"
        show un shy pioneer with dspr
        un "Н-не за что."
        hide un with dissolve
        "Она встала из-за стола и исчезла за болельщиками."

# ====================================================== Пропускаем часть диалога, если "выиграли" 1 тур скипом
        if not ds_day2_detour_semifinal:
            "А я не мог сдержать ликования."
            th "Я подебил! То есть я победил."
            dreamgirl "Ура! {w=.4}У девочки. {w=.4}В игру, которую ни ты, ни она не знаете. {w}Велико достижение."
            th "Заткнись."
            th "Я буду радоваться победе так, как буду радоваться только когда раскатаю эту рыжую нахалку!"
            dreamgirl "Нет, ну ты и правда герой. Спору нет."
            dreamgirl "Может, следовало дать девочке выиграть? Она и так выглядит не самой счастливой, а ты выбил из-под неё остатки почвы."
            dreamgirl "И как оно по ощущениям? Стоило того?"
            th "Я сказал — заткнись."
            show blinking with dissolve
            if herc or loki:
                "У меня цель — не ободрить каждого сирого, а утереть нос одной рыжей зазнайке!"
                "Хотя, честно сказать, искушение слить партию просто для того, чтобы посмотреть, как она выполнит свои угрозы, достаточно велико. {w}Нет, ну серьезно!"
                scene bg ext_square_sunset
                show prologue_dream
                with fade
                "Завтра мы встаём, идём на линейку, а там уже на трибуне, между Ольгой Дмитриевной и Славей, стоит она."
                show dv grin pioneer2 behind prologue_dream with diam
                "И своим вредным голосом говорит — так, мол, и так, некий Семён, приехать в лагерь ещё не успел, как пошёл подглядывать за мной и даже полапал немного."
                "Да это же реклама такая, что я за неё ещё и приплачивать должен!"
                "В духе «Сёма едет! Прячьте девок!»."
                hide dv with dissolve
            else:
                "Даже если девочки внезапно начнут строить мне глазки, я не собираюсь кому-либо из них сливать партию."
                "Представляю себе, как рыжая стерлядь воплотит свои угрозы."
                scene bg ext_square_sunset
                show prologue_dream
                with fade
                "Например, на утренней линейке."
                show dv grin pioneer behind prologue_dream with dissolve
                "Выйдет вперёд, самодовольно подмигнёт мне и скажет во всеуслышанье:"
                dv "{i}Ольга Дмитриевна, разрешите доложить!{/i}"
                "И далее по тексту."
                "Коллективный суд, а вместе с ним и позор, мне обеспечен."
                dreamgirl "А вот правильный перевод твоего словоблудия — я трясусь за свою шкуру."
                dreamgirl "Волков бояться — в лес не ходить, в курсе?"
                th "Мне и в городе неплохо живётся."
                th "А волки пускай достаются охотникам."
        scene bg int_dining_hall_sunset with dissolve

    elif ds_my_rival_1_tour.take == 'sl':
        "Славя резко вскочила и оперлась кулаками о стол."
        show sl serious pioneer with dspr
        sl "А ты серьёзный противник."
        "Исподлобья процедила она."
        show sl angry pioneer with dspr
        sl "Напомни мне никогда не недооценивать тебя!"
        me "Многие, кто недооценили Семёна, горько пожалели об этом!"
        "Подыграл я."
        show sl smile2 pioneer with dspr
        "Тут она не выдержала и разулыбалась, испортив всю сценку."
        sl "А партия действительно была интересная!"
        if lp_sl >= 6 and not ds_day2_detour_semifinal:
            menu:
                "Хочешь ещё разок?":
                    $ karma += 5
                    show sl smile pioneer with dspr
                    sl "Спасибо"
                    $ lp_sl += 1
                    show sl laugh pioneer with dspr
                    extend ", но… Нет!"
                    sl "Давай-ка ты сам покажешь класс!"
                    "Девочка потрепала меня по плечу и направилась в стан болельщиков."
                    hide sl with dissolve
                    jump ds_day2_semifinal
                "Ничего не делать":
                    pass
        else:
            pass
        "Я улыбнулся."
        me "Спасибо за игру!"
        sl "Тебе спасибо!"
        hide sl with dissolve
        "Кивнув мне, она поднялась и отошла к Ольге Дмитриевне, и у них там завязалась оживлённая беседа."

# ====================================================== Пропускаем часть диалога, если "выиграли" 1 тур скипом
        if not ds_day2_detour_semifinal:
            "Что ж, это была трудная схватка, но я победил."
            th "Идеальное же противостояние — игра, в которой вы оба ничего не понимаете."
            dreamgirl "Ну да, ну да."
            "Пробормотал внутренний голос."
            dreamgirl "Носкиллер рандомный."
            th "Помолчи. Ты ничего не понимаешь."
            th "Это вопрос индивидуального престижа. Я буду двигаться к финалу."
            if ds_result_dv_1_tour == 4:                                                       # Дваче в другом полуфинале
                th "И раскатаю там рыжее хамло!"
            elif ds_result_dv_1_tour == 3:                                                     # Дваче в 1/2 к Семёну
                th "И раскатаю там любого!"
            elif ds_result_dv_1_tour == 2:                                                     # Дваче слетела в 1 туре
                th "Чего не скажешь о Алисе. Значит, это будет лёгкая победа."
            dreamgirl "Надежды… Мечты… Фантазии…"
            th "Ты что, сомневаешься во мне?!"
            dreamgirl "Нет-нет-нет, ты что! {w}Я в тебя верю! Я знаю твой потенциал."
            th "Вот видишь!"
            dreamgirl "Ты слетишь на полпути."
            th "Да ну тебя!"
            if ds_result_dv_1_tour == 4:                                                                # Дваче в другом полуфинале
                "Может быть, это {i}она{/i} слетит на полпути!"
                "Вот возьмёт и проиграет."
                dreamgirl "Надежды… Мечты…"
                th "Ты повторяешься."
                dreamgirl "Просто ты слишком нос задираешь. {w}А, как говорят Великие, — настоящий мастер лишён гордыни."
            elif ds_result_dv_1_tour == 3:                                                              # Дваче в 1/2 к Семёну
                th "Между прочим, у нас сейчас как раз будет шанс стреножить Рыжевскую в полуфинале."
                dreamgirl "Ну да, это нам, конечно, повезло."
                dreamgirl "Но лучше приготовься к суровому испытанию — просто так она тебе победу не отдаст!"
            elif ds_result_dv_1_tour == 2:                                                              # Дваче слетела в 1 туре
                "Я усмехнулся."
                th "А даже если и слечу."
                th "Обращаю твоё внимание, что пока мы тут препирались, Двачевская изволила вылететь в самом первом раунде."
                "Я снял воображаемую шапку и прижал её к груди."
                me "Помянем!"
                show dv angry pioneer2 far at left with dissolve
                "Двачевская оскалилась, но ничего не сказала."

    elif ds_my_rival_1_tour.take == 'dv':
        show dv sad pioneer2 with dspr
        "Алиска облажалась."
        "Ха. Ха. Ха."
        "Её вид — это то, что не купишь ни за какие мастеркарды с визами."
        "Поистине бесценное зрелище!"

# ====================================================== Пропускаем часть диалога, если "выиграли" 1 тур скипом
        if not ds_day2_detour_semifinal:
            if lp_dv >= 6:
                menu:
                    "Ну что, как я тебя?":
                        $ karma += 5
                        if loki or herc:
                            $ lp_dv += 1
                            show dv rage pioneer2 with dspr
                            "Алиса надулась, набычилась…"
                            me "Разделал как Рандом черепаху!"
                            "Не удивлюсь, если она сейчас придумает ещё какую-нибудь гадость, только чтобы уязвить меня."
                            show dv angry pioneer2 with dspr
                            "Но она меня удивила."
                            show dv laugh pioneer2 with dspr
                            dv "А ты хорош! Хорош!"
                            "Расхохоталась она, ткнув меня кулаком в плечо."
                            dv "Пожалуй, будем считать наше пари закрытым."
                            th "Уффф."
                            "Я подавил желание облегчённо вытереть лоб."
                            show dv grin pioneer2 with dspr
                            dv "А то если хочешь, можем ещё на что-нибудь поспорить?"
                            "Я отшатнулся."
                            "Но постарался ответить солидно:"
                            me "Нет. {w}Свою натюрель ты уже поставила на кон."
                            dreamgirl "Дальше только честь девичья! {w}Ну-ка, скажешь это вслух?"
                            "Ага, сейчас. У меня и «натюрель»-то вышла дрожащим голосом."
                            show dv laugh pioneer2 with dspr
                            "Алиса снова рассмеялась, увидев мою реакцию, и поднялась."
                            show dv smile pioneer2 with dspr
                            dv "Удачи тебе."
                        else:
                            "Начал было я, и, чувствуя, как запал иссякает, продолжил уже куда спокойнее:"
                            me "Кажется, я победил."
                            dv "Угу."
                            me "И ты теперь…"
                            show dv sad pioneer2 with dspr
                            pause(.4)
                            show dv guilty pioneer2 with dissolve
                            dv "Да…"
                            dv "Никому я ничего не скажу. {w}Ты победитель."
                            "Алиса выглядела подавленной и какой-то… Обескураженной, что ли."
                            "Кажется, её смутил не столько проигрыш, сколько моя на него реакция."
                            dv "Ладно, бывай."
                        hide dv with dissolve
                        jump ds_day2_1_tour_end
                    "Партия":
                        hide dv with dissolve
                        "Алиса кивнула и молча поднялась из-за стола."
                        pass
            else:
                pass
        if ds_day2_dv_ultim == 1:
            "Кажется, свою малюсенькую проблему с пари я только что успешно решил."

    elif ds_my_rival_1_tour.take == 'mi':
        show mi surprise pioneer with dissolve
        mi "Ой!"
        "Она прижала руки ко рту."
        mi "Я что, я проиграла, да? А то я так и не поняла, что тут делать, только таскала у тебя карты и не отдавала тебе свои."
        show mi upset pioneer with dspr
        "Она покачала головой."
        mi "Какая-то непонятная игра."
        show mi smile pioneer with dspr
        mi "Но всё равно, спасибо, что играл со мной!"
        if lp_mi >= 6 and not ds_day2_detour_semifinal:
            menu:
                "Может, ещё?":
                    $ karma += 5
                    $ lp_mi += 1
                    "Мне понравилось просто сидеть с ней за одним столом."
                    "Тем более, что на нас всё равно никто не смотрел."
                    "Внимание зала сфокусировалось на основных действующих лицах сегодняшнего вечера — Алисе и Ульяне."
                    me "Давай?"
                    show mi shy pioneer with dspr
                    mi "А разве так можно?"
                    me "Нет, но… Кому какое дело?"
                    show el serious pioneer at left with dissolve
                    show mi surprise pioneer with dspr
                    el "Мне есть дело!"
                    "Ответил появившийся из ниоткуда Электроник."
                    el "Ты победил, пожалте за полуфинальный столик!"
                    hide el with dissolve
                    "Блин."
                    "Моя улыбка вышла извиняющейся."
                    me "Тогда увидимся."
                "Всегда рад":
                    "Я улыбнулся."
                    me "Если вдруг захочешь ещё как-нибудь сыграть, обращайся!"
            hide mi with dissolve
            "Мику кивнула и встала из-за стола."
        else:
            "Я улыбнулся."
            me "Всегда пожалуйста!"
            mi "Я пойду, ладно? Хочу увидеть, как ты будешь побеждать! Ты же будешь побеждать, правда? Я буду очень-очень за тебя болеть!"
            "Не в силах сдержать улыбку, я кивнул."
            me "Конечно же, буду."
            mi "Тогда удачи тебе дальше!"
            hide mi with dissolve
            "Она ушла."

# ====================================================== Пропускаем часть диалога, если "выиграли" 1 тур скипом
        if not ds_day2_detour_semifinal:
            "Не могу сказать, что пришлось потрудиться."
            "По мне, так это было чистое везение."
            "Хотя, конечно, моя карма и везение — это слова-антонимы."
            "Я — ходячее олицетворение закона Мэрфи."
            dreamgirl "Ну да, ну да. {w}А то, что ты вытянул билет даже не на миллион, а на новую жизнь, это мы в расчёт как бы не берём, да?"
            th "Ты о попадании в лагерь?"
            th "Я не могу назвать это везением в прямом смысле этого слова."
            dreamgirl "А как это ещё назвать?"
            th "Ну… Просто оказался в ненужном месте в ненужное время."
            dreamgirl "И получил полон рот молодости, лета и сексапильных пионерок."
            th "Знаешь, я не верю, когда много хорошо. {w}Обязательно где-то должен быть подвох."
            dreamgirl "И какой в этот раз?"
            th "Ну, например, может оказаться, что перенос в лагерь является побочным эффектом от попадания под луч космической энергии."
            th "Или вообще это спецслужбы тестировали прототип телепортатора, и у них что-то сбилось в настройках."
            dreamgirl "Не знаю, что ты употребляешь, но отсыпь немного."
            if ds_day2_dv_ultim == 1:
                dreamgirl "К тому же у тебя тут эротическое пари, помнишь?"
                if ds_result_dv_1_tour == 4:                                                                   # Дваче в другом полуфинале
                    th "Помню, помню."
                    th "Но у этого пари все шансы разрешиться совершенно самостоятельно."
                    dreamgirl "Надежды вьюношей питают…"
                    th "Не науки разве?"
                    dreamgirl "В твоём случае именно надежды."
                    dreamgirl "Будь уверен, она доберётся до тебя и порвёт на мелкие клочки, а потом исполнит свою угрозу."
                    th "О, спасибо тебе, мрачный зануда."
                elif ds_result_dv_1_tour == 3:                                                                 # Дваче в 1/2 к Семёну
                    th "Забудешь тут."
                    "Судя по графику, моим противником в полуфинале выступает как раз Двачевская."
                    dreamgirl "Вот свезло так свезло!"
                    dreamgirl "Давай сделаем ей больно!"
                elif ds_result_dv_1_tour == 2:                                                                 # Дваче слетела в 1 туре
                    "Это было бы даже смешно."
                    th "Пари? Какое пари?"
                    th "Пока мы тут о везении судачили, Алиску вышибли на первом же кону."
                    "Я снял воображаемую шапку и прижал её к груди."
                    me "Помянем!"
                    show dv angry pioneer2 far at left with dissolve
                    "Двачевская оскалилась, но ничего не сказала."

    elif ds_my_rival_1_tour.take == 'us':
        show us sad pioneer with dspr
        us "Так нельзя, я только разыгрываться начала!"
        me "Я тоже. {w}Ты проиграла, я победил. Всё честно."
        play music music_7dl["genki"] fadein 3
        us "Переиграем! Только ты теперь поддавайся, слышишь?"
        us "Я должна победить и забрать главный приз!"
        show us angry pioneer with dspr
        us "Ты должен проиграть! Должен! Понял!"
        "Ещё немного, и начну хохотать в голос, настолько потешно это выглядело."

# ====================================================== Пропускаем часть диалога, если "выиграли" 1 тур скипом
        if not ds_day2_detour_semifinal:
            if ds_day2_us_escape:
                us "Ах так! Да я тогда… Я тогда завтра снова сбегу, понял!"
                us "И чисти тогда свою картошку сам! На весь лагерь!"
                "А вот эта угроза была уже посерьёзнее, дежурить по столовой одному мне совершенно не улыбалось."
            else:
                us "Ах так! Тогда я всем расскажу про тебя и Двачевскую!"
                if (ds_day2_dv_ultim == 1) and (loki or herc):
                    me "Мелкая нахалка, не смей! Это только наш с ней спор, ты только разрубала!"
                    show us grin pioneer with dspr
                    "Ульяна только улыбнулась."
                else:
                    me "Ты всем расскажешь то, что она обещала рассказать? В случае моего проигрыша?"
                    "Она кивнула."
            if herc or loki:
                me "А тебе не надо горячего шоколада?"
                show us surp1 pioneer with dspr
                us "Что?"
                me "Я говорю, можешь делать как хочешь, но ты проиграла."
                show us dontlike pioneer with dspr
                me "А карточный долг священен. Всё, брысь отсюда, я к победе иду."
                "Она надулась, но сделала, как я сказал."
                hide us
                with flash_red
                "Правда, попутно наступила мне на ногу — пускай."
                stop music fadeout 3
                "Я был благодушен и простил ей эту маленькую шалость."
            if dr:
                me "Ладно"
                "Я вздохнул."
                me "Уговорила. Дам тебе ещё один шанс."
                show el serious pioneer at left with dissolve
                "Её крики привлекли внимание Электроника."
                el "Никаких переигровок!"
                el "Один матч, игра до двух побед, проигравший выбывает."
                "Ульяна кинула на Электроника недвусмысленный взгляд, означающий для него грядущие неприятности."
                stop music fadeout 3
                "Но хотя бы с меня внимание переключила, и я вздохнул с облегчением."
        else:
            me "Можешь делать как хочешь, но ты проиграла."
            me "А карточный долг священен. Всё, брысь отсюда, я к победе иду."
            "Она надулась, но сделала, как я сказал."
            hide us
            with flash_red
            "Правда, попутно наступила мне на ногу — пускай."
            stop music fadeout 3
            "Я был благодушен и простил ей эту маленькую шалость."
        play music music_list["my_daily_life"] fadein 5

    elif ds_my_rival_1_tour.take == 'sh':
        "Шурику не повезло."
        "Но, похоже, его больше интересовал сам процесс проверки новых правил и алгоритмов, чем победа."
        "Настоящий фанатик своего дела."
        show sh normal pioneer with dissolve
        sh "Ты очень хорошо умеешь приспособиться к новым правилам игры."
        "Похвалил он."
        hide sh with dissolve
        "И, пожав мне руку, удалился."


# ====================================================== Пропускаем часть диалога, если "выиграли" 1 тур скипом
        if not ds_day2_detour_semifinal:
            "Наверное, отправился изобретать очередную дикую штуку или строчить очерк об оной в стенгазету."
            "Я с удивлением поймал себя на мысли, что нахожу Шурика и Славю очень похожими."
            "Оба увлечены своим делом, оба дико ответственные."
            "И оба почти не отдыхают."
            th "Наверное, стоило бы сдать партию, я раздолбай, я и так способ ляжки потянуть найду, а он, похоже, сейчас уйдёт обратно сидеть в клуб."
            "Так и лето пройдёт, а он всё будет бледным."
            dreamgirl "Эй!"
            th "Что?"
            dreamgirl "Это у тебя там что за гадость? {w}Совесть? {w}Выброси её немедленно."
            dreamgirl "Вечно всякую дрянь с пола поднимаешь."
            if ds_day2_dv_ultim == 1:
                th "Что такое?"
                dreamgirl "Напоминаю, что мы не просто так тут штаны просиживаем."
                dreamgirl "У нас есть одна цель! Показать одной рыжей террористке, чего стоит слово!"
                if ds_result_dv_1_tour == 4:                                                           # Дваче в другом полуфинале
                    dreamgirl "И особый воспитательный момент несёт то, что мы умоем её в игре по её же правилам!"
                    th "Если она проиграет за другим столом, то никого мы не умоем."
                    dreamgirl "Есть подозрение, что такие, как она, так просто не сдаются."
                    th "Ну, если встретимся в финале, я её обыграю."
                    dreamgirl "С таким настроем ты никого не обыграешь. {w}Соберись!"
                elif ds_result_dv_1_tour == 3:                                                         # Дваче в 1/2 к Семёну
                    th "Ага, прямо сейчас и покажем."
                    dreamgirl "Здорово! Расправа оказалась куда ближе, чем мне казалось!"
                    if ds_day2_us_escape:
                        dreamgirl "Она просила сделать ей посопротивляться, исполни её просьбу."
                elif ds_result_dv_1_tour == 2:                                                         # Дваче слетела в 1 туре
                    "Заниматься оценками слов, честно говоря, было уже поздновато."
                    "Я посмотрел на таблицу участников — Алиса вылетела после первой же партии."
                    th "Не{w=.3} по{w=.2}вез{w=.3}ло."
                    th "Покойся с миром, дорогая бандитка."
                    th "Я отомщу за тебя."
            else:
                th "Что в этом плохого?"
                dreamgirl "То, что совесть рождает сомнения, а сомнения ведут к поражению."
                th "Я в курсе."
                th "Вот только нужна она мне — победа?"
                dreamgirl "Ты ещё начни лепетать чепуху про то, что «главное — участие»."
                "Фыркнул внутренний голос."
                th "Скажу — на всё воля Рандома."

    elif ds_my_rival_1_tour.take == 'mz':
        show mz normal glasses pioneer with dissolve
        "Реакция Жужи позабавила."
        mz "Аллилуйя!"
        show mz angry glasses pioneer far with dspr
        pause(0.5)
        hide mz with moveoutleft
        "Хлопнув по столу, она поднялась и исчезла."
        "Наверняка помчалась к своим лучшим друзьям — книгам."
        "Вот уж кому много не надо для счастья."

# ---------------------------------------------------- \\ Диалоги


# -------------------------------------------------------------------------
label ds_day2_1_tour_end:
# ЕСЛИ НЕ Славя, Мику или Шурик ИЛИ при скипе — итоги после диалогов
    if (ds_my_rival_1_tour.take not in ['sl','mi','sh']) or ds_day2_detour_semifinal:
        scene bg int_dining_hall_sunset with dissolve
        "Первый тур закончился."
        "Ситуация, между тем, складывалась следующая:"
        call ds_day2_1_tour_analizer                                                     # вызываем анализатор 1 тура
        $ renpy.block_rollback()                                                          # блокируем роллбак
    scene bg int_dining_hall_sunset with dissolve
    stop music fadeout 3
# -------------------------------------------------------------------------

    "Ладно, это всё лирика."
    jump ds_day2_semifinal                                             # переход в полуфинал

#-------------------------------------------------------------------------------------------------
label ds_day2_semifinal:
    stop music fadeout 1
    scene bg int_dining_hall_sunset with dissolve
    show el smile pioneer at left with dissolve
    play music music_list["get_to_know_me_better"] fadein 2
    el "Итак!"
    "Подал голос Электроник, явно гордящийся своей ролью мастер-церемониймейстера."
    el "Первый тур окончен, победители встречаются во втором туре!"

    $ ds_tournament_state = "semifinal_start"                                                      # устанавливаем начало полуфинала
#-------------------------------------------------------------------------------------------------
    if ds_day2_result_tour != 1:                                                                       # если не продули в 1 туре
        $ ds_day2_my_win = ds_day2_rival_win = ds_day2_game_played_out = 0                           # обнуляем результат игр
        $ ds_my_rival_semifinal = ds_get_me_rival(ds_day2_gamblers_semifinal)                        # узнаём своего соперника

        $ ds_name_my_rival_i = ds_my_rival_semifinal.name['i']                                        # узнаём ИМЯ своего соперника (в именительном падеже)
        $ ds_name_my_rival_r = ds_my_rival_semifinal.name['r']                                        # узнаём ИМЯ своего соперника (в родительном падеже)
        $ ds_name_my_rival_d = ds_my_rival_semifinal.name['d']                                        # узнаём ИМЯ своего соперника (в дательном падеже)
        $ ds_name_my_rival_v = ds_my_rival_semifinal.name['v']                                        # узнаём ИМЯ своего соперника (в винительном падеже)
        $ ds_name_my_rival_t = ds_my_rival_semifinal.name['t']                                        # узнаём ИМЯ своего соперника (в творительном падеже)

        $ ds_spr_my_rival = ds_my_rival_semifinal.take                                                # получаем спрайт соперника — заголовок
        $ ds_emo_my_rival = ds_sprites_rival_recognition[ds_spr_my_rival][0]                         # эмоция (строка)
        $ ds_acc_my_rival = ds_sprites_rival_recognition[ds_spr_my_rival][1]                         # аксессуар (строка)
        $ ds_clot_my_rival = ds_sprites_rival_recognition[ds_spr_my_rival][2]                        # одежда (строка)
        $ ds_pos_my_rival = ds_sprites_rival_recognition[ds_spr_my_rival][3]                         # положение

        $ ds_nick_my_rival = ds_my_rival_semifinal.nick                                               # получаем характер соперника (для диалога)

        if ds_my_rival_1_tour.take == 'un':
            hide el with dissolve
            "Лена скромно стояла в сторонке и следила за событиями турнира."
            show un smile2 pioneer far at right with dissolve
            "При этом на лице её не было ни злости, ни обиды, ни чего-либо в этом духе."
            "Напротив, она искренне поддерживала меня и остальных ребят."
            hide un with dissolve
            "Что ж, убедившись в том, что не обидел её, я немного расслабился."
    "Между тем, в таблице уже появились имена участников второго тура."
    call show_tournament_table                                                                      # "показали таблицу"
    $ ds_mstt = 0
    if ds_day2_result_tour != 1:                                                                       # если не продули в 1 туре
        $ places_my_table = ds_get_my_table(ds_day2_gamblers_semifinal)                               # Стол Семёна = [место Семёна, место соперника, № их стола]
    else:                                                                                               # продули в 1 туре
        $ ds_table_no = 5
    "И если верить этой таблице, то в полуфинале встречаются четыре игрока."
    $ ds_random_box_1 = range(1,len(ds_table_affiliation)+1)                                      # черный ящик — список от 1 до длины представлений столов +1
    while ds_table_no <= 6:                                                                        # перебираем столы от 5 по 6
        $ sitting_at_table,gambler_upper,gambler_lower,must_taunt = ds_declare_tournament_tables(ds_table_no)  #расссадка, игроки, таунты — по номеру стола
        "%(sitting_at_table)s"
        call show_tournament_table
        extend " %(gambler_upper)s"                                                                 # выводим в окно имя верхнего игрока
        call show_tournament_table
        extend " и %(gambler_lower)s."                                                              # выводим в окно имя нижего игрока
        if must_taunt != None:                                                                      # если таунт есть
            "%(must_taunt)s"                                                                        # выводим его
        if ds_day2_result_tour != 1:                                                                       # если не продули в 1 туре
            if ds_table_no != places_my_table[2]:                                                          # если номер стола — НЕ свой
                $ ds_day2_gamblers_semifinal[2*(ds_table_no-4)-renpy.random.choice([1,2])].winner = True  # тогда один из игроков (рандомно) — победитель в этапе
                $ renpy.block_rollback()
        $ ds_table_no += 1
    if (ds_day2_detour_number != 0):                                                               # если выбрали конкретного соперника для финала
        $ ds_day2_gamblers_semifinal[2].winner = False                                             # его соперник в полуфинале проигрывает
        $ ds_day2_gamblers_semifinal[3].winner = True                                              # а он сам выигрывает в полуфинале

    if ds_day2_result_tour == 1:                                                               # если продули в 1 туре
        scene bg int_dining_hall_sunset with joff_r
        $ ds_tournament_state = "semifinal_end"                                                # устанавливаем конец полуфинала
        $ ds_drawing_of_detour_semifinal()
        $ renpy.fix_rollback()                                                                  # фиксируем выбор — "откатом" поменять будет нельзя
        jump ds_day2_semifinal_detour                                                          # и переходим в конец проигрыша в 1/2

    pause (0.3)
    scene bg int_dining_hall_sunset with dissolve


# ---------------------------------------------------- ДИАЛОГИ
    if ds_my_rival_semifinal.take == 'un':
        show un shy pioneer with dspr
        me "Удачи нам обоим?"
        show un smile pioneer with dspr
        pause(.3)
        show un shy pioneer with dspr
        un "Д-да…"
        "Она попыталась улыбнуться, но тут же снова смешалась и смолкла."

    elif ds_my_rival_semifinal.take == 'sl':
        show sl smile pioneer with dspr
        sl "Ух! Не думала, что так далеко зайду!"
        "Улыбнулась Славя."
        me "Это не значит, что я теперь буду тебе поддаваться!"
        show sl laugh pioneer with dspr
        sl "И не надо!"
        "Рассмеялась девочка."
        sl "Пускай победит сильнейший!"

    elif ds_my_rival_semifinal.take == 'dv':
        "Ехидство и озорство во взгляде Алисы не сулило ничего хорошего для меня."
        show dv grin pioneer2 with dspr
        dv "Я придумала новое правило."
        "Прошептала она, наклонившись ко мне."
        me "Какое ещё правило?"
        dv "Если ты меня победишь сейчас, но проиграешь в финале — я всё равно всё всем расскажу."
        me "Эй, так нечестно!"
        show dv laugh pioneer2 with dspr
        dv "Хотя ты не победишь."
        "Рассмеялась девочка."
        dv "Тебе конец!"

    elif ds_my_rival_semifinal.take == 'mi':
        stop music fadeout 2
        show mi normal pioneer far with dissolve
        "Рандом послал мне в оппоненты Мику."
        play music music_7dl["tellyourworld"] fadein 3
        show mi normal pioneer with dspr
        "Пионерка заняла место напротив и спросила."
        show mi upset pioneer with dspr
        mi "Скажи, Сенечка, а какой у тебя размер?"
        "Я аж поперхнулся воздухом."
        dreamgirl "Ну, не стесняйся ты так! Девочка {b}хочет{/b} знать!"
        th "Это не те вещи, которые следует обсуждать на людях."
        dreamgirl "А где же ещё? Пионерке одиноко и тоскливо, она хочет тепла и ласки."
        th "Ты вообще о чём-нибудь другом думаешь?"
        dreamgirl "Думаю, конечно, но об этом интереснее!"
        me "Да я не…"
        show mi happy pioneer with dspr
        mi "Не знаешь? Не страшно. У меня в клубе есть всё необходимое."
        mi "Снимем мерки после турнира. А когда закончим, можем поиграть на гитарах!"
        if not ('music' in list_joined_clubs_7dl):
            show mi smile pioneer with dspr
            mi "Ты же умеешь играть, да?"
            show mi grin pioneer with dspr
            extend " Если нет, я тебя научу!"
        dreamgirl "Тебе однозначно понравится, соглашайся!"
        dreamgirl "Она аккуратно возьмёт в одну руку твой гриф, в другую каподастр…"
        dreamgirl "И поднимет голоску тональность!"
        show mi shocked pioneer with dspr
        mi "Ой, Сенечка, ты вдруг так покраснел. Тебе жарко? Или плохо? Может позвать ме…"
        show mi scared pioneer with dspr
        me "Не надо!" with vpunch
        "Замечательно. Испугал девушку и пустил петуха чуть-ли не на всю столовую."
        dreamgirl "Лох — это судьба."
        "Выдохнув, я попробовал ещё раз, уже спокойнее."
        show mi surprise pioneer with dspr
        me "Прости, что накричал. Со мной всё в порядке."
        show mi smile pioneer with dspr
        mi "Ничего страшного, Сенечка. Я всё понимаю."
        "Действительно ли понимаешь?"
        "Повезло, что Мику такая отходчивая."
        dreamgirl "Просто уточню — ты в самом деле собрался променять юное и мягкое на серое и унылое?"
        th "А сам как думаешь?"
        dreamgirl "Какой же ты…" # дегенерат, пиздец просто!
        me "Если найдёшь меня после турнира, схожу с тобой в клуб."
        show mi grin pioneer with dspr
        mi "Отлично! Ты будешь самым красивым на дискотеке!"
        "Дискотеке? А причём тут дискотека?"
        dreamgirl "Рубашку тебе пошить по размеру хотят, балбес."
        th "Почему сразу не сказал, Штирлиц?"
        dreamgirl "Был слишком далеко от провала."
        dreamgirl "Главное, сам не облажайся, когда будешь позировать для юной девы голышом."
        show mi smile pioneer with dspr
        stop music fadeout 2
        me "Кхм… Давай начнём игру уже."
        play music music_list["get_to_know_me_better"] fadein 3

    elif ds_my_rival_semifinal.take == 'us':
        stop music fadeout 2
        show us grin pioneer with dissolve
        us "Будешь поддаваться, будешь?"
        play music music_list["i_want_to_play"] fadein 1
        "С улыбкой до ушей она уставилась на меня."
        us "Я хочу всех победить!"
        if (ds_day2_dv_ultim == 1) and (loki or herc):
            me "Не буду."
            "Я отрицательно покачал головой."
            me "У нас же спор, помнишь?"
            if loki or herc:
                extend " Ты разбивала!"
            show us sad pioneer with dspr
            us "Спор — это да, но…"
            show us grin pioneer with dspr
        us "Играть будем по моим правилам!"
        me "Каким ещё правилам?!"
        us "Простым!"
        me "А-а-а! Очень информативно."
        us "А то!"
        show us laugh pioneer with dspr
        "Вдоволь насладившись моей кислой физиономией, Ульяна начала объяснять."
        show us smile pioneer with dspr
        us "Всё просто: ты отдаёшь мне хорошие карты, а я тебе — какие захочу."
        me "А мне с этого какая выгода?"
        us "Ты поможешь ребёнку выиграть и получишь…"
        show us normal pioneer with dspr
        "Ульяна задумалась."
        "Похоже есть не так много вещей, с которыми мелкая готова расстаться."
        us "Конфеты. Я дам тебе конфеты. " #(хочется написать «дружбу» или «и дружбу», но в дальнейшем это никак не проявит себя. Досадно.)
        me "Равноценный обмен…"
        show us grin pioneer with dspr
        us "Ну вот, рада, что мы пришли к кон…"
        show us calml pioneer with dspr
        extend " кансе…"
        show us angry pioneer with dspr
        extend " кунсекасу…"
        if herc:
            us "Что ты ржёшь?!"
            me "Тебе лучше не знать."
            us "А я хочу знать."
            us "Говори, новичок!"
            show us smile pioneer with dspr
            us "Или наутро проснёшься с муравьями под одеялом!"
            th "Внушительная угроза."
            me "Ладно, давай на ушко."
            show us grin pioneer close with dissolve
            us "То-то же!"
            "Ульянка подалась мне навстречу."
            "И когда между нами остались считанные сантиметры…"
            with hpunch
            show us surp2 pioneer with dspr
            us "Ай!"
            show us angry pioneer with dspr
            us "Ах ты!…"
            "Мелкая оказалась не промах: не растерялась и ударила лбом в лоб." with vpunch
            "Не сильно. Из этого положения у неё не вышло бы иначе."
            "Несколько секунд мы буравили другу друга взглядом."
            show us laugh pioneer with dspr
            "А потом оба не удержались и засмеялись."
            me "Ладно, давай играть уже, а то на нас вожатая косится."
            us "А муравьёв всё равно жди."
            th "Надеюсь, что она всё же шутит. Или забудет."
        else:
            me "Консенсусу."
            show us dontlike pioneer with dspr
            me "Не пытайся в сложные слова, рано тебе ещё."
            "И почему люди считают, что использование сложных слов делает их умнее в глазах других?"
            show us upset pioneer with dspr
            us "Бу-бу-бу. Вредина."
            me "Давай играть уже."

    elif ds_my_rival_semifinal.take == 'sh':
        show sh normal pioneer with dissolve
        sh "Это будет достойная схватка."
        "Кивнул он."
        me "Не думай, что я буду тебе поддаваться."
        show sh smile pioneer with dspr
        sh "И ты тоже не надейся!"
        me "Тогда к оружию!"

    elif ds_my_rival_semifinal.take == 'mz':
        "Серьёзно, как Жужа победить-то умудрилась, с таким отношением к игре?"
        show mz normal glasses pioneer with dissolve
        mz "Слушай. Как там тебя."
        "Начала она."
        me "Семён."
        mz "А, вот. Семён."
        mz "Семён, хочешь, я скажу, что ты победил, и пойду уже?"
        me "А так разве можно?"
        mt "Нет, нельзя! Играйте давайте!"
        "Крикнула со стороны болельщиков вожатая."
        show mz angry glasses pioneer with dspr
        "Чертыхнувшись, Женя отказалась от своих планов."
# ---------------------------------------------------- /ДИАЛОГИ

# ----------------------------------------------------------------------------------------------------
    if ds_day2_detour_semifinal:                                           # если пропуск полуфинала
        scene bg int_dining_hall_sunset with dissolve2
        pause(1.0)
        if not ds_day2_detour_final:                                       # Если НЕ пропуск финала
            jump ds_day2_semifinal_fail_end                            # на поражение в 1/2 финала
        elif ds_day2_detour_final:                                         # Если выбрано "проиграть в финале"
            jump ds_day2_semifinal_win_end                             # на победу в 1/2 финала

# ----------------------------------------------------------------------------------------------------
label ds_day2_semifinal_start:                                                     # начало полуфинала
    call ds_day2_stipulation                                                       # определяемся, кто первый ходит

    # первоначальные "настройки" игроков — могут меняться по результатам игры
    # 'defense' — защита, 'gamble' — риск, 'succumb' — слив, 'foolplay' — рандом
    # вероятность ошибки: 1 = 80%, …, 4 = 20%, 5 — ошибок нет.

    if ds_my_rival_semifinal.take == 'un':                                                    # Лена
        if ds_day2_dv_ultim != 1:                                                              # если с Алисой не спорить
            $ ds_day2_gambler_behavior = 'gamble'                                              # пытается рискнуть
            $ ds_day2_gambler_skill = 3                                                        # правда, ошибок многовато — 40%(3)
        else:
            $ ds_day2_gambler_behavior = 'succumb'                                             # Если поспорить — то также игра в поддавки
            $ ds_day2_gambler_skill = 4                                                        # может ошибиться  — 20%(4)
    elif ds_my_rival_semifinal.take == 'sl':                                                  # Славя будет защищаться, ошибок — 20%(4)
        $ ds_day2_gambler_behavior = 'defense'
        $ ds_day2_gambler_skill = 4
    elif ds_my_rival_semifinal.take == 'dv':                                                  # Алиса рискует, ошибок — 20%(4)
        $ ds_day2_gambler_behavior = 'gamble'
        $ ds_day2_gambler_skill = 4
    elif ds_my_rival_semifinal.take == 'mi':                                                  # Мику будет защищаться, ошибок — 20%(4)
        $ ds_day2_gambler_behavior = 'defense'
        $ ds_day2_gambler_skill = 4
    elif ds_my_rival_semifinal.take == 'us':                                                  # Ульяна будет защищаться по-своему
        $ ds_day2_gambler_behavior = 'defense'
        $ ds_day2_gambler_skill = 3                                                            # ошибок — 40%(3)
    elif ds_my_rival_semifinal.take == 'sh':                                                   # Шурик экспериментирует, так что может и рискнуть, и защищаться, и слить; ошибки 20%(4)
        $ ds_day2_gambler_behavior = renpy.random.choice(['defense', 'gamble'])                # у него своя кухня — набор из возможных вариантов
        $ ds_day2_gambler_skill = 4
    elif ds_my_rival_semifinal.take == 'mz':                                                  # Женя играет рандомно, как в классике, ошибки = 5
        $ ds_day2_gambler_behavior = 'foolplay'
        $ ds_day2_gambler_skill = 5

label ds_day2_semifinal_re_game:                                                           # игра в полуфинале — сюда возвращаемся на повторную игру
    $ ds_my_poker_hand = None
    $ ds_rival_poker_hand = None

    if ds_day2_walk == 1:
        $ VISIBLE = True
        $ INVISIBLE = True
    else:
        $ VISIBLE = True
        $ INVISIBLE = False

    python:
        dialogs = {
                        (0, 'win','jump'):'ds_day2_one_play_win',
                        (0, 'fail','jump'):'ds_day2_one_play_fail',
                        (0, 'draw','jump'):'ds_day2_one_play_draw'
                    }
        generate_cards_alt('bg hall', dialogs)


# ****************   НОВЫЕ  СОПЕРНИКИ   ******************************************

        if ds_my_rival_semifinal.take == 'un':
            rival = CardGameRivalWiseUsual(un_avatar_set, u"Лена", ds_day2_gambler_behavior, ds_day2_gambler_skill)
        elif ds_my_rival_semifinal.take == 'sl':
            rival = CardGameRivalWiseUsual(sl_avatar_set, u"Славя", ds_day2_gambler_behavior, ds_day2_gambler_skill)
        elif ds_my_rival_semifinal.take == 'dv':
            rival = CardGameRivalWiseUsual(dv_avatar_set, u"Алиса", ds_day2_gambler_behavior, ds_day2_gambler_skill)
        elif ds_my_rival_semifinal.take == 'mi':
            rival = CardGameRivalWiseUsual(mi_avatar_set, u"Мику", ds_day2_gambler_behavior, ds_day2_gambler_skill)
        elif ds_my_rival_semifinal.take == 'us':
            rival = CardGameRivalWiseLikeUS(us_avatar_set, u"Ульяна", ds_day2_gambler_behavior, ds_day2_gambler_skill)
        elif ds_my_rival_semifinal.take == 'sh':
            rival = CardGameRivalWiseUsual(sh_avatar_set, u"Шурик", ds_day2_gambler_behavior, ds_day2_gambler_skill)
        elif ds_my_rival_semifinal.take == 'mz':
            rival = CardGameRivalWiseUsual(mz_avatar_set, u"Женя", ds_day2_gambler_behavior, ds_day2_gambler_skill)

# ************************************************************************************

    $ ds_hint_poker = ds_hint_poker_contractual                                           # подсказки комбинаций — по просмору правил
    jump cards_gameloop_wise_alt                                                            # переход карточный стол

#-------------------------------------------------------------------------------------------------
label ds_day2_semifinal_fail_end:
    $ ds_day2_result_tour = 11                                                 # Семён проиграл в полуфинале
    $ persistent.altCardsWon1 = True

    $ ds_day2_gamblers_semifinal[places_my_table[1]].winner = True            # соперник выиграл
    $ ds_rival_final = ds_day2_gamblers_semifinal[places_my_table[1]]         # и он выходит в финал
    $ ds_day2_gamblers_semifinal[places_my_table[0]].winner = False            # Семён проиграл
    $ ds_tournament_state = "semifinal_end"                                   # устанавливаем конец полуфинала
    scene bg int_dining_hall_sunset with dissolve
    call ds_day2_summary_poker_round

# ---------------------------------------------------- ДИАЛОГИ;
    if ds_my_rival_semifinal.take == 'un':
        $ lp_un += 1
        stop music fadeout 2
        if ds_day2_dv_ultim == 1:
            show un serious pioneer at center with dissolve
            un "И зачем ты это сделал?"
            play music music_7dl["areyouabully"] fadein 3
            "Спросила она, смотря на меня с явно выраженной неприязнью."
            me "Извини?"
            un "Думаешь, я не слышала о вашем с Алисой маленьком «пари»?"
            un "Так и выигрывал бы!"
            if ds_day2_walk == 1:
                th "Да я и планировал. Даже карты пометил. Но…"
            th "Как-то не срослось."
            me "Да что теперь-то говорить? Я проиграл, ты победила. Удачного вечера."
            "Тем более, что мы не ведём переговоров с террористами."
        else:
            show un angry pioneer with dissolve
            un "Ты поддался, да?"
            play music music_7dl["areyouabully"] fadein 3
            "Лена наклонила голову набок и сверлила меня неприязненным взглядом."
            un "Вместо того, чтобы нормально играть, ты устроил поддавки."
            me "Тебе показалось."
            "Усмехнулся я."
        un "Прошу разрешить нам сыграть ещё раз!"
        "В наступившей тишине попросила Лена."
        un "Мой соперник поддавался."
        show dv grin pioneer2 far at fleft with dissolve
        dv "Поддавался — значит, сам дурак."
        "Фыркнула Алиса."
        "Ну да, она-то знает, что на кону."
        show un angry2 pioneer with dspr
        un "А ты бы вообще молчала! Это всё из-за тебя! Снова!"
        stop music fadeout 3
        show un sad pioneer with dspr
        "Она спрятала лицо в ладонях, а я поднялся из-за стола, чувствуя себя ракетной ступенью, что вывела на орбиту очередной шаттл."
        hide dv
        hide un
        with dissolve
        pause(0.3)
        play music music_list["get_to_know_me_better"] fadein 1

    elif ds_my_rival_semifinal.take == 'sl':
        show sl normal pioneer with dissolve
        sl "И снова меня заставляют заниматься непонятными вещами."
        me "Прости?"
        th "Заговаривается, что ли?"
        show sl serious pioneer with dspr
        "Славя отмахнулась."
        sl "Не обращай внимания, просто мысли вслух."
        me "Ясно. Что ж, тогда удачи тебе в финале!"
        sl "Точно."
        show sl sad pioneer with dissolve
        sl "Зачем я вообще играть согласилась?"
        me "Не любишь карты?"
        sl "Нет. Я другие игры люблю."
        "Она сморщилась, будто съела нечто кислое."
        "А я поднялся — меня ждала волнительная роль болельщика за финалистов."

    elif ds_my_rival_semifinal.take == 'dv':
        if ds_day2_dv_ultim == 1:
            show dv grin pioneer2 with dspr
            dv "Как думаешь, будет лучше, если я сама с трибуны объявлю?"
            "Алиса злорадствовала так, будто я был её кровный враг с традициями пяти колен."
            dv "Или лучше вытащить тебя на трибуну вместе с собой?"
            if ds_day2_walk == 1:
                th "Лучше объясни мне, откуда ты знаешь {i}мой собственный{/i} крап."
            me "Не получится."
            show dv surprise pioneer2 with dspr
            dv "Почему?"
            me "Потому что, если ты вытащишь меня на трибуны, никто в жизни не поверит, что мне хватило сил справиться с тобой и — что ты там говорила?"
            show dv laugh pioneer2 with dspr
            dv "Да. Ну…"
            "Ей пришла в голову мысль."
            dv "Я скажу, что ты меня связал."
            me "Колготками!"
        "Алиса весело расхохоталась, а я поднялся."
        "Господи, почему все стервы такие рыжие?"
        "Неужели у меня где-то написано «издеваться сюда»?"
        me "Играй. Тебя финал ждёт."
        me "А если проиграешь, то стыд тебе и позор."
        "Развернулся и ушёл к болельщикам."

    elif ds_my_rival_semifinal.take == 'mi':
        show mi happy pioneer with dspr
        mi "Ура! Я снова побеждаю!"
        mi "Да я, да я… Я супер-Мику!"
        me "О господи, где вы откопали это чудо?"
        "Пробормотал я."
        show mi smile pioneer with dspr
        mi "Я хочу отметить свою победу каким-нибудь очень хорошим делом или даже поступком, но мне что-то ничего в голову не приходит, может быть, ты, Сенечка, что-нибудь посоветуешь?"
        "Человек-пулемёт."
        th "Временами нами неминуемо на кон были выкинуты карты, да масти не те…"
        th "Солнышко, милая, ну хватит уже трещать, я же ничего плохого не сделал тебе, за что ты меня тут расстреливаешь!"
        me "Не знаю."
        "Угрюмо ответил я."
        "Поражение меня несколько подкосило."
        show mi happy pioneer with dspr
        mi "Ой, а я знаю, кажется! Да! Мне только что идея в голову пришла! Я…"
        show mi happy pioneer far with dissolve
        "Она забралась на стол."
        mi "Я вам спою!"
        "Она набрала в грудь воздуха, и…"
        show dv angry pioneer2 at cleft with easeinleft
        show mt angry pioneer at cright with easeinright
        with vpunch
        "Неизвестно откуда взявшиеся Ольга и Алиса, взревев в унисон, ринулись стаскивать её на пол."
        "Усмехнувшись, я встал из-за стола и отошёл к болельщикам."

    elif ds_my_rival_semifinal.take == 'us':
        if (ds_day2_dv_ultim == 1) and (loki or herc):
            show us laugh pioneer with dissolve
            us "Ура-ура-ура, прекрасная игра! Красив я и умён, и ловок, и силён!"
            "Прокричала она."
            me "Ты ещё фляк сделай от радости."
            th "Почему ей так нравится факт, что теперь меня освистают на весь лагерь?"
            me "Не знал, что твоим кумиром является Винни Пух со своими кричалками."
            us "А как же!"
            if ds_day2_us_escape:
                us "У меня и медведь есть!"
                "Она показала язык."
                us "Но не узнать лучшее в мире приведение… стыд и срам!"
        hide us with dissolve
        "Я поморщился и встал."
        us "Неудачникам привет."
        "Крикнула она мне в спину."
        "А я не среагировал. Привык."

    elif ds_my_rival_semifinal.take == 'sh':
        show sh normal pioneer with dissolve
        sh "Жаль, что так быстро всё закончилось."
        "С достоинством кивнул Шурик."
        sh "Идеально, если бы нам дали партий десять с одной колоды, чтобы можно было вычислить логику."
        me "И сидеть до утра?"
        me "Я-то не против, да кто ж нам позволит."
        "Я кивнул и поднялся из-за стола."

    elif ds_my_rival_semifinal.take == 'mz':
        show mz normal glasses pioneer with dissolve
        mz "Упс."
        "Пробормотала она себе под нос."
        mz "Специально же карты не открывала. Здесь вообще как-нибудь проиграть возможно?"
        me "Как видишь."
        "Сказал я и встал из-за стола."
# ---------------------------------------------------- \\ Диалоги

label ds_day2_semifinal_detour:
    pause(.5)
    scene bg int_dining_hall_sunset with dissolve
    "В полуфинале был такой расклад:"
#-------------------------------------------------------------------------------------------------
    call ds_day2_semifinal_analizer                                                  # анализ полуфинала
    $ renpy.block_rollback()                                                          # блокируем роллбак
    jump ds_day2_final                                 # и смотрим финал

#-------------------------------------------------------------------------------------------------
label ds_day2_semifinal_win_end:
    $ ds_day2_result_tour = 12                                             # Семён выиграл в полуфинале
    if not ds_day2_detour_final:                                           # если не "выигрыш" в полуфинале скипом
        $ persistent.altCardsWonRivals[ds_spr_my_rival] = True         # Выиграли у этого соперника

    $ persistent.altCardsWon2 = True
    $ ds_day2_gamblers_semifinal[places_my_table[0]].winner = True             # Семён выиграл
    $ ds_rival_final = ds_day2_gamblers_semifinal[places_my_table[0]]         # и он выходит в финал
    $ ds_day2_gamblers_semifinal[places_my_table[1]].winner = False            # Соперник проиграл
    $ ds_tournament_state = "semifinal_end"                                    # устанавливаем конец полуфинала
    scene bg int_dining_hall_sunset with dissolve
    call ds_day2_summary_poker_round

# ---------------------------------------------------- ДИАЛОГИ
    if ds_my_rival_semifinal.take == 'un':
        stop music fadeout 2
        "Лена старалась изо всех сил."
        play music music_list["lets_be_friends"]
        "Видно было, что ей понравилось то, как её восприняли всерьёз."
        "Жаль только, что иногда даже старания изо всех сил решительно недостаточно."
        show un sad pioneer with dissolve
        un "Досадно. У меня почти получилось."
        "Вот они злобятся, и кричат, и ножками мотылькают, и невдомёк им, почему окружающим так смешно."
        me "Хочешь реванш?"
        show un normal pioneer with dspr
        un "Нееет, реванш — это не то."
        "Вздохнула она."
        if ds_day2_walk == 1:
            th "Это ничего, знала бы ты, за счёт чего я тебя обыграл…"
        me "То есть всё нормально?"
        "Она кивнула."
        "Что она ещё могла сделать?"
        th "А она азартная."
        "Отметил я для себя."
        th "То есть, в случае чего, её можно взять на слаб{b}о{/b}?"
        "Кого-то она мне напомнила этой своей импульсивностью."
        "И когда я понял кого именно, то долго тряс головой, отгоняя глупые мысли."
        show un shy pioneer with dspr
        un "Почему ты смотришь так странно?"
        th "Да нет, быть не может."
        "Это просто я надышался запахов из столовой, и меня разбирает галлюцинациями."
        show un shocked pioneer with dspr
        me "Двачевскую!"
        "Алиса покосилась на меня — мол, кто поминает имя моё всуе — но промолчала."
        hide un with dissolve
        "А я, не объясняя ничего больше, отправился за стол местных небожителей."
        stop music fadeout 2
        th "Меня ждёт финал!"
        "Ребята за соседними столами тоже время даром не теряли."
        play music music_list["get_to_know_me_better"] fadein 2

    elif ds_my_rival_semifinal.take == 'sl':
        show sl smile2 pioneer with dspr
        "Славя тихонько вздохнула и улыбнулась."
        "Я не очень понимал, чем вызвана её позитивная реакция, но обрадовался, что не обидел своей победой девушку."
        show sl normal pioneer with dspr
        "Она легко поднялась со стула и кивнула мне:"
        sl "Не успел приехать, а уже первое место занял."
        sl "Так вот и становятся легендами!"
        me "Так я же ещё ничего не занимал…"
        show sl laugh pioneer with dspr
        sl "Только не говори мне, что ты не нацелен на победу!"
        hide sl with dissolve
        "Она отошла к болельщикам."
        "А я пошёл к столу финалистов, между делом оценивая получившуюся ситуацию."

    elif ds_my_rival_semifinal.take == 'dv':
        show dv surprise pioneer2 with dissolve
        $ lp_dv += 1
        if herc or loki:
            play music music_list["that_s_our_madhouse"] fadein 3
        else:
            play music music_list["glimmering_coals"] fadein 3
        th "Итак, Гагарин долетался, Пушкин дописался."
        th "Выиграл!!!"
        show dv sad pioneer2 with dspr
        th "А рыжая облажалась."
        "Я поднялся из-за стола и бросил пренебрежительный взгляд на несчастную Алису."
        "Кажется, она чувствовала себя совершенно не в своей тарелке."
        "Теперь мой путь лежит к горним высям, где мне оппонентами выступят сами боги!"
        th "А не всякие самодовольные гадины, считающие, что меня можно запугать или запутать."
        if herc or loki:
            "Я подмигнул Двачевской."
            me "Поздравляю!"
            dv "Что?"
            me "С позорным поражением тебя!"
            $ lp_dv += 1
            show dv rage pioneer2 with dspr
            "По-моему, она меня всё-таки обругала матом."
            "Не могу сказать — её перекосило так, что я расхохотался."
            th "Ладно, на сегодня с неё хватит."
        else:
            "Я молча встал и направился к столу финалистов."
            "У меня нет времени на детсадовскую возню с неудачниками."
        "Я пошёл к столу финалистов, между делом оценивая текущую ситуацию."

    elif ds_my_rival_semifinal.take == 'mi':
        show mi sad pioneer with dspr
        "Мику однозначно расстроилась из-за проигрыша."
        "Похоже, она начала худо-бедно разбираться в правилах — и тут на тебе."
        "Humiliating Defeat."
        "Наткнулась на меня."

        show mi serious pioneer with dspr
        mi "В следующий раз победа будет моя!"

        show mi serious pioneer far with dspr
        show mi serious pioneer far at left with move
        hide mi with moveoutleft

        "Она вздёрнула нос к потолку и, поднявшись, гордо удалилась, занимая место среди проигравших."

        show mi grin pioneer far at fleft with moveinleft
        "Правда, немного подпортила картинку, обернувшись и показав мне язык."

        show mi smile pioneer far with dspr
        pause(0.3)
        hide mi with moveoutleft

        "Культурный человек, наследие эпохи…"
        me "Спасибо за игру!"
        "Ребята за соседними столами тоже время даром не теряли."
        "Игра сложилась весьма занятно."

    elif ds_my_rival_semifinal.take == 'us':
        show us dontlike pioneer with dissolve
        "Выиграть у Ульяны оказалось легче, чем…"
        "Чем пережить последствия этой победы…"
        play music music_list["awakening_power"] fadein 1
        show us angry pioneer with dspr
        pause(0.3)
        "Потому что она вдруг перегнулась через стол и принялась колотить меня своими маленькими кулачками."
        "И довольно сильно!" with vpunch
        us "Ты ведь обещал проиграть!" with hpunch
        "Она была так обижена, будто я её предал!"
        us "Обещал! Я ведь тебя просила!" with vpunch
        "Интересно, она понимает, что только что призналась в жульничестве?" with hpunch
        if ds_day2_walk == 1:
            th "Впрочем, я и сам жульничал, но…"
        me "Ничего я не обещал!"
        "С трудом, но мне удалось вставить пару слов в перерыве между ударами…"
        "И мне было не ясно только одно…"
        th "Почему меня никто не спасает?!!" with vpunch
        th "Где Ольга Дмитриевна, когда она так нужна?!" with hpunch
        "Но, кажется, всем было настолько весело наблюдать, как меня убивают, что никто и не думал прекращать развлечение…"
        stop music fadeout 6
        "Наконец поставив сотый синяк на моих руках и голове, Ульяна немного запыхалась и перестала меня бить." with vpunch
        show us dontlike pioneer with dspr
        "Но она всё ещё была недовольна…"
        play music music_list["i_want_to_play"] fadein 2
        "И это ещё мягко сказано…"
        show us angry pioneer with dspr
        us "У-у-у!"
        "Она свирепо топнула ножкой." with vpunch
        us "Ладно-ладно!"
        us "Я это тебе ещё припомню."
        hide us with moveoutleft
        "И с этими словами она резко развернулась и пошла в зал."
        "У меня появилась пара минут на то, чтобы привести себя в порядок и уточнить ситуацию в плей-офф."

    elif ds_my_rival_semifinal.take == 'sh':
        show sh normal pioneer with dissolve
        "Шурик кивнул мне и поднялся."
        "Не знаю, впечатлил его мой навык игры, в которую я играю сегодня первый раз в жизни, или нет."
        "Так или иначе, он достаточно равнодушно отнёсся к поражению."
        if not ('cyber' in list_joined_clubs_7dl) and ('cyber' in list_voyage_7dl):
            show sh smile pioneer with dspr
            sh "Насчёт клуба кибернетиков, если вдруг что…"
            "Я кивнул."
        hide sh with dissolve
        if not ('cyber' in list_joined_clubs_7dl) and ('cyber' in list_voyage_7dl):
            "Но давайте насчёт кибернетики позже, а пока посмотрим, что там у других пионеров творится."
        else:
            "А я покамест решил посмотреть, что там у других пионеров творится."

    elif ds_my_rival_semifinal.take == 'mz':
        show mz normal glasses pioneer with dissolve
        "Реакция Жужи меня позабавила."
        "Сначала она бросила карты на стол и спрятала лицо в ладонях."
        "А затем вскинула руки вверх и рявкнула:"
        show mz laugh glasses pioneer with dspr
        mz "Аллилуйя!" with vpunch

        show mz normal glasses pioneer far with dissolve
        pause(0.25)
        show mz normal glasses pioneer far at fleft with move
        hide mz with moveoutleft

        "После чего телепортировалась из столовой."
        "А я же решил узнать, как там дела у соседей."
# ---------------------------------------------------- \\ Диалоги

#-------------------------------------------------------------------------------------------------
    pause(.5)
    call ds_day2_semifinal_analizer                                    # анализ полуфинала
    $ renpy.block_rollback()                                                          # блокируем роллбак
#-------------------------------------------------------------------------------------------------
label ds_day2_final:
    $ ds_day2_my_win = ds_day2_rival_win = ds_day2_game_played_out = 0                       # обнуляем результат игр
    $ ds_tournament_state = "final_start"                                                      # устанавливаем начало финала
    if ds_day2_result_tour == 1:                                                               # Если продул в 1 туре
        $ ds_drawing_of_detour_final()                                                         # вызываем рандомизатор
        $ renpy.fix_rollback()                                                                  # фиксируем выбор — "откатом" поменять будет нельзя
# -----------------------------------------------------------------------
    $ ds_my_rival_final, ds_index_rival_final = ds_get_me_rival_final(ds_day2_gamblers_final,ds_rival_final)      # узнаём второго соперника в финале и его индекс  в рассадке

    $ ds_name_my_rival_i = ds_my_rival_final.name['i']                                   # узнаём ИМЯ второго финалиста (в именительном падеже)
    $ ds_name_my_rival_r = ds_my_rival_final.name['r']                                   # узнаём ИМЯ второго финалиста (в родительном падеже)
    $ ds_name_my_rival_d = ds_my_rival_final.name['d']                                   # узнаём ИМЯ второго финалиста (в дательном падеже)
    $ ds_name_my_rival_v = ds_my_rival_final.name['v']                                   # узнаём ИМЯ второго финалиста (в винительном падеже)
    $ ds_name_my_rival_t = ds_my_rival_final.name['t']                                   # узнаём ИМЯ второго финалиста (в творительном падеже)

    $ ds_spr_my_rival = ds_my_rival_final.take                                                # получаем спрайт соперника — заголовок
    $ ds_emo_my_rival = ds_sprites_rival_recognition[ds_spr_my_rival][0]                     # эмоция (строка)
    $ ds_acc_my_rival = ds_sprites_rival_recognition[ds_spr_my_rival][1]                     # аксессуар (строка)
    $ ds_clot_my_rival = ds_sprites_rival_recognition[ds_spr_my_rival][2]                    # одежда (строка)
    $ ds_pos_my_rival = ds_sprites_rival_recognition[ds_spr_my_rival][3]                     # положение

    $ ds_nick_my_rival = ds_my_rival_final.nick                                               # получаем характер соперника (для диалога)
# -----------------------------------------------------------------------

    # ================================================ пересаживаемся за финальный стол.
    show el smile pioneer at left with dissolve
    el "Полуфиналы завершены, победители встречаются в финале!"
    hide el with dissolve
    $ ds_mstt = 2
    call show_tournament_table                                                                  # показать таблицу — итоги полуфинала
# ----------------------------------------------------------------------------------------------------
label ds_day2_final_choice:
    if ds_rival_final.take == 'me':                                                            # Семён прошел в финал
        "Я уверенно двигаюсь к победе, следующая моя жертва уже видна на горизонте."

# ---------------------------------------------------- ДИАЛОГИ
        if ds_my_rival_final.take == 'un':
            "Прости, Лена. Ничего личного."
        elif ds_my_rival_final.take == 'sl':
            "Славя. Ну, она всё равно без души играет, так что я ей только доброе дело сделаю."
        elif ds_my_rival_final.take == 'dv':
            "Алиса, ага."
            me "Алиса, а Алиса."
            dv "Чего?"
            me "Тебе конец."
            "Она расхохоталась."
        elif ds_my_rival_final.take == 'mi':
            "Мику."
            "Как галантный парень я склонен сдать эту партию, чтобы сделать девушке приятное."
            "Но как игрок я чувствую запах победы, поэтому никакой пощады!"
        elif ds_my_rival_final.take == 'us':
            "Мелкая? Блин, кто-нибудь, объясните мне внятно: какого чёрта это мелкое недоразумение забыло в финале?"
        elif ds_my_rival_final.take == 'sh':
            "Шурик? Хм. Это будет интересный бой."
        elif ds_my_rival_final.take == 'mz':
            "Жужелица."
            "Может быть, и скрипит о том, что играть не хочет, но — блин, она же в финале!"
            "Придётся потрудиться."
# ---------------------------------------------------- /ДИАЛОГИ

        if ds_day2_detour_final:                                                                  # если пропуск финала
            scene bg int_dining_hall_sunset with dissolve2
            pause(1.0)
            if not ds_day2_tournament_fast_win:                                                   # Если НЕ победа в финале
                $ ds_day2_result_tour = 21                                                         # Семён проиграл в финале
                "Похоже, у меня не было ни шанса."
                call ds_day2_summary_poker_round
                jump ds_day2_final_fail_end                                                    # на поражение в финале
            elif ds_day2_tournament_fast_win:                                                      # если победа в финале
                $ ds_day2_result_tour = 22                                                         # Семён выиграл в финале
                call ds_day2_summary_poker_round
                jump ds_day2_final_win_end                                                    # на победу в финале

        jump ds_day2_final_start                                                              # играем финал
# ----------------------------------------------------------------------------------------------------
    else:                                                                                      # Семён продул в 1/2
        $ ds_name_rival_final = ds_rival_final.name['i']                                     # Получаем имя финалиста — кому Семён проиграл
        if ds_day2_result_tour == 1:                                                           # Если продул в 1 туре
            if ds_rival_final.take == ds_my_rival_1_tour.take:                                # соперник в 1 туре и финале тот же
                "В финал выходит мой соперник в первом коне — %(ds_name_rival_final)s{nw}"
            else:
                if ds_my_rival_1_tour.take == 'sh':
                    "Шурик, мой удачливый соперник, в полуфинале проиграл."
                else:
                    $ ds_name_rival_1_tour = ds_my_rival_1_tour.name['i']
                    "%(ds_name_rival_1_tour)s, отправившая меня в компанию болельщиков, сама проиграла в полуфинале."
                "А в финал выходит %(ds_name_rival_final)s{nw}"
        else:
            "Так как я сдулся и проиграл, в финал отправляется %(ds_name_rival_final)s{nw}"
        extend ", где встретит{nw}"
# ---------------------------------------------------
        if ds_my_rival_semifinal == None:                                                                        # Если каким-то образом второй финалист не назначен (может быть и такое)
            $ ds_my_rival_semifinal = ds_day2_gamblers_final[1-ds_day2_gamblers_final.index(ds_rival_final)]  # Это НЕ тот, кому Семён проиграл
# ---------------------------------------------------

# ---------------------------------------------------- ДИАЛОГИ
        if ds_my_rival_final.take == 'un':
            extend " Лену и попытается обыграть её."
        elif ds_my_rival_final.take == 'sl':
            extend " Славю и докажет всем, что блондинка — это диагноз."
        elif ds_my_rival_final.take == 'dv':
            if ds_rival_final.take == 'us':
                extend "… Алису? Так они с самого начала это планировали?!"
            else:
                extend " Алису и попробует уцелеть в этой схватке."
        elif ds_my_rival_final.take == 'mi':
            extend " Мику. {w}Не думаю, что там будет много проблем. Хотя японка и добралась до финала."
        elif ds_my_rival_final.take == 'us':
            if ds_rival_final.take == 'dv':
                extend " Ульянку."
                "Смешно, но, похоже, рыжие в самом деле попросту разметали этот турнир по брёвнышку, как и хотели."
            else:
                extend " Ульяну и попробует выжить после встречи с ней."
        elif ds_my_rival_final.take == 'sh':
            extend " Шурика и попробует доказать, что мозги в карточной игре не решают."
        elif ds_my_rival_final.take == 'mz':
            extend " Женю."
            "Что ещё можно про сказать про оппонентку Ульянки?"
            "Во. Жужелица."
# ---------------------------------------------------- /ДИАЛОГИ
        scene bg int_dining_hall_sunset with joff_r
        $ ds_day2_gamblers_final[renpy.random.choice([0,1])].winner = True                                    #  один из игроков (рандомно) — победитель в финале
        $ ds_tournament_state = "final_end"
        call ds_day2_final_analizer

        if (ds_day2_dv_ultim == 1):
            "Что ж, теперь можно подвести итоги."
            "Спор я закономерно продул — с моей удачей надеяться было глупо. Задним умом теперь уж я понял, нужно было заранее узнать, во что мы будем играть."
            th "Это же не игра, а простое подбрасывание монетки! Случайно раздали карты, случайно выбираешь, какую из них забрать у противника."
            if (ds_day2_walk == 1) and (ds_my_rival_final.take != 'dv'):
                dreamgirl "Да ты же карты пометил, дубина! Как ты вообще с таким раскладом умудрился продуть?!"
                th "Критический промах."
            else:
                "В общем, в поражении я не виноват. Вот."
        $ renpy.block_rollback()                                                                                # блокируем роллбак
        stop music fadeout 2
        jump ds_day2_prepare_transition_to_supper
# ------------------------------------------------------------------------------------------------------------------------------

label ds_day2_final_start:
    call ds_day2_checking_scores
    call ds_day2_stipulation                                                       # определяемся, кто первый ходит
# ----------------------------------------------------------------------------
    # первоначальные "настройки" игроков — могут меняться по результатам игры
    # 'defense' — защита, 'gamble' — риск, 'succumb' — слив, 'foolplay' — рандом
    # вероятность ошибки: 1 = 80%, …, 4 = 20%, 5 — ошибок нет.
    if ds_my_rival_final.take == 'un':                                                    # Добрались сюда — так что нефиг, Лена защищается
        $ ds_day2_gambler_behavior = 'defense'
        $ ds_day2_gambler_skill = 4                                                       # ошибки, правда, есть — 20%(4)
    elif ds_my_rival_final.take == 'sl':                                                  # Славя будет защищаться, может ошибиться — 20%(4)
        $ ds_day2_gambler_behavior = 'defense'
        $ ds_day2_gambler_skill = 4
    elif ds_my_rival_final.take == 'dv':                                                  # Алиса рискует, вероятность ошибки 20%
        $ ds_day2_gambler_behavior = 'gamble'
        $ ds_day2_gambler_skill = 4
    elif ds_my_rival_final.take == 'mi':                                                  # Мику будет защищаться, может ошибиться — 20%(4)
        $ ds_day2_gambler_behavior = 'defense'
        $ ds_day2_gambler_skill = 4
    elif ds_my_rival_final.take == 'us':                                                  # Ульяна к финалу научилась играть и будет защищаться, но с ошибками 40% (3)
        $ ds_day2_gambler_behavior = 'defense'
        $ ds_day2_gambler_skill = 3                                                       # ошибок — 40%(3)
    elif ds_my_rival_final.take == 'sh':                                                  # Шурик экспериментирует по-прежнему, вероятность ошибки 20%
        $ ds_day2_gambler_behavior = renpy.random.choice(['defense', 'gamble'])           # у него своя кухня — набор из возможных вариантов
        $ ds_day2_gambler_skill = 4
    elif ds_my_rival_final.take == 'mz':                                                  # Женя играет рандомно, как в классике, вероятность ошибки 20%
        $ ds_day2_gambler_behavior = 'foolplay'
        $ ds_day2_gambler_skill = 4
# ----------------------------------------------------------------------------

    if ds_day2_walk == 1:
        $ VISIBLE = True
        $ INVISIBLE = True
    else:
        $ VISIBLE = True
        $ INVISIBLE = False

# ------------------------------------------------------------------------------------------------------------------------------
# Палим Семёна с крапом карт
    if ds_day2_walk == 1 and INVISIBLE:                                    # Если Сёма мухлевал И ЕГО ещё не поймали, его таки в финале МОГУТ спалить
        if ds_my_rival_final.take == 'dv':                               # палит Алиса
            "Но прежде, чем всё началось, Алиса с подозрением оглядела карты, которыми мы играли."
            th "Неужели…"
            "По спине пробежал холодок…"
            "А она слегка перегнулась через стол и, лукаво улыбаясь, спросила шёпотом — так, что слышать её мог только я…"
            show dv smile pioneer2 with dissolve
            dv "Так ты все карты пометил, да?"
            dv "Предусмотрительный…"
            th "Она знала, что я жульничал!!!"
            "Я покраснел."
            th "Если сейчас она встанет и скажет всем…"
            th "Это будет ужасно!!!"
            th "Невыносимо!!!"
            th "Кошмарно!!!"
            "Но Алиса, кажется, и не думала выдавать меня…"
            "Она улыбалась!"
            dv "Надеялся и меня так обыграть?"
            "И я, проклиная свою честность, тоже шёпотом, ответил:"
            me "Да…"
            "Она фыркнула, впрочем, совсем беззлобно."
            dv "Даже не мечтай…"
            "Незаметно для зрителей она достала из кармана совершенно новую колоду карт и поменяла её местами с помеченной мной…"
            dv "Играть будем моими!"
            show dv laugh pioneer2 with dissolve
            "Она довольно улыбнулась."
            dv "Я тоже предусмотрительная…"
            "Игра началась."
            $ INVISIBLE = False
# ------------------------------------------------------------------------------------------------------------------------------

label ds_day2_final_re_game:                                                           # игра в финале — сюда возвращаемся на повторную игру
    $ ds_my_poker_hand = None
    $ ds_rival_poker_hand = None

    python:
        dialogs = {
                        (0, 'win','jump'):'ds_day2_one_play_win',
                        (0, 'fail','jump'):'ds_day2_one_play_fail',
                        (0, 'draw','jump'):'ds_day2_one_play_draw'
                    }
        generate_cards_alt('bg hall', dialogs)

# ****************   НОВЫЕ  СОПЕРНИКИ   ******************************************
        if ds_my_rival_final.take == 'un':
            rival = CardGameRivalWiseUsual(un_avatar_set, u"Лена", ds_day2_gambler_behavior, ds_day2_gambler_skill)
        elif ds_my_rival_final.take == 'sl':
            rival = CardGameRivalWiseUsual(sl_avatar_set, u"Славя", ds_day2_gambler_behavior, ds_day2_gambler_skill)
        elif ds_my_rival_final.take == 'dv':
            rival = CardGameRivalWiseUsual(dv_avatar_set, u"Алиса", ds_day2_gambler_behavior, ds_day2_gambler_skill)
        elif ds_my_rival_final.take == 'mi':
            rival = CardGameRivalWiseUsual(mi_avatar_set, u"Мику", ds_day2_gambler_behavior, ds_day2_gambler_skill)
        elif ds_my_rival_final.take == 'us':
            rival = CardGameRivalWiseUsual(us_avatar_set, u"Ульяна", ds_day2_gambler_behavior, ds_day2_gambler_skill) # К финалу Ульянка уже и играть научиться должна бы
        elif ds_my_rival_final.take == 'sh':
            rival = CardGameRivalWiseUsual(sh_avatar_set, u"Шурик", ds_day2_gambler_behavior, ds_day2_gambler_skill)
        elif ds_my_rival_final.take == 'mz':
            rival = CardGameRivalWiseUsual(mz_avatar_set, ds_day2_gambler_behavior, ds_day2_gambler_skill)           # Женя играет рандомно, как в классике
# ************************************************************************************

    $ ds_hint_poker = ds_hint_poker_contractual                                           # подсказки комбинаций — по просмору правил
    jump cards_gameloop_wise_alt                                                            # переход карточный стол

#-------------------------------------------------------------------------------------------------
label ds_day2_final_fail_end:
    $ ds_day2_result_tour = 21                                             # Семён проиграл в финале
    scene bg int_dining_hall_sunset with dissolve
    $ persistent.altCardsWon2 = True

    if ds_day2_gamblers_final[0].take != 'me':                             # если 1-й игрок — НЕ Семён
        $ ds_day2_gamblers_final[0].winner = True                          # он и выиграл
    else:                                                                   # если 2-й игрок — НЕ Семён
        $ ds_day2_gamblers_final[1].winner = True                          # он и выиграл
    $ ds_tournament_state = "final_end"                                    # устанавливаем конец финала

    if not ds_day2_detour_final:                                           # если НЕ пропуск финала
        "Похоже, у меня не было ни шанса."
        call ds_day2_summary_poker_round

    scene
    call ds_day2_final_analizer
    $ renpy.block_rollback()                                                          # блокируем роллбак
    scene bg int_dining_hall_sunset with dissolve

# ---------------------------------------------------- ДИАЛОГИ
    if ds_my_rival_final.take == 'un':
        $ lp_un += 1
        stop music fadeout 2
        show un surprise pioneer with dissolve
        "Кажется, Лена ещё не до конца поняла, что именно сейчас произошло."
        play music music_7dl["take_my_hand"] fadein 3
        "А произошло рождение легенды, +50 к опыту, новый уровень и разблокировка уверенности в себе!"
        show un cry_smile pioneer with dspr
        "Лена смотрела на меня долго, неотрывно, и у неё тряслись руки."
        "Я молчу, она молчит, а вокруг как будто выросла некая отталкивающая стенка, защищающая нас — но лишь пока мы вместе."
        "Как будто два человека, каждый из которых неполон в одиночестве, вместе намного сильнее, чем если просто сложить их характеристики."
        "Я не могу сказать сейчас, поддавался ли я или играл в полную силу, но просто прийти сюда уже было хорошей идеей, сторицей окупившейся этими мгновениями."
        dreamgirl "Не влюбись в неё, барин, вы знакомы меньше суток."
        "Я пожал плечами."
        th "Ну и что?"
        "Ведь поют же все вокруг о любви с первого взгляда, почему бы и мне не пасть жертвой этого волшебного явления?"
        "Ну ладно, но просто признаться себе в том, что она мне нравится, я могу?"
        "Просто лицо, фигура и манера поведения."
        th "Возможно, у неё килограммовые тараканы там, и она только с виду няша-скромняша, глазки в пол, ресничками бяк-бяк."
        th "Но я-то об этом не знаю, правда?"
        th "А значит, буду наслаждаться неведением."
        th "Ибо оно и есть истинное блаженство."
        "Не знать плохого о любимых, не понимать смысл текста красивой песни на японском, не думать об удобрениях для клубники и яблонь, не понимать, что красивая шубка означает смерть животного."
        "Здесь и сейчас — на малую долю секунды — просто влюбиться, пасть жертвой ситуации, настроения и атмосферы."
        with fade
        "И отпустить мгновение, потому что пора просыпаться и идти на работу."
        me "Поздравляю с победой."
        "Улыбнулся я."
        show un shy pioneer with dspr
        un "С-спасибо…"
        "Её имя уже внесли в список победителей, и завтра, скорее всего, заставят поднимать флаг, как самую активную участницу."
        "Ведь нельзя же занять первое место, не принимая активного участия."
        "Правда?"
        "Ох, мои соболезнования."
        if ds_day2_dv_ultim == 1:
            th "Хотя это, наверное, мне соболезновать надо?"
            dreamgirl "Намекаешь на двачевские инсинуации? Не дрейфь, она умылась, не дойдя и до финала, постесняется."
            "Будто подтверждая мои слова, Алиса, что всю партию следила за нами, казалось, забыв дышать, вздрогнула и отвела глаза."
            "Похоже, да, не хватит ей пороху довести свою гадость до логического завершения."
        stop music fadeout 3

    elif ds_my_rival_final.take == 'sl':
        $ lp_sl -= 1
        $ karma += 10
        stop music fadeout 3
        show sl sad pioneer with dspr
        "Славя застонала и уронила голову на сложенные руки."
        play music music_list["forest_maiden"] fadein 5
        sl "Вы хотя бы пытались, ребята?"
        me "Я — старался!"
        sl "Семен, пожалуйста."
        show sl serious pioneer with dspr
        "Она нахмурилась."
        sl "Хуже меня нет игрока в карты, а я заняла… Ах, зачем я вообще согласилась!"
        me "Но мы же…"
        sl "Вам что, и правда было настолько всё равно, что вы даже поленились немного постараться?"
        show sl sad pioneer with dspr
        sl "Я очень, очень расстроена."
        sl "Если вы и на завтрашних танцах будете такими же активными, я пойму намёк, и до конца смены развлекайте себя сами."
        show mt laugh pioneer at left with dissolve
        mt "Что это у нас, а?"
        mt "Демарш победителя? Ну, наконец-то! {w}Я уже было подумала, что ты оживший экспонент мадам Тюссо." # "экспонент" — так задумано или меняем на "экспонат"? ## полагаю, трудно случайно вместо "экспонат" написать "экспонент"
        show sl angry pioneer with dspr
        sl "Ольга Дмитриевна, я серьёзно, а вы!"
        show mt normal pioneer with dspr
        mt "Славя, просто наслаждайся победой, хорошо? {w}Я знаю твоё отношение к карточным играм, и если бы у меня была возможность поставить кого-нибудь вместо тебя, я бы так и поступила."
        hide mt with moveoutleft
        "Ольга сочувственно повздыхала, подмигнула ей и скрылась на кухне."
        "Похоже, слова о призе имели под собой кое-какое обоснование!"

    elif ds_my_rival_final.take == 'dv':
        $ lp_dv = lp_dv/2
        stop music fadeout 2
        if loki or herc:
            "Проиграть было забавно."
            play music music_list["you_lost_me"]
            "С любой из сторон, как ни крути, я оказывался в выигрыше — в случае победы мне удастся немного заткнуть Двачевскую."
            dreamgirl "Ровно до того момента, пока она не созреет для новой шалости."
            th "Этого достаточно."
            "А в случае поражения она устроит мне пиар-акцию в духе «Сёма едет, прячьте тёлок.»"
            "Так что я от всей души пожелал удачи сопернице."
            "И приготовился к шоу."
        else:
            th "Я слил."
            th "Я облажался."
            play music music_list["you_lost_me"]
            th "Как всегда…"
            if ds_day2_walk == 1:                                                 # была лишняя проверка
                th "Несмотря даже на то, что я пометил карты."
            "Появилось это противное чувство, что сейчас на меня начнут показывать пальцем и шептаться «Смотрите, это он! Да, он! Он облажался.»"
            "Я двинулся прочь от стола, не поднимая ни на кого глаз."
            "Особенно — на Алису."
            "Её взгляд буквально жёг мне спину."
        if ds_day2_dv_ultim == 1:                                                 # Спорил
            th "Я проиграл пари."
            if loki or herc:
                "Теперь ждём завтрашнего дня и наслаждаемся бесплатной рекламой?"
            else:
                "Теперь мне… {w}Крышка? Кранты? Конец?"
                th "Может, сбежать из лагеря, пока не поздно?"
        else:                                                                       # НЕ спорил
            if ds_day2_dv_ultim == 2:                                              # Если лапал
                "И теперь, если она расскажет всем, что я её лапал — это же правдой будет, да?"
                "Как говорил мой батя в трудных ситуациях — не упс, а йопс."
            else:                                                                   # НЕ лапал
                "Хотя я не спорил с Двачевской, она теперь вполне может рассказать всем то, что она напридумывала на крыльце."
                "И ей поверят. Как обычно верят любому победителю."

        "Алиса победила, и все наперебой принялись её поздравлять."
        "Электроник взмахнул руками, ознаменовав окончание турнира, и дописал в таблицу её имя."
        th "Алиса выиграла…"
        if ds_day2_dv_ultim == 1:
            th "А я проиграл и турнир, и пари…"
        else:
            th "А я проиграл… Как и всегда, впрочем."
        th "Что же будет?!"
        show dv normal pioneer2 at fleft with dissolve
        "Я посмотрел на Алису. Казалось, на её лице не было и следа радости…"
        if ds_day2_dv_ultim == 2:
            "Алиса встала из-за стола и, ощутимо заставляя себя…"
            show mt normal pioneer at fright with dissolve
            "Направилась к вожатой! Да! Момент истины!"
            show dv normal pioneer2 at fleft with moveinleft
            th "Хватит ли девочке пороху?"
            "Внутри меня всё трепетало в предвкушении."
            "Я подвинулся поближе, пытаясь расслышать подробности"
            "Но она говорила шёпотом, и я ничего не мог расслышать…"
            show dv guilty pioneer2 at cright
            show mt normal pioneer at fright
            with dissolve
            "Она краснела всё сильнее, и я буквально мог читать по губам."
            "…руками…"
            "…прямо за грудь…"
            "…и под юбку…"
            me "Двачевская, у тебя такая пылкая фантазия!"
            "Подвёл черту их шептанью я."
            show dv sad pioneer2 at left
            show mt normal pioneer at right
            with dissolve
            me "Может, вслух расскажешь? Мне тоже охота послушать."
            stop music fadeout 3
            "А Ольга Дмитриевна спокойно посмотрела на меня и сказала:"
            mt "Алиса говорит, что игрок из тебя аховый."
            show mt smile pioneer at right with dspr
            mt "По-моему, всё верно."
            hide dv
            hide mt
            with dissolve
            "Я расхохотался и освободил столик."
            "Кто бы сомневался. Не такой реакции от меня ждала Алиска, совсем не такой."
        else:
            "С равнодушием, лениво бросив на меня прищуренный взгляд, Алиса…"
            show mt normal pioneer at fright with dissolve
            "Пошла прямо к Ольге Дмитриевне, стоявшей всё это время среди зрителей!"
            show dv normal pioneer2 at fleft with dspr:
                xalign 0.1
                linear 3.0 xalign 0.7
            if loki:
                th "Неужели скажет?"
            elif herc:
                th "Таки решила рассказать свою байку?"
            if dr:
                th "Она в самом деле расскажет?!"
            if not ds_day2_dv_ultim:
                if loki:
                    th "Я же не стал с ней спорить."
                elif herc:
                    th "До чего ж упёртая."
                    dreamgirl "Никого не напоминает?"
            if dr:
                "Всё во мне словно перевернулось."
                "Я бросился вслед за ней…"
                "Но было уже поздно…"
            elif herc:
                "Я поудобнее уселся и стал ждать развязки."
                dreamgirl "Не боишься?"
                th "Ничуть."
                th "Если вожатая поверит в эту чушь, я в ней разочаруюсь."
            show dv smile pioneer2 at cright
            show mt normal pioneer at fright
            with dissolve
            "Алиса стояла рядом с Ольгой Дмитриевной и что-то горячо шептала ей на ухо, весьма лукаво поглядывая на меня."
            if dr:
                "Этого я не мог допустить!"
                "С громким криком…"
                me "Это неправда!"
                me "Всё, что она говорит обо мне — НЕ-ПРАВ-ДА!"
                show dv smile pioneer2 at left
                show mt normal pioneer at right
                with dissolve
                "Я подбежал к ним."
                stop music fadeout 3
                "А Ольга Дмитриевна спокойно посмотрела на меня и сказала:"
                mt "А по-моему, всё верно."
                show mt smile pioneer at right with dspr
                mt "Ты совсем не умеешь играть в карты."
                "Такого позора я ещё никогда не испытывал."
            elif herc:
                "Я усмехнулся рыжей в ответ."
                me "Давай-давай."
                show dv sad pioneer2 at cright with dspr
                pause(0.3)
                show dv normal pioneer2 at cright with dissolve
                "Не думаю, что Двачевская умеет читать по губам, но она поняла насколько безразличны мне её потуги."
                th "Поздновато ты это поняла."
                dreamgirl "Подлей маслица в огонь."
                th "Каким образом?"
                "В воображении возникло по меньшей мере пять способов вогнать Двачевскую в краску."
                "И все пять — неприличные жесты."
                "Делать это я не стану, но мысль об этом меня позабавила."
                th "Спасибо."
                dreamgirl "К вашим услугам."
                "Ольга посмотрела на меня и спокойно сказала:"
                mt "Ну да, всё верно, не умеет играть."
                mt "Но похоже, его это не слишком заботит."
                stop music fadeout 3
                "Я едва не расхохотался."
                "Сдрейфила!"
            elif loki:
                show dv normal pioneer2 at cright with dissolve
                "Я старался держать лицо и не терять достоинства, ожидая развязки."
                "Не верю, что квалифицированный педагог, вроде нашей вожатой, поверит в эту нелепую чушь."
                "Тем более из уст Двачевской."
                "Если поверит, я в ней немного разочаруюсь."
                "А Двачевской я это припомню."
                "Наконец, Ольга спокойно сказала:"
                mt "Ну да, всё верно."
                mt "Он совсем не умеет играть в карты."
                stop music fadeout 3
                "Рыжая не смогла и пошла на попятную."
                "Я не скрывал улыбки."

    elif ds_my_rival_final.take == 'mi':
        stop music fadeout 3
        show mi happy pioneer with dspr
        $ lp_mi += 1
        $ karma += 10
        mi "Да! Да! Вы понимаете это?! Это снова я, и я снова на коне!"
        play music music_7dl["ourfirstmet"] fadein 3
        mi "У меня не было никаких сомнений в том, что я приду и всех победю!"
        mi "И я пришла и победила."
        mi "Да я, да я… Я супер-Мику!"
        me "Очаровательное чудовище."
        "Пробормотал я."
        show mi smile pioneer with dspr
        mi "Я не так часто выхожу из клуба, потому что всем постоянно что-то надо, все куда-то спешат и говорят мне «потом поговорим!»."
        mi "А я не хочу потом, я сейчас хочу! И сейчас, пока я победитель, вы все должны меня слушать и не ругаться, что я много болтаю!"
        th "Дефицит внимания, ласки, тепла и заботы… А я ещё себя хикикомори считал."
        me "А кричать-то зачем?"
        stop music fadeout 3
        "Оказаться в финале для меня уже было изрядным достижением, поэтому я не особо расстраивался насчёт проигрыша."
        play music music_7dl["tender_song"] fadein 3
        "А Мику вдруг воздела к небу пальчик."
        show mi happy pioneer with dspr
        mi "Ой, а я знаю, кажется! Да! Мне только что идея в голову пришла! Я…"
        show mi happy pioneer far with dissolve
        "Она забралась на стол."
        mi "Я вам спою!"
        "Она набрала в грудь воздуха, и…"
        show dv angry pioneer2 at cleft with easeinleft
        show mt angry pioneer at cright with easeinright
        with vpunch
        "Неизвестно откуда взявшиеся Ольга и Алиса, взревев в унисон, ринулись было стаскивать её на пол."
        "Но где там!"
        show mi laugh pioneer far at fleft with diam
        "Стол для игры финалистов был большой, не чета узеньким, за которым мы квалифицировались."
        "Поэтому маленькая, юркая японочка успешно прыгала между руками загребущими и голосила во всю силу своих развитых лёгких."
        "Пела она о чём-то своём, на лунном наречии, которое я даже под градусом считал зубодробительным, а потому и не пытался вслушиваться."
        "Куда интереснее было слушать голос."
        "И смеяться над тем, как тут и там в такт пению раздаются хлопки."
        "Чаще ловящих Мику Алисы и Ольги Дмитриевны, но и из благодарной публики тоже шла своя доля оваций."
        mi "Ла-ла, ла-ла-ла-ла, ла-ла-ла, ла-ла-ла-ла!"
        "Вопила она, бегая по столам, стульям и демонстрируя нам не только высокий уровень игры в карты, но и недюжинную подготовку по части паркура."
        "Я бы поставил на японку и не прогадал."
        "У неё вся жизнь такая."
        "Суетная, бегательно-прыгательная на сцене, и выступления не по три форматных минутки, а полноценные концерты на несколько часов."
        hide mt
        hide dv
        with dissolve
        "Так что ещё минут пять — и обе ловчих свалились рядом со столами, а она всё продолжала и продолжала петь, делая в воздухе странные, стригущие движения пальцами."
        "Отчего-то от таких движений, да ещё в исполнении ультрамаринового маникюра, неприятно-холодно ёкало в животе."
        show mi normal pioneer far at center with easeinleft
        with fade
        "Но всё когда-нибудь кончается."
        show mi smile pioneer with dissolve
        "Кончилась и долгоиграющая песенка японской старлетки, и она, подойдя по столу с моей стороны, протянула мне руку."
        "И я, как истинный джентльмен, принял её и помог девочке спуститься."
        show mi happy pioneer close with dspr
        mi "Спасибо! Ты мой герой!"
        show mt rage pioneer at fleft with dissolve
        mt "Ну, Хацунэ!"
        "Мику на миг прижалась ко мне всем телом, а затем убежала от криков разъярённой вожатой."
        hide mi with flash

    elif ds_my_rival_final.take == 'us':
        $ lp_us += 1
        stop music fadeout 2
        "Как известно, в карты везёт новичкам и дурачкам."
        play music music_7dl["genki"] fadein 3
        "Так как мы все здесь новички, мы были в равных условиях."
        "Но кое-кому перепало на один шанс больше!"
        "И все догадываются, о ком речь, и почему ему больше досталось!"
        show us normal pioneer with dissolve
        "Эти пустые, стеклянные голубые глаза очень странно смотрятся в обрамлении алой чёлки."
        "Косица пшеничного цвета, как у Слави, этому ребёнку подошла куда бы больше."
        "Такая вот несостоявшаяся блондинка."
        show us laugh pioneer with dspr
        us "Ура! Я победила!"
        "Она вскочила на стул!"
        us "Я победила! И теперь суперприз мой! {w}Моооооой!"
        me "Твой, твой. Ты только слезь со стула, а то брякнешься ещё."
        "Да где там."
        "Ульянка начала подпрыгивать на опасно скрипящем стуле и скандировать:"
        us "Приз! Приз! Приз!"
        me "Успокойся, а?"
        show us grin pioneer with dspr
        us "Ты просто завидуешь, что у меня будет приз, а у тебя нет!"
        "Понятия не имею, о каком призе она говорит."
        "Вообще, пойду-ка я, пока чего не случилось."
        hide us with dissolve
        scene
        call show_tournament_table
        "А в самом центре таблицы огромными красными буквами значилось имя."
        el "Победитель — Ульяна!"
        "Все стали кричать «поздравляем, поздравляем»!"
        scene bg int_dining_hall_sunset
        show us grin pioneer
        with dissolve
        "Но Ульяна отмахнулась. {w}Её интересовало другое:"
        us "А где призы?"

    elif ds_my_rival_final.take == 'sh':
        show sh normal pioneer with dissolve

        "Чествование Шурика выглядело неловко и натянуто."

        show sh serious pioneer far with dissolve
        pause(0.25)
        show sh serious pioneer far at fright with move
        hide sh with moveoutright

        "Он встал, поклонился и вышел из столовой, не дожидаясь даже, когда его имя внесут в таблицу лидеров."

        show mi shocked pioneer far at center with dspr
        mi "Кошмарный человек."
        "Заметила Мику."

        show mi upset pioneer far with dspr
        mi "Совершенно далёк от публичности."

        show un normal pioneer far at left with dspr
        show mi upset pioneer far at right with move
        un "У него другие достоинства."

        show us smile pioneer far at fleft with moveinleft
        us "Да? Ну-ка подробнее, пожалуйста, о достоинствах, а то я не расслышала."

        show mi surprise pioneer far at fright
        show un serious pioneer far at center
        with move
        un "Тебе бы только о похабностях слушать."

        show sl serious pioneer far at cleft with dspr
        show un serious pioneer far at cright with move
        sl "Лена, а ты бы сама немного думала, что говоришь в присутствии ребёнка."

        show un surprise pioneer far
        show us dontlike pioneer far
        show mi dontlike pioneer far
        with dspr
        us "Эй, мне уже четырнадцать!" #us "Эй, мне уже двадцать девять!"
        mi "Эй, мне уже шестнадцать!"

        un "Э…"
        sl "Да-да, ты тут о достоинствах Шурика разглагольствовала."

        show dv surprise pioneer2 far at center with dspr
        dv "Девочки, а что это вы тут обсуждаете, и без меня?"

        show mi cry_smile pioneer far:
            xcenter 0.86
        show un grin pioneer far:
            xcenter 0.67
        show sl surprise pioneer far:
            xcenter 0.33
        show us surp1 pioneer far:
            xcenter 0.10
        with move
        un "Ой, Двачевская, потеряйся! Кошмарище лесное, додумалась новичка сиськами запугивать."
        me "Эй, я всё ещё здесь!"

        show mi rage pioneer far
        show un rage pioneer far
        show dv rage pioneer2 far
        show sl angry pioneer far
        show us angry pioneer far
        with dspr
        all "Заткнись!" with vpunch

        show mi smile pioneer far
        show un shy pioneer far
        show dv grin pioneer2 far
        show sl shy pioneer far
        show us normal pioneer far
        with dspr
        "Я и заткнулся."

        show mi laugh pioneer far
        show un laugh pioneer far
        show dv laugh pioneer2 far
        show sl laugh pioneer far
        show us laugh pioneer far
        with dspr
        "Что мне ещё оставалось." #Сёма, какой же ты дегенерат, пиздец просто!

    elif ds_my_rival_final.take == 'mz':
        show mz normal glasses pioneer with dissolve
        "Жужелица встала."
        "Окинула всех диковатым взглядом."
        mz "Всё, что ли? Больше жертв не будет?"
        play sound sfx_7dl["highfive"]
        pause(1)
        play sound sfx_7dl["highfive"]
        pause(1)
        "В полной тишине спросила она."
        play sound sfx_7dl["highfive"]
        pause(1)
        play sound sfx_7dl["highfive"]
        show el smile pioneer at left with dissolve
        "Только Электроник продолжал хлопать."
        mz "Ну ладно. Я пойду тогда."
        el "Ура, да здравствует победитель!"

        show mz normal glasses pioneer far with dissolve
        pause(0.25)
        show mz normal glasses pioneer far at fleft with move
        hide mz with moveoutleft

        play sound sfx_7dl["highfive"]
        "Закричал Сыроежкин ей вслед."
        "По-моему, это всё-таки любовь."
        sh "Эл, всё, она ушла. Успокойся."
# ---------------------------------------------------- \\ Диалоги
    stop music fadeout 3
    jump ds_day2_prepare_transition_to_supper                        # пошли ужинать

#-------------------------------------------------------------------------------------------------
label ds_day2_final_win_end:
    $ ds_day2_result_tour = 22                                             # Семён выиграл в финале
    $ lp_dv += 1

    if not ds_day2_detour_final:                                          # если НЕ пропуск финала
        $ persistent.altCardsWonRivals[ds_spr_my_rival] = True        # Выиграли у этого соперника
    $ persistent.altCardsWon3 = True

    if ds_day2_gamblers_final[0].take == 'me':                             # если 1-й игрок — Семён
        $ ds_day2_gamblers_final[0].winner = True                            # он и выиграл
    else:                                                                   # если 2-й игрок — Семён
        $ ds_day2_gamblers_final[1].winner = True                            # он и выиграл
    $ ds_tournament_state = "final_end"                                   # устанавливаем конец финала

    if not ds_day2_detour_final:                                                # если НЕ пропуск финала
        call ds_day2_summary_poker_round

    scene
    call ds_day2_final_analizer
    $ renpy.block_rollback()                                                          # блокируем роллбак
    stop music fadeout 3
    scene bg int_dining_hall_sunset with dissolve

# ---------------------------------------------------- ДИАЛОГИ
    if ds_my_rival_final.take == 'un':
        show un shy pioneer with dissolve
        un "К-кажется, в-всё."
        play music music_7dl["take_my_hand"] fadein 3
        me "Что?"
        show un sad pioneer with dspr
        un "Н-ну… Ты выиграл. П-поздравляю."
        "Пробормотала она."
        "Её с трудом можно было разобрать за шумом толпы, а она всё продолжала и продолжала говорить…"
        "Будь моя воля, я бы, наверное, попросил её говорить громче."
        th "Но где там."
        th "Это же означает неминуемое сближение."
        scene bg int_dining_hall_sunset with dissolve
        "Не слушая больше то, что она мне говорит, я поднялся."
        "И пошёл к доске, где Электроник уже писал моё имя."
        scene
        call show_tournament_table
        "Моё!"
        if ds_day2_dv_ultim in (1, 2):
            th "И пусть только рыжая стерлядь попробует что-нибудь там вякнуть."
        scene bg int_dining_hall_sunset with dissolve
        if ds_day2_dv_ultim == 2:
            show dv shy pioneer2 with dissolve
            "Поймав мой взгляд, она покраснела как маков цвет."
            "А я, склонив голову набок, изобразил пантомиму под названием «натягиваю резиновую перчатку»."
            show dv shocked pioneer2 with dspr
            "И красноречиво так пошевелил пальцами."
            "Алисе аж плохо стало."
            th "Или это она подумала, что я не перчатку надеваю, а… Фу, какая она испорченная."
        else:
            "Лена потерялась где-то на заднем плане, а я неотрывно чувствовал чей-то взгляд лопатками."
            show dv smile pioneer2 with dspr
            play sound sfx_punch_medium
            dv "Поздравляю!" with vpunch
            "Поэтому почти ожидал хлопка между лопаток."
            "Видимо, Двачевская так приветствует всех, кто ей интересен."
        hide dv with dissolve

    elif ds_my_rival_final.take == 'sl':
        $ lp_sl += 1
        show sl smile pioneer with dspr
        "Я победил?"
        play music music_7dl["please_reprise"] fadein 3
        "Победил?!"
        me "Да!"
        "Бросив над головой карты, рявкнул я:"
        me "Я — победитель!!!" with vpunch
        show sl smile2 pioneer with dspr
        "Почему-то здесь и сейчас хотелось вести себя так, как душа лежит."
        "Не так, как правила того требуют, или «что же люди скажут»."
        "Это её влияние. Её."
        "А ведь мы знакомы меньше суток."
        "Но уже сейчас искренность проявлений чувств становится одной из самых важных добродетелей."
        sl "Да!"
        "Звонко произнесла она."
        "Её глаза сияли."
        sl "Ты победитель турнира."
        sl "Ты — победитель."
        "Как в боксе, она стоит рядом со мной."
        "Хватает меня за запястье."
        "И тянет к небу поднятой рукой."
        show sl happy pioneer with dspr
        sl "Се-{w=.3}мён! Се-{w=.3}мён!"
        "Скандирует она."
        "Трудно бороться с чувством сюрреалистичности происходящего."
        "Как будто бы я попал в какую-нибудь космическую оперу или ещё какой-то пафосный жанр."
        th "Но эти люди не умеют стесняться честного слова и честного чувства."
        "Они кричат вместе с ней."
        "Смотрят на меня."
        "Мои пятнадцать минут славы."
        dreamgirl "Пятнадцать минут Слави?"
        "А я расхохотался."
        th "Да! Да, чёрт возьми. Именно так."
        "К нам протолкалась Ольга Дмитриевна."
        show mt normal pioneer at left with dissolve
        mt "Не уходи никуда после ужина, будет вручение призов."
        show sl normal pioneer with dspr
        dv "Поздравляю!"
        "Из-за спины я услышал голос, который слышать бы очень не хотел."
        "Судя по сузившимся глазам Слави, не я один."
        "Но я обернулся."
        hide mt
        hide sl
        with dissolve
        show dv smile pioneer2 at cright with dissolve
        if ds_day2_dv_ultim == 1:
            dv "Ты победил в споре и турнире."
        else:
            dv "Молоток!"
        hide dv with dissolve
        "Она ткнула меня кулаком в плечо и, развернувшись, растворилась в толпе."

    elif ds_my_rival_final.take == 'dv':
        $ lp_dv += 1
        th "Я выиграл!"
        play music music_7dl["sheiscool"] fadein 3
        th "Выиграл?"
        th "Выиграл!!!"
        show dv normal pioneer2 with dspr
        "Ещё несколько часов назад я не мог и представить себя таким счастливым!"
        "Я победно смотрел на Алису, ещё не веря до конца в свою удачу…"
        "А вокруг уже все поздравляли меня с победой, и Электроник писал моё имя в своей таблице!"
        scene
        call show_tournament_table
        th "Моё имя!!!"
        th "Я выиграл турнир!"
        scene bg int_dining_hall_sunset with dissolve
        "Словно и не было этих часов переживаний и напряжения…"
        "Я стал лёгким как пёрышко…"
        "Я как будто научился летать!"
        if ds_day2_dv_ultim == 1:
            th "Я выиграл пари!!!"
        if ds_day2_dv_ultim == 2:
            show dv shy pioneer2 with dissolve
            "Алиса была готова на месте провалиться — до такой степени она покраснела."
            "Поймав её взгляд, я подмигнул, сделав препохабнейшую морду лица."
            show dv rage pioneer2 with dspr
            "Её перекосило."
            "А я расхохотался."
            "Вечер сегодня определённо мой!"
        else:
            show dv smile pioneer2 with dissolve
            "А Алиса наконец поднялась со своего места и, проходя мимо меня, хлопнула по плечу."
            dv "Поздравляю!"
            "И от этих слов мне стало так радостно!"
            th "Я победил Алису!!!"
        hide dv with dissolve

    elif ds_my_rival_final.take == 'mi':
        $ lp_mi += 2
        $ ds_day2_mi_snap = True
        show mi smile pioneer with dspr
        mi "Ты и правда победил! Ты молодец!"
        play music music_7dl["tellyourworld"] fadein 3
        "Воскликнула она."
        show mi normal pioneer with dspr
        mi "Только не думай, что тебе это поможет!"
        "Строго сказала девочка."
        mi "В следующий раз я тебя обязательно обыграю!"
        "Конечно. Сколько угодно. Но — в следующий раз."
        "А сейчас…"
        "В таблице красовалось моё имя, выведенное толстым красным маркером."
        "Мику схватила меня за руку и потащила за собой."
        me "Эй!"
        mi "Да быстрее же ты!"
        "Ничего не понимая, я поспешил за ней."
        me "И что?"
        "Мы остановились у доски, и девочка кому-то замахала."
        mi "Дядя Боря-сенсей! Мы здесь!"
        if ('sport_area' in list_voyage_7dl):
            th "Что ей может понадобиться от Саныча?"
            "С любопытством подумал я."
        show ba normal uniform at cleft behind mi # Здесь не надо meet поставить? ## "знакомство" уже состоялось к этому моменту либо при посещении спортплощадки, либо по завершению обхода на экстраде заочно
        show mi smile pioneer at right
        with dissolve
        ba "Да, мал{b}а{/b}я, чего звала?"
        mi "У вас ещё есть кадры?"
        show ba smile uniform with dspr
        ba "Для тебя, мал{b}а{/b}я, сколько влезет."
        "Из ниоткуда в его руках появился жёсткий коричневый чехол для фотоаппарата, а оттуда…"
        "Старый добрый «компакт-автомат», плёночный."
        "Я чуть было не сказал «раритет», но видно было, что машинка рабочая."
        ba "Только без вспышки сегодня, так что становитесь как-нибудь, где посветлее."
        "Мику улыбнулась и развернула кипучую деятельность, тормоша всех и переставляя."
        "В результате полотнище таблицы было снято и перенесено поближе к окошку, где Шурик и Электроник держали его нарастяг."
        scene bg int_dining_hall_sunset with dissolve
        with dissolve
        scene
        call show_tournament_table
        "Мику встала рядом."
        show mi normal pioneer at cleft with dissolve
        "Ещё ближе."
        "Ещё чуточку."
        show mi dontlike pioneer with dspr
        mi "Сень!"
        "Наконец не выдержала она."
        mi "Я же с тобой фотографируюсь! А ну, быстро обними девушку."
        me "Но я…"
        "Я вздохнул."
        th "Я не помню, когда я последний раз так фотографировался с кем-то."
        th "Я не умею никого обнимать для фото…"
        show mi normal pioneer with dspr
        mi "Смелее же, ну!"
        "Она нетерпеливо пошевелила плечиком."
        scene cg d2_mi_polaroid_7dl
        with dissolve
        "И я, вздохнув, положил ей на плечо руку."
        "Неловко — как и чувствовал себя — неловко."
        "Свисающая кисть, нечувствительные пальцы."
        "Как фотографировался бы с другом, а не с девушкой."
        "До меня слишком поздно дошло, что девушку надо обнимать за талию, а не вот так."
        "Но… поздно!"
        play sound sfx_7dl["snap"]
        scene
        $ renpy.show("cg d2_mi_polaroid_7dl", what = Sepia("cg d2_mi_polaroid_7dl"))
        show PolaroidFrame_7dl
        with flash
        pause(3)
        me "Сыыыр."
        "Запоздало опомнился я."
        scene bg int_dining_hall_sunset
        show mi laugh pioneer at cleft
        with dissolve
        mi "Хи-хи-хи."
        mi "Сенечка, ты чудо."
        hide mi with moveoutleft
        "Она рассмеялась и убежала."

    elif ds_my_rival_final.take == 'us':
        $ lp_us -= 1
        th "Я выиграл!"
        th "Выиграл?"
        th "Выиграл!!!"
        play music music_7dl["genki"] fadein 3
        "Бац!" with vpunch
        with flash_red
        show us calml pioneer with dissolve
        us "И ничего ты не выиграл!"
        "Она хмуро смотрела на меня снизу вверх."
        us "Ты играл неправильно, переигрываем!"
        me "Что это значит, «неправильно»?"
        show us dontlike pioneer with dspr
        me "Я выиграл турнир! {w}Как я могу играть неправильно?"
        us "Молча! Ты жульничал!"
        "Она топнула ногой."
        us "Ты неправильно играл и жульничал!"
        if ds_day2_walk == 1:
            th "Неужели про крап узнала? Но как?"
            th "Если она сейчас всем про него раcскажет, меня линчуют на ближайшей осине."
        us "Ты плохо мне поддавался."
        "А. Ну, это меняло всё дело."
        hide us with dissolve
        "Я расхохотался и отошёл."
        show dv smile pioneer2 with dissolve
        "А Алиса наконец поднялась со своего места и, проходя мимо меня, хлопнула по плечу."
        dv "Поздравляю!"
        "И от этих слов мне стало так радостно!"
        th "Я победил!!!"
        hide dv with dissolve

    elif ds_my_rival_final.take == 'sh':
        stop ambience
        show sh rage pioneer with dissolve
        sh "Значит, победил?"
        play music music_7dl["dead_silence"] fadein 3
        "Медленно произнёс он."
        "Он так странно стоял, что я никак не мог разглядеть его глаз из-за бликов на очках."
        show sh serious pioneer with dspr
        "Да и сама его поза…"
        "Почему-то вдруг вспомнился персонаж Элайджи Вуда из «Города Грехов»."
        "Вроде бы, ничего такого сверхъестественного не делал, но тревогу внушал примерно так же — одним появлением на экране."
        "И Шурик заставлял меня тревожиться."
        sh "То есть думаешь, что можно просто так прийти и выиграть мой турнир?"
        scene black
        show sh rage pioneer close
        with diam
        sh "Да кто ты такой вообще?"
        sh "Ведёшь себя, будто тебе уже давно не семнадцать лет."
        show sh rage pioneer close with dspr
        sh "А может быть, ты…"
        scene
        $ renpy.show("bg int_dining_hall_sunset", what = Noir("bg int_dining_hall_sunset"))
        show sh rage pioneer close with dspr:
            xalign .5 yalign .7 zoom 0.7
            ease 0.3 yalign .4 zoom 1.25
        "Он сделал резкий шаг в мою сторону и протянул руку."
        mt "Шурик!"
        stop music fadeout 3
        play ambience ambience_dining_hall_full fadein 5
        show blinking
        scene bg int_dining_hall_sunset with dissolve
        with diam
        show sh upset pioneer with dissolve
        "Наваждение момента исчезло, Шурик из зловещей фигуры превратился обратно в обычного, чуть рассеянного, парня."
        "Серые, давящие стены уступили место красноватому свету катящегося на закат светила."
        "И самое главное —"
        "Ведь я же победитель!"
        hide sh with dissolve
        scene
        call show_tournament_table
        "Электроник внёс моё имя в список победителей."
        el "А после ужина…"
        scene bg int_dining_hall_sunset with dissolve
        "Ольга Дмитриевна заткнула ему рот рукой."
        th "Правильно, пусть будет сюрпризом. А для спойлерщиков в аду отдельный котёл стоит."

    elif ds_my_rival_final.take == 'mz':
        "Реакция Жужелицы была обескураживающей."
        "Её не было."
        "Но меня это не смущало."
        "Самое главное, что я победил!"
        "Остальные пусть думают и делают что хотят."
        "Даже Алиса."
        "Сейчас-то ей никто не поверит."
        "И это, пожалуй, радует больше всего."
# ---------------------------------------------------- \\ Диалоги

    stop music fadeout 3
    jump ds_cards_prepare_transition_to_supper                                            # ушли ужинать

# ======================================================================================================================
#                                          ОБЩИЕ МЕТКИ ПО ОБРАБОТКЕ ТУРНИРА
# ======================================================================================================================

# ----------------------------------------------------------------------------------
# ОПРЕДЕЛЯЕМСЯ С ОЧЕРЁДНОСТЬЮ ПЕРВОГО ХОДА В КОНЕ
label ds_cards_stipulation:
    scene bg int_dining_hall_sunset with dissolve
    python:
        ds_spr_rival = [ds_spr_my_rival,ds_emo_my_rival,ds_acc_my_rival,ds_clot_my_rival]
        ds_spr_my_riv_1 = " ".join(ds_spr_rival)
        renpy.show(ds_spr_my_riv_1,[ds_pos_my_rival])
        renpy.transition(dspr)
    ds_nick_my_rival "Кто первый ходит?"

    $ ds_whose_first_move = renpy.random.choice(['rival', 'player'])
    pause(1)
    if ds_tournament_state == "1_round_start":                             # если первый тур
        "Я достал из нагрудного кармана пятирублёвую монетку — очень надеюсь, что ни у кого не возникнет вопросов касательно номинала — и подбросил её в воздух."
        "Сомнительная честь сделать первый ход выпала"
    elif ds_tournament_state == "semifinal_start":                         # если полуфинал
        "Я снова подбросил монетку в воздух."
        "В этот раз не повезло"
    elif ds_tournament_state == "final_start":                             # если финал
        "В третий раз закинул он невод… В смысле, подбросил монетку."
        "Похоже, первому ходить придётся"
    if ds_whose_first_move == 'rival':
        extend " %(ds_name_my_rival_d)s."
    elif ds_whose_first_move == 'player':
        extend " мне."

    return

# ----------------------------------------------------------------------------------
# Победа Семёна в очередной игре тура
label ds_day2_one_play_win:
    window auto
    $ ds_day2_my_win += 1                                                  # +1 к победам Семёна
    $ ds_day2_game_played_out += 1                                         # +1 результативная игра
    $ ds_day2_result_current_game = 1                                      # победа Семёна
    jump ds_day2_checking_scores                                           # считаем очки

# ----------------------------------------------------------------------------------
# Поражение Семёна в очередной игре тура
label ds_day2_one_play_fail:
    window auto
    $ ds_day2_rival_win += 1                                               # +1 к победам соперника
    $ ds_day2_game_played_out += 1                                         # +1 результативная игра
    $ ds_day2_result_current_game = 2                                      # победа соперника
    jump ds_day2_checking_scores                                           # считаем очки

#-----------------------------------------------------------------------------------
# НИЧЬЯ в очередной игре тура
label ds_day2_one_play_draw:
    window auto
    $ show_cards_alt()
    $ renpy.transition(dissolve)
    el "Ничья! Играйте ещё раз."
    if ds_tournament_state == "1_round_start":                             # если первый тур
        jump ds_day2_1_tour_re_game                                        # играем первый тур
    elif ds_tournament_state == "semifinal_start":                         # если полуфинал
        jump ds_day2_semifinal_re_game                                  # играем полуфинал
    elif ds_tournament_state == "final_start":                             # если финал
        jump ds_day2_final_re_game                                      # играем финал

#-----------------------------------------------------------------------------------
# Анилизируем счёт по играм в этапе
label ds_day2_checking_scores:
    scene bg int_dining_hall_sunset with dissolve
    if ds_day2_my_win == ds_day2_rival_win:                                                   # если счёт равный
        if ds_day2_game_played_out == 0:                                                       # ещё не играли (0:0)
            if ds_day2_gamblers_final[0].take == 'me':                                         # если 1-й игрок — Семён
                $ ds_day2_upper_gambler_name = "Семёном"
                $ ds_day2_bottom_gambler_name = ds_name_my_rival_t
            else:
                $ ds_day2_upper_gambler_name = ds_name_my_rival_t
                $ ds_day2_bottom_gambler_name = "Семёном"
            show el normal pioneer far at left with dissolve
            el "До начала финальной игры между %(ds_day2_upper_gambler_name)s и %(ds_day2_bottom_gambler_name)s осталась минута, счёт по-прежнему ноль-ноль."
            "Электроник комментировал игру, как умел."
            hide el with dissolve
            return
        else:                                                                                   # если 1:1
            call ds_day2_current_game_end_compare_hands                                        # сравнение комбинаций по итогам игры
            show el serious pioneer far at left with dspr
            el "Итак, по итогам двух игр у нас пока ничья; победитель определится в решающей игре."
            el "А кто будет ходить первым — сейчас разыграем, и поможет нам в этом портативный генератор случайных чисел."
            "Электроник выудил из кармана монету."
            el "Орёл? Решка?"
            menu:
                "Орёл":
                    $ ds_whose_first_move_choice = 1
                "Решка":
                    $ ds_whose_first_move_choice = 0
            $ ds_whose_first_move_random = renpy.random.choice([0, 1])
            if ds_whose_first_move_random == 0:
                "Эл подбросил монетку, выпала решка."
            else:
                "Подброшенная монета упала орлом."
            $ renpy.block_rollback()                                                                # блокируем роллбак
            if ds_whose_first_move_choice == ds_whose_first_move_random:
                if ds_name_my_rival_i == "Шурик":
                    el "Надо же, угадал. Первым ходить будет Шурик{nw}"
                else:
                    el "Надо же, угадал. Первой ходить будет %(ds_name_my_rival_i)s{nw}"
                if ds_whose_first_move == 'player':
                    extend ", как и в первой игре."
                else:
                    extend ", как и во второй игре."
                $ ds_whose_first_move = 'rival'
            else:
                el "Мимо. Так что первый ход — твой{nw}"
                if ds_whose_first_move == 'player':
                    extend ", как и во второй игре."
                else:
                    extend ", как и в первой игре."
                $ ds_whose_first_move = 'player'
            scene bg int_dining_hall_sunset with dissolve
            jump ds_day2_transition_to_game
    elif ds_day2_my_win > ds_day2_rival_win:                                                  # Семён ведёт в счёте
        call ds_day2_current_game_end_compare_hands                                            # сравнение комбинаций по итогам игры
        if ds_day2_game_played_out == 1:                                                       # по итогам первой игры
            show el normal pioneer far at left with dspr
            if ds_whose_first_move == 'rival':                                                 # если первым ходил соперник
                el "Семён, теперь первым будешь ходить ты."
                $ ds_whose_first_move = 'player'                                               # то первым ходит Семён
            else:                                                                               # если ходил Семён
                el "Право первого хода переходит к %(ds_name_my_rival_d)s."
                $ ds_whose_first_move = 'rival'                                                # то первым ходит соперник
            scene bg int_dining_hall_sunset with dissolve
            jump ds_day2_transition_to_game                                                    # переход к игре
        else:                                                                                   # по итогам тура
            show el normal pioneer far at left with dspr
            el "Семён выигрывает у %(ds_name_my_rival_r)s со счётом %(ds_day2_my_win)d-%(ds_day2_rival_win)d."
            scene bg int_dining_hall_sunset with dissolve
            if ds_tournament_state == "final_start":                                           # если финал
                jump ds_day2_final_win_end                                                 # победа в финале
            elif ds_tournament_state == "semifinal_start":                                     # если полуфинал
                jump ds_day2_semifinal_win_end                                             # победа в полуфинале
            elif (ds_tournament_state == "1_round_start"):                                     # если первый тур
                jump ds_day2_participate_win_end                                           # победа в 1 туре
    else:                                                                                       # соперник выигрывает
        call ds_day2_current_game_end_compare_hands                                            # сравнение комбинаций по итогам игры
        if ds_day2_game_played_out == 1:                                                       # по итогам первой игры
            show el normal pioneer far at left with dspr
            if ds_whose_first_move == 'rival':                                                 # если первым ходил соперник
                el "В следующей игре первым будет ходить Семён."
                $ ds_whose_first_move = 'player'                                               # то первым ходит Семён
            else:                                                                               # если ходил Семён
                el "%(ds_name_my_rival_i)s, теперь первый ход — твой."
                $ ds_whose_first_move = 'rival'                                                # то первым ходит соперник
            scene bg int_dining_hall_sunset with dissolve
            jump ds_day2_transition_to_game                                                    # переход к игре
        else:                                                                                   # по итогам тура
            show el normal pioneer far at left with dissolve
            el "%(ds_name_my_rival_i)s одерживает победу со счётом %(ds_day2_rival_win)d-%(ds_day2_my_win)d."
            scene bg int_dining_hall_sunset with dissolve
            if ds_tournament_state == "final_start":                                           # если финал
                jump ds_day2_final_fail_end                                                # поражение в финале
            elif ds_tournament_state == "semifinal_start":                                     # если полуфинал
                jump ds_day2_semifinal_fail_end                                            # поражение в полуфинале
            elif (ds_tournament_state == "1_round_start"):                                     # если первый тур
                jump ds_day2_participate_fail_end                                          # поражение в 1 туре


#-----------------------------------------------------------------------------------
# Возвращаемся к обратно к игре на соответствующий этап
label ds_day2_transition_to_game:                                                    # переход к игре
    if ds_tournament_state == "final_start":                                         # если финал
        jump ds_day2_final_re_game                                                   # играем финал
    elif ds_tournament_state == "semifinal_start":                                   # если полуфинал
        jump ds_day2_semifinal_re_game                                               # играем полуфинал
    elif (ds_tournament_state == "1_round_start"):                                   # если первый тур
        jump ds_day2_1_tour_re_game                                                  # играем 1 тур

#-----------------------------------------------------------------------------------
# Результат ИГРЫ (сравниваем и оцениваем комбинации)
label ds_day2_current_game_end_compare_hands:                                      # Результат текущей игры
    $ ds_day2_current_rout_status = 0                                              # текущая игра закончена
    if ds_day2_result_current_game == 1:                                           # победа Семёна
        $ ds_day2_summary_poker_1, ds_day2_summary_poker_2 = ds_comparison_poker_hands(ds_my_poker_hand, ds_rival_poker_hand, 'me', ds_spr_my_rival)
        if ds_day2_game_played_out == 1:                                           # сыграли раз
            $ ds_day2_current_rout_status = 1                                      # Семён выиграл 1-ю игру
        elif ds_day2_game_played_out == 2:                                         # сыграли два раза
            if ds_day2_rival_win == 1:                                             # соперник выиграл один раз
                $ ds_day2_current_rout_status = 2                                  # Семён отыгрался

    elif ds_day2_result_current_game == 2:                                         # победа соперника
        $ ds_day2_summary_poker_1, ds_day2_summary_poker_2 = ds_comparison_poker_hands(ds_rival_poker_hand, ds_my_poker_hand, ds_spr_my_rival, 'me')
        if ds_day2_game_played_out == 1:                                           # сыграли раз
            $ ds_day2_current_rout_status = 3                                      # соперник выиграл 1-ю игру
        elif ds_day2_game_played_out == 2:                                         # сыграли два раза
            if ds_day2_my_win == 1:                                                # Семён выиграл один раз
                $ ds_day2_current_rout_status = 4                                  # соперник отыгрался

    $ ds_day2_result_current_game = 0                                              # результат текущей игры = 0 (ничья)
    "%(ds_day2_summary_poker_1)s"
    "%(ds_day2_summary_poker_2)s"

    if ds_day2_current_rout_status in [1,2,3,4]:                                   # если игра не закончена
        call ds_day2_current_game_ending_dialogs                                   # вызов диалога по текущей ситуации
    else:
        pass
    return

#-----------------------------------------------------------------------------------
# диалоги по итогам очередной игры (выиграл/проиграл-сравнял счёт)
# сортировка — сначала по персонажам, потом — по ситуациям (0-проверка, 1 — Семён выиграл 1-ю, 2 — Семен сравнял счёт, 3 — соперник выиграл 1-ю, 4 — соперник сравнял счёт)
# ---------------------------------------------------------
# тут же "накручиваем" скилл соперникам по итогам очередной игры

label ds_day2_current_game_ending_dialogs:
# Лена
    if ds_spr_my_rival == 'un':
        if ds_day2_current_rout_status == 1:                   # если Семён выиграл первый раз
            if ds_day2_gambler_behavior != 'succumb':          # если не "поддавки"
                $ ds_day2_gambler_skill += 1                     # увеличиваем навык

            "Видимо, скилл удачи у Лены прокачан ещё ниже, чем у меня."
            show un smile pioneer at cright with dissolve
            "Но, похоже, её это не слишком расстраивает."
            un "Молодец."
            "Похвалила Лена."
            me "Спасибо."
            show un shy pioneer at cright with dspr
            "И через секунду залилась краской."


        elif ds_day2_current_rout_status == 2:                 # если Семён отыгрался
            if ds_day2_gambler_behavior != 'succumb':          # если не "поддавки"
                $ ds_day2_gambler_skill += 1                     # увеличиваем навык

            show un shy pioneer at cright with dissolve
            "Взгляд Лены метался от меня и до лежащих на столе карт, и так несколько раз."
            "Она явно хотела что-то сказать, но не могла перебороть смущение."
            "Не понимаю, что могло вогнать эту, пару минут назад серьёзную, девочку в краску."
            dreamgirl "Идиот."
            "Буркнуло подсознание."
            "В любом случае, тянуть из Лены слова клещами я не стану."


        elif ds_day2_current_rout_status == 3:                 # и она выиграла первый раз
            if ds_day2_gambler_behavior == 'succumb':          # если "поддавки"
                $ ds_day2_gambler_skill += 1                     # увеличиваем навык

            if ds_day2_gambler_behavior == 'succumb':
                "Мда. Я показал явно не лучший уровень игры. И Лена явно это заметила."
                show un serious pioneer at cright with dissolve
                "Её осуждающий взгляд пробудил во мне неясное чувство вины."
                "Будто я виноват в том, что проиграл."
                dreamgirl "Ещё как виноват."
                dreamgirl "Девочка поддавалась тебе, но ты всё равно облажался."
                th "Доказательства?"
                dreamgirl "Налицо."
                "Неясно ответил внутренний голос и замолчал."
            else:
                "Лена оказалась серьёзным противником, спрятавшим пару тузов в рукаве."
                show un shy pioneer at cright with dissolve
                "Не ожидал от неё такого упорства."
                "Видимо, она и сама была удивлена."


        elif ds_day2_current_rout_status == 4:                 # и она отыгралась
            if ds_day2_gambler_behavior == 'succumb':          # если "поддавки"
                $ ds_day2_gambler_skill += 1                     # увеличиваем навык

            if ds_day2_gambler_behavior == 'succumb':          # если "поддавки"
                show un sad pioneer at cright with dissolve
                "Сама Лена не слишком радовалась маленькой победе — наоборот, она глядела на меня так, словно провинилась в чём-то."
                dreamgirl "Не будь дубом и приободри."
                th "Без тебя знаю."
                me "Молодец, Лен. Хорошо сыграла."
                show un shy pioneer at cright with dspr
                un "С-спасибо."
                "Голос у девочки взволнованный, она не верила в то, что произошло."
                "Потому и вздрогнула, когда Электроник громко произнёс её имя."
            else:
                "Похоже, Лена не намерена сдаваться."
                show un smile pioneer at cright with dissolve
                un "Не надейся на лёгкую победу."
                "Только что она сидела, смутившись, а теперь ещё подзадоривает меня!"
                "Вот что азарт с людьми делает."
                show un shy pioneer at cright with dspr
                "Впрочем, эффект оказался недолгим."

# Славя
    elif ds_spr_my_rival == 'sl':
        if ds_day2_current_rout_status == 1:                   # если Семён выиграл первый раз
            $ ds_day2_gambler_skill += 1                     # увеличиваем навык

            show sl smile pioneer at cright with dissolve
            "Похоже, что Славя нисколько не огорчена поражением."
            sl "Всё-таки карты не моё."
            me "Тебе просто не повезло, вот и всё."
            show sl laugh pioneer at cright with dspr
            sl "Дело не в везении, я правда не умею!"
            show sl smile2 pioneer at cright with dspr
            sl "Много раз пробовала, всё без толку."
            sl "Не понимаю я смысла этой глупой игры."
            me "Так зачем играешь?"
            show sl smile pioneer at cright with dspr
            sl "Лагерное мероприятие, Семён. Все обязаны присутствовать."






        elif ds_day2_current_rout_status == 2:                 # если Семён отыгрался
            $ ds_day2_gambler_skill += 1                     # увеличиваем навык

            show sl smile pioneer at cright with dissolve
            sl "Ведь можешь же, когда захочешь!"
            me "Мне просто повезло."
            show sl normal pioneer at cright with dspr
            "Славя явно хотела услышать от меня большего, но я не знал, что тут ещё добавить."
            sl "Вот сейчас и узнаем — везение или талант."
            th "Второе, однозначно."
            th "Талантливый неудачник."
            "Славя словно услышала мои мысли и постаралась приободрить меня."
            show sl happy pioneer at cright with dspr
            sl "Выше нос!"



        elif ds_day2_current_rout_status == 3:                 # и она выиграла первый раз


            show sl surprise pioneer at cright with dissolve
            me "Что-то не так?"
            show sl normal pioneer at cright with dspr
            sl "Нет, просто…"
            sl "Я не очень хорошо играю в карты."
            me "Насколько «не очень»?"
            show sl sad pioneer at cright with dspr
            sl "Много раз пробовала, всё без толку."
            sl "Не понимаю я смысла этой глупой игры."
            "А мне казалось, что хуже меня игрока здесь нет."
            "Активистка преуспела во многом, кроме азартных игр."
            "Но даже она смогла меня обыграть."

        elif ds_day2_current_rout_status == 4:                 # и она отыгралась

            show sl angry pioneer at cright with dissolve
            sl "Ты нарочно, да?"
            "А я, стараясь сохранить невозмутимое выражение лица, ответил:"
            me "Нисколько."
            sl "Неправда! Ты же знаешь, что я…"
            pause(1)
            show sl normal pioneer at cright with dspr
            sl "Ладно, не важно."

# Алиса
    elif ds_spr_my_rival == 'dv':
        if ds_day2_current_rout_status == 1:                   # если Семён выиграл первый раз
            $ ds_day2_gambler_skill += 1                     # увеличиваем навык

            show dv surprise pioneer2 at cright with dissolve
            "Рыжая находилась в лёгком шоке."
            "Что тут скажешь — я умею удивлять.{w} Особенно себя."
            me "Мадмуазель готова пасть на колени и рыдать от поражения?"
            show dv smile pioneer2 at cright with dspr
            "Моя реплика вывела Алису из оцепенения и раззадорила."
            dv "Ещё чего!"
            show dv angry pioneer2 at cright with dspr
            dv "Мадмуазель готова съездить кавалеру по физиономии."
            "Я едва не расхохотался."

        elif ds_day2_current_rout_status == 2:                 # если Семён отыгрался
            $ ds_day2_gambler_skill += 1                     # увеличиваем навык
            $ ds_day2_gambler_behavior = 'gamble'          # и начинает рисковать

            show dv guilty pioneer2 at cright with dissolve
            "Приятно видеть, как маска надменности спадает с лица Двачевской."
            "Я даже говорить ничего не стал — молча подобрал эту самую маску и примерил на себя."
            show dv angry pioneer2 at cright with dspr
            "Алисе это не понравилось, Алиса сжала кулаки."
            if herc or loki:
                "А мне плевать."
                "Угрозы Двачевской меня не пугают."
                "Я с вызовом продолжил глядеть на рыжую."
                pause(1)
                show dv guilty pioneer2 at cright with dspr
                "Победителем в гляделки стал я."
                "Алиса разжала кулаки и отвела взгляд."
                if herc:
                    "Мне даже стало немного стыдно за то, что, кажется, обидел девушку."
                    "Но не настолько, чтобы торопиться извиняться."
                    "Алиса должна сама понять, что сделала не так."

                elif loki:
                    dreamgirl "Ну вот, обидел девочку."
                    th "Она заслужила, ибо нефиг."

            else:
                "Я поднял руки в примирительном жесте."
                me "Тише-тише, я просто пошутил."
                dv "Ещё одна такая шутка…"
                me "Понял, не дурак."




        elif ds_day2_current_rout_status == 3:                 # и она выиграла первый раз
            $ ds_day2_gambler_behavior = 'defense'              # садится в оборону

            show dv grin pioneer2 at cright with dissolve
            "Алиса с ехидной усмешкой глядела на меня."
            "Наверняка радуется, что получила подтверждение своим словам."
            "И это бесит."
            me "Не рановато празднуешь победу, Двачевская?"
            show dv laugh pioneer2 at cright with dspr
            dv "По-моему — нет."
            "Я уже собрался плюнуть ядом в рыжую, как услышал реплику внутреннего голоса."
            dreamgirl "Балда, она же специально провоцирует тебя, а ты ведёшься!"
            dreamgirl "Если хочешь утереть нос Двачевской, тебе нужно сохранять спокойствие."
            th "В этом есть смысл."
            show dv normal pioneer2 at cright with dspr
            "Алиса как-то разочарованно хмыкнула — явно ждала другой реакции."
            th "А вот фиг тебе."

        elif ds_day2_current_rout_status == 4:                 # и она отыгралась
            $ ds_day2_gambler_behavior = 'gamble'          # и начинает рисковать

            show dv laugh pioneer2 at cright with dissolve
            "Дваче чертовски довольна собой."
            me "Чего лыбу давишь?"
            show dv grin pioneer2 at cright with dspr
            dv "А нельзя?"
            dreamgirl "Можно!"
            th "Ты вообще на чьей стороне?"
            dreamgirl "Своей собственной."
            dreamgirl "А ты, балбес, не понял, что девочка заигрывает с тобой."
            th "Двачевская? Заигрывает?"
            th "Никогда не поверю. Не тот типаж."
            dreamgirl "Пф… Больно ты в них разбираешься."
            "Фыркнул внутренний голос и смолк."

# Мику
    elif ds_spr_my_rival == 'mi':

        if ds_day2_current_rout_status == 1:                   # если Семён выиграл первый раз
            $ ds_day2_gambler_skill += 1                     # увеличиваем навык

            stop music fadeout 2
            show mi smile pioneer at cright with dissolve
            mi "Молодец, Сенечка. Ты хорошо играешь."
            play music music_7dl["what_am_i_doing_here"] fadein 1
            me "Это всё везение."
            show mi shocked pioneer at cright with dspr
            mi "Правда? А я решила, что ты — опытный игрок."
            "Если у Мику такая тактика — наносить каждым словом удар по моей самооценке — у неё это получилось."
            dreamgirl "Можно подумать, она у тебя была."
            show mi sad pioneer at cright with dspr
            mi "А мне вот совсем не везёт в карты."
            mi "Я не умею в них играть! Не понимаю!{w} Или просто глупая."
            me "Ты не глупая."
            "Хотя мы не так хорошо знакомы, чтобы я мог это утверждать."
            dreamgirl "Так узнай её {i}поближе{/i}."
            "По спине аж мурашки прошли."
            "Закравшиеся в голос внутреннего пошляка интонации напомнили о нашей очаровательной медсестре."

            me "Просто у каждого человека что-то получается лучше, чем у другого."
            if loki:
                me "Я не понаслышке знаю, что научиться играть даже на одном инструменте непросто, а ты смогла сразу на нескольких."
                me "Это не просто талант, это упорный труд."
                me "Глупые такого не умеют."
                me "Как правило они…"
                "Слова комом застряли в горле."
                mi "Как правило — что?"
                me "Трудности их быстро ломают."
                th "Порой ещё и физически."
                me "Они застревают на одном месте и найдут тысячу оправданий, чтобы ныть о несбывшемся вместо хотя бы одной причины двигаться вперёд, к своей мечте."
                dreamgirl "Прямо как?.."
                th "Прямо как я."
            elif herc:
                me "Например у меня не сложилось с музыкой."
                th "Зато во владении холодным и огнестрельным оружием я преуспел."
                me "А у тебя получилось."
                me "Талант то или упорство — не суть."
                me "Глупые такого не умеют."
            elif dr:
                me "Азартные игры не твоё. Только и всего."

            mi "Наверное, ты прав."
            show mi smile pioneer at cright with dspr
            mi "Нет, так и есть!"
            show mi smile pioneer at cright with dspr
            mi "Вот уж кто действительно умеет играть в карты, так это Алиса."
            "Двачевская-то?"

            scene bg ext_dining_hall_near_day
            show dv smile pioneer2
            show prologue_dream
            with flash

            "Нисколько не сомневался."
            "Человек с такой самодовольной миной не стал бы предлагать пари, будучи не уверенным в победе."
            if (ds_day2_dv_ultim != 1) and (ds_day2_walk == 1):
                dreamgirl "А что ж ты тогда спорить-то не стал, шулер?"

            scene bg int_dining_hall_sunset
            show mi shy pioneer at cright
            with flash

            show mi normal pioneer at cright with dspr
            mi "Мы с ней как-то играли, и я проиграла шесть раз подряд!"

            menu:
                "Спросить про игру":

                    $ lp_mi += 1

                    me "Ты и в карты? С Двачевской?"
                    me "Ты, как там по вашему… камикадзе?!"
                    show mi laugh pioneer at cright with dspr
                    mi "Скажешь тоже! Оно само как-то так вышло!"
                    "Видимо это норма, что у женщин «оно» всегда само."
                    show mi normal pioneer at cright with dspr
                    mi "Я тогда сидела в клубе и расписывала ноты одной из моих песен для пианино."
                    mi "Очень красиво получилось. По-моему, даже лучше, чем в оригинале. Мелодичнее, эмоциональнее!"
                    show mi smile pioneer at cright with dspr
                    mi "Так вот, точно помню, что то была среда!"
                    show mi surprise pioneer at cright with dspr
                    mi "Хотя нет, меня в тот день Ульяна…"
                    "Я уже начал жалеть, что решил поддержать диалог, перешедший в монолог, когда Мику сама вернулась к теме."
                    show mi normal pioneer at cright with dspr
                    mi "В общем, неважно!"

                    scene bg int_musclub_day
                    show prologue_dream
                    with flash

                    mi "Я уже почти закончила с песней…"
                    mi "…как вдруг в клуб ворвалась взъерошенная Алиса!"

                    play sound sfx_open_door_strong
                    with vpunch
                    show dv scared pioneer2 far at center behind prologue_dream
                    with moveinright

                    dv "{i}Если Шляпа зайдёт — меня тут нет!{/i}"

                    hide dv with moveoutleft
                    play sound sfx_close_door_clubs_nextroom
                    with vpunch

                    mi "И спряталась в подсобке."

                    scene bg int_dining_hall_sunset
                    show mi shocked pioneer at cright
                    with fade

                    mi "Я сначала перепугалась: что такого сделала Алиса, чтобы настолько сильно испугаться вожатой?"
                    show mi happy pioneer at cright with dspr
                    mi "Ольга Дмитриевна же не злая. Она строгая, но добрая."
                    "Мику — прямо сама наивность."
                    dreamgirl "Воспользуешься?"
                    th "У тебя, смотрю, всё сплошные хиханьки да хаханьки, да всё об одном."
                    dreamgirl "О добром, вечном."
                    show mi dontlike pioneer at cright with dspr
                    mi "В общем, Алиса меня напугала."
                    show mi upset pioneer at cright with dspr
                    mi "Я замерла и всё прислушивалась: вдруг действительно кто-то идёт?"
                    show mi normal pioneer at cright with dspr
                    mi "Минут десять так сидела, пока Алиса не решила выбраться из укрытия."
                    show mi laugh pioneer at cright with dspr
                    mi "Ты бы видел её лицо!"
                    me "Представляю…"

                    scene bg int_musclub_day
                    show prologue_dream
                    with flash
                    show dv surprise pioneer2 at fleft behind prologue_dream with moveinleft
                    show dv surprise pioneer2 at fleft behind prologue_dream with dissolve
                    show dv normal pioneer2 at fleft behind prologue_dream with dspr

                    mi "Когда Алисочка собралась уходить, я её спросила:"
                    show dv normal pioneer2 at cright behind prologue_dream with move
                    mi "{i}Ой, Алиса, а что ты натворила? Зачем Ольге-сан тебя искать?{/i}"
                    show dv smile pioneer2 at cright behind prologue_dream with dspr
                    mi "В ответ она просто отмахнулась, представляешь!"
                    mi "Сказала, что потом как-нибудь расскажет, что у неё дело какое-то незаконченное."
                    "Ставлю на то, что Двачевская тупо отмазывалась."
                    "Болтливость Мику отталкивает людей."
                    mi "{i}А что за дело? Срочное? Могу я…{/i}"
                    show dv laugh pioneer2 at cright behind prologue_dream with dspr
                    dv "{i}Нет. Это секрет!{/i}"
                    mi "{i}Ну Алиса-а-а! Мне же интересно. Ну расскажи!{/i}"
                    show dv grin pioneer2 at cright behind prologue_dream with dspr
                    dv "{i}А давай пари?{/i}"
                    dv "{i}Выиграешь у меня, и я расскажу, что за дело.{/i}"
                    mi "И достала карты."
                    mi "{i}Ой, а я не умею. То есть я никогда не пробовала, поэтому…{/i}"
                    show dv smile pioneer2 at cright behind prologue_dream with dspr
                    dv "{i}Не страшно!{/i}"
                    show dv laugh pioneer2 at cright behind prologue_dream with dspr
                    dv "{i}Не хочешь — научим. Не можешь — заставим!{/i}"

                    scene bg int_dining_hall_sunset
                    show mi smile pioneer at cright
                    with flash2

                    mi "Вот такая вот история."
                    show mi smile pioneer at cright with dspr
                    mi "Алиса пыталась меня по ходу игры научить, но я так ничего и не поняла!"
                    me "Ясно."
                    $ lp_dv += 1
                    me "А Двачевская — не такая вредина, какой выглядит."
                    stop music fadeout 3
                    mi "Алисочка очень хорошая. Просто её нужно получше узнать."

                "Игнорировать":

                    $ lp_mi -= 1
                    stop music fadeout 3
                    me "Ясно."
                    show mi sad pioneer at cright with dspr
                    pause(1)
                    hide mi with dissolve

                    #if not(final):
                    #    "Я отвернулся к другим столам, посмотреть, как играет кто-нибудь из моих потенциальных соперников."
                    #    "Мику по ряду причин в их число уже не входила." # это же промежуточные итоги, Мику вполне может ещё отыграться

            play music music_list["my_daily_life"] fadein 2

        elif ds_day2_current_rout_status == 2:                 # если Семён отыгрался
            $ ds_day2_gambler_skill += 1                     # увеличиваем навык

            show mi smile pioneer at cright with dissolve
            "Мику нисколько не расстроилась из-за проигрыша."
            mi "Молодец, Сенечка, хорошо отбился."
            show mi upset pioneer at cright with dspr
            mi "Так, раз ты выиграл, теперь нас ждёт финальный раунд, верно?"
            "Уточнила Мику."
            show mi laugh pioneer at cright with dspr
            mi "Пускай мы товарищи, но поддаваться я не буду!"
            "Услышав впервые, я не придал этому особого значения и пропустил мимо ушей, однако…" # Возможен исход, при котором здесь "Сенечка" упоминается впервые. Лучше убрать эту строку вообще. ## Нет, здесь Семён отыгрался, значит, первый раз должна была выиграть Мику (см. ds_day2_current_rout_status == 3). Там Сенечка упоминается 2 раза.
            me "Мику, а почему «Сенечка»?"
            show mi shocked pioneer at cright with dspr
            mi "А?"
            show mi shy pioneer at cright with dspr
            "Изменение цвета лица обнаружено."
            "Не думал, что простым вопросом получится смутить нашу японку."
            show mi happy pioneer at cright with dspr
            mi "Потому что Семён слишком грубо и официально, а Сенечка звучит приятно."

        elif ds_day2_current_rout_status == 3:                 # и она выиграла первый раз
            show mi shy pioneer at cright with dissolve
            mi "Я победила?"
            me "Да."
            show mi happy pioneer at cright with dspr
            mi "Ура!"
            show mi smile pioneer at cright with dspr
            mi "Сенечка, ты только не переживай — в поражении нет ничего плохого."
            mi "Я тоже до конца не поняла, как играть в эту игру. Можно сказать, что мне повезло."
            me "Угу."
            show mi sad pioneer at cright with dspr
            mi "Ты всё-таки расстроился. Не переживай, поражение — тоже опыт."
            show mi smile pioneer at cright with dspr
            mi "Но я понимаю тебя. Я тоже расстроилась, когда проиграла Алисе в карты."
            th "Мику играла с Алисой в карты?"
            dreamgirl "А ты думал, что весь мир вертится вокруг тебя, и обитатели лагеря только и ждут, когда Его Величество появится на горизонте?"
            dreamgirl "У каждого своя жизнь, своя история, и она не начинается с твоим появлением, не обрывается с твоим уходом."
            dreamgirl "Нужна ли она тебе — вопрос важный, но отдельный."
            show mi serious pioneer at cright with dspr
            th "Тебе не кажется, что ты до черта умничаешь?"
            dreamgirl "Из нас двоих только я использую мозги по их прямому назначению."
            dreamgirl "А раз в нашем дуэте роль костыля для душевного инвалида выпала мне, вот тебе ещё один совет — хватит болтать с самим собой и поговори уже с девушкой."
            show mi normal pioneer at cright with dspr
            mi "Сенечка, всё хорошо? У тебя глаз дёргается."
            me "В порядке. Давай дальше."

        elif ds_day2_current_rout_status == 4:                 # и она отыгралась
            show mi surprise pioneer at cright with dissolve
            "Хафу долго всматривалась в карты и не могла понять очевидного."
            "К нам даже подошёл Электроник, утвердительно кивнув ей."
            show mi normal pioneer at cright with dspr
            mi "Я победила?"
            me "Да."
            show mi happy pioneer at cright with dspr
            mi "Ура!"

            if ds_result_dv_1_tour > 2 and ds_result_dv_semifinal > 2:
                show mi laugh pioneer at cright with dspr
                mi "Алиса! Вот видишь, я умею играть! Я смогла отыграться!"
                "Рыжая бестия за соседним столом аж покраснела."
                "На месте Алисы я бы не залился краской, а сделал вид, что не знаю Мику."

            show mi grin pioneer at cright with dspr
            mi "Ну держись, Сенечка! Сейчас я выиграю тебя!" # "Выиграю тебя" — так задумано или меняем на "обыграю"? ## задумано
            show mi smile pioneer at cright with dspr
            me "Ага, удачи."
            dreamgirl "Зря, она тебе понадобится."
            th "Сомневаешься в моих способностях?"
            dreamgirl "Я всё-таки одну голову с тобой делю. Так что не сомневаюсь — знаю."

# Ульяна
    elif ds_spr_my_rival == 'us':
        if ds_day2_current_rout_status == 1:                   # если Семён выиграл первый раз
            $ ds_day2_gambler_skill += 1                     # увеличиваем навык

            show us angry pioneer at cright with dissolve
            us "Почему ты не поддался мне?!"
            me "С чего бы это?"
            us "С того, что я ребёнок, а ты взрослый! Ты должен поддаваться!"
            me "С точки зрения закона я тоже все ещё ребёнок."
            dreamgirl "Почти встретивший третий десяток ребёнок."
            th "Цыц!"
            "Однако рыжую нужно как-то успокоить."
            "У неё аж венка на лбу набухла. Того гляди запрыгнет на стол и начнёт колотить меня."
            if herc:
                dreamgirl "А ты её «хоп!» — в медвежий захват — и броском назад!"
                th "Меня не для того учили, чтобы детей избивать!"
                th "Захвата за большой палец будет более чем достаточно…"
            me "Успокойся, это только первый раунд."
            me "У тебя ещё будет возможность отыграться, а с моей удачей шансы весьма высоки."
            show us dontlike pioneer at cright with dspr
            us "Смотри у меня, а не то…"
            if herc or loki:
                me "Не то что?"
                dreamgirl "Сколопендру тебе в штаны запустит, вот что."
                th "Мне так страшно, что уже поджилки трясутся."
            else:
                me "Не то что?.."
                "Я старался добавить в голос побольше уверенности, но получалось откровенно слабо."
                dreamgirl "Да брось, ты в самом деле перепугался мелкой девки?"
                dreamgirl "Ну засунет тебе сколопендру в штаны, и что? Смертельно?"
                th "Всегда ожидай худшее, чтобы радоваться лучшему."
            show us grin pioneer at cright with dspr
            if (counter_sl_7dl == 0) and dr:
                us "А то снова оболью!"
            else:
                us "Узнаешь!"
            us "Если не отдашь мне все лучшие карты, что у тебя есть."
            me "Идёт."
            dreamgirl "Серьёзно?"
            if loki:
                th "Может быть."
            elif herc:
                th "Посмотрю на её поведение."
            else:
                th "Рандом нам судья."

        elif ds_day2_current_rout_status == 2:                 # если Семён отыгрался
            $ ds_day2_gambler_skill += 1                     # увеличиваем навык

            show us dontlike pioneer at cright with dissolve
            us "Нечестно!"
            if renpy.random.randint(1, 95) == 1:
                me "А ты задонатила на победу?"
                us "Чего, это как?"
                me "Пожертвование, мелкая."
                us "Не буду я тебе до… да… жертвовать."
                us "Ты же не больной, руки-ноги целы."
                us "Пожертвования тебе не нужны."
                me "Зря. В моём…"
                "Я осёкся."
                "Чуть не сказал Ульяне «в моём времени»."
                "В её же времени о таком не слышали, но наверняка пресекалось бы и считалось тунеядством."
                "Никогда не понимал таких людей, что в этом такого?"
                "Очередной вид заработка же."
                "Не всем же стоять по восемь часов у станка, есть бойцы интеллектуального фронта."
                dreamgirl "Этого милого светлого мальчика зовут Семён."
                dreamgirl "Ему срочно нужна ваша помощь!"
                dreamgirl "Он страдает от тяжелого и неизлечимого заболевания."
                dreamgirl "Он — ох…"
            elif loki:
                "Соблазн вернуть шпильку оказался слишком велик."
                me "Ну ты же сама говорила, что игра простенькая и только дурак не поймёт."
                show us angry pioneer at cright with dspr
                "О да, вздувшаяся венка на лбу рыжей стала бальзамом на душу."
                "А как только мелкая поколотит меня, возможно, ногами, он мне потребуется ещё и для тела."
                "К счастью, меня спас вовремя подавший голос Электроник."
            elif herc:
                me "Не всё в мире измеряется честностью."
                us "{i}Не всё в мире измеряется честностью.{/i}"
                "Передразнила Ульяна."
                show us grin pioneer at cright with dspr
                us "Жди честного таракана под подушкой."
            elif dr:
                th "Я выиграл по воле Рандома, а понятие честности к нему не применимо."
                dreamgirl "Скажи это вслух — и получишь заслуженный удар по коленке или таракана в суп."
                th "Вот поэтому я лучше промолчу."
                "Ульяна угрожала тараканами под подушкой или подкараулить и облить из ведра с водой."
                "Я молча кивал изредка поддакивая."
                show us normal pioneer at cright with dspr
                "В конце концов рыжая сменила гнев на милость."
                show us grin pioneer at cright with dspr
                "Но, если я каким-то образом выиграю ещё и в финальном раунде, меня ждёт…{w=0.5} что-то нехорошее."
                "Такие вот дела."

        elif ds_day2_current_rout_status == 3:                 # и она выиграла первый раз

            show us surp1 pioneer at cright with dissolve
            us "Вот это да! А я и не думала, что такое бывает!"
            me "Какое такое?"
            us "Ну как? Как можно так плохо играть? Игра же простенькая!"
            show us laugh pioneer at cright with dspr
            us "Только такой зануда, как ты, не поймёт."
            th "Зараза мелкая!"

            if (counter_sl_7dl >= 1) or dr:
                "И ведь как мне хотелось ответить что-то токсичное, но ведь глупо это, обижаться на ребёнка, правда?"
                dreamgirl "Внешность бывает обманчива. Взгляни на неё и себя и сравни."
                dreamgirl "Разница в возрасте несущественная."
                th "Ты на что это намекаешь?"
                "Внутренний голос ответил молчанием."

            else:

                if loki:
                    me "Может, тебя ещё раз водичкой окатить? Пыл поумерить?"
                    show us grin pioneer at cright with dspr
                    us "А ты попробуй догони!"
                    me "Я возьму не скоростью, а хитростью."
                    show us smile pioneer at cright with dspr
                    me "Вот будешь одна в домике, я тихонько подкрадусь сзади, и…"

                elif herc:
                    me "С витамином «Р» знакома?"
                    show us smile pioneer at cright with dspr
                    us "Нет! А что это?"
                    me "Продолжай в том же духе…"
                    "Рука легла на пряжку ремня."
                    me "…узнаешь."
                    show us grin pioneer at cright with dspr
                    us "Хорошо!"




        elif ds_day2_current_rout_status == 4:                 # и она отыгралась

            show us grin pioneer at cright with dissolve
            us "Молодец, Сёмка. Ты на пути к исправлению!"
            "Похвалила Ульянка."
            dreamgirl "Ты всё-таки дурак."
            th "Ну, может, оно и к лучшему."
            dreamgirl "Просто напомню: игра ещё не закончена."

# Шурик
    elif ds_spr_my_rival == 'sh':
        $ ds_day2_gambler_skill += 1                     # увеличиваем навык — Шурику без вариантов

# ============================================================= эксперименты Шурика
        if ds_day2_current_rout_status in [3,4]:                               # Если Шурик выиграл игру
            pass
        else:                                                                   # если Шурик проиграл игру
            if ds_day2_gambler_behavior == 'defense':                          # если Шурик защищался
                $ ds_day2_gambler_behavior = 'gamble'                          # смена стратегии
            elif ds_day2_gambler_behavior == 'gamble':                         # если Шурик рисковал
                $ ds_day2_gambler_behavior = 'defense'                         # смена стратегии
# =============================================================

        if ds_day2_current_rout_status == 1:                   # если Семён выиграл первый раз

            show sh surprise pioneer at cright with dissolve
            sh "Недооценил я тебя."
            me "Ну спасибо."
            show sh smile pioneer at cright with dspr
            sh "Даже при моей достаточной высокой вероятности победить тебе выпали карты, которые меня разгромили."
            "Он что, пытался высчитать, какие у меня карты?"
            "Рандом не щадит таких."
            show sh serious pioneer at cright with dspr
            "Шурик протянул мне руку в знак уважения."
            if herc:
                "Я ответил."
                show sh upset pioneer at cright with dspr
                "Когда пионер слегка поморщился, я понял, что немного перестарался."
                "Ещё подумает, что пытаюсь вывести его из игры."
                dreamgirl "А ты «не»?"
                th "Да какой в этом смысл? Мы же не в покер на деньги играем."
            elif loki:
                "Я всегда брезгливо относился к рукопожатиям и не стал отвечать."
                show sh normal pioneer at cright with dspr
                "Кибернетик на это лишь хмыкнул и пожал плечами."
            else:
                "Я неуверенно взял его за руку и поморщился."
                show sh smile pioneer at cright with flash_red
                th "Словно в тисках сжали."
                th "Он это специально, не иначе."
                dreamgirl "Нет, просто ты дрищ."


        elif ds_day2_current_rout_status == 2:                 # если Семён отыгрался

            show sh serious pioneer at cright with dissolve
            sh "Недооценил я тебя."
            th "Не только ты."
            me "Ну спасибо."
            sh "Даже при моей достаточной высокой вероятности победить тебе выпали карты, которые меня разгромили."
            "Шурик протянул мне руку в знак уважения."
            if herc:
                "Я ответил."
                show sh upset pioneer at cright with dspr
                "Когда пионер слегка поморщился, я понял, что немного перестарался."
                "Ещё подумает, что пытаюсь вывести его из игры."
                dreamgirl "А ты «не»?"
                th "А ты вообще помалкивай, предатель! Я тебе слова не давал."
                dreamgirl "Больно мне нужно твоё разрешение."
                dreamgirl "Впрочем, сейчас посмотрим, что это было: удача или ты действительно что-то умеешь."
            elif loki:
                "Я всегда брезгливо относился к рукопожатиям и не стал отвечать."
                show sh normal pioneer at cright with dspr
                "Кибернетик на это лишь хмыкнул и пожал плечами."
                dreamgirl "К победе по чужим головам?"
                th "Не думаю. Он настроен серьёзнее и имеет все шансы победить."
                dreamgirl "Значит, сдался."
                th "Нет. Просто так не проиграю — пусть выцарапывает себе победу."
            else:
                "Я неуверенно взял его за руку и поморщился."
                show sh upset pioneer at cright with flash_red
                th "Словно в тисках сжали!"
                "Уж что-что, а это я умею — при 99%% шансе вытянуть несчастливый билет."
                "Мои мучения в турнире могли уже закончиться."






        elif ds_day2_current_rout_status == 3:                 # и он выиграл первый раз

            show sh normal pioneer at cright with dissolve
            sh "Хм, а ведь сработало…"
            me "Что?"
            show sh surprise pioneer at cright with dspr
            sh "А?"
            show sh normal pioneer at cright with dspr
            sh "Да я попробовал применить формулы расчёта вероятности более выигрышной комбинации у противника в покере к этой игре."
            sh "Пришлось, конечно, кое-что поправить, но и полученного результата хватило понять, что карты у тебя не лучше."
            "Он что, просто высчитал это? Увидев не больше половины?"
            dreamgirl "Будь с ним осторожен. Он не так прост, как кажется."
            th "Я уже заметил. Ты очень полезен."
            th "Лучше бы подсказал, как против такого играть."
            dreamgirl "Собрался выигрывать?"
            th "Есть другие варианты?"
            th "Встать из-за стола и просто уйти мне не дадут. А поддаваться глупо."
            dreamgirl "У тебя всё равно нет шансов."
            th "Рандом мне судья, а не ты."

        elif ds_day2_current_rout_status == 4:                 # и он отыгрался

            show sh smile pioneer at cright with dissolve
            sh "Хм, а ведь сработало…"
            me "Да что ты всё считаешь-то?"
            show sh upset pioneer at cright with dspr
            sh "А?"
            show sh normal pioneer at cright with dspr
            sh "Да я пробую применить формулы расчёта вероятности более выигрышной комбинации у противника в покере к этой игре."
            sh "Приходится, конечно, кое-что править, но и при таких условиях результат даёт представление о твоих картах."
            "Не видя и половины, он предсказывает весь набор?"
            "Не верю. Мистика какая-то."
            dreamgirl "Кто бы говорил…"

# Женя
    elif ds_spr_my_rival == 'mz': # Ей скилл не повышается, потому что foolplay? ## Ну ды
        show mz normal glasses pioneer at cright with dissolve
        if ds_day2_current_rout_status == 1:                   # если Семён выиграл первый раз

            "Жужа даже бровью не повела."
            "Эмоциональный штиль. «Покерфейс»."
            "Даже досадно немного. Могла бы изобразить хоть подобие разочарования."
            mz "Что?"
            me "Жень, а как ты сюда вообще попала?"
            me "По тебе заметно, что ты не в восторге."
            show mz angry glasses pioneer with dspr
            mz "Сюда — это куда? В лагерь? В библиотеку? Турнир? Мир?"
            mz "Задавай конкретные вопросы, если хочешь получить конкретный ответ."
            "Тяжелый человек."
            if herc or loki:
                "И почему мне так часто встречаются именно такие?"
                dreamgirl "Подобное притягивает подобное?"
                me "Если у меня найдётся время, я зайду к тебе на чашечку чая, и мы поговорим о чём угодно."
                me "О вождях пролетариата, о полёте на Марс или «Мартине Идене» Лондона."
                show mz rage glasses pioneer with dspr
                me "Да хоть свои детские фото, где ты в пелёнках, покажи."
                me "А пока мне интересно третье."
                me "Сделай одолжение простому смертному и поведай свой секрет."
                "Я ожидал от Жужелицы всякого: что она вскочит и даст мне по морде, что она заорёт на весь зал."
                "Да даже, что она пожалуется вожатой и потребует отпустить её в медпункт, так как она получила психологическую травму, и ей теперь требуется отдых."
                show mz laugh glasses pioneer with dspr
                pause(.5)
                show mz normal glasses pioneer with dspr
                "А она улыбнулась."
                "Всего на миг, но я готов поклясться, что видел это."
                dreamgirl "Чудеса!.. Ой, чудеса!.."
                mz "Вожатая."
                mz "Пришла и отчеканила: отрядное мероприятие, присутствуют все, возражения не принимаются."
                me "Ох уж эта Ольга Лен…{w=0.3} Дмитриевна."
            else:
                me "Неважно."
                "Буркнул я."
                show mz normal glasses pioneer with dspr
                "До чего ж вредный человек."
                "У Жени проблем в общении побольше, чем у меня."
                dreamgirl "А ты попробуй раскрутить её на разговор."
                dreamgirl "Вдруг узнаешь её с другой стороны."
                dreamgirl "А потом она позовёт тебя на чай в библиотеку, а там, среди стеллажей, книги посыплются с полок под громкие сто…"
                th "Нет!" with vpunch
                show mz bukal glasses pioneer with dspr
                mz "Псих."
                "Фыркнула Женя."
                dreamgirl "Если ты думаешь, то что затрещина поможет избавиться от меня, очень ошибаешься."
                th "Бла-бла-бла! Я тебя не слы-ышу-у-у!"
                dreamgirl "Идиот…"

        elif ds_day2_current_rout_status == 2:                 # если Семён отыгрался

            show mz normal glasses pioneer with dissolve
            mz "Продолжай в том же духе."
            "Если б это от меня зависело."
            me "Ничего не обещаю, но постараюсь."
            mz "Угу, постарайся."
            hide mz with dissolve

        elif ds_day2_current_rout_status == 3:                 # и она выиграла первый раз

            show mz bukal glasses pioneer at cright with dissolve
            "Сама победительница первого раунда устало вздохнула."
            "Если ей настолько не интересно, зачем вообще соглашалась?"
            "Могла же прикрыться занятостью в библиотеке перед вожатой."
            mz "У меня что-то на лице?"
            "Вяло спросила она."
            th "Скорее — отсутствие."
            "Подумал я, отвечая:"
            me "Нет, я просто задумался."
            show mz normal glasses pioneer at cright with dspr
            mz "Ясно."


        elif ds_day2_current_rout_status == 4:                 # и она отыгралась


            show mz bukal glasses pioneer at cright with dspr
            if herc or loki:
                "Женя сокрушенно выдохнула."
            else:
                "У жужелицы было такое лицо, словно оно впитало в себя все муки мира."

            mz "Сделай одолжение — не облажайся в следующем раунде."
            me "Если б это от меня зависело."
            mz "От кого ещё это может зависеть?"
            mz "Только не говори глупости вроде «бога»."
            "Пренебрежение, чуть ли не с ненавистью в голосе."
            "Истинная коммунистка!"
            th "Или это что-то личное?"
            me "И в мыслях не было."
            th "Рандом — он не бог. Он выше."
            show mz angry glasses pioneer at cright with dspr
            mz "Вот и славно."

    show el normal pioneer far at left with dissolve
    if ds_day2_current_rout_status == 1:
        el "В этой игре победил Семён, счёт 1-0 в его пользу."
    elif ds_day2_current_rout_status == 3:
        if ds_spr_my_rival == 'sh':                            # Шурик
            el "В этой игре победил Шурик, счёт 1-0 в его пользу."
        else:
            el "В этой игре %(ds_name_my_rival_i)s побеждает и ведёт в партии со счётом 1-0."
    elif ds_day2_current_rout_status == 2:
        el "Семён выигрывает и сравнивает счёт в раунде."
    elif ds_day2_current_rout_status == 4:
        if ds_spr_my_rival == 'sh':                            # Шурик
            el "Шурик выигрывает и сравнивает счёт в раунде."
        else:
            el "%(ds_name_my_rival_i)s победила и сравняла счёт в партии."
    return

#-----------------------------------------------------------------------------------
# Результат КОНА
label ds_cards_summary_round:
    if ds_day2_result_tour in [1,11,21]:                                                              # Если проигрыш в КОНЕ
        if ds_day2_detour_1_tour:                                                                     # если скипаем тур
            $ ds_day2_my_win = renpy.random.choice([1,0])                                             # рандомно выигрыш Семёна 0 или 1
    elif ds_day2_result_tour in [2,12,22]:                                                            # Если выигрыш в КОНЕ
        if ds_day2_detour_1_tour:                                                                     # если скипаем тур
            $ ds_day2_rival_win = renpy.random.choice([1,0])                                          # рандомно выигрыш соперника 0 или 1
    return

#-----------------------------------------------------------------------------------
# АНАЛИЗАТОР 1-го ТУРА
label ds_day2_1_tour_analizer:
    $ ds_table_no = 0                                                                  # № стола = 1 (начинаем с НУЛЯ в этом случае)
    $ ds_mstt = 0                                                                      # обнуляем глобальный счетчик таблицы
    call show_tournament_table                                                          #  показываем исходное положение ??? сортируем игроков ???
    $ ds_result_dv_1_tour = ds_get_result_dv(ds_day2_gamblers_1_tour, 8)             # а где там наша ДваЧе?
    pause(1)
    $ ds_random_box_1 = range(1,len(ds_table_winner)+1)                               # черный ящик 1 — список от 1 до длины победителей +1
    while ds_table_no <= 4:                                                            # перебираем столы от 1 до 4
    #результат, игроки, высказывания — по номеру стола
        $ renpy.block_rollback()                                                        # блокируем роллбак
        $ results_at_table,gambler_win,winner_remark,loser_remark = ds_declare_results_tables(ds_table_no, ds_day2_gamblers_1_tour)
        "%(results_at_table)s"                                                          # оглашаем результат за столом
        call show_tournament_table                                                      # переход по метке — вызов очередной фишки
        extend " %(gambler_win)s."                                                      # выводим в окно имя победителя
        $ a_c_i = 0                                                                     # счетчик фраз
        while a_c_i < len(winner_remark):                                               # пока счетчик фраз меньше их количества
            $ ds_gambler_saying = winner_remark[a_c_i][0]                              # кто говорит
            $ ds_gambler_remark = winner_remark[a_c_i][1]                              # фраза
            if ds_gambler_saying != None:                                              # если определено, от кого фраза
                ds_gambler_saying "%(ds_gambler_remark)s"                             # выводим её от лица говорящего
            else:                                                                       # если "от автора"
                "%(ds_gambler_remark)s"                                                # выводим фразу "от автора"
            $ a_c_i += 1                                                                # увеличиваем счетчик фраз
        call show_tournament_table                                                      # переход по метке — вызов очередной фишки
        $ a_c_i = 0                                                                     # счетчик фраз
        while a_c_i < len(loser_remark):                                                # пока счетчик фраз меньше их количества
            $ ds_gambler_saying = loser_remark[a_c_i][0]                               # кто говорит
            $ ds_gambler_remark = loser_remark[a_c_i][1]                               # фраза
            if ds_gambler_saying != None:                                              # если определено, от кого фраза
                ds_gambler_saying "%(ds_gambler_remark)s"                             # выводим её от лица говорящего
            else:                                                                       # если "от автора"
                "%(ds_gambler_remark)s"                                                # выводим фразу "от автора"
            $ a_c_i += 1                                                                # увеличиваем счетчик фраз
        $ ds_table_no += 1                                                             # следующий стол
    return

#-----------------------------------------------------------------------------------
# АНАЛИЗАТОР ПОЛУФИНАЛА
label ds_day2_semifinal_analizer:
    $ ds_table_no = 4                                                                  # № стола = 4 (начинаем с четвертого в этом случае)
    $ ds_mstt = 0                                                                      # обнуляем глобальный счетчик таблицы
    call show_tournament_table                                                          #  показываем исходное положение ??? сортируем игроков ???
    $ ds_result_dv_semifinal = ds_get_result_dv(ds_day2_gamblers_semifinal, 4)       # а где там наша ДваЧе?
    pause(1)
    $ ds_random_box_1 = range(1,len(ds_table_winner)+1)                               # черный ящик 1 — список от 1 до длины победителей +1
    while ds_table_no <= 6:                                                            # перебираем столы 5-6
    #результат, игроки, высказывания — по номеру стола
        $ renpy.block_rollback()                                                        # блокируем роллбак
        $ results_at_table,gambler_win,winner_remark,loser_remark = ds_declare_results_tables(ds_table_no, ds_day2_gamblers_semifinal)
        "%(results_at_table)s"                                                          # оглашаем результат за столом
        call show_tournament_table                                                      # переход по метке — вызов очередной фишки
        extend " %(gambler_win)s."                                                      # выводим в окно имя победителя
        $ a_c_i = 0                                                                     # счетчик фраз
        while a_c_i < len(winner_remark):                                               # пока счетчик фраз меньше их количества
            $ ds_gambler_saying = winner_remark[a_c_i][0]                              # кто говорит
            $ ds_gambler_remark = winner_remark[a_c_i][1]                              # фраза
            if ds_gambler_saying != None:                                              # если определено, от кого фраза
                ds_gambler_saying "%(ds_gambler_remark)s"                             # выводим её от лица говорящего
            else:                                                                       # если "от автора"
                "%(ds_gambler_remark)s"                                                # выводим фразу "от автора"
            $ a_c_i += 1                                                                # увеличиваем счетчик фраз
        call show_tournament_table                                                      # переход по метке — вызов очередной фишки
        $ a_c_i = 0                                                                     # счетчик фраз
        while a_c_i < len(loser_remark):                                                # пока счетчик фраз меньше их количества
            $ ds_gambler_saying = loser_remark[a_c_i][0]                               # кто говорит
            $ ds_gambler_remark = loser_remark[a_c_i][1]                               # фраза
            if ds_gambler_saying != None:                                              # если определено, от кого фраза
                ds_gambler_saying "%(ds_gambler_remark)s"                             # выводим её от лица говорящего
            else:                                                                       # если "от автора"
                "%(ds_gambler_remark)s"                                                # выводим фразу "от автора"
            $ a_c_i += 1                                                                # увеличиваем счетчик фраз
        $ ds_table_no += 1                                                             # следующий стол
    return

#-----------------------------------------------------------------------------------
# АНАЛИЗАТОР ФИНАЛА
label ds_day2_final_analizer:
    $ ds_mstt = 3
    call show_tournament_table                                                          # показываем исходное положение, сортируем игроков
    $ ds_take_tournament_winner = ds_day2_gamblers_final[0].take                      # Ник победителя
    if ds_take_tournament_winner == "me":
        $ ds_name_tournament_winner = "Семёна"
    else:
        $ ds_name_tournament_winner = ds_day2_gamblers_final[0].name['v']             #  Получаем имя победителя турнира

    $ ds_take_tournament_loser = ds_day2_gamblers_final[1].take                       # Ник проигравшего
    if ds_take_tournament_loser == "me":
        $ ds_name_tournament_loser = "Семёну"
    else:
        $ ds_name_tournament_loser = ds_day2_gamblers_final[1].name['d']              #  Получаем имя проигравшего в финале

    if ds_take_tournament_loser in ['me','sh']:
        $ ds_pronomen_final_loser = "он"
    else:
        $ ds_pronomen_final_loser = "она"

    $ winner_remark, loser_remark = ds_declare_results_final(ds_take_tournament_winner, ds_take_tournament_loser) # вызываем функцию на финал — фразы победителя, проигравшего — по их никам.

    show el normal pioneer at cleft with dissolve
    el "Итак, турнир окончен."
    "Вспомнил о своих обязанностях организатор."
    $ ds_mstt = 0
    el "Поздравляем нашего победителя — %(ds_name_tournament_winner)s!"
    play sound sfx_concert_applause
    call show_tournament_table                                                          # двигаем победителя
    pause(0.2)

    $ a_c_i = 0                                                                     # счетчик фраз
    while a_c_i < len(winner_remark):                                               # пока счетчик фраз меньше их количества
        $ ds_gambler_saying = winner_remark[a_c_i][0]                              # кто говорит
        $ ds_gambler_remark = winner_remark[a_c_i][1]                              # фраза
        if ds_gambler_saying != None:                                              # если определено, от кого фраза
            ds_gambler_saying "%(ds_gambler_remark)s"                             # выводим её от лица говорящего
        else:                                                                       # если "от автора"
            "%(ds_gambler_remark)s"                                                # выводим фразу "от автора"
        $ a_c_i += 1                                                                # увеличиваем счетчик фраз

    $ ds_mstt += 1
    el "А вот %(ds_name_tournament_loser)s сегодня немного не повезло; тем не менее, %(ds_pronomen_final_loser)s занимает почётное второе место."
    call show_tournament_table                                                      # прячем проигравшего
    pause(0.2)

    $ a_c_i = 0                                                                     # счетчик фраз
    while a_c_i < len(loser_remark):                                                # пока счетчик фраз меньше их количества
        $ ds_gambler_saying = loser_remark[a_c_i][0]                               # кто говорит
        $ ds_gambler_remark = loser_remark[a_c_i][1]                               # фраза
        if ds_gambler_saying != None:                                              # если определено, от кого фраза
            ds_gambler_saying "%(ds_gambler_remark)s"                             # выводим её от лица говорящего
        else:                                                                       # если "от автора"
            "%(ds_gambler_remark)s"                                                # выводим фразу "от автора"
        $ a_c_i += 1                                                                # увеличиваем счетчик фраз
    hide el with dissolve
    return

# --------------------------------------------------------------------------
# Подготовка перехода на ужин: — очистка слоя, разблокировка роллбэка
label ds_day2_prepare_transition_to_supper:
    python:
        renpy.scene('underlay')
        renpy.with_statement(dissolve)
    $ ds_who_how_plays_poker()                                                     # посмотрели, кто и как сыграл
    if ds_day2_gamblers_result['me'] <= 11:
        $ ds_my_rival_final.take = None
        if ds_day2_gamblers_result['me'] == 1:
            $ ds_my_rival_semifinal.take = None
    $ d2_cardgame_block_rollback = False
    return
