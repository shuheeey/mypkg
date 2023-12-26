# SPDX-FileCopyrightText: 2023 Shuhei Yanaighori shuheidaigaku22@gmail.com
# SPDX-License-Identifier: BSB-3-Clausei
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    global node
    if msg.data == 0:
        node.get_logger().info("     S T A R T     ")
        node.get_logger().info("大谷の給料と俺の給料計算")
    time = msg.data // 2
    ootani = time * 6567
    ore = time * 0.3
    if msg.data % 20 == 0 and msg.data !=0:
        node.get_logger().info("%d秒　　　大谷: %d 円   俺: %d 円   まじか" % (time, ootani, ore))
    if msg.data == 120:
        node.get_logger().info("    F I N I S H    ")



def main():
    global node
    rclpy.init()
    node = Node("listener3")
    sub = node.create_subscription(Int16, "countup", cb, 10)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
