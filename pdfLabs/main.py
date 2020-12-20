import time as t
from random import randint
import plotly.express as px


def create_matrix(n: int):
    matrix = [[randint(-10, 10) for i in range(n)] for i in range(n)]
    return matrix


def count(matrix):
    positive = 0
    negative = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (matrix[i][j] < 0):
                negative += matrix[i][j]
            else:
                positive += matrix[i][j]
    return positive, negative


def evaluate_results(repetitions: int) -> list:
    results = []
    for _ in range(repetitions):
        n = randint(500, 1000)
        start_time = t.time()
        create_matrix(n)
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


print(count(create_matrix(4)))
build_chart(sorted(evaluate_results(10), key=lambda tup: tup[0]))
