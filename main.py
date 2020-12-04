class BoolFunction:
    def __init__(self, file):
        with open(file) as fin:
            self.i = fin.readline()
            self.o = fin.readline()
            self.ilb = list(fin.readline().split())
            self.ob = list(fin.readline().split())
            self.row = int(fin.readline()[3:])
            self.vectors = [i.rstrip() for i in fin.readlines()[:-1]]

file_pla = 'sao2.pla'
f = BoolFunction(file_pla)

print(f.vectors)