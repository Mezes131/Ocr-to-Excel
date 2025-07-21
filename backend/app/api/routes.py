from fastapi import APIRouter, UploadFile, File
from app.services.ocr_service import extract_text_from_image
from app.services.excel_service import generate_excel
from fastapi.responses import FileResponse
import os
import uuid

router = APIRouter()

@router.post("/ocr-to-excel")
async def ocr_to_excel(file: UploadFile = File(...)):
    contents = await file.read()

    # Extract text
    text = extract_text_from_image(contents)

    # Generate excel file
    output_path = generate_excel(text, file.filename)

    return FileResponse(output_path, filename=os.path.basename(output_path), media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
