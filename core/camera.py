from os import mkdir
from os.path import exists

import cv2
import customtkinter as ctk
from PIL import Image

from .ai import analyze_image
from .const import EWASTE, COMPOST, RECYCLE, TRASH, FONT_SIZE, IMG_PATH

class CaptureButton(ctk.CTkButton):
    def __init__(self, master: ctk.CTk | ctk.CTkToplevel) -> None:
        """
        Simple button prompting the user to take a picture.
        """

        super().__init__(master = master,
                         text = "Take picture 📸",
                         height = 38,
                         font = ("Roboto", FONT_SIZE)
                         )

class CameraView(ctk.CTkButton):
    def __init__(self, master: ctk.CTk | ctk.CTkToplevel) -> None:
        """
        Displays the user's camera feed.
        """

        super().__init__(master = master,
                         state = ctk.DISABLED,
                         fg_color = "transparent",
                         text = "",
                         font = ("Roboto", FONT_SIZE)
                         )

        self.photo_image = None
        self.category = ctk.StringVar(master, "")

        self.feed = cv2.VideoCapture(0) # pylint: disable=no-member
        self.configure(require_redraw = True, width = self.feed.get(3) * 0.75)
        self.configure(require_redraw = True, height = self.feed.get(4) * 0.75)

        self.open_camera()

    def save_image(self, api_key: str, client_id: str) -> None:
        """
        Saves a screenshot of the webcam view.
        """

        _, frame = self.feed.read()
        frame = cv2.flip(frame, 1) # pylint: disable=no-member
        opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) # pylint: disable=no-member
        image = Image.fromarray(opencv_image)

        if not exists(IMG_PATH.removesuffix("/object.png")):
            mkdir(IMG_PATH.removesuffix("/object.png"))

        if exists(IMG_PATH):
            mode = "wb"
        else:
            mode = "xb"

        with open(IMG_PATH, mode) as file:
            image.save(file, "PNG")
            file.close()

        material = analyze_image(IMG_PATH, api_key, client_id)
        if material != 429: # when rate limits are not exceeded
            material = material.capitalize()

            if material.lower() in RECYCLE:
                self.category.set(f"Material: {material}\nCategory: Recyclable ♻️")
            elif material.lower() in COMPOST:
                self.category.set(f"Material: {material}\nCategory: Compostable 🌿")
            elif material.lower() in EWASTE:
                self.category.set(f"Material: {material}\nCategory: E-Waste 🔌")
            elif material.lower() in TRASH:
                self.category.set(f"Material: {material}\nCategory: Trash 🗑️")
            else:
                self.category.set(f"Material: {material}\nCategory: Trash 🗑️")

    def open_camera(self) -> None:
        """
        Displays the computer's webcam's view on a button.
        """

        _, frame = self.feed.read()
        frame = cv2.flip(frame, 1) # pylint: disable=no-member
        opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) # pylint: disable=no-member

        image = Image.fromarray(opencv_image)

        self.photo_image = ctk.CTkImage(light_image = image,
                                        size = (self.cget("width"), self.cget("height"))
                                        )

        self.configure(image = self.photo_image, require_redraw = True)

        self.after(10, self.open_camera)
