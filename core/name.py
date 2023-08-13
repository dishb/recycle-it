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
