'''
# very large computations
def solution(A):
    keys = set(A)
    unpaired = A[0]
    for key in keys:
        found = A.count(key)
        if found % 2 != 0:
            unpaired = key
            break
    return unpaired
'''
def solution(A):
    temp = {}
    for val in A:
        key = val
        if key in temp:
            temp[key] += 1
        else:
            temp[key] = 1
    unpaired = None
    for key, val in temp.items():
        if val % 2 != 0:
            unpaired = key
            break
    return unpaired

A = [9, 3, 9, 3, 9, 7, 9]
print(solution(A))