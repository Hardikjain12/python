class Student:
    def __init__(self,fullname):
        # print(self)
        self.name = fullname
        print("adding new student in Database...")
        
    def hello(self):
        print("hello everyone",self.name)
        
    
s1 = Student("Hardik")
print(s1.name)
s1.hello()


'''
Counstructor it is basiclly a init function in eery class 
It invoked at time of object creation
It is always executed if u write it or not python will create utomatically for u 

Comstructor always takes a parameter THAT IS "SELF"

__init__ Function

'''
