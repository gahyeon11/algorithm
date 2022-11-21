import math
def solution(n):
    answer = 1
    if(n % 6 != 0):
        answer =  n * 6 / math.gcd(n, 6) // 6
            
    else: answer = n // 6        
    return answer