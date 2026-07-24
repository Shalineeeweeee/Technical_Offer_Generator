from parser import read_excel
from validator import validate_columns
from mapper import map_columns
from word_generator import create_word_document

from data_validator import (
    check_empty_cells,
    check_duplicates,
    check_data_types,
)

from business_validator import validate_business_rules

from report_generator import (
    generate_report,
    save_report,
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

        has_errors = False

        # -------------------------
        # Empty Cell Validation
        # -------------------------

        empty_columns = check_empty_cells(mapped_data)

        if empty_columns:

            has_errors = True

            print("\nData Validation Failed!")
            print("The following columns contain empty values:")

            for column in empty_columns:
                print(f"- {column}")

        else:

            print("\nNo empty cells found.")

            # -------------------------
            # Duplicate Validation
            # -------------------------

            duplicates = check_duplicates(mapped_data)

            if not duplicates.empty:

                has_errors = True
                print("\nDuplicate records found!")
                print(duplicates)

            else:

                print("\nNo duplicate rows found.")

            # -------------------------
            # Data Type Validation
            # -------------------------

            type_errors = check_data_types(mapped_data)

            if type_errors:

                has_errors = True
                print("\nData Type Errors Found!")

                for error in type_errors:
                    print(error)

            else:

                print("\nAll data types are valid.")

            # -------------------------
            # Business Validation
            # -------------------------

            business_errors = validate_business_rules(mapped_data)

            if business_errors:

                has_errors = True

                print("\nBusiness Rule Errors Found!")

                for error in business_errors:
                    print(error)

            else:

                print("\nBusiness Rules Passed.")

            # -------------------------
            # Final Data
            # -------------------------

            print("\nFinal Processed Data:\n")
            print(mapped_data)

            # -------------------------
            # Generate Report
            # -------------------------

            if not has_errors:

                report = generate_report(mapped_data)

                save_report(report, "output/technical_offer.txt")

                print("\nTechnical Offer generated successfully!")
                print("Saved to: output/technical_offer.txt")

            else:

                print("\nReport generation cancelled because validation failed.")

    else:

        print("\nValidation Failed!")
        print("Missing Columns:")

        for column in missing:
            print(f"- {column}")

print("Saved to: output/technical_offer.txt")
create_word_document()

print("Word document created successfully!")