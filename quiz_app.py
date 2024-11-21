import pandas as pd
import random

quiz_size = 3


que_df = pd.read_csv('question_bank_new.csv')

questions = que_df.to_dict(orient='records')

print("Welcome to Quiz APP!!!!")
name = input("Enter ur Name: ")
print("Welcome {}!!".format(name))


selected_ques = {}

que_res = {}

score = 0


while(len(selected_ques) < quiz_size):
    que_no = random.randint(1, len(questions) - 1)
    if que_no not in selected_ques:
        selected_ques[que_no] = questions[que_no]

serial_no = 1

for que_no,que in selected_ques.items():
    print("\t{}. {} \n 1.{}\t\t2.{}\t\t3.{}\t\t\n".format(serial_no,
                                                            que['questions'],
                                                            que['a'],
                                                            que['b'],
                                                            que['c'],
                                                            ))
    ans = int(input("Enter ur Answer: "))
    if ans == que['d']:
        score += 10
    serial_no += 1

print("Your final score is {}".format(score))
print("")

# select your difficulty
#1.Easy Medium Hard
#2.score < 30 failed > 30 success