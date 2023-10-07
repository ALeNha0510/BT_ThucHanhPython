import math
from pathlib import Path
from phan_so import PhanSo

class DanhSachPhanSo:
    def __init__(self, danh_sach = []) -> None:
        self.ds_phan_so = list(danh_sach)

    def them(self, ps: PhanSo):
        self.ds_phan_so.append(ps)

    def xuat(self):
        for ps in self.ds_phan_so:
            print(ps, end='\t')
        print()

    def docTuFile(self, tenfile):
        base_path = Path(__file__).parent
        file_path = (base_path / tenfile).resolve()
        with open(file_path, 'r', encoding='utf-8') as f:
            for hang in f:
                du_lieu = hang.split('/')
                self.them(PhanSo(int(du_lieu[0]), int(du_lieu[1])))
    
    # đếm phân số âm trong danh sách - cách 1
    def demPhanSoAm(self):
        dem = 0
        for ps in self.ds_phan_so:
            if ps.laPhanSoAm():
                dem += 1 
        return dem
    
    # đếm phân số âm trong danh sách - cách 2
    def demPhanSoAmSS(self):
        dem = 0
        for ps in self.ds_phan_so:
            # chỉ so sánh được nếu có hàm ghi đè toán tử "<"
            if ps < 0: 
                dem += 1 
        return dem

    # tìm giá trị phân số dương nhỏ nhất
    def timGiaTriPsDuongNhoNhat(self):
        gt_nho_nhat = 1_000_000_000
        for ps in self.ds_phan_so:
            x = ps.tinhGiaTri()
            if x > 0 and x < gt_nho_nhat:
                gt_nho_nhat = x
        return gt_nho_nhat
    
    # tìm danh sách phân số dương nhỏ nhất - cách 1
    def timDSPhanSoDuongNhoNhat(self):
        gt_nho_nhat = self.timGiaTriPsDuongNhoNhat()
        kq = DanhSachPhanSo()
        for ps in self.ds_phan_so:
            if math.isclose(ps.tinhGiaTri(),gt_nho_nhat):
                kq.them(ps)
        return kq
    
    # tìm danh sách phân số dương nhỏ nhất - cách 2
    def timDSPhanSoDuongNhoNhat_C2(self):
        gt_nho_nhat = self.timGiaTriPsDuongNhoNhat()
        return DanhSachPhanSo([ps for ps in self.ds_phan_so if ps.tinhGiaTri() == gt_nho_nhat])

    # tìm phân số dương nhỏ nhất -> trả về phân số dương nhỏ nhất đầu tiên
    def timPhanSoDuongNhoNhat(self):
        ps_nho_nhat = PhanSo(1_000_000)
        for ps in self.ds_phan_so:
            if ps > 0 and ps < ps_nho_nhat:
                ps_nho_nhat = ps
        return ps_nho_nhat

    # tìm phân số dương nhỏ nhất - dùng min --> chỉ trả về 1 phân số trong danh sách
    def timPsDuongNhoNhatDungMin(self):
        return min(self.ds_phan_so, key = lambda x: x > 0 == True)

    # lấy danh sách tất cả phân số âm
    def layDsPsAm(self):
        return DanhSachPhanSo([ps for ps in self.ds_phan_so if ps < 0])

    # tổng các phân số âm trong danh sách
    def tinhTongPsAm(self):
        tongAm = PhanSo()
        for ps in self.ds_phan_so:
            if ps < 0:
                tongAm += ps
        return tongAm
       

    # xóa phân số x trong mảng
    def xoaPhanSo(self, x: PhanSo):
        for ps in self.ds_phan_so:
            if ps == x:
                self.ds_phan_so.remove(ps) 

    # xóa phân số x trong mảng - cách 2
    def xoaPhanSoDungIn(self, x: PhanSo):
        while x in self.ds_phan_so:
            self.ds_phan_so.remove(x) 

    # sắp xếp danh sách phân số tăng theo mẫu
    def sapXepTangTheoMauChonTT(self):
        chieu_dai = len(self.ds_phan_so)
        
        for i in range(chieu_dai):
            vi_tri_min = i
            for j in range(i + 1, chieu_dai):
                if self.ds_phan_so[j].coMauNhoHon(self.ds_phan_so[vi_tri_min]):
                    vi_tri_min = j
            (self.ds_phan_so[i], self.ds_phan_so[vi_tri_min]) = (self.ds_phan_so[vi_tri_min], self.ds_phan_so[i])

    # sắp xếp danh sách phân số tăng theo mẫu
    def sapXepTangTheoMauDoiChoTT(self):
        chieu_dai = len(self.ds_phan_so)
        
        for i in range(chieu_dai):
            for j in range(i + 1, chieu_dai):
                if self.ds_phan_so[j].coMauNhoHon(self.ds_phan_so[i]):
                    (self.ds_phan_so[i], self.ds_phan_so[j]) = (self.ds_phan_so[j], self.ds_phan_so[i])
