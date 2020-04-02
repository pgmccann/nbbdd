#!/usr/bin/python

"""
Parses Gherkin code from a Jupyter Notebook.

Takes the path to a Jupyter Notebook as an argument

Gherkin code should be marked up in Markdown cells in blocks of the form

```gherkin
Feature: ...
    Scenario: ...
        ...
```
"""

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

    for i, cell in enumerate(cells):
        if cell["cell_type"] == "markdown":
            source = cell["source"]
            gherkin_code = ""
            in_gherkin_block = False

            for line in source:
                if in_gherkin_block and line.startswith("```"):
                    in_gherkin_block = False
                elif in_gherkin_block:
                    gherkin_code += line
                elif line.startswith("```gherkin"):
                    in_gherkin_block = True

            if len(gherkin_code) > 0:
                feature_file = open(nb_file_path+"-"+str(i)+".feature", "w")
                feature_file.write(gherkin_code)
                feature_file.close()
