from PhanSo import PhanSo
from DSPhanSo import DSPhanSo


ds = DSPhanSo()
ds.DocTuFile("D:\\Trường Đại Học Đà Lạt\\Trường Đại Học Đà Lạt\\Lập Trình Python\\Bài Tập Thực Hành\\Lab02\\Bài 3, 4\\dulieu.txt")
print("Danh sách phân số: ")
ds.Xuat()



#Xuất ds phân số âm
ps_Am = ds.dem_ps_am()
print(f"Số phân số âm trong danh sách là: {ps_Am}")

#Xuất ds ps âm cách2
print("ps âm trong mảng là: ", ds.dem_ps_am2())

#Tổng các ps âm
tong_ps_Am = ds.tong_ps_Am()
print(f"Tổng các phân số âm là: {tong_ps_Am}")