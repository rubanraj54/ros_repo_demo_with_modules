cmake_minimum_required(VERSION 2.8.3)
project(hello_world)
find_package(catkin REQUIRED COMPONENTS
  rospy
)

catkin_python_setup()


catkin_package(
  CATKIN_DEPENDS
    rospy
)
