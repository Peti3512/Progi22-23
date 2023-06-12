
#8. faledat
x=float(input("Kérek egy valós számot: "))
y=int(input("Kérek egy egész számót: "))
z=x
for i in range(y-1):
    z*=x
print(z)

#6.feladat
x=int(input("Kérem az első számot: "))
y=int(input("Kérem a második számot: "))
z=int(input("Kérem a harmadik számot: "))
if x%2!=0 or z%2!=0 or y%2!=0:
    print("Van páratlan szám.")
else:
    print("Nics páratlan szám")


#14. feladat
def Kocka(x,y):
    for i in range(x):
        print("")
        for j in range(y):
            print("*", end="")

x=int(input("Kérem a sorok számát: "))
y=int(input("Kérem az oszlopok számát: "))
Kocka(x,y)

#16. feladat
def kethá(x):
    z=False
    if x%2==0 and x%3==0:
        z=True
    return z

x=int(input(f"\nKérem a számot: "))
print(f"{x} osztható 2-vel sé hárommal(True/False): {kethá(x)}")

#35. feladat
def palindrome(x):
    z=[]
    y=True
    for i in reversed(range(len(x))):
        z.append(x[i])
    for i in range(len(z)):
        if z[i]!=x[i]:
            y=False
            break
    return y

x=input("Kérek egy szót: ")
if palindrome(x):
    print("A szó palindróme")
else:
    print("A szó nem palindróme")


#17.feladat
def parpar(x,y,z):
    if x%2!=0 or z%2!=0 or y%2!=0:
        return False
    else:
        return True

x=int(input("Kérem az első számot: "))
y=int(input("Kérem a második számot: "))
z=int(input("Kérem a harmadik számot: "))
if parpar(x,y,z)==True:
    print("Mind három szám páros")
elif parpar(x,y,z)==False:
    print("Van a számok közt páratlan")


#18.feladat
def összeg(x,y):
    z=0
    if x==y:
        z="A két szám egyenlő, nincs intervallum."
        return z
    elif x>y:
        for i in range(y,x+1):
            z+=i
        return z
    else:
        for i in range(x,y+1):
            z+=i
        return z


x=int(input("Kérem az első számot: "))
y=int(input("Kérem a második számot: "))
print(f"Az intervallumban található számok összege: {összeg(x,y)}")

#Pitagoraszi feladat
def Pitagorasz(x,y,z):
    c=max(x,y,z)
    a=min(x,y,z)
    b=(x+y+z)-(c+a)
    if ((a*a)+(b*b))==(c*c):
        return True
    else:
        return False

x=int(input("Kérem az első számot: "))
y=int(input("Kérem a második számot: "))
z=int(input("Kérem a harmadik számot: "))
if Pitagorasz(x,y,z)==True:
    print("A háromszög derékszögű.")
else:
    print("A háromszög nem derékszögű.")