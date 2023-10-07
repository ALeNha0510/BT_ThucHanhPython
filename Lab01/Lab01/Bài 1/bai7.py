str = input("Nhập định dạng file cần lưu: ")
morong = str.split(".")

print("Phần mở rộng tệp có định dạng là: ", repr(morong[-1]))