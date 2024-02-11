from graphics import Window,Point,Line

class Cell:
    def __init__(self, first_point, second_point, window = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = first_point.x
        self._x2 = second_point.x
        self._y1 = first_point.y
        self._y2 = second_point.y
        self._win = window
        self._visited = False
    
    def draw(self):
        color = {True:"black",False:"white"}
        if self._win is None:
            return
        point_a = Point(self._x1, self._y1)
        point_b = Point(self._x1, self._y2)
        line_to_draw = Line(point_a, point_b)
        self._win.draw_line(line_to_draw,color[self.has_left_wall])

        point_a = Point(self._x2, self._y1)
        point_b = Point(self._x2, self._y2)
        line_to_draw = Line(point_a, point_b)
        self._win.draw_line(line_to_draw,color[self.has_right_wall])

        point_a = Point(self._x1, self._y1)
        point_b = Point(self._x2, self._y1)
        line_to_draw = Line(point_a, point_b)
        self._win.draw_line(line_to_draw,color[self.has_top_wall])

        point_a = Point(self._x1, self._y2)
        point_b = Point(self._x2, self._y2)
        line_to_draw = Line(point_a, point_b)
        self._win.draw_line(line_to_draw,color[self.has_bottom_wall])

        self._win.canvas.pack()

    def draw_move(self, to_cell, undo=False):
        mid_x1 = (self._x1 + self._x2) / 2
        mid_y1 = (self._y1 + self._y2) / 2
        mid_x2 = (to_cell._x1 + to_cell._x2) / 2
        mid_y2 = (to_cell._y1 + to_cell._y2) / 2
        if not undo:
            color = "red"

        else:
            color = "grey"
        point_a = Point(mid_x1, mid_y1)
        point_b = Point(mid_x2, mid_y2)
        line_to_draw = Line(point_a,point_b)
        self._win.draw_line(line_to_draw,color)
