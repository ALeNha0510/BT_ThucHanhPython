import math

def KTraNgTo(n):
   if n == 1:
       return False       

   for i in range(2, int(math.sqrt(n))+1):
       if n % i == 0:
           return False
   return True

def DSSoNgTo(a, b):
   for i in range(a, b + 1):
       if KTraNgTo(i):
           print(i)

a = int(input("Nhập khoảng đầu tiên: "))
b = int(input("Nhập khoảng kết thúc: "))
if a < 0 or b < 0:
    print("vui lòng nhập số nguyên dương!")
else:
    print(f"Danh sách số nguyên tố trong khoảng từ {a}-{b} là: ")
    DSSoNgTo(a, b)