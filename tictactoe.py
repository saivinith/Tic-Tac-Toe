
import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):    
    cx=0
    cy=0
    for i in range(3):
        for j in range(3):
            if(board[i][j]==X):
                cx = cx+1
            elif(board[i][j]==O):
                cy = cy+1
    if(cx==cy):
        return X
    else:
        return O
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    board_actions = set()
    for i in range(3):
        for j in range(3):
            if(board[i][j]==None):
                board_actions.add((i,j))
    return board_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_updated = copy.deepcopy(board)
    board_updated[action[0]][action[1]]=player(board)
    return board_updated


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    #row
    for i in range(3):
        Flagrow = True
        for j in range(2):
            if(board[i][j]!=board[i][j+1]):
                Flagrow=False
        if(Flagrow):
            #print('Flagrow')
            return board[i][j]           
    
    for i in range(3):
        Flagcol = True
        for j in range(2):
            if(board[j][i]!=board[j+1][i]):
                Flagcol=False
        if(Flagcol):
            #print('Flagcol')
            return board[j][i]
    
    if((board[0][0] == board[1][1]) and (board[1][1] == board[2][2])):
        return board[0][0]
    
    if(board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return board[0][2]
    
    return None    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    
    """
    Flag=0
    gameover = winner(board)
    #print(gameover)
    if(gameover == None):
        for i in board:
            if(None in i):
                Flag=1
                return False
        if(Flag==0):
            return True
    else:
        utility(board)
        return True
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    utility_value = winner(board)
    if(utility_value == X):
        return 1
    elif(utility_value == O):
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    
    """
    
    bestmove = tuple()
    moves = actions(board)
    print(moves)
    if(player(board)==X):
        bestscore = -10000000
        for i in moves:
                if(board[i[0]][i[1]] == None):
                    board[i[0]][i[1]] = player(board)
                    value = score(board,False)        
                    board[i[0]][i[1]] = None
                    print('value',value)
                    if(value > bestscore):
                        bestscore = value
                        bestmove = (i[0],i[1])
                    #print('bestmove',bestmove)
    if(player(board)==O):
        bestscore = 10000000
        for i in moves:
                if(board[i[0]][i[1]] == None):
                    board[i[0]][i[1]] = player(board)
                    value = score(board,True)        
                    board[i[0]][i[1]] = None
                    print('value',value)
                    if(value < bestscore):
                        bestscore = value
                        bestmove = (i[0],i[1])
                    #print('bestmove',bestmove)
    
    return bestmove
    
def score(board,ismaximizing):
    Flag = 0
    result = utility(board)
    if(result != 0):
        return result
    else:
        for i in board:
            if(None in i):
                Flag=1
        if(Flag==0):
            return result
    
    if(ismaximizing):
        #moves = actions(board)
        bestscore = -10000000
        for i in range(3):
            for j in range(3):
                if(board[i][j] == None):
                    board[i][j] = player(board)
                    value = score(board,False)
                    board[i][j] = None
                    bestscore = max(value,bestscore)
        return bestscore
    else:
        #moves = actions(board)
        bestscore = 10000000
        for i in range(3):
            for j in range(3):
                if(board[i][j] == None):
                    board[i][j] = player(board)
                    value = score(board,True)
                    board[i][j] = None
                    bestscore = min(value,bestscore)
        return bestscore
        
    #raise NotImplementedError