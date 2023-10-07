def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)) #Tức là số n - 1000 hoặc 2000 có nhỏ hơn bằng 100 không
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))   
print(near_thousand(2200))
