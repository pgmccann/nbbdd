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
early stage prototyping you research. Since TDD (Test Driven Development) can be a little be to much from the begging we found that it may be helpful
to start with a BDD (Behavior-driven development) approach by writing test cases in a natural language that 
non-programmers can read and also serve as a documentation more or less.

# The basic workflow will be:
1. Create initial notebook
2. Start writing test cases using natural language combined with Gherkin behaviour markup
3. [nbbdd](https://github.com/pgmccann/nbbdd) generates feature and skeleton step files, inserts step code, returns failing test results
4. Populate skeleton tests with real test code
5. Start write software while keeping in mind running also the tests until all pass

Some simple example for step 2 using [behave ](http://behave.github.io/behave.example/tutorials/tutorial02.html)
    
    Feature: Fight or Flight (Natural Language, tutorial02)
    
        In order to increase the ninja survival rate,
        As a ninja commander
        I want my ninjas to decide whether to take on an opponent
        based on their skill levels.

        Scenario: Weaker opponent
            Given the ninja has a third level black-belt
            When attacked by a samurai
            Then the ninja should engage the opponent
    
        Scenario: Stronger opponent
            Given the ninja has a third level black-belt
            When attacked by Chuck Norris
            Then the ninja should run for his life


Steps 4 and 5 can be identified as the TDD part which already requires some coding skills. 