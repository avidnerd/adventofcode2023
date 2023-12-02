import re
def main():     
    with open("day_2.in", "r", newline=None) as readfile:
        c = readfile.read().splitlines()
    games = {}
    for game in c:
        game_id, sets = game.split(":")
        game_id = int(game_id[5:])
        sets = sets.split(';')
        new_set = []
        for set in sets:
            set_dict = {'red': 0, 'green': 0, 'blue': 0}
            if 'red' in set:
                match = re.search(r'\d+\sred', set)
                reds = int(match.group().split()[0])
                set_dict['red'] = reds
            if 'green' in set:
                match = re.search(r'\d+\sgreen', set)
                greens = int(match.group().split()[0])
                set_dict['green'] = greens
            if 'blue' in set:
                match = re.search(r'\d+\sblue', set)
                blues = int(match.group().split()[0])
                set_dict['blue'] = blues
            new_set.append(set_dict)
        
        games[game_id] = new_set
    

    sum_pow = 0

    for game_id, new_set in games.items():
        print("ID:", game_id, "New:" , new_set)
        max_red = 0
        max_green = 0
        max_blue = 0
        for set_cubes in new_set:
            if set_cubes["red"] > max_red:
                max_red = set_cubes["red"]
            if set_cubes["green"] > max_green:
                max_green = set_cubes["green"]
            if set_cubes["blue"] > max_blue:
                max_blue = set_cubes["blue"]
           
        sum_pow += (max_blue*max_green*max_red)

    print(sum_pow)


    return ""

with open('day_2.out', "w") as file:
    result = main()
    file.write(str(result))

file.close()
