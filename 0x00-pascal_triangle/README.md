# Pascal's Triangle - README

## Description
This code provides a function `pascal_triangle(n)` that prints Pascal's triangle up to a specified number of rows `n`.

## Solution Approach
The implementation follows the standard approach to generate Pascal's triangle. Here's how the solution works:

1. The function initializes a 2D list `res` with the first row containing a single element, which is `1`. This represents the first row of Pascal's triangle.
2. The function also initializes a list `prev` with the same elements as the first row. This list `prev` keeps track of the previous row of Pascal's triangle.
3. If `n` is equal to `0`, an empty list is returned since there are no rows to print.
4. The function then proceeds to generate the remaining rows of Pascal's triangle using a nested loop.
5. The outer loop iterates from `1` to `n-1`, representing the row index of Pascal's triangle.
6. In each iteration, a new list `current` is created to store the elements of the current row.
7. The inner loop iterates from `1` to `i+1`, representing the column index of the current row.
8. In each inner loop iteration, the function calculates the elements of the current row based on the elements of the previous row.
9. The function checks if the indices `j` and `j-1` are within the bounds of the `prev` list. If they are, the function retrieves the corresponding elements from `prev` and adds them together to get the current element.
10. The calculated element is then appended to the `current` list.
11. After the inner loop completes, the `current` list becomes the new `prev` list for the next iteration, and it is appended to the `res` list to store the entire row.
12. Finally, the function returns the generated Pascal's triangle stored in the `res` list.

## Time Complexity
The time complexity of the solution is O(n^2), where `n` is the number of rows in Pascal's triangle. The nested loops iterate `n` times in the outer loop and `i+1` times in the inner loop for each row.

## Space Complexity
The space complexity of the solution is O(n^2) since the function uses a 2D list `res` to store the entire Pascal's triangle.

## Usage
To use this code, you can call the `pascal_triangle(n)` function, where `n` is the number of rows you want to print in Pascal's triangle. The function will return the Pascal's triangle as a 2D list.

Example usage:
```python
result = pascal_triangle(5)
print(result)
```

In the above example, `pascal_triangle(5)` generates Pascal's triangle with 5 rows and stores it in the `result` variable. The resulting triangle is then printed.

Feel free to modify the code and experiment with different inputs to generate Pascal's triangle with different numbers of rows.
