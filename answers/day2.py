from utils import cache_and_read_input


def is_safe_1(ls):
    ds = [ls[i + 1] - ls[i] for i in range(len(ls) - 1)]

    if not all(-3 <= d <= 3 and d != 0 for d in ds):
        return False

    if all(d > 0 for d in ds) or all(d < 0 for d in ds):
        return True

    return False


def is_safe_2(ls):
    if is_safe_1(ls):
        return True
    for i in range(len(ls)):
        modded = ls[:i] + ls[i + 1:]
        if is_safe_1(modded):
            return True
    return False


def question_two(data):

    safe_count = 0
    for line in data:
        nums = list(map(int, line.split()))
        if is_safe_2(nums):
            safe_count += 1
    return safe_count


if __name__ == "__main__":
    data = cache_and_read_input(2)
    b = question_two(data)
    print(b)
