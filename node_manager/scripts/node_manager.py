#!/usr/bin/env python
# -*- coding: utf-8 -*-

from std_msgs.msg import String
import rospy

from config import config
import world_controller


worldIDsToStart = []
worldIDsToStop = []


# ID (String) - Идентификатор мира, который следует промоделировать
def start(ID):
  rospy.loginfo("start: %s", ID.data)
  worldIDsToStart.append(ID.data)


# ID (String) - Идентификатор мира, который следует прервать
def stop(ID):
  rospy.loginfo("stop: %s", ID.data)
  worldIDsToStop.append(ID.data)


def run():
  rospy.init_node(config['config']['name'], anonymous=True)
  rospy.Subscriber(config['config']['start'], String, start)
  rospy.Subscriber(config['config']['stop'], String, stop)

  rate = rospy.Rate(config['config']['rate'])
  while not rospy.is_shutdown():
    for id in worldIDsToStart: world_controller.create(id)
    for id in worldIDsToStop: world_controller.destroy(id)

    del worldIDsToStart[:]
    del worldIDsToStop[:]

    rate.sleep()


if __name__ == '__main__': run()
