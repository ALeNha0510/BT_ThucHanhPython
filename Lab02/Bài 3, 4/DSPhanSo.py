from PhanSo import PhanSo
import math

class DSPhanSo:
    def __init__(self, danh_sach = []) -> None:
        self.DSPhanSo = list(danh_sach)

    def ThemPS(self, ps: PhanSo):
        self.DSPhanSo.append(ps)

    def Xuat(self):
        for ps in self.DSPhanSo:
            print(ps, end = "\t")
        print()

    def DocTuFile(self, tenfile):
        with open(tenfile, 'r', encoding='utf-8') as file:
            for line in file:
                item = line.split('/')
                self.ThemPS(PhanSo(int(item[0]), int(item[1])))

    #Đếm ps âm
    def dem_ps_am(self):
        return sum(1 for ps in self.DSPhanSo if ps.la_ps_Am())
    
    #Đếm ps âm cách 2
    def dem_ps_am2(self):
        dem = 0
        for ps in self.DSPhanSo:
            if ps.la_ps_Am():
                dem += 1
        return dem

    #Tính tổng ps âm
    def tong_ps_Am(self):
        tong = PhanSo()
        for ps in self.DSPhanSo:
            if ps.tu * ps.mau:
                tong += ps
        return tong
