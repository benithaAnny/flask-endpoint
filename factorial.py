import time
import numpy as np
from flask import Flask, request, jsonify
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def time_complexity_visualizer(algorithm, n_min, n_max, n_step):
    times = []
    inputs_sizes = list(range(n_min, n_max + 1, n_step))

    plt.ion()
    fig, ax = plt.subplots()
    ax.set_xlabel('Input Size')
    ax.set_ylabel('Running Time (seconds)')
    ax.set_title('Algorithm Time Complexity Visualizer (live)')
    line, = ax.plot([], [], 'o-')

    for i, n in enumerate(inputs_sizes):
        start_time = time.time()
        algorithm(n)
        end_time = time.time()
        times.append(end_time - start_time)

        line.set_data(inputs_sizes[:i + 1], times)
        ax.relim()
        ax.autoscale_view()
        plt.draw()
        plt.pause(0.01)

    plt.ioff()
    plt.show(block=True)

    filename = f"{algorithm.__name__}.png"
    fig.savefig(filename)

    return filename



def linear_search(n):
    
    for i in range(n * 1000):
        pass


def bubble_sort(n):
    for i in range(n):
        for j in range(n - 1):
            pass


def binary_search(n):
    left = 0
    right = n - 1

    while left <= right:
        middle = (left + right) // 2

        if middle == n - 1:
            return
        elif middle < n - 1:
            left = middle + 1
        else:
            right = middle - 1


def nested_loops(n):
    for i in range(n):
        for j in range(n):
            pass


algorithms = {
    "linear_search": linear_search,
    "bubble_sort": bubble_sort,
    "binary_search": binary_search,
    "nested_loops": nested_loops
}


app = Flask(__name__)


@app.route("/analyze")
def analyze():
    algo = request.args.get("algo", "")
    step = int(request.args.get("step", "1").replace(',', ''))
    n_max = int(request.args.get("n_max", "100").replace(',', ''))
    algo_names = [a.strip().strip("[]'\"") for a in algo.split(',') if a.strip()]

    results = []
    for name in algo_names:
        selected_algorithm = algorithms[name]

        filename = time_complexity_visualizer(
            selected_algorithm,
            0,
            n_max,
            step
        )

        with open(filename, "rb") as image:
            image_base64 = base64.b64encode(image.read()).decode("utf-8")

        results.append({
            "algorithm": name,
            "image_file": filename,
            "image_base64": image_base64
        })

    return jsonify({


        \
        "algorithms": results,
        "step": step,
        "n_max": n_max
    })


if __name__ == "__main__":

    app.run(
        host="localhost",
        port=8000
    )
    #time_complexity_visualizer(linear_search, 0, 100, 10)