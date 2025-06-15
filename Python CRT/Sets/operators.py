set={12,15,10,20,35}
print(type(set))
set.add(26)
print(set)
print(40 in set)
print(28 not in set)
# update
set1={100,85,23,99}
set.update(set1)
print(set)
# remove
set.remove(10)
print(set)
# pop
set.pop()
print(set)
# discard
set.discard(85)
print(set)
# union
set2={20,35,45,60,73}
# set2.union(set)
print(set2|set|set1)
# difference
print(set-set2)
# issubset
set.issubset(set2)
print(set)