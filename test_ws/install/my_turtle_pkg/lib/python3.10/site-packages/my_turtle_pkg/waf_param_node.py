import rclpy
from rclpy.node import Node

class ParamNode(Node):
    def __init__(self):
        super().__init__('waf_param_node')
        
        self.declare_parameter('robot_color', 'blue')
        self.declare_parameter('my_speed', 0.15)

        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        color = self.get_parameter('robot_color').get_parameter_value().string_value
        speed = self.get_parameter('my_speed').get_parameter_value().double_value
        
        self.get_logger().info(f'Color :[{color}] Set speed: {speed} m/s')

def main(args=None):
    rclpy.init(args=args)
    node = ParamNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
