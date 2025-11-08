import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('args', nargs='*', help='Arguments to print')
    args = parser.parse_args()

    if not args.args:
        print("no args")
    else:
        for arg in args.args:
            print(arg)

if __name__ == "__main__":
    main()