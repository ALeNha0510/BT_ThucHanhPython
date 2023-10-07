def is_group_member(arr, n):
   for value in arr:
       if n == value:
           return True
   return False

print(is_group_member([6, 8, 5, 2], 3))
print(is_group_member([0, 0, 1], 1))