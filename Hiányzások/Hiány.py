class Hiányzások:
    def __init__(self,sor:str):
        adatok=sor.strip().split(";")
        self.name=adatok[0]
        self.osztály=adatok[1]
        self.elsonap=int(adatok[2])
        self.utolso=int(adatok[3])
        self.orak=int(adatok[4])

hiány:list[Hiányzások]=[]

file=open("szeptember.csv","r")
file.readline()
for sor in file:
    hiány.append(Hiányzások(sor))
file.close()

összó=0
for i in hiány:
    összó+=i.orak
print(f"2.feladat\n\tÖsszes mulasztott órák száma: {összó}")
