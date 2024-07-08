import csv

def save_score(x, y):
    with open("high_scores.csv", "a", newline = "" ) as high_scores_file:
        high_scores_writer = csv.writer(high_scores_file, delimiter = ";")
        list = [x, y]
        high_scores_writer.writerow(list)

def read_score():
    with open("high_scores.csv", "r") as high_scores_file_2:
        high_scores_reader = csv.reader(high_scores_file_2, delimiter = ";")
        list = []
        for line in high_scores_reader:
            list.append(line)
        return list

def get_top_3(list):
    global count_var
    list_2 = []
    list_3 = []
    best = []
    count_var = 0
    for k in list:
        list_2.append(k[1])

    while count_var < 3:
        for j in list:
            if j[1] == max(list_2):
                best.append(j)
                list.remove(j)
                break
            else:
                continue
        if len(list) == 1:
            count_var += 3
        elif len(list) == 2:
            count_var += 2
        elif len(list) >= 3:
            count_var += 1

    return best


