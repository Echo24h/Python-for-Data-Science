import numpy as np
from PIL import Image
import os


def ft_load(path: str) -> np.ndarray:
    """
    Load an image.

    Args:
        path (str): The path to the image.

    Returns:
        array: The image as an array.
    """
    try:
        if not isinstance(path, str):
            raise TypeError("The path must be a string.")
        if not path:
            raise ValueError("The path must not be empty.")
        if not os.path.exists(path):
            raise FileNotFoundError(path)
        if not path.lower().endswith(".jpg") and not path.endswith(".jpeg"):
            raise AssertionError("The file must be a JPG or JPEG file.")

        image = Image.open(path)

        if image is None:
            raise AssertionError("Failed to load image.")

        image_arr = np.array(image)

        print("The shape of image is: " + str(image_arr.shape))
        return image_arr

    except Exception as error:
        print(type(error).__name__ + ":", error)
        exit(1)


if __name__ == "__main__":
    ft_load("landscape.jpg")
