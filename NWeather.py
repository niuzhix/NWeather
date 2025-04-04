"""
@discription  : Copyright © 2021-2025 Blue Summer Studio. All rights reserved.
@Author       : Niu zhixin
@Date         : 2025-03-15 17:07:53
@LastEditTime : 2025-03-29 07:15:41
@LastEditors  : Niu zhixin
"""

from tkinter import Tk, Entry, Button
from win11toast import ToastNotification
from tkinter import messagebox
import gettext
from configparser import ConfigParser
import os
from Scripts.get_weather import get_weather, get_city_data
from Scripts.createJWT import createJWT
from Scripts.Image_load import load
from Scripts.Canvas import RoundCanvas as Canvas
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(2)

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
        city_inputs_bg = menu.create_round_rect(
            24, 75, 376, 125, fill="#333333"
        )
        menu.create_image(
            40,
            100,
            anchor="w",
            image=load(self.master, f"{os.getcwd()}\\Lib\\search.png", (20, 20)),
        )
        self.city_inputs = Entry(menu, relief='flat',font=FONT,bg='#333333',fg='#ffffff',validate='key',validatecommand=lambda:self.update_city_data())
        self.city_inputs.place(x=61,y=100,anchor='w')
        
        
        self.weatherButton = menu.create_round_rect(
            10, 140, 389, 200, radius=10, fill="#0b4a9b"
        )
        self.settingButton = menu.create_round_rect(
            10, 211, 389, 271, radius=10, fill="#131313"
        )
        self.aboutButton = menu.create_round_rect(
            10, 282, 389, 342, radius=10, fill="#131313"
        )
        menu.create_text(
            20, 170, text=_("天气预报"), anchor="w", font=FONT, fill="#ffffff"
        )
        menu.create_text(
            20, 241, text=_("应用设置"), anchor="w", font=FONT, fill="#ffffff"
        )
        menu.create_text(
            20, 312, text=_("关于应用"), anchor="w", font=FONT, fill="#ffffff"
        )
        
        self.city_show = menu.create_round_rect(24,135,376,535,radius=10,fill="#4c545a",state="hidden")
    
        menu.bind("<Button-1>", self.on_menu_click)
        menu.bind()

    def __weather_pages__(self):
        pass

    def __settings_pages__(self):
        pass

    def on_menu_click(self, events):
        if 140 < events.y < 200:
            self.menuFocus = "weather"
            self.cmenu.set(self.weatherButton, fill="#0b4a9b")
            self.cmenu.set(self.settingButton, fill="#131313")
            self.cmenu.set(self.aboutButton, fill="#131313")
        elif 211 < events.y < 271:
            self.menuFocus = "setting"
            self.cmenu.set(self.weatherButton, fill="#131313")
            self.cmenu.set(self.settingButton, fill="#0b4a9b")
            self.cmenu.set(self.aboutButton, fill="#131313")
        elif 282 < events.y < 342:
            self.menuFocus = "about"
            self.cmenu.set(self.weatherButton, fill="#131313")
            self.cmenu.set(self.settingButton, fill="#131313")
            self.cmenu.set(self.aboutButton, fill="#0b4a9b")

    def update_weather_data(self):
        city = self.city_choose.get()
    
    def update_city_data(self):
        city_input = self.city_inputs.get()
        city_list = get_city_data(city_input)
        print(city_list)


def main():
    root = Tk()
    app = NWeather(root)
    app.__window__()
    root.mainloop()


if __name__ == "__main__":
    main()
