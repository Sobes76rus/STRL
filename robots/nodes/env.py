#!/usr/bin/env python

import rospy
from node_manager.srv import *
from node_manager.msg import *


def execute(req):
  r = Properties()
  r.position.x = 10
  return EnvExecuteResponse(r)


rospy.init_node('env')

rospy.Service('execute', EnvExecute, execute)

rospy.spin()
