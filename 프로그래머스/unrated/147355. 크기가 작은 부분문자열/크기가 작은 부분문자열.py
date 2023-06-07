def solution(t, p):
    length = int(len(p))
    t_list = []

    k = 0
    for n in str(t):
        t_list.append(n)
        
    for i in range(len(t_list)):
        i = int(i)
        if i+length <= len(t_list):
            num = int(''.join(t_list[i:i+length]))
            
            if num <= int(p):
                k += 1
    print(k)
    return k