import random
def lotto_numbers():
    results=[]
    while len(results)<6:
        random_numbers = random.randint(1,45)
        if random_numbers not in results:
            results.append(random_numbers)
    results.sort()
    return results
print("생성된 로또 번호는",lotto_numbers(),"입니다")
