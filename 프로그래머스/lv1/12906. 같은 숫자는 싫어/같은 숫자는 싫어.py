def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        if  arr[i] == arr[i+1]:
            arr.pop()
        else:
            continue
        
    return arr
        
        
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')