from ttt import Game
import random

def ai_optimum(board,depth,player):
    ai_moves=[]
    for pos in board.empty_pos():
        board.play_move(pos, player)

        val = board.minimax_algorithm(board, depth-1, toggle(player))
        board.play_move(pos,' ')
        if val > 50:
            ai_moves = [pos]
            break
        elif val == 50:
            ai_moves.append(pos)
    if len(ai_moves) > 0:
        return random.choice(ai_moves)
    else:
        return random.choice(board.empty_pos())

def toggle(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'

def main():
    game = Game()
    print('Human [X] ------vs------ AI [O]\n\n')
    game.display()
    while game.draw() == False:
        print('\n')
        human = input("Human : ")
        human = int(human)
        if game.board[human-1] == ' ':
            game.play_move(human-1,'X')
            if game.draw() == True:
                break
            print("\nAI is thinking...\n")
            ai = ai_optimum(game,-1,'O')
            game.play_move(ai,'O')
            game.display()
        else:
            print('Invalid Move. Try again')
    if game.winner() == 'O':
        print("\nWinner: AI [O]")
    elif game.winner() == 'X':
        print('\nWinner: Human [X]')
    else:
        print('\nDraw!')

main()