def TongCanBac2(n):
    if n <= 0:
        return 0
    else:
        tong =0 
        for i in range(1, n+1):
            sqrt = i ** 0.5
            tong += sqrt
    return tong

nhap = int(input("Nhập số n: "))
kq = TongCanBac2(nhap)
print(f"Tổng căn bậc 2 của {nhap} số nguyên đầu tiên là: {kq}")