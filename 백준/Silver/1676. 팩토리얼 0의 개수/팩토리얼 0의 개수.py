n = int(input())

result = 1
num = []
for i in range(1, n + 1):
  result *= i
  
strresult = list(str(result))
for j in strresult[::-1]:
  if int(j) == 0:
    num.append(j)
  if int(j) > 0:
    break


print(len(num))