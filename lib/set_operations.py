
from .student_data import students  # shared students list


def unique_majors(students_list):
   # Return a set of unique majors from the list of students
    # Set comprehension to grab the third element (major) from each tuple
    return {student[2] for student in students_list}


# Only runs if we execute this file directly
if __name__ == "__main__":
    majors = unique_majors(students)
    print("Unique majors:")
    print(majors)
