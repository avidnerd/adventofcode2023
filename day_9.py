def predict_next(sequence):
    orig_seq = sequence
    def differences(seq):
        return [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]

    differs = [orig_seq]
    while True:
        diffs = differences(sequence)
        if all(diff == 0 for diff in diffs):
            break
        differs.append(diffs)
        sequence = diffs
    curr_diff = differs[-1][0]
    for i in range(len(differs)-2, -1, -1):
        differs[i].insert(0, (differs[i][0] - curr_diff))
        curr_diff = differs[i][0]
    # orig_seq.insert(0, (orig_seq[0] - differs[0][0]))
    next_number = differs[0][0]
    return next_number
def main():    
   with open("day_9.in", "r", newline=None) as readfile:
       c = readfile.read().splitlines()
   c = [[int(i) for i in g.split()] for g in c]
   sum_extrapolation = 0
   for history in c:
       sum_extrapolation += predict_next(history)

   return sum_extrapolation

with open('day_9.out', "w") as file:
   result = main()
   file.write(str(result))

file.close()
