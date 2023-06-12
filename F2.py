#11. feladat
def terület(x,y):
    z=x*y
    return z


x=int(input("Kérem az első számot(m): "))
y=int(input("Kérem a második számot(m): "))
try:
    print(f"Telek területe: {terület(x,y)} m2")
except terület(x,y)<100:
    print("Hiba! Túl kicsi a terület!")
except x==-1 or y==-1:
    print("")
while x!=-1 or y!=-1:
    x=int(input("Kérem az első számot(m): "))
    y=int(input("Kérem a második számot(m): "))
    try:
        print(f"Telek területe: {terület(x,y)} m2")
    except terület(x,y)<100:
        print("Hiba! Túl kicsi a terület!")
    except x==-1 or y==-1:
        print("")


