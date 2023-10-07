def KTrFibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return KTrFibonacci(n-1) + KTrFibonacci(n-2)

num = int(input("Nhập số n: "))
tong = 0
for i in range(1, num + 1):
    tong += KTrFibonacci(i)
print(f"Tổng các số Fibonacci từ 1 - {num} là: {tong}")