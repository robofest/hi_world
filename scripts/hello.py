#!/usr/bin/env python

import rospy
from hi_big import * 
if __name__ == '__main__':
    
    rospy.init_node('hello_py_node')
    display_big_hi() 
    rospy.sleep(2) # 5 to 2
    rospy.loginfo('hello_py_node ended after 2 seconds')
