
def dda_line(x0, y0, x1, y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    x_inc = dx / steps
    y_inc = dy / steps
    #if m>1 , then inc will be m , if less than 1 , then inc will be 1/m

    x = x0
    y = y0
    points.append((round(x), round(y)))

    for _ in range(int(steps)):
        x += x_inc
        y += y_inc
        points.append((round(x), round(y)))
    
    return points

# Example usage
points = dda_line(2, 3, 10, 7)
for point in points:
    print(point)
