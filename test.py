
import datetime as dt

class Account:
    def __init__(self):
        self.statement = []
        self.balance = 0
        self.run()

    def run(self):
        x = input("存款按D/取款按W：")
        tim = dt.datetime.now()
        flag,val = x.split()
        if flag =='D':
            self.balance += int(val)
            self.statement.append(('存入', val, tim.isoformat()))
        elif flag == 'W':
            self.balance -= int(val)
            self.statement.append(('取出', val, tim.isoformat()))

    def show(self):
        for i in self.statement:
            print(i)
        print(self.balance)


acc = Account()
acc.run()
acc.show()