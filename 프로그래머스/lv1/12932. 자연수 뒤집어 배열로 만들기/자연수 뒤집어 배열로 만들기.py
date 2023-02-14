def solution(n):
    n_str = str(n)
    n_reverse = reversed(n_str)
    
    answer = []
    for i in n_reverse:
        answer.append(int(i))
    
    return answer