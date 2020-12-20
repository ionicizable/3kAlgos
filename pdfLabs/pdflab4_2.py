import numpy as np
import time as t
from random import randint
import plotly.express as px


def create_array(n: int):
    array = [randint(1, 10) for i in range(n)]
    return array


def shaker_sort(array: list):
    n = len(array)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False

        for i in range(start, end):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        if not swapped:
            break

        end -= 1

        for i in range(end, start, -1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        start += 1


def evaluate_results(repetitions: int) -> list:
    results = []
    for _ in range(repetitions):
        n = randint(5, 1000)
        start_time = t.time()
        shaker_sort(create_array(n))
        end_time = t.time()
        evaluated_time = end_time - start_time
        results.append((n, evaluated_time))
    return results


def build_chart(raw):
    chart_data = []

    for (n, time) in raw:
        chart_data.append(
            dict(
                size=n,
                evaluation=time
            )
        )
    fig = px.line(chart_data, x="size", y="evaluation")
    fig.show()


build_chart(sorted(evaluate_results(500), key=lambda tup: tup[0]))

