# 🖋️ OCR-to-Excel Web API

A web application that automatically extracts handwritten text from a scanned image (JPEG/PNG) and converts it into an Excel file (.xlsx). The backend is written in Python (FastAPI) and designed to integrate with a Vue.js frontend.

---

## 🚀 Features

* 📷 Image upload (photo or scan with handwritten text)
* 🧠 OCR processing using Tesseract (supports French language)
* 📄 Automatic generation of an Excel file containing the extracted text
* 🌐 RESTful API ready for frontend integration

---

## 🧰 Tech Stack

* Backend: Python 3.10+, FastAPI
* OCR: Tesseract OCR via pytesseract
* Excel file generation: openpyxl
* Image processing: Pillow
* File upload handling: python-multipart

---

## 🗂️ Project Structure

```
ocr_excel_backend/
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── api/routes.py        # API route (upload & response)
│   ├── services/
│   │   ├── ocr_service.py   # OCR processing logic
│   │   └── excel_service.py # Excel file generation
│   ├── utils/file_utils.py  # (optional) Utility functions
│   └── config.py            # Tesseract path configuration
├── requirements.txt         # Python dependencies
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the project

```bash
git clone https://github.com/your-username/ocr_excel_backend.git
cd ocr_excel_backend
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Tesseract OCR

* Download and install from: [https://github.com/UB-Mannheim/tesseract/wiki](https://github.com/UB-Mannheim/tesseract/wiki)
* By default, Tesseract installs to:
  C:\Program Files\Tesseract-OCR\tesseract.exe

🛠️ In app/config.py, update the path if needed:

```python
TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

## ▶️ Run the API

```bash
uvicorn app.main:app --reload
```

Then open the interactive Swagger documentation:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📤 Usage Example

1. Make a POST request to /ocr-to-excel
2. Upload an image (JPEG or PNG)
3. The API returns the generated .xlsx file containing the extracted text

---

## 🧪 Recommended Tests

* 📄 Clear and high-quality handwritten image
* 🧑‍🏫 Use the OCR model for French: lang='fra'
* 💬 Try different text formats (forms, notes, lists)

---

## 🧱 Roadmap (Next Steps)

* [ ] ✏️ Auto-structure data (e.g., Name, Age, Address → separate Excel columns)
* [ ] 🗂️ Use a temporary directory to store generated Excel files
* [ ] 🌍 Deployment (Railway, Render)
* [ ] 🌐 Vue.js frontend (drag & drop UI)

---

## 👨‍💻 Author

Developed by \[Mezes]
Contact: [mezatioange@gmail.com](mailto:mezatioange@gmail.com)
