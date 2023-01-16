def tiling(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  elif n == 2:
    return 2
  tile_array = [0, 1, 2]
  
  for i in range(3, n + 1):
    tile = tile_array[i - 1] +tile_array[i - 2] 
    tile_array.append(tile)
  return tile_array[n]

n = int(input())  
print(tiling(n) % 10007)