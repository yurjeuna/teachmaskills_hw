name = input("Hi! What's your name, friend? ")
year_birth = int(input("Ok,do you remember when you were born? \
Let's start with the year of birth - "))
month_birth = int(input("The month of your birth - "))
day_birth = int(input("And the day of your birth, please, - "))
experience = int(input("Have you studied programming before? \
Choose the right option: 1 No 2 On your own 3 On course 4 In the university "))
goal = input("What are your expectations from this course? Continue the phrase: I'm here for ... ")
year_now = int(input("So the last question," + name + ". What's the date of filling this form? \
Let's start with the year of filling - "))
month_now = int(input("The month of filling - "))
day_now = int(input("And the day of filling, please, - "))
if month_birth > month_now:
    age = year_now - year_birth
elif month_birth < month_now:
    age = year_now - year_birth + 1
elif month_birth == month_now:
    if day_birth > day_now:
        age = year_now - year_birth
    else:
        age = year_now - year_birth + 1
print("Thank you, ", name, ". You are ", age, " years old. It's the perfect age.", sep='')
if experience == 1:
    print("You haven't any experience in programming.")
elif experience == 2:
    print("You tried to study programming on your own.")
elif experience == 3:
    print("You have already tried to study programming on some course.")
elif experience == 4:
    print("You studied programming in the university.")
print("And now you are here for ", goal, ". So good luck to you! See you on lessons.", sep='')
