from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    robot_color = LaunchConfiguration('robot_color')
    my_speed = LaunchConfiguration('my_speed')

    config_path = PathJoinSubstitution([
        FindPackageShare('my_turtle_pkg'),
        'config',
        'waffle_params.yaml'
    ])

    return LaunchDescription([

        DeclareLaunchArgument(
            'robot_color',
            default_value='blue',
            description='Color of the robot'
        ),

        DeclareLaunchArgument(
            'my_speed',
            default_value='0.15',
            description='Linear speed of the robot'
        ),

        Node(
            package='my_turtle_pkg',
            executable='waf_circle_node',
            name='waf_circle_node',
            namespace='Chan',
            output='screen',
            parameters=[
                config_path,
                {
                    'robot_color': robot_color,
                    'my_speed': my_speed
                }
            ]
        )
    ])
