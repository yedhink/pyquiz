from colors import bcolors
from time import sleep


class Mcq:

    def __init__(self, qno, question, choices, correct_ans):
        self.qno = qno
        self.question = question
        self.choices = choices
        self.correct_ans = correct_ans

    def read_questions(self):
        fo = open("./data/quiz.txt", "r")
        lines = fo.readlines()
        fo.close()
        n = 0
        for i in range(0, len(lines), 7):
            self.question = lines[i]
            self.choices = lines[i+1:i+5]
            self.correct_ans = lines[i+5]
            self.qno[n] = [self.question, self.choices, self.correct_ans]
            n += 1

    def start_quiz(self, student):
        for key in self.qno.keys():
            ask_question(self.qno[key])
            get_ans(self.qno[key], student, self.qno[key][2][0])
        scores(student)


def get_ans(ques, student, num):
    print("Enter 1 or 2 or 3 or 4 as your answer" +
          bcolors.UNDERLINE+bcolors.CBOLD)
    choice = int(input("Enter your choice :"+bcolors.ENDC+" "))
    print(bcolors.ENDC)
    if choice == int(num):
        student.mark += 1
        print('''
{}Great job mate. You answered correctly.{}\n
{}CORRECT ANSWER{}
{}> choice {}{}\n
{}HOW?{}
{}> {}{}
                '''.format(
            bcolors.FAIL, bcolors.ENDC,
            bcolors.UNDERLINE, bcolors.ENDC,
            bcolors.FAIL+bcolors.BOLD, num, bcolors.ENDC,
            bcolors.UNDERLINE, bcolors.ENDC,
            bcolors.FAIL+bcolors.BOLD, ques[2][3:].rstrip(), bcolors.ENDC,
        )
        )
    else:
        print('''
{}You've got it wrong!! See below for the correct answer{}\n
{}CORRECT ANSWER{}
{}> choice {}{}\n
{}HOW?{}
{}> {}{}
                '''.format(
            bcolors.CRED, bcolors.ENDC,
            bcolors.UNDERLINE+bcolors.CGREENBG2, bcolors.ENDC,
            bcolors.FAIL+bcolors.BOLD, num, bcolors.ENDC,
            bcolors.UNDERLINE+bcolors.CGREENBG2, bcolors.ENDC,
            bcolors.FAIL+bcolors.BOLD, ques[2][3:].rstrip(), bcolors.ENDC,
        )
        )
    try:
        input(bcolors.CBLINK2+"PRESS ANY KEY TO CONTINUE"+bcolors.ENDC)
    except NameError:
        pass
    print("\033c", end="")


def ask_question(ques):
    print('''
||{:=<145}||
||\t{}{:<143}{}||
||{:=<145}||
            '''
          .format("", bcolors.BOLD+bcolors.CGREEN, ques[0].rstrip(), bcolors.ENDC, "")
          )
    print('''
||{:=<42}||{:=<101}||
||\t{}{:<40}{}|| {}{:<100}{}||
||\t{}{:<40}{}|| {}{:<100}{}||
||{:=<42}||{:=<101}||
            '''
          .format("", "",
                  bcolors.BOLD +
                      bcolors.CGREEN, ques[1][0].rstrip(), bcolors.ENDC,
                  bcolors.BOLD +
                      bcolors.CGREEN, ques[1][1].rstrip(), bcolors.ENDC,
                  bcolors.BOLD +
                      bcolors.CGREEN, ques[1][2].rstrip(), bcolors.ENDC,
                  bcolors.BOLD +
                      bcolors.CGREEN, ques[1][3].rstrip(), bcolors.ENDC,
                  "", "")
          )


def scores(student):
    score_sheet = {
        0: "And dont you worry mate. start working on python from today and you will come out better",
        1: "And dont you worry mate. start working on python from today and you will come out better",
        2: "And dont you worry mate. start working on python from today and you will come out better",
        3: "And dont you worry mate. start working on python from today and you will come out better",
        4: "And dont you worry mate. start working on python from today and you will come out better",
        5: "And dont you worry mate. start working on python from today and you will come out better",
        6: "And dont you worry mate. start working on python from today and you will come out better",
        7: "And dont you worry mate. start working on python from today and you will come out better",
        8: "And dont you worry mate. start working on python from today and you will come out better",
        9: "And dont you worry mate. start working on python from today and you will come out better",
        10: "And good job. I'm gonna assume that you didnt cherry pick the answers and got lucky! :D",
    }
    bye = "it was a pleasure knowing you {}({}) of {}".format(
        student.name, student.roll, student.course)
    print('''
||{:=<145}||
||\t{}{:^143}{}||
||{:=<145}||
            '''
          .format(
              "",
              bcolors.BOLD+bcolors.CGREEN+bcolors.CBLUEBG2,
              bye,
              bcolors.ENDC,
              "",
          )
          )
    sleep(3.0)
    print("\033c", end="")
    print('''
||{:=<145}||
||\t{}{:^143}{}||
||{:<145}||
||\t{}{:^143}{}||
||{:=<145}||
            '''
          .format(
              "",
              bcolors.BOLD+bcolors.CGREEN,
              score_sheet[student.mark],
              bcolors.ENDC,
              "",
              bcolors.BOLD+bcolors.CGREEN,
              "Your final score is "+str(student.mark)+"/10",
              bcolors.ENDC,
              ""
          )
          )
    sleep(5.0)
    print("\033c", end="")
