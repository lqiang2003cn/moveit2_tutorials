add_executable(mtc_tutorial src/mtc_node.cpp)
target_compile_options(mtc_tutorial PUBLIC -g -O0)
ament_target_dependencies(mtc_tutorial ${THIS_PACKAGE_INCLUDE_DEPENDS})

add_executable(minimal_mtc_tutorial src/minimal.cpp)
target_compile_options(minimal_mtc_tutorial PUBLIC -g -O0)
ament_target_dependencies(minimal_mtc_tutorial ${THIS_PACKAGE_INCLUDE_DEPENDS})

add_executable(global_parameter_server src/global_parameter_server_node.cpp)
ament_target_dependencies(global_parameter_server rclcpp)

add_executable(dump_moveit_config src/dump_moveit_config.cpp)
ament_target_dependencies(dump_moveit_config rclcpp)

add_executable(get_global_params_app src/get_global_params.cpp)
ament_target_dependencies(get_global_params_app rclcpp)

install(TARGETS mtc_tutorial minimal_mtc_tutorial
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        RUNTIME DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})
install(DIRECTORY config DESTINATION share/${PROJECT_NAME})
install(TARGETS global_parameter_server DESTINATION lib/${PROJECT_NAME})

