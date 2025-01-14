import logging
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from api.routes import root, question, profile, languages

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include essential routes
app.include_router(root.router)

# Mount static files after including routes
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load additional routes conditionally
# load_all_routes = os.getenv("LOAD_ALL_ROUTES", "false").lower() == "true"

# if load_all_routes:
#     app.include_router(question.router)
#     app.include_router(profile.router)
#     app.include_router(languages.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)