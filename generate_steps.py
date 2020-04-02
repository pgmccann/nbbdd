#!/usr/bin/python

"""
Generates skeleton step test functions from Gherkin feature file
"""

import sys
import os.path

if len(sys.argv) < 2:
    raise ValueError('Please specify feature file to parse.')

feature_file_path = sys.argv[1]

if not feature_file_path.endswith('.feature'):
    raise ValueError('Specified file does not appear to be a Gherkin feature file')

if not os.path.isfile(feature_file_path):
    raise ValueError('Specified file does not exist')

feature_dir = feature_file_path.replace('.feature','')
if not os.path.exists(feature_dir):
    os.makedirs(feature_dir)

def writeFailingMethod(tag,name):
    return f"@{tag}('{name}')\ndef step_{name.replace(' ','_')}(context):\n\tfail\n"

with open(feature_file_path,'r') as feat_file:

    scenarios = feat_file.read().split('Scenario')
    for scenario in scenarios[1:]:
        name = ''
        preceding_Given = False
        preceding_Then = False
        given = []
        when = ''
        then = []
        for line in scenario.split('\n'):
            if line.strip().startswith(':'):
                name = line.replace(':','').strip()
            elif line.strip().startswith('Given'):
                preceding_Given = True
                preceding_Then = False
                given.append(line.replace('Given','').strip())
            elif line.strip().startswith('When'):
                when = line.replace('When','').strip()
            elif line.strip().startswith('Then'):
                preceding_Given = False
                preceding_Then = True
                then.append(line.replace('Then','').strip())
            elif line.strip().startswith('And'):
                if preceding_Then:
                    then.append(line.replace('And','').strip())
                elif preceding_Given:
                    given.append(line.replace('And','').strip())
        
        with open(os.path.join(feature_dir,name+'.py'),'w') as steps_file:
            steps_file.write('from behave import given, when, then\n')
            for g in given:
                steps_file.write(writeFailingMethod('given',g))
            steps_file.write(writeFailingMethod('when',when))
            for g in then:
                steps_file.write(writeFailingMethod('given',g))
