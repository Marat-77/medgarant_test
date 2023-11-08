import pytest

from medgarant_fastapi_test.services import DoctorTime


@pytest.fixture
def get_doctor_time():
    busy = [
        {'start': '09:29',
         'stop': '10:00'},
        {'start': '10:30',
         'stop': '10:50'},
        {'start': '18:40',
         'stop': '18:50'},
        {'start': '14:40',
         'stop': '15:50'},
        {'start': '16:40',
         'stop': '17:20'},
        {'start': '20:05',
         'stop': '20:20'}
    ]
    WORK_TIME = ('09:00', '21:00')
    return DoctorTime(busy, WORK_TIME)


busy_1 = [
    {'start': '09:29',
     'stop': '10:00'},
    {'start': '10:30',
     'stop': '10:50'},
    {'start': '18:40',
     'stop': '18:50'},
    {'start': '14:40',
     'stop': '15:50'},
    {'start': '16:40',
     'stop': '17:20'},
    {'start': '20:05',
     'stop': '20:20'}
]
work_time_1 = ('09:00', '21:00')
expected_tuple_1 = (
    {'start': '10:00', 'stop': '10:30'},
    {'start': '10:50', 'stop': '11:20'},
    {'start': '11:20', 'stop': '11:50'},
    {'start': '11:50', 'stop': '12:20'},
    {'start': '12:20', 'stop': '12:50'},
    {'start': '12:50', 'stop': '13:20'},
    {'start': '13:20', 'stop': '13:50'},
    {'start': '13:50', 'stop': '14:20'},
    {'start': '15:50', 'stop': '16:20'},
    {'start': '17:20', 'stop': '17:50'},
    {'start': '17:50', 'stop': '18:20'},
    {'start': '18:50', 'stop': '19:20'},
    {'start': '19:20', 'stop': '19:50'},
    {'start': '20:20', 'stop': '20:50'}
)
busy_2 = [
    {'start': '10:30',
     'stop': '10:50'},
    {'start': '18:40',
     'stop': '18:50'},
    {'start': '14:40',
     'stop': '15:50'},
    {'start': '16:40',
     'stop': '17:20'},
    {'start': '20:05',
     'stop': '20:20'}
]
work_time_2 = ('09:00', '21:00')
expected_tuple_2 = (
    {'start': '09:00', 'stop': '09:30'},
    {'start': '09:30', 'stop': '10:00'},
    {'start': '10:00', 'stop': '10:30'},
    {'start': '10:50', 'stop': '11:20'},
    {'start': '11:20', 'stop': '11:50'},
    {'start': '11:50', 'stop': '12:20'},
    {'start': '12:20', 'stop': '12:50'},
    {'start': '12:50', 'stop': '13:20'},
    {'start': '13:20', 'stop': '13:50'},
    {'start': '13:50', 'stop': '14:20'},
    {'start': '15:50', 'stop': '16:20'},
    {'start': '17:20', 'stop': '17:50'},
    {'start': '17:50', 'stop': '18:20'},
    {'start': '18:50', 'stop': '19:20'},
    {'start': '19:20', 'stop': '19:50'},
    {'start': '20:20', 'stop': '20:50'}
)
expected_tuple_3 = (
    {'start': '09:00', 'stop': '09:50'},
    {'start': '10:50', 'stop': '11:40'},
    {'start': '11:40', 'stop': '12:30'},
    {'start': '12:30', 'stop': '13:20'},
    {'start': '13:20', 'stop': '14:10'},
    {'start': '15:50', 'stop': '16:40'},
    {'start': '17:20', 'stop': '18:10'},
    {'start': '18:50', 'stop': '19:40'}
)
params = [(busy_1, work_time_1, 30, expected_tuple_1),
          (busy_2, work_time_2, 30, expected_tuple_2),
          (busy_2, work_time_2, 50, expected_tuple_3)]


class TestFreeTimes:
    def test_get_free_times(self, get_doctor_time):
        """
        test for get_free_times with fixture.
        :param get_doctor_time: fixture
        :return: NoReturn
        """
        assert get_doctor_time.get_free_times() == expected_tuple_1

    @pytest.mark.parametrize('busy_, w_time, minutes, expected_tuple', params)
    def test_get_free_times_2(self, busy_, w_time, minutes, expected_tuple):
        """
        test for get_free_times with parametrize.
        :param busy_: busy time periods list
        :param w_time: work time tuple
        :param minutes: int
        :param expected_tuple: expected result
        :return: NoReturn
        """
        doc_time = DoctorTime(busy_, w_time)
        assert doc_time.get_free_times(minutes) == expected_tuple
