"""
@discription  : Copyright © 2021-2025 Blue Summer Studio. All rights reserved.
@Author       : Niu zhixin
@Date         : 2025-03-15 17:07:53
@LastEditTime : 2025-03-29 07:15:41
@LastEditors  : Niu zhixin
"""

from tkinter import Tk, Canvas
from win11toast import ToastNotification
from tkinter import messagebox
import gettext
from configparser import ConfigParser
import os
from Scripts.get_weather import get_weather, get_city
from Scripts.createJWT import createJWT
from Scripts.Image_load import load
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(2)

try:
    with open(
        f"{os.getcwd()}\\Lib\\ed25519-private.pem", encoding="utf-8"
    ) as private_key_file:
        PRIVATE_KEY = private_key_file.read()
    PROJECT_ID = "29KVBFNRAX"
    KEY_ID = "CHPN48PMNJ"
    JWT = createJWT(PRIVATE_KEY, PROJECT_ID, KEY_ID)
except Exception as e:
    os._exit(-1)

try:
    ini_cursor = ConfigParser()
    ini_cursor.read(f"{os.getcwd()}\\Lib\\config.ini", encoding="gb2312")
    LANG = ini_cursor.get("Settings", "language")
    if LANG == "English":
        lang = gettext.translation("en", localedir="locales", languages=["en"])
        lang.install()
        _ = lang.gettext
    else:

        def _(message: str) -> str:
            return message

except:

    def _(message: str) -> str:
        return message


FONT = ("LXGW WenKai GB Screen", 13)


class NWeather:
    def __init__(self, master: Tk | None):
        if not master is None:
            self.master = master

    def __window__(self):
        root = self.master
        root.resizable(False, False)
        root.title("NWeather")
        root.geometry("1500x800")

        self.menuFocus = "weather"

        self.cmenu = Canvas(root, background="#131313", width=400, highlightthickness=0)
        self.cmenu.pack(fill="y", side="left")
        self.__menu_page__()
        self.__weather_pages__()

    def __menu_page__(self):
        menu = self.cmenu
        city_inputs_left_round = menu.create_arc(
            20, 75, 70, 125, start=90, extent=180, fill="#333333", outline="#333333"
        )
        city_inputs_bg = menu.create_rectangle(
            44, 75, 356, 125, fill="#333333", outline="#333333"
        )
        city_inputs_right_round = menu.create_arc(
            330, 75, 380, 125, start=-90, extent=180, fill="#333333", outline="#333333"
        )
        menu.create_image(
            60,
            100,
            anchor="w",
            image=load(self.master, f"{os.getcwd()}\\Lib\\search.png", (30, 30)),
        )
        city_inputs = menu.create_text(
            100, 100, anchor="w", text="输入以查找城市...", font=FONT, fill="#d0d0d0"
        )

        self.weatherButton = menu.create_rectangle(
            0, 140, 399, 200, fill="#0b4a9b", outline="#0b4a9b"
        )
        self.settingButton = menu.create_rectangle(
            0, 201, 399, 261, fill="#131313", outline="#131313"
        )
        self.aboutButton = menu.create_rectangle(
            0, 262, 399, 322, fill="#131313", outline="#131313"
        )
        menu.create_text(
            30, 170, text=_("天气预报"), anchor="w", font=FONT, fill="#ffffff"
        )
        menu.create_text(
            20, 231, text=_("应用设置"), anchor="w", font=FONT, fill="#ffffff"
        )
        menu.create_text(
            20, 292, text=_("关于应用"), anchor="w", font=FONT, fill="#ffffff"
        )
        menu.bind("<Button-1>", self.on_menu_click)

    def __weather_pages__(self):
        pass

    def __settings_pages__(self):
        pass

    def on_menu_click(self, events):
        if 140 < events.y < 200:
            self.menuFocus = "weather"
            self.cmenu.itemconfig(self.weatherButton, fill="#0b4a9b", outline="#0b4a9b")
            self.cmenu.itemconfig(self.settingButton, fill="#131313", outline="#131313")
            self.cmenu.itemconfig(self.aboutButton, fill="#131313", outline="#131313")
        elif 201 < events.y < 261:
            self.menuFocus = "setting"
            self.cmenu.itemconfig(self.weatherButton, fill="#131313", outline="#131313")
            self.cmenu.itemconfig(self.settingButton, fill="#0b4a9b", outline="#0b4a9b")
            self.cmenu.itemconfig(self.aboutButton, fill="#131313", outline="#131313")
        elif 262 < events.y < 322:
            self.menuFocus = "about"
            self.cmenu.itemconfig(self.weatherButton, fill="#131313", outline="#131313")
            self.cmenu.itemconfig(self.settingButton, fill="#131313", outline="#131313")
            self.cmenu.itemconfig(self.aboutButton, fill="#0b4a9b", outline="#0b4a9b")

    def update_weather_data(self):
        city = self.city_choose.get()


def main():
    root = Tk()
    app = NWeather(root)
    app.__window__()
    root.mainloop()


if __name__ == "__main__":
    main()
