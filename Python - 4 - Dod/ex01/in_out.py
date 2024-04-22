def square(x: int | float) -> int | float:
    """
    This function takes a number as an argument and returns the square of the number.

    Args:
        x (int): A number.
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    This function takes a number as an argument and returns the power of the number.

    Args:
        x (int): A number.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    This function takes a number and a function as arguments and returns a function that takes no arguments.

    The returned function will return the result of the function passed as an argument with the number passed as an argument.

    Args:
        x (int): A number.
        function (function): A function.

    Returns:
        object: A function.
    """
    def inner() -> float:
        nonlocal x
        x = function(x)
        return x

    return inner


if __name__ == "__main__":
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())