import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CircleNode(Node):
	def __init__(self):
		super().__init__('waf_circle_node')
		self.declare_parameter('robot_color', 'blue')
		self.declare_parameter('my_speed', 0.15)
		self.declare_parameter('max_velocity')

		self.color = self.get_parameter('robot_color').get_parameter_value().string_value
		self.speed = self.get_parameter('my_speed').get_parameter_value().double_value
		self.max_speed = self.get_parameter('max_velocity').get_parameter_value().double_value

		self.get_logger().info(f'Color : {self.color},  Set speed : {self.speed} m/s, Max velocity : {self.max_speed}')
		self.pub = self.create_publisher(Twist, '/cmd_vel', 10)
		self.timer = self.create_timer(1.0, self.timer_callback)

	def timer_callback(self):
		msg = Twist()
		msg.linear.x = min(self.speed, self.max_speed)
		msg.angular.z = 0.3
		self.pub.publish(msg)


def main(args=None):
	rclpy.init(args=args)
	node = CircleNode()

	try:
		rclpy.spin(node)
	except KeyboardInterrupt:
		pass
	finally:
		node.destroy_node()
		rclpy.shutdown()

if __name__ == '__main__':
	main()
