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