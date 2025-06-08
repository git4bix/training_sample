class acc:
    def __init__(self, amount):
        self._am = amount


    def depo(self, deposite):
        if self._am < 0:
            print("walang pera")
        else:
            self._am += deposite
            return deposite

    def wid(self, widraw):
        if self._am < widraw:
            print("walang pera")
        else:
            self._am -= widraw
            return widraw


    def bal(self):
        return f"Your current Balance is {self._am}"


acnt1 = acc(amount=400)


dep_sit = acnt1.depo(20)
w_drw = acnt1.wid(30)
print(acnt1._am)
print(f"your current balance is {acnt1.bal()}, widrawn money {w_drw}, deposited money {dep_sit}")
