import random
import time

def isFull(L):
    for l in L:
        for e in range(len(l)):
            if l[e] == ' ':
                return False
    return True

def GenerateFreeSlots(L):
    C = []
    for l in range(len(L)):
        for e in range(len(L[l])):
            if L[l][e] == ' ':
                C.append((l,e))
    return C

def win(L,n):
    for j in range(0,n):
        c = 1
        for i in range(1,len(L)):
            if L[j][i] == L[j][i-1] != ' ':
                c += 1
        if c==len(L):
            return (True,L[j][0])

    for j in range(0,n):
        c = 1
        for i in range(1,len(L)):
            if L[i][j] == L[i-1][j] != ' ':
                c += 1
        if c==len(L):
            return (True,L[0][j])

    c = 1
    for i in range(0,len(L)-1):
        if L[i][i] == L[i+1][i+1] != ' ':
            c += 1
    if c==len(L):
        return (True,L[0][0])

    c = 1
    for i in range(0,len(L)-1):
        if L[i][n-1-i] == L[i+1][n-1-i-1] != ' ':
            c += 1
    if c==len(L):
        return (True,L[0][n-1])

    return (False,None)

def threat(L,n):
    for j in range(0,n):
        c = 1
        for i in range(1,len(L)):
            if L[j][i] == L[j][i-1] != ' ':
                c += 1
    if c==2=='X':
        return (i,j)

    for j in range(0,n):
        c = 1
        for i in range(1,len(L)):
            if L[i][j] == L[i-1][j] != ' ':
                c += 1
    if c==2=='X':
        return (i,j)

    c = 1
    for i in range(0,len(L)-1):
        if L[i][i] == L[i+1][i+1] != ' ':
            c += 1
    if c==2=='X':
        return (i,j)

    c = 1
    for i in range(0,len(L)-1):
        if L[i][n-1-i] == L[i+1][n-1-i-1] != ' ':
            c += 1
    if c==2=='X':
        return (i,j)

    return -1

def TicTacToe(n):
    L=[[' ' for i in range(n)] for j in range(n)]
    display(L)
    X = input('Would you like to be X or O? ')
    def XORec(L,X):
        assert X=='X' or X=='O', 'You must be either X or O!'
        if X=='X':
            O = 'O'
        elif X=='O':
            O = 'X'
        r = int(input('Enter row: '))
        c = int(input('Enter column: '))
        r -= 1
        c -= 1
        assert 0<=r<=n-1 and 0<=c<=n-1, 'Exceeded Number of Rows/Columns!'
        if L[r][c] != ' ':
            while L[r][c] != ' ':
                print('Row is occupied!')
                r = int(input('Enter row: '))
                c = int(input('Enter column: '))
                r -= 1
                c -= 1
        L[r][c] = X
        display(L)
        print('')
        (B,W) = win(L,n)
        if B==True:
            return 'Game Over! '+str(W)+' Wins!'
        if isFull(L): return 'Match Board is Full! Draw'
        C = GenerateFreeSlots(L)
        p = random.randint(0,len(C)-1)
        (i,j) = C[p]
        L[i][j] = O
        time.sleep(1)
        display(L)
        (B,W) = win(L,n)
        if B==True:
            return 'Game Over! '+str(W)+' Wins!'
        return XORec(L, X)
    return XORec(L, X)

def display(L):
    s = ''
    for l in L:
        for e in range(len(l)):
            s = s + ' ' + str(l[e]) + ' | '
        s = s[:-2]
        s += '\n' + '---'*(len(l)+1) + '\n'
    print(s[:((-3)*(len(l)+1))-2])

print(TicTacToe(2))