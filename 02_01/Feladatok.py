print("1. feladat")
x=float(input("Kérem az első számot: "))
y=float(input("Kérem a második számot: "))
if y>x:
    print(f"{y} nagyobb mint {x}.")
elif x>y:
    print(f"{x} nagyobb mint {y}.")
else:
    print("A két szám egyenlő")


print("4.feladat")
a=float(input("Kérem a téglalap egyik oldalát(cm): "))
b=float(input("Kérem a téglalap másik oldalát(cm): "))
print(f"Téglalap területe: {a*b}\nTégalalp kerülete: {2*(a+b)}")

print("6. feladat")
x=float(input("Kérem az első számot: "))
y=float(input("Kérem a második számot: "))
z=float(input("Kérem a harmadik számot: "))
lnagy=max(x,y,z)
lkis=min(x,y,z)
kozep=0
if z==lnagy or z==lkis:
    if y==lnagy or y==lkis:
        kozep=x
    elif x==lnagy or x==lkis:
        kozep=y
elif x==lnagy or x==lkis:
    if y==lnagy or y==lkis:
        kozep=z
    elif z==lnagy or z==lkis:
        kozep=y
elif y==lnagy or y==lkis:
    if x==lnagy or x==lkis:
        kozep=z
    elif z==lnagy or z==lkis:
        kozep=x
print(f"{lnagy} a legnagyobb, {kozep} a középső és {lkis} a legkisebb szám.")