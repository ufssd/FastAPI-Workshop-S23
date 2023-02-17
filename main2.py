import os
from fastapi import FastAPI 
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/SSD", responses={200: {"description": "SSD Logo", "content" : {"image/jpeg"}}})
def return_image():
    if os.path.exists("Logo.png"): # return the image if it exists
        return FileResponse("Logo.png", media_type="image/png", filename="SSD.png")
    return {"error" : "File not found!"} # return an error if the image does not exist