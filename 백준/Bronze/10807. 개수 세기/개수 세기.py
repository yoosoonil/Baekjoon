T = int(input())

num = list(map(int, input().split()))

cnt = 0

num_v = int(input())

for i in range(T):
  if int(num[i]) == int(num_v):
    cnt += 1

print(cnt)