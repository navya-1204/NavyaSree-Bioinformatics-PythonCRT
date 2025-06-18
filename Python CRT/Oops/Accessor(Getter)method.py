class Employee():
    def __init__(self,Empname,EmpID,Designation,Salary,DeptName):
        print("Object is created.")
        self.Empname=Empname
        self.EmpID=EmpID
        self.Designation=Designation
        self.Salary=Salary
        self.DeptName=DeptName
    def Get_Details(self):
        print(self.Empname)
        print(self.EmpID)
        print(self.Designation)
        print(self.Salary)
        print(self.DeptName)
E1=Employee("Navya","EMP01","Data Engineer",35000,"EmploymentTeam")
E1.Get_Details()
