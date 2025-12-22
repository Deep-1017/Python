set1 = {10, 20, 30, 40, 60}
set2 = {50, 60, 20}

x = frozenset({100, 200}) 
print(x) 

print(set1)
# set3 = set1.union(set2) 
# set1 | set2 
# set3 = set1.intersection(set2)
# set3 = set2.difference(set1) 
set3 = set1.symmetric_difference(set2)


print(set3) 