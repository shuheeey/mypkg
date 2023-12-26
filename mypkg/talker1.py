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
        global node
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        if self.n == 0:
            #print("送信中")
            node.get_logger().info("送信中")
        self.n += 1
        if self.n == 121:
            #print("終了")
            node.get_logger().info("終了")
            rclpy.shutdown()

def main():
    global node
    rclpy.init()
    node = Node("talker")
    talker = Talker(node)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
