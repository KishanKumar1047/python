# class car :
#     @staticmethod
#     def start():
#         print("car started")
        
# class mahindra(car) :
#     @staticmethod
#     def stop() :
#         print("car stopped")
        
# class suzuki(mahindra) :
#     def __init__(self,type) :
#         self.type = type
        
# c1 = suzuki("petrol")
# print(c1.start()) 
# print(c1.stop())  

class car :
    @staticmethod
    def start():
        print("car started")
        
class mahindra() :
    @staticmethod
    def stop() :
        print("car stopped")

class suzuki(mahindra,car) :
    def __init__(self,type) :
        self.type = type
       
       
c1 = suzuki("petrol")     
print(c1.start())  
print(c1.stop()) 
        
        
         