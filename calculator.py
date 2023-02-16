# Challenge 2: Implement a Calculator Class
class Calculator:
    num1=float(input("enter num : "))
    num2=float(input("enter other num : "))
    print(f"numbers are {num1} and {num2}")
    def add(self):
        return (self.num1+self.num2)
    def subtract(self):
        return (self.num1-self.num2)
    def multiply(self):
        return (self.num1*self.num2)
    def divide(self):
        return (self.num1//self.num2)
obj=Calculator()
print(obj.add())
print(obj.divide())
print(obj.subtract())
print(obj.multiply())





