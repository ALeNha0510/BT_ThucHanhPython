def ChuyenGPG(giay):
    gio = giay // 3600  # Số giờ trong số giây
    phut = (giay % 3600) // 60  # Số phút trong số giây còn lại sau khi đã tính giờ
    giay = giay % 60  # Số giây còn lại sau khi đã tính giờ và phút
    return gio, phut, giay

nhapgiay = int(input("Nhập số giây: "))
gio, phut, giay = ChuyenGPG(nhapgiay)
print(f"Bây giờ là: {gio:02d}:{phut:02d}:{giay:02d}")