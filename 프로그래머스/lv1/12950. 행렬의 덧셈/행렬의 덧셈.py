def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        ans_num = []
        for j in range(len(arr1[0])):
            ans_num.append(arr1[i][j] + arr2[i][j])
        
        answer.append(ans_num)
    return answer