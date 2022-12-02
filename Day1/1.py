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
            heapq.heappush(h, curValue)
 
            if len(h) > 3:
                heapq.heappop(h)
            
            curValue = 0
        else:
            curValue += int(line)
 
total = sum(h)
 
print(f"The total is: {total}")