napok=int(input("Hány napot vizsgáljak?: "))
while napok<1:
    napok=int(input("Hány napot vizsgáljak?: "))
n=1
esonap=[]
for i in range(napok):
    csapadek=int(input(f"A(z) {n}. napon mért csapadék(mm): "))
    while csapadek<0 or csapadek>1000:
        csapadek=int(input(f"A(z) {n}. napon mért csapadék(mm): "))
    if csapadek>0:
        esonap.append(n)
    n+=1
print(f"Ennyiszer esett az eső: {len(esonap)}")