hofok=[]
print("Ír be a mérésed eredményeit pl.(21.35), végjel '0': ",end="")
fok=float(input())
while (fok!=0):
    hofok.append(input())
    print("Ír be a mérésed eredményeit pl.(21.35), végjel '0': ",end="")
    fok=float(input())
print("Írd be az elvárt hőmérsékletet:",end="")
atlagFOk=float(input())
print("Írd be a megengedett eltérést százalékban: ",end="")
szazalek=float(input())

szazalek=atlagFOk*(szazalek/100)
atlag=sum(hofok)/len(hofok)

if(atlagFOk-szazalek)<=atlag and (atlagFOk+szazalek)<=atlag:
    print("Jók vagyunk")
else:
    print("Mindenki megfog fagyni!")
