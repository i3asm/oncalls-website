from enum import Enum
import random

from django.db import models


# Create your models here.

class Doctor:

    def __init__(self, name):
        self.name = name
        self.stat = [0] * 7
        self.tasks = [0]


class Day:

    def __init__(self, number_of_tasks):
        self.requests_on = []
        self.requests_off = []
        self.tasks = []
        for i in range(number_of_tasks):
            self.tasks.append(Doctor('__empty__'))


class Week(Enum):
    sun = 0
    mon = 1
    tue = 2
    wed = 3
    thu = 4
    fri = 5
    sat = 6


class Month:

    def __init__(self, number_of_days, number_of_tasks, beginning):
        self.days = []
        self.beginning = beginning
        for i in range(beginning, beginning + number_of_days):
            # print("[Month] init day ", i - beginning)
            self.days.append(Day(number_of_tasks))

    def get_day(self, day_index):
        return Week((day_index + self.beginning) % 7).name

    def get_index(self, day_index):
        return (day_index + self.beginning) % 7

    # this is supposed to get the index of a day object
    # def get_inde(self, day):
    #     print(self.days.index(day))
    #


doctors = [
    Doctor('nasser'),
    Doctor('fahad'),
    Doctor('khalid'),
    Doctor('ahmed'),
    Doctor('abood'),
    Doctor('najd'),
    Doctor('arwa'),
    Doctor('saleh'),
    Doctor('mohammed'),
    Doctor('john'),
    Doctor('teller'),
    Doctor('joe'),
    Doctor('mofleh'),
    Doctor('abadi'),
    Doctor('azoz'),
    Doctor('naif'),
    Doctor('hmood'),
    Doctor('zizo'),
    Doctor('hmadah'),
    Doctor('farhan'),
]


# update the stats of each doctor until certain day and task
def update_stat(day, task):
    for doctor in doctors:
        doctor.stat = [0] * 7
    for i in range(day):
        for j in range(len(month.days[i].tasks)):
            # print("[update] stat day:", i, "task:", j)
            try:
                if i == day and j == task:
                    return
                month.days[i].tasks[j].stat[month.get_index(i)] += 1
            except ValueError:
                print("maybe no doctors in there")


# # update stats for all doctors in every day.
# def update_stat():
#     for doctor in doctors:
#         doctor.stat = [0] * 7
#     for day in month.days:
#         for task in day.tasks:
#             print(month.get_index(month.days.index(day)))


def available_doctors(day, task):
    available = doctors.copy()
    print('[available] day: ', day, ', task: ', task)
    update_stat(day, task)
    available = _con_days(day, task, available)
    available = _con_weekends(day, task, available)

    return available


def _con_days(day, task, available):
    for i in range(max(day - 2, 0), day + 1):
        for j in range(len(month.days[i].tasks)):
            try:
                available.remove(month.days[i].tasks[j])
                if i == day and j == task:
                    return available
            except ValueError:
                if i == day and j == task:
                    return available
                print("maybe no doctors in there")
    return available


def _con_weekends(day, task, available):
    for i in range(day):
        pass

    return available


def print_month():
    for index, day in enumerate(month.days):
        # print("day:", index, "doctors: ", end='')
        for task in day.tasks:
            try:
                print(task.name, ',', sep='', end=' ')
            except AttributeError:
                print('attribute error')
                return
        print()


def pre_algorithm_v3():
    algorithm_v3(0, 0)
    # print(month.days)
    # return month


def algorithm_v3(days_index, tasks_index):
    if days_index == len(month.days):
        return True

    available = available_doctors(days_index, tasks_index)

    for i in range(len(available)):
        month.days[days_index].tasks[tasks_index] = available.pop(random.randint(0, len(available) - 1))
        # print(month.days[days_index].tasks[tasks_index].name)
        # print_month()

        # move the index
        if tasks_index < (len(month.days[days_index].tasks) - 1):
            if algorithm_v3(days_index, tasks_index + 1):
                return True
        else:
            if algorithm_v3(days_index + 1, 0):
                return True
        print("[algorithm] this doctor doesn't fit", days_index, 'task: ', tasks_index)

    # if we tried all doctors and failed
    print("\033[93m[algorithm] [critical] all doctors didn't work!, day: ", days_index, "task: ", tasks_index,
          "\033[0m")
    return False


# number_of_days = 4
# number_of_tasks = 4

month = Month(number_of_days=28, number_of_tasks=4, beginning=2)
pre_algorithm_v3()
print_month()
update_stat(len(month.days), len(month.days[len(month.days) - 1].tasks))
# for doctor in doctors:
#     print(doctor.name, ": ", doctor.stat)
