import test_slow_rectangle as tsr
import numpy as np
import time as t

file = open("manual_report.txt", 'w')

for i in range(3):
    start_random_array = t.time()
    array = tsr.random_array(1e5)
    end_random_array = t.time()

    # times['random_array']= float(end_random_array - start_random_array)

    start_snake_loop = t.time()
    filtered_array = tsr.snake_loop(array)
    end_snake_loop = t.time()

    # times['snake_loop']= float(end_snake_loop - start_snake_loop)

    start_snack_loop = t.time()
    filtered_array_snack = tsr.loop(array)
    end_snack_loop = t.time()

    # times['snack_loop']= float(end_snack_loop - start_snack_loop)

    times = {'random_array': float(end_random_array - start_random_array),  \
     'snake_loop': float(end_snake_loop - start_snake_loop), \
     'snack_loop': float(end_snack_loop - start_snack_loop)}

    file.write(f"-------- run number {i} ------- \n \n")
    file.write(f"random array: {times['random_array']} \n")
    file.write(f"snake_loop: {times['snake_loop']} \n ")
    file.write(f"snack loop: {times['snack_loop']} \n")

    #This is taken from stack overflow. Is that plagarism?
    max_val = max(times.values())  # maximum value
    max_key = [k for k, v in times.items() if v == max_val] # getting all keys containing the `maximum`

    file.write(f" {max_key} took the longest time \n")

file.close()
