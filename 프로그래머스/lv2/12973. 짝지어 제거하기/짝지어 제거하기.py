def solution(s):
    stack = []
    
    for i in s: # s = baabaa
        if len(stack) == 0: # stack 리스트에 요소가 없다면
            stack.append(i)
        elif stack[-1] == i: # stack 리스트 맨뒤 요소가 s의 i랑 같다면
            stack.pop() # stack 맨뒤 요소 삭제
        else:
            stack.append(i) # 그 외 -> stack에 요소가 하나라도 있고, 맨뒤 요소가 i랑 같지 않을 때
    if len(stack) == 0: # 결국, 짝 지어져서 stack에는 요소가 하나도 없다면 1 return
        return 1
    else:
        return 0 # stack에 요소가 하나라도 남아있다면 0 return
        

    return answer