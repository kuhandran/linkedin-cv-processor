from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>CV Processor</title>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body>
            <div style="max-width: 800px; margin: 50px auto; padding: 20px; font-family: system-ui, -apple-system, sans-serif;">
                <h1>CV Processor</h1>
                <p>Welcome to the CV Processor API. The service is running correctly.</p>
                <div id="status"></div>
            </div>
            <script>
                fetch('/health')
                    .then(response => response.json())
                    .then(data => {
                        document.getElementById('status').innerHTML = 
                            `<p>API Status: ${data.status}</p>`;
                    })
                    .catch(error => {
                        document.getElementById('status').innerHTML = 
                            `<p style="color: red;">Error: ${error.message}</p>`;
                    });
            </script>
        </body>
    </html>
    """

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

@app.get("/api/test")
async def test_endpoint():
    return {"message": "API is working correctly"}

