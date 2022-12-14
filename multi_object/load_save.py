from student import SinhVien
import pickle
import os


def save_data(data: list[SinhVien], path: str, file: str):
    try:
        with open(os.path.join(path, file), 'wb') as f:
            pickle.dump(data, f)
    except Exception as e:
        print('Saving failed')


def load_data(path: str, file: str) -> list[SinhVien]:
    try:
        with open(os.path.join(path, file), 'rb') as f:
            result = pickle.load(f)
        return result
    except Exception as e:
        return None


def read_line_by_line(data: list[SinhVien]):
    for item in data:
        print(item)