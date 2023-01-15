t = int(input())

n = list(map(int, input().split()))
max_ = max(n)
scores = 0
for i in range(t):
  falsescore = n[i] / max_ * 100
  scores += falsescore

print(scores/(len(n)))