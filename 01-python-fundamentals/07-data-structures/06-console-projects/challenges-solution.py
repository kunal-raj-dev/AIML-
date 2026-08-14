def main():
    # Registry dictionary: subject -> [(student_name, score), ...]
    registry = {}

    while True:
        print("\n--- Gradebook Registry App ---")
        print("1 - Add Grade")
        print("2 - Calculate Class Averages")
        print("3 - Display Registry")
        print("4 - Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            subject = input("Enter subject name: ").strip().capitalize()
            student = input("Enter student name: ").strip().title()
            
            try:
                score_str = input("Enter student score: ").strip()
                score = float(score_str)
                if score < 0 or score > 100:
                    print("Error: Score must be between 0 and 100.")
                    continue
                
                if subject not in registry:
                    registry[subject] = []
                registry[subject].append((student, score))
                print(f"Successfully added grade for {student} in {subject}.")
            except ValueError:
                print("Error: Invalid score. Please enter a valid number.")

        elif choice == '2':
            if not registry:
                print("Registry is empty. No averages to calculate.")
            else:
                print("\nClass Averages per Subject:")
                for subject, students in registry.items():
                    total_score = sum(student[1] for student in students)
                    average = total_score / len(students)
                    print(f"- {subject}: {average:.2f} (Total students: {len(students)})")

        elif choice == '3':
            if not registry:
                print("Registry is empty.")
            else:
                print("\nGradebook Registry:")
                for subject, students in registry.items():
                    print(f"\nSubject: {subject}")
                    for student, score in students:
                        print(f"  * {student}: {score:.2f}")

        elif choice == '4':
            print("Exiting Gradebook App. Goodbye!")
            break

        else:
            print("Error: Invalid option. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
