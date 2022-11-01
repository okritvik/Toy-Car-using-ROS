#! /usr/bin/env python3

import rospy
from std_msgs.msg import Float64

def velocity_callback(data):
    rospy.loginfo('Velocity: %f',-(data.data))
   
def rotation_callback(data):
    rospy.loginfo('Rotation: %f',-(data.data))
    
def listener():
    rospy.init_node('My_sub',anonymous=False)

    rospy.Subscriber('/robot_fourwheel/raj_velocity_controller/command',Float64,velocity_callback)
    rospy.Subscriber('/robot_fourwheel/flj_position_controller/command',Float64,rotation_callback)
    rospy.spin()
if __name__ == '__main__':
    listener()