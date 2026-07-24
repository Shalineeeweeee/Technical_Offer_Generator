def generate_report(dataframe):
    """
    Generates a simple technical offer report.
    """

    report = []

    report.append("=" * 60)
    report.append("TECHNICAL OFFER")
    report.append("=" * 60)
    report.append("")

    for index, row in dataframe.iterrows():

        report.append(f"Client              : {row['Client']}")
        report.append(f"Operating Voltage   : {row['Operating Voltage']}")
        report.append(f"Power Rating        : {row['Power Rating']}")
        report.append("-" * 60)

    return "\n".join(report)


def save_report(report, filename):
    """
    Saves the generated report to a text file.
    """

    with open(filename, "w") as file:
        file.write(report)