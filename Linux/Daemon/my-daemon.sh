#/usr/local/sbin/my-daemon.sh

#!/bin/bash
while true
do
echo āIām still in $(date +%Y%m%d-%H%M%S)ā
sleep 10
done

# chmod +x my-daemon.sh