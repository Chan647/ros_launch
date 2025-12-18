
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CircleTurtle(Node):
    def __init__(self):
        super().__init__('circle_turtle_node')

        self.declare_parameter('linear_speed', 0.1)
        self.declare_parameter('angular_speed', 0.5)
        self.declare_parameter('max_velocity', 0.25)
        self.declare_parameter('sensor_range', 3.5)
        

        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        linear = self.get_parameter('linear_speed').value
        angular = self.get_parameter('angular_speed').value
        max_vel = self.get_parameter('max_velocity').value
        sensor_range = self.get_parameter('sensor_range').value

        linear = max(min(linear, max_vel), -max_vel)

        msg = Twist()
        msg.linear.x = linear
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = angular
        self.publisher_.publish(msg)

        self.get_logger().info(
            f"x={msg.linear.x:.2f}, y={msg.linear.y:.2f}, z={msg.linear.z:.2f}"
        )



    def destroy_node(self):
        stop_msg = Twist()
        self.publisher_.publish(stop_msg)
        self.get_logger().info('Robot stopped')
        super().destroy_node()


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
