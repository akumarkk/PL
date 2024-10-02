students = {'john':['py', 'java'], 'navin': ['java']}

for i in students.keys():
    print( "students ", i, "are ")
    for c in students[i]:
        print("courses : ", c)