import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('numbers', nargs='*', type=int)

    try:
        args = parser.parse_args()
        nums = args.numbers

        if len(nums) == 0:
            print("NO PARAMS")
        elif len(nums) == 1:
            print("TOO FEW PARAMS")
        elif len(nums) == 2:
            print(nums[0] + nums[1])
        else:
            print("TOO MANY PARAMS")
    except SystemExit:
        pass
    except Exception as e:
        print(type(e).__name__)

if __name__ == "__main__":
    main()