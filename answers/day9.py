from utils import cache_and_read_input


def question_one(data):
    blocks = calculate_blocks(data)
    blocks_backwards = blocks[::-1]
    for i in range(len(blocks_backwards) - 1):
        block = blocks_backwards[i]
        if block != '.':
            next_empty_space = find_empty_space(blocks)
            if next_empty_space > (len(blocks) - 1) - i:
                break
            blocks[next_empty_space] = block
            blocks[(len(blocks) - 1) - i] = '.'
    sum = 0
    position = 0
    while blocks[position] != '.':
        sum += position * int(blocks[position])
        position += 1
    return sum


def find_empty_space(blocks):
    for i in range(len(blocks) - 1):
        if blocks[i] == '.':
            return i
    return None


def calculate_blocks(data):
    a = []
    for i, block in enumerate(data[0]):
        if i % 2 == 0:
            for _ in range(int(block)):
                a.append(int(i / 2))
        else:
            for _ in range(int(block)):
                a.append('.')
    return a


if __name__ == "__main__":
    data = cache_and_read_input(9)
    a = question_one(data)
    print(a)
