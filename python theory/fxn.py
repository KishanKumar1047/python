
#function in python

# def my_function(a,b) :
#     print('hello world', a+ b)
# my_function(7,9)    

# def fxn(a,b) :
#     average = (a+b)/2
#     print(average)

# fxn(8,3)    

def fxn(a,b) :
    """This is a function which will calculate average of two numbers
    and this function doesnot work for three numbers"""
    
    average = (a+b)/2
   # print(average)
    return average

m =  fxn(8,3)   
print(m) 
print(fxn.__doc__)
