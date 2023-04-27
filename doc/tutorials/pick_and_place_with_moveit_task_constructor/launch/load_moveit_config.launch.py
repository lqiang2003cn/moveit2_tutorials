from launch import LaunchDescription
from launch_ros.actions import Node
from moveit_configs_utils import MoveItConfigsBuilder


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("moveit_resources_panda").to_dict()

    # MTC Demo node
    global_param_node = Node(
        package='moveit2_tutorials',
        executable='global_parameter_server',
        name='global_parameter_server',
        parameters=[moveit_config]
    )

    return LaunchDescription([global_param_node])


if __name__ == "__main__":
    generate_launch_description()
