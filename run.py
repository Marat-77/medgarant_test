from medgarant_fastapi_test.services import DoctorTime

if __name__ == '__main__':
    x = DoctorTime()
    # print(x.get_free_times(20))
    print(x.get_free_times())

# busy_2 = [
#     {'start': '10:30',
#      'stop': '10:50'},
#     {'start': '14:40',
#      'stop': '15:50'},
#     {'start': '16:40',
#      'stop': '17:20'},
#     {'start': '18:40',
#      'stop': '18:50'},
#     {'start': '20:05',
#      'stop': '20:20'}
# ]
