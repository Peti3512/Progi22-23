from data import *

def Betoltes():
    file=open("jarmu.txt", "r", encoding="utf-8")
    for sor in file:
        adatok=sor.strip().split(" ")
        ora=int(adatok[0])
        perc=int(adatok[1])
        mperc=int(adatok[2])
        rendszam=adatok[3]
        ido=ora*3600+perc*60+mperc
        jaror.append((ora,perc,mperc,rendszam,ido))
    file.close()

def Munkaido():
    kezd=jaror[0][0]
    veg=jaror[-1][0]+1
    return veg-kezd

def Orankent():
    n=jaror[0][0]
    for i in range(len(jaror)):
        if jaror[i][0]==n:
            print(f"{n} óra: {jaror[i][3]}")
            n+=1

def Szamol():
    Kamion=0
    Busz=0
    Motor=0
    Kocsi=0
    for i in range(len(jaror)):
        if jaror[i][3][0]=="K":
            Kamion+=1
        if jaror[i][3][0]=="M":
            Motor+=1
        if jaror[i][3][0]=="B":
            Busz+=1
        else:
            Kocsi+=1
    print(f"{Kamion} db kamion.\n{Busz} db busz.\n{Motor} db motor.\n{Kocsi} db személygépkocsi.")

def Forgalom():
    max_ertek=0
    max_index=0
    for i in range(len(jaror)-1):
        if jaror[i+1][4]-jaror[i][4]>max_ertek:
            max_ertek=jaror[i+1][4]-jaror[i][4]
            max_index=i
    print(f"Leghosszabb forgalom mentes időszak: ", end="")
    print(f"{jaror[max_index][0]}:{jaror[max_index][1]}:{jaror[max_index][2]} - {jaror[max_index+1][0]}:{jaror[max_index+1][1]}:{jaror[max_index+1][2]}")

def Keres():
    jók=[]
    kers=input("Kérem a rendszámot: ")
    if kers[0]!="*":
        for i in range(len(jaror)):
            if kers[0]==jaror[i][3][0]:
                jók.append(jaror[i][3])
        if kers[1]!="*":
            for i in range(len(jók)):
                if kers[1]!=jók[i][1]:
                    jók.pop(i)
            if kers[3]!="*":
                for i in range(len(jók)):
                    if kers[3]!=jók[i][3]:
                        jók.pop(i)
                if kers[4]!="*":
                    for i in range(len(jók)):
                        if kers[4]!=jók[i][4]:
                            jók.pop(i)
                    if kers[5]!="*":
                        for i in range(len(jók)):
                            if kers[5]!=jók[i][5]:
                                jók.pop(i) 
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                    elif kers[5]=="*":
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                elif kers[4]=="*":
                    if kers[5]!="*":
                        for i in range(len(jók)):
                            if kers[5]!=jók[i][5]:
                                jók.pop(i) 
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                    elif kers[5]=="*":
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                if kers[4]!="*":
                    for i in range(len(jók)):
                        if kers[4]!=jók[i][4]:
                            jók.pop(i)
                    if kers[5]!="*":
                        for i in range(len(jók)):
                            if kers[5]!=jók[i][5]:
                                jók.pop(i) 
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
            elif kers[3]=="*":
                if kers[4]!="*":
                    for i in range(len(jók)):
                        if kers[4]!=jók[i][4]:
                            jók.pop(i)
                    if kers[5]!="*":
                        for i in range(len(jók)):
                            if kers[5]!=jók[i][5]:
                                jók.pop(i) 
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                    elif kers[5]=="*":
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                elif kers[4]=="*":
                    if kers[5]!="*":
                        for i in range(len(jók)):
                            if kers[5]!=jók[i][5]:
                                jók.pop(i) 
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                    elif kers[5]=="*":
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                    
        elif kers[1]=="*":
            if kers[3]!="*":
                for i in range(len(jók)):
                    if kers[3]!=jók[i][3]:
                        jók.pop(i)
                if kers[4]!="*":
                    for i in range(len(jók)):
                        if kers[4]!=jók[i][4]:
                            jók.pop(i)
                    if kers[5]!="*":
                        for i in range(len(jók)):
                            if kers[5]!=jók[i][5]:
                                jók.pop(i) 
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                    elif kers[5]=="*":
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                elif kers[4]=="*":
                    if kers[5]!="*":
                        for i in range(len(jók)):
                            if kers[5]!=jók[i][5]:
                                jók.pop(i) 
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                    elif kers[5]=="*":
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                if kers[4]!="*":
                    for i in range(len(jók)):
                        if kers[4]!=jók[i][4]:
                            jók.pop(i)
                    if kers[5]!="*":
                        for i in range(len(jók)):
                            if kers[5]!=jók[i][5]:
                                jók.pop(i) 
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
            elif kers[3]=="*":
                if kers[4]!="*":
                    for i in range(len(jók)):
                        if kers[4]!=jók[i][4]:
                            jók.pop(i)
                    if kers[5]!="*":
                        for i in range(len(jók)):
                            if kers[5]!=jók[i][5]:
                                jók.pop(i) 
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                    elif kers[5]=="*":
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                elif kers[4]=="*":
                    if kers[5]!="*":
                        for i in range(len(jók)):
                            if kers[5]!=jók[i][5]:
                                jók.pop(i) 
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                    elif kers[5]=="*":
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
    elif kers[0]!="*":
        for i in range(len(jaror)):
            jók.append(jaror[i][3])
        if kers[1]!="*":
            for i in range(len(jók)):
                if kers[1]!=jók[i][1]:
                    jók.pop(i)
            if kers[3]!="*":
                for i in range(len(jók)):
                    if kers[3]!=jók[i][3]:
                        jók.pop(i)
                if kers[4]!="*":
                    for i in range(len(jók)):
                        if kers[4]!=jók[i][4]:
                            jók.pop(i)
                    if kers[5]!="*":
                        for i in range(len(jók)):
                            if kers[5]!=jók[i][5]:
                                jók.pop(i) 
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                    elif kers[5]=="*":
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                elif kers[4]=="*":
                    if kers[5]!="*":
                        for i in range(len(jók)):
                            if kers[5]!=jók[i][5]:
                                jók.pop(i) 
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                    elif kers[5]=="*":
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                if kers[4]!="*":
                    for i in range(len(jók)):
                        if kers[4]!=jók[i][4]:
                            jók.pop(i)
                    if kers[5]!="*":
                        for i in range(len(jók)):
                            if kers[5]!=jók[i][5]:
                                jók.pop(i) 
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
            elif kers[3]=="*":
                if kers[4]!="*":
                    for i in range(len(jók)):
                        if kers[4]!=jók[i][4]:
                            jók.pop(i)
                    if kers[5]!="*":
                        for i in range(len(jók)):
                            if kers[5]!=jók[i][5]:
                                jók.pop(i) 
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                    elif kers[5]=="*":
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                elif kers[4]=="*":
                    if kers[5]!="*":
                        for i in range(len(jók)):
                            if kers[5]!=jók[i][5]:
                                jók.pop(i) 
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                    elif kers[5]=="*":
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                    
        elif kers[1]=="*":
            if kers[3]!="*":
                for i in range(len(jók)):
                    if kers[3]!=jók[i][3]:
                        jók.pop(i)
                if kers[4]!="*":
                    for i in range(len(jók)):
                        if kers[4]!=jók[i][4]:
                            jók.pop(i)
                    if kers[5]!="*":
                        for i in range(len(jók)):
                            if kers[5]!=jók[i][5]:
                                jók.pop(i) 
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                    elif kers[5]=="*":
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                elif kers[4]=="*":
                    if kers[5]!="*":
                        for i in range(len(jók)):
                            if kers[5]!=jók[i][5]:
                                jók.pop(i) 
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                    elif kers[5]=="*":
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                if kers[4]!="*":
                    for i in range(len(jók)):
                        if kers[4]!=jók[i][4]:
                            jók.pop(i)
                    if kers[5]!="*":
                        for i in range(len(jók)):
                            if kers[5]!=jók[i][5]:
                                jók.pop(i) 
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
            elif kers[3]=="*":
                if kers[4]!="*":
                    for i in range(len(jók)):
                        if kers[4]!=jók[i][4]:
                            jók.pop(i)
                    if kers[5]!="*":
                        for i in range(len(jók)):
                            if kers[5]!=jók[i][5]:
                                jók.pop(i) 
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                    elif kers[5]=="*":
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                elif kers[4]=="*":
                    if kers[5]!="*":
                        for i in range(len(jók)):
                            if kers[5]!=jók[i][5]:
                                jók.pop(i) 
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
                    elif kers[5]=="*":
                        if kers[6]!="*":
                            for i in range(len(jók)):
                                if kers[6]!=jók[i][6]:
                                    jók.pop(i)
                            print(jók)
                        elif kers[6]=="*":
                            print(jók)
        
        
        

