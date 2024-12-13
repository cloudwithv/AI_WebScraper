import json



with open("questions.json", "r") as f:
    data = json.load(f)

def test():

    for i in data["questions"]:
        question = i["question"]
        answer = i["answer"]
        position = []

        ask = input(f"{question} \n")

        if not isinstance(answer, list):
            if ask == answer:
                print("Correct")
            if ask != answer:
                print("Incorrect")
                print(f"Answer: {answer}")

        else:
            if isinstance(answer, list):
                if ask in answer:
                    print("Correct")
                if ask not in answer:
                    print("Incorrect")
                    print(f"Answer: {answer}")






test()