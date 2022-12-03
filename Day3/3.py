with open("input.txt", "r") as input_file:
    item_lines_and_midpoints = [([ord(ch) for ch in line], len(line) // 2) for line in input_file.readlines()]
    compartment_pairs = [(items[:midpoint], items[midpoint:]) for items, midpoint in item_lines_and_midpoints]
    common_items = [set(left).intersection(set(right)).pop() for left, right in compartment_pairs]
    priorities = [1 + item - ord('a') if item >= ord('a') else 27 + item - ord('A') for item in common_items]
    print(f"AOC 2022: day 3, part 1: {sum(priorities)}")
    
with open("input.txt", "r") as input_file:
    elves = [[ord(ch) for ch in line] for line in input_file.readlines()]
    groups = [tuple(elves[i:i+3]) for i in range(0, len(elves), 3)]
    badges = [[badge for badge in elf0 if badge in elf1 and badge in elf2][0] for (elf0, elf1, elf2) in groups]
    priorities = [(1 + item - ord('a') if item >= ord('a') else 27 + item - ord('A')) for item in badges]
    print(f"AOC 2022: day 3, part 2: {sum(priorities)}")