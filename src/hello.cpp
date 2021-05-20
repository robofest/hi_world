#include <ros/ros.h>
int main (int argc, char **argv)
{
	ros::init(argc, argv, "hello_ros_node");
	ros::NodeHandle nh;
	ROS_INFO("Hello_ros_node started");
	ros::Duration(3.0).sleep(); //seconds
	ROS_INFO("Bye");
}

