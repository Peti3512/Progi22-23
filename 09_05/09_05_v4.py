szám1=input('Mondj egy számot: ')
szám2=input('Mondjá még egyet testvérem és add má oda azt a Rolexet csak meg akarom nézni, hogy eredeti-e: ')
sz1=int(szám1)
sz2=int(szám2)
öszeg=sz1+sz2
kül1=sz1-sz2
kül2=sz2-sz1
hány1=sz1/sz2
hány2=sz2/sz1
szor=sz1*sz2
print('A két szám összege: ',öszeg)
print(sz1, '+', sz2, '=', öszeg)
print('A két szám egyik különbsége: ', kül1)
print(sz1, '-', sz2, '=', kül1)
print('A két szám másik különbsége: ', kül2)
print(sz2, '-', sz1, '=', kül2)
print('A két szám egyik hányadosa: ', hány1)
print(sz1, '/', sz2, '=', hány1)
print('A két szám másik hányadosa: ', hány2)
print(sz2, '/', sz1, '=', hány2)
print('A két szám szorzata: ',szor)
print(sz1, '*', sz2, '=', szor)
print(sz1//sz2)
print(sz1%sz2)
print(sz2//sz1)
print(sz2%sz1)