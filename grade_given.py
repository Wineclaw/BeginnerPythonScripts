# Chapter 5, Exercise 6

def grade_get(grade):
    """where 'grade' is the mark given""" # I know this makes no sense
    if grade >= 75:
        print("A grade of First is given")
    elif grade == 70:
        print("A grade of Upper Second or Second is given")
    elif grade > 70 and grade < 75:
        print("A grade of Upper Second is given")
    elif grade == 60:
        print("A grade of Second or Third is given")
    elif grade > 60 and grade < 70:
        print("A grade of Second is given")
    elif grade > 50 and grade < 60:
        print("A grade of Third is given")
    elif grade == 50:
        print("A grade of Third or F1 Supp is given")
    elif grade > 45 and grade < 50:
        print("A grade of F1 Supp is given")
    elif grade == 45:
        print("A grade of F1 Supp or F2 is given")
    elif grade > 40 and grade < 45:
        print("A grade of F2 is given")
    elif grade <= 40:
        print("A grade of F3 is given")
    else:
        print("No grade could be given")


xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
                     49.9, 45, 44.9, 40, 39.9, 2, 0]

for x in xs:
    grade_get(x)