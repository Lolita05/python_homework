# Глобальное выравнивание

seqI = "AAAAAAA"
seqJ = "ATAATATA"

# Функция, которая делает пустую матрицу
def zeros(rows, cols):
    # Определяем пустой лист
    retval = []
    # Ностройка строк матрицы
    for x in range(rows):
        # Пустой лист для каждой строки
        retval.append([])

        for y in range(cols):
            # Добавляем нули в каждую ячейку
            retval[-1].append(0)
    # Возвращаем матрицу с нулями
    return retval

# Функция глобального выравнивания
def global_align(seq1, seq2, gap_penalty, match_award, mismatch_penalty):
    # Длины последовательностей
    n = len(seq1)
    m = len(seq2)

    # Генерим пустую матрицу
    score = zeros(m + 1, n + 1)


    # Заполняем колонки
    for i in range(0, m + 1):
        score[i][0] = gap_penalty * i

    # Заполняем строки
    for j in range(0, n + 1):
        score[0][j] = gap_penalty * j


    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # функция присвоение скора для двух нуклеотидов
            def match_score(alpha, beta):
                if alpha == beta:
                    return match_award
                elif alpha == '-' or beta == '-':
                    return gap_penalty
                else:
                    return mismatch_penalty

            # Скоры для ячеек
            match = score[i - 1][j - 1] + match_score(seq1[j - 1], seq2[i - 1])
            delete = score[i - 1][j] + gap_penalty
            insert = score[i][j - 1] + gap_penalty
            # Вычисляем максимальный скор
            score[i][j] = max(match, delete, insert)


    align1 = ""
    align2 = ""


    i = m
    j = n

    # Используем i и j, чтобы отслеживать, где мы находимся в матрице
    while i > 0 and j > 0:
        score_current = score[i][j]
        score_diagonal = score[i - 1][j - 1]
        score_up = score[i][j - 1]
        score_left = score[i - 1][j]

        # обновление данных ячейки
        if score_current == score_diagonal + match_score(seq1[j - 1], seq2[i - 1]):
            align1 += seq1[j - 1]
            align2 += seq2[i - 1]
            i -= 1
            j -= 1
        elif score_current == score_up + gap_penalty:
            align1 += seq1[j - 1]
            align2 += '-'
            j -= 1
        elif score_current == score_left + gap_penalty:
            align1 += '-'
            align2 += seq2[i - 1]
            i -= 1

    while j > 0:
        align1 += seq1[j - 1]
        align2 += '-'
        j -= 1
    while i > 0:
        align1 += '-'
        align2 += seq2[i - 1]
        i -= 1

    align1 = align1[::-1]
    align2 = align2[::-1]

    return score[m][n], f'{align1} \n {align2}'

print(global_align(seqI, seqJ, -1, 1, -1))