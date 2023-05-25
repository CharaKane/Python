protasi="The rain in Spain stays mainly in the plain"
gramma= str(input("dose gramma:"))

thesi=0
s=0
print("To gramma a emfanizetai tis thesis:")

for x in protasi:
    thesi+=1

    if x==gramma:
        print(thesi)
        s+=1
print("kai emfanizetai sunolika", s, "fores")
