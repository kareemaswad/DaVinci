#!usr/bin/env pyhton
from sensor_msgs.msg import Joy
import rospy
import dvrk
import PyKDL
import math
import numpy
import Tkinter

current_arm = None


def set_psm1_callback():
    global current_arm
    rospy.loginfo("Selected PSM1 for spacenav control")
    current_arm = dvrk.psm('PSM1')

def set_psm2_callback():
    global current_arm
    rospy.loginfo("Selected PSM2 for spacenav control")
    current_arm = dvrk.psm('PSM2')

def set_ecm_callback():
    global current_arm
    rospy.loginfo("Selected ECM for spacenav control")
    current_arm = dvrk.ecm('ECM')



def joy_callback(msg):
    global current_arm
    if current_arm is not None:
        trans = PyKDL.Vector(msg.axes[3], -msg.axes[4], (msg.axes[2]-msg.axes[5])/2) * 0.002
        rot = PyKDL.Rotation.RPY(msg.axes[0]*0.01, msg.axes[1]*0.01, msg.axes[6]*0.01)
        rot = PyKDL.Rotation.RPY(0,0,0)
        d_frame = PyKDL.Frame(rot,trans)
        current_arm.dmove(d_frame, blocking=False)
        if msg.buttons[0] == 1:
            current_arm.close_jaw(blocking=False)
        if msg.buttons[1] == 1:
            current_arm.open_jaw(blocking=False)


if __name__ == '__main__':

    rospy.init_node('dvrk_nav_ds4')
    set_psm1_callback()

    # initialize the UI
    root = Tkinter.Tk()
    root.geometry("200x200")
    frame = Tkinter.Frame(root)
    frame.pack()
    set_psm1_button = Tkinter.Button(frame, text="PSM1", command=set_psm1_callback)
    set_psm1_button.pack()
    set_psm2_button = Tkinter.Button(frame, text="PSM2", command=set_psm2_callback)
    set_psm2_button.pack()
    set_ecm_button = Tkinter.Button(frame, text="ECM", command=set_ecm_callback)
    set_ecm_button.pack()
    
    # start listening on ROS topic
    joy_sub = rospy.Subscriber('/joy/', Joy, joy_callback)
    root.mainloop()
