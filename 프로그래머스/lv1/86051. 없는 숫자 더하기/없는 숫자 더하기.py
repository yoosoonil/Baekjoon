def solution(numbers):
    list_ = [i for i in range(0, 10)]
    
    cha_list = list(set(list_)-set(numbers))
    answer = sum(cha_list)
    
    return answer