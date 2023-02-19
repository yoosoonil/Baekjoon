def solution(arr, divisor):
    answer = []
    # 미리 오름차순으로 정렬
    arr.sort()
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    # answer의 길이가 0보다 크면, answer 반환
    # answer길이가 0이라면, -1반환
    return answer if len(answer)!=0 else [-1]