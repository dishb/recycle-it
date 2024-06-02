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
