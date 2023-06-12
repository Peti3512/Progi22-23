napok=int(input("Hány napon át mérted meg a jég vastagságát?: "))
while napok<1:
    napok=int(input("Hány napon át mérted meg a jég vastagságát?: "))
n=1
v0nap=[]
for i in range(napok):
    vastagság=int(input(f"A(z) {n}. napon mért vastagság: "))
    while vastagság<0 or vastagság>20:
        vastagság=int(input(f"A(z) {n}. napon mért vastagság: "))
    if vastagság==0:
        v0nap.append(n)
    n+=1
print(f"Eze(ke)n a nap(ok)on volt 0 centiméter vastag a jég: {v0nap}, azaz {len(v0nap)} nap nem volt jég")