#!/usr/bin/python3
"""fuction that returns a list of integers representing pascal's trangle"""


def pascal_triangle(n):
    """define triangle of size n"""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for y in range(len(tri) - 1):
            tmp.append(tri[y] + tri[y + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
