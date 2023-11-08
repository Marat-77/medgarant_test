from .data import busy, WORK_TIME
from datetime import datetime, timedelta
from typing import Iterable


class DoctorTime:
    """
    DoctorTime
    busy_ - time periods when Doctor is busy
    work_time - start and end of  Doctor's work day
    get_free_times - time periods when Doctor is not busy
    """

    def __init__(self, busy_: Iterable[dict[str, str]] | None = None,
                 work_time: tuple[str, str] = WORK_TIME):
        if busy_ is None:
            busy_ = busy
        self._busy = busy_
        self.work_time = work_time

    @property
    def sorted_busy_time(self):
        time_busy = [tuple(
            datetime.strptime(x, '%H:%M') for x in y.values()
        ) for y in self._busy]
        return sorted(time_busy, key=lambda t: t[0])

    def get_free_times(self, minutes: int = 30):
        minutes_ = timedelta(minutes=minutes)
        # start_time, stop_time = self.work_time
        start_time, stop_time = [
            datetime.strptime(wt, '%H:%M') for wt in self.work_time
        ]
        res = []
        for n, t in enumerate(self.sorted_busy_time):
            t_start, t_stop = t
            per_count = (t_start - start_time) // minutes_
            if per_count:
                res.extend(self.__list_periods(start_time,
                                               minutes_,
                                               per_count))
            if n == len(self.sorted_busy_time) - 1:
                per_count = (stop_time - t_stop) // minutes_
                if per_count:
                    res.extend(self.__list_periods(t_stop,
                                                   minutes_,
                                                   per_count))
            start_time = t_stop
        return self.__get_tuple_str_times(res)

    def __str__(self):
        return (f'DoctorBusyTime: '
                f'{self.__get_tuple_str_times(self.sorted_busy_time)}')

    def __repr__(self):
        return str(self)

    @classmethod
    def __get_tuple_str_times(cls, tuples_dt: list[tuple[datetime]]):
        return tuple(
            dict(zip(('start', 'stop'), cls.__str_time(t))) for t in tuples_dt
        )

    @staticmethod
    def __str_time(t_dt: tuple[datetime]) -> tuple[str, ...]:
        return tuple(t.strftime('%H:%M') for t in t_dt)

    @staticmethod
    def __list_periods(start_t, minutes_, counts):
        return [(start_t + c * minutes_,
                 start_t + (c + 1) * minutes_) for c in range(counts)]
