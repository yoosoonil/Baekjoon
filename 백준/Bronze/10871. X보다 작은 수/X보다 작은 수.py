a, b = map(int, input().split())

num = list(map(int, input().split()))

numlist = []

for i in range(a):
  if int(num[i]) < int(b):
    numlist.append(num[i])

print(*numlist, sep=' ') # 리스트에서 괄호 없애기 = *list, sep은 문자열 사이에 넣을 것 정해주기