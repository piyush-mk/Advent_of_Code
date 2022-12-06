if __name__ == '__main__':
    data = open("input5.txt", encoding="utf-8").read().splitlines() 
    initial_positions, instructions = [], []
    for line in data:  # Split the data into two lists
        if not line == '' and not "move" in line:   # If the line is not empty and does not contain the word "move"
            initial_positions.append(line)  # Add the line to the initial_positions list
        elif line.startswith('move'):   # If the line starts with the word "move"
            instructions.append(line)   # Add the line to the instructions list
    # Putting all crates in a dictionary
    position_dict_1, position_dict_2, string_positions = {}, {}, {v:k for k, v in enumerate(initial_positions[-1]) if v.isdigit()} # string_positions is a dictionary with the positions of the crates
    for crates in initial_positions[-2::-1]:    # Iterate through the list of crates in reverse order
        for stack, str_position in string_positions.items(): 
            if crates[str_position].isalpha():
                position_dict_1[stack] = position_dict_1.get(stack, []) + list(crates[str_position]) # position_dict_1 is a dictionary with the crates in the stacks
                position_dict_2[stack] = position_dict_2.get(stack, []) + list(crates[str_position]) 
    
    for instruction in instructions:
        number_to_move, src_stack, dst_stack = instruction.split()[1::2] # Getting the number of crates to move, the source stack and the destination stack
        stack_to_move = []
        for _ in range(int(number_to_move)):    # Iterate through the number of crates to move
            position_dict_1[dst_stack].append(position_dict_1[src_stack].pop())
            stack_to_move.append(position_dict_2[src_stack].pop())
        for crate in stack_to_move[::-1]:
            position_dict_2[dst_stack].append(crate)
    print(f"Part 1:{''.join([v[-1] for k, v in position_dict_1.items()])}")
    print(f"Part 2:{''.join([v[-1] for k, v in position_dict_2.items()])}")