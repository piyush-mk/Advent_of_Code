if __name__ == '__main__':
    data = open("input.txt", encoding="utf-8").read().splitlines()
    initial_positions, instructions = [], []
    for line in data:
        if not line == '' and not "move" in line:
            initial_positions.append(line)
        elif line.startswith('move'):
            instructions.append(line)
    # Let's put all these crates in a dictionary
    position_dict_1, position_dict_2, string_positions = {}, {}, {v:k for k, v in enumerate(initial_positions[-1]) if v.isdigit()}
    for crates in initial_positions[-2::-1]:
        for stack, str_position in string_positions.items():
            if crates[str_position].isalpha():
                position_dict_1[stack] = position_dict_1.get(stack, []) + list(crates[str_position])
                position_dict_2[stack] = position_dict_2.get(stack, []) + list(crates[str_position])
    # Parts 1/2
    for instruction in instructions:
        number_to_move, src_stack, dst_stack = instruction.split()[1::2]
        stack_to_move = []
        for _ in range(int(number_to_move)):
            position_dict_1[dst_stack].append(position_dict_1[src_stack].pop())
            stack_to_move.append(position_dict_2[src_stack].pop())
        for crate in stack_to_move[::-1]:
            position_dict_2[dst_stack].append(crate)
    print(f"Part 1:{''.join([v[-1] for k, v in position_dict_1.items()])}")
    print(f"Part 2:{''.join([v[-1] for k, v in position_dict_2.items()])}")