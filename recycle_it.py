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

from os import mkdir
from os.path import exists

import customtkinter as ctk

from core import *

class App(ctk.CTk):
    def __init__(self,
                 width: int,
                 height: int,
                 title: str,
                 resizable_x: bool | None = True,
                 resizable_y: bool | None = True
                 ) -> None:
        """
        The main application class. Simply create an instance and call the ".mainloop()" method.
        """

        super().__init__()

        self.geometry(f"{width}x{height}")
        self.title(title)
        self.resizable(resizable_x, resizable_y)

        ctk.FontManager.load_font("Roboto")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme(f"{SCRIPT_PATH}/themes/default.json")

        self.grid_rowconfigure(0, weight = 0)
        self.grid_rowconfigure(1, weight = 1)
        self.grid_rowconfigure(2, weight = 0)
        self.grid_rowconfigure(3, weight = 0)

        self.grid_columnconfigure(0, weight = 1)

        self.preferences = None
        self.id_popup = None
        self.key_popup = None

        self.recicl_key = None
        self.imgur_key = None

        self.name = Name(self)
        self.name.grid(row = 0,
                       column = 0,
                       padx = PADX,
                       pady = PADY,
                       sticky = STICKY
                       )

        self.camera_view = CameraView(self)
        self.camera_view.grid(row = 1,
                              column = 0,
                              padx = PADX,
                              pady = PADY,
                              sticky = STICKY
                              )

        self.capture_button = CaptureButton(self)
        self.capture_button.grid(row = 2,
                                 column = 0,
                                 padx = PADX,
                                 pady = PADY,
                                 sticky = STICKY
                                 )
        self.capture_button.configure(command = lambda:
                                                self.camera_view.save_image(self.recicl_key,
                                                                            self.imgur_key
                                                                            )
                                      )

        self.category_label = CategoryLabel(self)
        self.category_label.grid(row = 3,
                                 column = 0,
                                 padx = PADX,
                                 pady = PADY,
                                 sticky = STICKY
                                 )

        self.camera_view.category.trace_add("write", self.update_label)

        self.get_keys()

    def update_label(self, *args) -> None: # pylint: disable=unused-argument
        """
        Updates a label to the correct category.
        """

        self.category_label.configure(require_redraw = True,
                                      text = self.camera_view.category.get()
                                      )

    def open_preferences(self) -> None:
        """
        Creates a secondary window for user preferences
        """

        self.preferences = Preferences(self, 500, 400, "Preferences", False, False)

    def get_keys(self) -> None:
        """
        Gets the API keys from a file.
        """

        try:
            with open(f"{SCRIPT_PATH}/keys/recicl.key", "r", encoding = "utf-8") as file:
                contents = file.read()
                if contents == "" or contents is None:
                    raise FileNotFoundError

                self.recicl_key = contents
                file.close()

        except FileNotFoundError:
            self.key_popup = APIKeyDialog(300,
                                   200,
                                   "Error: Missing API key",
                                   "Please enter your RapidAPI key:",
                                   False,
                                   False
                                   )
            self.recicl_key = self.key_popup.get_input()
            if not exists(f"{SCRIPT_PATH}/keys/"):
                mkdir(f"{SCRIPT_PATH}/keys/")
            with open(f"{SCRIPT_PATH}/keys/recicl.key", "x", encoding = "utf-8") as file:
                file.write(self.recicl_key)
                file.close()

        try:
            with open(f"{SCRIPT_PATH}/keys/imgur.key", "r", encoding = "utf-8") as file:
                contents = file.read()
                if contents == "" or contents is None:
                    raise FileNotFoundError

                self.imgur_key = contents
                file.close()

        except FileNotFoundError:
            self.id_popup = APIKeyDialog(300,
                                  200,
                                  "Error: Missing Client-ID",
                                  "Please enter your Imgur Client-ID:",
                                  False,
                                  False
                                  )
            self.imgur_key = self.id_popup.get_input()
            if not exists(f"{SCRIPT_PATH}/keys/"):
                mkdir(f"{SCRIPT_PATH}/keys/")
            with open(f"{SCRIPT_PATH}/keys/imgur.key", "x", encoding = "utf-8") as file:
                file.write(self.imgur_key)
                file.close()

if __name__ == "__main__":
    app = App(1000, 720, "Recycle IT", False, False)
    app.mainloop()
