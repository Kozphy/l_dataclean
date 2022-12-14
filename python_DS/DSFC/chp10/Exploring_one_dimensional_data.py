from typing import List, Dict
from collections import Counter
import math

import matplotlib.pyplot as plt
import random
from chp6.scratch.probability import inverse_normal_cdf


def bucketize(point: float, bucket_size: float) -> float:
    """
    Floor the point to the next lower multiple of bucket_size
    """
    return bucket_size * math.floor(point / bucket_size)


def make_histogram(points: List[float], bucket_size: float) -> Dict[float, int]:
    """
    Buckets the points and counts how many in each bucket
    """
    return Counter(bucketize(point, bucket_size) for point in points)


def plot_histogram(points: List[float], bucket_size: float, title: str = ""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)


def Exec_1d_data():
    print("start Exec 1d data")
    random.seed(0)

    uniform = [200 * random.random() - 100 for _ in range(10000)]

    normal = [57 * inverse_normal_cdf(random.random()) for _ in range(10000)]

    plot_histogram(uniform, 10, "Uniform Histogram")

    # plot_histogram(normal, 10, "Normal Histogram")
    plt.show()


# Exec_1d_data()
