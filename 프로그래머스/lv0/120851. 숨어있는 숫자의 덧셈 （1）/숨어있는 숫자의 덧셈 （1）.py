import re
def solution(my_string):
    a = map(int, list(re.findall(r'\d', my_string)))
    answer = 0
    answer = sum(a)    
    return answer