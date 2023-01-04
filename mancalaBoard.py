class MancalaBoard:
    def __init__(self):
        # Initialisation du plateau de jeu
        # Les clés sont les indices des fosses et magasins, et les valeurs sont le nombre de seeds
        self.board = {'A': 4, 'B': 4, 'C': 4, 'D': 4, 'E': 4, 'F': 4,
                     'G': 4, 'H': 4, 'I': 4, 'J': 4, 'K': 4, 'L': 4,
                      1: 0, 2: 0}
        
        # Tuple pour stocker les indices des fosses du joueur 1
        self.player_1_pits = ('A', 'B', 'C', 'D', 'E', 'F')
        
        # Tuple pour stocker les indices des fosses du joueur 2
        self.player_2_pits = ('G', 'H', 'I', 'J', 'K', 'L')
        
        # Dictionnaire pour stocker la fosse opposée de chaque fosse
        self.opposite_pit = {'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K',
                         'F': 'L', 'G': 'A', 'H': 'B', 'I': 'C', 'J': 'D', 'K': 'E', 'L': 'F'}
        
        # Dictionnaire pour stocker la fosse suivante de chaque fosse
        self.next_pit = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': 1,
                     1: 'L', 'L': 'K', 'K': 'J', 'J': 'I', 'I': 'H', 'H': 'G', 'G': 2, 2: 'A'}

    def possibleMoves(self, player):
        # Si le joueur 1 joue, on retourne les indices des fosses du joueur 1 qui contiennent des seeds
        if player == 1:
            return [pit for pit in self.player_1_pits if self.board[pit] > 0]
        
        # Si le joueur 2 joue, on retourne les indices des fosses du joueur 2 qui contiennent des seeds
        else:
            return [pit for pit in self.player_2_pits if self.board[pit] > 0]

    def doMove(self, player, pit):
        # Récupération du nombre de seeds dans la fosse choisie
        seeds = self.board[pit]
        self.board[pit] = 0
        
        # Parcours du plateau en commençant par la fosse suivante de la fosse choisie
        while seeds > 0:
            pit = self.next_pit[pit]
            self.board[pit] += 1
            seeds = seeds-1
            
        # Si le tour se termine dans un magasin, c'est au même joueur de jouer à nouveau
        if (pit == player):
            return player
          
        # Si on atteint une fosse vide, on prend toutes les graines de la fosse opposée et on les ajoute au magasin du joueur
        if (player == 1):
            player_fosses = self.player_1_pits
        else:
            player_fosses = self.player_2_pits
        
        if (self.board[pit] == 1 and pit in player_fosses):
            self.board[pit] = 0
            opposite = self.opposite_pit[pit]
            self.board[player] += (self.board[opposite]+1)
            self.board[opposite] = 0

        
        if (player == 1):
            return 2
        else:
            return 1