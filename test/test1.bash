#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 5 ros2 launch mypkg talk_lislis2.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep -e 'Sum: 0' -e 'Count: 0 sec elapsed'
