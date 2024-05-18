"""
   *
   ***
  *****
 *******
*********
"""


def equilateral_triangle(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))

# Example usage
n = 5
equilateral_triangle(n)
