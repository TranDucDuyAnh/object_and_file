from load_save import *


sv = SinhVien('Lê Anh Duy', 2004, 10)


path = 'D:/data'
file = 'single_student.dat'


def main():
    save_data(sv, path, file)
    result = load_data(path, file)
    print(result)
    print('Ended')


if __name__ == '__main__':
    main()
