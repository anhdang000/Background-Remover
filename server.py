import io
from PIL import Image
from fastapi import FastAPI
from fastapi import UploadFile, File, Form
from fastapi.responses import FileResponse
from starlette.responses import StreamingResponse
import uvicorn

from model_configs import *
from demo import inference


app = FastAPI()

@app.post('/challenge')
def predict(challenge: str = Form(...), input: UploadFile = File(...)):
    # Check challenge name
    if challenge != 'cv3':
        return {"message": "The API only works for challenge `cv3`"}

    # Check file format
    file_ext = input.filename.split('.')[-1]
    supported_image_formats = ['bmp', 'jpg', 'jpeg', 'jp2', 'png', 'tiff', 'webp', 'xbm']
    if file_ext not in supported_image_formats:
        return {
            "error": "Cannot read the imported file. Please refer to our supported image formats", 
            "supported_image_formats": str(supported_image_formats)
            }

    # Check file validation
    try:
        image = Image.open(input.file).convert('RGB')
    except:
        return {"error": f"File {input.filename} could not be read"}

    if image is None:
        return {"error": f"File {input.filename} could not be read"}
    
    image = np.array(image)
    image, raw_image = preprocessing(image, device, CONFIG)
    labelmap = inference(model, image, raw_image, postprocessor)
    labels = np.unique(labelmap)

    mask = np.zeros((raw_image.shape[0], raw_image.shape[1]))
    for i, label in enumerate(labels):
        mask_inclass = labelmap == label

        class_name = classes[label]
        if class_name in classes_of_interest:
            mask += mask_inclass
    
    # Create mask
    mask = np.where(mask >= 1, 1, mask)
    mask = (mask * 255).astype(np.uint8)
    if np.max(mask) == 0:
        return {"warning": "Could not find any subjects in the image"}
    else:
        mask_3d = np.stack([mask]*3, axis=2)

    # Apply with source
    raw_rgb = raw_image[:, :, ::-1]
    output = np.where(mask_3d == 255, raw_rgb, 255)

    _, output_png = cv2.imencode('.png', output)

    return StreamingResponse(io.BytesIO(output_png.tobytes()), media_type="image/png")
