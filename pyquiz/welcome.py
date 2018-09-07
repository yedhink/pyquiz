from colors import bcolors


def give_tips(student):
    welcome = "Hi {}. See if you can crack this quiz.".format(
        student.name)
    print('''
          ||{:=<93}||
          ||\t{:^89}||
          ||\t{:<89}||
          ||\t{:<89}||
          ||\t{:<89}||
          ||\t{:<89}||
          ||\t{:<89}||
          ||\t{:<89}||
          ||\t{:<89}||
          ||\t{:<89}||
          ||{:=<93}||
          \n'''
          .format(
              "",
              welcome,
              "",
              "keep these tips in mind :-",
              "1) this is not a race. so dont be stupid enough to not read the question properly",
              "2) all the questions have only a single answer",
              "3) while entering a choice, enter either 1,2,3,4",
              "4) oh c'mon! seriously? dont peek into others pc for answers :D",
              "",
              "press enter to continue...",
              "",
          )
          )
    try:
        input(bcolors.CBLINK2 +
              "YES! IM INTERESTED IN TAKING THIS SHITTY QUIZ"+bcolors.ENDC)
    except NameError:
        pass
    print("\033c", end="")


def welcome_text():
    print("\033c", end="")
    print('''
 {}  ███████             ███████            ██        {}
 {} ░██░░░░██  ██   ██  ██░░░░░██          ░░         {}
 {} ░██   ░██ ░░██ ██  ██     ░░██  ██   ██ ██ ██████ {}
 {} ░███████   ░░███  ░██      ░██ ░██  ░██░██░░░░██  {}
 {} ░██░░░░     ░██   ░██    ██░██ ░██  ░██░██   ██   {}
 {} ░██         ██    ░░██  ░░ ██  ░██  ░██░██  ██    {}
 {} ░██        ██      ░░███████ ██░░██████░██ ██████ {}
 {} ░░        ░░        ░░░░░░░ ░░  ░░░░░░ ░░ ░░░░░░  {}
    \n'''
          .format(
              bcolors.CBLUEBG2 + bcolors.CBLUE,   bcolors.ENDC,
              bcolors.CBLUEBG2 + bcolors.CBLUE,   bcolors.ENDC,
              bcolors.CBLUEBG2 + bcolors.CBLUE,   bcolors.ENDC,
              bcolors.CBLUEBG2 + bcolors.CBLUE,   bcolors.ENDC,
              bcolors.CBLUEBG2 + bcolors.CBLUE,   bcolors.ENDC,
              bcolors.CBLUEBG2 + bcolors.CBLUE,   bcolors.ENDC,
              bcolors.CBLUEBG2 + bcolors.CBLUE,   bcolors.ENDC,
              bcolors.CBLUEBG2 + bcolors.CBLUE,   bcolors.ENDC,
          )
          )
