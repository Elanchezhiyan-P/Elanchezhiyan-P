import datetime

# Set your starting year of experience
start_date = datetime.datetime(2015, 1, 1)  # Change to your actual start date
current_date = datetime.datetime.now()

# Calculate total months of experience
total_months = (current_date.year - start_date.year) * 12 + (current_date.month - start_date.month)

# Calculate years in decimal format
years_of_experience = total_months / 12
formatted_experience = f"{years_of_experience:.1f}"

# Update the README.md directly
readme_path = 'README.md'

# Read the current README
with open(readme_path, 'r') as f:
    readme_content = f.readlines()

# Update the line with the placeholder
for i, line in enumerate(readme_content):
    if '<!-- years_of_experience_placeholder -->' in line:
        readme_content[i] = line.replace('<!-- years_of_experience_placeholder -->', formatted_experience)
    else:
        # If it's not the line with the placeholder, ensure we keep the placeholder for next time
        if formatted_experience not in line:
            readme_content[i] = line.replace(formatted_experience, '<!-- years_of_experience_placeholder -->')

# Write the updated content back to README.md
with open(readme_path, 'w') as f:
    f.writelines(readme_content)
