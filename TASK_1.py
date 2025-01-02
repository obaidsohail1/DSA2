import random

# 1a. Save the chessboard (8x8) into an appropriate variable/data structure and display it in your terminal.
def create_chessboard():
    return [[-1 for _ in range(8)] for _ in range(8)]

def print_chessboard(board):
    for row in board:
        print(' '.join(f"{cell:2}" for cell in row))
    print()

# Helper Functions
def is_valid_move(board, x, y):
    return 0 <= x < 8 and 0 <= y < 8 and board[x][y] == -1

def get_knight_moves():
    return [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

# 1bi. Las Vegas Algorithm with stop conditions (success/failure).
def las_vegas_knights_tour(board, x, y, closed):
    moves = get_knight_moves()
    move_count = 1
    board[x][y] = 0

    while move_count < 64:
        valid_moves = [(x + dx, y + dy) for dx, dy in moves if is_valid_move(board, x + dx, y + dy)]
        if not valid_moves:
            return False

        next_x, next_y = random.choice(valid_moves)
        board[next_x][next_y] = move_count
        x, y = next_x, next_y
        move_count += 1

    if closed:
        return any((x + dx == 0 and y + dy == 0) for dx, dy in moves)
    return True

# 1bii. Backtracking Algorithm with Warnsdorff's Heuristic.
def warnsdorff_sort(board, x, y, moves):
    def count_onward_moves(x, y):
        return sum(1 for dx, dy in moves if is_valid_move(board, x + dx, y + dy))

    valid_moves = [(x + dx, y + dy) for dx, dy in moves if is_valid_move(board, x + dx, y + dy)]
    return sorted(valid_moves, key=lambda pos: count_onward_moves(pos[0], pos[1]))

def backtracking_knights_tour(board, x, y, move_count, moves, closed):
    if move_count == 64:
        if closed:
            return any((x + dx == 0 and y + dy == 0) for dx, dy in moves)
        return True

    sorted_moves = warnsdorff_sort(board, x, y, moves)
    for next_x, next_y in sorted_moves:
        board[next_x][next_y] = move_count
        if backtracking_knights_tour(board, next_x, next_y, move_count + 1, moves, closed):
            return True
        board[next_x][next_y] = -1

    return False

# 1c. Simulate Success Rate
def simulate_knights_tour(algorithm, closed, runs):
    success_count = 0

    for _ in range(runs):
        chessboard = create_chessboard()
        if algorithm == "backtracking":
            chessboard[0][0] = 0
            success = backtracking_knights_tour(chessboard, 0, 0, 1, get_knight_moves(), closed)
        else:
            success = las_vegas_knights_tour(chessboard, 0, 0, closed)

        if success:
            success_count += 1

    return success_count / runs

# 1d. Visualize All Visited Squares Regardless of Success
def visualize_tour_result(board, success):
    print("Final Chessboard:")
    print_chessboard(board)
    if success:
        print("The knight's tour was successful!")
    else:
        print("The knight's tour failed!")

# Main Program
def main():
    # Ask user for tour type (Open/Closed) and algorithm choice
    chessboard = create_chessboard()
    print("Initial Chessboard:")
    print_chessboard(chessboard)

    tour_type = input("Choose the tour type (Open/Closed): ").strip().lower()
    while tour_type not in ["open", "closed"]:
        print("Invalid input. Please choose either 'Open' or 'Closed'.")
        tour_type = input("Choose the tour type (Open/Closed): ").strip().lower()

    algorithm = input("Choose the algorithm (Backtracking/Las Vegas): ").strip().lower()
    while algorithm not in ["backtracking", "las vegas"]:
        print("Invalid input. Please choose either 'Backtracking' or 'Las Vegas'.")
        algorithm = input("Choose the algorithm (Backtracking/Las Vegas): ").strip().lower()

    closed = tour_type == "closed"

    # Simulate for success rate
    runs = 10000
    success_rate = simulate_knights_tour(algorithm, closed, runs)

    # Execute one run to display result
    chessboard = create_chessboard()
    if algorithm == "backtracking":
        chessboard[0][0] = 0
        success = backtracking_knights_tour(chessboard, 0, 0, 1, get_knight_moves(), closed)
    else:
        success = las_vegas_knights_tour(chessboard, 0, 0, closed)

    visualize_tour_result(chessboard, success)
    print(f"Success Rate after {runs} runs: {success_rate * 100:.2f}%")

if __name__ == "__main__":
    main()
