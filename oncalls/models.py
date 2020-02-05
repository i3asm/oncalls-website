import random

from django.db import models


# Create your models here.

class Doctor:
    def __init__(self, name, tasks):
        self.name = name
        self.tasks = tasks

    def most_tasked(self):
        # this is stupid !!!
        self.tasks.sort(reverse=True)


class Day:
    requests_on = []
    requests_off = []
    number_of_tasks = 4
    tasks = []

    def __init__(self, number_tasks):
        self.number_of_tasks = number_tasks
        # self.tasks = [] * 4


def init_days():
    # number_of_days = int(input('how many days do you want? '))
    # number_of_tasks = int(input('how many tasks do you have each days? '))
    # number_of_doctors = int(input('how many doctors do you have? '))
    # doctors = [number_of_doctors]
    number_of_days = 28
    number_of_tasks = 4
    days = [Day] * number_of_days
    # for i in range(number_of_days):
    #     days[i] = Day(number_of_tasks)
    for day in days:
        day = Day(number_of_days)

    return days


def available_doctors(days_index, task_index):
    available = doctors.copy()

    for j in range(days_index, days_index - 2, -1):
        if j >= 0:
            for i in range(task_index + 1):
                print("available: day: ", j, "task: ", i)
                try:
                    available.remove(days[j].tasks[i])
                except ValueError:
                    print("no doctor I guess")
                    # TODO: remove print
                except IndexError:
                    print("no task I guess")

    return available


def algorithm2(days_index=0, task_index=0):
    # if success
    if days_index >= len(days):
        return True
    docs = available_doctors(days_index, task_index)

    try:
        print(days[days_index].tasks[task_index])
    except IndexError:
        days[days_index].tasks.append(Doctor)

    for doc in docs:
        days[days_index].tasks[task_index] = doc
        print("dr.", doc.name, " is assigned")
        if task_index < days[days_index].number_of_tasks:
            if algorithm2(days_index, task_index + 1):
                return days
        else:
            if algorithm2(days_index + 1, 0):
                return days
    return False


# def algorithm(days, days_index=0, task_index=0, doctor_index=0):
#     print(days_index)
#     # if days_index >= len(days):  # only if we filled all the days
#     #     return True
#     # if doctor_index >= len(available_doctors()):
#     #     return False
#
#     day_doctors = available_doctors(days, days_index)
#     for task_index in range(len(days[days_index].tasks)):  # all tasks
#         for doctor_index in range(len(day_doctors)):  # all doctors
#             if day_doctors[doctor_index].most_tasked() != task_index:
#                 #
#                 # we go bellow this line only if we correctly filled the task, means success
#                 assign_doctor(days[days_index].tasks[task_index], day_doctors[doctor_index])
#
#                 # if doctor_index < len(day_doctors):
#                 #     if task_index < len(days[days_index].tasks):
#                 #         algorithm(days, days_index, task_index + 1, doctor_index)


doctors = [
    Doctor(name='nasser', tasks=0),
    Doctor(name='fahad', tasks=0),
    Doctor(name='khalid', tasks=0),
    Doctor(name='ahmed', tasks=0),
    Doctor(name='abood', tasks=0),
    Doctor(name='najd', tasks=0),
    Doctor(name='arwa', tasks=0),
    Doctor(name='saleh', tasks=0),
    Doctor(name='mohammed', tasks=0),
    Doctor(name='john', tasks=0),
    Doctor(name='teller', tasks=0),
    Doctor(name='joe', tasks=0),
    Doctor(name='mofleh', tasks=0),
    Doctor(name='abadi', tasks=0),
    Doctor(name='azoz', tasks=0),
    Doctor(name='naif', tasks=0),
    Doctor(name='hmood', tasks=0),
    Doctor(name='zizo', tasks=0),
    Doctor(name='hmadah', tasks=0),
    Doctor(name='farhan', tasks=0),
]

days = init_days()
print(algorithm2())
