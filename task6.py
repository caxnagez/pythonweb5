import sys

def parse_args():
    args = sys.argv[1:]
    sort_flag = False
    if '--sort' in args:
        sort_flag = True
        args.remove('--sort')

    pairs = []
    for arg in args:
        if '=' in arg:
            key, value = arg.split('=', 1)
            pairs.append((key, value))
        else:
            continue

    if sort_flag:
        pairs.sort(key=lambda x: x[0])

    for key, value in pairs:
        print(f"Key: {key} Value: {value}")

if __name__ == "__main__":
    parse_args()