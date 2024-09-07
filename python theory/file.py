'''read file'''
f = open("demo.txt","r")
data = f.read()
 # print(data)
print(type(data))


data = f.read(5)# upto 5 letters
line1 = f.readline() # read entire line

# if no secondline then gives empty

f.close()

''' writing a file'''

f = open("demo.txt","w")
f.write("this is new line ")
# overwite the entire file


f = open("demo.txt","a")
f.write("this is new line ")
# add to file

'''creating new file'''

f = open("plain.txt","a")  # append or write
f.close()

''' reading and writing together'''

'''
a+ adding and reading
r+ for reading and writing
'''

# with syntax

with open("demo.txt","a") as f :
    data = f.read()
    print(data)
    
    
# delete file using module 

import os
os.remove("demo.txt")    