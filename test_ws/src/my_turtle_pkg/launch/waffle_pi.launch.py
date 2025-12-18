import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
	pkg_gazebo_ros = FindPackageShare(package='turtlebot3_gazebo').find('turtlebot3_gazebo')
	start_gazebo_cmd = IncludeLaunchDescription(
		PythonLaunchDescriptionSource(
			os.path.join(pkg_gazebo_ros, 'launch', 'turtlebot3_world.launch.py')))

	my_circle_node = Node(
		package = 'my_turtle_pkg',
		executable = 'circle_node',
		name = 'waffle_driver',
		output = 'screen' )

	return LaunchDescription([
		start_gazebo_cmd,
		my_circle_node ])
