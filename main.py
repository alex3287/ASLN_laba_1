class BoolFunction:
    def __init__(self, countInput, countOutput, ilb, ob, rows, vectors):
        self.countInput = countInput
        self.countOutput = countOutput
        self.ilb = ilb
        self.ob = ob
        self.rows = rows
        self.vectors = vectors

    def selectRow(self, function):
        '''собирает нужные строки ТИ из двумерного массива'''
        A = []
        for i in self.vectors:
            if i[1][function] == '1':
                A.append(i[0])
        return A

    def addVectors(self, A):
        '''Заменяет - на 0 и 1 тем самым увеличивает набор данных'''
        B = []
        while A:
            temp = A.pop(0)
            if '-' in temp:
                n = temp.find('-')
                first = temp[:n] + '0' + temp[n + 1:]
                second = temp[:n] + '1' + temp[n + 1:]
                if '-' in first:
                    A.append(first)
                    A.append(second)
                else:
                    B.append(first)
                    B.append(second)
            else:
                B.append(temp)
        return B

    def minDNF(self, A):
        '''формирует данные в читабельный список'''
        Names = self.ilb
        mDNF = []
        for vector in A:
            temp = ''
            for i in range(len(vector)):
                if vector[i] == '1':
                    temp += Names[i]+' '
                elif vector[i] == '0':
                    temp += 'not_'+Names[i]+' '
            mDNF.append(temp[:-1])
        return mDNF

    def glue(self, vector1, vector2):
        '''метод осуществляет склеивание векторв'''
        newVector = ''
        countGlue = 0
        for i, j in zip(vector1, vector2):
            if i == j:
                newVector += i
            else:
                newVector += '-'
                countGlue += 1
        if countGlue-1:
            return None
        return newVector

    def algKwaynMakKlascy(self, dnf):
        size = len(dnf)
        list1 = []
        list2 = []
        list3 = []
        mark = [0]*size
        m = 0
        # выполнения склеивания векторов
        for i in range(size-1):
            for j in range(i+1, size):
                temp = self.glue(dnf[i], dnf[j])
                if temp:
                    list1.append(temp)
                    mark[i] = 1
                    mark[j] = 1
        # делаем метку
        size2 = len(list1)
        mark2 = [0] * size2
        for i in range(size2-1):
            for j in range(i+1, size2):
                if i != j and mark2[i] == 0:
                    if list1[i] == list1[j]:
                        mark2[j] = 1
        # добавляем разные элементы для нового списка
        for i in range(size2):
            if mark2[i] == 0:
                list2.append(list1[i])

        # выбираем не учавствующие элементы
        for i in range(size):
            if mark[i] == 0:
                list3.append(dnf[i])
                m += 1

        if m == size or size == 1:
            return list3
        return list3 + self.algKwaynMakKlascy(list2)

    def saveResult(self, data, number):
        '''сохраняет результат в файл pla'''
        namesFun = self.minDNF(data)
        with open('output.pla','w') as fout:
        # формат вывода в одну строку
        #     print(' V '.join(namesFun), file=fout)

        # формат вывода по именам отдельно в каждую строку
        #     for i in namesFun:
        #         print(i, file=fout)

        # формат вывода по векторам как файлы pla
            print('.i', str(self.countInput), file=fout)
            print('.o', str(1), file=fout)
            print('.ilb', *self.ilb, file=fout)
            print('.ob', self.ob[number-1], file=fout)
            print('.p', len(data), file=fout)
            for i in data:
                print(i, 1, file=fout)
            print('.e', end='', file=fout)


def readFilePla(fileName):
    '''функция читает файл pla и забирает данные'''
    with open(fileName) as fin:
        countInput = int(fin.readline().split()[1])
        countOutput = int(fin.readline().split()[1])
        ilb = [i for i in fin.readline().split()[1:]]
        ob = [i for i in fin.readline().split()[1:]]
        rows = int(fin.readline().split()[1])
        vectors = [[j for j in i.rstrip().split()] for i in fin.readlines()[:-1]]
    return countInput, countOutput, ilb, ob, rows, vectors


if __name__ == '__main__':
    fileName = 'squar5.pla'  # тут вручную пишем имя файла
    f = BoolFunction(*readFilePla(fileName))
    print('Доступные функции', f.ob)
    number = int(input('Введите номер функции (нумерация с 1) -> '))
    A = f.selectRow(number-1)
    print(A, len(A))  # test
    B = f.addVectors(A)
    # print(B, len(B), sep='\n')  # test
    C = f.algKwaynMakKlascy(B)
    f.saveResult(C, number)