price = int(input())

T = int(input())

pp = []
for i in range(1, T+1):
  p, n = map(int, input().split())
  tp = p * n
  pp.append(tp)

tpp = sum(pp)
if price == tpp:
  print('Yes')
else:
  print('No')