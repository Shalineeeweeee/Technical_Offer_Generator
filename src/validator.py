def validate_columns(dataframe, required_columns):
    """
    Checks whether all required columns exist in the Excel file.
    Returns:
        (True, []) if valid
        (False, missing_columns) otherwise
    """

    missing_columns = []

    for column in required_columns:
        if column not in dataframe.columns:
            missing_columns.append(column)

    if len(missing_columns) == 0:
        return True, []

    return False, missing_columns