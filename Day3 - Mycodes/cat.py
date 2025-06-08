class Cat:
    def __init__(self, val_cat, door="close"):
        self.val_cat = val_cat
        self.door = door

    def close(self):
        if self.val_cat == "close" and self.door == "close":
            print("the door already close")
        else:
            print("you opened the door")
            self.val_cat = "open"
            return self.val_cat

    def open(self):
        if self.val_cat == "open" and self.door == "open":
            print("the door already open")
        else:
            print("you opened the door")
            self.val_cat = "close"
            return self.val_cat


#lags = input("please enter to 1=open and 2=close: ")

#if lags == 1:
kitten = Cat("open")
print(kitten.open())
#elif lags == 2:
kitten2 = Cat("close")
print(kitten2.close())

kitten3 = Cat("open")
print(kitten3.close())