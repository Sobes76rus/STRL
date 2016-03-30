#!/usr/bin/env python

import rospy
import imp, os
from node_manager.srv import *


def ready(req):
  return NumResponse(2)


def init():
  rospy.init_node('runner')
  rospy.loginfo(os.getcwd())

  service = rospy.Service('ready', Num, ready)


init()

rospy.set_param('%s/module'%rospy.get_name(), 'scripts/robot1/r.py')
filename = rospy.get_param('%s/module' % rospy.get_name())
rospy.delete_param('%s/module' % rospy.get_name())

(directory, _) = os.path.split(__file__)
filename = os.path.join(directory, '..', filename)

(path, name) = os.path.split(filename)
(name, ext) = os.path.splitext(name)
(file, filename, data) = imp.find_module(name, [path])
module = imp.load_module(name, file, filename, data)

module.run()
