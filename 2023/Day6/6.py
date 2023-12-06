#part 1

def calculate_ways_to_win(time, distance):
    ways_to_win = 0
    for button_press_time in range(time):
        travel_time = time - button_press_time
        speed = button_press_time
        total_distance = speed * travel_time
        if total_distance > distance:
            ways_to_win += 1
    return ways_to_win

example_times = [47, 98, 66, 98]
example_distances = [400, 1213, 1011, 1540]

example_ways_to_win = [calculate_ways_to_win(t, d) for t, d in zip(example_times, example_distances)]

example_product = 1
for ways in example_ways_to_win:
    example_product *= ways

print(example_product)


#part 2

time=[47986698]
disance=[400121310111540]

ways_to_win = [calculate_ways_to_win(t, d) for t, d in zip(time, disance)]
print(ways_to_win)