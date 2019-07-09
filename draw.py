# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 18:54:38 2019

"""
import numpy as np
 

n = [0, 0, 0]
w = [128, 128, 128]
g = [0, 128, 0]
b = [0, 0, 128]
r = [128, 0, 0]
 

pixels = [
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n
]

num2pix = {
    0:[[n, n],
       [n, n]],
    2:[[w, w],
       [w, g]],
    4:[[w, w],
       [g, g]],
    8:[[g, w],
       [g, g]],
    16:[[g, g],
        [g, g]],
    32:[[w, w],
        [w, b]],
    64:[[w, w],
        [b, b]],
    128:[[b, w],
         [b, b]],
    256:[[b, b],
         [b, b]],
    512:[[w, w],
         [w, r]],
    1024:[[w, w],
          [r, r]],
    2048:[[r, w],
          [r, r]]
}

def board2pixels(board):
    pix = np.copy(pixels)
 
    for mr in range(4):
        for cr in range(2):
            for mc in range(4):
                for cc in range(2):
                    pix[mr * 16 + cr * 8 + mc * 2 + cc] = num2pix[board[mr][mc]][cr][cc]

    return pix

