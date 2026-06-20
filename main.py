from fastapi import FastAPI, Depends, HTTPException,File,UploadFile
from huggingface_hub import snapshot_download
from sentence_transformers import SentenceTransformer
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from transformers import CLIPModel, CLIPProcessor
from PIL import Image
import torch,io
from typing import List

# snapshot_download(
#     repo_id="sentence-transformers/all-MiniLM-L6-v2",
#     local_dir="E:\Model",  # you can set any path
#     local_dir_use_symlinks=False  # makes actual copies instead of symlinks
# )

# print("Embedding shape:", model.encode("Test").shape)

app  = FastAPI()

# Allow requests from your frontend
origins = [
#        Add your frontend URL here, for example:
        "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] to allow all origins (less secure)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ProductData(BaseModel):
    whatToEmbed: str
@app.on_event('startup')
def load_model():
        global model,ImageModel,processor
        model = SentenceTransformer("Model")
        ImageModel = CLIPModel.from_pretrained("ImageModel")
        processor = CLIPProcessor.from_pretrained("ImageModel")
         
@app.post("/embed/text")
async def add_embeddings(data:ProductData):
        searchData = data.whatToEmbed
        embeddings = model.encode(searchData)
        return {"success":True,"status":200,"embeddings": embeddings.tolist()}

@app.post('/embed/image')
async def embedImage(files: List[UploadFile] = File(...)):
        embeddings_list = []
        
        for file in files:
                contents = await file.read()
                image = Image.open(io.BytesIO(contents))
                inputs = processor(images=image, return_tensors="pt")

        
        with torch.no_grad():
                image_embeddings = ImageModel.get_image_features(**inputs)
                image_embeddings = image_embeddings / image_embeddings.norm(p=2, dim=-1, keepdim=True)
                embeddings_list.append(image_embeddings.squeeze().tolist())
                # print(embeddings_list)
        return {"success":True,"status":200,"embeddings":  embeddings_list}
