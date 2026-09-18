"""
Draw Line: A monochrome screen is stored as a single array of bytes, allowing eight consecutive pixels to be stored in one byte.
The screen has width w, where w is divisible by 8 (that is, no byte will be split across rows). 
The height of the screen, of course, can be derived from the length of the array and the width. 
Implement a function that draws a horizontal line from (x1, y) to (x2, y) . 
The method signature should look something like: drawLine( byte[] screen, int width, int x1, int x2, int y )
"""
def draw_line(screen: bytearray, width: int, x1: int, x2: int, y: int):
    if width % 8 != 0 :
        raise ValueError("width must be divisible by 8")
    height = len(screen)// bytes_per_row
    if not (0 <= y < height):
        raise ValueError(f"y={y} out of range [0, {height})")

    if x1 > x2:
        x1, x2 = x2, x1

    if not 0 <= x1 <= x2 < width:
        raise ValueError
     
    bytes_per_row = width // 8
    start_byte = y * bytes_per_row + x1 // 8
    end_byte = y * bytes_per_row + x2 // 8
    start_offset = x1 % 8
    end_offset = x2 % 8

    start_mask = 0xFF >> start_offset
    end_mask = (~(0xFF >> (end_offset + 1))) & 0xFF

    if start_byte == end_byte:
        screen[start_byte] = screen[start_byte] | (start_mask & end_mask)
        return

    screen[start_byte] |= start_mask
    for b in range(start_byte+1, end_byte):
        screen[b] = 0xFF
    screen[end_byte] |= end_mask    