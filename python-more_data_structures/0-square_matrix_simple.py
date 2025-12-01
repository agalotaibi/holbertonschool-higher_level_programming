#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in range(len(matrix)):
        new_row = []
        for j in matrix[i]:
            squared_value = j ** 2
            new_row.append(squared_value)
        new_matrix.append(new_row)
    return new_matrix    
