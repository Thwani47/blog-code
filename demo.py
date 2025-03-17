"""
Skeleton code for CS114 project 2025: A QR code generator.

This skeleton code for the project is intended as a starting point for students
to get an idea of how they can begin to code the project. You are not required
to use any of the functions in this skeleton code, however you may find some of
the ideas useful. Your code, however, is required to have the line:

if __name__ == "__main__":

but you are free to and should modify the lines following this.

None of the functions are implemented yet, so if you would like to
use a particular function, you need to implement it yourself. If you decide not
to use any of the functions, you are free to leave them empty or remove them
from this file. You are also free to alter the function signatures (the name of
the function and its arguments), so if you need to pass more arguments to the
function, or do not need a particular argument, you are also free to add and
remove arguments as you see fit. We provide the function signatures only as a
guide for how we think you can start to approach the project.
"""

# imports
import os
import sys
# Your imports go here
import stdio

# global variables
# Your global variables go here


def draw_qr_grid(qr_grid):
    """
    Draws the given qr data onto the canvas of stddraw in the format specified in
    the project specification.

    Args:
        qr_grid (2D array of int): The data of the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def print_qr_grid(qr_grid):
    """
    Prints the given qr data out to the standard output in the format specified in
    the project specification.

    Args:
        qr_grid (2D array of int): The data of the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    for row in qr_grid:
        for index,cell in enumerate(row):
            if index != len(qr_grid) -1 :
                stdio.write(f"{cell} ")
            else:
                stdio.write(cell)
        stdio.writeln()


def make_position_pattern(pos_square_size):
    """
    Creates the position pattern of size pos_square_size and returning it as a
    2-dimensional array of int.

    Args:
        pos_square_size (int): The size of the position pattern to generate

    Returns:
        2D array of int: The position pattern
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pattern = [[0 for _ in range(pos_square_size)] for _ in range(pos_square_size)]
    
    if pos_square_size == 4:
        # Fill the first 3 columns of the first 3 rows with 1s
        for i in range(3):
            for j in range(3):
                pattern[i][j] = 1
    
    elif pos_square_size == 6:
        # Fill the last column with 1s except the last position
        for i in range(pos_square_size - 1):
            pattern[i][pos_square_size - 1] = 1
            
        # Fill the last row with 1s
        for j in range(pos_square_size):
            pattern[pos_square_size - 1][j] = 1
            
        # Fill the middle 3x3 square with 1s
        for i in range(1, 4):
            for j in range(1, 4):
                pattern[i][j] = 1
    
    else:  # pos_square_size >= 8
        # Fill the first column with 1s except the last position
        for i in range(pos_square_size - 1):
            pattern[i][0] = 1
            
        # Fill the first row with 1s except the last position
        for j in range(pos_square_size - 1):
            pattern[0][j] = 1
            
        # Fill the 7th column with 1s except the last position
        for i in range(pos_square_size - 1):
            pattern[i][pos_square_size - 2] = 1
            
        # Fill the 7th row with 1s except the last position
        for j in range(pos_square_size - 1):
            pattern[pos_square_size - 2][j] = 1
            
        # Fill the inner square pattern (3x3) repeated
        inner_start = 2
        inner_end = pos_square_size - 3
        for i in range(inner_start, inner_end):
            for j in range(inner_start, inner_end):
                pattern[i][j] = 1
                
    return pattern
                    


def make_alignment_pattern(align_square_size):
    """
    Creates the alignment pattern of size align_square_size and returning it as
    a 2-dimensional array of int.

    Args:
        align_square_size (int): The size of the alignment pattern to generate

    Returns:
        2D array of int: The alignment pattern
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    align_pattern = [[0 for _ in range(align_square_size)] for _ in range(align_square_size)]
    
    for row in range(align_square_size):
        align_pattern[0][row] = 1
        align_pattern[align_square_size-1][row] = 1
        align_pattern[row][0] = 1
        align_pattern[row][align_square_size-1] = 1
        
    for row in range(2, align_square_size-2):
        for col in range(2, align_square_size-2):
            if (row-2) % 2 == 0 and (col - 2) % 2 == 0:
                align_pattern[row][col] = 1
    
    return align_pattern

def rotate_pattern_clockwise(data):
    """
    Rotates the values in data clock-wise by 90 degrees

    Args:
        data (2D array of int): The array that should be rotated
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    size = len(data)
    rotated_grid = [[0 for _ in range(size)] for _ in range(size)]
    
    for row in range(size):
        for col in range(size):
            rotated_grid =[col][size - row - 1 ] = data[row][col]
            
    return rotated_grid


def add_data_at_anchor(qr_grid, anchor_x, anchor_y, data):
    """
    Places values contained in data to the qr_grid starting as positions given
    by achnor_x and anchor_y.

    Args:
        qr_grid (2D array of int): The QR grid
        anchor_x (int): the x position from where the data should be added
        anchor_y (int): the y position from where the data should be added
        data (2D array of int): The data that should be added to the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def add_data_snake(qr_grid, data):
    """
    Places values contained in data to the qr_grid in the snake layout as
    specified in the project specifications.

    Args:
        qr_grid (2D array of int): The QR grid
        data (array of int): The bit sequence of data that should be added to
        the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def add_data_real(qr_grid, data):
    """
    Places values contained in data to the qr_grid in the real layout as
    specified in the project specifications.

    Args:
        qr_grid (2D array of int): The QR grid
        data (array of int): The bit sequence of data that should be added to
        the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def apply_mask(qr_grid, reserved_positions, mask_id):
    """
    Applies the masking pattern specified by mask_id to the QR grid following
    the masking rules as specified by the project specifications.

    Args:
        qr_grid (2D array of int): The QR grid
        reserved_positions (2D array of int): the reserved positions
        mask_id (str): The mask id to apply to the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass

def encode_real(size, message, information_bits, pos_square_size, align_square_size):
    """
    Generates the QR code according to the project specifications using the
    real layout.

    Args:
        size (int): The size of the QR grid to be generated
        message (str): The message to be encoded
        information_bits (array of int): the 15-bit information pattern
        pos_square_size (int):  The size of the position pattern to generate
        align_square_size (int):  The size of the alignment pattern to generate

    Returns:
        2D array of int: The completed QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def encode_snake(size, message, pos_square_size, align_square_size):
    """
    Generates the QR code according to the project specifications using the
    snake layout.

    Args:
        size (int): The size of the QR grid to be generated
        message (str): The message to be encoded
        pos_square_size (int):  The size of the position pattern to generate
        align_square_size (int):  The size of the alignment pattern to generate

    Returns:
        2D array of int: The completed QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def main(args, message):
    # TODO: put logic here to check if the command-line arguments are correct,
    # and then call the game functions using these arguments.
    
    # The program takes in 4 command-line arguments (5 including the program name)
    if len(args) < 5:
        stdio.writeln("ERROR: Too few arguments")
        sys.exit()
    elif len(args) > 5:
        stdio.writeln("ERROR: Too many arguements")
        sys.exit()
    
    if not args[1].isdigit(): # encoding_parameter should be an interger
        stdio.writeln(f"ERROR: invalid encoding argument: {args[1]}")
        sys.exit()
        
    encoding_parameter = int(args[1])
        
    if encoding_parameter < 0 or encoding_parameter > 32: #encoding parameter should be between 0 and 32 (all incl.)
        stdio.writeln(f"ERROR: invalid encoding argument: {encoding_parameter}")
        sys.exit()
    
    if not args[2].isdigit(): # grid_size should be an interger
        stdio.writeln(f"ERROR: invalid size argument: {args[2]}")
        sys.exit()
        
    grid_size = int(args[2])
        
    if grid_size < 10 or grid_size > 48: #encoding parameter should be between 0 and 32 (all incl.)
        stdio.writeln(f"ERROR: invalid size argument: {grid_size}")
        sys.exit()
        
    
    if not args[3].isdigit(): # position_pattern_size should be an interger
        stdio.writeln(f"ERROR: Invalid position pattern size argument: {args[3]}")
        sys.exit()
        
    position_pattern_size = int(args[3])
        
    if position_pattern_size <= 3 or  position_pattern_size % 2 != 0: # position_pattern_size has to be > 3 and be an even number
        stdio.writeln(f"ERROR: Invalid position pattern size argument: {position_pattern_size}")
        sys.exit()
    
    if not args[4].isdigit(): # alignment_pattern_size should be an int
        stdio.writeln(f"ERROR: Invalid alignment pattern size argument: {args[4]}")
        sys.exit()        
        
    alignment_pattern_size = int(args[4])
    
    if alignment_pattern_size < 0 or (alignment_pattern_size - 1) % 4 != 0:
        stdio.writeln(f"ERROR: Invalid alignment pattern size argument: {args[4]}")
        sys.exit()
        
        
    total_cells = grid_size * grid_size
    reserved_cells = 3 * position_pattern_size * position_pattern_size + alignment_pattern_size * alignment_pattern_size # 3 position patterns + 1 alignment pattern
    
    remaining_cells = total_cells - reserved_cells
    
    total_bytes = remaining_cells // 8 # divide the remaining cells by 8 to determine how many bytes we can store in these cells 
     
    if len(message) > 255 or len(message) > (total_bytes - 1):
        stdio.writeln("ERROR: Payload too large")
        sys.exit() 
    
    
    # create grid
    # qr_grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
    # print_qr_grid(qr_grid)
    
    pos_pattern = make_position_pattern(4)
    print_qr_grid(pos_pattern)
    
    alignment_pattern = make_alignment_pattern(5)
    print_qr_grid(alignment_pattern)
    


if __name__ == "__main__":
    """Usage: echo 'message' | python3 SUXXXXXXXX.py 'encoding_string' 'size' 'pos_size' 'align_size'"""
    message = stdio.readAll().strip()
    main(sys.argv, message)
