matrix = [['a', 'b', 'c'], [ 1,   2,   3 ], ['x', 'y', 'z']]

def matrix_rot(matrix):
    """ This function rotates an N x N matrix by 90 degrees clockwise."""
    m = matrix[::-1]
    return list(zip(*m))

print('input matrix:  ', matrix)
print('output matrix: ', matrix_rot(matrix))