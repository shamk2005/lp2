# Expert System - Employee Performance Evaluation

def employee_system():

    print("==")
    print(" Employee Performance Evaluation ")
    print("==")

    # Employee Details
    name = input("Enter Employee Name : ")
    emp_id = input("Enter Employee ID : ")
    department = input("Enter Department : ")

    attendance = int(input("Enter Attendance Percentage : "))
    project = int(input("Enter Project Score (out of 100) : "))
    communication = int(input("Enter Communication Skill Score : "))
    teamwork = int(input("Enter Teamwork Score : "))

    # Calculate Average Score
    average = (project + communication + teamwork) / 3

    # Performance Evaluation
    if attendance >= 90 and average >= 85:
        performance = "Excellent"
        bonus = 10000
        promotion = "Eligible for Promotion"

    elif attendance >= 75 and average >= 65:
        performance = "Good"
        bonus = 5000
        promotion = "Can be Promoted Next Year"

    elif attendance >= 50 and average >= 40:
        performance = "Average"
        bonus = 2000
        promotion = "Needs Improvement"

    else:
        performance = "Poor"
        bonus = 0
        promotion = "Not Eligible"

    # Attendance Remark
    if attendance < 60:
        remark = "Attendance needs improvement."
    else:
        remark = "Attendance is satisfactory."

    # Display Report
    print("\n== Employee Report ==")
    print("Employee Name       :", name)
    print("Employee ID         :", emp_id)
    print("Department          :", department)
    print("Attendance          :", attendance, "%")
    print("Project Score       :", project)
    print("Communication Score :", communication)
    print("Teamwork Score      :", teamwork)
    print("Average Score       :", round(average, 2))
    print("Performance         :", performance)
    print("Bonus Amount        : ₹", bonus)
    print("Promotion Status    :", promotion)
    print("Remark              :", remark)

# Main Function
if __name__ == "__main__":
    employee_system()


#INPUT


#Enter Employee Name : Diya
#Enter Employee ID : E101
#Enter Department : IT
#Enter Attendance Percentage : 90
#Enter Project Score (out of 100) : 85
#Enter Communication Skill Score : 80
#Enter Teamwork Score : 88
