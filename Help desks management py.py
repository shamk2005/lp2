# Expert System - Help Desk Management

def helpdesk_system():
    print("=== Help Desk Management System ===")

    name = input("Enter User Name: ")
    department = input("Enter Department: ")
    issue = input("Enter Issue: ").lower()

    # Expert Decision Rules
    if "password" in issue:
        solution = "Reset your password using the 'Forgot Password' option."
        priority = "Medium"

    elif "internet" in issue or "network" in issue:
        solution = "Check network cables and restart the router."
        priority = "High"

    elif "slow" in issue or "hang" in issue:
        solution = "Restart the computer and close unused applications."
        priority = "Medium"

    elif "printer" in issue:
        solution = "Check printer connection and reinstall printer drivers."
        priority = "Low"

    elif "software" in issue or "application" in issue:
        solution = "Update or reinstall the software."
        priority = "Medium"

    else:
        solution = "Contact technical support team for detailed assistance."
        priority = "High"

    # Display Report
    print("\n=== Help Desk Report ===")
    print("User Name :", name)
    print("Department :", department)
    print("Issue :", issue)
    print("Priority Level :", priority)
    print("Suggested Solution :", solution)

if __name__ == "__main__":
    helpdesk_system()



#INPUT


#Enter User Name: Diya
#Enter Department: Computer
#Enter Issue: internet not working

    
