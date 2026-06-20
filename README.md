# Text and Image Embedding API

A professional FastAPI-based service that provides high-performance vector embeddings for both text and images. This project leverages state-of-the-art transformer models to convert unstructured data into dense vector representations, enabling advanced semantic search, image retrieval, and similarity analysis.

## 🚀 Features

- **Text Embeddings**: Generates semantic vectors from text using the `SentenceTransformer` model.
- **Image Embeddings**: Generates visual vectors from images using the `CLIP` (Contrastive Language-Image Pre-training) model.
- **FastAPI Integration**: High-performance asynchronous API endpoints.
- **CORS Enabled**: Pre-configured to allow requests from specified frontend origins.
- **Dockerized**: Ready for seamless deployment via Docker.

## 🛠️ Project Structure

```text
.
├── Dockerfile              # Docker configuration for deployment
├── main.py                 # FastAPI application logic
├── requirements.txt        # Python dependencies
├── ImageModel/             # CLIP model weights and configuration
└── Model/                  # SentenceTransformer model weights and configuration
```

## 📋 Prerequisites

- Python 3.9+
- Docker (optional, for containerized deployment)

## ⚙️ Installation & Setup

### Local Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <project-folder>
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

### Docker Setup

1. **Build the image**:
   ```bash
   docker build -t embedding-api .
   ```

2. **Run the container**:
   ```bash
   docker run -p 8000:8000 embedding-api
   ```

## 🔌 API Reference

### 1. Text Embedding
Converts a string of text into a vector embedding.

- **Endpoint**: `POST /embed/text`
- **Payload**:
  ```json
  {
    "whatToEmbed": "Your text here"
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "status": 200,
    "embeddings": [0.123, -0.456, ...]
  }
  ```

### 2. Image Embedding
Converts one or more images into vector embeddings.

- **Endpoint**: `POST /embed/image`
- **Payload**: `multipart/form-data` (Upload one or more image files)
- **Response**:
  ```json
  {///////////////////////////////////////////
    "success": true,
    "status": 200,
    "embeddings": [
      [0.123, -0.456, ...],
      [0.789, 0.012, ...]
    ]
  }
  ```

## 🧠 Model Details

- **Text Model**: Uses a local instance of `SentenceTransformer` located in the `/Model` directory.
- **Image Model**: Uses a local instance of `CLIP` located in the `/ImageModel` directory.

## 🛡️ CORS Configuration
The API is currently configured to allow requests from:
- `http://localhost:3000`

To change these, modify the `origins` list in `main.py`.
