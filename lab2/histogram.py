import numpy as np
import matplotlib.pyplot as plt

# Bresenham's line algorithm
def bresenham(x0, y0, x1, y1):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while True:
        points.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    
    return points

# Sample data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Define number of bins
num_bins = 4

# Calculate histogram using numpy
hist, bin_edges = np.histogram(data, bins=num_bins)

# Define dimensions
hist_height = 100
hist_width = 200

# Determine the scaling factor
max_freq = max(hist)
scale_factor = hist_height / max_freq

# Initialize the histogram array
histogram = np.zeros((hist_height, hist_width), dtype=int)

# Define bar width
bar_width = hist_width // num_bins

# Draw the histogram
for i, frequency in enumerate(hist):
    bar_height = int(frequency * scale_factor)
    x0, y0 = i * bar_width, hist_height - 1
    x1, y1 = x0, hist_height - 1 - bar_height
    
    for x, y in bresenham(x0, y0, x1, y1):
        for bw in range(bar_width):  # Fill the bar width
            if x + bw < hist_width and y < hist_height:
                histogram[y, x + bw] = 1

# Visualizing the histogram
plt.imshow(histogram, cmap='autumn', origin='lower')
plt.title('Histogram using Bresenham\'s Line Algorithm')
plt.show()
