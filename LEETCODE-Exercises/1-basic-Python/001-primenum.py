takeNum = int(input())


for num in range(1, takeNum+1):
    if takeNum > 1:
        for i in range(2, num):
            if num%i == 0:
                break
        else:
            print(num)