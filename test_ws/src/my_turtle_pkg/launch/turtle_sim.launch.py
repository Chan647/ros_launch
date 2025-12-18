from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	turtlesim_node = Node(
		package = 'turtlesim',
		executable = 'turtlesim_node',
		name = 'sim',
		output = 'screen')

	my_circle_node = Node(
		package = 'my_turtle_pkg',
		executable = 'circle_node',
		name = 'my_driver',
		output = 'screen',
		remappings = [('/cmd_vel', '/turtle1/cmd_vel')] )

	return LaunchDescription([
		turtlesim_node,
		my_circle_node ])
