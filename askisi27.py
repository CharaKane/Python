t= float(input("Dose timh:"))
f= float(input("Dose fpa 0.13 h 0.24:"))

while t<=0:
    t= float(input("Dose timh:"))
    f= float(input("Dose fpa 0.13 h 0.24:"))
    
if f==0.13:
     teltim=t+t*0.13
     print("H telikh timh tou einai:", teltim)

elif f==0.24:
     teltim=t+t*0.24
     print("H telikh timh tou einai:", teltim)
else:
  print("Lektiko Lathos")
    
