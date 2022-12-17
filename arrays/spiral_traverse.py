"""
Spiral Traverse:

Write a function that takes an nxm two-dimensional array and returns a one-dimensional
array of all the array's elements in spiral order. 

Spiral order starts at the top-left corner of the 2d array, goes to the right, then
proceeds in a spiral pattern all the way until every element has been visited.

Example:
[ 1,  2,  3,  4],
[12, 13, 14,  5],
[11, 16, 15,  6],
[10,  9,  8,  7]

returns 
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
"""

"""
- Need to know when to "pivot" 
- Need to know when we're done - count number visited

I'm thinking we'll need to mark cells as visited. 

step vector: (0, 1) -> (1, 0) -> (0, -1) -> (-1, 0) --|
               ^--------------------------------------|   

[ ]

"""
def step(pos, dir):
    return (pos[0] + dir[0], pos[1] + dir[1])

def pivot(dir):
    if dir == (0, 1):
        return (1, 0)
    elif dir == (1, 0):
        return (0, -1)
    elif dir == (0, -1):
        return (-1, 0)
    elif dir == (-1, 0):
        return (0, 1)
    else:
        print("invalid direction")
        return None
        
def spiralTraverse(array):
    # Write your code here.
    numberVisited = 0
    pos = (0,0)
    dir = (0, 1)
    visited = {}
    width = len(array[0])
    height = len(array)
    ans = []

    def outOfRange(pos):
        return pos[0] < 0 or pos[0] >= height or pos[1] < 0 or pos[1] >= width
    
    while numberVisited < width * height:
        visited[pos] = True
        numberVisited += 1
        ans.append(array[pos[0]][pos[1]])
        if step(pos, dir) in visited or outOfRange(step(pos, dir)):
            dir = pivot(dir)
        pos = step(pos, dir)
    return ans
        
        
    
