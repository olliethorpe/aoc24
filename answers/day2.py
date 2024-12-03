from utils import cache_and_read_input


def question_one(data):
    safe = 0
    for line in data:
        report = map(int, line.split())
        previous = None
        increasing = None
        is_safe = True

        for number in report:
            if previous is not None:
                diff = number - previous
                increment = diff > 0
                if increasing is None:
                    increasing = increment

                if increment != increasing or abs(diff) > 3 or diff == 0:
                    is_safe = False
                    break
            previous = number
        if is_safe:
            safe += 1
    return safe


def question_two(data):
    safe = 0
    for line in data:
        report = map(int, line.split())
        previous = None
        increasing = None
        is_safe = True
        dampener_limit = 1

        for number in report:
            if previous is not None:
                prev_inc = increasing
                increasing, is_safe = safety_check(increasing, previous, number)
                if not is_safe:
                    if dampener_limit:
                        dampener_limit -= 1
                        increasing = prev_inc
                        continue
                    break

            previous = number

        if is_safe:
            safe += 1
    return safe


def safety_check(increasing, prev_level, level):
    diff = level - prev_level
    increment = diff > 0

    if increasing is None:
        increasing = increment

    if increment != increasing or abs(diff) > 3 or diff == 0:
        return increasing, False

    return increasing, True


if __name__ == "__main__":
    data = cache_and_read_input(2)
    a = question_two(data)
    print(a)
