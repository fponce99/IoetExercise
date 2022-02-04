import unittest
import functions
from datetime import datetime


class Test(unittest.TestCase):
    def test_parse_employees_schedules_string_to_dictionary(self):
        self.assertEqual(functions.parse_employees_schedules_string_to_dictionary(
            ["GABRIELA=MO09:00-11:00,TH08:00-12:00", "CARLOS=MO08:15-11:15"]), {"GABRIELA": {
            "MO": {"Start Time": datetime.strptime("09:00", "%H:%M"),
                   "Finish Time": datetime.strptime("11:00", "%H:%M")},
            "TH": {"Start Time": datetime.strptime("08:00", "%H:%M"),
                   "Finish Time": datetime.strptime("12:00", "%H:%M")}}, "CARLOS": {
            "MO": {"Start Time": datetime.strptime("08:15", "%H:%M"),
                   "Finish Time": datetime.strptime("11:15", "%H:%M")}}})

    def test_create_dictionary_of_schedules_day_workingday(self):
        self.assertEqual(functions.create_dictionary_of_schedules_day_workingday("MO09:00-11:00,TH08:00-12:00"),
                         {"MO": {"Start Time": datetime.strptime("09:00", "%H:%M"),
                                 "Finish Time": datetime.strptime("11:00", "%H:%M")}, "TH":
                              {"Start Time": datetime.strptime("08:00", "%H:%M"),
                               "Finish Time": datetime.strptime("12:00", "%H:%M")}
                          })

    def test_create_dictionary_start_finish_time(self):
        self.assertEqual(functions.create_dictionary_start_finish_time("09:00-11:00"),
                         {"Start Time": datetime.strptime("09:00", "%H:%M"),
                                 "Finish Time": datetime.strptime("11:00", "%H:%M")})

    # def test_parse_hour_string_to_datetime(self):
    #    self.assertEqual(functions.parse_hour_string_to_datetime(),)

    def test_create_dictionary_match_schedules_per_couples_employees(self):
        self.assertEqual(functions.create_dictionary_match_schedules_per_couples_employees({"GABRIELA": {
            "MO": {"Start Time": datetime.strptime("09:00", "%H:%M"),
                   "Finish Time": datetime.strptime("11:00", "%H:%M")},
            "TH": {"Start Time": datetime.strptime("08:00", "%H:%M"),
                   "Finish Time": datetime.strptime("12:00", "%H:%M")}}, "CARLOS": {
            "MO": {"Start Time": datetime.strptime("08:15", "%H:%M"),
                   "Finish Time": datetime.strptime("11:15", "%H:%M")}}}),{"GABRIELA-CARLOS":1})

    def test_get_count_match_schedules_per_couples(self):
        self.assertEqual(functions.get_count_match_schedules_per_couples({
            "MO": {"Start Time": datetime.strptime("09:00", "%H:%M"),
                   "Finish Time": datetime.strptime("11:00", "%H:%M")},
            "TH": {"Start Time": datetime.strptime("08:00", "%H:%M"),
                   "Finish Time": datetime.strptime("12:00", "%H:%M")}},{
            "MO": {"Start Time": datetime.strptime("08:15", "%H:%M"),
                   "Finish Time": datetime.strptime("11:15", "%H:%M")}}),1)

    def test_validation_compare_schedules(self):
        self.assertTrue(functions.validation_compare_schedules({"Start Time": datetime.strptime("09:00", "%H:%M"),
                   "Finish Time": datetime.strptime("11:00", "%H:%M")},{"Start Time": datetime.strptime("08:15", "%H:%M"),
                   "Finish Time": datetime.strptime("11:15", "%H:%M")}))

    if __name__ == "__main__":
        unittest.main()
