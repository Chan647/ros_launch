import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn

class CircleTurtle(Node):
	def __init__(self):
		super().__init__('circle_turtle_node')
		self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
		self.client = self.create_client(Spawn, '/room2/spawn')
		self.spawn_callback()
		self.move_timer = self.create_timer(0.5, self.timer_callback)
		self.get_logger().info('Robot Turning start!')

	def timer_callback(self):
		msg = Twist()
		msg.linear.x = 0.5
		msg.angular.z = 0.5
		self.publisher.publish(msg)
		
	def spawn_callback(self):
		msg = Spawn.Request()
		msg.x = 8.0
		msg.y = 8.0
		msg.theta = 0.0
		future = self.client.call_async(msg)

def main(args=None):
	rclpy.init(args=args)
	node = CircleTurtle()

	try:
		rclpy.spin(node)
	except KeyboardInterrupt:
		pass
	finally:
		node.destroy_node()
		rclpy.shutdown()

if __name__ == '__main__':
	main()
