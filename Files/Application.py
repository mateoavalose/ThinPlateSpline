import Files.Functions as func
from Files.TPS import TPS
import numpy as np
import matplotlib.pyplot as plt

def runApp(csv_file):
    # Separate the data from the CSV file into two arrays
    x_values, y_values, fxy_values = func.csv_to_arrays(csv_file)

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
        degree = input("You chose Thin Plate Spline: choose a value for a (degree): ")
        b = input("Choose a value for b: ")
        input("Press Enter to calculate the weight matrix. ...")
        tpsFunction:TPS = TPS(degree = degree, b = b, x_values = x_values, y_values = y_values)
        # Calculate the centres and the weight matrix
        A = tpsFunction.matrix_A()
        w = func.invA_weight(A, fxy_values)
        # Interpolation points
        fx_interpolated = []
        n = int(input("\nHow many interpolation points do you want? "))
        x_interpolated = np.random.uniform(min(x_values), max(x_values), n)
        y_interpolated = np.random.uniform(min(y_values), max(y_values), n)
        for i in range(n):
            fx_interpolated.append(tpsFunction.interpolate(w, x_interpolated[i], y_interpolated[i]))
        calcDerivative = input("Do you want to calculate the derivative and second derivative? (y/n): ")
        if calcDerivative == "y":
            fxy_interpolated_derivativeX = []
            fxy_interpolated_derivativeY = []
            fxy_interpolated_derivative2X = []
            fxy_interpolated_derivative2Y = []
            for i in range(n):
                fxy_interpolated_derivativeX.append(tpsFunction.interpolateDerivateX(w, x_interpolated[i], y_interpolated[i]))
                fxy_interpolated_derivativeY.append(tpsFunction.interpolateDerivateY(w, x_interpolated[i], y_interpolated[i]))
                fxy_interpolated_derivative2X.append(tpsFunction.interpolateDerivate2X(w, x_interpolated[i], y_interpolated[i]))
                fxy_interpolated_derivative2Y.append(tpsFunction.interpolateDerivate2Y(w, x_interpolated[i], y_interpolated[i]))
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
    # Graph the interpolated points
    fig = plt.figure()
    if calcDerivative == "y":
        ax1 = fig.add_subplot(4, 2, (1,4), projection='3d')
    else:
        ax1 = fig.add_subplot(projection='3d')
    ax1.scatter(x_interpolated, y_interpolated, fx_interpolated, color='red', marker='o', label="Interpolated Points")
    plt.legend(loc='upper left')

    # Graph the original points
    graphOriginal = input("\nDo you want to graph the original points? (y/n): ")
    if graphOriginal == "y":
        ax1.scatter(x_values, y_values, fxy_values, color='blue', marker='x', label="Original Points")
        ax1.legend(loc='upper left')

    # Graph the derivative and second derivative of the interpolated points
    if calcDerivative == "y":
        ### First Derivative in X
        ax2 = fig.add_subplot(4, 2, 3, projection='3d')
        ax2.scatter(x_interpolated, fxy_interpolated_derivativeX, color='blue', marker='o', label="Derivative of Interpolated Points in X")
        ax2.legend(loc='upper left')

        ### First Derivative in Y
        ax3 = fig.add_subplot(4, 2, 4, projection='3d')
        ax3.scatter(y_interpolated, fxy_interpolated_derivativeY, color='green', marker='o', label="Derivative of Interpolated Points in Y")
        ax3.legend(loc='upper left')

        ### Second Derivative in X
        ax4 = fig.add_subplot(4, 2, 5, projection='3d')
        ax4.scatter(x_interpolated, fxy_interpolated_derivative2X, color='purple', marker='o', label="Second Derivative of Interpolated Points in X")
        ax4.legend(loc='upper left')

        ### Second Derivative in Y
        ax5 = fig.add_subplot(4, 2, 6, projection='3d')
        ax5.scatter(y_interpolated, fxy_interpolated_derivative2Y, color='orange', marker='o', label="Second Derivative of Interpolated Points in Y")
        ax5.legend(loc='upper left')
    
    plt.show()