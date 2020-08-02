'''
def solution(A):
    keys = set(A)
    unpaired = A[0]
    for key in keys:
        found = A.count(key)
        if found == 1:
            unpaired = key
            break
    return unpaired
'''
def solution(A):
    temp = {}
    for val in A:
        key = str(val)
        if key in temp:
            temp[key] += 1
        else:
            temp[key] = 1
    unpaired = None
    for key, val in temp.items():
        if val == 1:
            unpaired = int(key)
            break
    return unpaired

A = [42]
print(solution(A))