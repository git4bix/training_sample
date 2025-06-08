"""class Employee:

    def __init__(self, name, id):
        print(f"employee {name} assigned ID {id}")

employee1 = Employee("Rich","12315")
employee2 = Employee("John","12888")
"""

"""
class Employee:
   def __init__(self, name, id):
        self.nam = name
        self.ed = id
        self.task = []
        print(f"employee {name} assigned ID {id}")

    def add_work(self, task):
        return self.task.append(task)


employee1 = Employee("Rich", "12315")
employee2 = Employee("John", "12888")

print("employee 1 name: ", employee1.nam)
print("employee 1 name: ", employee2.nam)

employee1.add_work("create charts")
print(employee1.task)

"""
"""
class wall:
    def __init__(self, initial_am):
        self.amount = initial_am

fud_wallet = wall(250)
transpo = wall(1000)
nam1 = wall("samp")

print("food buget:", fud_wallet.amount)
print("transpo buget:", transpo.amount)
print("person:", nam1.amount)
"""
"""
class Student:
    def __init__(self, name, level):
        self.nam = name
        self.lvl = level

    def introduct(self):
        return f"I'm {self.nam}! I'm a {self.lvl}"

stud1 = Student("john", '3rd yr coll')
print(stud1.introduct())

stud2 = Student("jd", '2nd yr coll')
print(stud2.introduct())

"""

class Character:
    def __init__(self, hl=10, st=10, df=10):
        self.helt = hl
        self.stre = st
        self.dt = df

    def attack(self, other):
        dmg = self.stre - other.dt
        other.helt -= dmg

player = Character(st=100)
enemy = Character()

player.attack(enemy)
print(enemy.helt)