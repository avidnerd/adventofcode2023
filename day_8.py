import math
def main():     
    with open("day_8.in", "r", newline=None) as readfile:
        c = readfile.read().splitlines()
    pattern = list(c.pop(0))
    pattern = list(map(lambda x: x.replace('R', '1'), pattern))
    pattern = [int(i) for i in list(map(lambda x: x.replace('L', '0'), pattern))]
    blank = c.pop(0)
    dct = {}
    for key in c:
        dct[key[0:3]] = [key[7:10], key[12:15]]
    current_nodes = []
    for key in dct:
        if key[2] == "A":
            current_nodes.append(key)
    steps = 0
    pattern_ind = 0
    final_steps = []
    for node in current_nodes:
        new_node = node
        steps = 0
        while new_node[-1] != "Z":
            new_node = dct.get(new_node)[pattern[pattern_ind]]
            # import pdb; pdb.set_trace()
            steps += 1
            pattern_ind += 1
            if pattern_ind == len(pattern):
                pattern_ind = 0

        final_steps.append(steps)
    return math.lcm(*final_steps)

with open('day_8.out', "w") as file:
    result = main()
    file.write(str(result))

file.close()
