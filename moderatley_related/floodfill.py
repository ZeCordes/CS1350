import tkinter as tk


NEIGHBORS = [(-1, 0), (1, 0), (0, -1), (0, 1)] # no diagonals

grid_height = 20
grid_width = 20
cell_size = 30

root = tk.Tk()
canvas = tk.Canvas(root, width=grid_width * cell_size, height=grid_height * cell_size, bg="white")
canvas.pack()

grid_colors = [["white" for _ in range(grid_width)] for _ in range(grid_height)]

# This state will hold the color we are painting with during a mouse drag.
_paint_color = None

def draw_grid():
    canvas.delete("all")
    for r in range(grid_height):
        for c in range(grid_width):
            x1 = c * cell_size
            y1 = r * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            canvas.create_rectangle(x1, y1, x2, y2, fill=grid_colors[r][c], outline="black")

def in_bounds(row, col):
    # simple shorthand
    return 0 <= row < grid_height and 0 <= col < grid_width

def start_paint(event):
    """
    Begins a paint session on left-click.
    It determines the paint color (black or white) based on the clicked cell
    and then paints that cell.
    """
    global _paint_color
    column = event.x // cell_size
    row = event.y // cell_size
    if in_bounds(row, column):
        # Set the paint color based on the opposite of the clicked cell's color
        if grid_colors[row][column] == "white":
            _paint_color = "black"
        else:
            _paint_color = "white"
        # Immediately paint the first cell
        paint_on_drag(event)

def stop_paint(event):
    """Ends the paint session when the left mouse button is released."""
    global _paint_color
    _paint_color = None

def paint_on_drag(event):
    """Paints the cell under the mouse if a paint session is active."""
    if _paint_color is None:
        return

    column = event.x // cell_size
    row = event.y // cell_size
    # Only update and redraw if the cell is in bounds and its color is different
    if in_bounds(row, column) and grid_colors[row][column] != _paint_color:
        grid_colors[row][column] = _paint_color
        draw_grid()

def flood_fill(event):
    # on right click, flood-fill all connected cells of the same color to red or white if already red (to undo flood fill)
    start_col = event.x // cell_size
    start_row = event.y // cell_size
    if in_bounds(start_row, start_col):
        target_color = grid_colors[start_row][start_col]
        new_color = "white" if target_color == "red" else "red"
    
        to_fill = set()
        to_fill.add((start_row, start_col))
        filled = set()

        while to_fill:
            row, col = to_fill.pop()
            if (row, col) in filled:
                continue # shouldn't happen, but just in case
            filled.add((row, col))
            grid_colors[row][col] = new_color
            for delta_r, delta_c in NEIGHBORS:
                neighbor_r, neighbor_c = row + delta_r, col + delta_c
                if in_bounds(neighbor_r, neighbor_c) and grid_colors[neighbor_r][neighbor_c] == target_color:
                    if (neighbor_r, neighbor_c) not in filled:
                        to_fill.add((neighbor_r, neighbor_c))
    
    draw_grid()
        
                
        

canvas.bind("<Button-1>", start_paint)
canvas.bind("<B1-Motion>", paint_on_drag)
canvas.bind("<ButtonRelease-1>", stop_paint)
canvas.bind("<Button-3>", flood_fill)

draw_grid()
root.mainloop()
