import random
def lotto_numbers():
    results=[]
    while len(results)<6:
        random_numbers = random.randint(1,45)
        if random_numbers in results:
            print("results 안에 random_numbers가 있으므로, results 안에 추가하지 않습니다. ")
        else:
            results.append(random_numbers)
            print(random_numbers)
    results.sort()
    return results
print("생성된 로또 번호는",lotto_numbers(),"입니다")
