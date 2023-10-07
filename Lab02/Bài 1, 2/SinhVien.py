from datetime import datetime

class SinhVien:
    truong = "Đại học Đà Lạt"

    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maSo = maSo
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh

    @property    #Tương tự thuộc tính public giúp thuộc tính này truy cập được bên ngoài: maSo, hoTen
    def maSo(self):
        return self.__maSo
    
    @property
    def hoTen(self):
        return self.__hoTen

    @property
    def ngaySinh(self):
        return self.__ngaySinh

    @maSo.setter
    def maSo(self, maSo):
        if self.laMaSoHopLe(maSo):
            self.__maSo = maSo

    @staticmethod
    def laMaSoHopLe(maSo: int):
        return len(str(maSo)) == 7

    @classmethod
    def doiTenTruong(cls, tenmoi):  # Thay self bằng cls
        cls.truong = tenmoi

    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t\t{self.__ngaySinh}"

    def Xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t\t{self.__ngaySinh}")
    
    

class DanhSachSV:
    def __init__(self) -> None:
        self.dssv = []

    def themSV(self, sv: SinhVien):
        self.dssv.append(sv)

    def Xuat(self):
        for sv in self.dssv:
            print(sv)
    
    def nhapSV(self):
        while True:
            mssv = int(input("Nhập MSSV: "))
            if SinhVien.laMaSoHopLe(mssv):
                break
            else:
                print("MSSV không hợp lệ. Vui lòng nhập lại.")
        ten = input("Nhập tên: ")

        ngay = int(input("Nhập ngày sinh: "))
        thang = int(input("Nhập tháng sinh: "))
        nam = int(input("Nhập năm sinh: "))
        ngaysinh = datetime(nam, thang, ngay)
        return SinhVien(mssv, ten, ngaysinh)

    def timSvTheoMssv(self, mssv: int):
        return [sv for sv in self.dssv if sv.maSo == mssv]
    
    def timSvTheoTen(self, ten: str):
        return [sv for sv in self.dssv if sv.hoTen == ten]

    def timVTSvTheoMssv(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == mssv:
                return i
        return -1

    def xoaSvTheoMssv(self, maSo: int) -> bool:
        vt = self.timVTSvTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False

    def timSvSinhTruocNgay(self, ngay: datetime):
        return [sv for sv in self.dssv if sv.ngaySinh <= ngay]

    def docTuFile(self, ten_file):
        with open(ten_file, 'r', encoding='utf-8') as file:
            for line in file:
                mssv, ten, ngay_sinh_str = line.strip().split(',')
                ngay_sinh = datetime.strptime(ngay_sinh_str, '%d/%m/%Y')
                sv = SinhVien(int(mssv), ten, ngay_sinh)
                self.themSV(sv)

def main():
    danh_sach = DanhSachSV()

    sv1 = SinhVien(1234567, "Nguyen Van A", datetime(2000, 1, 1))
    sv2 = SinhVien(7654321, "Tran Thi B", datetime(1999, 5, 10))
    sv3 = SinhVien(2115244, "Thanh Nhã", datetime(2002, 10, 5))
    sv4 = SinhVien(2111868, "Phan Thị Cheese", datetime(1980, 9, 12))

    danh_sach.themSV(sv1)
    danh_sach.themSV(sv2)
    danh_sach.themSV(sv3)
    danh_sach.themSV(sv4)

    danh_sach.Xuat()
    

    sv = danh_sach.nhapSV()
    danh_sach.themSV(sv)
    danh_sach.Xuat()

    print("1. Tìm sv theo mssv")
    ma = int(input("Nhập MSSV: "))
    kq = danh_sach.timSvTheoMssv(ma)

    if kq:
        print(f"Sinh viên có MSSV {ma} là: ")
        for sv in kq:
            print(sv)
    else:
        print(f"Không tìm thấy sinh viên có MSSV {ma}")
    
    print("2. Tìm sv theo tên")
    ten = input("Nhập tên: ")
    kq = danh_sach.timSvTheoTen(ten)

    if kq:
        print(f"Sinh viên có tên {ten} trong danh sách là:")
        for sv in kq:
            print(sv)
    else:
        print(f"Không tìm thấy sinh viên có tên: {ten}")

    print("3. Xóa sinh viên theo MSSV")
    ma = int(input("Nhập MSSV: "))
    if danh_sach.xoaSvTheoMssv(ma):
        print(f"Xóa sinh viên MSSV {ma}")
        danh_sach.Xuat()
    else:
        print(f"Không tìm thấy sinh viên có MSSV {ma} để xóa")
    
    print("4. Tìm sinh viên sinh trước ngày")
    ngay = datetime(2000, 1, 1)
    kq = danh_sach.timSvSinhTruocNgay(ngay)

    if kq:
        print(f"Sinh viên sinh trước ngày {ngay.strftime('%d/%m/%Y')}:")
        for sv in kq:
            print(sv)
    else:
        print(f"Không có sinh viên nào sinh trước ngày {ngay.strftime('%d/%m/%Y')}")
    
    print("5. Tìm vị trí sinh viên theo MSSV")
    masv = int(input("Nhập MSSV: "))
    vt = danh_sach.timVTSvTheoMssv(masv)

    if vt != -1:
        print(f"Sinh viên có MSSV {masv} tại vị trí {vt + 1}")
    else:
        print(f"Không tìm thấy sinh viên với MSSV {masv}")


main()