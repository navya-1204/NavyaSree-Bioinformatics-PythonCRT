class Employee():
    def __init__(self,Empname,EmpID,Designation,Salary,DeptName): # constructor format fixed
        print("Object is created.")
        self.Empname=Empname
        self.EmpID=EmpID
        self.Designation=Designation
        self.Salary=Salary
        self.DeptName=DeptName
E1=Employee("Navya","EMP01","Data Analyst",25000,"DeploymentTeam")
print(f"Employee Name : {E1.Empname}")
print(f"Employee ID : {E1.EmpID}")
print(f"Employee Designation : {E1.Designation}")
print(f"Employee Salary : {E1.Salary}")
print(f"Department Name : {E1.DeptName}")