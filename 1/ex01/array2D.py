def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D list (array), prints its shape, and returns a
        new truncated version.

    Args:
        family (list): A 2D list representing rows of data.
        start (int): The starting row index for slicing.
        end (int): The ending row index for slicing.

    Returns:
        list: The truncated 2D list after slicing.
    """
    try:
        if not isinstance(family, list) or not all(isinstance(row, list)
                                                   for row in family):
            raise TypeError("Input must be a 2D list.")

        row_length = len(family[0])
        if not all(len(row) == row_length for row in family):
            raise ValueError("All rows must have the same number of elements.")

        print(f"My shape is : ({len(family)}, {row_length})")

        new_family = family[start:end]

        print(f"My new shape is : ({len(new_family)}, {row_length})")

        return new_family

    except Exception as error:
        print("An error occurred:", error)
        return []
