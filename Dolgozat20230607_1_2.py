import math

#1. feladat
print(f"1. feladat: Számok szorzata\nKérem az alsó és felső határt!")
x=int(input("a = "))
y=int(input("b = "))
while x>y:
    print("Az alsó határ kisebb legyen mint a felső!")
    x=int(input("a = "))
    y=int(input("b = "))
z=1
for i in range(x,y+1):
    z*=i
print(f"A számok szorzata: {z}")

#2. feladat
def atfogo(a,b):
    c=round(math.sqrt((a*a)+(b*b)),2)
    if c<5:
        raise ValueError("Hiba! Túl kicsi a derékszögű háromszög")
    return c

print("2. Derékszögűháromszög átfogójának kiszámítása!")
print("Kérem a befogó méretét!")
a=float(input("Egyik befogó mérete: "))
b=float(input("Másik befogó mérete: "))
try:
    print(f"Az átfogó mérete: {atfogo(a,b)}")
except ValueError as hiba:
    print(hiba)
while a!=0 or b!=0:
    a=float(input("Egyik befogó mérete: "))
    if a==0:
        break
    b=float(input("Másik befogó mérete: "))
    if b==0:
        break
    try:
        print(f"Az átfogó mérete: {atfogo(a,b)}")
    except ValueError as hiba:
        print(hiba)