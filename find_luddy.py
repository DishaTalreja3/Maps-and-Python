#!/usr/local/bin/python3
#
# find_luddy.py : a simple maze solver
#
# Submitted by : [Disha Ravi Talreja (dtalreja)]
#
# Based on skeleton code by Z. Kachwala, 2019
#

import sys
import json

# Parse the map from a given filename
def parse_map(filename):
	with open(filename,"r") as f:
		return [[char for char in line] for line in f.read().split("\n")]

# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
	return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
	moves=((row+1,col), (row-1,col), (row,col-1), (row,col+1))
    

	# Return only moves that are within the board and legal (i.e. on the sidewalk ".")
	return [ move for move in moves if valid_index(move, len(map), len(map[0])) and (map[move[0]][move[1]] in ".@" ) ]

# Perform search on the map
def search1(IUB_map):
	# Find my start position
    you_loc=[(row_i,col_i) for col_i in range(len(IUB_map[0])) for row_i in range(len(IUB_map)) if IUB_map[row_i][col_i]=="#"][0]
    fringe=[(you_loc,0)]
    row=[]
    col=[]
    for i in range(0,len(IUB_map)):
        for j in range(0,len(IUB_map[0])):
            col.append('')
        row.append(col.copy())
        col.clear()
    
    
           
    #print(fringe)
    traversed=[]
    

    while fringe:
        
        (curr_move, curr_dist)=fringe.pop()
        
       
        traversed.append(curr_move)
        #print(curr_move)    
        #print(row[curr_move[0]][curr_move[1]])
        for move in moves(IUB_map, *curr_move):
            if move not in traversed:
                path=str(row[curr_move[0]][curr_move[1]])
                if(curr_move[0]-1==move[0]):
                    path+="N"
                    
                elif(curr_move[0]+1==move[0]):
                    path+="S"
                   
                elif(curr_move[1]+1==move[1]):
                    path+="E"
                    
                elif(curr_move[1]-1==move[1]):
                    path+="W"
                    
                i=move[0]
                j=move[1]
                row[i][j]=path
                if IUB_map[move[0]][move[1]]=="@":
                    return (curr_dist+1,row[move[0]][move[1]])
                else:
                    fringe.append((move, curr_dist + 1))
    return 'Inf', '' 
        
                    
           
                                    
                        
        
                    

# Main Function
if __name__ == "__main__":
	IUB_map=parse_map(sys.argv[1])
	print("Shhhh... quiet while I navigate!")
	solution,path = search1(IUB_map)
	print("Here's the solution I found:\n"+str(solution)+' '+path)
    
	
    
   

    
   
    
    
    
    
    
    
    
    
    
    
