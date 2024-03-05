names = ['name1', 'name2', 'name3', 'name4']
grades = [100, 90, 80, 70]

grades_dict = {key:value+10 for key, value in zip(names, grades)}

print(grades_dict)