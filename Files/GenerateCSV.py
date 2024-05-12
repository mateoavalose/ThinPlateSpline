import csv
import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LinearLocator

def generate_random_points(n, startX, endX, startY, endY, function):
    points = []
    for _ in range(n):
        x = random.uniform(startX, endX)
        y = random.uniform(startY, endY)
        fx = function(x, y)
        points.append((x, y, fx))
    return points

def save_points_to_csv(points, filename):
    with open(filename, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['x', 'y', 'f(x)'])  # Write header
        for point in points:
            csv_writer.writerow(point)

# Main program
output_file = "DataSets/function_points.csv"

lowLimitX = -5
highLimitX = 5
lowLimitY = -5
highLimitY = 5
nPoints = 500

def eval_function(x, y):
    return x**2 * np.sin(y)

random_points = generate_random_points(n=nPoints, startX=lowLimitX, endX=highLimitX, startY=lowLimitY, endY=highLimitY, function=eval_function)
save_points_to_csv(random_points, output_file)
print(f"Random points saved to {output_file}")

# Graph the points using matplotlib
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
x_values = [point[0] for point in random_points]
y_values = [point[1] for point in random_points]
z_values = [point[2] for point in random_points]
ax.scatter(x_values, y_values, z_values, c='black', marker='o')
#plt.show()

# Graph the function
#fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
x_func = np.arange(lowLimitX, highLimitX, 0.01)   # start, stop, step
y_func = np.arange(lowLimitY, highLimitY, 0.01)   # start, stop, step
x_func, y_func = np.meshgrid(x_func, y_func)
z_func = x_func ** 2 * np.sin(y_func) #eval_function(x_func, y_func)
surf = ax.plot_surface(x_func, y_func, z_func, linewidth=0, antialiased=True, cmap='viridis') # type: ignore
# Customize the z axis.
ax.set_zlim(-40, 40) # type: ignore
ax.zaxis.set_major_locator(LinearLocator(10)) # type: ignore
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}') # type: ignore

plt.show()