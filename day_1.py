
def main():     
    with open("day_1.in", "r", newline=None) as readfile:
        c = readfile.read().splitlines()
    sum = 0
    nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for string in c:
        indices = []
        for i in range (0, len(string)):
            char = string[i]
            if char.isnumeric():
                indices.append((i, char))
        ind_ind = []
        for n in nums:
            ind = []
            i = 0
            while i < len(string):
                j = string.find(n, i)
                if j == -1:
                    break
                ind.append((j, n))
                i = j + len(n)
            ind_ind.append(ind)
        print(ind_ind)
        
        all_indices = indices + [item for sublist in ind_ind for item in sublist]
        all_indices.sort()
        first_num = all_indices[0][1]
        last_num = all_indices[-1][1]
        if first_num.isalpha():
            first_num = nums.index(first_num) + 1
        if last_num.isalpha():
            last_num = nums.index(last_num) + 1
        num = int(first_num) * 10 + int(last_num)
        sum += num
    return sum

with open('day_1.out', "w") as file:
    result = main()
    file.write(str(result))

file.close()