class Korcsolya:
    def __init__(self, sor:str):
        adatok=sor.strip().split(";")
        self.Név=adatok[0]
        self.Ország_kódja=adatok[1]
        self.Technikai_pontszám=float(adatok[2])
        self.Komponens_pontszám=float(adatok[3])
        self.Hibapont=int(adatok[4])

rövid:list[Korcsolya]=[]
döntő:list[Korcsolya]=[]
file=open("rovidprogram.csv", "r")
file.readline()
for sor in file:
    rövid.append(Korcsolya(sor))
file.close()

file=open("donto.csv", "r")
file.readline()
for sor in file:
    döntő.append(Korcsolya(sor))
file.close()

print(f"2. feladat\n\tA rövid programben {len(rövid)} induló volt")

x=False
for i in range(len(döntő)):
    if döntő[i].Ország_kódja=="HUN":
        x=True
        break
if x==False:
    print(f"3. feladat\n\tA magyar versenyző nem jutott be a kűrbe.")
elif x== True:
    print(f"3. feladat\n\tA magyar versenyző bejutott be a kűrbe.")

def ÖsszPontszám(index):
    z=rövid[index-1].Név
    index2=0
    q=False
    for i in range(len(döntő)):
        if z==döntő[i].Név:
            index2+=i
            q=True
    a=round(rövid[index-1].Komponens_pontszám+rövid[index-1].Technikai_pontszám-rövid[index-1].Hibapont,2)
    if q==False:
          return a
    else:
        b=round(a+döntő[index2].Komponens_pontszám+döntő[index2].Technikai_pontszám-döntő[index2].Hibapont, 2)
        return b

x=input(f"5. feladat\n\tKérem a versenyző nevét: ")
y=False
index=1
for i in range(len(rövid)):
    if rövid[i].Név==x:
        y=True
        index+=i
        break
if y==False:
    print(f"\tIlyen nevű induló nem volt.")
else:
    print(f"6. feladat\n\tA versenyző összpontszáma: {ÖsszPontszám(index)}")


x=[]
print("7. feladat")
for i in range(len(döntő)):
    if döntő[i].Ország_kódja not in x:
        x.append(döntő[i].Ország_kódja)
for i in x:
    y=0
    for j in range(len(döntő)):
        if i==döntő[j].Ország_kódja:
            y+=1
    if y>1:
        print(f"\t{i}: {y} versenyző")

class Top10:
    def __init__(self, sor:str):
        adatok=sor.strip().split(";")
        self.Név=adatok[0]
        self.Ország_kódja=adatok[2]
        self.Összponszám=adatok[3]


def ÖsszPontszám(index2):
    a=round(rövid[index-1].Komponens_pontszám+rövid[index-1].Technikai_pontszám-rövid[index-1].Hibapont,2)
    b=round(a+döntő[index2].Komponens_pontszám+döntő[index2].Technikai_pontszám-döntő[index2].Hibapont, 2)
    return b

pontok=[]
for i in range(len(döntő)):
    index2=i
    pontok.append(f"{döntő[i].Név};{döntő[i].Ország_kódja};{ÖsszPontszám(index2)}")
pontok.sort()
végeredmény:list[Top10]=[]
for i in pontok:
    végeredmény.append(Top10(i))
print(végeredmény)
