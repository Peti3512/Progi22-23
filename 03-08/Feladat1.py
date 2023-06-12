print("1. feladat: A háromszög szerkesztehetősége\nKérem a háromszög oldalait!")
a=float(input("a = "))
b=float(input("b = "))
c=float(input("c = "))
if a+b>c and a+c>b and c+b>a:
    print("A háromszög megszerkeszthető!")
else:
    print("A háromszög nem szerkeszthető a magadott adatokkal!")