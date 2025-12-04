
from .student_data import students  # import the shared students list


def filter_students_by_major(students_list, major):
   # Return a list of students who have the given major

    # Use a list comprehension to filter by major
    return [student for student in students_list if student[2] == major]


# Only runs if we execute this file directly
if __name__ == "__main__":
    cs_students = filter_students_by_major(students, "Computer Science")
    print("Students with major 'Computer Science':")
    for s in cs_students:
        print(s)
