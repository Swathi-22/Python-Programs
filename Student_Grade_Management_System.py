
def validate_mark(marks):
    for mark in marks:
        mark = int(mark)
        if mark < 0 or mark > 100:
            return False
    return True


def calculate_average(marks):
    toatl = 0
    for i in marks:
        toatl += int(i)
    avg = toatl / len(marks)
    return avg
    

def get_grade(average):
    if average >= 90:
        grade = "A"
    elif average >= 80 or average < 90:
        grade = "B"
    elif average >= 70 or average < 80:
        grade = "C"
    elif average >= 60 or average < 70:
        grade = "D"
    elif average < 60:
        grade = "F"
    return grade


marks = input("Enter marks for 5 subjects : ")
mrk_splt = marks.split()
if validate_mark(mrk_splt):
    average = calculate_average(mrk_splt)
    grade = get_grade(average)
    print(f"Average Marks: {average}")
    print(f"Grade: {grade}")
else:
    print("Error : Mark should between 0 and 100.")
