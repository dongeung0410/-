def calculate_average_price(current_shares, buy_price, additional_shares, current_price):

    total_investment = current_shares * buy_price


    new_total_investment = total_investment + additional_shares * current_price


    new_total_shares = current_shares + additional_shares


    average_price = new_total_investment / new_total_shares

    return average_price


num_trades = int(input("입력할 주식 거래 정보의 개수를 입력하세요: "))

for _ in range(num_trades):

    current_shares = float(input("보유한 주식의 수를 입력하세요: "))
    buy_price = float(input("주식을 산 가격을 입력하세요: "))
    current_price = float(input("현재 주식 가격을 입력하세요: "))
    additional_shares = float(input("현재 사려는 주식 수를 입력하세요: "))


    if current_shares < 0 or buy_price < 0 or current_price < 0 or additional_shares < 0:
        print("오류: 주식 정보에 음수 값이 포함되어 있습니다. 올바른 값을 입력하세요.")
        continue


    average_price = calculate_average_price(current_shares, buy_price, additional_shares, current_price)


    additional_shares_needed = (current_shares * average_price + additional_shares * current_price) / current_price - current_shares


    print("추가로 구매 했을 때 평균 단가:", average_price)
    print("현재 가격과 같은 평균 단가를 갖기 위해 추가로", additional_shares_needed, "주를 더 구매해야 합니다.")