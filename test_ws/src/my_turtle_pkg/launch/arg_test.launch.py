from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
	speed_arg = DeclareLaunchArgument(
		'target_speed',
		default_value = '2.0',
		description = 'Speed of the robot' )

	speed_config = LaunchConfiguration('target_speed')

	node = Node(
		package = 'my_turtle_pkg',
		executable = 'param_test_node',
		output = 'screen',
		parameters = [{'my_speed' : speed_config}])

	return LaunchDescription([
		speed_arg,
		node ])
