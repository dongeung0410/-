A=input("몇단까지 출력할까요:")
a=int(A)
for n in range(1,a+1):
    print("----[%s단]----"%n)
    for k in range(1,20):
        print(n,"x",k,"=",n*k )