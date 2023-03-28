name1 = input("Player X input your name: ")
name2 = input("Player O input your name: ")
boardSquares = ['0','1','2','3','4','5','6','\n', '.', '.', '.', '.', '.', '.' ,'.' ,'\n', '.', '.', '.', '.', '.', '.' ,'.' ,'\n', '.', '.', '.', '.', '.', '.' ,'.' ,'\n', '.', '.', '.', '.', '.', '.' ,'.' ,'\n', '.', '.', '.', '.', '.', '.' ,'.' ,'\n', '.', '.', '.', '.', '.', '.' ,'.' ,'\n', '.', '.', '.', '.', '.', '.' ,'.' ,'\n']
def print_board(list):
    final = ''
    for place in range(64):
        if boardSquares[place] == '.':
            final += '.'
            final += ' '
        elif boardSquares[place] == 'X':
            final += 'X'
            final += ' '
        elif boardSquares[place] == 'O':
            final += 'O'
            final += ' '
        elif boardSquares[place] == '\n':
            final += '\n'
        else:
            final += boardSquares[place]
            final += ' '
    return final
print(print_board(boardSquares))
def win(list, turn):
    for place in range(64):
        if list[place] in 'XO':
            if (place<60) and (list[place] == list[place+1]) and (list[place+1] == list[place+2]) and (list[place+3] == list[place+2]) and list[place] != '.' and list[place+1] != '.' and list[place+2] != '.' and list[place+3] != '.':
                return True
            else:
                pass
            if (place<40) and (list[place] == list[place+8]) and list[place+8] == list[place+16] and list[place+16] == list[place+24] and list[place] != '.' and list[place+8] != '.' and list[place+16] != '.' and list[place+24] != '.':
                return True
            else:
                pass
            if place<43 and list[place] == list[place+7] and list[place+7] == list[place+14] and list[place+14] == list[place+21] and list[place] != '.' and list[place+7] != '.' and list[place+14] != '.' and list[place+21] != '.':
                return True
            else:
                pass
            if (place<32) and list[place] == list[place+9] and list[place+9] == list[place+18] and list[place+18] == list[place+27] and list[place] != '.' and list[place+9] != '.' and list[place+18] != '.' and list[place+27] != '.':
                return True
            else:
                pass
        else:
            pass
for i in range(49):
    column = int(input(str(name1)+ "(X), which column would you like to play in? "))
    if 56+column<64 and boardSquares[56+column] == '.':
        boardSquares.pop(56+column)
        boardSquares.insert(56+column, 'X')
    elif 48+column<64 and boardSquares[48+column] == '.':
        boardSquares.pop(48+column)
        boardSquares.insert(48+column, 'X')
    elif 40+column<64 and boardSquares[40+column] == '.':
        boardSquares.pop(40+column)
        boardSquares.insert(40+column, 'X')
    elif 32+column<64 and boardSquares[32+column] == '.':
        boardSquares.pop(32+column)
        boardSquares.insert(32+column, 'X')
    elif 24+column<64 and boardSquares[24+column] == '.':
        boardSquares.pop(24+column)
        boardSquares.insert(24+column, 'X')
    elif 16+column<64 and boardSquares[16+column] == '.':
        boardSquares.pop(16+column)
        boardSquares.insert(16+column, 'X')
    elif 8+column<64 and boardSquares[8+column] == '.':
        boardSquares.pop(8+column)
        boardSquares.insert(8+column, 'X')
    else:
        print("Not a valid option")
    if win(boardSquares, 'X'):
        print(print_board(boardSquares))
        print(str(name1)+" wins!")
        break
    else:
        pass
    print(print_board(boardSquares))
    column = int(input(str(name2)+ "(O), which column would you like to play in? "))
    if 56+column<64 and boardSquares[56+column] == '.':
        boardSquares.pop(56+column)
        boardSquares.insert(56+column, 'O')
    elif 48+column<64 and boardSquares[48+column] == '.':
        boardSquares.pop(48+column)
        boardSquares.insert(48+column, 'O')
    elif 40+column<64 and boardSquares[40+column] == '.':
        boardSquares.pop(40+column)
        boardSquares.insert(40+column, 'O')
    elif 32+column<64 and boardSquares[32+column] == '.':
        boardSquares.pop(32+column)
        boardSquares.insert(32+column, 'O')
    elif 24+column<64 and boardSquares[24+column] == '.':
        boardSquares.pop(24+column)
        boardSquares.insert(24+column, 'O')
    elif 16+column<64 and boardSquares[16+column] == '.':
        boardSquares.pop(16+column)
        boardSquares.insert(16+column, 'O')
    elif 8+column<64 and boardSquares[8+column] == '.':
        boardSquares.pop(8+column)
        boardSquares.insert(8+column, 'O')
    else:
        print("Not a valid option")
    if win(boardSquares, 'O'):
        print(print_board(boardSquares))
        print(str(name2)+ " wins!")
        break
    else:
        pass
    print(print_board(boardSquares))
    
                      

    
