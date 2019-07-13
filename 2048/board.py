# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 23:08:31 2019

@author: flodek (Volodymyr Shumara)
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

def merge_line(line, directions='r'):
    line = line[np.nonzero(line)].tolist()
    j = 0
    while j < (len(line) - 1):
        if (line[j]==line[j+1]):
            line[j] *= 2
            del line[j+1]
        j += 1
    return [0] * (4 - len(line)) + line if directions=='r' else line + [0] * (4 - len(line))

def shift_right(matrix):
    res = np.copy(matrix)
    for i in range(4):
        res[i] = merge_line(res[i])
    return res

def shift_left(matrix):
    res = np.copy(matrix)
    for i in range(4):
        res[i] = merge_line(res[i], 'l')
    return res

def shift_down(matrix):
    res = np.copy(matrix)
    for i in range(4):
        res[:, i] = merge_line(res[:, i])
    return res

def shift_up(matrix):
    res = np.copy(matrix)
    for i in range(4):
        res[:, i] = merge_line(res[:, i], 'l')
    return res
