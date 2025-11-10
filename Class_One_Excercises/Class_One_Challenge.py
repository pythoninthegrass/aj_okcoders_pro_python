from datetime import date

name_of_user = input('Please enter your name: ')
age_of_user = int(input('Please enter your age: '))

date_today = date.today()

current_year = date_today.year

# print('Curr year: ', current_year)

# Get birth year of user. We need to subtract one year from the current year, since the user is going on another year, but has completed a certain number of years already. E.g., if someone is currently 44 years old in 2025, you cannot do 2025 - 44, because that would give you 1981, when the person was actually born in 1980 (1980 + 44 = 2024, not 2025). Thus, we cannot actually take into account the current year, we have to subtract one from it.
user_birth_year = (current_year - 1) - age_of_user

# Calculate the number of years it will take for the user to become 100 years old
years_to_100 = 100 - age_of_user

# Now add the current year to the above number (years_to_100); that will be the year in which the user turns 100 years old
year_turning_100 = (current_year - 1) + years_to_100

# Print the result with a formatted string
print(f'\nThanks {name_of_user}!')
print(f'Year in which you were born: {user_birth_year}')
print(f'Year in which you will turn 100 years old: {year_turning_100}')
