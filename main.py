import json

with open("questions.json", "r") as f:
    questions = json.load(f)

print(questions["questions"][1]["answer2"])