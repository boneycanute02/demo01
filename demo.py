class Student:
    name = None # properties
    age = None  # variables
    cgpa = None # Data members
    temp = 10

    def __init__(self,name,age,cgpa):   #Constructor
        print("Constructor Invoked")
        self.name = name;
        self.age = age;
        self.cgpa = cgpa;

    # behaviors : actions : functions
    def introduce(self):
        print("Hi , I am ",self.name,". My age is ",self.age,". I have a CGPA of ",self.cgpa," temp = ",self.temp)

    # self : represents an object of the current class  


# syntax : <ObjectName> = <Constructor>()
Apple = Student("Apple",45,10.3) # Real - entity : Memory is allocated for the object 
Apple.introduce()
Apple.temp = 20


Orange = Student("Orange",78,9.6)
Orange.introduce()
Apple.introduce()
# Cosntructor is automatically invoked dureing object creation


# Static variable will only have a single memory allocated to it 