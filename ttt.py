def toggle(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'

class Game:
    def __init__(self):
        self.board = [' ']*9

    def minimax_algorithm(self,node,depth,player):
        if depth == 0 or node.draw():
            if node.check() == "X":
                return 0
            elif node.check() == "O":
                return 100
            else:
                return 50

        if player == "O":
            optimum_value = 0
            for pos in node.empty_pos():
                node.play_move(pos, player)
                val = self.minimax_algorithm(node,depth-1,toggle(player))
                node.play_move(pos,' ')
                optimum_value = max(optimum_value,val)
            return optimum_value

        if player == "X":
            optimum_value = 100
            for pos in node.empty_pos():
                node.play_move(pos, player)
                val = self.minimax_algorithm(node,depth-1,toggle(player))
                node.play_move(pos,' ')
                optimum_value = min(optimum_value,val)
            return optimum_value

    def display(self):
        print(" %c | %c | %c " % (self.board[0], self.board[1], self.board[2]))
        print("___|___|___")
        print(" %c | %c | %c " % (self.board[3], self.board[4], self.board[5]))
        print("___|___|___")
        print(" %c | %c | %c " % (self.board[6], self.board[7], self.board[8]))
        print("   |   |   ")

    def check(self):
        win_cases = ([0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6])
        for p in ('X','O'):
            possible = self.filled_pos(p)
            for case in win_cases:
                win = True
                for pos in case:
                    if pos not in possible:
                        win = False
                if win == True:
                    return p

    def winner(self):
        if self.check() == 'X':
            return 'X'
        elif self.check() == 'O':
            return 'O'
        elif self.draw() == True:
            return 'Draw'

    def draw(self):
        if self.check() != None:
            return True
        for i in self.board:
            if i == ' ':
                return False
        return True

    def play_move(self,pos,player):
        self.board[pos] = player

    def empty_pos(self):
        empty = []
        for i in range(9):
            if self.board[i]==' ':
                empty.append(i)
        return empty

    def filled_pos(self, player):
        filled = []
        for i in range(0,9):
            if self.board[i] == player:
                filled.append(i)
        return filled