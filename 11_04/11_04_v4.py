napok=int(input("Hány napot vizsgáljak?: "))
while napok<1:
    napok=int(input("Hány napot vizsgáljak?: "))

fok=float(input("Hány napot vizsgáljak?: "))
while fok<-20 or fok>50:
    fok=float(input("Hány napot vizsgáljak?: "))

n=1
melegek=0

for i in range(napok):
    napifok=int(input(f"A(z) {n}. napi hőmérséklet: "))
    while napifok<-20 or napifok>50:
        napifok=float(input("Hány napot vizsgáljak?: "))
    if napifok>fok:
        melegek+=1
    n+=1
print(f"{melegek} {fok} foknál melegebb nap volt.")