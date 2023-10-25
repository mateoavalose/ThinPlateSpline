import Files.Functions as func
from Files.TPS import TPS
import numpy as np
import matplotlib.pyplot as plt

def runApp(csv_file):
    # Separate the data from the CSV file into two arrays
    x_values, fx_values = func.csv_to_arrays(csv_file)

    # Build the A matrix
    print("What radial base function do you want (RBF)?")
    print("1. Thin Plate Spline")
    print("2. Gaussian")
    print("3. Multiquadric")
    print("4. Inverse Multiquadric")
    print("5. Cubic")
    RBF_Type = input("Type the number of your choice: ")
    print("--------------------")
    if RBF_Type == "1":
        ### Thin Plate Spline (TPS) is the only radial base function implemented
        # Create the TPS object
        degree = input("You chose Thin Plate Spline: what degree do you want? ")
        b = input("What value of b do you want? ")
        tpsFunction:TPS = TPS(degree = 1, b = 1, x_values = x_values)
        # Calculate the centres and the weight matrix
        A = tpsFunction.matrix_A()
        w = func.invA_weight(A, fx_values)
        # Interpolation points
        fx_interpolated = []
        n = int(input("How many interpolation points do you want? "))
        x_interpolated = np.random.uniform(min(x_values), max(x_values), n)
        for i in range(n):
            fx_interpolated.append(tpsFunction.interpolate(w, x_interpolated[i]))
    elif RBF_Type == "2":
        ### Gaussian RBF
        print("Gaussian RBF not implemented yet")
        return
    elif RBF_Type == "3":
        ### Multiquadric RBF
        print("Multiquadric RBF not implemented yet")
        return
    elif RBF_Type == "4":
        ### Inverse Multiquadric RBF
        print("Inverse Multiquadric RBF not implemented yet")
        return
    elif RBF_Type == "5":
        ### Cubic RBF
        print("Cubic RBF not implemented yet")
        return
    else:
        print("Invalid choice")
        return

    ### Plot the interpolated data points

    # Graph Original Function
    x_sine = np.arange(0, 4*np.pi, 0.1)   # start, stop, step
    y_sine = np.sin(x_sine)
    plt.plot(x_sine, y_sine, color='blue', linewidth=2.0, linestyle='-', label="Original Function")

    # Graph the original points
    print("Do you want to graph the original points? (y/n)")
    graphOriginal = input("Type y or n: ")
    if graphOriginal == "y":
        plt.scatter(x_values, fx_values, color='green', marker='o', label="Original Points")
    # Graph the interpolated points
    plt.scatter(x_interpolated, fx_interpolated, color='red', marker='x', label="Interpolated Points")
    plt.legend(loc='upper left')
    plt.show()