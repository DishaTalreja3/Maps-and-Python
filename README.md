# a0
## Part 1: find_luddy

Set of valid states: (i,j) where IUB_map(i,j)="."
Successor function:[(i,j+1),(i,j-1),(i+1,j),(i-1,j)] where IUB_map[(i,j+1),(i,j-1),(i+1,j),(i-1,j)]!="&" (only sidewalks allowed: ".") 
Cost Function: 1
Goal state definition: (i,j) where IUB_map(i,j)="@"
Initial State: (i,j) where IUB_map(i,j)="#"

The given program entered an infinite loop because the successor function included previously traversed states also. Repetitive movement between 2 states causes the loop to run infinitely.
I escaped the infinite loop by keeping a track of all traversed(visited) nodes and storing them in a list 'traversed[]'. All states returned by successor function which were present in the list traversed[], were removed. To keep a track of the directions of the movements, I compared the locations of curr_move(current position) and move(next position) to retrieve the direction chosen.
Initially, the optimal path was not printed. The printed path included the directions traversed in the wrong direction(with dead end).
I solved that by associating the path travelled from (0,0) to (i,j) with (i,j) where (i,j) is the current position.


## Part 2: hide 

Set of valid states: IUB_map  with n friends("F") in the same row or column only if there exists a "&" or "@" between two F's
Successor function: Insertion of "F" where IUB_map!="&" 
Cost Function: 1
Goal state definition: IUB_map with k friends(F) such that any two friends(F) have "&" or "@" in between, in the same row or column.
Initial State: IUB_map(without any friends)

The given program did not satisfy the required condition of no two friends in line of sight of each other. They were being placed randomly. 
For every element in IUB_map, successor function was computed. Every state in successor function that was visited is stored in the list 'traversed[]'. To satisfy the given condition, for every element, it checks if there exists a "F" in the same row or column, my program looks for "&" in all four drections(left,right,above,below) and if found, inserts an "F" in the current position. If there are no "F" in the same row or column, inserts an F in the current position.




