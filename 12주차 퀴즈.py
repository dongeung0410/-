class 붕어빵:
    def __init__(self,name,price2):
        self.contents=name
        self.price=price2
        self.total=0
    def sell(self):
        self.total += self.price
        print(self.contents,"를",self.price,"가격에 판매하였습니다.")

    def eat(self):
        print(self.contents,"을 먹습니다.")

슈붕 = 붕어빵("슈붕",1000)

슈크림_붕어빵 = 붕어빵("슈붕", 1000)
슈크림_붕어빵.sell()
슈크림_붕어빵.sell()
슈크림_붕어빵.sell()
슈크림_붕어빵.sell()
print(슈크림_붕어빵.total)

