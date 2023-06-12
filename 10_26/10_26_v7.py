szavak=[]
aktual_word=""
i=1

while (aktual_word!='.' or '!'):
    aktual_word=szavak.append(input(f"Kérem a {i}. szót: "))
    aktual_word=[i-1]
    i += 1
print(szavak)