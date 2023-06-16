
user_number = int(input("enter your number"))

fac = 1
factoril = []

for i in range(1, user_number+1):
    fac = fac * i
    factoril.append(fac)
    
if user_number in factoril:
        print("your number is fac")
else:
        print("your number is not fac")    


