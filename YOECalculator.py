import datetime

# Set your starting year of experience
start_year = 2015  # Change this to your starting year
current_year = datetime.datetime.now().year
years_of_experience = current_year - start_year

# Write the result to a file
with open('years_of_experience.txt', 'w') as f:
    f.write(f"{years_of_experience} years of experience")
