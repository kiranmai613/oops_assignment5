# Challenge 3: Implement the Complete Student Class
class Student:
    def __init__(self,__name,__RollNmber):  #private properties
        self.__name=__name
        self.__RollNumber=__RollNmber
        print(f"name  : {self.__name} \nrollno : {__RollNmber}")

    def setName(self,name): 
        self.__name=name
    def getName(self):
        return self.__name
    def setRollNumber(self,Rollnumber):
        self.__RollNumber=Rollnumber
    def getRollNumber(self):
        return self.__RollNumber
obj=Student("sia",67)
(obj.setName("kim"))
(obj.setRollNumber(7))
print((obj.getName()))
print((obj.getRollNumber()))




    