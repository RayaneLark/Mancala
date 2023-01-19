from mancalaBoard import MancalaBoard
import math

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
        # Calcul du score final et retourne le gagnant et le score final
        score_player_1 = self.state.board[1]
        score_player_2 = self.state.board[2]
        
        # Détermination du gagnant
        if score_player_1 > score_player_2:
            return 1, score_player_1
        else:
            return 2, score_player_2

    def evaluate(self):
        H1 = self.hoard_leftmost_pit()
        H2 = self.hoard_player_side()
        H3 = self.have_many_moves()
        H4 = self.max_seeds_in_store()
        H5 = self.proximity_to_winning_1()
        H6 = self.proximity_to_winning_2()
        
        return 0.3*H6 + 0.3*H5 + 0.1*H4 + 0.1*H3 + 0.1*H2 + 0.1*H1
    
    def hoard_leftmost_pit(self):
        leftmost_pit = self.state.board['G']
        return leftmost_pit
    
    def hoard_player_side(self):
        sum_seeds = 0
        for x in self.state.player_1_pits:
            sum_seeds += self.state.board[x]
        return sum_seeds
    
    def have_many_moves(self):
        possible_moves = self.state.possibleMoves(2)
        return len(possible_moves)
    
    def max_seeds_in_store(self):
        return self.state.board[2]
    
    def proximity_to_winning_1(self):
        current_seeds = self.state.board[2]
        opponent_seeds = self.state.board[1]
        if current_seeds >= 1.5 * opponent_seeds and opponent_seeds > 5:
            return 1
        else:
            return 0
        
    def proximity_to_winning_2(self):
        return self.state.board[1] - self.state.board[2] 
