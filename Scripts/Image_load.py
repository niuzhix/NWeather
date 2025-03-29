from PIL import Image, ImageTk
from tkinter import Tk, PhotoImage

def load(master: Tk | None = None,image_file: str | bytes | None = None,size: tuple[int, int] | None = None) -> PhotoImage:
    global img_load, img
    img_load = Image.open(image_file)
    if not size is None:
        img_load.thumbnail(size)
    if not master is None:
        img = ImageTk.PhotoImage(img_load)
        return img
    else:
        return img_load