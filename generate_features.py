#!/usr/bin/python

import sys
import json
import os.path

if len(sys.argv) < 2:
    raise ValueError('Please specify notebook file to parse.')

nb_file_path = sys.argv[1]

if not nb_file_path.endswith('.ipynb'):
    raise ValueError('Specified file does not appear to be a Jupyter Notebook')

if not os.path.isfile(nb_file_path):
    raise ValueError('Specified file does not exist')

with open(nb_file_path) as nb_file:
    data = json.load(nb_file)
    cells = data["cells"]
    for cell in cells:
        cell_type = cell["cell_type"]
        if cell_type == "markdown":
            print(cell["source"])
