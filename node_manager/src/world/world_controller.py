import rospy, converter
import world_creator, world_runner
from config import config
import node_manager.srv


worlds = {}

def create(ID): 
  if ID in worlds: destroy(ID)
  rospy.loginfo("create: %s", ID)
  worlds[ID] = launch(ID)
  #world_runner.init(worlds[ID])


def destroy(ID): 
  rospy.loginfo("destroy: %s", ID)
  worlds[ID].stop()
  #world_destroyer.destroy(worlds[ID])
  del worlds[ID]


def run(): 
  for world in worlds: 
    worlds[world].interview()
  #for world in worlds: 
   # world_runner.run(worlds[world])    


def launch(ID): 
  data = loadWorldData(ID)
  return launchByData(data, ID)


def launchByData(data, ID):
  return world_creator.launch(data, ID)


def loadWorldData(ID): 
  return converter.loadObjectFromFile(config['root']+'/node_manager/src/world.json')
