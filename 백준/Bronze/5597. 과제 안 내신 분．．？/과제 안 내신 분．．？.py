p = []
p_ = []

for i in range(1, 31):
  p.append(i)
  
for j in range(1, 29):
  n = int(input())
  p_.append(n)
  

set_ = set(p) - set(p_)

print(min(set_))
print(max(set_))