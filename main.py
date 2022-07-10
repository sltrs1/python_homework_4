import json


with open('abiturients.txt', 'r', encoding='utf-8') as fp:
    stud = json.load(fp)

studSort = sorted(stud, key=lambda d: d['score'])
studSort.reverse()

for s in studSort:
    print("Name:", s["last_name"], s["first_name"], s["middle_name"], "city:", s["city"], "age:", s["age"], "score:", s["score"])

while True:
    inp = input("Enter number of accepted students: ")
    if inp.isdigit():
       numAccepted = int(inp)
       break
    else:
        print("Incorrect number")

while True:
    inp = input("Enter minimal score to be accepted: ")
    if inp.isdigit():
       scoreAccepted = int(inp)
       break
    else:
        print("Incorrect number")

accepted = []

countAcc = 0
for s in studSort:
    if countAcc < numAccepted and s["score"] >= scoreAccepted:
        accepted.append(s)
        countAcc += 1

with open('result.txt', 'w', encoding='utf-8') as fp:
    json.dump(accepted, fp)