from parser import read_excel
from validator import validate_columns
from mapper import map_columns
from data_validator import (
    check_empty_cells,
    check_duplicates,
    check_data_types,
)
from config import REQUIRED_COLUMNS, COLUMN_MAPPING


# Path to the Excel file
file_path = "sample_input/sample.xlsx"


# Read Excel file
data = read_excel(file_path)

if data is not None:

    # Validate required columns
    valid, missing = validate_columns(data, REQUIRED_COLUMNS)

    if valid:

        print("\nValidation Successful!")

        # Rename columns
        mapped_data = map_columns(data, COLUMN_MAPPING)

        # -------------------------
        # Empty Cell Validation
        # -------------------------
        empty_columns = check_empty_cells(mapped_data)

        if empty_columns:

            print("\nData Validation Failed!")
            print("The following columns contain empty values:")

            for column in empty_columns:
                print(f"- {column}")

        else:

            print("\nNo empty cells found.")

            # -------------------------
            # Duplicate Check
            # -------------------------
            duplicates = check_duplicates(mapped_data)

            if not duplicates.empty:

                print("\nDuplicate records found!")
                print(duplicates)

            else:

                print("\nNo duplicate rows found.")

            # -------------------------
            # Data Type Validation
            # -------------------------
            type_errors = check_data_types(mapped_data)

            if type_errors:

                print("\nData Type Errors Found!")

                for error in type_errors:
                    print(error)

            else:

                print("\nAll data types are valid.")

            # -------------------------
            # Display Final Data
            # -------------------------
            print("\nFinal Processed Data:\n")
            print(mapped_data)

    else:

        print("\nValidation Failed!")
        print("Missing Columns:")

        for column in missing:
            print(f"- {column}")