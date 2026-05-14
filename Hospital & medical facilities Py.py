# Expert System - Hospital and Medical Facilities

def hospital_system():
    print("=== Hospital Expert System ===")

    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    problem = input("Enter Health Problem: ").lower()

    # Expert Decision
    if "fever" in problem or "cold" in problem:
        doctor = "General Physician"
        advice = "Take rest and drink plenty of fluids."

    elif "heart" in problem or "chest pain" in problem:
        doctor = "Cardiologist"
        advice = "ECG and heart checkup recommended."

    elif "skin" in problem or "allergy" in problem:
        doctor = "Dermatologist"
        advice = "Avoid dust and use prescribed medicines."

    elif "bone" in problem or "fracture" in problem:
        doctor = "Orthopedic"
        advice = "X-ray and proper rest required."

    else:
        doctor = "General Checkup"
        advice = "Consult hospital for detailed diagnosis."

    # Display Report
    print("\n=== Patient Report ===")
    print("Name :", name)
    print("Age :", age)
    print("Problem :", problem)
    print("Suggested Doctor :", doctor)
    print("Advice :", advice)

if __name__ == "__main__":
    hospital_system()



    #INPUT

#Enter Patient Name: Diya
#Enter Age: 22
#Enter Health Problem: Fever
