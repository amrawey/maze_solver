from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    point_1 = Point(4,0)
    point_2 = Point(4,100)
    line = Line(point_1, point_2)
    win.draw_line(line)
    win.wait_for_close()

if __name__ == "__main__":
    main()