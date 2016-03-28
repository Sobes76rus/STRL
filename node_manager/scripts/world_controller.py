import rospy, converter
import world_creator, world_destroyer
from config import config


worlds = {}

def create(ID): 
  if (ID in worlds): destroy(ID)
  rospy.loginfo("create: %s", ID)
  worlds[ID] = launch(ID)


def destroy(ID): 
  rospy.loginfo("destroy: %s", ID)
  del worlds[ID]


def launch(ID): 
  data = loadWorldData(ID)
  return launchByData(data)


def launchByData(data):
  return world_creator.launch(data)


def loadWorldData(ID): 
  return converter.loadObjectFromFile(config['root']+'/node_manager/scripts/world.json')

