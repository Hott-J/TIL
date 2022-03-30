#!/bin/bash

arr_test_string=("abc" "def" "ghi" "jkl")

arr_test_string+=("mno")
arr_test_string+=("pqr" "stu")

for i in ${arr_test_string[@]}; do
	echo $i
done

arr_test_string=(1 2 3 4 5)

arr_test_string+=(6)
arr_test_string+=(7 8)

for i in ${arr_test_string[@]}; do
	echo $i
done
