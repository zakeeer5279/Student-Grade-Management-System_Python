# List to store all student data
students = []

# Function to calculate total score and grade
def calculate_grade(scores):
    total = sum(scores)
    average = total / len(scores)
    
    # Grading criteria (can be modified as needed)
    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    return total, grade

# Function to input student details
def input_student_data(name=None, student_id=None, scores=None):
    # If no name is provided, ask for input
    if name is None:
        name = input("Enter student name: ")
    if student_id is None:
        student_id = input("Enter student ID: ")
    
    # If no scores are provided, ask for input
    if scores is None:
        scores = []
        for i in range(1, 4):
            score = float(input(f"Enter score for subject {i}: "))
            scores.append(score)
    
    # Calculate total and grade
    total, grade = calculate_grade(scores)
    
    # Store student data
    student = {
        'name': name,
        'id': student_id,
        'scores': scores,
        'total': total,
        'grade': grade
    }
    students.append(student)
    print(f"\n{name}'s total score is {total} and their grade is {grade}.\n")

# Function to display all students' details
def display_all_students():
    if not students:
        print("No student data available.")
        return
    
    print("\n--- Student Details ---")
    for student in students:
        print(f"Name: {student['name']}, ID: {student['id']}, Scores: {student['scores']}, Total: {student['total']}, Grade: {student['grade']}")
    print()

# Main program loop
def main():
    # Pre-add Zakir's details
    zakir_scores = [85, 78, 92]  # Example scores for Zakir in 3 subjects
    input_student_data(name="Zakir", student_id="22593", scores=zakir_scores)
    
    while True:
        print("Student Grade Management System")
        print("1. Add a Student")
        print("2. Display All Students")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            input_student_data()
        elif choice == '2':
            display_all_students()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

# Run the program
if __name__ == "__main__":
    main()
