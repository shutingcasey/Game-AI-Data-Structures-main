#    Main Author(s): Christine Ang
#    Main Reviewer(s): Hyeri Jang & Casey Hsu

from a1_partc import Queue

#This function accepts a 2D array and returns a list of 2 valued tuples
#The tuples refer to a value in the 2D array that are considered to be "overflowing"
#A value is considered to be overflowing if its absolute value is greater than or equal to the number of its neighbors
def get_overflow_list(grid):
	
	total_rows = len(grid)
	
	total_cols = len(grid[0])

	result = []

	for i in range(total_rows):
		for j in range(total_cols):
			
			value = abs(grid[i][j])

			if (i == 0 or i == total_rows-1) and (j == 0 or j == total_cols-1) and value >= 2:
				result.append((i,j))
			elif  (i == 0 or i == total_rows-1) and (j >= 1 and j <= total_cols-2) and value >=3:
				result.append((i,j))
			elif (j == 0 or j == total_cols -1) and (i > 0 and i < total_rows-1) and value >= 3:
				result.append((i,j))
			else:
				if value >= 4:
					result.append((i,j))
			
	if not result:
		return None
	else:
		return result
			
		
#This is a recursive function that accepts a 2D array, a queue list, and int that tracks how many times a 2D array is added to the queue list. 
#The 2D array is considered to be "overflowing" if one or more values of the array is overflowing (determined by calling the get_overflow_list(grid)) or if signs of the non-zero cells are not all the same
#The function will continue to be recursive until the 2D array is no longer "overflowing"
#The function will return the number of times data is added to the queue list 
def overflow (grid, a_queue, counter=0):
    
    total_rows = len(grid)
    total_cols = len(grid[0])
    
    all_positive = True 
    all_negative = True

	#check if all values in the grid are positive
    for row in grid:
        for cell_value in row:
            if cell_value != 0:
                if cell_value < 0:
                    all_positive = False
                elif cell_value > 0:
                    all_negative = False

    
    #get overflow tuples
    overflow_tuples = get_overflow_list(grid)
   
    #Base Case
    if all_positive or all_negative or overflow_tuples==None:
        
        return counter
        #exit recursion
    else:
        #continue with recursion
      
        #find if OF are positive or negative
        row, col = overflow_tuples[0]
        if grid[row][col]>0:
            overflow_sign = 1
        else:
            overflow_sign = -1
            
        
        #make overflow cells zero
        for(row, col) in overflow_tuples:           
            grid[row][col] = 0
            
        
        #add 1 and make neighbours same as the OF sign
        for(row, col) in overflow_tuples:
            
            #corner
            if (row == 0 or row == total_rows-1) and (col == 0 or col == total_cols-1):

                if row == 0 and col == 0:
                    
                    value = abs(grid[row+1][col]) + 1
                    value *= (overflow_sign)
                    grid[row+1][col] = value

                    value = abs(grid[row][col+1]) + 1 
                    value *= (overflow_sign)
                    grid[row][col+1] = value
                                   
                if row == 0 and col == total_cols-1:

                    value = abs(grid[row+1][col]) + 1
                    value *= (overflow_sign)
                    grid[row+1][col] = value
                    
                    value = abs(grid[row][col-1]) + 1
                    value *= (overflow_sign)
                    grid[row][col-1] = value
                    
                if row == total_rows-1 and col == 0:
                    
                    value = abs(grid[row-1][col]) + 1 
                    value *= (overflow_sign)
                    grid[row-1][col] = value
                    
                    value = abs(grid[row][col+1]) + 1 
                    value *= (overflow_sign)
                    grid[row][col+1] = value
                    
                if row == total_rows-1 and col == total_cols-1:
                   
                   value = abs(grid[row-1][col]) + 1 
                   value *= (overflow_sign)
                   grid[row-1][col] = value
                   
                   value = abs(grid[row][col-1]) + 1
                   value *= (overflow_sign)
                   grid[row][col-1] = value
                
            #edge        
            elif  (row == 0 or row == total_rows-1) and (col >= 1 and col <= total_cols-2):

                if(row == 0):
                    #down                    
                    value = abs(grid[row+1][col]) + 1
                    value *= (overflow_sign)
                    grid[row+1][col] = value

                if(row == total_rows-1):
                    #up
                    value = abs(grid[row-1][col]) + 1 
                    value *= (overflow_sign)
                    grid[row-1][col] = value
                
                #right
                value = abs(grid[row][col+1]) + 1
                value *= (overflow_sign)
                grid[row][col+1] = value
                
                #left
                value = abs(grid[row][col-1]) + 1
                value *= (overflow_sign)
                grid[row][col-1] = value
                
            #edge
            elif (col == 0 or col == total_cols -1) and (row > 0 and row < total_rows-1):
                
                if(col == 0):
                    #right
                    value = abs(grid[row][col+1]) + 1
                    value *= (overflow_sign)
                    grid[row][col+1] = value
                if(col == total_cols-1):
                    #left
                    value = abs(grid[row][col-1]) + 1
                    value *= (overflow_sign)
                    grid[row][col-1] = value
                
                #up
                value = abs(grid[row-1][col]) + 1 
                value *= (overflow_sign)
                grid[row-1][col] = value
                
                #down
                value = abs(grid[row+1][col]) + 1
                value *= (overflow_sign)
                grid[row+1][col] = value
                
            #other
            else:
                #right
                value = abs(grid[row][col+1]) + 1
                value *= (overflow_sign)
                grid[row][col+1] = value
                
                #left
                value = abs(grid[row][col-1]) + 1
                value *= (overflow_sign)
                grid[row][col-1] = value
                
                #up
                value = abs(grid[row-1][col]) + 1 
                value *= (overflow_sign)
                grid[row-1][col] = value
                
                #down
                value = abs(grid[row+1][col]) + 1
                value *= (overflow_sign)
                grid[row+1][col] = value

    
    #make a new grid with the new values
    new_grid = []
    for row in grid:
        new_row = []
        for value in row: 
            new_row.append(value)
        new_grid.append(new_row)
    
    #add the copy of the grid to the queue so that the queue is not altered when the grid is
    a_queue.enqueue(new_grid)
    
    #keep track of how many times a new grid is added 
    counter += 1
    
    return overflow(grid,a_queue,counter)