#!/bin/bash

# Numeric if statement
test_num=5

if [ "${test_num}" -eq 2 ]; then
	echo "number is 2"
elif [ "${test_num}" -eq 3 ]; then
	echo "number is 3"
else
	echo "number is not 2 or 3"
fi

# Numeric if statement
test_num=5

if (( ${test_num} > 3 )); then
	echo "number is greater than 3"
else
	echo "number is not greater than 3"
fi

# String if statement
test_str="test"

if [ "${test_str}" = "test" ]; then
	echo "test_str is test"
else
	echo "test_str is not test"
fi
