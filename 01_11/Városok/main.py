from functiones import *
from typing import List

varosLista:List[Varos]=[]

FaljBeolvas(varosLista)
print(f'3. feladat: Városok száma: {len(varosLista)} db')
print(f"4. feladat: Indiai nagyvárosok lakosságának összgege {Indiai(varosLista)}")
print(f'5. feladat: A legnagyobb város adatai:')
print(f"\tNév: {varosLista[Legnagyobb(varosLista)].Nev}")
print(f"\tOrszág: {varosLista[Legnagyobb(varosLista)].Orszag}")
print(f"\tLakosság: {varosLista[Legnagyobb(varosLista)].lakossag}")
print(f"6. feladat: {Magyar(varosLista)}")
print(f"7. feladat: Városok egy szóközzel: {EgySzokoz(varosLista)}")
print(f"8. feladat: Ország statisztika:")
print(Statisztika(varosLista))
print(f"9. feladat: kína.txt")
KinaiVarosok(varosLista)