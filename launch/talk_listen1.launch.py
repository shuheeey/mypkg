import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    talker = launch_ros.actions.Node(
            package='mypkg',
            executable='talker1',
            )
    listener = launch_ros.actions.Node(
            package='mypkg',
            executable='listener1',
            output='screen'
            )

    return launch.LaunchDescription([talker1, listener1])
