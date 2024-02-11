from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self,width,height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root,bg="white",height=height,width=width)
        self.canvas.pack(fill=BOTH,expand=1)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW",self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas,fill_color)


class Point:
    def __init__(self, x_cord, y_cord):
        self.x = x_cord
        self.y = y_cord

class Line:
    def __init__(self, first_point, second_point):
        self.point1 = first_point
        self.point2 = second_point

    def draw(self, canvas_ele, fill_color):
        # fill_color is a string
        canvas_ele.create_line(
            self.point1.x, self.point1.y,
            self.point2.x, self.point2.y,
            fill= fill_color, width = 2
        )
        canvas_ele.pack()


