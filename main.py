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


    # def addNewRow(self, A):
    #     '''меняем - на 0 и 1'''
    #     # B = [] fixme
    #     # while A:
    #     #     tempA = []
    #     #     temp = A.pop(0)
    #     #     tempA.append(temp)
    #     #     while '-' in tempA[0]:
    #     #         n = len(tempA)
    #     #         while n:
    #     #             n -= 1
    #     B = A[:]
    #     for vector in A:
    #         if '-' in vector:
    #             temp1, temp2 = self.modification(vector)
    #             B.remove(vector)
    #             B.append(temp1)
    #             B.append(temp2)
    #             return self.addNewRow(B)
    #     return B
    #
    # def modification(self, s):
    #     '''делаем 2 вектора из одного'''
    #     n = s.index('-')
    #     s1 = s[:n]+'0'+s[n+1:]
    #     s2 = s[:n]+'1'+s[n+1:]
    #     return s1, s2


file_pla = 'sao2.pla'
f = BoolFunction(file_pla)

print(f.ilb)
print(f.ob)
print(f.choceFunction(1))

# for i in f.selectRow(0):
#     print(i,'->','1')
A = f.selectRow(3)
print(A, len(A))
print(f.minDNF(A))
# print(f.ilb)
# print(f.dictVectorIn(f.vectors[0]))