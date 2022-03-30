#!/bin/bash

cnt=0
while (( "${cnt}" < 5 )); do
    echo "${cnt}"
    (( cnt = "${cnt}" + 1 )) # 숫자와 변수의 연산은 (())가 필요합니다.
done
