from utils import cache_and_read_input


def question_one(data):
    next_dir = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}
    guard_pos, direction = find_guard(data)
    print(f'Guard found at {guard_pos} in direction {direction}')
    visited_positions = 0
    while True:
        guard_pos = (guard_pos[0] + direction[0], guard_pos[1] + direction[1])
        print(F'NEXT POS {guard_pos}')
        try:
            next_object = data[guard_pos[1]][guard_pos[0]]
            visited_positions += 1
        except:
            print(f'Guard exited map at {(guard_pos[0] - direction[0], guard_pos[1] - direction[1])} in direction {direction}')
            return visited_positions

        if next_object == '#':
            guard_pos = (guard_pos[0] - direction[0], guard_pos[1] - direction[1])
            visited_positions -= 1
            direction = next_dir[direction]


def find_guard(data):
    guard = {'v': (0, -1), '>': (1, 0), '<': (-1, 0), '^': (0, -1)}
    for y in range(len(data)):
        for x in range(len(data[y])):
            search = data[y][x]
            if search in guard.keys():
                return (x, y), guard[search]


if __name__ == "__main__":
    data = cache_and_read_input(6)
    answer = question_one(data)
    print(answer)
