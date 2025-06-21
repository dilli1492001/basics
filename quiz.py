question =[
    {
        "question":"what is the capital of india ?",
        "answer":["A.Ap","B.TG","C.DELHI","D.NONE"],
        "answer":"C"
    },
    {
        "question":"1+2 = ?",
        "answer":["A.1","B.3","C.2","D.6"],
        "answer":"B"
    }

]
count = 0
for i in question:
    print(f"Question : ",i["question"])
    print(f"question : ",i["answer"])
    a = input("enter your answer[A,B,C,D] : ")
    if a == i["answer"]:
        print("correct answer : a")
        count +=1
print(f"your score : {count}/2")