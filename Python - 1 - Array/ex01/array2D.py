import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D list.

    Args:
        family (list): A 2D list.
        start (int): The start index.
        end (int): The end index.

    Returns:
        list: The sliced 2D list.
    """
    try:

        if not isinstance(family, list):
            raise TypeError("The family must be a list.")
        if not isinstance(start, int):
            raise TypeError("The start must be an integer.")
        if not isinstance(end, int):
            raise TypeError("The end must be an integer.")
        for item in family:
            if len(item) != 2:
                raise ValueError("The family must be a 2D list.")

        family_arr = np.array(family)

        print("My shape is : " + str(family_arr.shape))
        sliced_family = family_arr[start:end]
        print("My new shape is : " + str(sliced_family.shape))

        return sliced_family.tolist()

    except Exception as error:
        print(type(error).__name__ + ":", error)
        exit(1)


if __name__ == "__main__":
    family = [
            [1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]
            ]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))
