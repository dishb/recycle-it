import base64

import requests

from .cloud_storage import upload_store
from .popup import Popup

def encode_image(image_path: str) -> str:
    """
    Encodes an image into base64.
    """

    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read())

        return encoded_image.decode("utf-8")

def analyze_image(image: str, api_key: str, client_id: str) -> None:
    """
    Analyzes an image using RapidAPI's Recicl API.
    """

    api_url = "https://reciclapi-garbage-detection.p.rapidapi.com/predict"
    url = upload_store(image, client_id)

    payload = { "image": url }
    headers = {"content-type": "application/json",
               "X-RapidAPI-Key": api_key,
               "X-RapidAPI-Host": "reciclapi-garbage-detection.p.rapidapi.com"
               }

    response = requests.post(api_url, json = payload, headers = headers)
    if response.status_code != 429: # in case we exceed API rate limits
        material = response.json()[0]["class"]

        return material

    Popup(300,
        300,
        "Error: Rate Limit",
        "The rate limit for your RapidAPI\nkey has been exceeded.\nPlease try again later.",
        False,
        False
        )

    return 429
