import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray

class BasicNode(Node):
    def __init__(self):
        super().__init__('basic_controls')
        self.publisher = self.create_publisher(Float64MultiArray, '/joint_velocity_controller/commands', qos_profile=10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period_sec=timer_period, callback=self.timer_callback)
        
    def timer_callback(self):
        msg = Float64MultiArray()
        msg.data.append(5.0)
        msg.data.append(0.0)
        
        self.publisher.publish(msg=msg)
        self.get_logger().info("Publishing...") 

def main(args=None):
    rclpy.init(args=args)
    node = BasicNode() 
    rclpy.spin(node=node)
    rclpy.shutdown()
