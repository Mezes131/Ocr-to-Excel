from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="OCR to Excel API",
    description="API to extract handwritten text from an image and generate an Excel file.",
    version="1.0.0"
)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)