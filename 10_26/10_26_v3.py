emberek = int(input("Hány embert vízsgáljak meg?: "))
tanuló_jegyek = []
osztályzatok=[0,0,0,0,0]
for i in range(emberek):
    tanuló_jegyek.append(int(input(f"A(z) {i+1}. tanuló jegye: ")));
    osztályzatok[tanuló_jegyek[i]-1] += 1

print(tanuló_jegyek)
print(emberek)
for i in range(5):
    print(f"{i+1} osztályzatból isszesen {osztályzatok[i]}db született az évfolyamon.")
print(osztályzatok)