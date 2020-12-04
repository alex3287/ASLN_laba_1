class BoolFunction:
    def __init__(self, file):
        with open(file) as fin:
            self.i = fin.readline()
            self.o = fin.readline()
            self.ilb = list(fin.readline().split())[1:]
            self.ob = list(fin.readline().split())
            self.row = int(fin.readline()[3:])
            self.vectors = [i.rstrip() for i in fin.readlines()[:-1]]

    def dictVectorIn(self, s1):
        inVar, outVar = s1.split()
        vectorIn = {i: j for i,j in zip(self.ilb, inVar)}
        vectorOut = {i:j for i,j in zip(self.ob, outVar)}
        return vectorIn, vectorOut




file_pla = 'sao2.pla'
f = BoolFunction(file_pla)

print(f.vectors)
print(f.ilb)
print(f.dictVectorIn(f.vectors[0]))