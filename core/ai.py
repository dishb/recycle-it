#
#    Helping you help the planet. Recycling made easy.
#    Copyright (C) 2023  Dishant B. (@dishb) <code.dishb@gmail.com>
#    and contributors.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

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
