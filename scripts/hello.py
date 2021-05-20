#!/usr/bin/env python

import rospy

if __name__ == '__main__':
    
    rospy.init_node('hello_py_node')
    rospy.loginfo('hello_py_node started')
    rospy.sleep(3) # 5 to 3
    rospy.loginfo('hello_py_node ended')
