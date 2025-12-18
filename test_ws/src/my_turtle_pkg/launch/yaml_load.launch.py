import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
	config_path = PathJoinSubstitution([
		FindPackageShare('my_turtle_pkg'), 'config', 'params.yaml' ])

	return LaunchDescription([
		Node(
			package = 'my_turtle_pkg',
			executable = 'param_test_node',
			name = 'custom_param_node',
			output = 'screen',
			parameters = [config_path] ) ])
