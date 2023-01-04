
import pygame
from graphic import Drawer
from play import Play
from game import Game
import time

draw = Drawer()

# Run the game loop
running = True
test = Play()
game = Game(1)
player = 1
while (not game.gameOver()):
    if (player == 1):
        draw.DisplayPossibleMoves(game.state.possibleMoves(1))
        player = test.humanTurn(game)
        draw.RemovePossibleMoves(game.state.possibleMoves(1))
        draw.Update1(game.state.board)
        draw.DisplayTurn(player)
    else:
        player, game = test.computerTurn(game, test)
        time.sleep(1)
        draw.Update2(game.state.board)
        draw.DisplayTurn(player)
    # Handle events
    for event in pygame.event.get():
        # Quit the game if the user closes the window
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
player, score = game.findWinner()
draw.DisplayTheWinner(player, score)
time.sleep(10)
pygame.quit()