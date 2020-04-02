#!/bin/bash

for nb in *.ipynb; do
    python generate_features.py $nb
    for feature in *.feature; do
        python generate_steps.py $feature
    done
done
