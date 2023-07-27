import requests
from PIL import Image
from io import BytesIO

def get_image_from_url(url):
    try:
        response = requests.get(url)
    except:
        return None
    img = None
    try:
        img = Image.open(BytesIO(response.content))
    except:
        return None
    return img