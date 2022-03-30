#/usr/local/sbin/my-daemon.sh

#!/bin/bash
while true
do
echo “I’m still in $(date +%Y%m%d-%H%M%S)”
sleep 10
done

# chmod +x my-daemon.sh