total_items = 5 # Initialize a variable with the quiz item count.
user_score = 0 # Initialize a variable for score count
# user_answer variable will be use to store user's answer
# TODO(Arguelles): Add your question, and implement answer checking logic











# TODO(Caya): Add your question, and implement answer checking logic











# TODO(Condino): Add your question, and implement answer checking logic























# TODO(Gutierrez): Add your question, and implement answer checking logic
print("\n(King Andrei Gutierrez) When is my birthday?")
print("a)February 21, 2004          c)February 20, 2004")
print("b)February 20, 2005          d)February 21, 2005")

user_answer = input("Enter your answer: ").upper()

if user_answer == 'D':
    print(f"{user_answer} is Correct!")
    user_score += 1
else:
    print(f"{user_answer} is incorrect!. The correct answer is D.")
    
# Display user score
print(f"\nCongratulations! You got {user_score} out of {total_items} items.")