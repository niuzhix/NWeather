'''
@discription  : Copyright © 2021-2025 Blue Summer Studio. All rights reserved.
@Author       : Niu zhixin
@Date         : 2025-03-15 17:07:53
@LastEditTime : 2025-03-27 18:00:56
@LastEditors  : Niu zhixin
'''

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
from win11toast import ToastNotification
import gettext
from configparser import ConfigParser
import os
import json
from Scripts.get_weather import get_weather
from Scripts.createJWT import createJWT

try:
    with open(f'{os.getcwd()}\\Lib\\ed25519-private.pem',encoding='utf-8') as private_key_file:
        PRIVATE_KEY = private_key_file.read()
    PROJECT_ID = '29KVBFNRAX'
    KEY_ID = 'CHPN48PMNJ'
    JWT = createJWT(PRIVATE_KEY,PROJECT_ID,KEY_ID)
except Exception as e:
    print(e)
    Messagebox.show_error('资源文件丢失\n(-1).')
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


class NWeather:
    def __init__(self, master: ttk.Window | None):
        if not master is None:
            self.master = master

    def __window__(self):
        root = self.master
        main_page = ttk.Notebook(root)
        main_page.pack(fill=BOTH, expand=True)
        self.weather_page = ttk.Frame(main_page)
        self.__weather_pages__()
        self.weather_page.pack(fill=BOTH, expand=True)
        main_page.add(self.weather_page, text=_("天气(W)"))

    def __weather_pages__(self):
        page = self.weather_page
        self.city_choose = ttk.Entry(page)
        self.city_choose.grid(column=0,row=0,padx=10,pady=10)
        
        self.search = ttk.Button(page,bootstyle=(PRIMARY, "outline-button"),text='查询(S)',command=lambda:self.update_weather_data())
        self.search.grid(column=1,row=0,padx=10,pady=10)
        
        self.main_weather = ttk.Label(page,text='')
        self.main_weather.grid(column=0,row=1,padx=10,pady=10)
    
    def __settings_pages__(self):
        pass

    def update_weather_data(self):
        city = self.city_choose.get()
        


def main():
    root = ttk.Window(themename="darkly",title="NWeather",size=(400, 500),resizable=(False,False),alpha=0.95)
    app = NWeather(root)
    app.__window__()
    root.mainloop()

if __name__ == "__main__":
    main()
