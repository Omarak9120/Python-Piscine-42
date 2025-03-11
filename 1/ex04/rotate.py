import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom_image(
        image: np.ndarray, center_x: int, center_y: int, size: int
) -> np.ndarray:
    """
    Extracts a zoomed-in section from the image.

    Args:
        image (np.ndarray): Original image as a NumPy array.
        center_x (int): X-coordinate of the center for zoom.
        center_y (int): Y-coordinate of the center for zoom.
        size (int): Half of the width and height for the zoomed section.

    Returns:
        np.ndarray: Zoomed-in section of the image.
    """
    try:
        if image.size == 0:
            raise ValueError("Empty image array.")

        x_start = max(center_x - size, 0)
        x_end = min(center_x + size, image.shape[1])
        y_start = max(center_y - size, 0)
        y_end = min(center_y + size, image.shape[0])

        zoomed_img = image[y_start:y_end, x_start:x_end]

        print(f"New shape after slicing: {zoomed_img.shape}")
        print(zoomed_img)

        return zoomed_img

    except Exception as error:
        print("\033[31mError:", error, "\033[0m")
        return np.array([])


def convert_to_grayscale(image: np.ndarray) -> np.ndarray:
    """
    Converts an RGB image to grayscale.

    Args:
        image (np.ndarray): Image as a NumPy array.

    Returns:
        np.ndarray: Grayscale image.
    """
    try:
        if len(image.shape) == 3 and image.shape[2] == 3:
            grayscale_img = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
            return grayscale_img.astype(np.uint8)
        return image

    except Exception as error:
        print("\033[31mError:", error, "\033[0m")
        return np.array([])


def rotate_image(image: np.ndarray) -> np.ndarray:
    """
    Rotates an image by 90 degrees counterclockwise.

    Args:
        image (np.ndarray): Input image as a NumPy array.

    Returns:
        np.ndarray: Rotated image.
    """
    try:
        if image.size == 0:
            raise ValueError("Empty image array.")

        rotated_img = np.rot90(image)

        print(f"New shape after rotation: {rotated_img.shape}")
        print(rotated_img)

        return rotated_img

    except Exception as error:
        print("\033[31mError:", error, "\033[0m")
        return np.array([])


def display_image(image: np.ndarray):
    """
    Displays an image in black and white using Matplotlib.

    Args:
        image (np.ndarray): Image as a NumPy array.
    """
    try:
        if image.size == 0:
            raise ValueError("Cannot display an empty image.")

        plt.imshow(image, cmap="gray")
        plt.colorbar()
        plt.title("Rotated & Zoomed Image (Black & White)")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.show()

    except Exception as error:
        print("\033[31mError:", error, "\033[0m")


if __name__ == "__main__":
    image = ft_load("animal.jpeg")

    center_x, center_y = image.shape[1] // 2, image.shape[0] // 2
    zoom_size = 200

    zoomed_image = zoom_image(image, center_x, center_y, zoom_size)

    bw_image = convert_to_grayscale(zoomed_image)

    rotated_bw_image = rotate_image(bw_image)

    display_image(rotated_bw_image)
