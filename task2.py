import zipfile
import os
import sys

def bytes_to_human_readable(size_bytes):
    if size_bytes == 0:
        return "0Б"
    size_names = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    return f"{round(size_bytes)}{size_names[i]}"

def print_zip_structure(archive_path):
    try:
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            file_list = zip_ref.namelist()
            for file_path in file_list:
                level = file_path.count('/')
                indent = "  " * level
                if file_path.endswith('/'):
                    print(f"{indent}{file_path.rstrip('/')}")
                else:
                    info = zip_ref.getinfo(file_path)
                    size = bytes_to_human_readable(info.file_size)
                    print(f"{indent}{file_path.split('/')[-1]} {size}")
    except zipfile.BadZipFile:
        print(f"[ERROR] Файл {archive_path} не является ZIP-архивом или повреждён.")
        sys.exit(1)
    except FileNotFoundError:
        print(f"[ERROR] Файл {archive_path} не найден в текущей директории.")
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] Произошла ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    ARCHIVE_NAME = "trasher\d1.zip"
    print_zip_structure(ARCHIVE_NAME)