#! /usr/bin/env python3

import rospy

from std_msgs.msg import Float64

import sys, select, termios, tty

msg = ""

"""
Moving Around:
--------------------
        w
    a       s
        d

    Space Bar
    
spacebar: stop the vehicle abruptly
longpress w: increase the forward velocity
longpress d: decrease the velocity and move backward
longpress a: move to the left 
longpress s: move to the right

"""


def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

velocity = 0
turn = 0
max_velocity = 20


if __name__=="__main__":
    try:
        settings = termios.tcgetattr(sys.stdin)
        
        rospy.init_node('my_teleop')

        pub_move = rospy.Publisher('/robot_fourwheel/raj_velocity_controller/command', Float64, queue_size=10) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
        pub_left = rospy.Publisher('/robot_fourwheel/flj_position_controller/command', Float64, queue_size=10)
        pub_right = rospy.Publisher('/robot_fourwheel/frj_position_controller/command', Float64, queue_size=10) # Add your topic for move here '' Eg '/my_robot/longitudinal_controller/command'
        while not rospy.is_shutdown():
            key_pressed = getKey()
            if key_pressed == 'w':
                velocity += 0.25
            elif key_pressed =='s':
                velocity -= 0.25
            elif (key_pressed == 'a' and turn>-0.45):
                turn -= 0.05
            elif (key_pressed == 'd' and turn<0.45):
                turn +=0.05
            elif key_pressed == ' ':
                velocity = 0
                turn = 0
            
            if(velocity>=0):
                velocity = min(velocity,max_velocity)
            else:
                velocity = max(velocity,-(max_velocity))

            print("Velocity: ",velocity, " turn: ",turn,"\n")
            pub_move.publish(-(velocity))
            pub_left.publish(-(turn))
            pub_right.publish(-(turn))

        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)    
    except rospy.ROSInterruptException:
        pass