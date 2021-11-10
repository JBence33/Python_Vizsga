lista=[]
print("Írd be a szánmokat: ",end="")
be=input()
while(be!="*"):
    try:
        be=float(be)
    except:
        print("Számokat írj bele pl:12.43: ",end="")
    else:
        lista.append(be)
        print("Írd be a számokat: ",end="")
    be=input()
print(lista)
atlag=sum(lista)/len(lista)
if(atlag%1==0):
    atlag=int(atlag,2)
else:
    atlag=round(atlag,2)
print("Átlag: "+str(atlag))

print("Elvárt átlag: ",end="")
eA=float(input())

print("Tűrés (%): ",end="")
tures=float(input())
tures=eA*tures/100
if((eA-tures)<=atlag) and ((eA+tures)>=atlag):
    print("Az adatok átlaga megfelel az elvárásoknak")
else:
    print("Az adatok hibásak!")
