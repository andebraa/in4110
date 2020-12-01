import test_slow_rectangle as tsr
import numpy as np
import cProfile
import pstats
import io

pr = cProfile.Profile()
pr.enable()

random_array = tsr.random_array(1E5)

pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr, stream = s).sort_stats('tottime')
ps.print_stats()

print("random_array")
with open('cProfile_report.txt', 'w+') as f:
    f.write("random array \n")
    f.write(s.getvalue())


pr.enable()

filtered_array = tsr.snake_loop(random_array)

pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr, stream = s).sort_stats('tottime')
ps.print_stats()

print("snake_loop")
with open('cProfile_report.txt', 'a') as f:
    f.write("\n snake_loop \n")
    f.write(s.getvalue())


pr.enable()

filtered_array_snack = tsr.loop(random_array)

pr.disable()
s = io.StringIO()
ps = pstats.Stats(pr, stream = s).sort_stats('tottime')
ps.print_stats()

print("snack loop")
with open('cProfile_report.txt', 'a') as f:
    f.write("\n snack loop \n")
    f.write(s.getvalue())
