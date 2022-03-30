#!/bin/bash

arr_test=("abc" "def" "defghi")
remove_element=("def")

# Get index of array
echo ${!arr_test[@]}

for i in ${!arr_test[@]}; do
	if [ ${arr_test[i]} = ${remove_element} ]; then
		# Use unset
		unset arr_test[i]
	fi
done

for i in ${arr_test[@]}; do
	echo $i
done
