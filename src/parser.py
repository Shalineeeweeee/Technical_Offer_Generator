import pandas as pd

def read_excel(file_path):
    """
    Reads an Excel file and returns a Pandas DataFrame.
    """

    try:
        df = pd.read_excel(file_path)

        print("Excel file loaded successfully!")
        return df

    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None