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


if __name__ == "__main__":
    data = cache_and_read_input(3)
    answer = question_one(data)
    print(answer)
