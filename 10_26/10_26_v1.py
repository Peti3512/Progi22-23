napook_szama = int(input("Napok száma: "))
tömb = []
esös_napok = 0

for i in range(napook_szama):
    mm=int(input(f"Kérem a {i+1} napi csapadékot miliméterben: "))
    tömb.append(mm)
    if  tömb[i]>0:
        esös_napok+=1
print(tömb)
print(f"Esős napok száma: {esös_napok}")