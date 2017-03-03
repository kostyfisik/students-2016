#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
#    Copyright(C) 2017 Vitaly Yaroshenko <yarokha@gmail.com>
#
#    This file is part of python-scattnlay
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import numpy as np

def isCheck(m, a, b, num):
    n = 3 * (int(a / 3)) + int(b / 3)
    x = 3 * int(n / 3)
    y = 3 * (n - x)
    return num in m[x:x + 3, y:y + 3] or num in m[0:9, b] or num in m[a, 0:9]
def Search(m):
    for x in range(0, 9):
        for y in range(0, 9):
            if m[x, y] == 0:
                return True, x, y
    return False, x, y
def Solver(m):
    m_temp = np.copy(m)
    test, x, y = Search(m)
    if test:
        ch = False
        for i in range(1, 10):
            if not isCheck(m, x, y, i):
                ch = True
                m[x, y] = i
            if ch is True:
                check, m = Solver(m)
                if check is True:
                    return True, m
                elif check is False:
                    m = np.copy(m_temp)
                    ch = False
        if ch is False:
            return False, m
    else:
        return True, m

# m = np.matrix([
# [6,4,0, 0,1,3, 0,7,0],
# [3,0,0, 6,0,8, 0,1,5],
# [8,1,2, 5,7,0, 0,3,0],
# [2,0,0, 4,0,5, 1,0,7],
# [4,0,7, 0,0,0, 9,0,3],
# [0,8,0, 7,9,6, 5,0,2],
# [0,2,0, 3,0,7, 6,5,0],
# [7,0,8, 1,5,0, 3,9,0],
# [0,3,1, 0,6,4, 0,0,8]])
#
# m = np.matrix([
# [0,0,0, 5,0,7, 0,0,0],
# [0,0,2, 4,0,6, 3,0,0],
# [0,9,0, 0,1,0, 0,2,0],
# [2,7,0, 0,0,0, 0,6,8],
# [0,0,3, 0,0,0, 1,0,0],
# [1,4,0, 0,0,0, 0,9,3],
# [0,6,0, 0,4,0, 0,5,0],
# [0,0,9, 2,0,5, 6,0,0],
# [0,0,0, 9,0,3, 0,0,0]])
#
# m = np.matrix([
# [4,0,0, 8,0,0, 0,0,0],
# [0,0,7, 0,6,0, 0,0,5],
# [0,0,3, 0,0,0, 0,9,0],
# [0,0,4, 0,0,1, 0,0,7],
# [0,5,0, 0,0,8, 0,1,0],
# [2,0,0, 0,0,0, 3,0,0],
# [0,2,0, 0,0,0, 4,0,0],
# [9,0,0, 0,3,0, 6,0,0],
# [0,0,0, 0,0,7, 0,0,3]])
m = np.matrix([
[8,0,0, 0,0,0, 0,0,0],
[0,0,3, 6,0,0, 0,0,0],
[0,7,0, 0,9,0, 2,0,0],
[0,5,0, 0,0,7, 0,0,0],
[0,0,0, 0,4,5, 7,0,0],
[0,0,0, 1,0,0, 0,3,0],
[0,0,1, 0,0,0, 0,6,8],
[0,0,8, 5,0,0, 0,1,0],
[0,9,0, 0,0,0, 4,0,0]])

print(m)
check, m = Solver(m)
print(m)

