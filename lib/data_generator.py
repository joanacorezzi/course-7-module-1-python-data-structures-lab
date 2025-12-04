# This module defines a generator function to return

def student_generator(students, major):
    #Returns a generator that yields students with the given major.
    # Generator expression that filters students by their major
    return (student for student in students if student[2] == major)
# This block is only for manual testing (not used by pytest)
if __name__ == "__main__":
    from .student_data import students  # import from lib package

    print("Mathematics students (using generator):")
    math_gen = student_generator(students, "Mathematics")

    for student in math_gen:
        print(student)
