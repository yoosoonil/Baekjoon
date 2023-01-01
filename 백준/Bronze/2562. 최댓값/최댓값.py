num_list = []

for i in range(1, 10):
  num = int(input())
  num_list.append(num)

max_ = max(num_list)
print(max_)

for i in range(len(num_list)):
  if num_list[i] == max_:
    print(i+1)