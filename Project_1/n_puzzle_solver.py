import heapq

def read_puzzle(): # Reads the puzzle configuration from a file.
    
    with open('n-puzzle.txt', 'r') as f:
        puzzle = []
        for line in f:
            row = list(map(int, line.strip().split()))
            puzzle.append(row)
    return puzzle

def find_blank(puzzle): # Finds the coordinates (row, column) of the blank space (0) in the puzzle.
    
    for r, row in enumerate(puzzle):
        for c, val in enumerate(row):
            if val == 0:
                return r, c

def calculate_manhattan_distance(puzzle, target): # Calculates the Manhattan distance heuristic for the given puzzle state.
    
    distance = 0
    n = len(puzzle)
    for r in range(n):
        for c in range(n):
            value = puzzle[r][c]
            if value != 0:  # Ignore the blank space
                target_r, target_c = divmod(value - 1, n)
                distance += abs(r - target_r) + abs(c - target_c)
    return distance

def generate_target_puzzle(n): # Generates the target puzzle configuration (tiles in order, blank in the bottom right).
    
    target = [[0] * n for _ in range(n)]
    num = 1
    
    for r in range(n):
        for c in range(n):
            if num <= n * n - 1:
                target[r][c] = num
                num += 1
            else:
                
                target[r][c] = 0
    return target

def get_neighbors(puzzle): # Generates possible neighbor puzzle states by moving the blank space.
    
    n = len(puzzle)
    r0, c0 = find_blank(puzzle) # Find the row and column of the blank space
    neighbors = []
    
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)] # possible moves (right, left, down, up)
    # Iterate through possible moves
    for dr, dc in moves:
        # Calculate the new row and column for the blank space
        nr, nc = r0 + dr, c0 + dc
        # Check if the new position is within the bounds of the puzzle
        if 0 <= nr < n and 0 <= nc < n:
            # Create a copy of the puzzle to avoid modifying the original
            neighbor_puzzle = [row[:] for row in puzzle]
            # Swap the blank space with the tile at the new position
            neighbor_puzzle[r0][c0], neighbor_puzzle[nr][nc] = neighbor_puzzle[nr][nc], neighbor_puzzle[r0][c0]
            # Add the new puzzle state to the list of neighbors
            neighbors.append(neighbor_puzzle)
    return neighbors

def solve_n_puzzle(start_puzzle, target): # Solves the N-puzzle using A* search.
    
    # Create the initial node: (f, h, puzzle, path)
    start_node = (0, calculate_manhattan_distance(start_puzzle, target), start_puzzle, [])
    # Initialize the priority queue with the start node
    priority_queue = [start_node]
    # Initialize the visited set to keep track of visited states
    visited = set()

    # While there are nodes in the priority queue
    while priority_queue:
        # Get the node with the lowest f value from the priority queue
        f, h, current_puzzle, path = heapq.heappop(priority_queue)

        # If the current puzzle is the target puzzle, return the path
        if current_puzzle == target:
            return path

        # Convert the puzzle to a tuple so it can be added to the visited set
        puzzle_tuple = tuple(tuple(row) for row in current_puzzle)
        # If the puzzle has already been visited, skip it
        if puzzle_tuple in visited:
            continue

        # Add the current puzzle to the visited set
        visited.add(puzzle_tuple)

        # Generate the neighbors of the current puzzle
        for neighbor in get_neighbors(current_puzzle):
            # Calculate g (the cost from the start to the neighbor)
            g = len(path) + 1
            # Calculate h (the heuristic estimate from the neighbor to the target)
            h = calculate_manhattan_distance(neighbor, target)
            # Calculate f (the total estimated cost)
            new_f = g + h
            # Create a new node for the neighbor
            new_node = (new_f, h, neighbor, path + [neighbor])
            # Add the neighbor to the priority queue
            heapq.heappush(priority_queue, new_node)

    # If no solution is found, return None
    return None

def print_puzzle(puzzle):  # Prints the puzzle configuration
   
    for row in puzzle:
        print('\t'.join(map(str, row)))

if __name__ == "__main__":
    
    start_puzzle = read_puzzle()
    n = len(start_puzzle)
    target_puzzle = generate_target_puzzle(n)
    solution_path = solve_n_puzzle(start_puzzle, target_puzzle)

    if solution_path:
        print("Solution found:")
        print("Initial Puzzle:")
        print_puzzle(start_puzzle)

        for step_number, puzzle in enumerate(solution_path):
            print(f"\nStep: {step_number + 1}")
            print_puzzle(puzzle)

    else:
        print("No solution found.")