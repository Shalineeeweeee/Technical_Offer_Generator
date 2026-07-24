def validate_business_rules(dataframe):
    """
    Validates business-specific rules.
    """

    errors = []

    for index, row in dataframe.iterrows():

        # Power Rating must be greater than zero
        if float(row["Power Rating"]) <= 0:
            errors.append(
                f"Row {index + 1}: Power Rating must be greater than zero."
            )

        # Voltage should end with kV
        voltage = str(row["Operating Voltage"])

        if not voltage.endswith("kV"):
            errors.append(
                f"Row {index + 1}: Operating Voltage must end with 'kV'."
            )

    return errors