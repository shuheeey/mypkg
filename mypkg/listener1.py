# SPDX-FileCopyrightText: 2023 Shuhei Yanaighori shuheidaigaku22@gmail.com
# SPDX-License-Identifier: BSB-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    global sum
    sum += msg.data
    node.get_logger().info("Sum: %d" % sum)

def main():
    global node
    global sum
    rclpy.init()
    node = Node("listener")
    sum = 0
    sub = node.create_subscription(Int16, "countup", cb, 10)
    rclpy.spin(node)

if __name__ == '__main__':
    main()

