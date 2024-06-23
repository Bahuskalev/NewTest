import random

def drawBoard(board):
    print('___________')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---+---+---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---+---+---')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---+---+---')

def isWinner(bo, le): #варианты победы
    if ((bo[7] == le and bo[8] == le and bo[9] == le) or #верхняя линия
            (bo[4] == le and bo[5] == le and bo[6] == le) or #средняя
            (bo[1] == le and bo[2] == le and bo[3] == le) or #нижняя
            (bo[7] == le and bo[4] == le and bo[1] == le) or #вертикальная слева
            (bo[8] == le and bo[5] == le and bo[2] == le) or #центр
            (bo[9] == le and bo[6] == le and bo[3] == le) or #правая
            (bo[7] == le and bo[5] == le and bo[3] == le) or #диагональ
            (bo[9] == le and bo[5] == le and bo[1] == le)): #диагональ
        return True
    else:
        return False

def isBoardFull(board): #проверка заполненности поля
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    return True

def randomMove(board, movesList): #рандомный ход компа
    possibleMoves = free(board, movesList)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def free(board, movesList): #свободные ячейки
    possibleMoves = []
    for i in movesList:
        if board[i] == ' ':
            possibleMoves.append(i)
    return possibleMoves

def getComputerMove(board): #ход компа
    possibleMoves = free(board, [1,2,3,4,5,6,7,8,9])
    for i in possibleMoves:
        old = board[i]
        board[i] = computerLetter
        if isWinner(board, computerLetter):
            board[i] = old
            return i

        board[i] = playerLetter
        if isWinner(board, playerLetter):
            board[i] = old
            return i
        board[i] = old

    move = randomMove(board, [1, 3, 7, 9])

    if move != None:
        return move
    elif board[5] == ' ':
        return 5
    else:
        return randomMove(board, [2, 4, 6, 8])



print('Игра "Крестики-Нолики"')

print('Каким знаком Вы будете играть? (X или 0)')
playerLetter = input()
if playerLetter == 'X':
    computerLetter = '0'
else:
    computerLetter = 'X'

if random.randint(0, 1) == 0: #выбор хода, кто первый
    turn = 'Компьютер' #очередь
else:
    turn = 'Игрок'
print('Первым будет ходить ' + turn)

board = [' '] * 10 #для удобства нумерации
while True:
    if turn == 'Игрок':
        drawBoard(board) #прорисовка доски

        print('Ваш ход (1-9):')
        move = int(input()) #ход игрока
        board[move] = playerLetter

        if isWinner(board, playerLetter):
            drawBoard(board)
            print('Поздравляю!!! Вы победили!')
            break
        else:
            if isBoardFull(board):
                drawBoard(board)
                print('Ничья. В следующий раз сыграете лучше.')
                break
            else:
                turn = 'Компьютер'
    else:
        move = getComputerMove(board) #ход компа
        board[move] = computerLetter

        if isWinner(board, computerLetter):
            drawBoard(board)
            print('Компьютер победил! Вы проиграли...')
            break
        else:

            if isBoardFull(board):
                drawBoard(board)
                print('Ничья. В следующий раз сыграете лучше.')
                break
            else:
                turn = 'Игрок'


    
