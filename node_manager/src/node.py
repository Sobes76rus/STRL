import roslaunch.core, rospy
from config import config

class Node(roslaunch.core.Node):

  def __init__(self, obj, name, node_type):

    self.obj = obj

    roslaunch.core.Node.__init__(self,
        package=config['robots']['root'],
        node_type=config['robots'][node_type],
        name=name, namespace=obj.namespace)


  def get_env(self): return '%s%s' % (self.namespace, self.name)

  def get_param(self, key):
    key = '%s/%s' % (self.get_env(), key)
    return rospy.get_param(key)

  def set_param(self, key, value): 
    key = '%s/%s' % (self.get_env(), key)
    rospy.set_param(key, value)

  def get_srv(self, name, srv):
    name = '%s/%s' % (self.namespace, name)
    rospy.wait_for_service(name)
    return rospy.ServiceProxy(name, srv)
    
