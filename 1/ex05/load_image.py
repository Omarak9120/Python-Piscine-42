import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def ft_load(path: str) -> np.ndarray:
    """
    Loads an image, prints its shape, and returns it as a NumPy array.

    Args:
        path (str): Path to the image file.

    Returns:
        np.ndarray: NumPy array representing the image.

    Handles errors related to incorrect file paths and formats.
    """
    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")

        img = Image.open(path)
        img_array = np.array(img)

        print(f"The shape of image is: {img_array.shape}")
        print(img_array)

        display_image(img_array, "Figure VIII.1: Original")

        return img_array

    except FileNotFoundError:
        print("\033[31mError: File not found.\033[0m")
    except AssertionError as error:
        print("\033[31mAssertionError:", error, "\033[0m")
    except Exception as error:
        print("\033[31mUnexpected Error:", error, "\033[0m")

    return np.array([])


def display_image(image: np.ndarray, title: str):
    """
    Displays an image using Matplotlib with a given title.

    Args:
        image (np.ndarray): Image as a NumPy array.
        title (str): Title for the window.
    """
    plt.figure(title)
    plt.imshow(image)
    plt.title(title)
    plt.axis("off")
    plt.show()
