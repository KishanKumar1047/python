#string modify 
# mystr = 'ram is, Good guy'
# print(mystr.upper())
# print(mystr.lower())
# print(mystr)
# print(mystr.strip())
# print(mystr.replace('r','k'))
# print(mystr.split(" , "))


#python list
# numbers = [2,7,1,9,13]
# print(numbers[2])
# numbers.sort()
# print(numbers)
# numbers.append(98)
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers.insert(3,89)
# print(numbers)
# print(type(numbers))


#swap two numbers.
# a = 1
# b = 8
# a,b = b,a
# print(a,b)


 #short hand if else 
# a = 2
# b = 8
# print('a') if a>b else print ("=") if a==b else print (b)

#use of pass statement
# a = 33
# b = 200
# if b > a :
#     pass


#while loop

# i = 1
# while i<6 :  
#     print(i)
#     i += 1



#break statement in while loop
# i = 1
# while i<6 :
#         print(i)
#         if i == 3 :
#             break
#         i += 1

#continue statement in while loop

# i = 0
# while i<6 :
#       i += 1
#       if i == 3 :
#             continue
#       print(i)        

# else statement in while loop
# i  = 1
# while i<6 :
#     print(i)
#     i += 1
# else :
#     print('i is no longer less than 6')

# python for loops

# fruits = ['apple','banana','cherry']
# for x in fruits :
#     print(x)
#     if x == 'banana' :
#         break


# fruits = ['apple','banana','cherry']
# for x in fruits :
#      if x == 'banana' :
#          continue 
#      print(x)




#range_function

# for x in range (6) :
#     print(x)



# for x in range (2,6) :
#     print(x)    
    


# nested loops.

adj = ['red','big','tasty']
fruits = ['apple','banana','cherry']

for x in adj :
    for y in fruits :
        print(x,y)