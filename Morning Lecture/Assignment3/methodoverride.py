#Method overriding
from multipledispatch import dispatch

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def printInfo(self):
        print(f"Name: {self.name}\nAge: {self.age}")
        
    # @dispatch(string)
    # def erroll(name):
    #     print
    
    
class Student(Person):
    def __init__(self,name,age,reg_no):
        super().__init__(name,age)
        self.regno = reg_no
    
    def printInfo(self):
        print(f"Name:\t{self.name}\nAge:\t{self.age}\nReg_No:\t{self.regno}")

class Lecturer(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary
        
    def printInfo(self):
        print(f"Name:\t{self.name}\nAge:\t{self.age}\nSalary:\t{self.salary}")
        
def main():
    student1 = Student("Andrew",21,"23/U/05555/PS")
    student1.printInfo()
    print("\n\n")
    lecturer1 = Lecturer("Dr Jeff",32,2500000)
    lecturer1.printInfo()
    
    #Method Resolution Order (MRO) is the order in which python searches for methods or attributes in a class hierarchy,
    #especially in multiple inheritence. it uses a depth first left to right ordering.
    print(Lecturer.mro())
    
if __name__ == "__main__":
    main()
    
    
        