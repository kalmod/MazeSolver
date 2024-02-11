import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols
        )

    def test_maze_create_uneven(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 22, 8)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols
        )

    def test_maze_create_large(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 100, 100)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols
        )

    def test_maze_create_large(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 1, 1)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols
        )

    def test_visited_cells(self):
        num_cols = 13
        num_rows = 14
        m1 = Maze(0, 0, num_rows,num_cols,1 ,1)
        m1._reset_cells_visited()
        print(len(m1._cells), len(m1._cells[0]))
        for i in range(num_rows):
            for j in range(num_cols):
                if m1._cells[i][j]._visited:
                    assert False
        assert True

if __name__ == "__main__":
    unittest.main()
