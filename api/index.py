from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import spacy

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except:
    nlp = None

@app.get("/")
async def read_root():
    return {"message": "CV Processor API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "spacy_model": "loaded" if nlp else "not loaded"}

@app.post("/process-cv")
async def process_cv(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        text = contents.decode()
        
        if nlp:
            doc = nlp(text)
            # Basic extraction (you can expand this based on your needs)
            entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
            
            return {
                "status": "success",
                "filename": file.filename,
                "entities": entities
            }
        else:
            return JSONResponse(
                status_code=500,
                content={"message": "Spacy model not loaded"}
            )
            
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": f"Error processing file: {str(e)}"}
        )

