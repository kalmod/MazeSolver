from graphics import Window,Point,Line
from cell import Cell
from maze import Maze
       
def main():
    win = Window(800,600)

    a = Point(10,10)
    b = Point(100,100)
    c = Point(110,10)
    d = Point(200,100)
 #   line_to_draw = Line(a,b)

 #   win.draw_line(line_to_draw,"red")


    # box = Cell(win,a,b)
    # box.draw()
    #
    # box2 = Cell(win,c,d)
    # box2.draw()
    #
    # box2.draw_move(box,True)

    maze = Maze(10,10,15,15,25,25,win,0)
    maze.solve()
    win.wait_for_close()

main();
