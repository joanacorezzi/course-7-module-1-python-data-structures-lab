
from .student_data import students  # import the student list from lib


def format_student_data(student):
    # Return a formatted string for a single student
    # unpack the tuple into separate variables
    student_id, name, major = student

    # build and return the string (do NOT print here)
    return f"ID: {student_id} | Name: {name} | Major: {major}"


def display_students(students_list):
   #Print information for each student in the list
   
    for student in students_list:
        # use the helper to get the text, then print it
        line = format_student_data(student)
        print(line)
# Only runs if we execute this file directly
if __name__ == "__main__":
    print("All students:")
    display_students(students)
