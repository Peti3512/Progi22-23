class Lift:
    def __init__(self,sor:str):
        adatok=sor.strip().split(" ")
        self.használat_idopontja=adatok[0]
        self.kartya_sorszama=int(adatok[1])
        self.induloszint=int(adatok[2])
        self.erkezeoszint=int(adatok[3])
lift:list[Lift]=[]

file=open("hotellift.txt", "r")
for sor in file:
    lift.append(Lift(sor))
file.close

print(f"3.feladat: Összes lifthasználat: {len(lift)}")
print(f"4.feladat: {lift[0].használat_idopontja} - {lift[-1].használat_idopontja}")
x=0
for i in lift:
    if i.erkezeoszint>x:
        x=i.erkezeoszint
print(f"5. feladat: Célszint max: {x}")
print("6.feladat:")
x=input("\tKártya száma: ")
y=input("\tCélszint száma: ")
try:
    kartya=int(x)
except:
    kartya=int(5)
try:
    celszint=int(y)
except:
    celszint=int(5)
z=0
for i in lift:
    if i.kartya_sorszama==kartya and i.erkezeoszint==celszint:
        print(f"A(z) {kartya}. kártyával utaztak a(z) {celszint}. emeltre!")
        z=1
        break

if z==0:
    print(f"A(z) {kartya}. kártyával nem utaztak a(z) {celszint}. emeltre!")


print("8.feladat: Statisztika")
napok=[]
for i in lift:
    if i.használat_idopontja not in napok:
        napok.append(i.használat_idopontja)
for i in napok:
    a=0
    for j in lift:
        if i==j.használat_idopontja:
            a+=1
    print(f"\t{i} - {a}x")

stat={}
print("")
for i in lift:
    if i.használat_idopontja not in stat:
        stat[i.használat_idopontja]=1
    else:
        stat[i.használat_idopontja]+=1
for i in stat:
    print(f"\t{i} - {stat[i]}x")