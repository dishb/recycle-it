import customtkinter as ctk

from .const import FONT_SIZE, SCRIPT_PATH

class Name(ctk.CTkLabel):
    def __init__(self, master: ctk.CTk | ctk.CTkToplevel) -> None:
        """
        The name of the application.
        """

        ctk.FontManager.load_font(f"{SCRIPT_PATH}/fonts/Roboto Bold.ttf")
        font = ctk.CTkFont(family = "Roboto Bold", size = FONT_SIZE + 30, weight = "bold")

        super().__init__(master = master,
                         font = font,
                         text = "Recycle IT",
                         text_color = "#2FA572"
                         )
