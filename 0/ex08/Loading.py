"""This module provides a progress bar similar to tqdm."""
import sys


def ft_tqdm(lst: range) -> None:
    """
    Create a progress bar for iterating through a range.

    Parameters:
        lst (range): The range to iterate through.

    Yields:
        Each element in the range while displaying a progress bar.
    """
    total = len(lst)

    for i, item in enumerate(lst, 1):
        percent = (i / total) * 100

        bar_length = 60
        filled_length = int(bar_length * i // total)

        progress_bar = ('[' + '=' * filled_length + '>' +
                        ' ' * (bar_length - filled_length - 1) + ']')

        sys.stdout.write(f"\r{percent:3.0f}%|{progress_bar}| {i}/{total}")
        sys.stdout.flush()

        yield item
