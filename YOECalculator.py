import datetime
import re

# Define your start date (e.g., 2019-01-01)
start_date = datetime.date(2019, 8, 1)

# Calculate the difference between today and the start date
today = datetime.date.today()
experience_years = today.year - start_date.year + (today.month - start_date.month) / 12

# Round the experience to 1 decimal place
experience_years = round(experience_years, 1)

# Read the existing README.md file with utf-8 encoding
with open("README.md", "r", encoding="utf-8") as file:
    readme_content = file.read()

# Use regex to find and update the experience value dynamically
pattern = r"(\d+\.\d+) years of hands-on experience"
updated_readme_content = re.sub(pattern, f"{experience_years} years of hands-on experience", readme_content)

# Write the updated content back to the README.md file with utf-8 encoding
with open("README.md", "w", encoding="utf-8") as file:
    file.write(updated_readme_content)

print(f"Experience updated to {experience_years} years.")
