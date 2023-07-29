import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
# from std_msgs.msg import Header
from builtin_interfaces.msg import Duration

class BasicNode(Node):
    def __init__(self):
        super().__init__('basic_controls')
        self.joint_publisher = self.create_publisher(JointTrajectory, '/joint_trajectory_controller/joint_trajectory', qos_profile=10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period_sec=timer_period, callback=self.timer_callback)
        
    def timer_callback(self):
        pt = JointTrajectoryPoint()
        pt.positions = [1.0, 1.0]
        pt.time_from_start = Duration(sec=2)
        
        traj = JointTrajectory()
        traj.joint_names = ['base_rotater_joint', 'rotator_arm_joint']
        traj.points.append(pt)

        self.joint_publisher.publish(msg=traj)
        self.get_logger().info('publishing...')

def main(args=None):
    rclpy.init(args=args)
    node = BasicNode() 
    rclpy.spin(node=node)
    rclpy.shutdown()
