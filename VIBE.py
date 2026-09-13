# Alicie Robertson
# CIS261
# WK10 VIBE Coding - Student Grade Calculator

import os
import sys


class Student:
    """Class to represent a student with grades and calculated metrics."""
    
    def __init__(self, name, student_id, test1, test2, test3):
        """Initialize a student with name, ID, and three test scores."""
        self.name = name
        self.id = student_id
        self.test1 = test1
        self.test2 = test2
        self.test3 = test3
        self.average = self._calculate_average()
        self.grade = self._calculate_grade()
    
    def _calculate_average(self):
        """Calculate the average of three test scores."""
        return (self.test1 + self.test2 + self.test3) / 3
    
    def _calculate_grade(self):
        """Calculate letter grade based on average score."""
        if self.average >= 90:
            return 'A'
        elif self.average >= 80:
            return 'B'
        elif self.average >= 70:
            return 'C'
        elif self.average >= 60:
            return 'D'
        else:
            return 'F'
    
    def __str__(self):
        """Return string representation of student."""
        return (f"{self.name} | {self.id} | {self.test1:.2f} | "
                f"{self.test2:.2f} | {self.test3:.2f} | {self.average:.2f} | {self.grade}")
    
    def to_file_format(self):
        """Return student data in pipe-delimited format for file storage."""
        return (f"{self.name}|{self.id}|{self.test1:.2f}|"
                f"{self.test2:.2f}|{self.test3:.2f}|{self.average:.2f}|{self.grade}")
    
    @staticmethod
    def from_file_format(line):
        """Create a Student object from pipe-delimited file format."""
        parts = line.strip().split('|')
        if len(parts) == 7:
            name, student_id, test1, test2, test3, average, grade = parts
            student = Student(name, student_id, float(test1), float(test2), float(test3))
            return student
        return None


def load_students(filename="student_grades.txt"):
    """Load student records from file."""
    students = []
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    student = Student.from_file_format(line)
                    if student:
                        students.append(student)
            print(f"\n✓ Loaded {len(students)} student records from '{filename}'.")
        except IOError as e:
            print(f"\n✗ Error loading file: {e}")
    return students


def save_students(students, filename="student_grades.txt"):
    """Save all student records to file."""
    try:
        with open(filename, 'w') as file:
            for student in students:
                file.write(student.to_file_format() + '\n')
        print(f"\n✓ Saved {len(students)} student records to '{filename}'.")
        return True
    except IOError as e:
        print(f"\n✗ Error saving file: {e}")
        return False


def add_student(students):
    """Prompt user to add a new student record."""
    print("\n" + "="*60)
    print("ADD NEW STUDENT")
    print("="*60)
    
    try:
        name = input("Enter student name: ").strip()
        if not name:
            print("✗ Student name cannot be empty.")
            return
        
        student_id = input("Enter student ID: ").strip()
        if not student_id:
            print("✗ Student ID cannot be empty.")
            return
        
        # Get test scores
        test1 = float(input("Enter Test 1 score (0-100): ").strip())
        if not (0 <= test1 <= 100):
            print("✗ Test score must be between 0 and 100.")
            return
        
        test2 = float(input("Enter Test 2 score (0-100): ").strip())
        if not (0 <= test2 <= 100):
            print("✗ Test score must be between 0 and 100.")
            return
        
        test3 = float(input("Enter Test 3 score (0-100): ").strip())
        if not (0 <= test3 <= 100):
            print("✗ Test score must be between 0 and 100.")
            return
        
        # Create and add student
        student = Student(name, student_id, test1, test2, test3)
        students.append(student)
        
        print(f"\n✓ Student '{name}' added successfully!")
        print(f"  Average: {student.average:.2f}")
        print(f"  Grade: {student.grade}")
        
    except ValueError:
        print("✗ Invalid input. Please enter valid numbers for test scores.")


def display_all_students(students):
    """Display all students in a formatted table."""
    if not students:
        print("\n✗ No student records found.")
        return
    
    print("\n" + "="*110)
    print("ALL STUDENT RECORDS")
    print("="*110)
    print(f"{'Name':<20} | {'ID':<12} | {'Test 1':<8} | {'Test 2':<8} | {'Test 3':<8} | {'Average':<8} | {'Grade':<6}")
    print("-"*110)
    
    for student in students:
        print(f"{student.name:<20} | {student.id:<12} | {student.test1:>7.2f} | "
              f"{student.test2:>7.2f} | {student.test3:>7.2f} | {student.average:>7.2f} | {student.grade:>5}")
    
    print("="*110)


def calculate_class_statistics(students):
    """Calculate and display class statistics."""
    if not students:
        print("\n✗ No student records found.")
        return
    
    averages = [student.average for student in students]
    highest_avg = max(averages)
    lowest_avg = min(averages)
    class_avg = sum(averages) / len(averages)
    
    # Find students with highest and lowest averages
    highest_student = [s for s in students if s.average == highest_avg][0]
    lowest_student = [s for s in students if s.average == lowest_avg][0]
    
    print("\n" + "="*60)
    print("CLASS STATISTICS")
    print("="*60)
    print(f"Total Students: {len(students)}")
    print(f"Class Average: {class_avg:.2f}")
    print(f"Highest Average: {highest_avg:.2f} ({highest_student.name})")
    print(f"Lowest Average: {lowest_avg:.2f} ({lowest_student.name})")
    print("="*60)


def search_student(students):
    """Search for a student by name (case-insensitive)."""
    if not students:
        print("\n✗ No student records found.")
        return
    
    search_name = input("\nEnter student name to search: ").strip().lower()
    
    if not search_name:
        print("✗ Search name cannot be empty.")
        return
    
    matching_students = [s for s in students if s.name.lower() == search_name]
    
    if not matching_students:
        print(f"✗ No student found with name '{search_name}'.")
        return
    
    print("\n" + "="*110)
    print(f"SEARCH RESULTS: '{search_name}'")
    print("="*110)
    print(f"{'Name':<20} | {'ID':<12} | {'Test 1':<8} | {'Test 2':<8} | {'Test 3':<8} | {'Average':<8} | {'Grade':<6}")
    print("-"*110)
    
    for student in matching_students:
        print(f"{student.name:<20} | {student.id:<12} | {student.test1:>7.2f} | "
              f"{student.test2:>7.2f} | {student.test3:>7.2f} | {student.average:>7.2f} | {student.grade:>5}")
    
    print("="*110)


def display_menu():
    """Display the main menu."""
    print("\n" + "="*60)
    print("STUDENT GRADE CALCULATOR")
    print("="*60)
    print("1. Add New Student")
    print("2. Display All Students")
    print("3. Calculate Class Statistics")
    print("4. Search Student by Name")
    print("5. Save Student Records")
    print("6. Exit (or press ESC)")
    print("="*60)


def main():
    """Main program loop."""
    print("\nWelcome to Student Grade Calculator!")
    
    # Load existing student records
    students = load_students()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip().upper()
        
        # Check for ESC (user might type 'ESC' or just press Enter on ESC key)
        if choice == 'ESC' or choice == '6':
            response = input("\nSave records before exiting? (y/n): ").strip().upper()
            if response == 'Y':
                save_students(students)
            print("\n✓ Thank you for using Student Grade Calculator. Goodbye!")
            break
        
        elif choice == '1':
            add_student(students)
        
        elif choice == '2':
            display_all_students(students)
        
        elif choice == '3':
            calculate_class_statistics(students)
        
        elif choice == '4':
            search_student(students)
        
        elif choice == '5':
            save_students(students)
        
        else:
            print("✗ Invalid choice. Please enter a valid option (1-6).")


if __name__ == "__main__":
    main()
