import pandas as pd


def save_excel(
    english,
    hindi,
    marathi,
    output_file
):

    with pd.ExcelWriter(
        output_file,
        engine="openpyxl"
    ) as writer:

        pd.DataFrame(english).to_excel(
            writer,
            sheet_name="English",
            index=False
        )

        pd.DataFrame(hindi).to_excel(
            writer,
            sheet_name="Hindi",
            index=False
        )

        pd.DataFrame(marathi).to_excel(
            writer,
            sheet_name="Marathi",
            index=False
        )