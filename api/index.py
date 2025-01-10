from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "CV Processor API is running"}

@app.get("/ui", response_class=HTMLResponse)
async def ui():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CV Processor</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: system-ui, -apple-system, sans-serif; margin: 0; padding: 20px; }
            .container { max-width: 800px; margin: 0 auto; }
            .status { margin-top: 20px; padding: 10px; border-radius: 4px; }
            .success { background-color: #e6ffe6; }
            .error { background-color: #ffe6e6; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>CV Processor</h1>
            <p>Welcome to the CV Processor. This is a public endpoint.</p>
            <div id="status"></div>
        </div>
        <script>
            fetch('/')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('status').innerHTML = `
                        <div class="status success">
                            ${data.message}
                        </div>
                    `;
                })
                .catch(error => {
                    document.getElementById('status').innerHTML = `
                        <div class="status error">
                            Error: ${error.message}
                        </div>
                    `;
                });
        </script>
    </body>
    </html>
    """

@app.get("/health")
async def health():
    return {"status": "healthy"}

