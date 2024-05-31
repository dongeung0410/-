class Drink:
    def __init__(self,name,n):
        self.menu={"커피":3000,"녹차":2500,"아이스티":3000}
        self.name = name
        self.total = 0
        self.count=n

    def sell(self):
        if self.name == "커피" or self.name == "녹차" or self.name == "아이스티":
            print(self.name,n,self.menu[self.name]*self.count)
        else:
            print("음료 주문이 틀렸습니다.")



name = input("주문할 음료를 말하세요:")
n= int(input("수량을 선택하세요:"))
drink = Drink(name, n)
drink.sell()