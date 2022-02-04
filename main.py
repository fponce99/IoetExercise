from functions import *
import os


print("Menu:\n1.- Example 1\n2.- Example 2\n3.- Indicate path\n4.- Run test")
print("Choice a option: ", end="")
option = input()
file=""
bucle=True
while(bucle):
    if option=="1":
        file="./cronograma1.txt"
    elif option=="2":
        file="./cronograma2.txt"
    elif option=="3":
        print("Write the file path and change the backslash of the path for slash")
        file=input()
    elif option=="4":
        os.system("python -m unittest -v test.py")
        exit(0)
    else:
        print("Invalid option. Try again.")
    employee_data = readTxt(file)
    employees_schedule_list=parse_employees_schedules_string_to_dictionary(employee_data)
    cross_schedules=create_dictionary_match_schedules_per_couples_employees(employees_schedule_list)
    show_cross_schedules_employees(cross_schedules)
    bucle=False