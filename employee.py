#!/usr/bin/env python

import rospy

if __name__ == "__main__":
	rospy.init_node("hello_jarvis")
	print 'hello world'
	rospy.spin()
