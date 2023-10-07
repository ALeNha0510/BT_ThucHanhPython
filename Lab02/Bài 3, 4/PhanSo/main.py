from phan_so import PhanSo
from ds_phan_so import DanhSachPhanSo

ds = DanhSachPhanSo()
ds.docTuFile("du_lieu.txt")
print("Danh sách phân số đọc từ tập tin: ")
ds.xuat()


print("*"*50)
print("Danh sách phân số âm: ")
kq = ds.layDsPsAm()
kq.xuat()

print("*"*50)
print("Danh sách phân số dương nhỏ nhất - Cách 1: ")
ps = ds.timDSPhanSoDuongNhoNhat()
ps.xuat()
print("Danh sách phân số dương nhỏ nhất - Cách 2: ")
ps = ds.timDSPhanSoDuongNhoNhat_C2()
ps.xuat()
#ps = ds.timPsDuongNhoNhatDungMin() # chỉ trả về 1 phân số
#print(ps)

print("*"*50)
print("Số lượng phân số âm của danh sách là: ", ds.demPhanSoAm())
print("Số lượng phân số âm của danh sách là: ", ds.demPhanSoAmSS())

print("*"*50)
print("Tổng các phân số âm trong danh sách là: ", ds.tinhTongPsAm())

x = PhanSo(5,6)
ds.xoaPhanSoDungIn(x)
print(f"Danh sách phân số sau khi xóa phân số {x}: ")
ds.xuat()

ds.xoaPhanSo(PhanSo(2/5))
ds.xuat()

print("*"*50)
print("Danh sách phân số đọc từ tập tin: ")
ds.xuat()
print("Danh sách phân số sau khi sắp xếp tăng theo mẫu: ")
#ds.sapXepTangTheoMauDoiChoTT()
ds.sapXepTangTheoMauChonTT()
ds.xuat()
