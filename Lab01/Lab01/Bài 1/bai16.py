print("CÁCH 1")
def SoSanh(n):
    if n <= 17:
        return abs(17 - n)
    else:
        return (n - 17)*2

nhap = int(input("Nhập n: "))
print(SoSanh(nhap))

print("CÁCH 2")

n = int(input("Nhập n: "))
print(abs(17 - n)) if n < 17 else print((n - 17)*2)