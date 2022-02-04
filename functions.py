from datetime import datetime

#
def readTxt(file_path):
    """
    Read the file and get the data
    ...
    Parameters
    ----------
    file_path : str
        The schedule file path

    Return
    ------
    employee_data: str
        The data of the file
    """
    file = open(file_path, 'r')
    employee_data = file.readlines()
    file.close()
    return employee_data


def parse_employees_schedules_string_to_dictionary(employee_data):
    """
    Get a dictionary with employee as a key and schedule as value
    ...
    Parameters
    ----------
    employee_data : list
        The list of file lines

    Return
    ------
    employees_schedules_dictionary : dict
        A dictionary that include the employee with his schedule
    """
    employees_schedules_dictionary={}
    for info in employee_data:
        employee, schedule = info.strip().split("=")
        employees_schedules_dictionary[employee]=create_dictionary_of_schedules_day_workingday(schedule)
    return employees_schedules_dictionary


def create_dictionary_of_schedules_day_workingday(schedule):
    """
    Get a dictionary with day as a key and a dictionary with the times as a value
    ...
    Parameters
    ----------
    schedule : str
        A string of employee schedule

    Return
    ------
    schedule_per_day_and_hour : dict
        A dictionary that contains the start time and finish time per day
    """
    schedule_per_day_and_hour = {}
    schedule_per_day = schedule.strip().split(",")
    for day_schedule in schedule_per_day:
        day = day_schedule[:2]
        hour = day_schedule[2:]
        working_day = create_dictionary_start_finish_time(hour)
        schedule_per_day_and_hour[day] = working_day
    return schedule_per_day_and_hour


def create_dictionary_start_finish_time(hour):
    """
    Separate the string with the times and save in a dictionary.
    ...
    Parameters
    ----------
    hour : str
        A string of schedule of the day

    Return
    ------
    working_day : dict
        A dict that contains the start time and finish time of employee
    """
    working_day = {}
    hour_from, hour_to = hour.split("-")
    working_day["Start Time"] = parse_hour_string_to_datetime(hour_from)
    working_day["Finish Time"] = parse_hour_string_to_datetime(hour_to)
    return working_day


def parse_hour_string_to_datetime(hour,format_datetime="%H:%M"):
    """
    Parse a string to datetime
    ...
    Parameters
    ----------
    hour : str
        A string of start time or finish time
    format_datetime : str
        The format to convert the string

    Return
    ------
    datetime.strptime(hour.strip(), format_datetime) : datetime
        A datatime
    """
    return datetime.strptime(hour.strip(), format_datetime)


def create_dictionary_match_schedules_per_couples_employees(employees_schedule):
    """
    Get a dictionary with the couples employees as a key and the amount match schedules as a value
    ...
    Parameters
    ----------
    employees_schedule : dict
        A dictionary  of schedule per employees

    Return
    ------
    cross_schedules : dict
        A dictionary with match schedules amount per couples
    """
    cross_schedules = {}
    employees=list(employees_schedule.keys())
    for i in range(len(employees)):
        for j in range(i+1,len(employees)):
            couple_employee = employees[i] + "-" + employees[j]
            count = get_count_match_schedules_per_couples(employees_schedule[employees[i]], employees_schedule[employees[j]])
            cross_schedules[couple_employee] = count
    return cross_schedules


def get_count_match_schedules_per_couples(employee1_schedule, employee2_schedule):
    """
    Count the times that match schedules.
    ...
    Parameters
    ----------
    employee1_schedule : dict
        A dictionary of schedule of employee2
    employee2_schedule : dict
        A dictionary of schedule of employee2

    Return
    ------
    count : int
        The match schedules amount
    """
    count = 0
    for day in employee1_schedule.keys():
        validation_employee1=validation_compare_schedules(employee1_schedule.get(day),employee2_schedule.get(day))
        validation_employee2=validation_compare_schedules(employee2_schedule.get(day),employee1_schedule.get(day))
        if validation_employee1 and validation_employee2:
            count += 1
    return count


def validation_compare_schedules(employee1_schedule,employee2_schedule):
    """
    Check that the times match
    ...
    Parameters
    ----------
    employee1_schedule : dict
        A dictionary with the start time and finish time
    employee2_schedule : dict
        A dictionary with the start time and finish time

    Return
    ------
    times : bool
        Check that the times match
    """
    if employee1_schedule is not None and employee2_schedule is not None:
        times=employee2_schedule["Finish Time"]>=employee1_schedule["Start Time"]
        return times


def show_cross_schedules_employees(cross_schedules):
    """
    Show the couples employee with the match schedules amount
    ...
    Parameters
    ----------
    cross_schedules : dict
        A dictionary with the couples employees with the matching schedule amount
    """
    for couples in cross_schedules:
        print(couples + " " + str(cross_schedules[couples]))