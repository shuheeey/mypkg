import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    global node
    if msg.data == 0:
        node.get_logger().info("--- Count every 10 sec ---")
    if msg.data % 20 == 0 and msg.data !=0:
        node.get_logger().info("----- %d sec elapsed -----" % (msg.data // 2))

def main():
    global node
    rclpy.init()
    node = Node("listener2")
    sub = node.create_subscription(Int16, "countup", cb, 10)
    rclpy.spin(node)

if __name__ == '__main__':
    main()

