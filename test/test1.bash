#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 5 ros2 launch mypkg talk_lis3.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep -e 'Sum: 0' -e '     S T A R T     ' -e '--- Count every 10 sec ---' -e '送信中'
