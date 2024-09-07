# find the factors of voth the nubmers 
# compare the factors


a = int(input('enter 1st number to check for co-prime'))
b = int(input('enter 2nd  number to check for co-prime'))
l1 = []
l2 = []
for i in range (2, a + 1) :
    if a % i == 0 :
        l1.append(i)
print(l1)        

for i in range (2, b + 1) :
    if b % i == 0 :
        l2.append(i)
print(l2)

for m in l1:
    
    for n in l2:
        z=n
        if(m==n):
            print(f"{a} and {b} are not co prime")
            break
    if(m==z):
        break
    
    if(m==a):
        print("Coprime ")
        break






