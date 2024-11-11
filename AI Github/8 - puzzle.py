import heapq

class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.empty_tile = self.board.index(0)  # Find the index of the empty tile
        self.heuristic = self.calculate_heuristic()
        self.priority = self.moves + self.heuristic  # f(n) = g(n) + h(n)

    def calculate_heuristic(self):
        # Manhattan distance heuristic
        goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        distance = 0
        for i in range(9):
            if self.board[i] != 0:
                x, y = divmod(i, 3)
                gx, gy = divmod(goal.index(self.board[i]), 3)
                distance += abs(x - gx) + abs(y - gy)
        return distance

    def generate_next_states(self):
        moves = []
        x, y = divmod(self.empty_tile, 3)
        possible_moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

        for nx, ny in possible_moves:
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_empty_tile = nx * 3 + ny
                new_board = self.board[:]
                new_board[self.empty_tile], new_board[new_empty_tile] = new_board[new_empty_tile], new_board[self.empty_tile]
                moves.append(PuzzleState(new_board, self.moves + 1, self))
        return moves

    def is_goal(self):
        return self.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def __lt__(self, other):
        return self.priority < other.priority

def solve_puzzle(initial_board):
    start = PuzzleState(initial_board)
    if start.is_goal():
        return []

    open_list = []
    heapq.heappush(open_list, start)
    closed_set = set()

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.is_goal():
            path = []
            while current_state:
                path.append(current_state.board)
                current_state = current_state.previous
            return path[::-1]

        closed_set.add(tuple(current_state.board))

        for next_state in current_state.generate_next_states():
            if tuple(next_state.board) not in closed_set:
                heapq.heappush(open_list, next_state)

    return None  # No solution found

# Example usage
initial_board = [1, 2, 3, 4, 5, 6, 0, 7, 8]
solution_path = solve_puzzle(initial_board)

if solution_path:
    print("Solution found in", len(solution_path) - 1, "moves:")
    for step in solution_path:
        print(step[0:3])
        print(step[3:6])
        print(step[6:9])
        print()
else:
    print("No solution found.")

