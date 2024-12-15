from utils import cache_and_read_input


def question_one(data):
    valid = []
    for y in range(len(data)-1):
        for x in range(len(data[y])-1):
            if data[y][x] != '.':
                antinodes = find_next_antinodes(data, x, y)
                for next_x, next_y in antinodes:
                    diff_x = next_x - x
                    diff_y = next_y - y
                    antinode_1 = (x - diff_x, y - diff_y)
                    antinode_2 = (next_x + diff_x, next_y + diff_y)
                    for ant in [antinode_1, antinode_2]:
                        if ant[0] >= 0 and ant[1] >= 0 and ant[0] <= len(data[y].removesuffix('\n')) - 1 and ant[1] <= len(data) - 1:
                            valid.append(ant)
    return set(valid)


def question_two(data):
    cp = [d for d in data]
    valid = []
    for y in range(len(data)-1):
        for x in range(len(data[y])-1):
            if data[y][x] != '.':
                antinodes = find_next_antinodes(data, x, y)
                if antinodes:
                    valid.append((x, y))
                    valid.append(node for node in antinodes)
                for next_x, next_y in antinodes:
                    diff_x = next_x - x
                    diff_y = next_y - y
                    antinode_1 = (x - diff_x, y - diff_y)
                    antinode_2 = (next_x + diff_x, next_y + diff_y)
                    while True:
                        both = 0
                        for ant in [antinode_1, antinode_2]:
                            if ant[0] >= 0 and ant[1] >= 0 and ant[0] <= len(data[y].removesuffix('\n')) - 1 and ant[1] <= len(data) - 1:
                                valid.append(ant)
                                line = [l for l in cp[ant[1]].removesuffix('\n')]
                                line[ant[0]] = '#'
                                cp[ant[1]] = ''.join(line)
                            else:
                                both += 1
                        antinode_1 = (antinode_1[0] - diff_x, antinode_1[1] - diff_y)
                        antinode_2 = (antinode_2[0] + diff_x, antinode_2[1] + diff_y)
                        if both == 2:
                            break
    with open('day8cp.txt', 'w') as f:
        f.write('\n'.join(cp))
    return set(valid)


def find_next_antinodes(data, x_start, y_start):
    antinodes = []
    ant = data[y_start][x_start]
    for y in range(y_start, len(data)-1):
        for x in range(len(data[y])-1):
            if y == y_start:
                if x <= x_start:
                    continue
            if data[y][x] == ant:
                antinodes.append((x, y))
    return antinodes


if __name__ == "__main__":
    data = cache_and_read_input(8)
    answer = question_two(data)
    print(len(answer))
