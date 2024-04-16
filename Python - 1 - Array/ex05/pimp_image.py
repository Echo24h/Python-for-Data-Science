import numpy as np
from PIL import Image


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Invert an image.

    Args:
        array (array): The image as an array.

    Returns:
        array: The inverted image as an array.
    """
    try:
        if not isinstance(array, np.ndarray):
            raise TypeError("The array must be an array.")
        if not array.size:
            raise ValueError("The array must not be empty.")

        inverted_array = 255 - array

        image = Image.fromarray(inverted_array)

        image.show()

        image.save("inverted.jpg")

        return inverted_array

    except Exception as error:
        print(type(error).__name__ + ":", error)
        exit(1)


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Get the red channel of an image.

    Args:
        array (array): The image as an array.

    Returns:
        array: The red channel of the image as an array.
    """
    try:
        if not isinstance(array, np.ndarray):
            raise TypeError("The array must be an array.")
        if not array.size:
            raise ValueError("The array must not be empty.")

        red_array = array.copy()
        red_array[:, :, 1] = 0
        red_array[:, :, 2] = 0

        image = Image.fromarray(red_array)

        image.show()

        image.save("red.jpg")

        return red_array

    except Exception as error:
        print(type(error).__name__ + ":", error)
        exit(1)


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Get the green channel of an image.

    Args:
        array (array): The image as an array.

    Returns:
        array: The green channel of the image as an array.
    """
    try:
        if not isinstance(array, np.ndarray):
            raise TypeError("The array must be an array.")
        if not array.size:
            raise ValueError("The array must not be empty.")

        green_array = array.copy()
        green_array[:, :, 0] = 0
        green_array[:, :, 2] = 0

        image = Image.fromarray(green_array)

        image.show()

        image.save("green.jpg")

        return green_array

    except Exception as error:
        print(type(error).__name__ + ":", error)
        exit(1)


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Get the blue channel of an image.

    Args:
        array (array): The image as an array.

    Returns:
        array: The blue channel of the image as an array.
    """
    try:
        if not isinstance(array, np.ndarray):
            raise TypeError("The array must be an array.")
        if not array.size:
            raise ValueError("The array must not be empty.")

        blue_array = array.copy()
        blue_array[:, :, 0] = 0
        blue_array[:, :, 1] = 0

        image = Image.fromarray(blue_array)

        image.show()

        image.save("blue.jpg")

        return blue_array

    except Exception as error:
        print(type(error).__name__ + ":", error)
        exit(1)


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Convert an image to greyscale.

    Args:
        array (array): The image as an array.

    Returns:
        array: The greyscale image as an array.
    """
    try:
        if not isinstance(array, np.ndarray):
            raise TypeError("The array must be an array.")
        if not array.size:
            raise ValueError("The array must not be empty.")

        grey_array = np.dot(array[..., :3], [0.2989, 0.5870, 0.1140])

        image = Image.fromarray(grey_array.astype(np.uint8))

        image.show()

        image.save("grey.jpg")

        return grey_array

    except Exception as error:
        print(type(error).__name__ + ":", error)
        exit(1)


if __name__ == "__main__":
    ft_blue(np.array(Image.open("landscape.jpg")))
    ft_green(np.array(Image.open("landscape.jpg")))
    ft_grey(np.array(Image.open("landscape.jpg")))
    ft_invert(np.array(Image.open("landscape.jpg")))
    ft_red(np.array(Image.open("landscape.jpg")))
