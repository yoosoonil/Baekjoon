def solution(A,B):
    answer = 0
    A.sort(reverse=True)
    B.sort()
    for i in range(len(A)):
        num = A[i] * B[i]
        answer += num

    return answer