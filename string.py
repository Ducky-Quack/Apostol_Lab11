# Ask the user to enter 10 words
ten_words = []
print("Please enter 10 words in the entry.")

for i in range(1, 11):
    while True:
        word = input(f"Enter your word {i}: ")
        if word.isalpha():
            ten_words.append(word)
            break
        else: 
            print("Invalid input! Please enter a word with letters only (no numbers or special characters).")
print()

# Filtering words
while True: 
    num_letters_input = input("Enter the number of letters you want to be filter: ")
    if num_letters_input.isdigit():
        num_letters = int(num_letters_input)
        break
    else:
        print("Invalid input! Please enter with valid integer.")

matching_words = []
for word in ten_words:
    if len(word) == num_letters:
        matching_words.append(word)

# Printing the results
if matching_words:
    print(f"Here are the words with {num_letters} letters:")
    for word in matching_words:
        print(word)
    print()
else:
    print(f"No words with {num_letters} letters were found.")