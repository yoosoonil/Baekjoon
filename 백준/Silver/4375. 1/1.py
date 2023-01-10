while True:   # 문제에서 테스트 수를 안줘서 try, exept 사용
    try:
        n = int(input())
    except:
        break
    num = 0
    i = 1
    
    while True:
        num = num*10 + 1
        num %= n
        if num == 0:
            print(i)
            break
        i+=1