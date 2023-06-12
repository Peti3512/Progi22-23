def Tökeletes(i):
    osztok=0
    for j in range(1,i):
        if i%j==0:
            osztok+=j
    if osztok!=i:
        return False
    return True
            


print("2. feladat: Tökéletes számok\nKérek két természetes számot:")
x=int(input("tól = "))
y=int(input("ig = "))
print(f"Tökéletes számok {x} és {y} között:")
Z=0
for i in range(x,y+1):
    Tökeletes(i)
    if Tökeletes(i)==True:
        Z+=1
    if Tökeletes(i)==True and Z==1:
        print(i, end="")
    elif Tökeletes(i)==True and Z>1:
        print(f"; {i}", end="")
if Z==0:
    print("A megadott tartományban nincsen tökéletes szám!")