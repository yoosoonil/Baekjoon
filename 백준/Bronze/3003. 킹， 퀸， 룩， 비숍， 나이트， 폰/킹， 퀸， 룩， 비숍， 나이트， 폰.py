numbers = list(map(int, input().split()))

chessnumber =[1, 1, 2, 2, 2, 8]

num = []
for i in range(6):
    change = chessnumber[i] - numbers[i]
    if change >= 0:
        num.append(change)
    else:
        num.append(change)
        
print(*num, sep=' ')
        