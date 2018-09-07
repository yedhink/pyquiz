from welcome import give_tips, welcome_text
from student import Student
from mcq import Mcq


def main():
    welcome_text()
    student = Student(input("Enter your name\t\t\t\t\t: "),
                      input("Enter your roll no\t\t\t\t: "),
                      input("Enter your department and batch : "),
                      0)
    print("\033c", end="")
    give_tips(student)
    mcq = Mcq({}, "", [], 0)
    mcq.read_questions()
    mcq.start_quiz(student)


if __name__ == '__main__':
    main()
