#!/usr/bin/python3
if__name__ == "__main__":
    import sys
    result = 0
    for arg in sys.argv[1:]:
        result += int(arg)
        print("{}".format(result))
