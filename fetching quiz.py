import json
# https://opentdb.com/api_config.php -> To fetch more of these datas

with open("quix2.json", "r") as file:
    data = json.load(file)
    # print(k)

question = ""
difficulty = []
correct_answer = []
incorrect_answers = []

for ctn in data["results"]:
    # ctn["question"].append(question)
    ques = ctn["question"]
    # print(ques)
    # print(type(ques))
    # q = list(ques)
    # print(q)
    # print(type(q))
    ques.append(question)

# print(question)