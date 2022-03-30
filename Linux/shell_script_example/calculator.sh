#!/bin/bash

echo -n "Enter A: "
read A

echo -n "Enter Operator: "
read B

echo -n "Enter B: "
read C

if [ "$B" = "+" ] ; then
	echo "$A + $C = `expr $A + $C`"
elif [ "$B" = "-" ] ; then
	echo "$A - $C = `expr $A - $C`"
elif [ "$B" = "*" ] ; then
	echo "$A * $C = `expr $A \* $C`"
elif [ "$B" = "/" ] ; then
	echo "$A / $C = `expr $A / $C`"
else
	echo "Error"
	exit 1
fi
