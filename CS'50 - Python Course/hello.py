# Ask user for their name
name = input("What's your name ? ")

# Remove Whitespace from string
# name = name.strip()

# Capitalize user's name
# name = name.capitalize()   # for capitalize first word
# name = name.title()  # for capitalize all word

# Remove and Capitalize first letter at the same time
name = name.strip().title()

# Say hello to user
print(f"Hello, {name}")

