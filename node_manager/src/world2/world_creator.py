from roslaunch.scriptapi import ROSLaunch
from pack.node import Node
from std_msgs.msg import String
import rospy

import converter, os.path
from config import config
from pack.world import World

nodes = []
worldID = 0
robotID = 0


def launch(world, world_id):
  return World(ident=world_id, json=world)

  global nodes, worldID, robotID
  nodes, worldID, robotID = [], world_id, 0

  launch = ROSLaunch()
  launch.start()

  parseWorld(world)
  for node in nodes: 
    launch.launch(node)

  return {
    'nodes': nodes,
    'launch': launch, 
    'ID': world_id, 
    'tick': 0
  }


def parseWorld(world):
  for robot in world['robot']: parseRobot(robot)


def parseRobot(robot):
  robot_type = robot['name']
  robot_xml = findRobot(robot_type)
  launchRobot(robot_xml)
  

def findRobot(robot_name):
  xml = converter.loadObjectFromFile(os.path.join(config['root'], 
    config['robots']['root'], config['robots']['config']))
  for robot in xml['robot']:
    if (robot.get('name') == robot_name): return robot
  
  
def launchRobot(robot):
  global robotID; robotID += 1
  path = os.path.join(config['root'], config['robots']['root'], robot.get('src'))
  for file_name in config['robots']['launch']:
    file_path = os.path.join(robot.get('src'), file_name+'.py')
    if (os.path.isfile(os.path.join(path, file_name+'.py'))):
      launchFile(robot.get('src'), file_path, file_name, robot)


def launchFile(path, filepath, filename, robot):
  rospy.loginfo(filepath + " " + robot)
  node = Node(filename=filepath, name=filename, namespace="%s/%s"%(worldID, robotID),
      params=[('module', filepath)])
  nodes.append(node)
