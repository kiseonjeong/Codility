def solution(A, K):
    arr_len = len(A)
    rotated = A[:]
    for i, val in enumerate(A):
        idx = (i + K) % arr_len
        rotated[idx] = val
    return rotated

A = [3, 8, 9, 7, 6]
K = 3
#A = [1, 2, 3, 4]
#K = 4
print(A)
print(solution(A, K))
print(solution(solution(A, K), K))
print(solution(solution(solution(A, K), K), K))
