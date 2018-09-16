"""Two functions that together calculate the determinant of any matrix.
The first function calculates the determinant of a 1x1 matrix,
a 2x2 matrix, and adds together the minors of a nxn matrix if n > 2.
The second function calculates the determinant of the minors."""

def determinant(m):
    if len(m) == 1:
        return m[0][0]
    elif len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    else:
        det = 0 
        for i in range(len(m)):
            det += ((-1) ** i) * m[0][i] * determinant(calcminor(m, 0, i))
        return det
        
def calcminor(m, j, k):
    return [row[:k] + row[k+1:] for row in (m[:j]+m[j+1:])]
