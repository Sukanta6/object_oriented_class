# class Employee():
#     x=10
#     print('Inside Class Display',x)

#     def display(self):
#         self.y=20
#         print('Inside Display',self.y)

# emp = Employee()
# emp.display()

class Employee_1():
    x=10
    print('Inside Class Display',x)

    def __init__(self,y):
        self.a=y
        print('Inside Display',self.a)
    def display(self,b):
        self.c=b
        print('Inside Display',self.c)

emp = Employee_1(20)
emp.display(30)