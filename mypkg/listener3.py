import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import time

def cb(msg):
    global node
    if msg.data == 0:
        node.get_logger().info("START")
    if input() == "":
        node.get_logger().info("%d 秒！" % msg.data)
        rclpy.shutdown()



def main():
    global node
    rclpy.init()
    node = Node("listener3")
    sub = node.create_subscription(Int16, "countup", cb, 10)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
