def solution(n):
    answer = 1
    for x in range(1,n):
        if(n % x ==0): answer += 1
    return answer