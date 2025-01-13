# LinkedIn CV Processor

This project is a FastAPI application for processing CVs. It extracts information from CVs, stores the data in a MongoDB database, and provides endpoints for various operations such as uploading CVs, asking questions, and deleting profiles.

## Project Structure

/project-root ├── api │ ├── init.py │ ├── routes │ │ ├── init.py │ │ ├── cv.py │ │ ├── question.py │ │ ├── profile.py │ │ └── languages.py ├── controllers │ ├── init.py │ └── cv_controller.py ├── services │ ├── init.py │ └── cv_service.py ├── helpers │ ├── init.py │ └── logger.py │ └── cv_processor_helper.py ├── models │ ├── init.py │ └── profile_model.py ├── static │ └── styles.css ├── templates │ ├── index.html │ └── upload.html ├── main.py ├── vercel.json └── requirements.txt


## Setup

### Prerequisites

- Python 3.11
- MongoDB
- Node.js (for Vercel deployment)

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/your-username/linkedin-cv-processor.git
   cd linkedin-cv-processor
   

2. Create a virtual environment and activate it:

 ``sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the dependencies:
   ``sh
   pip install -r requirements.txt

4. Set up MongoDB:

Ensure MongoDB is running and accessible.
   Update the MongoDB connection URI in profile_model.py if necessary.
   Running the Application
   Start the FastAPI application:

5. Running the Application
   Start the FastAPI application:
    ``sh
   uvicorn main:app --reload

6. Deployment
   Deploy the project:
    ``sh
   vercel

### Explanation

- **Project Structure**: Provides an overview of the project's directory structure.
- **Setup**: Instructions for setting up the project, including prerequisites, installation, and running the application.
- **Usage**: Examples of how to use the API endpoints with `curl` commands.
- **Deployment**: Instructions for deploying the project using Vercel.
- **Contributing**: Information on how to contribute to the project.
- **License**: Information about the project's license.

By following these instructions, users should be able to set up, run, and use your FastAPI application for processing CVs.
### Explanation

- **Project Structure**: Provides an overview of the project's directory structure.
- **Setup**: Instructions for setting up the project, including prerequisites, installation, and running the application.
- **Usage**: Examples of how to use the API endpoints with `curl` commands.
- **Deployment**: Instructions for deploying the project using Vercel.
- **Contributing**: Information on how to contribute to the project.
- **License**: Information about the project's license.

By following these instructions, users should be able to set up, run, and use your FastAPI application for processing CVs.