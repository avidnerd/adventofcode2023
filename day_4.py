def main():     
    with open("day_4.in", "r", newline=None) as readfile:
        c = readfile.read().splitlines()
    total_points = 0
    for card in c:
        winning, list = card.split("|")
        winning = (winning.split(":"))[1]
        winning = winning.split(" ")
        list = list.split(" ")
        result = [i for i in winning if i in list]
        result = [i for i in result if i != '']
        if len(result) > 0:
            card_pt_val = 1
        else:
            card_pt_val = 0
        for i in range(len(result)-1):
            card_pt_val = card_pt_val * 2
        total_points += card_pt_val

    return total_points

with open('day_4.out', "w") as file:
    result = main()
    file.write(str(result))

file.close()
