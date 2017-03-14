#!/bin/bash
python program.py < test.txt > out.txt
if diff out.txt test_sample_output.txt; then 
    echo "OK";
fi
rm out.txt
