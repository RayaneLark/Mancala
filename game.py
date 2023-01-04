from mancalaBoard import MancalaBoard

class Game:
    def __init__(self, player):
        # représenter l’état (c’est-à-dire une instance de la classe MancalaBoard)
        self.state = MancalaBoard()
        # le numéro du joueur choisi par l’utilisateur (player1 ou player2)
        self.playerSide = player

    def gameOver(self):  
        # Vérifie si l'un des joueurs n'a plus de graines dans ses trous
        player_1_empty = all(self.state.board[x] == 0 for x in self.state.player_1_pits)
        player_2_empty = all(self.state.board[x] == 0 for x in self.state.player_2_pits)
        # Si le joueur 1 gagne
        if player_1_empty:
            for x in self.state.player_2_pits:
                self.state.board[1] += self.state.board[x]
            return True
        
        # Si le joueur 2 gagne
        elif player_2_empty:
            for x in self.state.player_1_pits:
                self.state.board[2] += self.state.board[x]
            return True
        
        # Si aucune des conditions n'est satisfaite, alors la partie n'est pas finie
        return False

    def findWinner(self):
        # Calcul du score final
        score_player_1 = self.state.board[1]
        score_player_2 = self.state.board[2]
        
        # Détermination du gagnant
        if score_player_1 > score_player_2:
            return 1, score_player_1
        else:
            return 2, score_player_2

    def evaluate(self):
        # Estimation du gain
        return self.state.board[1] - self.state.board[2]