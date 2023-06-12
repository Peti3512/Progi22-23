class Eredmény:
    def __init__(self, sor:str):
        adatok=sor.strip().split(";")
        self.Verszenyzo=adatok[0]
        self.Rajtszam=adatok[1]
        self.Kategoria=adatok[2]
        self.Versenydio=adatok[3]
        self.TavSzazalek=int(adatok[4])

eredmény:list[Eredmény]=[]

file=open("ub2017egyeni.txt", "r", encoding="UTF-8")
file.readline()
for sor in file :
    eredmény.append(Eredmény(sor))
file.close

z=0
print(f"3.2 feladat: Futók száma: {len(eredmény)}")
for i in range(len(eredmény)):
    if eredmény[i].TavSzazalek==100 and eredmény[i].Kategoria=="Noi":
        z+=1
print(f"3.3 feladat: Célba érkező női sportolók: {z} fő")


hossz=0
index=0
for i in range(len(eredmény)):
    if len(eredmény[i].Verszenyzo)>hossz:
        index=i
        hossz=len(eredmény[i].Verszenyzo)
print(f"3.4 feladat: Leghosszabb nevű futó\n\tNév: {eredmény[index].Verszenyzo}\n\tRajtszám: {eredmény[index].Rajtszam}\n\tEredmény: {eredmény[index].Versenydio}")

össz=0
db=0
for i in range(len(eredmény)):
    if eredmény[i].Kategoria=="Ferfi" and eredmény[i].TavSzazalek==100:
        ido=eredmény[i].Versenydio.split(":")
        ora=float(ido[0])+(float(ido[1])/60)+(float(ido[2])/3600)
        össz+=ora
        db+=1
print(f"3.5 Férfi sportolók átlagos ideje: {össz/db} óra")