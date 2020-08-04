"""
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
"""
def solution(N, A):
    # Initialize the counters
    counters = [0 for i in range(N)]

    # Do operations
    for X in A:
        counters = increase(counters, X, N)
        print(counters)
    return counters

def increase(counters, X, N):
    # Do increase operation
    if X == N + 1:
        return __max_counter(counters, N)
    else:
        idx = X - 1
        counters[idx] += 1
        return counters
    
def __max_counter(counters, N):
    # Do max_counter operation
    max_val = max(counters)
    counters = [max_val for i in range(N)]
    return counters

N = 5
A = [3, 4, 4, 6, 1, 4, 4]
#B = [0 for _ in range(10)]
B = list(map(3, int))
print(B)
B[0][1] = 3.14
print(B)
#print(solution(N, A))