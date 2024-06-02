import customtkinter as ctk

from .const import FONT_SIZE, PADX, PADY

class Popup(ctk.CTkToplevel):
    def __init__(self,
                 width: int,
                 height: int,
                 title: str,
                 message: str,
                 resizable_x: bool | None = True,
                 resizable_y: bool | None = True
                 ) -> None:
        """
        A popup window displaying a error or message.
        """

        super().__init__()

        self.geometry(f"{width}x{height}")
        self.title(title)
        self.resizable(resizable_x, resizable_y)

        self.grid_rowconfigure(0, weight = 1)

        self.grid_columnconfigure(0, weight = 1)

        self.label = ctk.CTkLabel(self,
                                  text = message,
                                  font = ("Roboto", FONT_SIZE)
                                  )
        self.label.grid(row = 0,
                        column = 0,
                        padx = PADX,
                        pady = PADY,
                        sticky = "nsew"
                        )

class APIKeyDialog(ctk.CTkInputDialog):
    def __init__(self,
                 width: int,
                 height: int,
                 title: str,
                 message: str,
                 resizable_x: bool | None = True,
                 resizable_y: bool | None = True
                 ) -> None:
        """
        A popup window asking the user to input their API keys.
        """

        super().__init__(text = message)

        self.geometry(f"{width}x{height}")
        self.title(title)
        self.resizable(resizable_x, resizable_y)
