number=int(input("Enter the number:"))

for i in range(0,11):
    if i==5:
        continue
    print(number,"*",i,"=",number*i)
   