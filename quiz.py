

questions = ("Who is Priyankar's crush?: ",
            "Who is wife of Vansh?: ",
            "Who is a good bro of Varnit?: ",
            "Who is a good hubby of mishraji?: ",
            "Who is the bf of chotu?: ")

options = (("A. Saumya", "B. Rose", "C. MOMO", "D. Gwen"), 
          ("A. Jhalak", "B. Chipkali", "C. Ananya", "D. Gayatri"),
          ("A. Vansh", "B. Mansi^2", "C. Pri", "D. All of the above"),
          ("A. Pushkar", "B. kaushal", "C. Deepak", "D. none of em"), 
          ("A. Rishab", "B. Someone from sec B", "C. mishraji(male)", "D. koi tho hai but bta nhi rhi"))

answers = ("A","D","D","C","C")

guesses= []
score = 0 
question_num = 0

for question in questions:
    print("------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input('Enter (A, B, C, D): ').upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print("CORRECT")
    else:
        print("WRONG!!!!")  
          
    question_num += 1