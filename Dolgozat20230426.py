import random

#1.feladat
N=int(input("Hány alkalommal legyen feldobás? "))
e=0
f=0
for i in range(N):
    a=random.randint(1,6)
    b=random.randint(1,6)
    c=random.randint(1,6)
    d=a+b+c
    print(f"\tDobás: {a} + {b} + {c} = {d}\tNyert: ", end="")
    if d<10:
        print("Anni")
        e+=1
    else:
        print("Panni")
        f+=1
print(f"A játék során {e} alkalommal Anni, {f} alkalommal Panni nyert.")



#2.feladat
def jegy(pont,x):
    if pont>=round(x*0.85):
        z="jeles (5)"
    elif pont<round(x*0.85) and pont>=round(x*0.70):
        z="jó (4)"
    elif pont<round(x*0.70) and pont>=round(x*0.55):
        z="közepes (3)"
    elif pont<round(x*0.55) and pont>=round(x*0.40):
        z="elégséges (2)"
    elif pont<round(x*0.40) and pont>=round(x*0):
        z="elégtelen (1)"
    return z
y=0

x=int(input("Mennyi a dolgozat maximális pontszáma: "))
for i in range(3):
    print(f"A(z) {i+1}. tanuló:")
    nev=input(f"\tNeve: ")
    pont=int(input(f"\tPontszáma: "))
    if pont<0 or pont>x:
        print(f"\tHelytelen pontszám")
        pont=int(input(f"\tPontszáma: "))
    y+=pont
    print(f"\t{nev} osztályzata: {jegy(pont,x)}")
print(f"A dolgozatok átlaga: {y/3}")