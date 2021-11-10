#1.feladaT Dolgozók száma? 

f=open("berek2020.txt",encoding="utf-8")
fo=0
asztalosok=0
karbFo,karbFiz=0,0
maxFiz=0
maxDolg=[]
sor=f.readline()
for sor in f:
    fo+=1
    sor=sor.strip('\n').split(";")
    if(sor[2]=="asztalosműhely"):
        asztalosok+=1
    if(sor[2]=="karbantartás"):
        karbFo+=1
        karbFiz+=int(sor[4])
    
    if maxFiz<int(sor[4]):
        maxFiz=int(sor[4])
        maxDolg=sor
    #print(sor)

f.close()
print("1.feladat: "+str(fo)+" fő")
print("2.feladat: "+str(asztalosok)+" fő")
karbAtlag=karbFiz/karbFo
if karbAtlag%1==0:
    karbAtlag=int(karbAtlag)
else:
    karbAtlag=round(karbAtlag,1)
print("3.feladat: "+str(karbAtlag)+" Ft")
print("4.feladat")
print("\tNév"+maxDolg[0])
print("\tFizetés: "+maxDolg[4])
