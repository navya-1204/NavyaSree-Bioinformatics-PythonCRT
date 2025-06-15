#example1
Dict={101:'Python',102:'Java',103:'SQL',104:'Javascript'}
print(Dict)
print(type(Dict))
print(Dict[101])

#example2
#creating
Stu={101:'navya',102:'chamu',103:'midhi'}
Fees={'navya':2000,'chamu':3000,'midhi':5000}
#accessing complete dict
print(Stu)
#accessing req element
print(Stu[101])
print(Stu[102])
print(Stu[103])
print(Fees['navya'])
print(Fees['chamu'])
print(Fees['midhi'])
#modification
Fees['navya']=2500
Stu[102]='chamu'
print(Stu)
print(Fees)