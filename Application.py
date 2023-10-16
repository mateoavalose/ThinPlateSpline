import Functions as func
import numpy as np

def runApp(csv_file):
    print()
    # Separate the data from the CSV file into two arrays
    x_values, fx_values = func.csv_to_arrays(csv_file)
    print("X Values from CSV:", x_values)
    print("f(X) Values from CSV:", fx_values)

    print()
    # Build the A matrix
    print("What radial base function do you want (RBF)? Type the number of your choice:")
    print("1. Thin Plate Spline")
    #print("2. Gaussian 3. Multiquadric 4. Inverse Multiquadric 5. Cubic")
    RBF_Type = input()
    if RBF_Type == "1":
        print("You chose Thin Plate Spline")
    else:
        pass

    print()
    # Thin Plate Spline (TPS) is the only radial base function implemented
    TPS_centres = func.TPS_Centres(x_values)
    A = func.TPS_matrix_A(degree = 1, b = 1, TPS_Centres = TPS_centres, x_values = x_values)
    print("A matrix:\n", A)
    print("b matrix:\n", fx_values)
    
    print()
    A_inv = np.linalg.inv(A)
    print("A inverse:\n", A_inv)

    print()
    w = np.matmul(A_inv, fx_values)
    print("w matrix size:", w.shape)
    print("w matrix:\n", w)