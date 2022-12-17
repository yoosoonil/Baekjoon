a = int(input())
b = int(input())
a_list = list(map(int, str(a)))
b_list = list(map(int, str(b)))

c_list = []
for i in range(2, -1, -1):
  c = a * b_list[i]
  print(c)
  c_list.append(c)

d = c_list[0] + c_list[1]*10 + c_list[2]*100

print(d)