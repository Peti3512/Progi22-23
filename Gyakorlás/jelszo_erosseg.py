def jelszo_erosseg(jelsz):
    erösseg=2
    if len(jelsz)==5 or len(jelsz)==6:
        erösseg+=1
    if len(jelsz)>=7:
        erösseg+=2
    for karakter in jelsz:
        if karakter.isalpha():
            erösseg+=0
        elif karakter.isdigit():
            erösseg+=0
        else:
            erösseg+=2
    if len(jelsz)<1 or "123" in jelsz.lower():
            erösseg==0
    print(f'Jelszó erőssége: {erösseg}') 
jelsz=input('Kérem a jelszót: ')
jelszo_erosseg(jelsz)
 