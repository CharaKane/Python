s=0
i=1
p=0
d=0
while i<=3:
 a= float(input("Dose thermokrasia"))
 i=i+1
 s=s+a
 if a>p:
     p=a
 else:
     d=a

mo=s/3


print("O mesos oros ton thermokrasion einai:", mo, "H megisti thermokrasia einai:", p, "H elaxisti thermokrasia einai:", d) 
