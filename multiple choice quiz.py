from questions import question
question_ptompts=[
    "what color are apples?\n (a) Red/Green\n(b) purple\n (c)orange\n\n" ,
    "what color are banans?\n (a) Red/Green\n Magenta\n (c) Yellow\n\n" ,
     "what color are strawberries?\n (a) Yellow\n (b)Red\n (c)Blue\n\n"
]
questions=[
    question(question_ptompts[0],"a"),   #object from the class    "instance"question(question.promt,question.answer)
    question(question_ptompts[1],"c"),
    question(question_ptompts[2],"b")
]
def start_exam(questions):  #pass the list
    score=0
    for question in questions:
        answer=input(question.prompt)
        if answer==question.answer:
           score+=1
    print("you get "+ str(score)+ "/"+str(len(questions))+" correct")
start_exam(questions)