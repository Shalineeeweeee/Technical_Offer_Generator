from mapper import map_columns
from config import REQUIRED_COLUMNS, COLUMN_MAPPING
from parser import read_excel
from validator import validate_columns

file_path = "sample_input/sample.xlsx"

from config import REQUIRED_COLUMNS

data = read_excel(file_path)

if data is not None:

    valid, missing = validate_columns(data, REQUIRED_COLUMNS)

    if valid:

        print("\nValidation Successful!\n")

        mapped_data = map_columns(data, COLUMN_MAPPING)

        print(mapped_data)

    else:

        print("\nValidation Failed!")

        print("Missing Columns:")

        for column in missing:
            print("-", column)