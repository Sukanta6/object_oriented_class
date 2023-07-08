
# Simple Class with instances
class Employee:
    pass

emp_1= Employee()
emp_2= Employee()

emp_1.first = 'sukanta'
emp_1.last = 'biswas'

emp_2.first = 'John'
emp_2.last = 'Cook'

# print(emp_1.first, emp_1.last, emp_1.first+'.'+emp_1.last+'@gmail.com')
# print(emp_2.first, emp_2.last, emp_2.first+'.'+emp_2.last+'@gmail.com')


class employee_evo():
    "*** Code smarter not harder ***"
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {} {}'.format(self.first, self.last, self.email)

emp_1 = employee_evo('Sukanta', 'Biswas', 50000)
emp_2 = employee_evo('John', 'Cook', 60000)

print(employee_evo.__doc__)
print(emp_1.fullname())
print(employee_evo.fullname(emp_2))