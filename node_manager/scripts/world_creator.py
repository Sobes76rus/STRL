from roslaunch.scriptapi import ROSLaunch
from roslaunch.core import Node
from std_msgs.msg import String
import rospy


def launch(world):
  launch = ROSLaunch()

  parseWorld(world)
  for node in nodes: launch.launch(node)
  launch.start()

  return launch


def parseWorld(world):
  for robot in world['robot']
    


