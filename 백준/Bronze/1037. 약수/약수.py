num = int(input())

약수들 = list(map(int, input().split()))

진짜수 = min(약수들) * max(약수들)

print(진짜수)