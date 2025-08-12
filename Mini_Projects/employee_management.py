# main menu function
employees = {}

def add_employee(emp_id,name,age,salary,department):
    employees[emp_id] = {
        "Name":name,
        "Age":age,
        "Salary":salary,
        "Dept":department
        }
    print(f"Employee {name} added successfully")
    
def view_employee():
    if employees:
        for emp_id,emp_details in employees.items():
            print(f"Id : {emp_id},Details: {emp_details}")
    else:
        print("No employees Added yet")

def update_employee(emp_id,name = None,age = None,salary = None,dept = None):
    try:
        if emp_id in employees:
            if name :
                employees[emp_id]["Name"] = name
            if age :
                employees[emp_id]['Age'] = age
            if salary:
                employees[emp_id]['Salary'] = salary
            if dept:
                employees[emp_id]['Dept'] = dept
            print(f"Employee {emp_id} updated succesfully")
        else:
            print(f"Emplyee with Id {emp_id} is Not Found")
            
    except KeyError as e:
        print(f"Error updating Employee Details : {emp_id}")

def remove_employee(emp_id):
    try:
        emp = employees.pop(emp_id)
        print(f"Employee {emp['Name']} removed successfully")
        
    except KeyError:
        print(f"Employee with Id {emp_id} not found")

def save_to_file(filename):
    try:
        with open(filename , "w") as file :
            for emp_id,details in employees.items():
                line = f"{emp_id} : -- > {details['Name']},{details['Age']},details['Salary'],details['department']"
        
        print("Employee data saved Successfully")
    except Exception as e:
        print(f" Error : {e}")
        
def load_from_file(filename):
    try:
        with open(filename,'r') as file:
            global employees
            employees = {} # clear the existing dictionary before loading
    
            for line in file:
                emp_data = line.strip().split(',')
                emp_id,name,age,salary,department = emp_data

                employees[emp_id] = {
                    'Name':name,
                    "Age":age,
                    'Salary':salary,
                    'dept':department
                    }
        print("Employee data loaded successfully")
    
    except FileNotFoundError :
        print(f"File {filename} not found")
        
    except Exception as e:
        print(f"Error : {e}")

                
def menu():

    while True:
        print("Welcome to the Employee Management System : ")
        
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Exit")

        choice = input("\nEnter your choice : ")
        
        if choice == "1":
            emp_id = input("Enter Employee Id : ")
            name = input("Enter Employee name : ")
            age = int(input("Enter Employee Age : "))
            salary = float(input("Enter your salary : "))
            department = input("Enter Department : ")
            
            add_employee(emp_id,name,age,salary,department)
            
        elif choice == "2":
            view_employee()
            
        elif choice == "3":
            emp_id = input("Enter Employee Id to update : ")
            name = input("Enter New Name (Leave blank to skip)") or None
            age_input = input("Enter New Age (Leave blank to skip): ")
            age_input = int(age_input) if age_input else None

            salary = input("Enter New Salary (Leave blank to skip)") or None
            salary = float(salary) if salary else None
            dept = input("Enter New Department (Leave blank to skip)") or None
            
            update_employee(emp_id,name,age,salary,dept)
            
        elif choice == "4":
            emp_id = input("Enter Employee Id to Remove : ")
            remove_employee(emp_id)
            
        elif choice == "5":
            filename = input("Enter file name to save : ")
            save_to_file(filename)
            
        elif choice == "6":
            filename = input("Enter filename to load : ")
            load_from_file(filename)
            
        elif choice == "7":
            break
        
        else:
            print(f"{choice} not a valid choice... Choose(1 to 7)")
        print()
        
        
menu()
