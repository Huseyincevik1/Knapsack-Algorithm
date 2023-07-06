from __future__ import division, print_function
from collections import namedtuple
import time
import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd

Item = namedtuple("Item", ['index', 'value', 'weight'])
files = ["ks_4_0", "ks_19_0", "ks_200_0","ks_10000_0"]

def solve(input_filename):
    data_iter = (line.split() for line in open(input_filename))
    data = [(int(v), int(w)) for i, (v, w) in enumerate(data_iter)]
    item_count, capacity = data[0]

    items = [Item(i, v, w) for i, (v, w) in enumerate(data[1:])]
    items.sort(key=lambda x: x.value / x.weight, reverse=True)

    dp = [0] * (capacity + 1)

    for i in range(item_count):
        for j in range(capacity, items[i].weight - 1, -1):
            dp[j] = max(dp[j], dp[j - items[i].weight] + items[i].value)

    total_value = dp[capacity]
    print(total_value)

    included_items = [0] * item_count
    remaining_capacity = capacity
    for i in range(item_count - 1, -1, -1):
        if remaining_capacity >= items[i].weight and dp[remaining_capacity] == dp[remaining_capacity - items[i].weight] + items[i].value:
            included_items[items[i].index] = 1
            remaining_capacity -= items[i].weight

    print(*included_items)
    return total_value

#kodun ne kadar sürede çalıştığını gösteren kod parçası.
def solve_time(file_name):
    start = time.perf_counter()
    last_input = solve(file_name)
    stop = time.perf_counter()
   # print(stop - start) süreyi yazdırır
    return (stop - start)

if __name__ == "__main__":
    ks_4 = solve_time("ks_4_0.txt")
    ks_19 = solve_time("ks_19_0.txt")
    ks_200 = solve_time("ks_200_0.txt")
    ks_10000 = solve_time("ks_10000_0.txt")

    data = {'Boyut': ['4', '19', '200', '10000'],
            'Zaman': [ks_4, ks_19, ks_200, ks_10000]}

    df = pd.DataFrame(data)
   # print(df) boyut zaman tablosu çıktısını verir.
    sns.lineplot(x='Boyut', y='Zaman', data=df)
    plt.grid()
    plt.show()
