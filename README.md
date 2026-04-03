# Text Extractor 📄

A powerful web application for extracting text from images and PDFs using OCR (Optical Character Recognition). Upload documents and instantly get their text content through an intuitive web interface.

## Features ✨

- **Image OCR**: Extract text from PNG, JPG, JPEG, TIFF, BMP, GIF, and WebP images
- **PDF Processing**: Automatically convert and extract text from PDF files
- **Web Interface**: Beautiful, responsive drag-and-drop UI
- **Fast & Reliable**: Uses Tesseract OCR and pdf2image for accurate text extraction
- **RESTful API**: JSON endpoints for programmatic access

## Tech Stack 🛠️

- **Backend**: FastAPI (Python)
- **OCR Engine**: Tesseract OCR
- **PDF Processing**: pdf2image with Poppler
- **Frontend**: HTML5 with vanilla JavaScript
- **IDE**: Visual Studio Code

## Prerequisites 📋

For Windows, you need:

- **Windows 10/11**
- **Python 3.8+** (Download from [python.org](https://www.python.org/downloads/))
- **Visual Studio Code** (Download from [code.visualstudio.com](https://code.visualstudio.com/))
- **Tesseract OCR** (Download from [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki))
- **Poppler** (Download from [poppler-windows](https://blog.alivate.com.au/poppler-windows/))

## Setup Instructions 🚀 (Windows)

### 1. Install Required Software

#### Install Tesseract OCR
- Download installer from: https://github.com/UB-Mannheim/tesseract/wiki
- Run the installer and note the installation path (default: `C:\Program Files\Tesseract-OCR`)

#### Install Poppler
- Download from: https://blog.alivate.com.au/poppler-windows/
- Extract to a folder (e.g., `C:\Program Files\poppler-25.12.0\Library\bin`)

### 2. Clone or Extract Repository
```bash
git clone https://github.com/chetanraje27/Text-Extractor.git
cd TextExtractor
```

### 3. Open in VS Code
```bash
code .
```

### 4. Create Virtual Environment in VS Code

Open the integrated terminal in VS Code (Ctrl + `):

```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt.

### 5. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 6. Configure Environment Variables

1. Copy `.env.example` to `.env` in the project root
2. Open `.env` and update the paths with your actual installation paths:

```env
TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe
POPPLER_PATH=C:\Program Files\poppler-25.12.0\Library\bin
```

### 7. Run the Application

In VS Code terminal (with venv activated):

```bash
python -m uvicorn main:app --reload
```

You'll see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

### 8. Open in Browser
Click on or navigate to: **http://127.0.0.1:8000**

## Usage 💻

### Web Interface
1. Application will automatically open at `http://127.0.0.1:8000`
2. Drag & drop or click to browse image/PDF files
3. Supported formats: `.pdf`, `.png`, `.jpg`, `.jpeg`, `.tiff`, `.bmp`, `.gif`, `.webp`
4. Extracted text appears in the results section
5. Copy the extracted text with one click

### API Testing in VS Code
Install the **REST Client** extension in VS Code:
1. Open Extensions (Ctrl+Shift+X)
2. Search for "REST Client" by Huachao Mao
3. Install it

Create a file `test.http` in project root:
```http
POST http://127.0.0.1:8000/extract/
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW

------WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="file"; filename="test.pdf"
Content-Type: application/pdf

< ./test.pdf
------WebKitFormBoundary7MA4YWxkTrZu0gW--
```

Click "Send Request" to test the API.

## Project Structure 📁

```
TextExtractor/
├── main.py              # FastAPI application & routes
├── ocr.py               # OCR & PDF processing logic
├── templates/
│   └── index.html       # Web UI
├── uploads/             # Temporary uploaded files (auto-created)
├── .vscode/             # VS Code settings (optional)
├── venv/                # Virtual environment (created during setup)
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (LOCAL ONLY - NOT in git)
├── .env.example         # Environment variables template
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Environment Variables 🔐

In the project root, create a `.env` file (copy from `.env.example`):

```env
# Windows Tesseract OCR path (REQUIRED)
# Default installation: C:\Program Files\Tesseract-OCR\tesseract.exe
TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe

# Windows Poppler bin path (REQUIRED)
# Extract and note the path where poppler is extracted
POPPLER_PATH=C:\Program Files\poppler-25.12.0\Library\bin
```

**Important**: 
- Never commit `.env` to git (already in `.gitignore`)
- Update paths according to your installation directory
- Use full paths, not relative paths

## API Reference 📚

### GET /
Returns the web interface HTML.

**Access in browser**: http://127.0.0.1:8000

### POST /extract/
Extract text from an uploaded file.

**Using REST Client in VS Code**:
```http
POST http://127.0.0.1:8000/extract/
Content-Type: multipart/form-data; boundary=----Boundary

------Boundary
Content-Disposition: form-data; name="file"; filename="document.pdf"
Content-Type: application/pdf

< ./document.pdf
------Boundary--
```

**Success Response** (200):
```json
{
  "text": "extracted text content here..."
}
```

**Error Response** (400/500):
```json
{
  "error": "Unsupported file type..." or "Error processing file..."
}
```

**Supported File Types**:
- Images: `.png`, `.jpg`, `.jpeg`, `.tiff`, `.bmp`, `.gif`, `.webp`
- Documents: `.pdf`

## Troubleshooting 🔧 (Windows)

### "Tesseract is not installed"
- Ensure you've downloaded and installed Tesseract from the official source
- Check that installation path is correct in `.env` file
- Try the default path: `C:\Program Files\Tesseract-OCR\tesseract.exe`
- If still failing, verify the file exists in that folder using Windows Explorer

### "Poppler not found"
- Download Poppler from: https://blog.alivate.com.au/poppler-windows/
- Extract the ZIP file to a location (e.g., `C:\Program Files\poppler-25.12.0`)
- Update `POPPLER_PATH` in `.env` to the `Library\bin` subfolder
- Example: `C:\Program Files\poppler-25.12.0\Library\bin`

### "No text extracted from file"
- Ensure the image quality is high enough for OCR
- Text must be visible and reasonably sized
- Try with a sample PDF/image to test

### "Module not found" error
- Ensure venv is activated: Look for `(venv)` in the terminal prompt
- Run: `pip install -r requirements.txt` again
- Try: `pip install --upgrade pip`

### "Port 8000 already in use"
In VS Code terminal:
```bash
python -m uvicorn main:app --reload --port 8001
```
Then access at `http://127.0.0.1:8001`

### Quick Debug in VS Code
In **Debug Console** (Ctrl+Shift+Y), you can check environment variables:
```python
import os
print(os.environ.get('TESSERACT_PATH'))
print(os.environ.get('POPPLER_PATH'))
```

## VS Code Recommended Extensions 🎨

Install these extensions for better development experience:

1. **Python** - by Microsoft
2. **Pylance** - by Microsoft (better IntelliSense)
3. **FastAPI** - Better FastAPI support
4. **REST Client** - Test API endpoints directly
5. **Thunder Client** - Alternative to REST Client

To install: Open Extensions (Ctrl+Shift+X) and search by name.

## Development Tips 💡

### Running with Auto-Reload
The `--reload` flag automatically restarts the server when you save code:
```bash
python -m uvicorn main:app --reload
```

### VS Code Debug Mode
Create `.vscode/launch.json`:
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "FastAPI",
            "type": "python",
            "request": "launch",
            "module": "uvicorn",
            "args": ["main:app", "--reload"],
            "jinja": true,
            "justMyCode": true
        }
    ]
}
```
Then press F5 to start debugging.

### Check Installed Packages
In VS Code terminal:
```bash
pip list
```

### Clear Uploaded Files
Periodically clear the `uploads/` folder to save disk space.

## Getting Help 🆘

### In VS Code
1. Check the **Problems** panel (Ctrl+Shift+M) for Python errors
2. Check the **Output** panel for server logs when running
3. Use Python extension's **Run and Debug** feature (F5)

### Debugging Steps
1. Verify `.env` file exists in project root
2. Check `TESSERACT_PATH` and `POPPLER_PATH` are correct
3. Run a simple test: `python ocr.py` 
4. Check terminal output for specific error messages

### Still Having Issues?
- Google the exact error message
- Check the prerequisites are properly installed
- Verify paths in `.env` file exist on your system



---

**Happy extracting! 🎉 Start the server with `python -m uvicorn main:app --reload` and open your browser to http://127.0.0.1:8000**
