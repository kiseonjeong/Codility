"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""
def solution(A):
    # Generate a table
    table = {0:0}
    count = 0
    for val in A:
        if val <= 0:
            table[0] += 1
        elif not val in table:
            table[val] = 1
            count += 1
        else:
            table[val] += 1
    
    # Check the flag
    if count < 1:
        return 1
        
    # Find a minimum value in the table
    for i in range(count):
        val = i + 1
        if not val in table:
            return val
            
    return count + 1
        
A = [1, 3, 6, 4, 1, 2]
print(solution(A))