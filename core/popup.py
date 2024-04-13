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
