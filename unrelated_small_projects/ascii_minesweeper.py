from random import randint, sample

# Board Settings (these are the default settings, feel free to change them) (8x8 default, heh chessboard settings [this does not line up with an actual chessboard as A1 is in the bottom left of a chessboard, not the top left])
NUM_ROWS = 8 # max: 98 (99 would proce a label of 100, which would work but offset the last row)
NUM_COLS = 8 # max: 26 (for each letter, this wont work if you go over the max unless you change the LETTER_MAP)
NUM_MINES = 10 # the number of mines on the board
DELTA_MODE = False # i stole this from 4d minesweeper, it makes more sense there but the functionality is still nice

LETTER_MAP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # for the x axis of the board, must be unique and uppercase (result of the .upper() function), currently the 26 letters of the alphabet
# the y axis just uses numbers (1 indexed so it looks nicer)


def main():
    start_y, start_x = randint(0, NUM_ROWS - 1), randint(0, NUM_COLS - 1) # random starting position
    board, game_state = new_game((start_y, start_x)) # create a new game board
    board, game_state = reveal_cell(board, game_state, start_y, start_x) # reveal the starting cell
    
    print_board(board, game_state) # show the board
    # game loop
    while True:
        # prompt the user for input
        while True: # validation loop
            temp = input(f"Enter 'r' to reveal a cell, 'f' to flag (or unflag) a cell, h to view help, or 'q' to quit: ").lower().strip() # make the input lowercase and remove whitespace
            if temp == '': # if the input is empty, ask for input again
                print('Please enter a letter.')
                continue
            
            action = temp[0] # get the first character of the input (this is a bit of a hack, but it works)
            if action in ['r', 'f', 'h', 'q', 'd']: # check if the input is valid
                break # if the input is valid, break the loop
            else:
                print('Please enter a valid action [r, f, h, q].') # exclude the debug command from the prompt, its not a normal action so the user shouldn't know about it
        
        if action == 'r': # reveal action
            x = get_letter_map_input('Enter the x coordinate of the cell to reveal: ', 0, NUM_COLS - 1)
            y = get_int_input('Enter the y coordinate of the cell to reveal: ', 1, NUM_ROWS) - 1 # correct for 0 indexing
            
            if board[y][x]['is_revealed']: # if the cell is revealed do 'chord' detection
                # reveal all neighboring cells if there are a number of adjacent flags equal to the number of adjacent mines (can easily end the game, but this is an assumed risk)
                neighbors = get_adjacent_cells(y, x)
                if board[y][x]['num_adjacent_flags'] >= board[y][x]['num_adjacent_mines']: # if the number of adjacent flags is equal to the number of adjacent mines then 'use' the 'chord'
                    for a_y, a_x in neighbors:
                        if not board[a_y][a_x]['is_flagged']: # if the adjacent cell is not flagged, reveal it
                            board, game_state = reveal_cell(board, game_state, a_y, a_x)
            else:
                board, game_state = reveal_cell(board, game_state, y, x)
        
        elif action == 'f': # flag action
            x = get_letter_map_input('Enter the x coordinate of the cell to flag: ', 0, NUM_COLS - 1)
            y = get_int_input('Enter the y coordinate of the cell to flag: ', 1, NUM_ROWS) - 1 # correct for 0 indexing
            
            if not board[y][x]['is_revealed']: # not revealed
                if board[y][x]['is_flagged']:
                    board = unflag_cell(board, game_state, y, x) # unflag the cell
                else:
                    board = flag_cell(board, game_state, y, x) # flag the cell
            elif board[y][x]['is_revealed']: # if the cell is revealed, don't allow flagging
                print("You can't flag a revealed cell")
            else:
                print('Invalid coordinates')
        
        elif action == 'h': # help action
            print("""
            Enter 'r' to reveal a cell
            Enter 'f' to flag (or unflag) a cell
            Enter 'h' to view help
            Enter 'q' to quit
            
            You can activate a 'chord' by revealing a cell with a number of adjacent flags equal to the number of adjacent mines (its displayed number). This will reveal all neighboring cells.
            
            The x axis is represented by letters (A-Z) and the y axis is represented by numbers starting from 1.
            
            The game will end if you reveal a mine (loss) or if you reveal all the cells that are not mines. (win)""")
            
        elif action == 'q': # quit action
            confirmation = input('Are you sure you want to quit? (y/n): ').lower().startswith('y') # check if the user wants to quit
            if confirmation:
                break
        
        elif action == 'd': # debug action (for testing purposes)
            # regenerate the board
            start_y, start_x = randint(0, NUM_ROWS - 1), randint(0, NUM_COLS - 1) # random starting position
            board, game_state = new_game((start_y, start_x)) # create a new game board
            board, game_state = reveal_cell(board, game_state, start_y, start_x) # reveal the starting cell
            if game_state['is_dead']:
                print('DEBUG ERROR: starting cell was not safe')
        
        print_board(board, game_state) # show the board
        
        # check if the game is over
        if game_state['is_dead'] or game_state['has_won']:
            print('You win!' if game_state['has_won'] else 'You lost :(')
            again = input("Enter 'y' to play again, or 'n' to quit: ").lower().startswith('y') # check if the user wants to play again
            if not again: # if the user doesn't want to play again, ask for confirmation to quit 
                confirmation = input('Are you sure you want to quit? (y/n): ').lower().startswith('y') # check if the user wants to play again
                if confirmation: # if the user wants to quit, break the loop
                    break # leave the loop, the regeneration of the game board will not run
            
            # happens if the user enters 'y' to play again or doesn't enter 'y' in quit confirmation
            start_y, start_x = randint(0, NUM_ROWS - 1), randint(0, NUM_COLS - 1) # random starting position
            board, game_state = new_game((start_y, start_x)) # create a new game board
            board, game_state = reveal_cell(board, game_state, start_y, start_x)
            print_board(board, game_state)


# -- Board Generation Functions --

def new_game(start_pos: tuple) -> tuple[list[list[dict[str, int|bool]]], dict[str, bool]]:
    """Makes and populates a game board then returns the board and the base game state.

    Args:
        start_pos (tuple): (y, x) the 'start point' of the game, a 3x3 centered on this point cannot have any mines

    Returns:
        list[list[cell_state_list]]: the game board
        dict: the game state
    """
    board = []
    available_for_mines = [] # cells that can be used for mines (not in the 3x3 centered on the start position)
    for y in range(NUM_ROWS):
        row = []
        for x in range(NUM_COLS):
            row.append({
                'num_adjacent_mines': 0,
                'is_revealed': False,
                'is_mine': False,
                'is_flagged': False,
                'num_adjacent_flags': 0
                }) # some comments may refer to the original cell state list
            if y < start_pos[0] - 1 or y > start_pos[0] + 1 or x < start_pos[1] - 1 or x > start_pos[1] + 1: # if the cell is not in the 3x3 centered on the start position
                available_for_mines.append((y, x)) # add the cell position tuple to the available cells for mines
        
        board.append(row) # add the row to the board
    
    mines = sample(available_for_mines, NUM_MINES) # randomly select the mines from the available cells

    for y, x in mines:
        board[y][x]['is_mine'] = True
    
    for y in range(NUM_ROWS):
        for x in range(NUM_COLS):
            if board[y][x]['is_mine']: # dont count adjeacent mines for cells that are themselves mines
                continue
            
            board[y][x]['num_adjacent_mines'] = count_adjacent_mines(board, y, x)
    
    
    return board, {'is_dead': False, 'has_won': False} # returns the populated board and the base game state


def count_adjacent_mines(board, y, x):
    num_adjacent_mines = 0
    
    adjacent_cells = get_adjacent_cells(y, x)
    for adj_y, adj_x in adjacent_cells:
        if board[adj_y][adj_x]['is_mine']: # if the cell is a mine
            num_adjacent_mines += 1
    
    return num_adjacent_mines

# -- Board Display Functions --

def print_board(board, state):
    if not state['is_dead']:
        cells = flatten_list(board) # flatten the board to a single list
        mines_left = NUM_MINES # set the mines left to the number of mines
        
        for cell in cells:
            if cell['is_flagged']:
                mines_left -= 1 # allow the 'mines left' counter to be negative (this is a feature, it shows the user that they have 'false flags')
        
        print(f'Mines left: {mines_left}')
    
    print()
    print('     ' + ' '.join(LETTER_MAP[:NUM_COLS])) # puts a space between each letter in the spliced LETTER_MAP, along with leading spaces to align the labels with the cells
    print()
    
    for row_index in range(len(board)):
        if row_index < 9: print(' ', end='') # add a space for single digit numbers to align the board
        print(row_index + 1, end='   ') # print 1-indexed numbers for the y axis
        for j in range(len(board[row_index])):
            print(get_cell_icon(board[row_index][j], is_death=state['is_dead'], delta=DELTA_MODE), end=' ')
        print(' ', row_index + 1) # with newline end to move the cursor to the next line
    
    print()
    print('     ' + ' '.join(LETTER_MAP[:NUM_COLS]))
    print()


def get_cell_icon(cell_dict, is_death=False, delta=False): # its a big conditional tree, peek programming
    num_adjacent_mines = cell_dict['num_adjacent_mines']
    is_revealed = cell_dict['is_revealed']
    is_mine = cell_dict['is_mine']
    is_flagged = cell_dict['is_flagged']
    
    if is_death:
        if is_flagged:
            if is_mine:
                return '>'
            else:
                return 'X' # false flag
        elif is_mine:
            return '*'
        else:
            return ' '
    else:
        if is_flagged:
            return '>'
        elif is_revealed:
            if is_mine or is_flagged:
                return '%' # error icon (shouldn't show up)
            else:
                n = num_adjacent_mines
                
                if n == 0:
                    return '.'
                else:
                    if delta:
                        n -= cell_dict['num_adjacent_flags'] # subtract the number of adjacent flags from the number of adjacent mines (this is what delta mode does, it is purely visual and does not affect game logic)
                    
                    if n < 0:
                        return '!' # return ! as negative numbers are 2 characters ('-', '1') and that breaks everything
                    
                    return str(n)
        else:
            return '#'

# -- Board Handling Functions --

def reveal_cell(board, state: dict[str, bool], y: int, x: int) -> tuple[list[list[dict[str, int|bool]]], dict[str, bool]]: # recursive function to reveal a cell and all adjacent cells if the cell has no adjacent mines
    if state['is_dead']:
        return
    
    board[y][x]['is_revealed'] = True # reveal the cell
    is_mine = board[y][x]['is_mine']
    reveal_neighbors = board[y][x]['num_adjacent_mines'] == 0 # check if the cell has no adjacent mines
    
    if is_mine:
        state['is_dead'] = True
        return board, state # return the board and state early
    
    if reveal_neighbors:
        for a_y, a_x in get_adjacent_cells(y, x):
            if not (board[a_y][a_x]['is_revealed'] or board[a_y][a_x]['is_flagged']): # if the cell is neither revealed nor flagged
                board, state = reveal_cell(board, state, a_y, a_x) # NOTE: this may raise a recursion error if the board is too big, but it should be fine for the default settings (8x8)
                # possible TODO if project was continued: use a proper flood-fill algorithm instead of recursion
    
    if is_solved(board):
        state['has_won'] = True # if all safe cells are revealed, the game is won
    
    return board, state # return the updated board and state


def is_solved(board) -> bool:
    # checks if all safe cells are revealed (i.e. all cells that are not mines), this is the most common way to check if a minesweeper game is won
    cells = flatten_list(board) # flatten the board to a single list

    for cell in cells:
        if not (cell['is_revealed'] or cell['is_mine']): # if any cell is neither revealed nor a mine, the board is not solved (python wont let me use nor as a keyword :[ )
            return False
    
    return True # return True if all cells are revealed or are mines (the function will return earlier if this is not the case)

def flag_cell(board, state, y, x) -> list[list[dict[str, int|bool]]]:
    if state['is_dead']:
        return
    
    board[y][x]['is_flagged'] = True
    
    # update all neighbors adjacent flag count
    for a_y, a_x in get_adjacent_cells(y, x):
        board[a_y][a_x]['num_adjacent_flags'] += 1 # increment num_adjacent_flags

    return board # flagging doesn't effect the state so just return the board


def unflag_cell(board, state, y, x) -> list[list[dict[str, int|bool]]]:
    if state['is_dead']:
        return
    
    board[y][x]['is_flagged'] = False
    
    # update all neighbors adjacent flag count
    for a_y, a_x in get_adjacent_cells(y, x):
        board[a_y][a_x]['num_adjacent_flags'] -= 1 # decrement num_adjacent_flags
    
    return board # unflagging also doesn't affect the game state


def get_adjacent_cells(y: int, x: int) -> list[tuple[int, int]]:
    adjacent_cells = []
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dy == 0 and dx == 0: # skip the current cell
                continue
            
            if 0 <= y + dy < NUM_ROWS and 0 <= x + dx < NUM_COLS: # check if the cell is within bounds
                adjacent_cells.append((y + dy, x + dx))

    return adjacent_cells


# -- HELPER FUNCTIONS --
# these aren't made exclusively for the game, but are used in the game so they are here
def flatten_list(nested_list: list[list]) -> list:
    flattened = []
    for sublist in nested_list:
        flattened += sublist # add the sublist to the flattened list
    return flattened # return the flattened list


def get_int_input(prompt, min_val, max_val):
    """Contuniously prompts the user for an integer until a valid input is given in the specified range (inclusive).

    Args:
        prompt (str): prompt to be used for input command
        min_val (int): the minimum value for the input (inclusive)
        max_val (int): the maximum value for the input (inclusive)

    Returns:
        int: the valid integer input from the user
    """
    while True:
        temp = input(prompt)
        if temp.isdigit() and not '.' in temp:  # check if the input is a number and not a float
            value = int(temp)
            if min_val <= value <= max_val:
                return value
            else:
                print(f'Please enter a value between {min_val} and {max_val}.')
        else:
            print('Invalid input. Please enter a valid integer.')


def get_letter_map_input(prompt, min_val, max_val, can_number=True):
    """Contuniously prompts the user for a letter in the defined constant LETTER_MAP until a valid input is given in the specified range (inclusive).

    Args:
        prompt (str): prompt to be used for input command
        min_val (int): the minimum value for the input (inclusive)
        max_val (int): the maximum value for the input (inclusive)
        can_number (bool, optional): Whether to allow the user to enter a number to shortcut the map. Defaults to True.

    Returns:
        int: the mapped integer value of the letter input from the user
    """
    min_letter, max_letter = LETTER_MAP[min_val], LETTER_MAP[max_val] # get the letters for the min and max values (shortens the code)
    while True:
        temp = input(prompt)
        temp = temp.upper().strip() # make the input uppercase and remove whitespace
        if temp == '': # if the input is empty, ask for input again
            print('Please enter a letter.')
            continue
        
        temp = temp[0] # get the first character of the input (this is a bit of a hack, but it works)
        if can_number and temp.isdigit() and not '.' in temp:  # check if the input is a number and not a float
            value = int(temp)
            if min_val <= value <= max_val:
                return value
            else:
                print(f'Please enter a value between {min_val} ({min_letter}) and {max_val} ({max_letter}).') # only clarify the integer values if the user entered a number
        elif temp in LETTER_MAP[min_val:max_val + 1]: # check if the input is a letter in the range of the min and max values
            return LETTER_MAP.index(temp) + min_val # return the index of the letter in the LETTER_MAP + min_val to get the correct index
        else:
            print(f'Please enter a letter between {min_letter} and {max_letter}.')
          


  
main() # run everything
print('Thanks for playing!') # displays when the user quits