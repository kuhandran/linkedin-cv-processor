from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "CV Processor API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/process-cv")
async def process_cv(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        return {
            "status": "success",
            "filename": file.filename,
            "size": len(contents)
        }
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": f"Error processing file: {str(e)}"}
        )

