# class Student :
#     name = "karan"
     
# s1 = Student()
# print(s1.name)    

# s2 = Student()
# print(s2.name)

# class Car :
#     name = "Mercedes"
#     brand = "Royal"
    
# car1 = Car()
# print(car1.name)
# print(car1.brand)    

'''constructor or __init__ function, always executed when object is initiated '''

# class Student :
#     name = "karan"
    
#     # default constructor
#     def __init__(self):
#         pass
    
#     # parameterized constructor
#     def __init__(self, fullname,marks) :
#         self.name = fullname
#         self.marks = marks
#         print("adding new student in database..")
        
# s1 = Student("karan",97)
# print(s1.name,s1.marks)    

# s2 = Student("arjun",88)
# print(s2.name,s2.marks)   


""" attributes - any data like name ,marks 
  s1,s2,s3,s4 """ 
  
# class Student :
#     college_name = "ABC College" # class attributes
#     name = "anonymous" # another class attributes
    
#     # parameterized constructor
#     def __init__(self,name,marks) :
#         self.name = name  # object attributes
#         self.marks = marks
#         print("adding students")
        
# s1 = Student("karan", 99)
# print(s1.name) # karan is output bcz object have higher preference over class
# print(s1.college_name)
        
''' methods - fxn belons to objects''' 
# class Student :
#     def __init__(self,name,marks) :
#         self.name = name
#         self.marks = marks
        
#     # methods
#     def welcome(self) :
#         print("welcome student,",self.name) 
        
#     def get_marks(self) :
#         return self.marks       
        
# s1 = Student("karan", 99)
# s1.welcome()    
# print(s1.get_marks())    
        
        
# let's practice

class Student :
    def __init__(self,name,marks) :
        self.name = name
        self.marks = marks 
        
    def avg(self) :
        sum = 0
        for val in self.marks :
            sum += val
        print("hello",self.name,"your avg score is : ",sum/3)    
                   
s1 = Student("KISHAN",[99,95,97]) 
s1.avg()

# s1.name = "rahul"
# s1.avg()








