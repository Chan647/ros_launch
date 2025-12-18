from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	return LaunchDescription([
		Node(
			package = 'my_turtle_pkg',
			executable = 'param_test_node',
			name = 'custom_param_node',
			output = 'screen',
			parameters = [{'my_speed': 10.0},
			{'robot_name': 'SuperBot'} ] ) ])
