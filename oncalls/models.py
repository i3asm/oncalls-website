import random

from django.db import models


# Create your models here.

class Doctor:

    def __init__(self, name):
        self.name = name


class Day:
    requests_on = []
    requests_off = []
    tasks = []

    def __init__(self, number_tasks):
        self.tasks = []


class Month:
    days = []

    def __init__(self, number_of_days, number_of_tasks):
        days = [Day] * number_of_days
        for i in range(number_of_days):
            print("daaaay")
            days.append(Day(number_of_tasks))
        # days = [Day(number_tasks=number_of_tasks)] * number_of_days


# def init_days():
#     # number_of_days = int(input('how many days do you want? '))
#     # number_of_tasks = int(input('how many tasks do you have each days? '))
#     # number_of_doctors = int(input('how many doctors do you have? '))
#     # doctors = [number_of_doctors]
#     number_of_days = 3
#     number_of_tasks = 4
#     days = [Day] * number_of_days
#     for day in days:
#         day = Day(number_of_tasks)
#
#     return days


# def available_doctorsV2(days_index, task_index):
#     available = doctors.copy()
#     # print(days)
#     print(days[0].tasks)
#     print(days[1].tasks)
#
#     for j in range(days_index, days_index - 2, -1):
#         if j >= 0:
#             for i in range(task_index + 1):
#                 print("available: day: ", j, "task: ", i)
#                 try:
#                     available.remove(days[j].tasks[i])
#                 except ValueError:
#                     print("no doctor I guess")
#                     # TODO: remove print
#                 except IndexError:
#                     print("no task I guess")
#     # print(available)
#
#     return available


# def algorithmV2(days_index=0, task_index=0):
#     # if success
#     if days_index >= len(days):
#         return True
#     docs = available_doctorsV2(days_index, task_index)
#
#     try:
#         (days[days_index].tasks[task_index])
#     except IndexError:
#         days[days_index].tasks.append(Doctor)
#
#     for doc in docs:
#         days[days_index].tasks[task_index] = doc
#         print("dr.", doc.name, " is assigned")
#         if task_index < days[days_index].number_of_tasks:
#             if algorithmV2(days_index, task_index + 1):
#                 return days
#         else:
#             if algorithmV2(days_index + 1, 0):
#                 return days
#     return False


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


def available_doctors(day, task):
    available = doctors.copy()
    for i in range(len(month.days)):
        for j in range(len(month.days[i].tasks)):
            try:
                available.remove(month.days[i].tasks[j])
            except ValueError:
                print("maybe no doctors in there")
            if i == day and j == task:
                return available
    return available


def print_month():
    for index, day in enumerate(month.days):
        print("day: ", index, "doctors: ", end='')
        for task in day.tasks:
            print(" ", task.name, end='')
        print()


def pre_algorithm_v3():
    algorithm_v3(0, 0)
    print(month.days)
    return month


def algorithm_v3(days_index, tasks_index):
    if days_index == len(month.days):
        return True

    available = available_doctors(days_index, tasks_index)

    for doc in available:
        month.days[days_index].tasks[tasks_index] = doc

        if tasks_index < len(month.days[days_index].tasks):
            if algorithm_v3(days_index, tasks_index + 1):
                return True
        else:
            if algorithm_v3(days_index + 1, 0):
                return True
    return False


number_of_days = 3
number_of_tasks = 4
month = Month(number_of_days, number_of_tasks)
print(month.days)
pre_algorithm_v3()
print_month()
# days = init_days()
# algorithmV2()
