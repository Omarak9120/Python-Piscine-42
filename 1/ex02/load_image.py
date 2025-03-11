import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the specified path and return it as a NumPy array.

    Parameters:
    path (str): The path to the image file to be loaded.

    Returns:
    np.ndarray: A NumPy array representing the loaded image.

    Raises:
    AssertionError: If the image format is wrong or the file is not found.

    Loads an image from the given path and performs checks to ensure
    compatibility and validity. Only JPG and JPEG formats are supported.
If the file does not exist or the format is not supported, an error is raised.
    The image is then converted to a NumPy array and its shape is printed.
    """
    try:
        if not path.lower().endswith(("jpg", "jpeg")):
            raise AssertionError("Only JPG and JPEG formats are supported.")

        img = Image.open(path)
        img_array = np.array(img)

        print(f"The shape of image is: {img_array.shape}")

        return img_array

    except FileNotFoundError:
        print("\033[31mError: File not found.\033[0m")
    except AssertionError as error:
        print("\033[31mAssertionError:", error, "\033[0m")
    except Exception as error:
        print("\033[31mUnexpected Error:", error, "\033[0m")

    return np.array([])


if __name__ == "__main__":
    print(ft_load("landscape.jpg"))
