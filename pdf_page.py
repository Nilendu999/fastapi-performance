from fastapi import FastAPI, File, UploadFile, Form
from typing import Dict
import shutil
import tempfile
import os
import PyPDF2

app = FastAPI()

def count_pdf_pages(file_path: str) -> int:
    with open(file_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        return pdf_reader.numPages

@app.post("/upload/")
async def upload_pdf(file: UploadFile, response_type: str = Form(...)):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            shutil.copyfileobj(file.file, tmp_file)

        page_count = count_pdf_pages(tmp_file.name)

        if response_type == "json":
            response_data = {
                "filename": file.filename,
                "page_count": page_count,
            }
        elif response_type == "text":
            response_data = f"Filename: {file.filename}, Page Count: {page_count}"
        else:
            return {"error": "Invalid response_type. Use 'json' or 'text'."}

        return response_data

    finally:
        os.unlink(tmp_file.name)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
