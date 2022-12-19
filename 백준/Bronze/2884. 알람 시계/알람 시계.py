h, m = map(int, input().split())

if m >= 45:
  min = m - 45
  print(h, min, sep=(' '))
if h > 0 and m < 45:
  min = m + 15
  hour = h - 1
  print(hour, min, sep=(' '))
if h == 0 and m < 45 :
  hour = h + 23
  min = m + 15
  print(hour, min, sep=(' '))