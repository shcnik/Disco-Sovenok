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
            renpy.call_in_new_context(game_interuptions[position])
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
    if persistent.ds_cards_demo == None:
        $ persistent.ds_cards_demo= False
    if persistent.ds_cards_max_stage == None:
        $ persistent.ds_cards_max_stage = -1
    if persistent.ds_cards_rules_read == None:
        $ persistent.ds_cards_rules_read = False

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
label show_tournament_table:                                                                                        # сюда ныряем из турнира
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