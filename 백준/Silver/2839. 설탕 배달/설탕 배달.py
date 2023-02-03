n = int(input())

cnt = 0

while n >= 0:
  # 5로 나눈 나머지가 0 = 5의 배수
  if n % 5 == 0:
    # 봉지 수는 5의 배수(몫)
    cnt += int(n // 5)
    print(cnt)
    break
  # 5의 배수가 아닐때, 3을 빼면서 봉지수가 하나씩 늘어남
  # 3kg짜리 봉지가 늘어나는 셈
  # 3씩 빼면서 5의 배수가 될때까지 while문은 돌아가는 것임.
  n -= 3
  cnt += 1
  
else:
  print(-1)
  