from utils import cache_and_read_input


def question_one(data):
    count = 0
    for y_pos in range(len(data)):
        line = data[y_pos]
        for x_pos in range(len(line)):
            if line[x_pos] == 'X':
                for y_int in [-1, 0, 1]:
                    new_y = y_pos + y_int
                    if len(data) <= new_y or new_y < 0:
                        continue
                    for x_int in [-1, 0, 1]:
                        new_x = x_pos + x_int
                        if len(line) <= new_x or new_x < 0 or (x_pos, y_pos) == (new_x, new_y):
                            continue
                        if data[new_y][new_x] == 'M':
                            found = True
                            next_x = new_x
                            next_y = new_y
                            for other_letter in 'AS':
                                next_x += x_int
                                next_y += y_int
                                if len(line) <= next_x or next_x < 0 or len(data) <= next_y or next_y < 0:
                                    found = False
                                    break
                                if data[next_y][next_x] != other_letter:
                                    found = False
                                    break
                            if found:
                                count += 1
    return count


def question_two(data):
    count = 0
    pattern = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
    for y_pos in range(1, len(data) - 1):
        line = data[y_pos]
        for x_pos in range(1, len(line) - 1):
            if line[x_pos] == 'A':
                letters = []
                for dx, dy in pattern:
                    new_x = x_pos + dx
                    new_y = y_pos + dy
                    letters.append(data[new_y][new_x])
                if sorted(letters) == ['M', 'M', 'S', 'S']:
                    count += 1
    return count


if __name__ == "__main__":
    data = cache_and_read_input(4)
    answer = question_two(data)
    print(answer)
