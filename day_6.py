def main():     
    time = 60947882
    records = 475213810151650
    way_to_win = 0
    for i in range(time):
        holding_time = i
        distance = (time - i) * holding_time
        if distance > records:
            way_to_win += 1

    return way_to_win

with open('day_6.out', "w") as file:
    result = main()
    file.write(str(result))

file.close()

