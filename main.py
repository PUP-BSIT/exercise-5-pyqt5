total_items = 5 # Initialize a variable with the quiz item count.
user_score = 0 # Initialize a variable for score count
# user_answer variable will be use to store user's answer
# TODO(Arguelles): Add your question, and implement answer checking logic












print("\n(Karl Christian Caya) What is my favorite color?")
print("a) Red               c) Yellow")
print("b) Orange            d) Green")

user_answer = input("Enter your answer: ").upper()
 
if user_answer == 'D':
    print(f"{user_answer} is correct.")
    user_score +=1
else:
    print(f"{user_answer} is incorrect. The correct answer is D.")

# TODO(Condino): Add your question, and implement answer checking logic











# TODO(Cordova): Add your question, and implement answer checking logic











# TODO(Gutierrez): Add your question, and implement answer checking logic











# Display user score
print(f"\nCongratulations! You got {user_score} out of {total_items} items.")