import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    
    config_path = PathJoinSubstitution([
        FindPackageShare('my_turtle_pkg'),
        'config',
        'wf_params.yaml'
    ])

    color_arg = DeclareLaunchArgument(
        'robot_color',
        default_value='blue',
        description='color of the robot'
    )
    color_config = LaunchConfiguration('robot_color')


    my_circle_node = Node(
        package='my_turtle_pkg',
        executable='ct_node',
        name='my_driver',
        namespace='LEEJUNWOO',
        output='screen',
        parameters=[
            config_path, 
            {'my_color': color_config},
            {'use_sim_time':False}
        ]
    )

    return LaunchDescription([
        color_arg,
        my_circle_node
    ])