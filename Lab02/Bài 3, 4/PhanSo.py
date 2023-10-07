import math


class PhanSo:
    def __init__(self, tu:int, mau:int) -> None:
        if mau == 0:
            print("Mẫu số không thể bằng 0")
        self.tu = tu
        self.mau = mau

    def __str__(self):
        return (f"{self.tu}/{self.mau}")

    @staticmethod
    def ucln(tu, mau):
        while (mau):
            tu, mau = mau, tu % mau
        return tu

    def RutGon(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu = self.tu/ucln
        self.mau = self.mau/ucln

    def __add__(self, other):
        if not isinstance(other, PhanSo):
            other = PhanSo(other)

        tuSo = self.tu * other.mau + other.tu * self.mau
        mauSo = self.mau * other.mau
        return PhanSo(tuSo, mauSo).RutGon()
    
    def __sub__(self, other):
        if not isinstance(other, PhanSo):
            other = PhanSo(other)
            
        tuSo = self.tu * other.mau - other.tu * self.mau
        mauSo = self.mau * other.mau
        return PhanSo(tuSo, mauSo).RutGon()

    def __mul__(self, other):
        if not isinstance(other, PhanSo):
            other = PhanSo(other)
            
        tuSo = self.tu * other.tu
        mauSo = self.mau * other.mau
        return PhanSo(tuSo, mauSo).RutGon()

    def __truediv__(self, other):
        if not isinstance(other, PhanSo):
            other = PhanSo(other)
            
        tuSo = self.tu * other.mau
        mauSo = self.mau * other.tu
        return PhanSo(tuSo, mauSo).RutGon()

    def soSanh(self, other):
        if not isinstance(other, PhanSo):
            other = PhanSo(other)

        if(self.tu * other.mau > self.mau * other.tu):
            return 1
        elif (self.tu * other.mau == self.mau * other.tu):
            return 0
        else:
            return -1

    def la_ps_Am(self):
        return self.tu * self.mau < 0

      
