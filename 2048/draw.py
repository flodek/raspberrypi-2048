# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 18:54:38 2019

@author: flodek (Volodymyr Shumara)
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
       [w, w]],
    4:[[w, w],
       [w, g]],
    8:[[w, w],
       [g, g]],
    16:[[g, w],
       [g, g]],
    32:[[g, g],
        [g, g]],
    64:[[w, w],
        [w, b]],
    128:[[w, w],
        [b, b]],
    256:[[b, w],
         [b, b]],
    512:[[b, b],
         [b, b]],
    1024:[[w, w],
         [w, r]],
    2048:[[w, w],
          [r, r]],
    4096:[[r, w],
          [r, r]],
    8192:[[r, r],
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

