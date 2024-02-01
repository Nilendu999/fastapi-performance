
from fastapi import FastAPI, File, UploadFile, Response, HTTPException
import os, tempfile, shutil
import io
from fastapi.responses import JSONResponse,FileResponse
import json
import zipfile
import tarfile
from typing import List

app = FastAPI()

@app.get("/evaluate") 
async def send_html():
    file_path = "./test.html"
    return FileResponse(file_path, media_type="text/html")
@app.post("/evaluate_t") 
async def extract_and_zip(file: List[UploadFile] = File(...)):
    index_file = {
        "message": "Evaluation successful",
        "status": "success",
        "data": {
            "file_name": len(file)
        }
    }
    return JSONResponse(content=index_file)

@app.post("/evaluate_v") 
async def extract_and_zip(file: List[UploadFile] = File(...)):
    temp_dir = tempfile.mkdtemp()
    print(file.filename)
    subdirectory_name = file.filename.split(".")[0]
    subdirectory_path = os.path.join(temp_dir, subdirectory_name)
    print("Extracted files stored at : "+subdirectory_path)
    os.mkdir(subdirectory_path)
    file_path = f"{subdirectory_path}{os.path.sep}{file.filename}"
    file_path = f"./{file.filename}"
    print("Zip file stored at : ",file_path)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    if file.filename.endswith(".zip"):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(subdirectory_path)    
    elif file.filename.endswith(".tar"):
        with tarfile.open(file_path, 'r') as tar_ref:
            tar_ref.extractall(subdirectory_path)
    send_file={"files":os.listdir(subdirectory_path)} 
    return JSONResponse(content=send_file)
