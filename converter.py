class EU():
    cigarete,alcohol, other=0.3,0.2,0.15
    def calculate(self, *args):
        print("Tax of Cigarete: "+str(self.cigarete*args[0]))
        print("Tax of Alcohol: "+str(self.alcohol*args[1]))
        print("Tax of Others: "+str(self.other*args[2]))

class United_Kingdom(EU):
    wine=2
    cigarete = 0.2
    def calculate(self, *args):
        w_weight=args[0]/75
        w_price=args[1]
        print("Tax on wine per 75cl: "+str(self.wine*w_weight*w_price))
        print("Tax on cigarette: "+str(self.cigarete*args[2]))

class German(EU):
    def calculate(self, *args):
        list=[]
        for i in range(0, len(args)):
            if args[i]>2:
                list.append(args[i] - 2)
        print("Tex on cigarette: "+str(self.cigarete*(list[0]-2)))

class France(EU):
    def calculate(self, *args):
        print("Tax of Cigarete: " + str(0.4 * args[0]))
        print("Tax of Alcohol: " + str(0.25 * args[1]))

class Spain(EU):
    def calculate(self, *args):
        list = []
        for i in range(0, len(args)):
            if args[i]>4:
                list.append(args[i] - 4)
        print("Tax of Cigarete: " + str(0.1 * args[0]))
        print("Tax of Alcohol: " + str(0.1 * args[1]))

class Poland(EU):
    def calculate(self, *args):
        list = []
        for i in range(0, len(args)):
            if args[i] > 50:
                list.append(args[i] - 50)
        list=self.convert(list)
        print("Tax will be calculated for amount of: ", end="")
        lst=list[-1]
        for l in list:
            if l==lst:
                print(str(l) + " euro")
            else:
                print(str(l) + ", ", end="")

    def convert(self,args):
        list=[]
        for arg in args:
            euro=arg/4.31
            list.append(euro)    # 1Euro= 4.31 Zloty
        return list

e=EU()
uk=United_Kingdom()
g=German()
f=France()
s=Spain()
p=Poland()
if __name__ == '__main__':
    while True:
        print("1. Europe\n2.United Kingdom\n3.German\n4.France\n5.Spain\n6.Poland\nEnter your choice: ",end="")
        ch=int(input("Enter your choice: "))
        if ch is 1:
            e.calculate(int(input("Enter price of cigarette: ")),int(input("Enter price of alcohol: ")),int(input("Enter others: ")))
        elif ch is 2:
            uk.calculate(int(input("Enter amount of wine: ")), int(input("Enter price of wine: ")),
                        int(input("Enter price of cigarette: ")))
        elif ch is 3:
            g.calculate(int(input("Enter price of cigarette: ")))
        elif ch is 4:
            f.calculate(int(input("Enter price of cigarette: ")),int(input("Enter price of alcohol: ")))
        elif ch is 5:
            s.calculate(int(input("Enter price of cigarette: ")),int(input("Enter price of alcohol: ")))
        elif ch is 6:
            p.calculate(int(input("Enter price of cigarette: ")),int(input("Enter price of alcohol: ")),int(input("Enter others: ")))
        else:
            break