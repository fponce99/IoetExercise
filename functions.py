from datetime import datetime

def show_execution_menu():
    print("Menu:\n1.- Example 1\n2.- Example 2\n3.- Indicate path")
    print("Choice a option: ", end="")
    option = input()
    option_execution(option)


def option_execution(option):
    file=""
    if option=="1":
        file="./cronograma1.txt"
    elif option=="2":
        file="./cronograma2.txt"
    elif option=="3":
        print("Write the file path and change the backslash of the path for slash")
        file=input()
    else:
        print("Invalid option. Try again.")
        file=show_execution_menu()
    employee_data=readTxt(file)
    employees_schedule_list=parse_employees_schedules_string_to_dictionary(employee_data)
    cross_schedules=get_count_cross_schedules_per_couples_emloyees(employees_schedule_list)
    show_cross_schedules_employees(cross_schedules)


def readTxt(file_path):
    file = open(file_path, 'r')
    employee_data = file.readlines()
    file.close()
    return employee_data


def parse_employees_schedules_string_to_dictionary(employee_data):
    employees_schedules_dictionary={}
    for info in employee_data:
        employee, schedule = info.strip().split("=")
        employees_schedules_dictionary[employee]=create_dictionary_of_schedules_day_workingday(schedule)
    return employees_schedules_dictionary


def create_dictionary_of_schedules_day_workingday(schedule):
    schedule_per_day_and_hour = {}
    schedule_per_day = schedule.strip().split(",")
    for day_schedule in schedule_per_day:
        day_workingday = create_dictionary_schedule_per_day(day_schedule)
        schedule_per_day_and_hour[day_workingday["day"]] = day_workingday["working day"]
    return schedule_per_day_and_hour


def create_dictionary_schedule_per_day(day_schedule):
    schedule_of_the_day={}
    day = day_schedule[:2]
    hour = day_schedule[2:]
    working_day=create_dictionary_start_finish_time(hour)
    schedule_of_the_day["day"]=day
    schedule_of_the_day["working day"]=working_day
    return schedule_of_the_day


def create_dictionary_start_finish_time(hour):
    working_day = {}
    hour_from, hour_to = hour.split("-")
    working_day["Start Time"] = parse_hour_string_to_datetime(hour_from)
    working_day["Finish Time"] = parse_hour_string_to_datetime(hour_to)
    return working_day


def parse_hour_string_to_datetime(hour):
    return datetime.strptime(hour.strip(), "%H:%M")


def get_count_cross_schedules_per_couples_emloyees(employees_schedule):
    cross_schedules = {}
    employees=list(employees_schedule.keys())
    for i in range(len(employees)):
        for j in range(i+1,len(employees)):
            couple_employee = employees[i] + "-" + employees[j]
            count = get_count_cross_schedules_per_coupes(employees_schedule[employees[i]], employees_schedule[employees[j]])
            cross_schedules[couple_employee] = count
    return cross_schedules


def get_count_cross_schedules_per_coupes(employee1_schedule, employee2_schedule):
    count = 0
    for day in employee1_schedule.keys():
        validation_employee1=validation_compare_schedules(employee1_schedule.get(day),employee2_schedule.get(day))
        validation_employee2=validation_compare_schedules(employee2_schedule.get(day),employee1_schedule.get(day))
        if validation_employee1 or validation_employee2:
            count += 1
    return count

def validation_compare_schedules(employee1_schedule,employee2_schedule):
    if employee1_schedule!=None and employee2_schedule!=None:
        entry_time = employee1_schedule["Start Time"] <= employee2_schedule["Start Time"]
        closing_time = employee1_schedule["Finish Time"] >= employee2_schedule["Finish Time"]
        return entry_time and closing_time

def show_cross_schedules_employees(cross_schedules):
    for couples in cross_schedules:
        print(couples + " " + str(cross_schedules[couples]))