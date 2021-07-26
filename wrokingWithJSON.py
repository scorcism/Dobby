import json

jsonn = {
    "results": [
        {
            "category": "Entertainment: Video Games",
            "type": "multiple",
            "difficulty": "medium",
            "question": "When Halo 3: ODST was unveiled in 2008, it had a different title. What was the game formally called?",
            "correct_answer": "Halo 3: Recon",
            "incorrect_answers": [
                "Halo 3: Helljumpers",
                "Halo 3: Phantom",
                "Halo 3: Guerilla"
            ]
        }
    ]
}

# k  =(json.dumps(jsonn))
# print(k)

print(jsonn['results'][0]['correct_answer'])