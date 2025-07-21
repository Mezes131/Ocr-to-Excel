from openpyxl import Workbook
import os
import uuid

def generate_excel(text: str, original_filename: str) -> str:
    """
    Generate a excel file from ocr text.
    :param text: Extracted raw text
    :param original_filename: Original image name (to name the Excel file)
    :return: Path to the generated Excel file
    """
    try:
        # Create a new Excel workbook
        wb = Workbook()
        ws = wb.active
        ws.title = "Texte OCR"

        # Insert text into the Excel file
        lines = text.splitlines()
        for idx, line in enumerate(lines, start=1):
            ws.cell(row=idx, column=1, value=line.strip())

        # Unique name for the output file
        safe_name = os.path.splitext(original_filename)[0].replace(" ", "_")
        file_id = uuid.uuid4().hex[:6]
        output_path = f"ocr_{safe_name}_{file_id}.xlsx"

        # Save the file
        wb.save(output_path)

        return output_path
    except Exception as e:
        print(f"Error during Excel file generation : {e}")
        return ""
