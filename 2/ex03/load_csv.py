import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """
    Loads a CSV file into a Pandas DataFrame.

    Args:
        path (str): The file path of the dataset.

    Returns:
        pd.DataFrame: The loaded dataset or None if an error occurs.
    """
    try:
        if not os.path.exists(path):
            raise AssertionError("The file doesnt exist")
        if not path.lower().endswith('.csv'):
            raise AssertionError("The file fromat is not .csv")
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return None
