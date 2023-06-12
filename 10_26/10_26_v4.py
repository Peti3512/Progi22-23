körök_száma=int(input("Kérem a körök számát: "))
jörök_idö=[]
összeg=0

for i in range(körök_száma):
    jörök_idö.append(float(input(f"Kérem a {i+1}. kör idejét.")))
    összeg+=jörök_idö[i]
print(f"Az átlag kör idő {összeg/körök_száma}")