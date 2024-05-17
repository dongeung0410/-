def valid_RRN(numbers):

    numbers = numbers.replace("-","")

    if len(numbers) != 13:
        return "주민 번호 숫자 입력 오류입니다."

    check_code_numbers =[2,3,4,5,6,7,8,9,2,3,4,5]

    total_sum = sum(int(numbers[i])* check_code_numbers[i] for i in range(12))

    k_number=total_sum%11

    z_number= (11 - k_number) % 10

    if z_number == int(numbers[-1]):
        return "유효한 주민등록번호입니다"
    else:
        return "잘못된 주민등록번호입니다."

RRN_numbers=input("주민등록번호 입력하세요:")
print(valid_RRN(RRN_numbers))
