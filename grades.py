grades = []
x = 1

# "Grade entry" Machine
while True:
    entry = input(f"Enter your grade {x} (or type 'done' to finish): ")
   
    if entry.lower() == "done":
        if grades:
            break
        else:
            print("\nNo grades entered. Exiting the program...")
            exit()

    if entry.isdigit():
        grade = int(entry)
        if 40 <= grade <= 100:
            grades.append(grade)
            x += 1
        else:
            print("\nYou can only enter between 40-100 in range.\nExiting the program...\n")
            exit()
    else:
        print("\nYou have entered incorrect data.\nExiting the program...\n")
        exit()

if grades:
    # Computing average grades
    average_grade = round(sum(grades) / len(grades), 2)

    # Count passed subjects
    passed_grades = 0
    for i in range(len(grades)):
        if grades[i] >= 75:
            passed_grades += 1
        
    # Passed subjects Percentage (%)
    passing_ratio = round(passed_grades / len(grades) * 100)

    # Printing results
    print(f"\nYour average grades: {average_grade}%")
    print(f"Passed subjects: {passed_grades} ({passing_ratio}%)")
    print(f"Grades: {grades}\n")
else:
    print("\nNo valid grades entered.")