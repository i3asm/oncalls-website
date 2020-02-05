import random

from django.db import models


# Create your models here.

class Doctor:
    def __init__(self, name, tasks):
        self.name = name
        self.tasks = tasks

    def most_tasked(self):
        self.tasks.sort(reverse=True)


class Day:
    requests_on = []
    requests_off = []
    tasks = []

    def __init__(self, number_tasks):
        self.tasks = [Doctor] * 4


def init_days():
    # number_of_days = int(input('how many days do you want? '))
    # number_of_tasks = int(input('how many tasks do you have each days? '))
    number_of_days = 28
    number_of_tasks = 4
    days = [Day] * number_of_days
    for i in range(number_of_days):
        days[i] = Day(number_of_tasks)

    return days


# number_of_doctors = int(input('how many doctors do you have? '))
# doctors = [number_of_doctors]

def available_doctors(days, days_index):
    available = doctors.copy()

    for task in days[days_index].tasks:
        if task:
            available.remove(task)

    if days[days_index - 1 >= 0]:
        for task in days[days_index - 1].tasks:
            available.remove(task)
        if days[days_index - 2 >= 0]:
            for task in days[days_index - 2].tasks:
                available.remove(task)
    return available


def pre_algorithm():
    days = init_days()
    # print(days[0])
    days = algorithm(days)


def algorithm(days, days_index=0, task_index=0, doctor_index=0):
    if days_index >= len(days):  # only if we filled all the days
        return days
    # print(days)
    if task_index >= len(days[days_index].tasks):
        days_index += 1

    day_doctors = available_doctors(days, days_index)
    for task_index in range(len(days[days_index].tasks)):  # all tasks
        for doctor_index in range(len(day_doctors)):  # all doctors
            if day_doctors[doctor_index].most_tasked() != task_index:
                # we go bellow this line only if we correctly filled the task, means success
                days[days_index].tasks[task_index] = day_doctors[doctor_index]
                algorithm(days, days_index, task_index, doctor_index)


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

pre_algorithm()
