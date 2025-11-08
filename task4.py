import os
import zipfile
from datetime import datetime

def make_reserve_arc(source, dest):
    if not os.path.isdir(source):
        raise ValueError("Source must be a directory")
    if not os.path.isdir(dest):
        raise ValueError("Destination must be a directory")

    arc_name = f"archive_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    arc_path = os.path.join(dest, arc_name)

    with zipfile.ZipFile(arc_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, source))

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python task4.py <source_dir> <dest_dir>")
        exit(1)
    make_reserve_arc(sys.argv[1], sys.argv[2])