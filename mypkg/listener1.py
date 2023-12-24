# SPDX-FileCopyrightText: 2023 Shuhei Yanaighori shuheidaigaku22@gmail.com
# SPDX-License-Identifier: BSB-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def cb(msg):
    global sum
    sum += msg.data
    node.get_logger().info("Sum: %d" % sum)
    if is_prime(sum):
        node.get_logger().info("%d は素数！" % sum)
    if is_prime(msg.data):
        node.get_logger().info("plus %d は素数！" % msg.data)

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

