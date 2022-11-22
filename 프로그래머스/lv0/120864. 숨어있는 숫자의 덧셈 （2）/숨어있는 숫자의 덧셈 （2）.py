import re
def solution(my_string):
    num = re.findall(r'\d+', my_string)
    numbers = list(map(int, num))
    return sum(numbers)