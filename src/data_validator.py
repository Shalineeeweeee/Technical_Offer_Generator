import pandas as pd


def check_empty_cells(dataframe):
    """
    Returns a list of columns that contain empty values.
    """

    empty_columns = []

    for column in dataframe.columns:
        if dataframe[column].isnull().any():
            empty_columns.append(column)

    return empty_columns

def check_duplicates(dataframe):
    """
    Returns all duplicate rows.
    """

    duplicates = dataframe[dataframe.duplicated()]

    return duplicates

def check_data_types(dataframe):
    """
    Checks whether each column contains the expected data type.
    """

    errors = []

    for index, row in dataframe.iterrows():

        # Operating Voltage should end with "kV"
        voltage = str(row["Operating Voltage"])

        if not voltage.endswith("kV"):
            errors.append(
                f"Row {index + 1}: Invalid Operating Voltage ({voltage})"
            )

        # Power Rating should be a number
        try:
            float(row["Power Rating"])
        except:
            errors.append(
                f"Row {index + 1}: Invalid Power Rating ({row['Power Rating']})"
            )

    return errors