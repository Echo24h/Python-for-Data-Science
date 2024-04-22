def ft_statistics(*args: any, **kwargs: any) -> None:
    """This function takes any number of arguments and keyword arguments.
    It calculates the mean, median, quartile, standard deviation, and variance of the arguments.
    The function then prints the result of the calculation based on the keyword argument.

    Args:
        *args (any): Any number of arguments.
        **kwargs (any): Any number of keyword arguments.

    Returns:
        None: This function does not return anything."""
    for key, value in kwargs.items():
        if args == ():
            print("ERROR")
            continue
        if value in ["mean", "median", "quartile", "std", "var"]:
            if value == "mean":
                print(f"{value} : {sum(args)/len(args)}")
            elif value == "median":
                args = sorted(args)
                if len(args) % 2 == 0:
                    print(f"{value} : {(args[len(args)//2] + args[len(args)//2 - 1]) / 2}")
                else:
                    print(f"{value} : {args[len(args)//2]}")
            elif value == "quartile":
                args = sorted(args)
                if len(args) % 2 == 0:
                    q1 = args[len(args)//4]
                    q3 = args[len(args)//4*3]
                else:
                    q1 = args[len(args)//4]
                    q3 = args[len(args)//4*3]
                print(f"{value} : {[float(q1), float(q3)]}")
            elif value == "std":
                mean = sum(args)/len(args)
                std = (sum([(x - mean) ** 2 for x in args]) / len(args)) ** 0.5
                print(f"{value} : {std}")
            elif value == "var":
                mean = sum(args)/len(args)
                var = sum([(x - mean) ** 2 for x in args]) / len(args)
                print(f"{value} : {var}")


if __name__ == "__main__":
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")