# Information Management Expert System

def information_system():

    print(" Information Management System ")

    # Input
    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    city = input("Enter City : ")
    course = input("Enter Course : ")
    marks = float(input("Enter Percentage : "))

    # Grade Decision
    if marks >= 75:
        grade = "Excellent"
    elif marks >= 60:
        grade = "Good"
    elif marks >= 40:
        grade = "Average"
    else:
        grade = "Poor"

    # Status Decision
    if age >= 18:
        status = "Adult"
    else:
        status = "Minor"

    # Scholarship
    if marks >= 85:
        scholarship = "Eligible"
    else:
        scholarship = "Not Eligible"

    # Output
    print("\n Student Report ")
    print("Name :", name)
    print("Age :", age)
    print("City :", city)
    print("Course :", course)
    print("Percentage :", marks)
    print("Performance :", grade)
    print("Status :", status)
    print("Scholarship :", scholarship)


# Main Function
if __name__ == "__main__":
    information_system()


     #INPUT

    #Enter Name : Diya
#Enter Age : 22
#Enter City : pune
#Enter Course : Computer Engineering
#Enter Percentage : 88


