class Question():
    def __init__(self,prompt,answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "\033[1;31;40m 1.who wears the jersey number 18 in indian cricket team?\n a: MS dhoni\n b: Virat kohli\n c: Rohit sharma\n d: Sanju samson\n",
    "\n\n\033[1;32;40m 2.who won the ballon d'or most times?\n a: Cristiano ronaldo\n b: Mezut ozil\n c: lionel messi\n d: nicolas ottamendi\n",
    "\n\n \033[1;33;40m 3.which national  team has won the euro cup last year?\n a: Italy\n b: Germany\n c: Spain\n d: Switzerland\n",
    "\n\n \033[1;36;40m 4.which country,s domestic football league is known as bundes liga?\n a: Argentina\n b: Brazil\n c: Germany\n d: France\n",
    "\n\n \033[1;33;40m 5.Which player scored the fastest hat-trick in the Premier League?\n a: mohammed salah\n b: christian erikson\n c: vardy\n d: Mane\n",
    "\n\n \033[1;33;40m 6.In which year the ballon dor was awareded to former brazilian international kaka?\n a: 2007\n b: 2011\n c: 2008\n d: 2012\n",
    "\n\n \033[1;36;40ma 7.In which year lionel messi has made his debute at FC Barcelona?\n a: 2003\n b: 2004\n c: 2005\n d: 2006\n",
    "\n\n \033[1;36;40ma 8.Puskas award will be given to ?\n a: best goal of the year\n b: best goalkeeper of the year\n c: best defender of the year\n d: best best striker of the year\n",
    "\n\n \033[1;36;40ma 9.In which year leicester city has won the english premier league?\n a: 2007/08\n b: 2010/11\n c: 2014/15\n d: 2017/18\n",
    "\n\n \033[1;36;40ma 10.Which team has won the uefa champions leauge most times?\n a: barcelona\n b: real madrid\n c: chelsea\n d: manchester city\n"

]



questions = [ Question(question_prompts[0],"b"),
               Question(question_prompts[1], "c"),
               Question(question_prompts[2], "a"),
               Question(question_prompts[3], "c"),
              Question(question_prompts[4], "d"),
              Question(question_prompts[5], "a"),
              Question(question_prompts[6], "b"),
                Question(question_prompts[7],"a"),
               Question(question_prompts[8], "c"),
               Question(question_prompts[9], "b")
              ]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer =(input(question.prompt)).lower()
        if answer == question.answer:
            score += 1
    print("\n\n YOU GOT " + str(score) + "/" + str(len(questions)))
    if score == len(questions):
        print("\n DAMN YOU GOT IT FULL !!")
    if score == 0:
        print("\n YOU LOSER !!")


run_quiz(questions)





