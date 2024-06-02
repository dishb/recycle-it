import customtkinter as ctk

from .const import PADX, PADY, STICKY, FONT_SIZE

class Preferences(ctk.CTkToplevel):
    def __init__(self,
                 master: ctk.CTk,
                 width: int,
                 height: int,
                 title: str,
                 resizable_x: bool | None = False,
                 resizable_y: bool | None = False,
                 ) -> None:
        """
        A basic window for user preferences. This is boilerplate code.
        """

        super().__init__()

        self.geometry(f"{width}x{height}")
        self.title(title)
        self.resizable(resizable_x, resizable_y)
        # self.minsize(int, int)

        self.master = master

        self.grid_rowconfigure(0, weight = 0)
        self.grid_rowconfigure(1, weight = 0)

        self.grid_columnconfigure(0, weight = 0)
        self.grid_columnconfigure(1, weight = 0)

        self.scale_label = ScaleLabel(self)
        self.scale_label.grid(row = 0,
                              column = 0,
                              padx = PADX,
                              pady = PADY,
                              sticky = STICKY
                              )

        self.scale_menu = ScaleMenu(self)
        self.scale_menu.grid(row = 0,
                             column = 1,
                             padx = PADX,
                             pady = PADY,
                             sticky = STICKY
                             )

        self.appearance_label = AppearanceLabel(self)
        self.appearance_label.grid(row = 1,
                                   column = 0,
                                   padx = PADX,
                                   pady = PADY,
                                   sticky = STICKY
                                   )

        self.appearance_menu = AppearanceMenu(self)
        self.appearance_menu.grid(row = 1,
                                  column = 1,
                                  padx = PADX,
                                  pady = PADY,
                                  sticky = STICKY
                                  )

class ScaleLabel(ctk.CTkLabel):
    def __init__(self,
                 master: ctk.CTk | ctk.CTkToplevel,
                 ) -> None:
        """
        A widget to explain the what the ScalingMenu is.
        """

        super().__init__(master = master,
                         text = "UI Scaling:",
                         font = ("Roboto", FONT_SIZE)
                         )

class ScaleMenu(ctk.CTkOptionMenu):
    def __init__(self,
                 master: ctk.CTk | ctk.CTkToplevel
                 ) -> None:
        """
        A widget to change the UI scale of the application.
        """

        self.options = ["80%", "90%", "100%", "110%", "120%"]

        super().__init__(master = master,
                         values = self.options,
                         command = self.scale_ui,
                         font = ("Roboto", FONT_SIZE)
                         )

        self.set("100%")

    def scale_ui(self, scale_percent: str) -> None:
        """
        Changes the UI scale of the application.
        """

        scale_float = int(scale_percent.replace("%", "")) / 100
        ctk.set_widget_scaling(scale_float)

class AppearanceLabel(ctk.CTkLabel):
    def __init__(self,
                 master: ctk.CTk | ctk.CTkToplevel
                 ) -> None:
        """
        A widget to explain what the AppearanceMenu is.
        """

        super().__init__(master = master,
                         text = "Appearance:",
                         font = ("Roboto", FONT_SIZE)
                         )

class AppearanceMenu(ctk.CTkOptionMenu):
    def __init__(self,
                 master: ctk.CTk | ctk.CTkToplevel
                 ) -> None:
        """
        A widget to change the appearance (dark, light modes) of the application.
        """

        self.options = ["System", "Light", "Dark"]

        super().__init__(master = master,
                         values = self.options,
                         command = self.change_appearance,
                         font = ("Roboto", FONT_SIZE)
                         )

    def change_appearance(self, new_appearance: str) -> None:
        """
        Changes the appearance mode of the application.
        """

        ctk.set_appearance_mode(new_appearance.lower())
