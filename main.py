import json

with open("questions.json", "r") as f:
    questions = json.load(f)

for i in questions["questions"]:
    print(i)


# print(questions["questions"][0]["question1"])
