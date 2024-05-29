import random
import time

minimum_num = 0
maximum_num = 50
operator = ["+", "-", "*"]

want_to_play = 'yes'
asked_questions = 0


def question():
    num1 = random.randint(minimum_num, maximum_num)
    num2 = random.randint(minimum_num, maximum_num)
    ques = f"{str(num1)}  {random.choice(operator)}  {str(num2)}"
    return ques


while want_to_play == 'yes':
    try:
        no_of_questions = int(input("How many questions do you want?  "))
        ans = question()
        while asked_questions < no_of_questions:
            print(ans)
            start = time.time()
            try:
                guess = int(input("What is the answer ? "))
                if eval(ans) == guess:
                    stop = time.time()
                    print(f"{guess} is the right answer")
                    print(f"You solved the question in {round(stop - start)} seconds")
                    ans = question()
                    asked_questions += 1
                else:
                    print("That is not the right answer as integer !!!")
                    while guess != eval(ans):
                        guess = int(input("Please, write the correct answer! : "))
                        if eval(ans) == guess:
                            stop = time.time()
                            print(f"{guess} is the right answer")
                            print(f"You solved the question in {round(stop - start)} seconds")
                            asked_questions += 1
                    ans = question()
            except ValueError:
                print("Write an integer!!! ")
        want_to_play = input("Do you want to play again?? (yes / no): ")
        want_to_play = want_to_play.lower()
        if want_to_play != "no":
            asked_questions = 0
    except ValueError:
        print("Type an integer !!!")
