import math
import numpy as np

# Data structures
Students = []  # List of tuples: (name, student_id, dob)
Courses = []   # List of tuples: (course_name, course_id, credits)
Marks = {}     # Dict: {course_name: {student_id: mark}}


def input_student():
    total_student = int(input("Number of students in class: "))
    for _ in range(total_student):
        name = input("Student name: ")
        student_id = int(input("Student ID: "))
        dob = input("DoB: ")
        Students.append((name, student_id, dob))


def input_course():
    total_course = int(input("Number of courses: "))
    for _ in range(total_course):
        course_name = input("Course name: ")
        course_id = int(input("Course ID: "))
        credits = int(input("Credits: "))
        Courses.append((course_name, course_id, credits))


def input_mark():
    course = input("Course name to mark students: ")
    for c in Courses:
        if course == c[0]:  # Matching course name
            if course not in Marks:
                Marks[course] = {}
            for s in Students:
                raw_mark = float(input(f"{c[0]} mark for {s[0]}: "))
                # Round-down score to 1-digit decimal using math.floor
                rounded_mark = math.floor(raw_mark * 10) / 10.0
                Marks[course][s[1]] = rounded_mark  # Store by Student ID
            return
    print("Course not found!")


def calculate_gpa(student_id):
    student_marks = []
    course_credits = []

    for course in Courses:
        c_name = course[0]
        c_credit = course[2]

        # Check if student has a mark for this course
        if c_name in Marks and student_id in Marks[c_name]:
            student_marks.append(Marks[c_name][student_id])
            course_credits.append(c_credit)

    if not course_credits:
        return 0.0

    # Calculate weighted average GPA using NumPy arrays
    marks_array = np.array(student_marks)
    credits_array = np.array(course_credits)

    weighted_gpa = np.sum(marks_array * credits_array) / np.sum(credits_array)
    return round(weighted_gpa, 2)


def list_student():
    print("\n--- STUDENT INFO (Sorted by GPA Descending) ---")
    
    # Calculate GPA for all students and store in a list of tuples: (GPA, student_tuple)
    student_gpas = []
    for s in Students:
        gpa = calculate_gpa(s[1])
        student_gpas.append((gpa, s))

    # Sort students by GPA descending
    student_gpas.sort(key=lambda x: x[0], reverse=True)

    for gpa, s in student_gpas:
        print(f"Student name: {s[0]} - ID: {s[1]} - DoB: {s[2]} - GPA: {gpa}")


def list_course():
    print("\n--- COURSE INFO ---")
    for c in Courses:
        print(f"Course name: {c[0]}, Course ID: {c[1]}, Credits: {c[2]}")


def student_marks():
    print("\n--- VIEWING MARKS ---")
    course = input("Course name for viewing marks: ")
    if course in Marks:
        for student in Students:
            s_name, s_id = student[0], student[1]
            if s_id in Marks[course]:
                print(f"Student: {s_name} (ID: {s_id}), Mark: {Marks[course][s_id]}")
    else:
        print("No marks found for this course.")


# Main Execution
if __name__ == "__main__":
    input_student()
    input_course()
    input_mark()

    list_course()
    list_student()
    student_marks()
