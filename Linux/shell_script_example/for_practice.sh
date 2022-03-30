#!/bin/bash

arr_num=(1 2 3 4 5 6 7)

# 배열에 @는 모든 원소를 뜻합니다.
for i in ${arr_num[@]}; do
    printf $i
done
echo

for (( i = 0; i < 10; i++)); do
    printf $i
done
echo
