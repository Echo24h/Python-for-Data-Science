import numpy as np


def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    """
    Calculate the BMI of a list of people.

    Args:
        height (list[int | float]): A list of heights in cm.
        weight (list[int | float]): A list of weights in kg.

    Returns:
        list[int | float]: A list of BMIs.
    """
    try:

        if (len(height) != len(weight)):
            raise ValueError("The length of lists must be the same.")

        for i in range(len(height)):
            if not isinstance(height[i], (int, float)):
                raise TypeError("The height and weight must be int or float.")
            if not isinstance(weight[i], (int, float)):
                raise TypeError("The height and weight must be int or float.")

        for i in range(len(height)):
            if height[i] <= 0 or weight[i] <= 0:
                raise ValueError("The height and weight must be positive.")

        height_arr = np.array(height)
        weight_arr = np.array(weight)

        bmi_arr = weight_arr / (height_arr ** 2)

        return bmi_arr.tolist()

    except Exception as error:
        print(type(error).__name__ + ":", error)
        exit(1)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to a list of BMIs.

    Args:
        bmi (list[int | float]): A list of BMIs.
        limit (int): The limit to apply.

    Returns:
        list[bool]: A list of booleans indicating whether the BMI
        is above the limit.
    """
    bmi_arr = np.array(bmi)

    above_limit = bmi_arr > limit

    return above_limit.tolist()


if __name__ == "__main__":
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
