import pandas as pd
import os


def load(file_path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: The DataFrame containing the CSV data.
    """
    try:
        if not isinstance(file_path, str):
            raise TypeError("The path must be a string.")
        if not file_path:
            raise ValueError("The path must not be empty.")
        if not os.path.exists(file_path):
            raise FileNotFoundError(file_path)
        if not file_path.lower().endswith(".csv"):
            raise AssertionError("The file must be a CSV file.")

        data = pd.read_csv(file_path)

        print("Loading dataset of dimensions " + str(data.shape))

        if data is None:
            raise AssertionError("Failed to load CSV.")

        return data

    except Exception as error:
        print(type(error).__name__ + ":", error)
        exit(1)


if __name__ == "__main__":
    load("life_expectancy_years.csv")
