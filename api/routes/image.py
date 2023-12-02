""" Image routes for the API. """
import io

import numpy as np
import rasterio
from fastapi import UploadFile
from fastapi.responses import StreamingResponse
from fastapi.routing import APIRouter
from PIL import Image

router = APIRouter(tags=["Image"])


@router.post("/attributes")
async def get_image_attributes(image: UploadFile):
    file_content = await image.read()
    with rasterio.open(io.BytesIO(file_content)) as dataset:
        attributes = {
            "image_size": {
                "width": dataset.width,
                "height": dataset.height
            },
            "number_of_bands": dataset.count,
            "coordinate_reference_system": dataset.crs.to_string(),
            "georeferenced_bounding_box": dataset.bounds
        }
    return attributes


@router.post("/thumbnail")
async def generate_thumbnail(image: UploadFile, resolution: int = 100):
    file_content = await image.read()
    with rasterio.open(io.BytesIO(file_content)) as dataset:
        data = dataset.read()
        rgb_image = np.dstack((data[0], data[1], data[2]))
        thumbnail = Image.fromarray(rgb_image.astype(np.uint8))
        thumbnail.thumbnail((resolution, resolution))
        thumbnail_bytes = io.BytesIO()
        thumbnail.save(thumbnail_bytes, format="PNG")
        thumbnail_bytes.seek(0)
    return StreamingResponse(content=thumbnail_bytes, media_type="image/png")
