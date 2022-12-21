h, m = map(int, input().split())
p = int(input())
if p < 60:
  min = m + p
  if min >= 60:
    min = min - 60
    hour = h + 1
    if hour >= 24:
      hour = hour - 24
      print(hour, min, sep=(' '))
    else:
      print(hour, min, sep=(' '))
  else:
    hour = h
    print(hour, min, sep=(' '))

if p >= 60:
  p_hour = divmod(p, 60)[0]
  p_min = divmod(p, 60)[1]
  min = m + p_min
  hour = h + p_hour
  if min >= 60 :
    min = min - 60
    hour = hour + 1
    if hour >= 24:
      hour = hour - 24
      print(hour, min, sep=(' '))
    else:
      print(hour, min, sep=(' '))
  else:
    hour = hour
    if hour >= 24:
      hour = hour - 24
      print(hour, min, sep=(' '))
    else:
      print(hour, min, sep=(' '))