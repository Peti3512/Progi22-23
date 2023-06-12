Sakk=['Julcsi', 'Ádám', 'Réka']
Kézi=['Ádám', 'Patrik', 'Zsombor']
Foci=['Patrik', 'Réka', 'Lili', 'Áron']
Szakkör=[]

for i in range(len(Sakk)):
    Szakkör.append(Sakk[i])

for i in range(len(Kézi)):
    talat=False
    for j in range(len(Szakkör)):
        if Szakkör[j]==Kézi[i]:
            talat=True
    if talat==False:
        Szakkör.append(Kézi[i])

for i in range(len(Foci)):
    talat=False
    for j in range(len(Szakkör)):
        if Szakkör[j]==Foci[i]:
            talat=True
    if talat==False:
        Szakkör.append(Foci[i])

print(Szakkör)