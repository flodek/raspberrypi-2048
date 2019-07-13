# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 22:04:25 2019

@author: flodek (Volodymyr Shumara)
"""
from sense_hat import SenseHat
import time
import numpy as np
import draw as d
import board as b

hat = SenseHat()

init_board = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

board = b.add_new_number(init_board)
board = b.add_new_number(board)

hat.set_pixels(d.board2pixels(board))

while True:
    for event in hat.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                new_board = b.shift_up(board)
            elif event.direction == "down":
                new_board = b.shift_down(board)
            elif event.direction == "left":
                new_board = b.shift_left(board)
            elif event.direction == "right":
                new_board = b.shift_right(board)

            hat.set_pixels(d.board2pixels(new_board))
            time.sleep(0.2)

            if(b.get_num_ofempty(new_board) == 0):
                hat.show_message("Game Over")
                raise SystemExit(0)

            if(np.array_equal(new_board, board)):
                continue
            board = new_board

            board = b.add_new_number(board)
            
            hat.set_pixels(d.board2pixels(board))
    
    time.sleep(0.1)
