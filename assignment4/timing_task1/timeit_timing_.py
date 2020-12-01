import test_slow_rectangle as tsr
import timeit as tit
import numpy as np


file = open("timeit_reportit.txt", "w")

for i in range(3):
    start_random_array = tit.default_timer()
    array = tsr.random_array(1e5)
    end_random_array = tit.default_timer()

    # times['random_array']= float(end_random_array - start_random_array)

    start_snake_loop = tit.default_timer()
    filtered_array = tsr.snake_loop(array)
    end_snake_loop = tit.default_timer()

    # times['snake_loop']= float(end_snake_loop - start_snake_loop)

    start_snack_loop = tit.default_timer()
    filtered_array_snack = tsr.loop(array)
    end_snack_loop = tit.default_timer()

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

infile = open("manual_report.txt", 'r')
man_times = []

for line in infile:
    print(line[0])
    if line[0] == '-' or line[0] == '\n' or line[0] == '[' or line[0] ==' \n' or line[0] == ' [' or line[0] == ' ':
        infile.readline()
    else:
        elem = line.split(':')
        print(elem)
        print('\n')
        man_times.append(elem[1])
infile.close()



file.write("comparing manual and timeit \n")
file.write("\n")
file.write(f"random array manual {man_times[0]} random array timeit {times['random_array']} \n")
file.write(f"snake_loop manual {man_times[1]} snake_loop timeit {times['snake_loop']} \n")
file.write(f"snack_loop manual {man_times[2]} snack_loop timeit {times['snack_loop']} \n")

file.close()
