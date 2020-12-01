Each function implemented above has a lot of plots and prints hardcoded. 
User interface is not included, so you'll have to access each and alter the code

Each implementation also writes a timing.txt with a corresponding name. Python simply
writes, but successive implementations such as numba, numpy etc also read and compare
runtimes to each other. This means that if you run the code, these files will be re-written
with your own machines runtime. ( i call it a feature, not a bug)
