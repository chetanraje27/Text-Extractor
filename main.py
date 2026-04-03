from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
import shutil
import os

from ocr import extract_text, extract_text_from_pdf

app = FastAPI()

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {".pdf", ".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif", ".webp"}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.get("/", response_class=HTMLResponse)
async def home():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.post("/extract/")
async def extract_file(file: UploadFile = File(...)):
    try:
        ext = os.path.splitext(file.filename)[1].lower()
        if ext not in ALLOWED_EXTENSIONS:
            return JSONResponse(
                {"error": f"Unsupported file type. Allowed: {', '.join(ALLOWED_EXTENSIONS)}"},
                status_code=400
            )

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        if ext == ".pdf":
            text = extract_text_from_pdf(file_path)
        else:
            text = extract_text(file_path)

        if not text.strip():
            return JSONResponse(
                {"error": "Could not extract any text from the file."},
                status_code=400
            )

        return JSONResponse({"text": text})

    except Exception as e:
        return JSONResponse(
            {"error": f"Error processing file: {str(e)}"},
            status_code=500
        )
