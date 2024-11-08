grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# преобразование множества в список с помощью функции list()
stud_list = list(students)
# После преобразования множества в список сортируем с помощью sorted()
stud_sorted = sorted(stud_list)
#print(stud_sorted)
# разобъём на группы для расчёта средней
from statistics import mean
grades_0 = (grades[0])
avg0 = mean(grades_0)
#print("The average is ", round(avg0, 2))
grades_1 = (grades[1])
avg1 = mean(grades_1)
#print("The average is ", round(avg1, 2))
grades_2 = (grades[2])
avg2 = mean(grades_2)
#print("The average is ", round(avg2, 2))
grades_3 = (grades[3])
avg3 = mean(grades_3)
#print("The average is ", round(avg3, 3))
grades_4 = (grades[4])
avg4 = mean(grades_4)
#print("The average is ", round(avg4, 3))
# соберём список средних значений
avg_list = [avg0, avg1, avg2, avg3, avg4]
#print(avg_list)
# объеденим списки в словарь с помощью dict(zip())
journal = dict(zip(stud_sorted, avg_list))
print(journal)