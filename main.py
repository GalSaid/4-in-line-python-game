import pygame
import sys
import gui
import math
import random
from gui import *
from audio import *

from Board import Board
from AIBoard import AIBoard


def game_with_1_player(board):
    """
    A function that manages the game queue after queue until victory.
    Link between the display and the logic of the AI board.
    taking into account the mouse clicks of the player on his queue.
    """
    game_is_over = False
    turn = random.randint(AIBoard.PLAYER_PIECE, AIBoard.AI_PIECE)
    while not game_is_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                # change the mouse motion to circle in player's color
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
                posx = event.pos[0]
                if turn == AIBoard.PLAYER_PIECE:
                    pygame.draw.circle(screen, RED, (posx, SQUARESIZE/2), RADIUS) # A circle in the player's color
                    # will appear instead of the mouse mark
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:  # If the player drop the piece
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))
                if board.is_valid_location(col):  # Only if the player is put the piece in the correct position
                    # the mouse pointer will disappear
                    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))

                # Ask for player1
                if turn == AIBoard.PLAYER_PIECE and not board.place_is_over():
                    if board.is_valid_location(col):
                        row = board.get_next_free_row(col)
                        board.drop_piece(row, col, AIBoard.PLAYER_PIECE)
                        if board.win_on_the_board(AIBoard.PLAYER_PIECE):
                            label = font.render("You wins!", 1, RED)
                            screen.blit(label, (45, 10))
                            game_is_over = True
                        draw_board_after_drop(screen, board.getBoard(), row, col)
                        turn = AIBoard.AI_PIECE

        if turn == AIBoard.AI_PIECE and not game_is_over and not board.place_is_over():
            col = board.get_best_move(AIBoard.AI_PIECE)
            if board.is_valid_location(col):
                pygame.time.wait(500)  # time interval between the insertion of the player's piece to the computer
                row = board.get_next_free_row(col)
                board.drop_piece(row, col, AIBoard.AI_PIECE)
                if board.win_on_the_board(AIBoard.AI_PIECE):
                    label = font.render("The computer wins!", 1, YELLOW)
                    screen.blit(label, (45, 10))
                    game_is_over = True
                turn = AIBoard.PLAYER_PIECE
            draw_board_after_drop(screen, board.getBoard(), row, col)

        if game_is_over:
            if turn == AIBoard.PLAYER_PIECE:
                audio_end_game("The computer wins!")
            else:
                audio_end_game("You wins!")
        if board.place_is_over():
            audio_end_game("No one win!")
            game_is_over = True


def game_with_2_players(board):
    """
     A function that manages the game queue after queue until victory.
     Link between the display and the logic of the board with two players.
     taking into account the mouse clicks of the two players.
     """
    game_is_over = False
    turn = 0
    while not game_is_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                # change the mouse motion to circle in player's color
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, RED, (posx, SQUARESIZE / 2), RADIUS)
                else:
                    pygame.draw.circle(screen, YELLOW, (posx, SQUARESIZE / 2), RADIUS)
                pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:  # If the player drop the piece
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))
                if board.is_valid_location(col):  # Only if the player is put the piece in the correct position
                    # the mouse pointer will disappear
                    pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
                # Ask for player1
                if turn == 0 and not board.place_is_over():
                    if board.is_valid_location(col):
                        row = board.get_next_free_row(col)
                        board.drop_piece(row, col, 1)
                        if board.win_on_the_board(1):
                            label = font.render("Player 1 wins!", 1, RED)
                            screen.blit(label, (45, 10))
                            game_is_over = True
                        turn = 1

                # Ask for player2
                elif not board.place_is_over():
                    if board.is_valid_location(col):
                        row = board.get_next_free_row(col)
                        board.drop_piece(row, col, 2)
                        if board.win_on_the_board(2):
                            label = font.render("Player 2 wins!", 1, YELLOW)
                            screen.blit(label, (45, 10))
                            game_is_over = True
                        turn = 0

                draw_board_after_drop(screen, board.getBoard(), row, col)
                if game_is_over:
                    audio_end_game("Player " + str(turn) + " wins!")
                if board.place_is_over():
                    audio_end_game("No one win!")
                    game_is_over = True


screen, font = gui.setting()
while True:
    choice = selection_game()  # return which game is chosen
    draw_board(screen)  # display the board
    if choice == 1:
        my_board = AIBoard(ROW_COUNT, COL_COUNT)
        game_with_1_player(my_board)
    elif choice == 2:
        my_board = Board(ROW_COUNT, COL_COUNT)
        game_with_2_players(my_board)
    gui.resetGame(screen)




