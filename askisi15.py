t= float(input ("dose timi:"))


if t<=200:
    print("To teliko poso pliromis einai:", t-t*0.07)
elif t<=400:
    print("To teliko poso pliromis einai:", t-t*0.13)
elif t<=600:
   print("To teliko poso pliromis einai:", t-t*0.18)
else:
    print("To teliko poso pliromis einai:", t-t*0.25)

