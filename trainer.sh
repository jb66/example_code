#!/bin/bash

echo "running ......... "

python retrain_one.py --image_dir ~/anti-crossing

python retrain_two.py --image_dir ~/inorganic-bandstructure

