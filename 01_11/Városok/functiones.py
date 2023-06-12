from data import *

def FaljBeolvas(varosLista:list):
    file=open("varosok.txt", "r", encoding="utf-8")
    file.readline()
    for sor in file:
        varosLista.append(Varos(sor))
    file.close()

def Indiai(varosLista:list):
    összeg=0
    for i in varosLista:
        if i.Orszag=="India":
            összeg+=i.lakossag*1000
    return összeg

def Legnagyobb(varosLista:list):
    max=0
    for i in range(len(varosLista)):
        if varosLista[i].lakossag>varosLista[max].lakossag:
            max=i
    return max

def Magyar(varosLista:list):
    for i in range(len(varosLista)):
        if varosLista[i].lakossag=="Magyarország":
            van="Van Magyar város"
            return van
        van="Nincs Magyar város"
    return van

def EgySzokoz(varosLista:list):
    db=0
    for i in varosLista:
        if len(i.Nev.split(' '))==2:
            db+=1
    return db

def Statisztika(varosLista:list):
    szt={}
    for i in varosLista:
        if i.Orszag in szt.keys():
            szt[i.Orszag]+=1
        else:
            szt[i.Orszag]=1
    dict(sorted(szt.items()))
    for key, value in szt.items():
        if value>6:
            print(f"\t{key} - {value}")
    
def KinaiVarosok(varosLista:list):
    file=open("kina.txt","w",encoding="utf-8")
    for i in varosLista:
        if i.Orszag=="Kína":
            file.write(f"{i.Nev};{i.lakossag}\n")
    file.close