# Toy Car using ROS
Project 1 of ENPM 662 - Robot Modelling

## Instructions for teleop:
1) Go to the package folder and copy the packages into catkin_ws/src
2) Go to the catkin_ws folder
3) Run the command "catkin_make clean && catkin_make"
4) Open a new terminal and run the command "roslaunch robot_fourwheel control.launch"
5) To run teleop, run the command "rosrun project1_control my_teleop.py"
6) Keys used for Teleop:
	W: Move forward with increasing velocity on longpress
	A: Move left with increasing turning angle on longpress
	S: Decrease the forward velocity/move backwards with increasing velocity on longpress 
	D: Move right with increasing turning angle on longpress
	Space: Stop the vechicle abruptly
7) Open the rviz and add LaserScan

## Instructions for moving the robot on a straight line or circular path:
1) Open a terminal
2) Run the command "roslaunch robot_fourwheel move_freely.launch"
3) Open a new terminal and run the publisher node
	"rosrun project1_control move_straight.py"
4) Open a new terminal and run the subscriber node
	"rosrun project1_control my_subscriber.py"
To move the robot in circular path, press ctrl+c on the publisher terminal
1) Run the command: "rosrun project1_control move_circular.py"

If any package is missing in your system, please run sudo apt-get install <package name>
