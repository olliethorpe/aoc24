from utils import cache_and_read_input


def is_report_safe(report, report_id):
    dampened = False
    increasing = None

    current_index = 1
    previous_index = 0
    report_length = len(report)
    cnt = 1
    while True:
        if current_index >= report_length:
            return True

        diff = report[current_index] - report[previous_index]

        # Check for invalid differences
        if abs(diff) > 3 or diff == 0:
            if dampened:
                print(f"Report {report_id} unsafe: Invalid step between {report[previous_index]} and {report[current_index]}")
                return False
            print(f"Dampening report {report_id} due to invalid step between {report[previous_index]} and {report[current_index]}")
            dampened = True
            current_index += 1
            continue

        # Determine direction
        current_increasing = diff > 0

        # Initialize direction if not set
        if increasing is None:
            increasing = current_increasing

        # Check for direction inconsistency
        if current_increasing != increasing:
            if dampened:
                print(f"Report {report_id} unsafe: Direction change between {report[previous_index]} and {report[current_index]}")
                return False
            print(f"Dampening report {report_id} due to direction change between {report[previous_index]} and {report[current_index]}")
            dampened = True
            # Reset direction since dampening occurred
            increasing = None
            current_index += 1
            continue

        if dampened and cnt:
            cnt -= 1
            previous_index += 1

        previous_index += 1
        current_index += 1


def question_two(data):

    safe_count = 0

    for report_id, line in enumerate(data, start=1):
        report = list(map(int, line.split()))
        forwards = is_report_safe(report, report_id)
        backwards = is_report_safe(list(reversed(report)), report_id)
        if forwards or backwards:
            print(f"Report {report_id} deemed safe")
            safe_count += 1
        else:
            print(f"Report {report_id} deemed unsafe")

    return safe_count



if __name__ == "__main__":
    data = cache_and_read_input(2)
    a = question_two(data)
    print(a)
