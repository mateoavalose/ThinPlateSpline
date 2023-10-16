import csv
import random
import math

def generate_random_points(n, start, finish, function):
    points = []
    for _ in range(n):
        x = random.uniform(start, finish)
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
n = 3  # Number of random points to generate
output_file = "sine_points.csv"

random_points = generate_random_points(n, 0, 2*math.pi, eval_function)
save_points_to_csv(random_points, output_file)
print(f"{n} random points saved to {output_file}")