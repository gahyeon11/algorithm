def solution(my_string):
    
    st = [x for x in my_string]
    target = ['a','e', 'i', 'o', 'u']
    answer = [a for a in st if a not in target]
    
    return "".join(answer)