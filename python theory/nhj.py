# class car :
#     def start(self) :
#         print('car started..')
        
# class toyo :
#     def stop(self) :
#         print('car stopped..')
        
# class sona(car,toyo) :
#     def going(self) :
#         print("self lol")
        
# c1 = sona()
# print(c1.start())
# print(c1.stop())
# print(c1.going())                       

class person :
    def __init__(self,name,age) :
        self.name = name 
        self.age = age
        
        
p1 = person("nishu",22)   
print(p1.name)
print(p1.age)    
        