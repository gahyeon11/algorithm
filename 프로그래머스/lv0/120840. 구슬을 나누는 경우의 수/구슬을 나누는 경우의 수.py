import math

def solution(balls, share):
    b = math.factorial(balls)
    b_s = math.factorial(balls-share)
    s = math.factorial(share)
    return b / (b_s * s)
    