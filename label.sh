#!/bin/bash

echo "running ......... "

for f in *.png
	 do
	     python label_image.py --graph=/tmp/output_graph.pb --labels=/tmp/output_labels.txt --input_layer=Placeholder --output_layer=final_result --image=/home/nisrael/example_code/$f

	     python label_image.py --graph=/tmp/output_graph_one.pb --labels=/tmp/output_labels_one.txt --input_layer=Placeholder --output_layer=final_result_one --image=/home/nisrael/example_code/$f

	     echo "$f" | sed -r "s/.+\/(.+)\..+/\1/" >>material_names.dat
	 done

#python label_image.py --graph=/tmp/output_graph_one.pb --labels=/tmp/output_labels_one.txt --input_layer=Placeholder --output_layer=final_result_one --image=/home/nisrael/Research/Topological_Insulators/work/inorganic-bandstructure/gret.jpg
