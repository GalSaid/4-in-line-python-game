import pygame
from audio import *
import sys
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ROW_COUNT = 6
COL_COUNT = 7
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 7)
WIDTH = COL_COUNT * SQUARESIZE
HEIGHT = (ROW_COUNT + 1) * SQUARESIZE


def initial_screen(screen):
    """
    This function shows the initial screen where you choose how many players there are.
    :param: A screen where we will add the appropriate view
    """
    pygame.draw.rect(screen, WHITE, (SQUARESIZE * 2, SQUARESIZE * 2, SQUARESIZE * 3, SQUARESIZE - 20))
    font = pygame.font.SysFont("monospace", 50, True)
    label1 = font.render("2 players", 1, BLACK)
    screen.blit(label1, (SQUARESIZE * 2 + 10, SQUARESIZE * 2))
    pygame.draw.rect(screen, WHITE, (SQUARESIZE * 2, SQUARESIZE * 3, SQUARESIZE * 3, SQUARESIZE - 20))
    label2 = font.render("1 player", 1, BLACK)
    screen.blit(label2, (SQUARESIZE * 2 + 10, SQUARESIZE * 3))


def selection_game():
    """
    This function responds to a button press by the user, choosing which game to play. Against the computer or two
    players, one against the other.
    :param: None
    :return: the choice: 1 -> against the computer, 2->one against the other.
    :rtype: integer
    """
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                posy = event.pos[1]
                if SQUARESIZE * 2 <= posx <= SQUARESIZE * 2 + SQUARESIZE * 3 and SQUARESIZE * 2 <= posy <= SQUARESIZE * 2 + SQUARESIZE - 20:
                    return 2
                    done = True
                elif SQUARESIZE * 2 <= posx <= SQUARESIZE * 2 + SQUARESIZE * 3 and SQUARESIZE * 3 <= posy <= SQUARESIZE * 3 + SQUARESIZE - 20:
                    return 1
                    done = True
                else:
                    done = False


def draw_board(screen):
    # The initial display of the start board.
    for r in range(ROW_COUNT):
        for c in range(COL_COUNT):
            # Each cube in the board is painted blue and has a black circle inside that forms the full board
            pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE + SQUARESIZE/2)), RADIUS)


def draw_board_after_drop(screen, board, r, c):
    # update the display after the player drops to location (r,c), fill the empty circle with the appropriate color
    if board[r][c] == 1:
        pygame.draw.circle(screen, RED, (int(c * SQUARESIZE + SQUARESIZE / 2), int((ROW_COUNT-1-r) * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    if board[r][c] == 2:
        pygame.draw.circle(screen, YELLOW, (int(c * SQUARESIZE + SQUARESIZE / 2), int((ROW_COUNT-1-r) * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()


def resetGame(screen):
    font1 = pygame.font.SysFont("monospace", 25, True)
    pygame.draw.rect(screen, WHITE, (WIDTH - 1.5 * SQUARESIZE - 5, SQUARESIZE / 1.5, SQUARESIZE * 1.5, SQUARESIZE / 3))
    resetbtn = font1.render("New game", 1, BLACK)
    screen.blit(resetbtn, (WIDTH - 1.5 * SQUARESIZE + 10, SQUARESIZE / 1.5))
    pygame.display.update()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                posx = event.pos[0]
                pygame.draw.circle(screen, BLACK, (posx, SQUARESIZE / 2), RADIUS)
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                posy = event.pos[1]
                x = WIDTH - 1.5 * SQUARESIZE - 5
                y = SQUARESIZE / 1.5
                if x <= posx <= x+SQUARESIZE * 1.5 and y <= posy <= y+ SQUARESIZE/3:
                    done = True
                else:
                    done = False
    screen.fill(BLACK)
    initial_screen(screen)
    pygame.display.update()


def setting():
    # Initializes the game window
    pygame.init()
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    audio_start_game()  # Says "welcome to 4 connect game"
    initial_screen(screen)
    pygame.display.update()  # update the display after the changes
    font = pygame.font.SysFont("monospace", 50, True)
    return screen, font
