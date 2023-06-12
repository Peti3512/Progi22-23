class Pilota:
    def __init__(self, sor:str):
        adatok=sor.strip().split(";")
        self.név=adatok[0]
        self.szül_dátum=adatok[1]
        self.nemzetiség=adatok[2]
        self.rajtszám=adatok[3]
pilota:list[Pilota]=[]
file=open("pilotak.csv","r",encoding="UTF-8")
file.readline()
for sor in file:
    pilota.append(Pilota(sor))
file.close()

print(f"3. feladat: {len(pilota)}")
print(f"4. feladat: {pilota[-1].név}")
print("5. feladat")
for i in pilota:
    x=i.szül_dátum.strip().split(".")
    y=int(x[0]+x[1]+x[2])
    if y<19010101:
        print(f"\t{i.név} ({i.szül_dátum})")

x=99
y=0
print("6.feladat: ", end="")
for i in pilota:
    if i.rajtszám!="": 
        if int(i.rajtszám)<int(x):
            x=i.rajtszám
            y=i
for i in pilota:
    if i.rajtszám!="": 
        if int(i.rajtszám)==int(x):
            print(i.nemzetiség, end=" ")

x=[]
z=[]
a=1
for i in pilota:
    if i.rajtszám!="":
        if i.rajtszám not in x:
            x.append(i.rajtszám)
for i in x:
    y=0
    for j in pilota:
        if j.rajtszám!="":
            if i==j.rajtszám:
                y+=1
                
    if y>1 and a==1:
        print(f"\n7. feladat: {i}", end="")
        a+=1
    elif y>1 and a>1:
        print(f", {i}", end="")
