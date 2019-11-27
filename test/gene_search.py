#Поиск генов в строке ДНК
# Инпут функции - строка ДНК, оутпут - все найденные в ней гены. Генами будем считать последовательности начинающиеся со старт-кодона
# заканчивающиеся стоп-кодоном имеющие больше 4-ёх кодонов
# а также нужно, чтобы число нуклеотидов было кратно трём (триплетность)
# В выдаваемом гене должны быть старт и стоп кодоны. Результат - список строк

dna_string = 'AAGGTGATGCTGTAAATGTAAATGATGATGgggcATTAA'
dna_string2 = 'aaaaatgtaaatgatgaaaagtttTAAatgctGATGA'

# Функция поиска всех стартовых позиций

def findStartPositions(seq):
    startCodon = 'ATG'
    # Делаем все заглавными
    seq = seq.upper()
    # Определяем список результатов
    result = []
    # Перебираем все индексы, кроме 2 последних, потому что уже не триплет
    for i in range(len(seq)-2):
        # Проверяем, является ли кодон стартовым
        if seq[i:i+3] == startCodon:
            # Добавляем старт кодон в список
            result.append(i)
    return result

# Функция поиска всех позиций после первого

def findNextCodon(seq, start, codon):
    # Прыгаем по триплетам
    for i in range(start, len(seq), 3):
        # Проверяем, является ли кодон стартовым
        if seq[i:i+3] == codon:
            # Возвращаем индекс стартового кодона
            return i
    return None

# Функция поиска всех конечных позиций

def findNextStopCodon(seq, start):
    stopCodons = ['TAG', 'TGA', 'TAA']
    # Делаем все заглавными
    seq = seq.upper()
    # Определяем список результатов
    results = []
    # Перебираем стоп кодоны
    for stopCodon in stopCodons:
        # Находим индекс следующего стоп кодона
        pos = findNextCodon(seq, start, stopCodon)
        # Проверка, найден ли кодон
        if pos != None:
            # Добавляем стартовую позицию стоп кодона
            results.append(pos)
    if len(results) > 0:
        return min(results)
    else:
        return None

# Функция поиска всех рамок считывания гена

def findOpenReadingFrames(seq):
    # Определяем список результатов
    result = []
    # Перебираем список индексов из findStartPositions
    for startPosition in findStartPositions(seq):
        # Получаем стоп позицию для каждой начальной позиции
        stopPosition = findNextStopCodon(seq, startPosition)
        if stopPosition != None:
            # Добавляем кортеж начала и конца рамки считывания
            result.append( (startPosition, stopPosition) )
    return result

# Функция, выдающая список генов по рамке считывания

def GeneSearch(seq):
    # Делаем все заглавными
    seq = seq.upper()
    # Определяем список результатов
    result = []
    for start, stop in findOpenReadingFrames(seq):
        gene = seq[start:stop+3]
        result.append(gene)
    return result

print(GeneSearch(dna_string))
print(GeneSearch(dna_string2))
