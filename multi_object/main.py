from load_save import *


sv = [SinhVien('Lê Anh Duy', 2004, 10),
    SinhVien('Hồ Tăng Nhật Hiếu', 2005, 11),
    SinhVien('Phan Bá Hùng', 2004, 8),
    SinhVien('Phạm Nhật Huy', 2004, 7),
    SinhVien('Nguyễn Lê Duy Khang', 2005, 9),
    SinhVien('Hoàng Nhật Minh', 2005, 8.5)]


path = 'D:/data'
file = 'mul_student.dat'


def main():
    save_data(sv, path, file)
    result = load_data(path, file)
    read_line_by_line(result)
    print('Ended')


if __name__ == '__main__':
    main()
