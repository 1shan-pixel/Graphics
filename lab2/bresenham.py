#for slope less than 1 
def bresenham_less(x0, y0, x1, y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    D = 2*dy - dx
    y = y0

    for x in range(x0, x1 + 1):
        points.append((x, y))
        if D > 0:
            y = y + yi
            D = D - 2*dx
        D = D + 2*dy
    
    return points



#for slope greater than 1 
def bresenham_more(x0, y0, x1, y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx
    D = 2*dx - dy
    x = x0

    for y in range(y0, y1 + 1):
        points.append((x, y))
        if D > 0:
            x = x + xi
            D = D - 2*dy
        D = D + 2*dx
    
    return points


