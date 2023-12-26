import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    talker1 = launch_ros.actions.Node(
            package='mypkg',
            executable='talker1',
            )
    listener1 = launch_ros.actions.Node(
            package='mypkg',
            executable='listener1',
            output='screen'
            )
    listener2 = launch_ros.actions.Node(
            package='mypkg',
            executable='listener2',
            output='screen'
            )
    listener3 = launch_ros.actions.Node(
            package='mypkg',
            executable='listener3',
            output='screen'
            )

    return launch.LaunchDescription([talker1, listener1, listener2, listener3])
