import rospy
from config import config
from node_manager.srv import *


configs = {}

def init(world): 
  ID = world['ID']
  configs[ID] = {
    'maxrate': max(map(lambda node: config['robots']['rate'][node.name], world['nodes'])),
    'tick': 0, 'rates': map(lambda node: (node, config['robots']['rate'][node.name]), world['nodes'])
  }

    
def run(world): 
  rospy.loginfo(configs)
  conf = configs[world['ID']]

  if conf['tick'] == conf['maxrate']: 
    conf['tick'], world['tick'] = 0, world['tick'] + 1
  conf['tick'] += 1

  for (node, rate) in conf['rates']:
    run_node(node, rate, conf)

  rospy.loginfo('%s %s' % (world['tick'], conf['tick']))
  

def run_node(node, rate, conf): 
  percent = rate * conf['tick'] / conf['maxrate']
  if rate * (conf['tick'] - 1) / conf['maxrate'] == percent: return

  rospy.loginfo('%s%s', node.namespace, node.name)
  rospy.wait_for_service('%s%s' % (node.namespace, 'ready'))
  ready = rospy.ServiceProxy('%s%s' % (node.namespace, 'ready'), Num)
  rospy.loginfo(ready())
