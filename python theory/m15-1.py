print('simple calculator :')
a = int(input('enter 1st number :'))
b = int(input('enter 2nd number :'))
ch = input('enter operator :')

if ch == '+' :
 print(a + b)

elif ch == '-' :
 print(a-b)

elif ch == '*' :
  print(a*b)

elif ch == '/' :

  print (a/b)

elif ch == '**' :
 print(a**b)

else :
  print ('error !')