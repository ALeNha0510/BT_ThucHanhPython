def list_count_4(arr):
  dem = 0  
  for num in arr:
    if num == 4:
      dem = dem + 1

  return dem

print(list_count_4([1, 4, 6, 7, 4]))
print(list_count_4([1, 4, 6, 4, 7, 4, 2, 7, 3, 6, 1, 4]))
