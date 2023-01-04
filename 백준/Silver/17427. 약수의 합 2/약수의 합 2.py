num = int(input())

divisors = 0

# 처음 짠 코드인데, 시간복잡도로 시간초과.
# for j in range(1, num+1):
#   for k in range(1, j+1):
#     if j % k == 0:
#       divisors += k

# 시간복잡도가 O(n)이기에 시간초과하지 않음.
for i in range(1, num+1):
  divisors += (num//i) * i  
# num이하의 자연수 중에서 i를 약수로 갖는 개수는 num//i개이다. 즉, i의 배수의 개수 = i를 약수로 갖는 수

print(divisors)
