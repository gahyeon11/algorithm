from string import ascii_lowercase
def solution(age):
    a = list(ascii_lowercase)
    answer = ''
    for i in str(age):
        answer += a[int(i)]
    return answer