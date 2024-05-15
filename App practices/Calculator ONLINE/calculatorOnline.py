# Now we're gonna make a roster with employees

# first the employee class
class Employee:
    def __init__(self, name, age, roll, is_working):
        self.name = name
        self.age = age
        self.roll = roll
        self.is_working = is_working


manyEmployees = int(input("How many employees do you have?"))

for x in manyEmployees:
    name = str(input("Name: "))
    age = int(input("Age: "))
    roll = str(input("Roll: "))
    is_working = input("YES OR NOT: ")


    createEmployees = True
    while createEmployees is True:
        return employee + str(x) =  Employee(name, age, roll, is_working)


        ++1

        if manyEmployees >= len(manyEmployees):
            createEmployees = False