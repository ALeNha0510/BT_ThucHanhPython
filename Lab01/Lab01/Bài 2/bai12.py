day = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,6]

def XuatCacSoLeKoChiaHetCho5(so: int):
    return (so % 2 != 0 and so % 5 != 0)
    
day_moi = list(filter(XuatCacSoLeKoChiaHetCho5, day))
print("Các số lẻ ko chi hết cho 5 là: ", day_moi)
#=========================================================
def KTrFibonacci(n):
    if n == 0:
        return True
    a, b = 0, 1
    while b <= n:
        if b == n:
            return True
        a, b = b, a + b
    return False

day_Fibo = list(filter(KTrFibonacci, day))
print("Các số Fibonacci là: ", day_Fibo)
#=========================================================
import math
def KTraNgTo(so):
   if so == 1:
       return False       

   for i in range(2, int(math.sqrt(so))+1):
       if so % i == 0:
           return False
   return True

def TimSoNgToMax(so):
    max = 0
    for i in so:
        if KTraNgTo(i):
            if max == 0 or i > max:
                max = i
    return max

SoNgto_Max = TimSoNgToMax(day)
if SoNgto_Max > 0:
    print("Số nguyên tố lớn nhất là: ", SoNgto_Max)
else:
    print("Không có số nguyên tố trong dãy!!!")
#========================================================
def luythua(n):
    tim_sqrt = int(n ** 0.5)
    return tim_sqrt * tim_sqrt == n

def TimSoFibonacci(num):
    if num < 0:
        return False
    if num == 0 or num == 1:
        return True
    return luythua(5 * num * num + 4) or luythua(5 * num * num - 4)

def TimFibo_Min(n):
    min = 0
    for i in n:
        if TimSoFibonacci(i):
            if min == 0 or i < min:
                min = i
    return min

fibo_min = TimFibo_Min(day)

if fibo_min > 0:
    print("Số Fibonacci nhỏ nhất trong mảng:", fibo_min)
else:
    print("Không có số Fibonacci trong mảng.")
#=========================================================
def TinhTB_SoLe(mang):
    soLe = [i for i in mang if i % 2 != 0]
    if not soLe:
        return 0
    
    tong = sum(soLe)
    count = len(soLe)
    
    tb = tong / count
    return tb

tb_soLe = TinhTB_SoLe(day)
print("Trung bình các số lẻ trong dãy:", tb_soLe)
#============================================================
def HoanVi(mang, so1, so2):
    mang[so1], mang[so2] = mang[so2], mang[so1]

print("Mảng trước khi đổi chỗ:", day)

so1 = int(input("Nhập vị trí thứ nhất: "))
so2 = int(input("Nhập vị trí thứ hai: "))

HoanVi(day, so1, so2)

print("Mảng sau khi đổi chỗ:", day)
#=========================================================
def DaoNguocday(day):
    return day[::-1]

print("Mảng ban đầu:", day)

day_nguoc = DaoNguocday(day)

print("Mảng sau khi đảo ngược:", day_nguoc)
#==========================================================
def SoLon_ThuNhi(day):
    if len(day) < 2:
        return None
    
    lonNhat = max(day[0], day[1])
    lonNhi = min(day[0], day[1])
    
    for i in day[2:]:
        if i > lonNhat:
            lonNhi = lonNhat
            lonNhat = i
        elif i > lonNhi and i != lonNhat:
            lonNhi = i
    
    return lonNhi

kq = SoLon_ThuNhi(day)
print("Số lớn thứ nhì trong mảng là:", kq)
#==================================================
from collections import Counter

def So_XuatHien_Nhieu(day):
    dem = Counter(day)
    nhieunhat = max(dem.values())
    xuathien_nhieu = [i for i, count in dem.items() if count == nhieunhat]
    return xuathien_nhieu

day_co_so_xuathien_nhieu = So_XuatHien_Nhieu(day)
print("Số xuất hiện nhiều nhất trong mảng là: ", day_co_so_xuathien_nhieu)

