from datetime import datetime
import os
from PIL import Image
import uuid

UPLOAD_FOLDER = 'static'

def save_image(img, prefix):
    filename = f'{prefix}_{format(datetime.now().strftime("%Y%m%d_%H%M%S"))}_{str(uuid.uuid4())}.webp'
    path = os.path.join(UPLOAD_FOLDER, filename)
    imagen_pil = Image.open(img)
    if imagen_pil.mode != 'RGB':
        imagen_pil = imagen_pil.convert('RGB')
    imagen_pil.save(path, 'WEBP')
    return f"/{UPLOAD_FOLDER}/{filename}"
