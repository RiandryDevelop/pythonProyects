from Question import Question


Question_prompts = [
        "What color are the apples: \n(A)RED\n(B)YELLOW\n(C)GREEN\n\n",
        "What color are the bananas: \n(A)RED\n(B)YELLOW\n(C)GREEN\n\n",
        "What color are the limonade: \n(A)RED\n(B)YELLOW\n(C)GREEN\n\n"
]

questions = [
        Question(Question_prompts[0], 'A'),
        Question(Question_prompts[1], 'B'),
        Question(Question_prompts[2], 'C')
]

def run_test(questions):
        score = 0
        for question in questions:
                answer = input(question.prompt)
                if answer.upper() == question.answer:
                        score += 1

        print("You got: " + str(score) + "/" + str(len(questions)) + " correct")


run_test(questions)

print("Create a new Account right now:")
username = input("Username: ")
password = input("Password: ")

print("Your account have been created succesfully")
print("Log in Now!!")

username_Confirmation = input("Username: ")
password_Confirmation = input("Password: ")


if username == username_Confirmation and password == password_Confirmation:
        print("\nLogged in succesfullly")
else:
        print("\nInvalid credentials")