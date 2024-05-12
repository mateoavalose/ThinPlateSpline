import csv
import random
import math
import matplotlib.pyplot as plt

def generate_random_points(n, start, end, function):
    points = []
    for _ in range(n):
        x = random.uniform(start, end)
        fx = function(x)
        points.append((x, fx))
    return points

def eval_function(x):
    return math.sin(x)

def save_points_to_csv(points, filename):
    with open(filename, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(['x', 'f(x)'])  # Write header
        for point in points:
            csv_writer.writerow(point)

# Main program
output_file = "DataSets/sine_points.csv"

random_points = generate_random_points(n=100, start=0, end=4*math.pi, function=eval_function)
save_points_to_csv(random_points, output_file)
print(f"Random points saved to {output_file}")

# Graph the points using matplotlib
x_values = [point[0] for point in random_points]
y_values = [point[1] for point in random_points]
plt.scatter(x_values, y_values)
plt.show()