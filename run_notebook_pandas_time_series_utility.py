### IMPORT/DEPENDENCIES

import os
import json
import sys
from os import makedirs
from os.path import join
import datetime 
import subprocess as sp  # jupyter execution

today = datetime.date.today().strftime('%Y-%m-%d')

### SET UP ENV  INPUT

inputdir = f"./plots/"

env = os.environ

#print(f"Date to view set to {today}")
print(f"Date to view set to {today}")

### SET UP ENV OURPUT

outdir = f"./data/plots"
makedirs(outdir, exist_ok=True)

output_html = join(outdir, "frc_plot_output.html")
output_log = join(outdir, "frc_plot_output.html.log")

sp.check_call(f"jupyter nbconvert --execute pandas_time_series_utility.ipynb --to html --output {output_html} --ExecutePreprocessor.timeout=1800 --ExecutePreprocessor.allow_errors=True 1>{output_log} 2>&1 " ,  shell=True, env=env)

print("======= EXECUTION FINISHED =======")
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
