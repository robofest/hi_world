#!/usr/bin/env python
import rospy

if __name__ == '__main__':

    rospy.init_node('hellos_Py_node')
    rate = rospy.Rate(2) # 2 Hz, two times per second
    while not rospy.is_shutdown():
        rospy.loginfo('Hello')
        rate.sleep()
