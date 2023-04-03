kw= float(input ("dose tin katanalosi sou:"))

if kw<=100:
    print("To teliko poso pliromis einai:", kw*0.171)
elif kw<=300:
    print("To teliko poso pliromis einai:", kw*0.2145)
elif kw<=500:
   print("To teliko poso pliromis einai:", kw*0.25023)
elif kw<=1000:
    print("To teliko poso pliromis einai:", kw*0.3591)
elif kw<=5000:
    print("To teliko poso pliromis einai:", kw*0.5504)
else:
    print("To teliko poso pliromis einai:", kw*0.674)
    
