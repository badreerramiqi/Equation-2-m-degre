import math
def descriminant(a,b,c) :
 delta = (b**2) - 4 * a * c
 if delta > 0 :
        x1 =( - b - sqrt(delta) )/(2 * a )
        x2 = ( - b - sqrt(delta) )/(2 * a)
        print("les solutions sont :",x1,"et",x2)
 elif  delta == 0 :
        x = ( - b ) / (2 * a)
        print("la solution est :",x)
 else :
        print("no solution reel .")
a = int(input("entrer a :"))
b = int(input("entrer b :"))
c = int(input("entrer c :"))
descriminant(a,b,c)