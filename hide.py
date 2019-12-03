

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 13:55:19 2019

@author: disha
"""

#!/usr/local/bin/python3
#
# hide.py : a simple friend-hider
#
# Submitted by : Disha Ravi Talreja (dtalreja)
#
# Based on skeleton code by D. Crandall and Z. Kachwala, 2019
#
# The problem to be solved is this:
# Given a campus map, find a placement of F friends so that no two can find one another.
#

import sys

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().split("\n")]

# Count total # of friends on board
def count_friends(board):
    return sum([ row.count('F') for row in board ] )

# Return a string with the board rendered in a human-friendly format
def printable_board(board):
    return "\n".join([ "".join(row) for row in board])

# Add a friend to the board at the given position, and return a new board (doesn't change original)
def add_friend(board, row, col):
        if valid(board,row,col)==True:
            #print(printable_board(board))
            return board[0:row] + [board[row][0:col] + ['F',] + board[row][col+1:]] + board[row+1:] 
        return ''
        

def valid(board,r,c):
    lflag=0
    rflag=0
    uflag=0
    dflag=0
    if (board[r][c] == '.'):
        for i in range(c,-1,-1):
            if board[r][i]=="&":
                break
            elif board[r][i]=="F":
                lflag=1
                break
        for i in range(c+1,len(board[0])):
            if  board[r][i]=='&':
                break
            elif board[r][i]=="F":
                rflag=1
                break
        for i in range(r,-1,-1):
            if board[i][c]=='&':
                break
            elif board[i][c]=="F":
                uflag=1
                break
        for i in range(r,len(board)):
            if board[i][c]=='&':
                break
            elif board[i][c]=="F":
                dflag=1
                break
    if (lflag==1 or rflag==1 or uflag==1 or dflag==1):    
        return False
    else:
        return True
                        
                #return add_friend(board, r, c)            
# Get list of successors of given board state
def successors(board):
    #print(printable_board(board))
    #print("\n")
    #return [valid(board)]
    return [ add_friend(board, r, c) for r in range(0, len(board)) for c in range(0,len(board[0])) if (board[r][c] == '.')]
                        
#and 'F' not in (board[r][0:len(board[0])] and board[0:len(board)][c])"""
    

# check if board is a goal state
def is_goal(board):
    return count_friends(board) == K 

# Solve n-rooks!
def solve(initial_board):
    fringe = [initial_board]
    traversed=[]
    while len(fringe) > 0:
        xyz=fringe.pop()
        traversed.append(xyz)
        for s in successors(xyz):
            if is_goal(s):
                return(s)
            else:
               
                if s not  in traversed:
                    fringe.append(s)
    return False

# Main Function
if __name__ == "__main__":
    IUB_map=parse_map(sys.argv[1])

    # This is K, the number of friends
    K = int(sys.argv[2])
    print ("Starting from initial board:\n" + printable_board(IUB_map) + "\n\nLooking for solution...\n")
    solution = solve(IUB_map)
    print ("Here's what we found:")
    print (printable_board(solution) if solution else "None")
    

