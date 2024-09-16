def task():

    # grade should be a tuple containing student name (str), subject (str) and score (int)
    name = input("student name \n")
    sub = input("subject studied \n")
    score = int(input("test score \n"))
    grade = (name , sub , score)

    return grade
