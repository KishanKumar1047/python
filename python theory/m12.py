# cel =int(input("enter temperature in celsius"))
# fahrn= cel*(9/5) + 32
# print("the temperature in fahrenheit is" + str(fahrn))



 #prime number
n=int(input("enter num"))
prime = True
for i in range(2,n):  
    if(n%i==0):
        prime= False
        break
    else:
        prime= True

if prime:
    print("num is prime") 
else:
    print("not prime")           




        


