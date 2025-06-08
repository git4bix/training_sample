class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def intro(self):
        return f"I'm {self.lname} {self.fname}"

    def sleep(self):
        print("I will sleep for 8hr")

class Stud(Person):
    def __init__(self, lname, fname, level):
        super().__init__(fname,lname)
        self.level = level

    def intro(self):
        return super().intro() + f" And I'am {self.level} student"

pr = Person("JD","valenzuela")
st = Stud("Aki","Valenz","Grade6")

print(pr.intro())
print(st.intro())