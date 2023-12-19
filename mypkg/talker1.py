# SPDX-FileCopyrightText: 2023 Shuhei Yanaighori shuheidaigaku22@gmail.com
# SPDX-License-Identifier: BSB-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import random

class Talker():
    def __init__(self, node):
        self.pub = node.create_publisher(Int16, "countup", 10)
        node.create_timer(2.0, self.cb)

    def cb(self):
        msg = Int16()
        msg.data = random.randint(0, 100)
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = Node("talker")
    talker = Talker(node)
    rclpy.spin(node)

if __name__ == '__main__':
    main()

