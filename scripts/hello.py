#!/usr/bin/env python

import rospy

if __name__ == '__main__':
    
    rospy.init_node('hello_py_node')
    rospy.loginfo('hello_py_node started')
    rospy.sleep(2) # 5 to 2
    rospy.loginfo('hello_py_node ended after 2 seconds')
