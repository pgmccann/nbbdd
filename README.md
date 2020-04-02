[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# BDD for Jupyter Notebooks

This is a Hackday project at the [SSI Collaborations Workshop
2020](https://www.software.ac.uk/cw20).

This is a Python-based command-line tool for parsing
[Gherkin code](https://cucumber.io/docs/gherkin/reference/) in Markdown cells
in a [Jupyter](https://jupyter.org/) Notebook and generating skeleton unit
tests which are then inserted into the Notebook at the appropriate points.

The idea of this project is improve the Jupyter notebooks by adding validations but all
this is not something new, there is already something available as a plug in for Jupyter called [nbval](https://github.com/computationalmodelling/nbval)
which work nice if you want to use the TDD approach which sometime can be a little bit painful when you are in an 
early stage prototyping you research. Since TDD can be a little be to much from the begging we found that it may be helpful
to start with a BDD (Behavior-driven development) approach by writing test cases in a natural language that 
non-programmers can read and also serve as a documentation more or less.

