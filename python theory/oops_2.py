
#del object

# class Student :
#     def __init__(self,name) :
#         self.name = name 
        
# s1 = Student("kishan")
# # del s1
# print(s1.name)     

""" # for private atributes two underscore

        self.__name # like """
        
        
# Inheritance { parent base - child base} 

# class Car :
#     color = "black"
#     @staticmethod
#     def start() :
#         print("car started..")
        
#     @staticmethod
#     def stop () :
#         print("car stopped. ")
        
# class ToyotoCar(Car) :  # use of inheritance
#     def __init__(self,name) :
#         self.name = name
        
# car1 = ToyotoCar("fortuner")
# car2 = ToyotoCar("prius")

# print(car1.start())    
# print(car1.color)    
                

""" upto this single inheritance"""

# class Fortuner(ToyotoCar) :
#     def __init__(self,type) :
#         self.type = type
        
# car1 = Fortuner("diesel")
# car1.start()        

""" up to this multi-level inheritance"""

# multilevel inheritance

# class A :
#     varA = "welcome to class A"
    
# class B :
#     varB = "welcome to class B"  
      
# class C(A,B) :
#     varC = "welcome to class C"   
    
# c1 = C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)


# supermethod - to access parent's  class method

# class Car :
#     def __init__(self,type) :
#         self.type = type
   
#     @staticmethod
#     def start() :
#         print("car started..")
        
#     @staticmethod
#     def stop () :
#         print("car stopped. ")
        
# class ToyotoCar(Car) :  
#     def __init__(self,name,type) :
#         super().__init__(type)
#         self.name = name
       
        
# car1 = ToyotoCar("prius","electric")
# print(car1.type)

     

# class method

# class Person :
#     name = "anonymous"
    
#     @classmethod
#     def ChangeName(cls,name) :
       
#      cls.name = name  
    
    
# p1 = Person()
# p1.ChangeName("rahul kumar")
# print(p1.name)
# print(Person.name)
    
    
# @property decorator use

# class Student :
#         def __init__(self,phy,chm,maths) :
#                 self.phy = phy   
#                 self.chm = chm  
#                 self.maths = maths  
                

        
#         @property
#         def Percentage(self) :
#                 return str((self.phy + self.chm + self.maths)/3) + "%"
        
# stu1 = Student(98,97,99)
# print(stu1.Percentage)

# stu1.phy = 86
# print(stu1.Percentage)
        
# polymorphism - overloading-same operators different meaning


# compex number usnig class

# dunder function __add__ ; __sub__ ; __mul__


class Complex :
        def __init__(self,real,imag) :
                self.real = real
                self.imag = imag  
        def shownumber (self) :
                print(self.real ,"i +",self.imag,"j")
                
        def add(self,num2) :
                newreal = self.real + num2.real  
                newImg = self.imag + num2.imag  
                return Complex(newreal,newImg)
        
        #using dunder fxn
        def __add__(self,num2) :
                newreal = self.real + num2.real  
                newImg = self.imag + num2.imag  
                return Complex(newreal,newImg)
        
        def __sub__(self,num2) :
                newreal = self.real - num2.real  
                newImg = self.imag - num2.imag  
                return Complex(newreal,newImg)
                 
                

num = Complex(1,3)
num.shownumber()
num2 = Complex(4,5)
num2.shownumber()

# num3 = num.add(num2)
# num3.shownumber()

num3 = num + num2
num3.shownumber()

num3 = num - num2
num3.shownumber()




                        
       
        