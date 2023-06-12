tejfaj=int(input("Hány tejfélét vizsgálunk?: "))
while tejfaj<1 or tejfaj>100:
    tejfaj=int(input("Hány tejfélét vizsgálunk?: "))
P=float(input("Mennyi legyen a minimum ársapka?: "))
while P<1 or P>999:
    P=float(input("Mennyi legyen a minimum ársapka?: "))
Q=float(input("Mennyi legyen a maximum ársapka?: "))
while Q<P or Q>1000:
    Q=float(input("Mennyi legyen a maximum ársapka?: "))
x=1
jo=0
for i in range(tejfaj):
    ar=float(input(f"Kérem a(z) {x}. tej árát: "))
    while ar<1 or ar>1000:
        ar=float(input(f"Kérem a(z) {x}. tej árát: "))
    if ar>P and ar<Q:
        jo+=1
    x+=1
print(f"{jo} tej van az ársapkákon belül.")
