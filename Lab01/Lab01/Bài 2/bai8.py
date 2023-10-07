print("CÁCH 1")
import math

a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))

delta = b*b - 4*a*c

if delta < 0:
    print("Phương trình vô nghiệm.")
elif delta == 0:
    nghKep = -b/(2*a)
    print(f"Phương trình có một nghiệm kép x1 = x2 = {nghKep}")
else:
    x2 = (-b + math.sqrt(delta))/(2*a)
    x1 = (-b - math.sqrt(delta))/(2*a)
    print(f"Phương trình có hai nghiệm x1= {x1}, x2= {x2}")