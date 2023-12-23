#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 5 ros2 launch mypkg talk_listen1.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep 'Sum: 0'