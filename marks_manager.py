def calculate_grade(average):
    if average >= 90:
        return 'A+'
    elif average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'
def student_manager():
    print("--- Students Mark Manager ---")
    name = input("Enter student name: ")
    try:
        m1 = float(input("Enter marks for Subject 1: "))
        m2 = float(input("Enter marks for Subject 2: "))
        m3 = float(input("Enter marks for Subject 3: "))
        total = m1 + m2 + m3
        average = total / 3
        grade = calculate_grade(average)

        print("\n--- Report Card ---")
        print(f"Student Name : {name}")
        print(f"Total Marks: {total:.2f} / 300")
        print(f"Average Marks: {average:.2f}%")
        print(f"Grade: {grade}")
    except ValueError:
        print("Invalid input! Please enter numeric values for marks.")
if __name__ == "__main__":
    student_manager()