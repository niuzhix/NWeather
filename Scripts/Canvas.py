import tkinter

class RoundCanvas(tkinter.Canvas):
    def create_round_rect(self, x0, y0, x1, y1, radius=25, **kwargs):
        fill_color = kwargs.get('fill', '')
        outline_color = fill_color

        rect_objects = []

        # 绘制四个圆角
        rect_objects.append(self.create_arc(x0, y0, x0 + 2 * radius, y0 + 2 * radius, start=90, extent=90, style=tkinter.CHORD, outline=outline_color, fill=fill_color))
        rect_objects.append(self.create_arc(x1 - 2 * radius, y0, x1, y0 + 2 * radius, start=0, extent=90, style=tkinter.CHORD, outline=outline_color, fill=fill_color))
        rect_objects.append(self.create_arc(x0, y1 - 2 * radius, x0 + 2 * radius, y1, start=180, extent=90, style=tkinter.CHORD, outline=outline_color, fill=fill_color))
        rect_objects.append(self.create_arc(x1 - 2 * radius, y1 - 2 * radius, x1, y1, start=270, extent=90, style=tkinter.CHORD, outline=outline_color, fill=fill_color))

        # 如果有填充颜色，绘制一个填充多边形覆盖中间部分
        if fill_color:
            points = [
                x0 + radius, y0,
                x1 - radius, y0,
                x1, y0 + radius,
                x1, y1 - radius,
                x1 - radius, y1,
                x0 + radius, y1,
                x0, y1 - radius,
                x0, y0 + radius
            ]
            rect_objects.append(self.create_polygon(points, fill=fill_color, outline=outline_color))

        return rect_objects

    def set(self, rect:list, fill=None, **kwargs):
        for obj in rect:
            if fill is not None:
                self.itemconfig(obj, fill=fill, outline=fill, **kwargs)