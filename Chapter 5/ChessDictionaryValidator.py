def main():
    board = {'1h': 'bking', '3e': 'wking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen'}
    print(isValidChessBoard(board))

def isValidChessBoard(board):
    # Check for 1 black king and 1 white king
    if 'bking' not in board.values() or 'wking' not in board.values():
        return False
    
    bkings = 0
    wkings = 0
    for value in board.values():
        if value == 'bking':
            bkings += 1
        if value == 'wking':
            wkings += 1
    
    if bkings != 1 or wkings != 1:
        return False
    
    # Check for total of 16 pieces, total of 8 pawns, and valid locations
    bpieces = 0
    wpieces = 0
    bpawns = 0
    wpawns = 0
    validNames = ['pawn', 'knight', 'queen', 'king', 'bishop', 'rook']

    for key, value in board.items():
        if value[1:] not in validNames:
            return False

        if value[0] == 'b':
            bpieces += 1
            if value == 'bpawn':
                bpawns += 1
        elif value[0] == 'w':
            wpieces += 1
            if value == 'wpawn':
                wpawns += 1
        else:
            return False

        if int(key[0]) < 1 or int(key[0]) > 8:
            return False

        if ord(key[1]) < ord('a') or ord(key[1]) > ord('h'):
            return False
    
    if bpieces > 16 or wpieces > 16 or bpawns > 8 or wpawns > 8:
        return False

    return True



if __name__ == '__main__':
    main()