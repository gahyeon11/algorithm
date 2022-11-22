def solution(numbers):
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for num, word in enumerate(nums):
        numbers = numbers.replace(word, str(num))
    return int(numbers)