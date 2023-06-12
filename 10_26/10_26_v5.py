számok_száma=int(input("Hány szám faktoriálisát kéri:"))
számok=[]
faktoriális=[]
for i in range(számok_száma):
    számok.append(int(input(f"Kérem a(z) {i+1}. számot: ")))
    fakt_szám=1
    for j in range(1, számok[i]+1):
        fakt_szám *=j
    faktoriális.append(fakt_szám)
print(számok)
print(faktoriális)