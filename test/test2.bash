#!/bin/bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 65 ros2 run mypkg talker1 > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep -e '送信中' -e '終了'
