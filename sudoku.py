import numpy as np
import pandas as pd
import random

with open('/home/xueho/coding_challenges/sudoku.txt', 'r') as f:
    lines = f.readlines()

b=[]
for line in lines:
    line = list(line.strip("'"))
    line = [c for c in line if c not in (' ', '\n')]
    line = [int(c) if c != '_' else c for c in line ]
    b.append(line)   

board = pd.DataFrame(b,index = ['r1','r2','r3','r4','r5','r6','r7','r8','r9'],
                            columns = ['c1','c2','c3','c4','c5','c6','c7','c8','c9'])

# generate dictionary of missing values for each small square

full_set = {1,2,3,4,5,6,7,8,9}
    
def sq_missing(df):
    """get missing values in each 3x3 square """
    
    all_nums = []
    for i in range(0,3):
        nums = [n for n in df.iloc[i] if n != '_' ]
        all_nums.extend(nums)
    missing = full_set - set(all_nums)
    return list(missing)

def sq_dic(df):
    m_dic = {}
    for i in range(0,3):
        for j in range(0,3):
            tmp = df.iloc[i*3:(i*3+3), j*3:(j*3+3)]
            m_dic[i*3+j] = sq_missing(tmp)
    return m_dic 

def mis_pos_in_square(df_sq,k):
    m_pos = []
    for i in range(0,3):
        for j in range(0,3):
            if df_sq.iloc[i,j] == '_':
                r = i+3*(k//3)
                c = j+3*(k%3)
                m_pos.append((r,c))

    return list(set(m_pos))

def mis_pos_in_squares(df):
    """Record positions for '_' on the whole board. """
    
    # loop through squares
    all_pos = []
    for i in range(3):
        for j in range(3):
            df1 = df.iloc[i*3:(i*3+3), j*3:(j*3+3)]
            k = 3*i+j
            m_pos = mis_pos_in_square(df1,k)
            all_pos.extend(m_pos) 

    return all_pos

def fill_board(df, sq_miss):
    w = df.shape[0]
    filled_pos = []
    for row in range(w):
        exist_num_row = [x for x in df.iloc[row] if x !='_']
        for col in range(w):
            exist_num_col = [y for y in df.iloc[:, col] if y !='_'] 
                     
            if df.iloc[row, col] == '_':
                k = 3*(row//3) + col//3
                df1 = df.iloc[3*(row//3):3*(row//3)+3, 3*(col//3):3*(col//3)+3]
                for v in sq_miss[k]:
                    if v not in df1.values and v not in exist_num_row and v not in exist_num_col:
                        df.iloc[row, col] = v
                        filled_pos.append((row, col, v))
                        exist_num_row = [x for x in df.iloc[row] if x !='_']
                        exist_num_col = [y for y in df.iloc[:, col] if y !='_'] 
     
    return df, filled_pos 

if __name__ == '__main__':
    full_set = {1,2,3,4,5,6,7,8,9}
    sq_mis = sq_dic(board)
    finished, filled_pos = fill_board(board, sq_mis)
    print(finished)
    print()
    print(finished[finished=='_'].count().sum())
    