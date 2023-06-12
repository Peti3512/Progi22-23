from functions import *

AutoBetolt()

choice=''
while choice!='0':
    choice=menu()
    if choice=='1':
        AutóFelvétel()
    elif choice=='2':
        Listázás()
    elif choice=='3':
        AutóTörlés()