
# Document Chat Assistant

This project is a RESTful API built using FastAPI, PostgreSQL, MongoDB. Users can upload PDF files, extract content from them. User authentication is done via JWT.

## 🚀 Getting Started

### Requirements
- Python 3.8 or higher
- PostgreSQL
- MongoDB (for storing PDF data using GridFS)s

### Installation

1. **Create and activate a Python virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   .\venv\Scripts\activate  # Windows
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure database settings:**
   - Update the PostgreSQL connection settings in the `base_config.py` file.
   - Update the MongoDB connection settings in the `core/mongo.py` file.

### Running Locally

To run the project locally, use:
   ```bash
   uvicorn main:app --host 127.0.0.1 --port 8000 --reload
   ```

## 🖥 API Usage

### 1. **User Registration and Login**

#### **POST /register**
- Registers a new user.

#### **POST /login**
- Authenticates a user and returns a JWT token.

### 2. **PDF Management**

#### **POST /pdf-upload**
- Uploads a PDF file, stored in MongoDB using GridFS.

#### **GET /pdf-list**
- Returns a list of uploaded PDFs.

#### **POST /pdf-parse**
- Extracts text content from a PDF.

#### **POST /pdf-select**
- Selects a PDF for chatting.

### License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
