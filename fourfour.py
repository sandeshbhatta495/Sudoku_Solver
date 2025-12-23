# 4x4 Sudoku Solver using Backtracking with Pygame Visualization

import pygame
import sys

# ---------------- CONFIG ----------------
N = 4
WINDOW_SIZE = 500
CELL_SIZE = WINDOW_SIZE // N
FPS = 60
INFO_HEIGHT = 100
TOTAL_HEIGHT = WINDOW_SIZE + INFO_HEIGHT

# ---------------- COLORS ----------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
LIGHT_GRAY = (240, 240, 240)
LIGHT_YELLOW = (255, 255, 200)
RED = (255, 100, 100)
GREEN = (0, 180, 0)

# ---------------- STATS ----------------
stats = {
    'attempts': 0,
    'backtracks': 0,
    'current_cell': None,
    'current_num': None,
    'is_backtrack': False
}

# ---------------- VALIDITY CHECK ----------------
def is_valid(board, row, col, num):
    # Row
    for j in range(N):
        if board[row][j] == num:
            return False

    # Column
    for i in range(N):
        if board[i][col] == num:
            return False

    # Subgrid (2x2)
    start_row = (row // 2) * 2
    start_col = (col // 2) * 2

    for i in range(start_row, start_row + 2):
        for j in range(start_col, start_col + 2):
            if board[i][j] == num:
                return False

    return True

# ---------------- SOLVER ----------------
def solve(board, screen, clock, initial_board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:

                # Handle quit events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                for num in range(1, 5):
                    stats['attempts'] += 1
                    stats['current_cell'] = (i, j)
                    stats['current_num'] = num
                    stats['is_backtrack'] = False

                    if is_valid(board, i, j, num):
                        board[i][j] = num

                        draw_board(screen, board, initial_board)
                        pygame.display.update()
                        clock.tick(10)

                        if solve(board, screen, clock, initial_board):
                            return True

                        # Backtrack
                        board[i][j] = 0
                        stats['backtracks'] += 1
                        stats['is_backtrack'] = True

                return False
    return True

# ---------------- DRAW BOARD ----------------
def draw_board(screen, board, initial_board):
    screen.fill(WHITE)

    font = pygame.font.Font(None, 48)
    info_font = pygame.font.Font(None, 20)

    # Cells
    for i in range(N):
        for j in range(N):
            x, y = j * CELL_SIZE, i * CELL_SIZE

            if stats['current_cell'] == (i, j):
                color = RED if stats['is_backtrack'] else LIGHT_YELLOW
                pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))

            pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)

            if board[i][j] != 0:
                color = BLACK if initial_board[i][j] != 0 else GREEN
                text = font.render(str(board[i][j]), True, color)
                screen.blit(text, text.get_rect(center=(x + CELL_SIZE//2, y + CELL_SIZE//2)))

    # Thick grid lines
    for i in range(0, N + 1):
        thickness = 4 if i % 2 == 0 else 1
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (WINDOW_SIZE, i * CELL_SIZE), thickness)
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_SIZE), thickness)

    # Info panel
    pygame.draw.rect(screen, LIGHT_GRAY, (0, WINDOW_SIZE, WINDOW_SIZE, INFO_HEIGHT))
    screen.blit(info_font.render(f"Attempts: {stats['attempts']}", True, BLACK), (10, WINDOW_SIZE + 10))
    screen.blit(info_font.render(f"Backtracks: {stats['backtracks']}", True, BLACK), (10, WINDOW_SIZE + 40))

# ---------------- MAIN ----------------
board = [
    [1, 0, 0, 4],
    [0, 0, 3, 0],
    [0, 3, 0, 0],
    [2, 0, 0, 1]
]

initial_board = [row[:] for row in board]

pygame.init()
pygame.font.init()   # ✅ REQUIRED FIX
screen = pygame.display.set_mode((WINDOW_SIZE, TOTAL_HEIGHT))
pygame.display.set_caption("4x4 Sudoku Solver Visualization")
clock = pygame.time.Clock()

draw_board(screen, board, initial_board)
pygame.display.update()
pygame.time.wait(1500)

solve(board, screen, clock, initial_board)

draw_board(screen, board, initial_board)
pygame.display.update()

# Keep window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(30)

pygame.quit()
