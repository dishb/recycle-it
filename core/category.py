import customtkinter as ctk

from .const import FONT_SIZE

class CategoryLabel(ctk.CTkLabel):
    def __init__(self, master: ctk.CTk | ctk.CTkToplevel) -> None:
        """
        Displays the category of the trash.
        """

        super().__init__(master = master,
                         text = "Category:",
                         height = 38,
                         font = ("Roboto", FONT_SIZE)
                         )
