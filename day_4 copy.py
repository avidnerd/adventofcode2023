from collections import defaultdict
def main():     
    with open("day_4.in", "r", newline=None) as readfile:
        c = readfile.read().splitlines()
    n = defaultdict(int)
    for num, card in enumerate(c):
        n[num] += 1
        winning, list = card.split("|")
        winning = (winning.split(":"))
        winning = winning[1]
        winning = winning.split(" ")
        list = list.split(" ")
        result = [i for i in winning if i in list]
        result = [i for i in result if i != '']
        num_copies = len(result)
        for j in range(num_copies):
            n[num+1+j] += n[num]

    return sum(n.values())

with open('day_4_2.out', "w") as file:
    result = main()
    file.write(str(result))

file.close()
