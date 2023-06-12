def mghlt(napok):
    max=0
    index=0
    for i in range(len(napok)):
        db=0
        for j in napok[i]:
            if j in "aáeéiíoóöőuúüű":
                db+=1
        if db>max:
            max=db
            index=i
    return index

napok=["hétfő", "kedd", "szerda", "csütörtök", "péntek"]
print(f"A legtöbb magánhangzó a {napok[mghlt(napok)]}-ben van.")

