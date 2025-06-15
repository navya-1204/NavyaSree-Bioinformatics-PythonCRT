JobRole={101:'Full Stack Developer',102:'Cloud',103:'Data Analyst',104:'Data Scientist'}
print(JobRole)
JobRole[102]='Cloud Engineer'
print(JobRole)
del JobRole[102]
print(JobRole)
print(len(JobRole))
print(JobRole.keys())
print(JobRole.values())
print(JobRole.items())
b=JobRole.copy()
print(b)