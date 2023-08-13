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

import requests

def upload_store(image_path: str, client_id: str) -> str:
    """
    Uploads the image to Imgur, giving us a URL.
    """

    url = "https://api.imgur.com/3/image"
    headers = {"Authorization": f"Client-ID {client_id}"}

    with open(image_path, "rb") as file:
        response = requests.post(url, headers = headers, files = {"image": file})

    data = response.json()
    image_url = data["data"]["link"]

    return str(image_url)
