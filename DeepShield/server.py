from fastapi import FastAPI, UploadFile
import numpy as np
import cv2

from mesonet import MesoNet

app = FastAPI()

# Load model (make sure you have pretrained weights in ./weights/mesonet.h5)
model = MesoNet()
model.load_weights("weights/Meso4_DF.h5")

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (256, 256))
    img = img.astype("float32") / 255.0
    return np.expand_dims(img, axis=0)



@app.post("/detect-deepfake/")
async def detect_deepfake(file: UploadFile):
    if not file:
        return {"error": "Please upload an image."}

    try:
        # ✅ Read uploaded file directly into memory
        file_bytes = await file.read()
        np_arr = np.frombuffer(file_bytes, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        if img is None:
            return {"error": "Could not decode image"}

        # ✅ Preprocess
        img = cv2.resize(img, (256, 256))
        img = img.astype("float32") / 255.0
        img = np.expand_dims(img, axis=0)

        # ✅ Predict
        prediction = model.predict(img)[0][0]

        return {
            "deepfake_score": float(prediction),
            "is_fake": bool(prediction > 0.5)
        }

    except Exception as e:
        return {"error": str(e)}

