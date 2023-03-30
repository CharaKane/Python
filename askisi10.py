import math

a= int (input ("dose ton proto arithmo: "))
b= int (input ("dose ton deytero arithmo: "))
c= int (input ("dose ton trito arithmo: "))

D=b**2-4*a*c

if D>0:
  x1=(-b+math.sqrt(D))/(2*a)
  x2=(-b-math.sqrt(D))/(2*a)
  print("H diakrinousa einai: " , D)
  print (" H proti riza exei apotelesma: " , x1, " kai h deyteri riza exei apotelesma: " , x2)

else:
  print("H diakrinousa einai arnitiki. Den iparxoun lisis ")
