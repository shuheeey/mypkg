# SPDX-FileCopyrightText: 2023 Shuhei Yanaighori shuheidaigaku22@gmail.com
# SPDX-License-Identifier: BSB-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker():
    def __init__(self, node):
        self.pub = node.create_publisher(Int16, "countup", 10)
        self.n = 0
        node.create_timer(0.5, self.cb)

    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.n += 1

def main():
    rclpy.init()
    node = Node("talker")
    talker = Talker(node)
    pub1 = node.create_publisher(Int16, "countup", 10)
    pub2 = node.create_publisher(Int16, "countup", 10)
    rclpy.spin(node)

    while rclpy.ok():
        msg = Int16()
        msg.data = self.n
        if self.n % 2 == 0:
            pub1.publish(msg)
        else:
            pub2.publish(msg)
        self.n += 1

if __name__ == '__main__':
    main()
