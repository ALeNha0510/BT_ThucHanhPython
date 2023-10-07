def luythua(n):
    tim_sqrt = int(n ** 0.5)
    return tim_sqrt * tim_sqrt == n

def TimSoFibonacci(num):
    if num < 0:
        return False
    if num == 0 or num == 1:
        return True
    return luythua(5 * num * num + 4) or luythua(5 * num * num - 4)

nhap = int(input("Nhập số nguyên cần tìm: "))
if TimSoFibonacci(nhap):
    print(f"{nhap} là số Fibonacci.")
else:
    print(f"{nhap} không phải là số Fibonacci.")
