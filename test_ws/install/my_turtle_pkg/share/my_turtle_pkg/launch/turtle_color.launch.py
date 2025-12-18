from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	red_turtlesim = Node(
		package = 'turtlesim',
		executable = 'turtlesim_node',
		name = 'red_sim',
		output = 'screen',
		parameters = [{'background_r' : 255},
		{'background_g' : 0},
		{'background_b' : 0}])

	my_circle_node = Node(
		package = 'my_turtle_pkg',
		executable = 'circle_node',
		name = 'my_driver',
		output = 'screen',
		remappings = [('/cmd_vel', '/turtle1/cmd_vel')] )

	return LaunchDescription([
		red_turtlesim,
		my_circle_node])
