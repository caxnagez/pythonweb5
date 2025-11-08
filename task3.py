import os
from pathlib import Path

def get_dir_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for filename in filenames:
            filepath = Path(dirpath) / filename
            try:
                total_size += filepath.stat().st_size
            except (OSError, FileNotFoundError):
                pass
    return total_size

def get_top_dirs(path="."):
    dir_sizes = []
    for item in os.listdir(path):
        item_path = Path(path) / item
        if item_path.is_dir():
            size = get_dir_size(item_path)
            dir_sizes.append((size, item_path.name))
    top_dirs = sorted(dir_sizes, key=lambda x: x[0], reverse=True)[:10]
    for size, name in top_dirs:
        readable_size = bytes_to_human_readable(size)
        print(f"{name} - {readable_size}")

def bytes_to_human_readable(size_bytes):
    if size_bytes == 0:
        return "0Б"
    size_names = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    return f"{round(size_bytes)}{size_names[i]}"

if __name__ == "__main__":
    import sys
    target_path = sys.argv[1] if len(sys.argv) > 1 else "."
    get_top_dirs(target_path)