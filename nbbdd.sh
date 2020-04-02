#!/bin/bash

for nb in *.ipynb; do
    python generate_features.py $nb
    for feature in *.feature; do
        python generate_steps.py $feature
    done
    index=1
    for dir in $nb*/; do
        for testfile in "$dir/*"; do
            cat ${testfile} >> test$index
        done
        ((index++))
    done
    python insert_tests.py test* $nb
    mv $nb $nb-old
    mv $nb.new $nb
done
