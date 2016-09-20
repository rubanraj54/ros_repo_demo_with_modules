#!/usr/bin/env python
'''
This script demostrates the way of filling 
ros std_msgs by giving few examples.
'''
import rospy


class DemoClass():
    def __init__(self):
        rospy.loginfo("constructor called")
        self.do_something()

    def do_something(self):
        rospy.loginfo("Do something called")
