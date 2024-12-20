from collections import Counter
from utils import cache_and_read_input


def question_one(data):
    first_list, second_list = zip(*(map(int, line.split()) for line in data))
    answer = sum(abs(first - second) for first, second in zip(sorted(first_list), sorted(second_list)))
    print(f'The answer to question one is: {answer}')
    return first_list, second_list


def question_two(first_list, second_list):
    similarity_score = 0
    second_list_counter = Counter(second_list)

    for number, first_lst_cnt in Counter(first_list).items():
        if sec_list_cnt := second_list_counter.get(number):
            similarity_score += number * sec_list_cnt * first_lst_cnt
    print(f'The answer to question two is: {similarity_score}')
    return similarity_score


if __name__ == '__main__':
    data = cache_and_read_input(1)

    first_list, second_list = question_one(data)  # 1722302

    score = question_two(first_list, second_list)  # 20373490
