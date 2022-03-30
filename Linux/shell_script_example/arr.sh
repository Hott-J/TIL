#!/bin/bash

arr_test_string=("abc" "def" "ghi" "jkl")
echo "${arr_test_string[2]}"

arr_test_char=('a' 'b' 'c')
echo "${arr_test_char[0]}"

arr_test_num=(1 2 3 100 10000)
echo "${arr_test_num[3]}"

echo "${arr_test_num[@]}"
 
