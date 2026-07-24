from engineering_parser import parse_engineering_sheet
from word_generator import create_word_document

# ============================================
# Select Engineering Excel File
# ============================================

file_path = "sample_input/sample.xlsx"

print("\nReading Engineering Excel Sheet...\n")

# ============================================
# Parse Engineering Sheet
# ============================================

pump_data = parse_engineering_sheet(file_path)

print("Engineering sheet loaded successfully!")

# ============================================
# Display Extracted Data
# ============================================

print("\n" + "=" * 60)
print("EXTRACTED DATA")
print("=" * 60)

total = 0

for section, fields in pump_data.items():

    print("\n" + "=" * 60)
    print(section.upper())
    print("=" * 60)

    for key, value in fields.items():
        print(f"{key} : {value}")
        total += 1

print(f"\nTotal Parameters Found: {total}")

# ============================================
# Generate Technical Offer
# ============================================

create_word_document(pump_data)

print("\nTechnical Offer generated successfully!")
print("Saved to: output/technical_offer.docx")