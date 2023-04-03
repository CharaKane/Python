v= float(input ("dose to varos sou:"))
y= float (input ("dose to ycos sou:"))

dms=v/y**2

if dms>=15:
    print("Poli sovara lipovaris")
elif dms<=16:
    print("Sovara lipovaris")
elif dms<=18.5:
   print("Lipovaris")
elif dms<=25:
    print("Kanoniko varos")
elif dms<=30:
    print("Ypervaros")
elif dms<=35:
    print("Metria Paxisarkos")
elif dms<=40:
    print("Sovara paxisarkos")
else:
    print("Poli sovara paxisarkos")

