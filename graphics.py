from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self,width,height):
        self.width = width
        self.height = height

        self.__root = Tk()
        self.__root.title("Maze Game")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root, width=width, height=height)

        self.__canvas.pack(fill=BOTH, expand=True)
        self.__running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    def draw_line(self, line):
        self.__canvas.delete("all")
        line.draw(self.__canvas)
        self.__canvas.update()
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def draw(self, canvas):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill="black", width=2)