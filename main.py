import json



with open("questions.json", "r") as f:
    data = json.load(f)

def test():

    for i in data["questions"]:
        question = i["question"]
        answer = [i["answer"]]
        position = []

        ask = input(f"Question: {question} ")

        if ask in answer:
            print("Correct")
        else:
            print("Incorrect")
            print(f"Answer: {answer}")






test()