import unittest
import n_puzzle_solver  

class TestNPuzzle(unittest.TestCase):

    def test_read_puzzle(self):
        
        with open("test_puzzle.txt", "w") as f:
            f.write("1\t2\t3\t4\t5\n")
            f.write("12\t6\t7\t9\t10\n")
            f.write("13\t17\t8\t23\t14\n")
            f.write("11\t18\t22\t15\t0\n")
            f.write("16\t21\t24\t19\t20\n")
        
        puzzle = n_puzzle_solver.read_puzzle()
        self.assertEqual(puzzle, [[1, 2, 3, 4 ,5], [12, 6, 7, 9, 10], [13, 17, 8, 23, 14],[11, 18, 22, 15, 0],[16, 21, 24, 19, 20]])

    def test_find_blank(self):
        puzzle = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
        r, c = n_puzzle_solver.find_blank(puzzle)
        self.assertEqual(r, 1)
        self.assertEqual(c, 1)

    def test_calculate_manhattan_distance(self):
        puzzle = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
        target = n_puzzle_solver.generate_target_puzzle(3)
        distance = n_puzzle_solver.calculate_manhattan_distance(puzzle, target)
        self.assertEqual(distance, 2)  # Expected Manhattan distance for this example

    def test_get_neighbors(self):
        puzzle = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
        neighbors = n_puzzle_solver.get_neighbors(puzzle)
        self.assertEqual(len(neighbors), 4)  # 4 possible moves
    
    def test_solve_puzzle(self):
        start_puzzle = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
        target = n_puzzle_solver.generate_target_puzzle(3)
        solution = n_puzzle_solver.solve_n_puzzle(start_puzzle, target)
        self.assertIsNotNone(solution)
        
        
        #Test a unsolvable puzzle.
        unsolvable_puzzle = [[8, 1, 2], [0, 4, 3], [7, 6, 5]]  
        solution = n_puzzle_solver.solve_n_puzzle(unsolvable_puzzle, n_puzzle_solver.generate_target_puzzle(3))
        self.assertIsNone(solution)
        
        
        #Test already solved
        solved_puzzle = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        solution = n_puzzle_solver.solve_n_puzzle(solved_puzzle, n_puzzle_solver.generate_target_puzzle(3))
        self.assertEqual(solution, [])  # Should return an empty path because already solved


if __name__ == '__main__':
    unittest.main()