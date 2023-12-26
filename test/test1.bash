#!/bin/bash
# SPDX-FileCopyrightText: 2023 Shuhei Yanaighori shuheidaigaku22@gmail.com
# SPDX-License-Identifier: BSB-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 15 ros2 launch mypkg talk_lis3.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log |
grep -e 'Sum: 0' -e '     S T A R T     ' -e '--- Count every 10 sec ---' -e '送信中' -e '大谷の給料と俺の給料計算' -e 'Sum: 3 は素数！' -e '↑素数足された( + 2 )↑' -e '----- 10 sec elapsed -----' -e '10秒　　　大谷: 65670 円   俺: 3 円   まじか' 
