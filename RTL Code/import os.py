import os
files = [f for f in os.listdir() if f.endswith(".v")]
s = "vlog" 
for i in files:
    s = s +" " + i
os.system(s)