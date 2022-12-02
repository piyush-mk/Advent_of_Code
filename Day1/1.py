import heapq # heapq is a min heap
maxValue = 0    
curValue = 0 
with open("input.txt", "r") as reader: 
    for line in reader.readlines():
        line = line.strip()
        if len(line) == 0:
            maxValue = max(maxValue,curValue)
            curValue = 0
        else:
            curValue += int(line)
 
print(f"The max value was: {maxValue}")
 
h = []
curValue = 0
with open("input.txt", "r") as reader:
 
    for line in reader.readlines():
        line = line.strip()
        if len(line) == 0: 
            heapq.heappush(h, curValue) # push the current value to the heap
 
            if len(h) > 3:
                heapq.heappop(h) # pop the smallest value from the heap
            
            curValue = 0
        else:
            curValue += int(line) # add the current value to the current value
 
total = sum(h)  # sum the 3 largest values
 
print(f"The total is: {total}") 