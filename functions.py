from datetime import datetime


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
        day = day_schedule[:2]
        hour = day_schedule[2:]
        working_day = create_dictionary_start_finish_time(hour)
        schedule_per_day_and_hour[day] = working_day
    return schedule_per_day_and_hour


def create_dictionary_start_finish_time(hour):
    working_day = {}
    hour_from, hour_to = hour.split("-")
    working_day["Start Time"] = parse_hour_string_to_datetime(hour_from)
    working_day["Finish Time"] = parse_hour_string_to_datetime(hour_to)
    return working_day


def parse_hour_string_to_datetime(hour,format_datetime="%H:%M"):
    return datetime.strptime(hour.strip(), format_datetime)


def create_dictionary_match_schedules_per_couples_employees(employees_schedule):
    cross_schedules = {}
    employees=list(employees_schedule.keys())
    for i in range(len(employees)):
        for j in range(i+1,len(employees)):
            couple_employee = employees[i] + "-" + employees[j]
            count = get_count_match_schedules_per_couples(employees_schedule[employees[i]], employees_schedule[employees[j]])
            cross_schedules[couple_employee] = count
    return cross_schedules


def get_count_match_schedules_per_couples(employee1_schedule, employee2_schedule):
    count = 0
    for day in employee1_schedule.keys():
        validation_employee1=validation_compare_schedules(employee1_schedule.get(day),employee2_schedule.get(day))
        validation_employee2=validation_compare_schedules(employee2_schedule.get(day),employee1_schedule.get(day))
        if validation_employee1 and validation_employee2:
            count += 1
    return count


def validation_compare_schedules(employee1_schedule,employee2_schedule):
    if employee1_schedule is not None and employee2_schedule is not None:
        times=employee2_schedule["Finish Time"]>=employee1_schedule["Start Time"]
        return times


def show_cross_schedules_employees(cross_schedules):
    for couples in cross_schedules:
        print(couples + " " + str(cross_schedules[couples]))