import functools    # for cache
import copy        # for deepcopy

with open("input7.txt") as f:   # read the input into a list of strings
    lines = [str.strip(s) for s in f.readlines()]   # strip the whitespace
    dirs = []   # the current directory
    contents = {}   # the contents of each directory

    listing = False # whether we are currently listing the contents of a directory

    for line in lines:  # for each line
        if line.startswith("$"):    # if it is a command
            listing = False # stop listing
            line = line[2:] # remove the $ and the space
            if line.startswith("cd"):   # if it is a cd command
                dir = line.split(" ")[-1]   # get the directory
                if dir == "/":  # if it is the root directory
                    dirs = [""]     # set the current directory to the root
                elif dir == "..":   # if it is a parent directory
                    dirs.pop()  # remove the last directory
                else:   # if it is a subdirectory
                    dirs.append(dir)    # add it to the current directory
            elif line.startswith("ls"): # if it is a ls command
                listing = True  # start listing
        elif listing:   # if we are listing
            key = "/".join(dirs)    # get the current directory
            if key not in contents: # if we haven't seen this directory before
                contents[key] = {"size": 0, "files": []}    # add it to the contents
            if line.startswith("dir"):  # if it is a directory
                contents[key]["files"].append(line.split(" ")[1])   # add it to the list of files
            else:   # if it is a file
                contents[key]["size"] += int((line.split(" "))[0])  # add its size to the total size

    @functools.cache    # cache the results of this function
    def file_size(key): # get the size of a directory
        sub_size = sum([file_size(key + "/" + d) for d in contents[key]["files"]])  # get the size of all the subdirectories
        return contents[key]["size"] + sub_size   # add the size of the files in this directory

    count = 0   # the total size of the files in the root directory

    for key in contents:
        size = file_size(key)
        if size <= 100000:
            count += size

    print("Part 1 " + str(count))

    total = 70000000
    needed = 30000000
    best = 70000000

    for key in contents:
        old_size = file_size(key)
        new_contents = copy.deepcopy(contents)

        def remove(key):
            new_contents[key]["size"] = 0
            for f in new_contents[key]["files"]:
                remove(key + "/" + f)
                new_contents[key]["files"] = []

        remove(key)

        @functools.cache
        def rfs(key):
            sub_size = sum([rfs(key + "/" + d) for d in new_contents[key]["files"]])
            return new_contents[key]["size"] + sub_size

        c = rfs("")
        if total - c >= needed:
            if old_size < best:
                best = old_size
    print("Part 2 " + str(best))
