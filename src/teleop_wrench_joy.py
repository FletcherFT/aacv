#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Wrench

class teleop_wrench_joy:
    def __init__(self):
        self.wrench_pub = rospy.Publisher('wrench',Wrench,queue_size=1)
        self.joy_sub = rospy.Subscriber('joy',Joy,self.callback)
        
    def callback(self,joy):
        wrench = Wrench()
        wrench.force.x = joy.axes[1]
        wrench.force.y = joy.axes[0]
        wrench.torque.z = joy.axes[2]
        if joy.buttons[0]==1:
            self.wrench_pub.publish(wrench)

def main():
    rospy.init_node('teleop_wrench_joy')
    h = teleop_wrench_joy()
    rospy.spin()

if __name__=='__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
