from utils import cache_and_read_input
import re


def question_one(data):
    total = 0
    pattern = re.compile(r'mul\((\d+,\d+)\)')

    for line in data:
        for match in re.findall(pattern, line):
            n1, n2 = map(int, match.split(','))
            total += n1 * n2

    return total


def question_two(data):
    total = 0
    pattern = re.compile(r"mul\((\d+,\d+)\)|(do\(\))|(don't\(\))")
    do = True

    for line in data:
        for match in re.findall(pattern, line):
            if match[2]:
                do = False
            elif match[1]:
                do = True
            else:
                if do:
                    n1, n2 = map(int, match[0].split(','))
                    total += n1 * n2
    return total


if __name__ == "__main__":
    data = cache_and_read_input(3)
    answer = question_two(data)
    print(answer)  # 77055967
