import math
import terbeli

test=terbeli.kup()
print("Felszín: "+str(test.felszin()))
print("Térfogat: "+str(test.terfogat()))

sikIdom=terbeli.rombusz(4,math.pi)
print("Kerulet: "+str(sikIdom.kerulet))
print("Terulet: "+str(sikIdom.terulet))