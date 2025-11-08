import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sort', action='store_true', help='Sort by key')
    args, unknown = parser.parse_known_args()

    pairs = []
    for arg in unknown:
        if '=' in arg:
            key, value = arg.split('=', 1)
            pairs.append((key, value))

    if args.sort:
        pairs.sort(key=lambda x: x[0])

    for key, value in pairs:
        print(f"Key: {key} Value: {value}")

if __name__ == "__main__":
    main()