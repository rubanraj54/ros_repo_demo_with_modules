#!/usr/bin/env python


import rospy
from sub_module_one import *

def initlize_node():

    rospy.init_node('hello_world_node', anonymous=False)
    rospy.loginfo("hello_world_node is now running")
    demo_class1 = DemoClass()
    
    r = rospy.Rate(0.5)
    while not rospy.is_shutdown():
    	demo_class1.do_something()
    	r.sleep()
    
def  main():
    initlize_node()