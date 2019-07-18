def main():
    filename = "data.txt"
    students = {}

    populate_dicts(students, filename)
    add_letter_grades(students)
    display_students(students)

# This will add the student data from the file into the dictinoary that was initiailzed in the main() function
def populate_dicts(students, filename):
    datafile = open(filename)

    for line in datafile.readlines():
        cleaned = line.rstrip().split(',')
        id_number, grade = "".join(cleaned[1].split()), eval("".join(cleaned[2].split()))
        
        students[cleaned[0]] = [id_number, grade]

    datafile.close()

# This will add the letter grades to the end of the dictionary keys
def add_letter_grades(students):
    for student in students:
        grade = students[student][1]
        if grade >= 80:
            letter = "A"
        elif grade >= 65:
            letter = "B"
        elif grade >= 50:
            letter = "C"
        else:
            letter = "D"
        students[student].append(letter)

# This will write the student data to a new file (names, IDs, letter grades)
# Hint: start by figuring out how to print all the data needed
def display_students(students):
    for student in students:
        print(student.ljust(10)+str(students[student][0])+"   "+students[student][2])

if __name__ == "__main__":
    main()
