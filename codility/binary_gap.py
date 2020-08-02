def solution(N):
    str_val = bin(N).split('b')[1]
    gap_list = []
    begin, end, gap = -1, -1, 0
    for i, c in enumerate(str_val):
        if c != '1':
            continue
        if begin == -1:
            begin = i
            continue
        if end == -1:
            end = i
        gap = end - (begin + 1)
        gap_list.append(gap)
        begin = i
        end = -1

    if len(gap_list) == 0:
        return 0
    else:
        return max(gap_list)

print(solution(15))