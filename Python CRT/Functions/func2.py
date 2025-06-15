"""
functions:(4 types)
user defined functions
Built in functions
lamda functions
Recursion function

syntax:
def function_name():
    Local Variables
    block the statement
    return (variable or expression)
# all three represents function body

def function_name(para1,para2...)
    local variable
    block of statement
    return(ariable or expression)
note: need to maintain proper indentation
"""
def display():
    return "Hey..! I'm the zero arg function....!"
Res=display()
print(Res)
def Namefunction(name):
    return f"Hey..! I'm the one arg function called by {name}"
Res1=Namefunction("Navya")
print(Res1)