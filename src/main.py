from mapper import map_columns
from data_validator import check_empty_cells
from config import REQUIRED_COLUMNS, COLUMN_MAPPING
from parser import read_excel
from validator import validate_columns

file_path = "sample_input/sample.xlsx"

data = read_excel(file_path)

if data is not None:

    valid, missing = validate_columns(data, REQUIRED_COLUMNS)

    if valid:

        print("\nValidation Successful!\n")

        mapped_data = map_columns(data, COLUMN_MAPPING)

        empty_columns = check_empty_cells(mapped_data)

        if empty_columns:

            print("\nData Validation Failed!")
            print("The following columns contain empty values:")

            for column in empty_columns:
                print(f"- {column}")

        else:

            print("\nNo empty cells found.\n")
            print(mapped_data)

    else:

        print("\nValidation Failed!")
        print("Missing Columns:")

        for column in missing:
            print("-", column)