#!/bin/bash

echo "running ......... "

for f in *.png
do
	convert "$f"
done

