import os

def bytes_to_human_readable(size_bytes):
    if size_bytes == 0:
        return "0Б"
    size_names = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    return f"{round(size_bytes)}{size_names[i]}"

def get_file_sizes():
    current_dir = os.getcwd()
    results = []
    for item in os.listdir(current_dir):
        path = os.path.join(current_dir, item)
        if os.path.isfile(path):
            size = os.path.getsize(path)
            readable_size = bytes_to_human_readable(size)
            results.append(f"{item} {readable_size}")
    return " ".join(results)

if __name__ == "__main__":
    print(get_file_sizes())