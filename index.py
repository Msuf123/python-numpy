# GRADED FUNCTION: row_echelon_form
import numpy as  np
def augmented_matrix(A, B):
    augmented_M = np.hstack((A,B))
    return augmented_M
def get_index_first_non_zero_value_from_column(M, column, starting_row):
    column_array = M[starting_row:,column]
    for i, val in enumerate(column_array):
        if not np.isclose(val, 0):

            index = i + starting_row
            return index
    return -1
def swap_rows(M, row_index_1, row_index_2):
    M = M.copy()
    # Swap indexes
    M[[row_index_1, row_index_2]] = M[[row_index_2, row_index_1]]
    return M
def row_echelon_form(A, B):

    det_A = np.linalg.det(A)

    # Returns "Singular system" if determinant is zero
    if np.isclose(det_A, 0) == True:
        return 'Singular system'

    # Make copies of the input matrices to avoid modifying the originals
    A = A.copy()
    B = B.copy()

    # Convert matrices to float to prevent integer division
    A = A.astype('float64')
    B = B.astype('float64')

    # Number of rows in the coefficient matrix
    num_rows = len(A)

    ### START CODE HERE ###

    # Transform matrices A and B into the augmented matrix M
    M = augmented_matrix(A, B)

    # Iterate over the rows.

    new_Matrix=M

    for row in range(num_rows):

        # The first pivot candidate is always in the main diagonal, let's get it.
        # Remember that the diagonal elements in a matrix has the same index for row and column.
        # You may access a matrix value by typing M[row, column]. In this case, column = None

        pivot_candidate = new_Matrix[row,row]


        # If pivot_candidate is zero, it cannot be a pivot for this row.
        # So the first step you need to take is to look at the rows below it to check if there is a non-zero element in the same column.
        # The usage of np.isclose is a good practice when comparing two floats.
        if np.isclose(pivot_candidate, 0) == True:
            # Get the index of the first non-zero value below the pivot_candidate.
            first_non_zero_value_below_pivot_candidate = get_index_first_non_zero_value_from_column(M, row, row)

            # Swap rows
            M = swap_rows(M, row, first_non_zero_value_below_pivot_candidate)

            # Get the pivot, which is in the main diagonal now
            pivot = M[row, row]

            # If pivot_candidate is already non-zero, then it is the pivot for this row
        else:
            pivot = pivot_candidate

            # Now you are ready to apply the row reduction in every row below the current

        # Divide the current row by the pivot, so the new pivot will be 1. You may use the formula current_row -> 1/pivot * current_row
        # Where current_row can be accessed using M[row].
        M[row] = 1/pivot * M[row]

        # Perform row reduction for rows below the current row
        for j in range(row + 1, num_rows):
            # Get the value in the row that is below the pivot value.
            # Remember that, since you are dealing only with non-singular matrices, the pivot is in the main diagonal.
            # Therefore, the values in row j that are below the pivot, must have column index the same index as the column index for the pivot.
            value_below_pivot = M[j,row ]

            # Perform row reduction using the formula:
            # row_to_reduce -> row_to_reduce - value_below_pivot * pivot_row
            M[j] = M[j] - value_below_pivot * M[row]

    ### END CODE HERE ###

    return M
A = np.array([[1,2,3],[0,1,0], [0,0,5]])
B = np.array([[1], [2], [4]])
print(row_echelon_form(A, B))