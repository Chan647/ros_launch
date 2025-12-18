from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	blue_turtlesim = Node(
		package = 'turtlesim',
		executable = 'turtlesim_node',
		name = 'blue',
		namespace = '/room1',
		output = 'screen')
		
	yellow_turtlesim = Node(
		package = 'turtlesim',
		executable = 'turtlesim_node',
		name = 'yellow',
		namespace = '/room2',
		output = 'screen',
		parameters  = [{'background_r' : 255},
		{'background_g' : 255},
		{'background_b' : 0}] )
		
	new_circle_node = Node(
		package = 'my_turtle_pkg',
		executable = 'circle_node',
		name = 'cicle',
		output = 'screen',
		remappings = [('/cmd_vel', '/room2/turtle2/cmd_vel')] )
		
	return LaunchDescription([
		blue_turtlesim,
		yellow_turtlesim,
		new_circle_node ])
		
