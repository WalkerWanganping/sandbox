"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    list_of_lists = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the intege is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        list_of_lists.append(parts)
        # print(parts)  # See if that worked
        # print("----------")
    return list_of_lists
    input_file.close()


def main():
    data = get_data()
    return data


def print_details():  # print course name, teacher's name and students number
    course_data = main()
    for i in range(1, int(len(course_data))+1):
        course_data_separate = course_data[i-1]
        print("{:2} is taught by {:2} and has {:2} students".format(course_data_separate[0],
        course_data_separate[1],course_data_separate[2]))


print_details()


