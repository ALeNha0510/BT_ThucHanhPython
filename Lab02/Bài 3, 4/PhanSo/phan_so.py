class PhanSo:
    def __init__(self, tu=1, mau=1):
        '''Nếu phân số có mẫu là số âm, chuyển dấu tử số để đảm bảo sự chính xác
        của các phép toán so sánh
           Nếu người dùng đưa vào giá trị mẫu số bằng 0 thì mẫu số được gán lại thành 1
        '''
        self.tu = tu if mau >= 0 else -tu
        self.mau = mau if mau > 0 else -mau if mau < 0 else 1

    def __str__(self) -> str:
        '''Khi hiển thị số nguyên ra màn hình nếu phân số có tử số chia hết cho mẫu số
         Ví dụ: 8/4 sẽ hiển thị là 2 '''
        return str(self.tu//self.mau) if self.tu % self.mau == 0 else "{}/{}".format(self.tu,self.mau)

    @staticmethod
    # Dùng @staticmethod để self không được truyền mặc định vào tham số của hàm
    def timUCLN(num1, num2):
        while (num2):
            num1, num2 = num2, num1 % num2
        return num1

    def rutGon(self):
        ucln = self.timUCLN(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln

    def tinhGiaTri(self):
        return self.tu/self.mau

    def laPhanSoAm(self):
        return self.tu * self.mau < 0

    def coMauNhoHon(self, other):
        return self.mau < other.mau

    def coMauNhoHonHoacBang(self, other):
        return self.mau <= other.mau

    def coTuNhoHon(self, other):
        return self.tu < other.tu

    def __add__(self, other):
        '''Cộng 2 phân số ps1 + ps2'''
        kq = PhanSo()
        if  not isinstance(other, PhanSo): 
            other = PhanSo(other)
        kq.tu = self.tu * other.mau + self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq

    def __sub__(self, other):
        '''Trừ 2 phân số ps1 - ps2'''
        kq = PhanSo()
        if  not isinstance(other, PhanSo): 
            other = PhanSo(other)
        kq.tu = self.tu * other.mau - self.mau * other.tu
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq

    def __mul__(self, other):
        '''Nhân 2 phân số ps1 * ps2'''
        kq = PhanSo()
        if  not isinstance(other, PhanSo): 
            other = PhanSo(other)
        kq.tu = self.tu *  other.tu
        kq.mau = self.mau * other.mau
        kq.rutGon()
        return kq

    def __truediv__(self, other):
        '''Chia 2 phân số ps1 / ps2'''
        kq = PhanSo()
        if  not isinstance(other, PhanSo): 
            other = PhanSo(other)
        kq.tu = self.tu *  other.mau
        kq.mau = self.mau * other.tu
        kq.rutGon()
        return kq
    def __eq__(self, other) -> bool:
        if  not isinstance(other, PhanSo): 
            other = PhanSo(other)
        if self.mau == other.mau:
            return self.tu == other.tu
        return self.tu * other.mau == self.mau * other.tu

    def __lt__(self, other):
        if  not isinstance(other, PhanSo): 
            other = PhanSo(other)
        if self.mau == other.mau:
            return self.tu < other.tu
        return self.tu * other.mau < self.mau * other.tu

    def __gt__(self, other):
        if  not isinstance(other, PhanSo): 
            other = PhanSo(other)
        if self.mau == other.mau:
            return self.tu > other.tu
        return self.tu * other.mau > self.mau * other.tu
    