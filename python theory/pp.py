
n = int(input('enter number'))
prime = True
for i in range(2,n) :
    if n%i == 0 :
        prime = False
        break
    else :
        prime = True
        #list.append(i)
if prime == True :
    list.append(i)

print(list)
