from fastapi import FastAPI, UploadFile
from transformers import AutoImageProcessor, ResNetForImageClassification
import torch
from datasets import load_dataset
from loguru import logger
from PIL import Image
import io

app = FastAPI()

processor = AutoImageProcessor.from_pretrained("microsoft/resnet-50")
model = ResNetForImageClassification.from_pretrained("microsoft/resnet-50")

@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.post('/uploadfile')
async def upload_animal_file(file: UploadFile):
    logger.info("file is uploaded", file.filename)
    return {"filename": file.filename}

@app.post('/predict')
async def predict(file: UploadFile):
    # dataset = load_dataset("huggingface/cats-image")
    # image = dataset["test"]["image"][0]
    file_content = await file.read()
    image = Image.open(io.BytesIO(file_content))

    inputs = processor(image, return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits

    # model predicts one of the 1000 ImageNet classes
    predicted_label = logits.argmax(-1).item()
    string_label = model.config.id2label[predicted_label]
    logger.info(f"predicted label is {string_label}")
    return string_label

