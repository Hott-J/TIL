#!/bin/bash

# Scan new disk
for y in `lspci | grep 'LSI Logic' | awk '{print $1}'` # y변수에 할당
do
FNAME = `find /sys/devices -name scan | grep $y`
echo '- - -' | sudo tee $FNAME $FANME 2>$1 > /dev/null
done

# Print HDD info
echo
lsblk | grep disk