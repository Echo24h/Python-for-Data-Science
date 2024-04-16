import numpy as np
from PIL import Image
from load_image import ft_load


def ft_zoom(image: np.ndarray, X: int, Y: int, size: int) -> np.ndarray:
    """
    Zoom an image.

    Args:
        image (array): The image as an array.
        X (int): The X coordinate.
        Y (int): The Y coordinate.
        size (int): The size of the zoom.

    Returns:
        array: The zoomed image as an array.
    """
    try:
        if not isinstance(image, np.ndarray):
            raise TypeError("The image must be an array.")
        if not isinstance(X, int):
            raise TypeError("The X must be an integer.")
        if not isinstance(Y, int):
            raise TypeError("The Y must be an integer.")
        if not isinstance(size, int):
            raise TypeError("The size must be an integer.")
        if X < 0 or X >= image.shape[0]:
            raise ValueError("The X must be positive and less\
 than the image's width.")
        if Y < 0 or Y >= image.shape[1]:
            raise ValueError("The Y must be positive and less\
 than the image's height.")
        if X + size > image.shape[0]:
            raise ValueError("The X + size must be less than\
 the image's width.")
        if Y + size > image.shape[1]:
            raise ValueError("The Y + size must be less than\
 the image's height.")

        zoomed_image = image[X:X+size, Y:Y+size]

        return zoomed_image

    except Exception as error:
        print(type(error).__name__ + ":", error)
        exit(1)


def ft_rotate(image: np.ndarray) -> np.ndarray:
    """
    Rotate an image.

    Args:
        image (array): The image as an array.

    Returns:
        array: The rotated image as an array.
    """
    try:
        if not isinstance(image, np.ndarray):
            raise TypeError("The image must be an array.")

        # rotated_image = np.rot90(image, 1)

        rotated_image = np.zeros_like(image)

        for i in range(image.shape[1]):
            for j in range(image.shape[0]):
                rotated_image[j, i] = image[i, j]

        return rotated_image

    except Exception as error:
        print(type(error).__name__ + ":", error)
        exit(1)


if __name__ == "__main__":

    image = ft_load("animal.jpeg")
    new_image = ft_zoom(image, 100, 450, 400)

    new_image = Image.fromarray(new_image)
    new_image = new_image.convert("L")
    new_image.save("new_image.jpg")
    new_image_arr = ft_load("new_image.jpg")

    print("The shape of image is: " + str(new_image_arr.shape))
    print(new_image_arr)

    new_image_arr = ft_rotate(new_image_arr)

    print("New shape after Transpose: " + str(new_image_arr.shape))
    print(new_image_arr)

    new_image_arr = new_image_arr.astype(np.uint8)

    new_image = Image.fromarray(new_image_arr)
    new_image.save("new_image.jpg")
    new_image.show()
