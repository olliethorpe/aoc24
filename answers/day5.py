from utils import cache_and_read_input


def calculate_sum(updates):
    sum = 0
    for update in updates:
        middle_index = int((len(update) - 1) / 2)
        sum += int(update[middle_index])  # Assuming each update is a odd length
    return sum


def is_update_valid(update, orders):
    for number in update:
        for n1, n2 in orders:
            if number == n1 and n2 in update:
                if n2 not in update[update.index(n1)+1:]:
                    return None
    return update


def fix_update(update, orders):
    index = 0
    while index < len(update):
        number = update[index]
        for n1, n2 in orders:
            if number == n1 and n2 in update and (n2 in update[:(loc := update.index(n1) + 1)]):
                remove_index = update[:loc].index(n2)
                update.insert(loc - 1, update.pop(remove_index))
                index -= 1
        index += 1
    return update


def main(data):
    orders = []
    updates = []
    correct_updates = []
    fixed_updates = []

    for line in data:
        line = line.removesuffix('\n')
        if ',' in line:
            updates.append(line.split(','))
        elif '|' in line:
            orders.append(line.split('|'))

    for update in updates:
        if not (correct_update := is_update_valid(update, orders)):
            fixed_updates.append(fix_update(update, orders))
        else:
            correct_updates.append(correct_update)

    print(f'The sum of correct updates is: {calculate_sum(correct_updates)}')
    print(f'The sum of corrected updates is: {calculate_sum(fixed_updates)}')


if __name__ == "__main__":
    data = cache_and_read_input(5)
    main(data)
