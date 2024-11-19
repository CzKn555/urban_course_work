#  самый короткий способ решения
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
print(dict(zip(students, list(map(lambda g: sum(g) / len(g), grades)))))

# используя только пройденный материал
mean_grades = (
        sum(grades[0])/len(grades[0]),
        sum(grades[1])/len(grades[1]),
        sum(grades[2])/len(grades[2]),
        sum(grades[3])/len(grades[3]),
        sum(grades[4])/len(grades[4]))

st_gr = {students[0]: mean_grades[0], students[1]: mean_grades[1],
         students[2]: mean_grades[2], students[3]: mean_grades[3],
         students[4]: mean_grades[4]}
print(st_gr)