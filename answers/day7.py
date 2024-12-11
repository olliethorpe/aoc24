from utils import cache_and_read_input
import re
import itertools


def question_one(data):
    sum_of_correct_tests = 0
    pattern = re.compile(r'(\d+):([\d\s]+)')
    operators = ['*', '+']
    for row in data:
        match = re.match(pattern, row)
        result = int(match[1])
        numbers = match[2].split()
        combs = itertools.product(operators, repeat=len(numbers)-1)
        for comb in combs:
            total = int(numbers[0])
            for num, op in zip(numbers[1:], comb):
                total = eval(f"{total} {op} {num}")
            if total == result:
                sum_of_correct_tests += result
                break

    return sum_of_correct_tests


def question_two(data):
    sum_of_correct_tests = 0
    pattern = re.compile(r'(\d+):([\d\s]+)')
    operators = ['*', '+', '||']
    for row in data:
        match = re.match(pattern, row)
        result = int(match[1])
        numbers = match[2].split()
        combs = itertools.product(operators, repeat=len(numbers)-1)
        for comb in combs:
            total = int(numbers[0])
            for num, op in zip(numbers[1:], comb):
                total = eval(f"{total} {op} {num}")
            if total == result:
                sum_of_correct_tests += result
                break

    return sum_of_correct_tests


if __name__ == "__main__":
    data = cache_and_read_input(7)
    answer = question_two(data)
    print(answer)
