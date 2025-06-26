paper =[
    {"question":"2+2=?",
     "options":["A.1","B.5","C.4"],
     "answer":"C"},
     {
         "question":"2/2 = ?",
         "options":["A.1","B.2","C.3"],
         "answer":"A"
     },
     {
         "question":"2*2 = ?",
         "options":["A.4","B.2","C.1"],
         "answer":"A"
     }
]
score = 0
attemp = []
for i , q in enumerate(paper):
    print(f"Question {i+1} : {q.get("question")}")
    for options in q["options"]:
        print(options)
    chooice  = input("Enter your question : ")
    attemp_entry = (i, chooice , q["answer"])
    if chooice.upper() == q["answer"]:
        score += 2
    else :
        score -= 0.5
    attemp.append(attemp_entry)
    print(" ")


print(f"YOUR SCORE {score}")

print(f"SUMMARY")
print(f"******* user answer ******** correct answer")
for entry in attemp:
    index,user_answer,correct_answer = entry
    print(f"Question {index+1} :     {user_answer} :         {correct_answer}")



        























