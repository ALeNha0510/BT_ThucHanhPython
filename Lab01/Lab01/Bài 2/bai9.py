#CÁCH 1
import math

n = int(input("Nhập n: "))
print(f"{n}! = {math.factorial(n)}")

#CÁCH 2
def GiaiThua(n):
    if n==0 or n==1:
        return 1
    else:
        return n * GiaiThua(n-1)

n = int(input("Nhập n: "))
print(f"{n}! = {GiaiThua(n)}")