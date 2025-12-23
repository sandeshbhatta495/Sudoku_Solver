import pygame
import sys
import time

# ---------------- CONFIG ----------------
N = 4
SIZE = 500
CELL = SIZE // N
INFO = 80
HEIGHT = SIZE + INFO

# ---------------- COLORS ----------------
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (180,180,180)
YELLOW = (255,255,200)
RED = (255,120,120)
GREEN = (0,180,0)

# ---------------- STATS ----------------
current = {"cell": None, "backtrack": False}

# ---------------- VALID CHECK ----------------
def is_valid(board, r, c, num):
    for i in range(N):
        if board[r][i] == num or board[i][c] == num:
            return False

    sr = (r // 2) * 2
    sc = (c // 2) * 2
    for i in range(sr, sr + 2):
        for j in range(sc, sc + 2):
            if board[i][j] == num:
                return False
    return True

# ---------------- DRAW ----------------
def draw(screen, board):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 48)

    for r in range(N):
        for c in range(N):
            x, y = c * CELL, r * CELL

            if current["cell"] == (r, c):
                color = RED if current["backtrack"] else YELLOW
                pygame.draw.rect(screen, color, (x,y,CELL,CELL))

            pygame.draw.rect(screen, BLACK, (x,y,CELL,CELL), 1)

            if board[r][c] != 0:
                text = font.render(str(board[r][c]), True, GREEN)
                screen.blit(text, text.get_rect(center=(x+CELL//2,y+CELL//2)))

    # thick lines
    for i in range(N+1):
        t = 4 if i % 2 == 0 else 1
        pygame.draw.line(screen, BLACK, (0,i*CELL),(SIZE,i*CELL),t)
        pygame.draw.line(screen, BLACK, (i*CELL,0),(i*CELL,SIZE),t)

    pygame.display.update()

# ---------------- SOLVER ----------------
def solve(board, screen):
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit(); sys.exit()

                for num in range(1,5):
                    if is_valid(board, r, c, num):
                        board[r][c] = num
                        current["cell"] = (r,c)
                        current["backtrack"] = False
                        draw(screen, board)
                        time.sleep(0.2)

                        if solve(board, screen):
                            return True

                        board[r][c] = 0
                        current["backtrack"] = True
                        draw(screen, board)
                        time.sleep(0.2)
                return False
    return True

# ---------------- MAIN ----------------
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((SIZE, HEIGHT))
pygame.display.set_caption("4x4 Sudoku – Empty Board Visualization")

board = [[0]*N for _ in range(N)]

draw(screen, board)
time.sleep(2)

solve(board, screen)

# keep window open
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
