class BoolFunction:
    def __init__(self, file):
        with open(file) as fin:
            self.i = fin.readline()
            self.o = fin.readline()
            self.ilb = list(fin.readline().split())[1:]
            self.ob = list(fin.readline().split())[1:]
            self.row = int(fin.readline()[3:])
            self.vectors = [[j for j in i.rstrip().split()] for i in fin.readlines()[:-1]]

    def dictVectorIn(self, s1):
        inVar, outVar = s1.split()
        vectorIn = {i: j for i,j in zip(self.ilb, inVar)}
        vectorOut = {i: j for i,j in zip(self.ob, outVar)}
        return vectorIn, vectorOut

    def choceFunction(self, number):
        '''возвращает имя выходной функции по введенному номеру, нумерация с 1'''
        return self.ob[number]

    def selectRow(self, function):
        '''собирает нужные строки ТИ из двумерного массива'''
        A = []
        for i in self.vectors:
            if i[1][function] == '1':
                A.append(i[0])
        return A

    def minDNF(self, A):
        Names = self.ilb
        mDNF = []
        for vector in A:
            temp = ''
            for i in range(len(vector)):
                if vector[i] == '1':
                    temp += Names[i]+' '
                elif vector[i] == '0':
                    temp += 'n_'+Names[i]+' '
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

    def getMinDNF(self, dnf):
        size = len(dnf)
        list1 = []
        list2 = []
        list3 = []
        mark = [0]*size
        m = 0
        # выполнения склеивания векторов
        for i in range(size-1):  # TODO тут перепроверить нужно
            for j in range(i+1, size):
                temp = self.glue(dnf[i], dnf[j])
                if temp:
                    list1.append(temp)
                    mark[i] = 1
                    mark[j] = 1
        # делаем метку
        mark2 = [0]*size
        size2 = len(list1)
        for i in range(size2-1):  # TODO тут размер нормальный?
            for j in range(i+1, size2):
                if i != j and mark2[i] == 0:  # TODO why i != j
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

        if m == size or size == 1:  # TODO size == 1
            return list3
        return list3 + self.getMinDNF(list2)

file_pla = 'exampl.pla'
f = BoolFunction(file_pla)

print(f.ilb)
print(f.ob)
print(f.choceFunction(0))

# for i in f.selectRow(0):
#     print(i,'->','1')
A = f.selectRow(0)
print(A, len(A))
# print(f.minDNF(A))
# print(f.ilb)
# print(f.dictVectorIn(f.vectors[0]))

v1 = '0101-10'
v2 = '1101-10'
print(f.glue(v1,v2))
print(f.getMinDNF(A))