def count_visible(a, b): # a is a list of elements, b is the element to count visible of
    return next((n+1 for n, x in enumerate(a) if x >= b), len(a)) # return the index of the first element >= b, or the length of the list if none are

with open("input8.txt") as infile:
    rows=[] 
    for line in infile: 
        rows.append(list(line.strip())) # read the input into a list of lists

    max_score = 0  # part 2
    visible = 2*(len(rows)-1) + 2*(len(rows[0])-1)  # part 1
    for y in range(1, len(rows)-1): # skip the edges
        for x in range(1, len(rows[0])-1):  # skip the edges
            elem = rows[y][x]   # the element to count visible of

            if max(rows[y][:x]) < elem or ( # if the element is the max in any of the 4 directions
                max(rows[y][x+1:]) < elem) or ( # then it is visible
                max(rows[yy][x] for yy in range(0,y)) < elem) or (  # so increment the count
                max(rows[yy][x] for yy in range(y+1,len(rows))) < elem):    # and the max score
                visible += 1    # part 1

            score = count_visible(rows[y][x-1::-1], elem)  
            score *= count_visible(rows[y][x+1:], elem) 
            score *= count_visible([rows[yy][x] for yy in reversed(range(0,y))], elem)  # count_visible returns the number of elements >= elem
            score *= count_visible([rows[yy][x] for yy in range(y+1,len(rows))], elem) # so we can multiply them together to get the score
            max_score = score if max_score < score else max_score 

    print("Part 1: ",visible, end="\n")
    print("Part 2: ",max_score)
