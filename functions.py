from datetime import datetime


def readTxt(file_path):
    file = open(file_path, 'r')
    employee_data = file.readlines()
    file.close()
    transform_employees_schedules_string_to_lists(employee_data)


def transform_employees_schedules_string_to_lists(employee_data):
    employees_list = []
    schedule_list = []
    for info in employee_data:
        employee, schedule = info.strip().split("=")
        employees_list.append(employee)
        schedule_list.append(schedule)
    schedule_dictionary_day_workingday = create_dictionary_of_schedules_day_workingday(schedule_list)
    join_employee_with_schedule(employees_list, schedule_dictionary_day_workingday)


def join_employee_with_schedule(employees_list, schedule_list_tranformed):
    employees_schedule_list = {}
    for i in range(len(employees_list)):
        employees_schedule_list[employees_list[i]] = schedule_list_tranformed[i]
    get_couples_emloyees(employees_schedule_list)


def create_dictionary_of_schedules_day_workingday(schedule_list):
    schedule_employee_list = []
    for schedule in schedule_list:
        schedule_per_day_and_hour = {}
        schedule_per_day = schedule.strip().split(",")
        for day_schedule in schedule_per_day:
            day_workingday = transform_string_to_datetime(day_schedule)
            schedule_per_day_and_hour[day_workingday[0]] = day_workingday[1]
        schedule_employee_list.append(schedule_per_day_and_hour)
    return schedule_employee_list


def transform_string_to_datetime(day_schedule):
    working_day = []
    day = day_schedule[:2]
    hour = day_schedule[2:]
    hour_from, hour_to = hour.strip().split("-")
    working_day.append(datetime.strptime(hour_from, "%H:%M"))
    working_day.append(datetime.strptime(hour_to.strip(), "%H:%M"))
    return [day, working_day]


def get_couples_emloyees(employees_schedule):
    cross_schedules = {}
    couples_check = create_dictionary_couples_check(employees_schedule)
    for employee1 in employees_schedule.keys():
        for employee2 in employees_schedule.keys():
            validation_first_employeeCheck = couples_check[employee2].__contains__(employee1)
            validation_second_employeeCheck = couples_check[employee1].__contains__(employee2)
            if employee1 != employee2 and (not validation_first_employeeCheck and not validation_second_employeeCheck):
                couple_employee = employee1 + "-" + employee2
                couples_check[employee1].append(employee2)
                couples_check[employee2].append(employee1)
                count = compare_schedules(employees_schedule[employee1], employees_schedule[employee2])
                cross_schedules[couple_employee] = count
    show_cross_schedules_employees(cross_schedules)


def create_dictionary_couples_check(employees_schedule):
    couples_check = {}
    for employee1 in employees_schedule.keys():
        couples_check[employee1] = []
    return couples_check


def compare_schedules(employee_schedule1, employee_schedule2):
    count = 0
    for day in employee_schedule1.keys():
        if employee_schedule2.keys().__contains__(day):
            entry_time = employee_schedule2[day][0] >= employee_schedule1[day][0] and employee_schedule2[day][0] < \
                         employee_schedule1[day][1]
            closing_time = employee_schedule2[day][1] <= employee_schedule1[day][1] and employee_schedule2[day][1] > \
                           employee_schedule1[day][0]
            if entry_time and closing_time:
                count += 1
    return count


def show_cross_schedules_employees(cross_schedules):
    for couples in cross_schedules:
        print(couples + " " + str(cross_schedules[couples]))
