#Локальное выравнивание

seqI = "AAAAAAA"
seqJ = "ATAATATA"


def local_align(seqI, seqJ, match, mismatch, gap): # Делаем локальное выравнивание последовательностей
    lenI = len(seqI)
    lenJ = len(seqJ)
    smat = [[0 for x in range(lenJ + 1)] for y in range(lenI + 1)] # scorematch
    tb = [[0 for x in range(lenJ + 1)] for y in range(lenI + 1)] # матрица

    for i in range(0, lenI + 1):
        smat[i][0] = i * gap
        tb[i][0] = 1

    for j in range(0, lenJ + 1):
        smat[0][j] = j * gap
        tb[0][j] = -1

    for i in range(1, lenI + 1):
        for j in range(1, lenJ + 1):

            if seqI[i - 1] == seqJ[j - 1]:
                s = match
            else:
                s = mismatch
            Sub = smat[i - 1][j - 1] + s
            Del = smat[i][j - 1] + gap
            Ins = smat[i - 1][j] + gap

            if Sub > Del and Sub > Ins:
                smat[i][j] = Sub
                tb[i][j] = 0
            elif Del > Ins:
                smat[i][j] = Del
                tb[i][j] = -1
            else:
                smat[i][j] = Ins
                tb[i][j] = 1

    i = lenI
    j = lenJ
    lenAln = 0
    alnI = []
    alnJ = []

    while ((i == 0 and j == 0) != 1):
        if (tb[i][j] == 0):
            i -= 1
            j -= 1
            alnI.append(seqI[i])
            alnJ.append(seqJ[j])
        elif (tb[i][j] == -1):
            j -= 1
            alnI.append('-')
            alnJ.append(seqJ[j])
        elif (tb[i][j] == 1):
            i -= 1
            alnI.append(seqI[i])
            alnJ.append('-')
        lenAln += 1

    alnI = alnI[::-1]
    alnJ = alnJ[::-1]

    alnI = ''.join(alnI)
    alnJ = ''.join(alnJ)

    return "Optimal Score= %d" % (smat[lenI][lenJ]), f'{alnI} \n {alnJ}'


print(loсal_align(seqI, seqJ, 10, -5, -5))
