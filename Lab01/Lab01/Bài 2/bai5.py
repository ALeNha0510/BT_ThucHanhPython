def Dequy_Fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    else:
        return Dequy_Fibonacci(n-1) + Dequy_Fibonacci(n-2)
    
num = int(input("Nhập số n: "))
if num < 0:
    print("Số n phải là số nguyên dương")
else:
    xuat = Dequy_Fibonacci(num)
    print(f"Số Fibonacci thứ {num} là: {xuat}.")