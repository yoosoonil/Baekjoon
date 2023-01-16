t = int(input())

for _ in range(1, t + 1):
  scores = list(map(int, (input().split())))
  avg = sum(scores[1:]) / scores[0]
  
  cnt = 0
  for i in scores[1:]:
    if i > avg:
      cnt += 1
  
  per = (cnt/scores[0]) * 100    
  # %.3f는 소수셋째자리까지 출력
  print('%.3f' %per + '%')