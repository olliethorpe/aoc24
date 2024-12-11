from utils import cache_and_read_input


def question_one(data):
    next_dir = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}
    guard_pos, direction = find_guard(data)
    visited_positions = set()
    visited_positions.add(guard_pos)
    while True:
        guard_pos = (guard_pos[0] + direction[0], guard_pos[1] + direction[1])
        try:
            next_object = data[guard_pos[1]][guard_pos[0]]
            if guard_pos[0] < 0 or guard_pos[0] >= len(data[0]) or guard_pos[1] < 0 or guard_pos[1] >= len(data):
                return visited_positions
        except:
            print(f'Guard exited map at {(guard_pos[0] - direction[0], guard_pos[1] - direction[1])} in direction {direction}')
            return visited_positions

        if next_object == '#':
            guard_pos = (guard_pos[0] - direction[0], guard_pos[1] - direction[1])
            direction = next_dir[direction]
        else:
            visited_positions.add(guard_pos)


def find_guard(data):
    guard = {'v': (0, -1), '>': (1, 0), '<': (-1, 0), '^': (0, -1)}
    for y in range(len(data)):
        for x in range(len(data[y])):
            search = data[y][x]
            if search in guard.keys():
                return (x, y), guard[search]


def find_loop(data):
    next_dir = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}
    guard_pos, direction = find_guard(data)
    record = set([(guard_pos, direction),])
    while True:
        guard_pos = (guard_pos[0] + direction[0], guard_pos[1] + direction[1])
        try:
            next_object = data[guard_pos[1]][guard_pos[0]]
            if guard_pos[0] < 0 or guard_pos[0] >= len(data[0]) or guard_pos[1] < 0 or guard_pos[1] >= len(data):
                return False
        except:
            return False

        if next_object == '#':
            guard_pos = (guard_pos[0] - direction[0], guard_pos[1] - direction[1])
            direction = next_dir[direction]
        else:
            if (guard_pos, direction) in record:
                return True
            record.add((guard_pos, direction))


def question_two(data):
    total_loops = 0
    for y in range(len(data)):
        line = [x for x in data[y]]
        for x in range(len(line)):
            before = data[y][x]
            if before in ['^']:
                continue
            line[x] = '#'
            data[y] = ''.join(line)
            if before != '#' and find_loop(data):
                total_loops += 1
            line[x] = before
            data[y] = ''.join(line)

    return total_loops


if __name__ == "__main__":
    data = cache_and_read_input(6)
    data = [line.replace('\n', '') for line in data]
    answer = question_two(data)
    print(answer)
