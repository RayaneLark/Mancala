import pygame
import random
from mancalaBoard import MancalaBoard
import time

# Initialize Pygame
pygame.init()

# create a font object.
font = pygame.font.Font('arial.ttf', 30)
# Set the window size
WIDTH, HEIGHT = (1300, 700)

# Déclaration des couleurs
LIGHT_GRAY = (150, 150, 150)
DARK_GRAY = (40, 40, 40)
BLACK = (0, 0, 0)
BLUE = (131, 140, 222)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Set the board properties
board_width = WIDTH-50
board_height = HEIGHT-50
board_color = DARK_GRAY
board_x = 50
board_y = 50

# Set the fosse properties
fosse_width = 55
fosse_color = BLACK
fosse_spacing = 65

# Set the store properties
store_width = 100
store_height = HEIGHT-300
store_color = LIGHT_GRAY
store1_x = 150
store1_y = 150
store2_x = WIDTH-250
store2_y = 150

# Set the seeds properties
seed_width = 15
seed_color = [
              # Couleur verte foncée
              #(34, 139, 34),
              
              # Couleur rouge vif
              #(255, 99, 71),
              
              # Couleur jaune
              (255, 215, 0),
              
              # Couleur indigo
              #(75, 0, 130),
              
              # Couleur magenta foncée
              #(139, 0, 139)
            ]


class Drawer:
    def __init__(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # Set the title of the window
        pygame.display.set_caption("Mancala by Rayane")
        self.board = dict()
        self.drawBoard()
        self.drawFosses()
        self.drawStore1()
        self.drawStore2()
        for cle, valeur in self.board.items():
            self.drawSeed(valeur)
            self.drawSeed(valeur)
            self.drawSeed(valeur)
            self.drawSeed(valeur)
            '''if (cle in ["A", "B", "C", "D", "E", "F"]):
                self.PitValue(valeur, 4, -100)
            else:
                self.PitValue(valeur, 4, 100)'''
        self.PlayerScore(1, 0)
        self.PlayerScore(2, 0)
        self.DisplayTurn(1)
        self.Store1 = 0
        self.Store2 = 0
        self.change = {"A": 4, "B": 4, "C": 4, "D": 4, "E": 4, "F": 4,
                       "G": 4, "H": 4, "I": 4, "J": 4, "K": 4, "L": 4}
        pygame.display.flip()

    def drawBoard(self):
        pygame.draw.rect(self.screen, board_color, (board_x, board_y,
                         board_width, board_height), width=0, border_radius=50)
        pygame.display.flip()

    def drawStore1(self):
        pygame.draw.rect(self.screen, store_color, (store1_x, store1_y,
                         store_width, store_height), width=0, border_radius=50)
        pygame.display.flip()

    def drawStore2(self):
        pygame.draw.rect(self.screen, store_color, (store2_x, store2_y,
                         store_width, store_height), width=0, border_radius=50)
        pygame.display.flip()

    def drawFosses(self):
        # Draw fosses
        m = MancalaBoard()
        f1 = m.player_1_pits
        f2 = m.player_2_pits
        fosse_y = HEIGHT-200
        for i in range(len(f1)):
            fosse_x = 335 + (i * (fosse_width + fosse_spacing))

            pygame.draw.circle(self.screen, fosse_color,
                               (fosse_x, fosse_y), fosse_width)
            self.board[f1[i]] = (fosse_x, fosse_y)
        fosse_y = 200
        for i in range(len(f2)):
            fosse_x = 335 + (i * (fosse_width + fosse_spacing))
            pygame.draw.circle(self.screen, fosse_color,
                               (fosse_x, fosse_y), fosse_width)
            self.board[f2[i]] = (fosse_x, fosse_y)
        pygame.display.flip()

    def drawFosseP1(self, i):
        fosse_y = HEIGHT-200
        fosse_x = 335 + (i * (fosse_width + fosse_spacing))

        pygame.draw.circle(self.screen, fosse_color,
                           (fosse_x, fosse_y), fosse_width)
        pygame.display.flip()

    def drawFosseP2(self, i):
        fosse_y = 200
        fosse_x = 335 + (i * (fosse_width + fosse_spacing))
        pygame.draw.circle(self.screen, fosse_color,
                           (fosse_x, fosse_y), fosse_width)
        pygame.display.flip()
        pygame.display.flip()

    def drawSeed(self, cor):
        x, y = cor
        x = x+random.randint(-29, 29)
        y = y+random.randint(-29, 29)
        pygame.draw.circle(self.screen, random.choice(seed_color),
                           (x, y), seed_width)
        pygame.draw.circle(self.screen, BLACK,
                           (x, y), seed_width, 1)
        pygame.display.flip()

    '''def PitValue(self, cor, value, add):
        x, y = cor
        y = y+add
        # create a text surface object,
        # # on which text is drawn on it.
        text = font.render(f" {value} ", True, WHITE, DARK_GRAY)
        # create a rectangular object for the
        # # text surface object
        textRect = text.get_rect()
        # set the center of the rectangular object.
        textRect.center = x, y
        self.screen.blit(text, textRect)
        pygame.display.flip()'''

    def updateFosses(self, lettre):
        pygame.draw.circle(self.screen, fosse_color,
                           self.board[lettre], fosse_width)
        pygame.display.flip()

    def PlayerScore(self, Player, value):
        if (Player == 1):
            text = font.render(f"You : {value}", True, WHITE, DARK_GRAY)
            textRect = text.get_rect()
            textRect.center = WIDTH-200, 100

        else:
            text = font.render(f"AI : {value}", True, WHITE, DARK_GRAY)
            textRect = text.get_rect()
            textRect.center = 200, 100
        self.screen.blit(text, textRect)
        pygame.display.flip()

    def DisplayTurn(self, Player):
        font = pygame.font.Font('Arial.ttf', 25)
        if (Player == 2):
            text = font.render(f"* It's AI turn! *", True,
                               (220, 20, 60), DARK_GRAY)
        else:
            text = font.render(f" It's your turn! ", True,
                               (220, 20, 60), DARK_GRAY)
        textRect = text.get_rect()
        textRect.center = WIDTH/2, 100
        self.screen.blit(text, textRect)
        pygame.display.flip()

    def drawSeedStore(self, value, player):
        if (player == 2):
            x, y = store1_x, store1_y
            n = value-self.Store1
            self.Store1 = value
        else:
            x, y = store2_x, store2_y
            n = value-self.Store2
            self.Store2 = value
        x = x+random.randint(22, store_width-22)
        y = y+random.randint(22, store_height-22)
        for i in range(n):
            pygame.draw.circle(self.screen, random.choice(seed_color),
                               (x, y), seed_width)
            pygame.draw.circle(self.screen, BLACK,
                               (x, y), seed_width, 1)
        pygame.display.flip()

    def Update1(self, board, player=1):
        liste = ["A", "B", "C", "D", "E", "F"]
        for i in liste:
            if (self.change[i] != board[i]):
                add = -100
                self.drawFosseP1(liste.index(i))
                for j in range(board[i]):
                    self.drawSeed(self.board[i])
                #self.PitValue(self.board[i], board[i], add)
                time.sleep(0.8)
            self.change[i] = board[i]
        self.PlayerScore(player, board[player])
        self.drawSeedStore(board[player], player)
        time.sleep(0.5)
        liste = ["L", "K", "J", "I", "H", "G"]
        l = ["G", "H", "I", "J", "K", "L"]
        for i in liste:
            if (self.change[i] != board[i]):
                add = 100
                self.drawFosseP2(l.index(i))
                for j in range(board[i]):
                    self.drawSeed(self.board[i])
                #self.PitValue(self.board[i], board[i], add)
                time.sleep(0.8)
            self.change[i] = board[i]
        time.sleep(0.5)

    def Update2(self, board, player=2):
        liste = ["L", "K", "J", "I", "H", "G"]
        l = ["G", "H", "I", "J", "K", "L"]
        for i in liste:
            if (self.change[i] != board[i]):
                add = 100
                self.drawFosseP2(l.index(i))
                for j in range(board[i]):
                    self.drawSeed(self.board[i])
                #self.PitValue(self.board[i], board[i], add)
                time.sleep(0.8)
            self.change[i] = board[i]
        self.PlayerScore(player, board[player])
        self.drawSeedStore(board[player], player)
        time.sleep(0.5)
        liste = ["A", "B", "C", "D", "E", "F"]
        for i in liste:
            if (self.change[i] != board[i]):
                add = -100
                self.drawFosseP1(liste.index(i))
                for j in range(board[i]):
                    self.drawSeed(self.board[i])
                #self.PitValue(self.board[i], board[i], add)
                time.sleep(0.8)
            self.change[i] = board[i]
        time.sleep(0.5)

    def DisplayTheWinner(self, player, score):
        self.drawBoard()
        font = pygame.font.Font('Arial.ttf', 40)
        if (player == 1):
            text = font.render(f"The Winner is : You ", True, WHITE, DARK_GRAY)
        else:
            text = font.render(f"The Winner is : AI ", True, WHITE, DARK_GRAY)

        text2 = font.render(f"Score:{score}", True, WHITE, DARK_GRAY)
        textRect = text.get_rect()
        textRect.center = WIDTH/2, (HEIGHT/2-60)
        self.screen.blit(text, textRect)
        textRect = text2.get_rect()
        textRect.center = WIDTH/2, (HEIGHT/2+60)
        self.screen.blit(text2, textRect)
        pygame.display.flip()

    def DisplayPossibleMoves(self, liste):
        for i in liste:

            l = ["A", "B", "C", "D", "E", "F"]
            fosse_y = HEIGHT-200
            fosse_x = 335 + (l.index(i) * (fosse_width + fosse_spacing))

            pygame.draw.circle(self.screen, (220, 20, 60),
                               (fosse_x, fosse_y), fosse_width, 2)
        pygame.display.flip()

    def RemovePossibleMoves(self, liste):
        for i in liste:

            l = ["A", "B", "C", "D", "E", "F"]
            fosse_y = HEIGHT-200
            fosse_x = 335 + (l.index(i) * (fosse_width + fosse_spacing))

            pygame.draw.circle(self.screen, LIGHT_GRAY,
                               (fosse_x, fosse_y), fosse_width, 2)
        pygame.display.flip()