class Repülők:
    def __init__(self,sor:str):
        adatok=sor.strip().split(";")
        self.típus=adatok[0]
        self.év=int(adatok[1])
        self.utas=adatok[2]
        self.személyzet=adatok[3]
        self.utazósebesség=int(adatok[4])
        self.felszállótömeg=int(adatok[5])
        self.fesztáv=float(adatok[6].replace("," , "."))
        if self.utazósebesség>=1200:
            self.sebesség="Szuperszonikus"
        if int(adatok[4])>=1000 and int(adatok[4])<1200:
            self.sebesség="Transzszonikus"
        if int(adatok[4])>=500 and int(adatok[4])<1000:
            self.sebesség="Szubszonikus"
        if int(adatok[4])<500:
            self.sebesség="Alacsony sebebességű"
repülők:list[Repülők]=[]

file=open("utasszallitok.txt", "r")
file.readline()
for sor in file:
    repülők.append(Repülők(sor))
file.close

print(f"2. feladat: Adatsorok száma: {len(repülők)}")

x=0
for i in repülők:
    if x<i.fesztáv:
        x=i.fesztáv
for i in repülők:
    if i.fesztáv==x:
        print(f"3. feladat: Legnagyobb fesztávú utasszállító típus: {i.típus}")
        break

a=[]
for i in repülők:
    if "Boeing" in i.típus and i.típus not in a:
        a.append(i.típus)
print(f"4. feladat: Boeing típusok száma: {len(a)}")

y=0
p=""
for i in repülők:
    if "-" in i.utas:
        r=i.utas
        u=r.split("-")
        z=u[1]
        if int(z)>y:
            y=int(z)
            p=i.típus
    else:
        r=i.utas
        if int(r)>y:
            y=int(r)
            p=i.típus

for i in repülők:
    if p==i.típus:
        print(f"5. feladat: A legtöbb utast szállító repülőgéptípus\n\tTípus: {p}\n\tElső felszállás: {i.év}\n\tUtasok száma: {i.utas}\n\tSzemélyzet: {i.személyzet}\n\tUtazósebesség: {i.utazósebesség}")
        break
    

x={'Alacsony sebebességű': 0, 'Szubszonikus': 0, 'Transzszonikus': 0,  'Szuperszonikus': 0, }
for i in repülők:
    if i.sebesség in x:
        x[i.sebesség]+=1

print("6. feladat:\n\t", end="")
p=False
for i in x:
    if x[i]==0:
        print(f"{i} ")
        p=True
if p==False:
    print("\tMinden sebesség kategóriában van repülőgéptípus!")


print(f"7. feladat:")
for i in x:
    print(f"\t{i}: {x[i]} db")