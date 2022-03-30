#!/bin/bash

arr_test=(1 2 3)
remove_element=(3)

arr_test=( "${arr_test[@]/$remove_element}" )

for i in ${arr_test[@]}; do
	echo $i
done


arr_test=("abc" "def" "ghi")
remove_element=("ghi")

arr_test=( "${arr_test[@]/$remove_element}" )

for i in ${arr_test[@]}; do
	echo $i
done

# !!! Be careful when you delete like below !!!
# Use second method in this case

arr_test=("abc" "def" "defghi")
remove_element=("def")

arr_test=( "${arr_test[@]/$remove_element}" )

for i in ${arr_test[@]}; do
	echo $i
done
