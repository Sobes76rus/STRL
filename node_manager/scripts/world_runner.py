#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from config import config


def run():
  pub = rospy.Publisher(config['config']['start'], String, queue_size=10);
  rospy.init_node('talker', anonymous=True)
  rate = rospy.Rate(1)
  while not rospy.is_shutdown():
    rospy.loginfo('1')
    pub.publish('1')
    rate.sleep()
    

run()
