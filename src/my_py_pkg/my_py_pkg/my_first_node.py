#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("py_test")
        self.counter_ = 0
        self.get_logger().info("Hello world")
        self.create_timer(1.0, self.timer_callback)
    
    def timer_callback(self):
        self.get_logger().info("Hello " + str(self.counter_))
        self.counter_ +=1

def main(args=None): # args ekta parameter jeitar default value hocche None
    rclpy.init(args=args) # jodi argument deya hoy, taile args hobe uporer args
    node = MyNode()
    rclpy.spin(node) # its gonna keep the node alive before shutting down
    rclpy.shutdown()

if __name__ == "__main__":
    main()