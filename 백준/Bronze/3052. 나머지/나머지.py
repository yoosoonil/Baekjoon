import sys

rd_ =[]

for _ in range(10):
  n = int(sys.stdin.readline())
  rd = n % 42
  rd_.append(rd)
  
print(len(set(rd_)))