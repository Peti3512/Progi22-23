from data import autók

filename="autók.csv"

def menu():
    print('0 - Kilépés')
    print('1 - Új autó felvétele')
    print('3 - Autó törlése')
    return input('Kérem válasszon: ')

def AutoBetolt():
    file=open(filename, 'r', encoding='utf-8')
    global cimsor
    cimsor=file.readline().strip()
    for sor in file:
        darabol=sor.strip().split(';')
        autók[darabol[0]]=int(darabol[1])
    file.close()

def AutóFelvétel():
    print('Új autó:\n')
    a=input('Autó típusa: ')
    t=int(input('Teljesítmény: '))
    autók[a]=t
    file=open(filename, 'a', encoding='utf-8')
    file.write(f'\n{a};{t}')
    file.close

def Listázás():
    print('Autók listája:\n')
    for key,value in autók.items():
        print(f'{key} - {value}')

def AutóTörlés():
    print('Autó törlése:\n')
    a=input('A törlendő autó típusa: ')
    if a in autók:
        autók.pop(a)
        file=open(filename, 'w', encoding='utf-8')
        file.write(cimsor)
        for key,value in autók.item():
            file.write(f'\n{key};{value}')
        file.close()