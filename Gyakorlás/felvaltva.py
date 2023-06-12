def felvaltva(szöveg):
    szöveg=szöveg.upper()
    for szavak in szöveg:
        i=1
        if i%2==0:
            szavak=szöveg[i-1].lower()
        i+=1
    print(szöveg)
szöveg=str(input("Kérem a szöveget: "))
felvaltva(szöveg)