#!/usr/bin/env python

import rospy
from node_manager.srv import *


def compute(req):
  return ReqResponse(max(req.x + req.vx, 100))


rospy.init_node('env')
serv = rospy.Service('compute', Req, compute)
rospy.spin()
