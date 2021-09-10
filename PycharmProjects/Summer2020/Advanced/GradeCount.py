with open("grades.txt", "r+", encoding="utf-8") as dosya:
    list = dosya.read()

list = list.split("\n")

for i in range(len(list)):
    list[i] = list[i].split(",")


note_list = []

def count_grade(element):
    name = element[0]
    g1 = int(element[1])
    g2 = int(element[2])
    g3 = int(element[3])
    total = g1 * 0.3 + g2 * 0.3 + g3 * 0.4
    note_list.append(total)
    letterNote = str
    if total >= 95:
        letterNote = "AA"
    elif total >= 85:
        letterNote = "BA"
    elif total >= 75:
        letterNote = "BB"
    elif total >= 60:
        letterNote = "CC"
    else:
        letterNote = "FF"

    return "Name: {}\n".format(name) + "Grade: {}\n".format(total) + "Letter Note: {}\n".format(letterNote) + "------------------------------\n"




add_list = []
for i in range(len(list)):
    add_list.append(count_grade(list[i]))

sum = 0
for i in note_list:
    sum += i

average = sum / len(note_list)

with open("finals.txt", "w", encoding="utf-8") as file2:
    for element in add_list:
        file2.write(element)
    sentence = "Average is: {}".format(average)
    file2.write(sentence)

passed = []
not_passed = []

def passed_not():
    for i in range(len(list)):
        person_total = int(list[i][1]) * 0.3 + int(list[i][2]) * 0.3 + int(list[i][3]) * 0.4
        if person_total < average:
            result = list[i][0] + " " + str(person_total) + "\n"
            not_passed.append(result)
        else:
            result = list[i][0] + " " + str(person_total) + "\n"
            passed.append(result)

    with open("passed.txt", "w", encoding="utf-8") as dosya1:
        for a in passed:
            dosya1.write(a)

    with open("not_passed.txt", "w", encoding="utf-8") as dosya2:
        for b in not_passed:
            dosya2.write(b)

passed_not()








