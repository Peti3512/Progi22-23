print("LNKO kivonás algoritmussal")
a= int(input("a = "))
b= int(input("b = "))
mszam=max(a,b)
kszam=min(a,b)
while mszam!=kszam:
    if mszam>kszam:
        while mszam>kszam:
            mszam-=kszam
    else:
        while kszam>mszam:
            kszam-=mszam
    if mszam<0 or kszam<0:
        print("A legnagyobb közös osztó az 1")
        break
print(f"LNKO({a},{b}) = {mszam}")
