class SinhVien:
    def __init__(self, fullname: str, year: int, avgscore: float):
        self.hoten = fullname
        self.namsinh = year
        self.dtb = avgscore

    def __str__(self) -> str:
        message = 'Họ tên: ' + self.hoten \
                  + ' | Năm sinh: ' + str(self.namsinh) \
                  + ' | Điểm trung bình: ' + str(self.dtb)
        return message

    def __gt__(self, other):
        return self.dtb > other.dtb

    def __ge__(self, other):
        return self.dtb >= other.dtb

    def __lt__(self, other):
        return self.dtb < other.dtb

    def __le__(self, other):
        return self.dtb <= other.dtb

    def __eq__(self, other):
        return self.dtb == other.dtb
