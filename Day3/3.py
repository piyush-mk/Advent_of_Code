with open("input3.txt", "r") as input_file:
    item_lines_and_midpoints = [([ord(ch) for ch in line], len(line) // 2) for line in input_file.readlines()] # ord() returns the unicode code point for a one-character string
    compartment_pairs = [(items[:midpoint], items[midpoint:]) for items, midpoint in item_lines_and_midpoints]  # Split the list of items in half
    common_items = [set(left).intersection(set(right)).pop() for left, right in compartment_pairs] # Find the common item in each pair of lists
    priorities = [1 + item - ord('a') if item >= ord('a') else 27 + item - ord('A') for item in common_items] # Convert the common item to a priority
    print(f"Part 1: {sum(priorities)}") # Sum the priorities
    
with open("input3.txt", "r") as input_file:
    elves = [[ord(ch) for ch in line] for line in input_file.readlines()] 
    groups = [tuple(elves[i:i+3]) for i in range(0, len(elves), 3)] # Split the list of elves into groups of 3
    badges = [[badge for badge in elf0 if badge in elf1 and badge in elf2][0] for (elf0, elf1, elf2) in groups] # Find the common badge in each group of 3
    priorities = [(1 + item - ord('a') if item >= ord('a') else 27 + item - ord('A')) for item in badges] # Convert the common badge to a priority
    print(f"Part 2: {sum(priorities)}") # Sum the priorities