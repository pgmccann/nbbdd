#!/usr/bin/python

"""
Inserts tests into a Jupyter Notebook

Usage: ./insert_test.py testfile1 testfile2 ... notebook.ipynb

"""

import sys
import json
import os.path

if len(sys.argv) < 3:
    raise ValueError('Please specify tests to insert and notebook to be updated.')

nb_file_path = sys.argv[-1]

if not nb_file_path.endswith('.ipynb'):
    raise ValueError("Last file does not appear to be a Jupyter Notebook")

for file_path in sys.argv[1:]:
    if not os.path.isfile(file_path):
        raise ValueError("Specified file does not exist")

tests = list()
for test_file_path in sys.argv[1:-1]:
    with open(test_file_path) as test_file:
        tests.append(test_file.readlines())

def contains_gherkin(source):
    for line in source:
        if "```gherkin" in line:
            return True
    return False

def create_cell(source_content):
    return { "cell_type": "code", "execution_count": 0, "metadata": {}, "outputs": [], "source": source_content }

with open(nb_file_path) as nb_file:

    data = json.load(nb_file)
    cells = data["cells"]
    updated_cells = list()

    found_gherkin = False
    for cell in cells:
        # Found a gherkin block
        if cell["cell_type"] == "markdown" and contains_gherkin(cell["source"]):
            found_gherkin = True
            updated_cells.append(cell)
        # Found code after a gherkin block - append a test cell after it
        elif cell["cell_type"] == "code" and found_gherkin:
            updated_cells.append(cell)
            updated_cells.append(create_cell(tests.pop(0)))
            found_gherkin = False
        else:
            updated_cells.append(cell)

    data["cells"] = updated_cells

    with open(nb_file_path+".new", "w") as output_file:
        json.dump(data, output_file)


