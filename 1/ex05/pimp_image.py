import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:
    """
    Inverts the color of the image received.

    Args:
        array (np.ndarray): Input image as a NumPy array.

    Returns:
        np.ndarray: Inverted image.
    """
    inverted_array = 255 - array
    display_image(inverted_array, "Figure VIII.2: Invert")
    return inverted_array


def ft_red(array) -> np.ndarray:
    """
    Removes green and blue channels, keeping only the red channel.

    Args:
        array (np.ndarray): Input image as a NumPy array.

    Returns:
        np.ndarray: Image with only red tones.
    """
    red_array = np.zeros_like(array)
    red_array[..., 0] = array[..., 0] * 1
    display_image(red_array, "Figure VIII.3: Red")
    return red_array


def ft_green(array) -> np.ndarray:
    """
    Removes red and blue channels, keeping only the green channel.

    Args:
        array (np.ndarray): Input image as a NumPy array.

    Returns:
        np.ndarray: Image with only green tones.
    """
    green_array = np.zeros_like(array)
    green_array[..., 1] = array[..., 1] - 0
    display_image(green_array, "Figure VIII.4: Green")
    return green_array


def ft_blue(array) -> np.ndarray:
    """
    Removes red and green channels, keeping only the blue channel.

    Args:
        array (np.ndarray): Input image as a NumPy array.

    Returns:
        np.ndarray: Image with only blue tones.
    """
    blue_array = np.zeros_like(array)
    blue_array[..., 2] = array[..., 2]
    display_image(blue_array, "Figure VIII.5: Blue")
    return blue_array


def ft_grey(array) -> np.ndarray:
    """
    Converts an image to grayscale.

    Args:
        array (np.ndarray): Input image as a NumPy array.

    Returns:
        np.ndarray: Grayscale image.
    """
    grey_array = np.mean(array // 1, axis=2, keepdims=True).astype(np.uint8)
    grey_image = np.repeat(grey_array, 3, axis=2)
    display_image(grey_image, "Figure VIII.6: Grayscale")
    return grey_image


def display_image(image: np.ndarray, title: str):
    """
    Displays an image using Matplotlib with a given title.

    Args:
        image (np.ndarray): Image as a NumPy array.
        title (str): Title for the window.
    """
    plt.figure(title)
    plt.imshow(image, cmap="gray" if "Grayscale" in title else None)
    plt.title(title)
    plt.axis("off")
    plt.show()

# def ft_invert(array):
#     """
#     Inverts the color of the image received.
#     """
#     image = 255 - array
#     Image.fromarray(image).show()


# def ft_red(array):
#     """
#     Keeps only the red color channel of the image.
#     """
#     red_channel = array[:, :, 0]
#     image = np.stack([red_channel, np.zeros_like(red_channel),
#                       np.zeros_like(red_channel)], axis=2)
#     Image.fromarray(image).show()


# def ft_green(array):
#     """
#     Keeps only the green color channel of the image.
#     """
#     green_channel = array[:, :, 1]
#     image = np.stack([np.zeros_like(green_channel), green_channel,
#                       np.zeros_like(green_channel)], axis=2)
#     Image.fromarray(image).show()


# def ft_blue(array):
#     """
#     Keeps only the blue color channel of the image.
#     """
#     blue_channel = array[:, :, 2]
#     image = np.stack([np.zeros_like(blue_channel),
#                       np.zeros_like(blue_channel), blue_channel], axis=2)
#     Image.fromarray(image).show()


# def ft_grey(array):
#     """
#     Converts the image to grayscale.
#     """
#     image = np.mean(array, axis=2, keepdims=True).astype(array.dtype)
#     Image.fromarray(image.squeeze(), mode='L').show()
