e=0
k=0
h=0
n=0
ö=0
x=1

diakok=int(input("Kérem a diákok számát: "))
if diakok<1:
    diakok=int(input("Kérem a diákok számát: "))
for i in range(diakok):
    jegy=int(input(f"Kérem a(z) {x}. diák jegyét: "))
    while jegy>5 or jegy<1:
        jegy=int(input(f"Kérem a(z) {x}. diák jegyét: "))
    if jegy==5:
        ö+=1
    if jegy==4:
        n+=1
    if jegy==3:
        h+=1
    if jegy==2:
        k+=1
    if jegy==1:
        e+=1
    x+=1
print(f"{e} egyes, {k} kettes, {h} hármas, {n} négyes és {ö} ötös lett.")