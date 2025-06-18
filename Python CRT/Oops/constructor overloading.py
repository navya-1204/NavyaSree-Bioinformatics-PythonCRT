"""
write a python program to create an employee class and declare the states and create 5 objects 
using different constructors 
"""
class employee:
    def __init__(self, Empname,EmpID,Job,Salary,Location,Dept):
        self.Empname=Empname
        self.EmpID=EmpID
        self.Job=Job
        self.Salary=Salary
        self.Location=Location
        self.Dept=Dept
        print("Hey...!I'm a six parameterized constructor")
    def __init__(self, Empname,EmpID,Job,Salary,Location):
        self.Empname=Empname  
        self.EmpID=EmpID
        self.Job=Job
        self.Salary=Salary
        self.Location=Location
        print("Hey...!I'm a five parameterized constructor")
    def __init__(self, Empname,EmpID,Job,Salary):
        self.Empname=Empname
        self.EmpID=EmpID
        self.Job=Job
        self.Salary=Salary
        print("Hey...!I'm a four parameterized constructor")
    def __init__(self, Empname,EmpID,Job):
        self.Empname=Empname
        self.EmpID=EmpID
        self.Job=Job
        print("Hey...!I'm a three parameterized constructor")
    def __init__(self, Empname,EmpID):
        self.Empname=Empname
        self.EmpID=EmpID
        print("Hey...!I'm a two parameterized constructor")
    def __init__(self, Empname):
        self.Empname=Empname
        print("Hey...!I'm a one parameterized constructor")
    def __init__(self):
        print("Hey.I'm no parameterized constructor")
Emp1=employee()
