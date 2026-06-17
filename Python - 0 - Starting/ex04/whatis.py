import sys


def str_is_number(num: str) -> bool:
    try:
        int(num)
        return True
    except ValueError:
        return False


try:
    if len(sys.argv) != 2:

        if (len(sys.argv) > 2):
            raise AssertionError("More than one argument is provided")
        else:
            sys.exit(0)

    else:

        if str_is_number(sys.argv[1]):

            num = int(sys.argv[1])
            if num % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
            sys.exit(0)
        else:
            raise AssertionError("Argument is not an integer")

except AssertionError as error:
    print(AssertionError.__name__ + ":", error)
    sys.exit(1)
