def solution(a, b):
    
    result = []
    if a < b:
        for i in range(a, b+1):
            result.append(i)
    else:
        for i in range(b, a+1):
            result.append(i)
        
    return sum(result)