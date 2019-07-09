# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 23:08:31 2019

"""
import numpy as np
import random

def get_num_ofempty(board):
    return len(np.where(board == 0)[0])

def add_new_number(board):
    new_board = np.copy(board)
    empty = np.where(new_board == 0)
    empty_indexes = list(zip(empty[0], empty[1]))
    position = random.randrange(0, len(empty_indexes), 1)
    num = 2 if random.randrange(1, 11, 1) <= 9 else 4
    new_board[empty_indexes[position][0]][empty_indexes[position][1]] = num
    
    return new_board

def shift_right(board):
    new_board = np.copy(board)
    
    for i in range(4):
        for j in range(3, 0, -1):
            for k in range(j - 1, -1, -1):
                if(new_board[i][j] == new_board[i][k]):
                    new_board[i][j] = new_board[i][j] + new_board[i][k]
                    new_board[i][k] = 0
                    if(new_board[i][j] != 0):
                        break
                else:
                    if(new_board[i][j] == 0):
                        new_board[i][j] = new_board[i][k]
                        new_board[i][k] = 0
                    else:
                        if(new_board[i][k] != 0):
                            break

    return new_board

def __shift_right_with_rotation(board, k):
    new_board = np.rot90(np.copy(board), k)
    return np.rot90(shift_right(new_board), 4 - k)

def shift_down(board):
    return __shift_right_with_rotation(board, 1)

def shift_left(board):
    return __shift_right_with_rotation(board, 2)

def shift_up(board):
    return __shift_right_with_rotation(board, 3)
