def TamGiacDuoi(hang):
    for i in range( 1, hang + 1):
        for j in range(hang - i + 1, 1):
            print(" ", end="")
        for k in range(1, i + 1):
            print("*", end="")
        print()

hang = int(input("Nhập số hàng: "))
TamGiacDuoi(hang)