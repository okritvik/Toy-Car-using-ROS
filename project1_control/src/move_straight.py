#! /usr/bin/env python3

import rospy
from std_msgs.msg import Float64

def rotate_circular():
    pub_move = rospy.Publisher('/robot_fourwheel/raj_velocity_controller/command', Float64, queue_size=10) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
    pub_left = rospy.Publisher('/robot_fourwheel/flj_position_controller/command', Float64, queue_size=10)
    pub_right = rospy.Publisher('/robot_fourwheel/frj_position_controller/command', Float64, queue_size=10)
    rospy.init_node('Move_Circular',anonymous=False)
    rate = rospy.Rate(10)
    velocity = 3.0
    rotation = 0.0
    rospy.loginfo('Publishing rotatation')
    pub_left.publish(-(rotation))
    pub_right.publish(-(rotation))
    while not rospy.is_shutdown():
        rospy.loginfo("Publishing velocity %f",velocity)
        pub_move.publish(-(velocity))
        rate.sleep()
if __name__ == '__main__':
    try:
        rotate_circular()
    except rospy.ROSInterruptException:
        pass