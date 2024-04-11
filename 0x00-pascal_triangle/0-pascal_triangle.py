#!/usr/bin/python3
def pascal_triangle(n):
    res = [[1]]
    prev = [1]

    for i in range(1, n):
        current = [1]
        for j in range(1, i + 1):
            if j > len(prev) - 1:
                up = 0
            else:
                up = prev[j]
            if j - 1 < 0:
                right = 0
            else:
                right = prev[j-1]
            current.append(up + right)
        prev = current
        res.append(current)
    return(res)
