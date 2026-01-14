#variables for my goals
goals_hours = 1000
hours_per_day = 4

#math from python
days_to_goal = goals_hours / hours_per_day

# The f-string replaces all three of your previous print lines
print(f"Goal: {goals_hours} hours. Progress: {hours_per_day} hrs/day. Total days needed: {days_to_goal}")

# print ("Days to reach my python learning goal:", days_to_goal)
# print("it will take me", days_to_goal, "days to reach my goal of", goals_hours, "hours of python learning.")
# print(days_to_goal)

# Asking for your name
user_name = input("What is your name? ")

# Printing a personalized greeting using an f-string
print(f"Welcome to the Python Lab, {user_name}!")