nevek = ['Németh Mihály','Lukács Mónika','Szűcs Sándor','Varga Imre','Farkas József','Deák Eszter','Sipos Krisztián','Lakatos János','Szabó István','Boros Gyula','Fazekas Norbert','Boros Krisztián','Kiss Károly','Fülöp Zsuzsanna','Szilágyi Viktória','Sipos Tímea','Papp Szabolcs','Gulyás János','Fodor Sándor','Antal Gábor','Szűcs János','Farkas Csaba','Horváth Mihály','Balogh Csaba','Gál Szabolcs','Kis Csaba','Hegedűs Gabriella','Somogyi István','Szalai Katalin','Balogh Miklós','Török István','Deák Krisztina','Kovács György','Pintér Lajos','Varga Péter','Mészáros Norbert','Kovács Csaba','Szabó Zoltán','Tóth Gyula','Németh Erzsébet','Sipos György','Gulyás Imre','Lukács Lajos','Magyar Szabolcs','Fülöp Tibor','Juhász Tibor','Balázs Károly','Varga Andrea','Király Éva','Szűcs Edit','Szilágyi Róbert','Simon Erzsébet','Katona András','Szűcs Péter','Fehér József','Sipos Tímea','Simon Zsuzsanna','Nagy Tibor','Kiss János','Hegedűs András','Tóth József','Németh Viktória','Simon Mónika','Fekete Sándor','Nagy Erika','Mészáros Imre','Pintér János','Fekete Zsolt','Deák Imre','Szabó Róbert','Szilágyi Tamás','Fekete Erzsébet','Fazekas Krisztián','Nagy Ferenc','Somogyi Gyula','Török Gabriella','Szalai Eszter','Katona Mihály','Király Viktória','Fazekas Tibor','Szilágyi Mónika','Antal Szilvia','Lakatos László','Fülöp Szilvia','László Zsuzsanna','Fülöp László','Mészáros Ildikó','Bíró Péter','Kovács Ildikó','Török Ferenc']
szazalekok = [56,84,44,44,92,84,52,64,84,92,48,76,44,88,52,64,40,80,84,100,56,76,40,68,72,60,40,60,40,100,84,76,88,88,88,76,64,56,88,92,96,52,100,100,44,76,52,100,48,92,100,60,56,52,72,80,96,100,92,72,60,76,88,92,88,48,96,96,48,48,80,56,48,76,60,84,88,84,52,56,100,64,52,60,48,68,80,100,44,100]

#1. Hány vizsgázó adata van az állományban?
print(f"{len(nevek)} vizsgázó szerepel a listában.")
#2. Hányan tettek sikeres vizsgát (75% vagy felette)?
n = 0
for i in range(len(szazalekok)):
    if i>=75:
        n+=1
print(f"{n} sikeres vizsga született.")
#3. Mi a legrosszabb eredmény?
print(f"{min(szazalekok)} %-os a legrosszabb vizsga eredmény")
#4. Írja ki, hogy kik érték el a legrosszabb eredményt?
n=[]
for i in range(len(szazalekok)):
    if i == min(szazalekok):
        n+=nevek[i]
for i in range(len(n)):
    print(n[i], end="")
print("érte el a legrosszabb eredményt.")
#5. Kérjen be egy nevet, írja ki, hogy hány százalékot ért el a tanuló! Ha nincs ilyen tanuló akkor írja ki, hogy "Nincs ilyen tanuló!"
n=input("Kérek egy nevet: ")
m=False
for i in range(len(nevek)):
    if n==nevek[i]:
        print(f"{n} eredménye: {szazalekok[i]}")
        m=True
if m==False:
    print("Nincs ilyen vizsgázó a listában.")
