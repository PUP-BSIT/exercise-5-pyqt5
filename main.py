total_items = 5 # Initialize a variable with the quiz item count.
user_score = 0 # Initialize a variable for score count
# user_answer variable will be use to store user's answer
# TODO(Arguelles): Add your question, and implement answer checking logic











# TODO(Caya): Add your question, and implement answer checking logic












print("\n(Ciara Marie Condino) What is my favorite game? ")
print("a) Valorant			c) Minecraft")
print("b) Roblox			d) Mobile Legends")

user_answer = input("Enter your answer: ").upper()

if user_answer == "C":
    print(f"{user_answer} is correct.")
    user_score += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is C.")










# TODO(Cordova): Add your question, and implement answer checking logic
print("\n(Aron Stephen Cordova) What is the chemical symbol for Gold?")
print("a) Au           c) Ag")
print("b) Fe           d) Pb")

user_answer = input("Enter your answer: ").upper()

if user_answer == "A":
    print(f"{user_answer} is correct.")
    user_score += 1
else:
    print(f"{user_answer} is incorrect. The correct answer is A")
# TODO(Gutierrez): Add your question, and implement answer checking logic











# Display user score
print(f"\nCongratulations! You got {user_score} out of {total_items} items.")