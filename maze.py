from graphics import Window,Point,Line
from cell import Cell
import time, random

class Maze:
    def __init__(self, x1,y1,num_rows,num_cols,cell_size_x,cell_size_y,win=None,seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        if seed is not None:
            random.seed(seed)
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self.num_rows):
            rows = []
            for j in range(self.num_cols):
                cell = self._draw_cells(i, j)
                rows.append(cell)
            self._cells.append(rows)
                

    def _draw_cells(self,i,j):
        y1 = self.y1 + (i * self.cell_size_y)
        x1 = self.x1 + (j * self.cell_size_x)
        y2 = (y1 + self.cell_size_y)
        x2 = (x1 + self.cell_size_x)
        cell = Cell(Point(x1,y1),Point(x2,y2),self.win)
        cell.draw()
        self._animate()
        return cell

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.02);

    def _break_entrance_and_exit(self):
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        entrance_cell.draw()
        exit_cell = self._cells[-1][-1]
        exit_cell.has_bottom_wall = False
        exit_cell.draw()
    
    def _break_walls_r(self,i,j):
        cur_cell = self._cells[i][j]
        cur_cell._visited = True
        while True:
            cells_to_visit = []
            directions = {"r": [0,1],"l": [0,-1],"u":[-1,0],"d":[1,0]}
            for dir,dir_cord in directions.items():
                n_i = i+dir_cord[0]
                n_j = j+dir_cord[1]
                if 0 <= n_i < self.num_rows and 0 <= n_j < self.num_cols:
                    if not self._cells[n_i][n_j]._visited:
                        cells_to_visit.append([n_i,n_j,dir])
            if len(cells_to_visit) == 0:
                cur_cell.draw() # This ensures that once we've finished traversing
                # The drawing of the current cell persists and isn't over written by 
                # the drawing "lower" in the traversal.
                return
            random_cell = random.choice(cells_to_visit)
            self._break_down_wall(cur_cell,random_cell[2])
            self._break_walls_r(random_cell[0],random_cell[1])

    def _break_down_wall(self, cell, wall):
        if wall == "r":
            cell.has_right_wall = False
        if wall == "l":
            cell.has_left_wall = False
        if wall == "u":
            cell.has_top_wall = False
        if wall == "d":
            cell.has_bottom_wall = False
        cell.draw()
        return
    
    def _reset_cells_visited(self):
        for cols in self._cells:
            for row in cols:
                row._visited = False

    def solve(self,i=0,j=0):
        return self._solve_r(i,j)

    def _solve_r(self,i,j):
        # DFS Solution, returns True if the current cell is an end cell. Else: False
        self._animate()
        cur_cell = self._cells[i][j]
        cur_cell._visited = True
        if cur_cell == self._cells[-1][-1]:
            return True
        else: 
            directions = {"r": [0,1],"l": [0,-1],"u":[-1,0],"d":[1,0]}
            for dir,co in directions.items():
                n_i = i+co[0]
                n_j = j+co[1]
                if 0 <= n_i < self.num_rows and 0 <= n_j < self.num_cols:
                    next_cell = self._cells[n_i][n_j]
                    if dir == "r" and not cur_cell.has_right_wall and not next_cell._visited:
                        cur_cell.draw_move(next_cell)
                        isSolution = self._solve_r(n_i,n_j)
                        if isSolution:
                            return True
                        cur_cell.draw_move(next_cell,undo=True)
                    if dir == "l" and not cur_cell.has_left_wall and not next_cell._visited:
                        cur_cell.draw_move(next_cell)
                        isSolution = self._solve_r(n_i,n_j)
                        if isSolution:
                            return True
                        cur_cell.draw_move(next_cell,undo=True)
                    if dir == "u" and not cur_cell.has_top_wall and not next_cell._visited:
                        cur_cell.draw_move(next_cell)
                        isSolution = self._solve_r(n_i,n_j)
                        if isSolution:
                            return True
                        cur_cell.draw_move(next_cell,undo=True)
                    if dir == "d" and not cur_cell.has_bottom_wall and not next_cell._visited:
                        cur_cell.draw_move(next_cell)
                        isSolution = self._solve_r(n_i,n_j)
                        if isSolution:
                            return True
                        cur_cell.draw_move(next_cell,undo=True)
            return False

